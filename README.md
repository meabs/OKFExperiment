# OKF Experiment

**Does generated repository knowledge help coding agents?** About 720 measured agent runs on how an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) (v0.2) bundle should be generated, flagged and shared.

Codex `gpt-5.6-luna` · Click as the main repository · bundles from a deterministic generator (`kgen okf`, no language model)

[Findings](#findings) · [Recommendations](#recommendations) · [Evidence](#evidence) · [Example](#what-a-bundle-looks-like) · [Conformance](#is-it-valid-okf) · [Method and limits](#method-and-limits) · [Reproduce](#reproducing) · [Layout](#repository-layout)

---

## Findings

| | Finding | Evidence |
| :-: | --- | --- |
| 1 | **Accuracy was already at the ceiling.** With or without a bundle, almost every answer was right and every change verified. No bundle beat having none on tokens. | Experiment A, 312 runs |
| 2 | **An unflagged bundle misled agents.** After three planted refactors they followed the old fact in **8 of 12** answers. With no bundle: 0 of 12. | Experiment B, 160 runs |
| 3 | **One sentence fixed it.** "Read the source to confirm before you rely on it" in the agent file took stale-following to **0 of 12**, at no extra token cost. Per-line tags, banners and OKF-native provenance fields did not help. | Experiment B3, 20 runs, same bundle and prompt |
| 4 | **Another repository's bundle added cost, not accuracy** (about 25% more tokens) when the dependency was readable. A dependency the agent cannot read is untested. | Experiment C, 72 runs, synthetic pair |

## Recommendations

What the data supports, in order of how much it matters. One model and small repositories, so treat these as defaults to test on your own agent.

1. **Add one sentence to the agent file:** "read the source to confirm before you rely on it." It was the only thing that stopped stale-following, and it cost nothing. `kgen okf --pointer AGENTS.md` writes the text.
2. **Do not expect a bundle to make a small repository cheaper.** Build one when the repository is too large or too unfamiliar to search quickly, and measure on yours first.
3. **If you generate one, keep citations, links and a routing index.** The thinnest bundle (names only) was always the dearest. Per-line tags and banners added size without reducing stale-following.
4. **Keep it fresh instead of flagging it.** Regenerate on change. When you cannot, mark only the concepts whose source changed with a past `stale_after` (`--stale-against`).
5. **Do not vendor another repository's bundle by default.** Use it when the agent genuinely cannot read the dependency, and rewrite its links so they stay inside the mirror.

The recommended configuration is the `recommended` preset: one concept per module, OKF-native fields, links, `path:line` citations, cross-module call edges and a routing index. Full reasoning: [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md).

## Evidence

Bars are measured counts and ratios. Read anything under 8 runs per arm as provisional.

### B. Which flags stop agents following stale claims?

Click after three planted refactors (a renamed function, a new intermediate base class, a call moved behind a helper); the bundle is from before them. 12 drift answers per arm. Efficiency prompt, no instruction to verify.

| Arm | Followed a stale claim | Cost vs no bundle |
| --- | --- | --- |
| No bundle | `░░░░░░░░░░░░` 0 / 12 | 1.00 |
| Bundle, no flags | `████████░░░░` **8 / 12** | 1.42 |
| + OKF-native fields (`generated`, `sources`, `status`) | `█████████░░░` 9 / 12 | 1.25 |
| + per-line `[high]/[medium]` tags | `████████░░░░` 8 / 12 | 1.31 |
| + banner telling the reader to check | `██████████░░` 10 / 12 | 1.28 |
| + tags, banner and `verified` stamps | `████████░░░░` 8 / 12 | 1.32 |
| + `stale_after` on changed concepts only | `█████░░░░░░░` 5 / 12 | 1.29 |
| + `stale_after` on every concept | `██████░░░░░░` 6 / 12 | 1.34 |
| **No flags + the one sentence** (B3) | `░░░░░░░░░░░░` **0 / 12** | same as no flags |

- An unflagged bundle was worse than none: 8/12 against 0/12 (Fisher exact, two-sided p ≈ 0.001).
- Tags, banners and provenance fields did not help (pooled 26/36 against 8/12, p = 0.77). `stale_after` helped a little (11/24 against 43/60, one-sided, post-hoc, p = 0.025): suggestive, not settled.
- The renamed function was followed most often: agents answered from the bundle without searching for the new name.

### A. Which bundle shape? (Click: 5 questions and 3 change tasks)

Cost relative to no bundle (1.00). Accuracy was 14 or 15 of 15 on questions and 8 or 9 of 9 on change tasks in **every** arm. The v1 column had the confirm sentence in the agent file; v2 did not.

| Bundle | v1 (24 runs) | v2 (24 runs) |
| --- | --- | --- |
| Minimal: names only, no citations, links, calls or index | `██████████████` 1.42 dearer | `█████████████` 1.26 dearer |
| No call edges | `████████████` 1.21 dearer | `███████████` 1.10 |
| **Default**: citations, links, cross-module calls, routing index | `█████████████` 1.30 dearer | `███████████` **1.07** |
| Code graph only (`kg`) | `███████████` 1.15 dearer | `███████████` 1.14 |

No bundle beat having none. The best (default, v2) was level on questions (0.99) and about 21% dearer on change tasks. Per-package concepts, no index and full intra-module call edges were no better than the default (v1 only).

### C. Does another repository's bundle help? (synthetic library and consumer)

| Arm | Verified | Cost vs library installed only |
| --- | --- | --- |
| Library installed only | 12/12 | 1.00 |
| Library source location given | 12/12 | 1.28 dearer |
| Library bundle vendored under `okf/references/` | 12/12 | 1.25 dearer |
| The same with tags, banner and `verified` stamps | 12/12 | 1.25 dearer |
| Stale bundle from an older library version | 12/12 | 1.05 |
| Stale, with tags, banner and targeted `stale_after` | 12/12 | 1.10 |

Everything passed and no run hit a stale-API error. The library was installed and readable, so the agent could always inspect it. This does not show that cross-repo bundles never help; a dependency the agent cannot read is untested.

**What went wrong first.** My first runs of A and B put the confirm sentence in every arm, which hid the differences between flags and inflated cost. They were kept ("v1"), rerun without it ("v2"), and a third trial (B3) tested the sentence alone. Raw reports: [results/](results/).

## What a bundle looks like

A real concept file from the Click bundle: OKF frontmatter, then a body where every line ends with the file and line it came from.

```markdown
---
type: Code Module
title: "click.core"
resource: "https://github.com/pallets/click/blob/2247b35.../src/click/core.py"
generated: { by: "kgen/0.4.0", at: "2026-10-04T15:19:53-07:00" }
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35.../src/click/core.py"
    sha256: "26307e89b7b2..."
status: stable
---

## Types
- `Option` (class) extends `click.core.Parameter`  `src/click/core.py:3057`

## Functions and methods
- `Context.get_parameter_source(name: str) -> ParameterSource | None`  `src/click/core.py:970`

## Calls
- `Parameter.consume_value` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value`  `src/click/core.py:2718`
```

The generated bundles are in [end-state/](end-state/): Click, Click after the refactors (two concepts marked stale), and the cross-repo pair with the library's bundle mirrored under `references/`.

## Is it valid OKF?

Yes. All four end-state bundles are conformant with OKF v0.2 (§11), parse and validate with the reference agent's own parser, and pass [`scripts/check_okf.py`](scripts/check_okf.py), a checker written from the spec's MUST and SHOULD rules, with no findings. There is no official validator, so the checker is an interpretation of the prose.

The first version was conformant but filled four optional fields in ways the spec does not intend (a made-up `repo:` URI scheme, a content digest in `sources[].id`, a possible reserved-filename clash, and HEAD time as every file's `last_modified`). Those were found and fixed. What remains by design (`path:line` citations instead of footnotes, a single root index) and what it means for the experiments, whose agents read bundles generated before the fix, is in [docs/CONFORMANCE.md](docs/CONFORMANCE.md).

## Method and limits

| | Question | Target | Runs |
| --- | --- | --- | --- |
| **A** | Which generated bundle shape helps most per token? | Click at `2247b35`: 5 questions and 3 change tasks with hidden tests | 192 + 120 |
| **B** | Which confidence flags stop agents following stale claims? | Click after planted refactors ([patch](drift/click-drift.patch)) | 160 + 160 + 20 |
| **C** | Does another repository's bundle help an agent change this one? | A synthetic pair, [`ledger-lib`](fixtures/ledger-lib) and [`invoice-service`](fixtures/invoice-service), 3 change tasks | 72 |

- Every hidden test was checked to fail on the unmodified repository and pass on a reference solution, on both the original and the drifted Click. The planted refactors keep Click's own 2261 tests passing.
- Runs use [AgentTrialRig](https://github.com/meabs/AgentTrialRig), which records tokens, tool calls and whether the bundle was opened.

**Limits.**
- One model (Codex `gpt-5.6-luna`, medium reasoning); other agents may differ.
- 3 to 4 runs per cell. One small repository (Click, about 25 modules) for A and B; a synthetic pair for C, so it is not a real service.
- The graders and the planted drift were written by the experimenters, and the pooled flag comparisons in B were chosen after seeing the data.
- A deterministic generator can vouch for structure (names, signatures, call edges), not behaviour.
- Every run also loads the author's global agent skills (a constant overhead in all arms), and v1 and v2 were not run at the same time.
- The agents read bundles generated before a later fix to a few optional frontmatter fields; the bundle bodies are unchanged and nothing was rerun.
- **A larger, real repository is the obvious next test.**

## Reproducing

`kgen okf` is not released yet. Until it is, apply the patch to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at commit `dd26ee6` (v0.4.0):

```bash
git clone https://github.com/meabs/AgentGraphWorkTree && cd AgentGraphWorkTree
git checkout dd26ee6 && git apply ../OKFExperiment/scripts/kgen-okf.patch
python .apm/skills/agent-graph/tool/kgen.py sync --repo R
python .apm/skills/agent-graph/tool/kgen.py okf --repo R --out R/okf --pointer R/AGENTS.md
python ../OKFExperiment/scripts/check_okf.py R/okf
```

`kgen` needs `tree-sitter` and `tree-sitter-java`; see that repository. Reproduction from a clean clone is byte-identical to the published bundles. To rerun a trial, `scripts/make_a.py`, `make_b.py` and `make_c.py` build each arm and its TOML for AgentTrialRig.

## Repository layout

| Path | What it holds |
| --- | --- |
| [`docs/`](docs/) | the detail behind this page: [RESULTS.md](docs/RESULTS.md), [RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md), [CONFORMANCE.md](docs/CONFORMANCE.md) |
| [`results/`](results/) | each trial's raw report ([index](results/README.md)) |
| [`end-state/`](end-state/) | the recommended bundles and their `AGENTS.md` pointers ([guide](end-state/README.md)) |
| [`scripts/`](scripts/) | trial builders, `kgen-okf.patch`, `okf.py` (emitter copy), `check_okf.py`, `verify*.sh`, `analyse_b.py` |
| [`hidden/`](hidden/), [`fixtures/`](fixtures/), [`drift/`](drift/) | the hidden tests, the cross-repo pair, and the Click refactor |
