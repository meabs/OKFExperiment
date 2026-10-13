# Experiment J: a repository set up for agents against one left as it is

> **Terms.** A *guide* is a generated OKF bundle: a folder of markdown files. A *graph* is the code graph made by `kgen sync` in [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree), queried with its `kg` command. This page was written **before any counted run** and fixes what will be measured and how it will be judged. Changes after the first counted run are listed under *Deviations*.

## The question

Earlier experiments tested single ingredients: a guide (A to I), a contract or a note (H). A team that sets a repository up for agents would use several together, with instructions. So: **does a repository set up the recommended way give an agent a better result, or a lower cost, than the same repository left as it is?**

## The repository

The Shopizer backend used in D to I (1,173 Java files, several modules), readable, in the agent's workspace. It is large and full of repeated names: one method can have six overloads (`calculateProductPrice`), one interface can have seven implementations in another module (`PaymentModule`), and many methods share a name (`saveOrUpdate`, `getShippingQuote`).

## Two arms

| Arm | The agent gets |
| --- | --- |
| `plain` | The repository and nothing added: no `AGENTS.md`, no guide, no graph, no skills. |
| `optimised` | The same repository plus (a) the guide in `okf/` (the `recommended` preset, with file-and-line references, links, calls and an index); (b) the graph and its `kg` tool in `.agent-knowledge/`, inside the workspace so isolation does not block it; (c) three **operating skills** in `.agents/skills/` that say how to work here, not about the technology (`navigate-the-repo`, `change-the-code`, `check-your-work`, in `fixtures/operating-skills/`); (d) an `AGENTS.md` that points to all three, lists the `kg` commands and carries the sentence "read the source to confirm before you rely on it". |

The optimised arm bundles four things, so a result cannot say which one mattered. That is deliberate: this tests the whole setup. Splitting it is a later step if there is anything to split.

Both arms can still read the agent's own global skills under the home folder (`--ignore-user-config` does not stop that), so the `plain` arm is not fully bare.

## Seven tasks

**Four changes**, graded exactly by `hidden/j/verify_j.py`: each file must equal the original with the expected edit at exactly the true sites. Comments, imports and whitespace are ignored. Sites were found from the parse tree (`hidden/j/make_j_sites.py`), not from the guide or graph, and the grader was tested on the exact answer, no change, and a blanket edit.

| Task | Change | Why it is hard |
| --- | --- | --- |
| j1 | Rename `PaymentModule.authorizeAndCapture` | Interface in `sm-core-modules`, seven implementations and one caller in `sm-core`. 9 sites in 9 files. |
| j2 | Add a trailing parameter `boolean refresh` to one overload of `calculateProductPrice`, `(Product, List<ProductAttribute>)`, and pass `false` at its calls | Six overloads and about 20 calls; calls split over several lines; commented-out calls that must not matter. 6 sites in 5 files. |
| j3 | Remove the unused parameter `origin` from `ShippingQuoteModule.getShippingQuotes` | Interface and six implementations in another module; one call that passes it under a different name. 8 sites in 8 files. |
| j7 | Rename the generic base-service method `SalesManagerEntityService.delete(E)` | The hard one. The base interface, its base class, 25 overrides and redeclarations, 49 calls through typed service variables and 26 calls to the inherited method from inside implementations (`super.`, `this.`, unqualified): **101 sites in 57 files**, in two modules and in tests. 17 other one-argument `delete` calls, on repositories, a storage manager and unrelated facades, must not change. |

**Three questions**, graded by expected class names (all must appear) and, for j4, by names that must not appear:

| Task | Question | Answer |
| --- | --- | --- |
| j4 | Which classes really call the two-argument attributes overload of `calculateProductPrice`? | `ShoppingCartServiceImpl`, `ShoppingCartFacadeImpl`, `ProductVariationApi`. Callers of other overloads and commented-out calls are wrong. |
| j5 | Which class holds the only direct call to `getShippingQuotes`, which facade calls it, which endpoint calls the facade? | `ShippingServiceImpl`, `OrderFacadeImpl`, `ShippingQuoteEndpoint` |
| j6 | Which classes lie on the path from the `POST /api/v1/cart/{code}/checkout` handler to `authorizeAndCapture`? | `OrderApi`, `OrderFacadeImpl`, `OrderServiceImpl`, `PaymentServiceImpl` |

