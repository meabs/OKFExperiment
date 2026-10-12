# Experiment I: does a guide improve an engineering outcome, not only answers about structure?

> **Terms.** A *guide* is a generated OKF bundle: a folder of markdown files. This page was written **before any counted run** and fixes what will be measured and how it will be judged. Changes after the first counted run are listed at the end under *Deviations*.

## The question

Tests D to H show that a guide answers questions about what calls what (H2: 21 of 24 against 8 for a contract). They do not show that this helps an agent do the work. Tests A and C found no gain where the agent can read the code, but they used a small library (Click, about 25 modules). Untested: **a large readable codebase, where a text search over-matches.** So: when an agent must change code in a large repository it can read, does having a guide of that repository improve the outcome or lower the cost?

## Design

The Shopizer backend (the renamed copy used in D to H, 1,173 Java files), readable, in the agent's workspace. Four tasks, each a **rename** of one method of a service interface, with all its callers:

| Task | Method | True sites | Hits of a plain text search for `.name(` |
| --- | --- | --- | --- |
| i1 | `ProductService.findOne` | 15 in 9 files | 33 calls in 24 files |
| i2 | `ShoppingCartService.saveOrUpdate` | 12 in 7 files | 71 calls in 32 files |
| i3 | `MerchantConfigurationService.saveOrUpdate` | 12 in 7 files | 71 calls in 32 files |
| i4 | `LanguageService.toLocale` | 10 in 9 files | 9 calls in 8 files |

The other `findOne` and `saveOrUpdate` methods (repositories, other services, a private method in the product service) must keep their names. A rename can be graded exactly without a Java compiler (there is none on the test machine): the right answer is the original code with the name changed at the true sites and nowhere else.

**True sites** were found by `scripts/make_i_sites.py`, independently of the guide's claims: the declaration in the interface and the implementation, every call through a variable declared with the interface type (including a mistyped variable name, `lamguageService`), and unqualified or `this.` calls inside the implementation. As written before the runs, the guide's own call claims were thought to miss 3 of these sites (two `findOne` calls in `ProductFacadeImpl` and `ProductFacadeV2Impl`, one `toLocale` call in `LanguageUtils`). **That was partly wrong:** the two `findOne` lines are inside a block comment, so they are dead code and the guide rightly leaves them out. Only the `LanguageUtils` call (i4) is a real call the guide lacks. See Deviations, item 3. The sites list was checked by hand against the source and the grader was tested on the exact answer (passes), no change (fails), a missed site (fails) and a blanket rename (fails, 52 other lines wrong).

Two arms:

| Arm | The agent gets |
| --- | --- |
| `plain` | The repository, and a line saying where the backend source is. |
| `guide` | The same, plus the generated guide (`kgen okf`, `recommended` preset) in `okf/`, and the pointer sentence "read the source to confirm before you rely on it". |

8 repetitions × 4 tasks × 2 arms = **64 runs**. Same model and settings as before (`gpt-5.6-luna`, medium reasoning).

