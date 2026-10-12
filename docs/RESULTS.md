# Results

> **Terms.** A *bundle* is OKF's name for a generated guide to a codebase: a folder of markdown files, one per module or package, listing what it contains and where each fact came from. The [main README](../README.md) calls it a *guide*.

Codex `gpt-5.6-luna` (medium reasoning), AgentTrialRig 0.6.1. Bundles come from `kgen okf` (deterministic, no language model; [how to get it](../README.md#reproducing)). Raw reports are in [`../results/`](../results/). Read anything under 8 runs per arm as provisional; intervals are 95%.

## A. Which bundle shape? (Click, 5 questions and 3 change tasks)

**Accuracy was at the ceiling in every arm** (questions 14 or 15 of 15, change tasks 8 or 9 of 9 verified, with or without a bundle). So the question is cost.

| arm (what it contains) | v1: pointer told the agent to confirm in source (24 runs/arm) | v2: no such sentence (24 runs/arm) |
| --- | --- | --- |
| none | 1.00 | 1.00 |
| minimal (types and function names only; no citations, links, call edges or index) | 1.42 (1.25-1.59) dearer | 1.26 (1.14-1.39) dearer |
| no call edges | 1.21 (1.08-1.37) dearer | 1.10 (0.97-1.25) no clear difference |
| default (citations, links, cross-module calls, routing index) | 1.30 (1.14-1.47) dearer | 1.07 (0.99-1.16) no clear difference |
| all calls / one concept per package / no index | 1.30 / 1.26 / 1.22, all dearer | not rerun |
| code graph only (`kg`) | 1.15 (1.03-1.28) dearer | 1.14 (0.99-1.32) no clear difference |

Relative cost = tokens divided by the no-bundle mean for the same question (1.00 = equal).

- No bundle beat having none on tokens. The best (default, v2) was level on questions (0.99) and about 21% dearer on change tasks.
- The thinnest bundle was always the dearest: without citations and links the agent still has to search, so the bundle is extra reading.
- Per-package concepts, a missing index and full call edges did not beat the default (v1 only).
- **The "read the source to confirm" sentence moved the cost**: the default arm fell from 1.30 to 1.07 when it was removed. The two runs were not simultaneous, so treat the size as indicative.
- The graph is dearer here because most of these are one-hop lookups, which matches earlier results (it pays off on multi-level callers).

## B. Confidence flags (Click after three planted refactors; the bundle is from before them)

Drifts: a renamed function (`_resolve_context` to `_resolve_completion_context`), a new intermediate base class (`PositionalParameter`) and a call moved behind a helper (`_ordered_params`). Two further questions were unchanged (controls). 12 drift answers per arm (3 questions x 4 runs). "Followed stale" = the answer gives the old fact and not the new one.

**v1 (the pointer told the agent to confirm in source): 1 of 84 drift answers followed a stale claim across all seven bundle arms.** The flags could not be compared, because every arm already had a verification instruction.

**v2 (that sentence removed, and an efficiency prompt: "use the repository knowledge ... avoid unnecessary file reads"):**

| arm | followed stale (of 12) | correct on the 2 control questions | relative cost |
| --- | --- | --- | --- |
| no bundle | 0 | 7/8 | 1.00 |
| bundle, no flags | **8** | 7/8 | 1.42 |
| + OKF-native fields (`generated`, `sources`, `status`) and a trust-tier sentence | 9 | 8/8 | 1.25 |
| + per-line `[high]/[medium]` tags | 8 | 7/8 | 1.31 |
| + banner telling the reader to check the source | 10 | 6/8 | 1.28 |
| + tags, banner and `verified` stamps | 8 | 8/8 | 1.32 |
| + `stale_after` only on concepts whose source changed | 5 | 8/8 | 1.29 |
| + `stale_after` on every concept | 6 | 8/8 | 1.34 |

- An unflagged bundle is harmful under efficiency pressure: 8/12 against 0/12 with no bundle (Fisher exact, two-sided p about 0.001).
- Tags, banners and OKF-native provenance did not help (pooled 26/36 against 8/12, p = 0.77). The banner arm was the worst.
- `stale_after` helped a little: 11/24 against 43/60 for the arms without it (one-sided, post-hoc pooled, p = 0.025). Targeted against no flags was 5/12 against 8/12 (p = 0.21). Suggestive, not settled.
- The renamed function was followed most often: agents answered from the bundle without searching for the new name.

**B3, the clean test of the sentence** (same bundle as "no flags", same efficiency prompt, one sentence added to the pointer: "read the source to confirm before you rely on it"): **0 of 12 followed stale, against 8 of 12 without it** (p about 0.001), at the same cost (77k against 79k tokens). Nothing else changed.

## C. Cross-repo (synthetic: `ledger-lib` and `invoice-service`, 3 change tasks, 12 runs per arm)

| arm | verified | relative cost |
| --- | --- | --- |
| library installed only (nothing said) | 12/12 | 1.00 |
| library source location given | 12/12 | 1.28 (1.11-1.47) dearer |
| library bundle vendored under `okf/references/` | 12/12 | 1.25 (1.09-1.40) dearer |
| the same with tags, banner and `verified` stamps | 12/12 | 1.25 (1.11-1.39) dearer |
| library bundle from an older version (stale) | 12/12 | 1.05 (0.96-1.12) |
| stale, with tags, banner and targeted `stale_after` | 12/12 | 1.10 (0.96-1.25) |

- Everything passed, and no run hit a stale-API error in any arm (0 of 12 each). The library was installed and readable, so the agent could always inspect it, and the other repo's bundle added cost without adding accuracy.
- This does **not** show that cross-repo bundles never help. A dependency the agent cannot read (a private service, a binary) is untested, and the pair is synthetic.

## D. A complex repository as a dependency the agent cannot read

The working repository is the real [Shopizer React storefront](https://github.com/shopizer-ecommerce/shopizer-shop-reactjs). It calls a backend, [Shopizer](https://github.com/shopizer-ecommerce/shopizer) (1,173 Java files, 325 routes), that is **not available** to the agent. Eight questions each trace one storefront call to the backend: the controller method, the request class, and a field or path variable. Examples: the cart POST in `cartActions.js`, the login request in `LoginRegister.js`, the search request, the config request.

**The backend's question-relevant identifiers were renamed** (`scripts/privatize.py`), so the answers cannot come from memory of a famous public repository. A first attempt without this let the agent answer from memory (it found `AuthenticateCustomerApi` unaided); that was caught in a smoke test before any trial run.

### D1. Backend current (96 runs: 8 questions x 4 arms x 3 runs)

| Arm | Correct | Tokens per run (95% CI) | Cost vs no backend |
| --- | --- | --- | --- |
| No backend | **1 / 24** | 785k (513k to 1118k) | 1.00 |
| Backend source checked out (read-only) | 24 / 24 | 181k (155k to 212k) | 0.43 (0.25 to 0.65) |
| Backend bundle, with the confirm sentence | 24 / 24 | 189k (161k to 219k) | 0.41 (0.26 to 0.61) |
| Backend bundle, without it | 24 / 24 | 169k (138k to 208k) | 0.34 (0.24 to 0.45) |

- A bundle gave the same accuracy as the full source at the same cost, and a fraction of what searching blind cost. The "no backend" cost is the cost of failing.
- The intervals on the ratios are wide (the no-backend runs vary from 55k to 3.0M tokens, median 722k); the accuracy gap is not in doubt.
- **Contamination.** Codex can read the whole disk. 3 of 24 no-backend runs searched it. One found another run's bundle in its work folder and answered correctly (the 1 of 24), so the no-backend arm is, if anything, flattered. Two found copies of the backend source and still answered wrongly. No bundle-arm run reached outside its own workspace (`scripts/leak_check.py`); the source arm was given the path.

### D2. Backend refactored after the bundle was generated (128 runs: 8 questions x 4 arms x 4 runs)

Four renames on the backend (a handler method, a request-class field, a path variable, a request class): four questions have a new answer, four are controls. The bundle is from before the refactor. Efficiency prompt ("use the repository knowledge ... avoid unnecessary file reads"), as in B2.

| Arm | Gave the **old** fact | Gave the new fact | Controls correct | Tokens per run |
| --- | --- | --- | --- | --- |
| Backend source (refactored) | 0 / 16 | 16 / 16 | 16 / 16 | 148k |
| Stale bundle | **14 / 16** | 0 / 16 | 16 / 16 | 157k |
| Stale bundle + the confirm sentence | **16 / 16** | 0 / 16 | 16 / 16 | 158k |
| Stale bundle + the sentence + `stale_after` on the 7 changed concepts | **16 / 16** | 0 / 16 | 16 / 16 | 156k |

- Every drift answer from a bundle arm was wrong, and none of the 46 stale answers carried a caveat.
- The confirm sentence could not help: there was no backend source to confirm against.
- `stale_after` did not help either. The seven marked concepts included the routes concept and the packages the questions touched, the pointer explained the field, and still not one of 32 answers in that arm mentioned staleness.
- Unchanged facts stayed correct (controls 16/16 in every arm), so the harm is exactly the drifted facts.
- No run in D2 reached outside its own workspace.

## Spec findings from building it

- Bundle-relative links (`/modules/x.md`) point at the bundle root, so a bundle copied under `references/<name>/` has every internal link broken unless they are rewritten. The emitter rewrites them; the spec does not say how a vendored bundle should be linked.
- A deterministic generator can vouch for structure (names, signatures, call edges, citations), not behaviour. The spec's `verified` field cannot express that, and most concepts contain medium-confidence call edges, so `verified` stamps rarely applied.

## Limits

One model; one repository for A and B (Click, about 25 modules); a synthetic pair for C; 3 to 4 runs per cell; graders and drift written by the experimenters; a constant overhead from the author's global agent skills in every run; v1 and v2 not run simultaneously. The pooled B comparisons were chosen after seeing the data. The bundles the agents read were generated before a later fix to a few optional frontmatter fields (`resource`, `sources[].id`, `last_modified`; see [CONFORMANCE.md](CONFORMANCE.md)); concept bodies were unchanged and nothing was rerun. A language-model arm was excluded by design. D uses the complex repository only as a dependency: whether a bundle saves cost *inside* a large repository the agent can search was not tested. D's backend is real code with the question-relevant identifiers renamed and the planted refactors applied as text edits that were not compiled; it is still recognisably Shopizer by package name.
