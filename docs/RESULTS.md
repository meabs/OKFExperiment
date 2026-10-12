# Results

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

## Spec findings from building it

- Bundle-relative links (`/modules/x.md`) point at the bundle root, so a bundle copied under `references/<name>/` has every internal link broken unless they are rewritten. The emitter rewrites them; the spec does not say how a vendored bundle should be linked.
- A deterministic generator can vouch for structure (names, signatures, call edges, citations), not behaviour. The spec's `verified` field cannot express that, and most concepts contain medium-confidence call edges, so `verified` stamps rarely applied.

## Limits

One model; one repository for A and B (Click, about 25 modules); a synthetic pair for C; 3 to 4 runs per cell; graders and drift written by the experimenters; a constant overhead from the author's global agent skills in every run; v1 and v2 not run simultaneously. The pooled B comparisons were chosen after seeing the data. The bundles the agents read were generated before a later fix to a few optional frontmatter fields (`resource`, `sources[].id`, `last_modified`; see [CONFORMANCE.md](CONFORMANCE.md)); concept bodies were unchanged and nothing was rerun. A language-model arm was excluded by design.
