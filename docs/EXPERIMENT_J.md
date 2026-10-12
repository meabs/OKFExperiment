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

## Six tasks

**Three changes**, graded exactly by `hidden/j/verify_j.py`: each file must equal the original with the expected edit at exactly the true sites. Comments, imports and whitespace are ignored. Sites were found from the parse tree (`hidden/j/make_j_sites.py`), not from the guide or graph, and the grader was tested on the exact answer, no change, and a blanket edit.

| Task | Change | Why it is hard |
| --- | --- | --- |
| j1 | Rename `PaymentModule.authorizeAndCapture` | Interface in `sm-core-modules`, seven implementations and one caller in `sm-core`. 9 sites in 9 files. |
| j2 | Add a trailing parameter `boolean refresh` to one overload of `calculateProductPrice`, `(Product, List<ProductAttribute>)`, and pass `false` at its calls | Six overloads and about 20 calls; calls split over several lines; commented-out calls that must not matter. 6 sites in 5 files. |
| j3 | Remove the unused parameter `origin` from `ShippingQuoteModule.getShippingQuotes` | Interface and six implementations in another module; one call that passes it under a different name. 8 sites in 8 files. |

**Three questions**, graded by expected class names (all must appear) and, for j4, by names that must not appear:

| Task | Question | Answer |
| --- | --- | --- |
| j4 | Which classes really call the two-argument attributes overload of `calculateProductPrice`? | `ShoppingCartServiceImpl`, `ShoppingCartFacadeImpl`, `ProductVariationApi`. Callers of other overloads and commented-out calls are wrong. |
| j5 | Which class holds the only direct call to `getShippingQuotes`, which facade calls it, which endpoint calls the facade? | `ShippingServiceImpl`, `OrderFacadeImpl`, `ShippingQuoteEndpoint` |
| j6 | Which classes lie on the path from the `POST /api/v1/cart/{code}/checkout` handler to `authorizeAndCapture`? | `OrderApi`, `OrderFacadeImpl`, `OrderServiceImpl`, `PaymentServiceImpl` |

The answers were traced by hand with text search and reading, and then checked, not taken from the graph.

8 repetitions × 6 tasks × 2 arms = **96 runs**, `gpt-5.6-luna`, medium reasoning. **Isolation** on (AgentTrialRig `isolate`): the agent cannot read other repositories, results or hidden tests. The model needs the network, so it stays on and use is counted.

## Measures

1. **Passed**, per part: changes (48 runs) and questions (48 runs), never pooled.
2. **Tokens per run**, relative to `plain`.
3. **Adoption** in the `optimised` arm: runs that opened `AGENTS.md`, the guide, a skill file, and ran `kg`. If the setup is not used, the comparison says little.
4. Network use and isolation breaks.

## What I expect, fixed in advance

- **Adoption:** the agent opens `AGENTS.md` in most runs and runs `kg` in most; it reads a skill file in fewer than half.
- **Questions (j4 to j6):** `optimised` uses fewer tokens, because `kg` answers caller and path questions in one call (an earlier trial on a small library found about a third of the tokens). Pass rates are level, because the model finds these by text search too, though j4 should favour `optimised`: the graph merges overloads, so the agent still has to confirm in the source.
- **Changes (j1 to j3):** no reliable difference in pass rate, as in experiment I. `optimised` is no cheaper, and probably dearer, as in A, C and I. j2 is where the skills could matter (the overload trap); I expect at most a modest gain.
- **Overall:** a mixed picture, with a cost saving on structure questions and no saving on edits. A clear gain in correct changes would be a new result, and I will say so.

## How it will be judged

Fisher's exact test on pass counts, `plain` against `optimised`, per part and per task. **Only p < 0.05 is called a difference.** With 24 runs per arm in each part, gaps under about 35 points cannot be separated. Cost is the ratio of mean tokens with its interval; a difference under 15%, or an interval that includes 1.00, is not called. Reported as it comes out.

## Not tested

Which of the four ingredients matters; other repositories, languages or models; changes that need more than mechanical edits; whether the graph and guide stay fresh as the code moves; any effect on a repository the agent cannot read.

## Deviations

*(none yet)*