The answers were traced by hand with text search and reading, and then checked, not taken from the graph.

8 repetitions × 7 tasks × 2 arms = **112 runs**, `gpt-5.6-luna`, medium reasoning. **Isolation** on (AgentTrialRig `isolate`): the agent cannot read other repositories, results or hidden tests. The model needs the network, so it stays on and use is counted.

## Measures

1. **Passed**, per part: changes (64 runs) and questions (48 runs), never pooled.
2. **Tokens per run**, relative to `plain`.
3. **Adoption** in the `optimised` arm: runs that opened `AGENTS.md`, the guide, a skill file, and ran `kg`. If the setup is not used, the comparison says little.
4. Network use and isolation breaks.

## What I expect, fixed in advance

- **Adoption:** the agent opens `AGENTS.md` in most runs and runs `kg` in most; it reads a skill file in fewer than half.
- **Questions (j4 to j6):** `optimised` uses fewer tokens, because `kg` answers caller and path questions in one call (an earlier trial on a small library found about a third of the tokens). Pass rates are level, because the model finds these by text search too, though j4 should favour `optimised`: the graph merges overloads, so the agent still has to confirm in the source.
- **Changes (j1 to j3):** no reliable difference in pass rate, as in experiment I. `optimised` is no cheaper, and probably dearer, as in A, C and I. j2 is where the skills could matter (the overload trap); I expect at most a modest gain.
- **j7:** the only task I expect `plain` to find hard (fewer than half of runs exactly right: a missed override, a missed `super.delete` call or a renamed repository call). The graph resolves each receiver by its declared type and may not map a call on `ProductService` to the base method `SalesManagerEntityService.delete`, so I expect `optimised` to help only partly; the skills' list-then-check method may matter more. I am not confident of the direction or the size.
- **Overall:** a mixed picture, with a cost saving on structure questions and no saving on edits. A clear gain in correct changes would be a new result, and I will say so.

## How it will be judged

Fisher's exact test on pass counts, `plain` against `optimised`, per part and per task. **Only p < 0.05 is called a difference.** With 32 runs per arm in the changes and 24 in the questions, gaps under about 30 to 35 points cannot be separated. Cost is the ratio of mean tokens with its interval; a difference under 15%, or an interval that includes 1.00, is not called. Reported as it comes out.

## Not tested

Which of the four ingredients matters; other repositories, languages or models; changes that need more than mechanical edits; whether the graph and guide stay fresh as the code moves; any effect on a repository the agent cannot read.

## Deviations

1. **A harder task was added after a pilot.** A pilot (one run per arm on j2 and j5, one `plain` run on each of j1, j3, j4 and j6; six runs, discarded, not counted) showed `plain` passing five of the six original tasks, so the test risked a ceiling. Task j7 was designed and its grader tested (exact answer passes; no change and a blanket replace fail) before any counted run. The pilot also showed the agent opening the skills, running `kg` and reading the guide in the `optimised` arm. Codex loads `AGENTS.md` itself, so adoption of `AGENTS.md` cannot be seen in the commands and is not measured.
2. **The j7 ground truth missed four string literals, and was corrected after the runs.** Every one of the 16 j7 runs (8 per arm) changed one file that the grader did not list: `PublishProductAspect.java`, which holds four AspectJ pointcut strings of the form `execution(* ...ProductService.delete(Product))`. They name the method as text, so a rename that leaves them alone breaks the aspect without a compile error. The agents were right and the site finder, which looked only at method declarations and calls, was wrong. The finder now also finds string literals that name a service's `delete` method (105 sites in 58 files); the corrected grader passes the exact answer and fails no change. The runs' work folders were not kept, so the 16 j7 runs were re-scored from the diffs the grader had saved (`scripts/regrade_j.py`): a run passes if its other 57 files were exactly right and its edit to the aspect changed exactly the four lines, each by renaming `.delete(` to `.removeEntity(`. The three tasks j1, j2, j3 and the questions are unaffected: no string or other non-code references to their methods exist (checked by parsing every string literal in the repository). The first grader's figure (0 of 16) is kept in the raw report.

