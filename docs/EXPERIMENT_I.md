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

**True sites** were found by `scripts/make_i_sites.py`, independently of the guide's claims: the declaration in the interface and the implementation, every call through a variable declared with the interface type (including a mistyped variable name, `lamguageService`), and unqualified or `this.` calls inside the implementation. The guide's own call claims miss 3 of these sites (two `findOne` calls in `ProductFacadeImpl` and `ProductFacadeV2Impl`, one `toLocale` call in `LanguageUtils`); this is left as it is, because a real generated guide has gaps and a test that hid them would flatter it. The sites list was checked by hand against the source and the grader was tested on the exact answer (passes), no change (fails), a missed site (fails) and a blanket rename (fails, 52 other lines wrong).

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

*(none yet)*