**Isolation.** New in this experiment: AgentTrialRig's `isolate` option runs each agent under a macOS sandbox profile that denies reading and writing the other repositories, the results, the scratch folders and the hidden tests. Only the run's own workspace is readable. (The agent's model calls need the network, so the network stays on; commands using it are counted by `scripts/net_check.py`.) `scripts/leak_check.py` is run as well.

## Measures

1. **Passed**: every true site renamed and nothing else changed (exact).
2. **Sites renamed** and **other lines wrongly changed**, per run, to tell a miss from a spoilt edit.
3. **Tokens per run**, as a cost proxy, relative to `plain`.
4. Network use and isolation breaks, counted.

## What I expect, fixed in advance

- The model reads code well; with a text search and a type check it will find most sites. **I expect no reliable difference in the pass rate** between the two arms (about half of runs pass in each), as in tests A and C.
- On i1 and i4, where the guide's call claims are incomplete, the `guide` arm will miss the sites the guide lacks more often than `plain` does, if the agent trusts the guide.
- Cost: the `guide` arm will use more tokens, as in tests A and C (+7 to +30%), unless the guide saves enough searching in the large repository to cancel it. This is the part of the question where I am least sure.
- A result in which the guide raises the pass rate or lowers the cost would be the first such result for a repository the agent can read, and I will report it with the caveat that it is one repository and one task type.

## How it will be judged

- Fisher's exact test on pass counts, `plain` against `guide`, overall and per task. **Only p < 0.05 is called a difference.** With 32 runs per arm, a difference smaller than about 30 points cannot be separated.
- Cost is the ratio of mean tokens, with the spread. A difference smaller than 15% is not called.
- Reported as it comes out, including a null result. One task type (renames), one repository, one model.

## Not tested

Other task types (adding a parameter, changing behaviour); a repository the agent cannot read (tests D to H); other models; a guide kept out of date (tests B and D).

## Deviations

1. **Pilot and grader fix 1 (comments).** A two-run pilot (task i4, discarded) showed both agents also renaming a commented-out call, which the exact grader counted as wrong. Before the counted runs the grader was changed to accept either choice for comment lines.
2. **Grader fix 2 (trailing blank line), and a full rerun.** The first 64 counted runs were graded with an exact whole-file comparison. Task i1 failed in all 16 runs. Rerunning one i1 run with its work folder kept showed why: the agent had renamed all 15 sites correctly, but its editing tool had also removed the blank line at the end of `ProductService.java`, and the grader counted that as a wrong edit. The work folders of the first batch had been deleted, so it could not be regraded. The grader was changed to ignore trailing whitespace and blank lines at the end of a file, retested on the exact answer (passes), no change (fails), one missed site (fails) and a blanket rename (fails), and **all 64 runs were repeated**, this time with the grader saving each run's verdict and its Java diff (a first attempt that kept every work folder filled the disk and was abandoned after 14 runs, which were discarded). The first batch is kept in the results as `I-first-batch-strict-grader.md` and the second is the one reported; both are shown in the README. This change was made after seeing the first batch's results, for a defect in the measurement, not in the direction of either arm.
3. **Two required sites were dead code (found after the rerun).** The site finder for i1 treated two commented-out calls (`ProductFacadeImpl` line 235 and `ProductFacadeV2Impl` line 245, inside a block comment) as required, because it skipped only lines that start with a comment marker. The grader therefore required agents to edit dead code. Every i1 run that passed had edited those lines (a blanket text replace does so). `scripts/regrade_i.py` re-scores the saved per-run diffs with those two sites optional: **no run changes its result** (plain 22 and guide 24 of 32 either way). The experiment J site finder uses the parse tree and cannot make this mistake.

## Results

Raw reports: [`results/I-rename-in-large-repo.md`](../results/I-rename-in-large-repo.md) (reported), [`results/I-first-batch-strict-grader.md`](../results/I-first-batch-strict-grader.md) (discarded, see Deviations), per-run verdicts and diffs in [`results/I-grades/`](../results/I-grades/).

| Task | `plain` | `guide` |
| --- | --- | --- |
| i1 `findOne` (15 sites) | 8 / 8 | 7 / 8 |
| i2 cart `saveOrUpdate` (12 sites) | 2 / 8 | 3 / 8 |
| i3 configuration `saveOrUpdate` (12 sites) | 5 / 8 | 6 / 8 |
| i4 `toLocale` (10 sites) | 7 / 8 | 8 / 8 |
| **Passed** | **22 of 32** | **24 of 32** |
| Tokens per run | 267k | 318k (1.22 times, interval 1.07 to 1.37: reliably more) |

- **Pass rate: no reliable difference** (22 against 24 of 32, p = 0.78). The first, discarded batch, graded too strictly, gave 15 against 14 of 32; that grader defect hit both arms alike.
- **Where runs failed:** almost entirely on the two `saveOrUpdate` renames, whose name has about 70 hits in the codebase. Across i2 and i3, `plain` missed 15 sites and edited 13 lines of the wrong class; `guide` missed 10 and edited 8. Both arms made the same two kinds of mistake (a missed call, or an edit to a caller of a different class with the same method name); the difference in counts between the arms was not tested for reliability.
- **Cost: the guide was reliably dearer**, by about 22%, as in tests A and C.
- **Isolation held.** In 11 of 64 runs (6 `plain`, 5 `guide`) a command was refused by the sandbox; they were `find ..` and similar commands looking for another copy of the repository. No network use was detected.

| Prediction | Outcome |
| --- | --- |
| No reliable difference in pass rate | **Held** (22 against 24 of 32). |
| The guide misses the sites its call claims lack (written for i1 and i4; only i4 has a real one) more often than `plain` | **Not seen.** `guide` missed no site on i4, and 1 on i1 (a real site, not one of the dead-code lines). |
| The guide costs more | **Held**, 1.22 times, reliably. |

What this adds: in a large repository the agent can read, with a task designed so that a text search over-matches, a generated guide did not improve the result and cost about a fifth more. It does not say anything about other task types, other repositories or other models. It also does not test the case this experiment was meant to approach in the end, a change whose correct form depends on internal structure the agent cannot otherwise see.