## Results

Raw report: [`results/J-optimised-repo.md`](../results/J-optimised-repo.md); per-run verdicts and diffs in [`results/J-grades/`](../results/J-grades/).

| Part | `plain` | `optimised` | Tokens per run |
| --- | --- | --- | --- |
| Changes (j1, j2, j3, j7), of 32 | 28 | 29 (p = 1.0) | 407k and 526k (1.29 times) |
| Questions (j4, j5, j6), of 24 | 16 | 19 (p = 0.52) | 150k and 234k (1.56 times) |
| All 56 runs per arm | | | 297k and 401k: **1.48 times, interval 1.38 to 1.60, reliably more** |

| Task | `plain` | `optimised` |
| --- | --- | --- |
| j1 rename payment method (9 sites) | 8 / 8 | 8 / 8 |
| j2 add parameter to one overload (6 sites) | 8 / 8 | 7 / 8 |
| j3 remove unused parameter (8 sites) | 8 / 8 | 8 / 8 |
| **j7 rename generic `delete` (105 sites in 58 files)** | **4 / 8** (p = 0.61) | **6 / 8** |
| j4 callers of one overload | 1 / 8 | 3 / 8 (p = 0.57) |
| j5 shipping call chain | 7 / 8 | 8 / 8 |
| j6 checkout call path | 8 / 8 | 8 / 8 |

- **No reliable difference in correctness anywhere**, per part or per task. The optimised arm was ahead by 4 runs of 56 (48 against 44), which is within chance, and reliably dearer overall.
- **The setup was used.** In all 56 optimised runs the agent ran `kg` and opened the guide; it read `navigate-the-repo` in 55, `change-the-code` in 32 and `check-your-work` in 34. (Whether `AGENTS.md` was read cannot be seen, because Codex loads it itself.)
- **The cost came with it.** The optimised runs took more turns (8.8 against 5.9) and more tokens, because the agent read the instructions, the guide and the graph output and then still searched and read the source.
- **The hidden dependency was found by everyone.** All 16 j7 agents updated the four pointcut strings without being told.
- **j4's failures are one mistake in both arms:** 11 of 16 answers listed `ProductFacadeImpl` or `ProductFacadeV2Impl`, whose calls sit inside a block comment, although the question said to count only real code.
- **Isolation held:** 10 runs (4 plain, 6 optimised) had a command refused by the sandbox; no network use was detected.

| Prediction | Outcome |
| --- | --- |
| The agent opens `AGENTS.md` and runs `kg` in most runs; reads a skill in fewer than half | **Partly wrong.** `kg` in all runs, as predicted; but `navigate-the-repo` was read in 55 of 56 and the other two skills in over half. `AGENTS.md` not measurable. |
| Questions: `optimised` uses fewer tokens | **Not seen.** 1.56 times more. |
| Questions: pass rates level (j4 favours `optimised`) | **Held** (16 against 19 of 24; j4 1 against 3 of 8, not reliable). |
| Changes: no reliable difference; `optimised` no cheaper | **Held**, and dearer (1.29 times). |
| j2: at most a modest gain from the skills | **Not seen** (8 against 7 of 8). |
| j7: `plain` finds it hard; `optimised` helps only partly | **Half right.** `plain` passed 4 of 8 (not fewer than half); `optimised` passed 6 of 8, not reliable. |

What this adds: a repository set up the recommended way, with a guide, a graph, operating skills and a configured `AGENTS.md`, did not give a reliably better result than the same repository left as it was, on mechanical changes and structure questions in a large readable codebase, and it cost about 48% more tokens. The one hard task, a 58-file rename with 105 sites, favoured the setup by two runs of eight, which this size of experiment cannot tell from chance. The plain arm was already strong: it passed 44 of 56 runs. One repository, one model, one task type (mechanical edits and structure questions); the optimised arm bundles four ingredients, so this does not say which would help alone. An earlier trial of the graph on a small library found about a third of the tokens on caller questions (AgentGraphWorkTree's own evaluation); that did not carry over to this repository, where the agent used the graph and still searched.

