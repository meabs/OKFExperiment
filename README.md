# OKF experiment

How should a repository's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (v0.2) bundle be generated, flagged and shared across repositories so that coding agents do better work with it?

Three experiments, about 720 agent runs with Codex `gpt-5.6-luna`, bundles from a deterministic generator (`kgen okf`, no language model).

**Read next:** [Recommendations](docs/RECOMMENDATIONS.md) (what to do) · [Results](docs/RESULTS.md) (the tables) · [End-state bundles](end-state/) (the recommended output, generated) · [Raw reports](results/)

## The answer in five lines

| Finding | Evidence |
| --- | --- |
| Accuracy was at the ceiling with or without a bundle, and no bundle beat having none on tokens. | A: 8 bundle shapes, 192 + 120 runs |
| An unflagged bundle made agents follow stale claims: 8 of 12 drift answers, against 0 of 12 with no bundle. | B: 160 runs |
| One sentence in the agent file, "read the source to confirm before you rely on it", stopped it (0 of 12) at no extra cost. Per-line tags, banners and OKF-native provenance fields did not help. | B3: 20 runs, same bundle and prompt |
| `stale_after` on only the changed concepts helped a little (5 of 12 against 8 of 12); suggestive, not settled. | B: 160 runs |
| Another repository's bundle added about 25% cost and no accuracy when the dependency was readable. | C: 72 runs, synthetic pair |

## The three experiments

| | Question | Target | Arms |
| --- | --- | --- | --- |
| A | Which auto-generated bundle shape helps most per token? | [Click](https://github.com/pallets/click) at `2247b35`: 5 questions and 3 change tasks with hidden tests | none, minimal, no call edges, cross-module calls, all calls, package-level, no index, code graph only |
| B | Which confidence flags stop agents following stale claims without making them distrust correct ones? | Click after three planted refactors ([`drift/click-drift.patch`](drift/click-drift.patch)); the bundle is generated before them | none, no flags, OKF-native fields, per-line tags, banner, tags + banner + `verified`, targeted `stale_after`, blanket `stale_after` |
| C | Does another repository's bundle help an agent change this one? | a synthetic pair, [`fixtures/ledger-lib`](fixtures/ledger-lib) and [`fixtures/invoice-service`](fixtures/invoice-service): 3 change tasks with hidden tests | library installed only, library source pointed at, fresh bundle, fresh tagged bundle, stale bundle, stale tagged bundle |

## What makes a result believable

- Every hidden test was checked to fail on the unmodified repository and pass on a reference solution ([`scripts/solve.py`](scripts/solve.py), [`solve_c.py`](scripts/solve_c.py)), on both the original and the drifted Click.
- The planted Click refactors keep Click's own 2261 tests passing.
- Arms within a trial differ in a small, listed set of switches (see [Results](docs/RESULTS.md) for what each arm adds), so a difference can be traced to them.
- Runs use [AgentTrialRig](https://github.com/meabs/AgentTrialRig), which records tokens, tool calls and whether the bundle was opened.

## What went wrong first, and how it was handled

The first runs of A and B (labelled "v1") had a pointer in the agent file that told the agent to confirm in the source, in every arm. That hid the differences between flags and may have inflated cost. They were kept, reported next to reruns without that sentence ("v2"), and a further run (B3) tested the sentence alone. A cross-repo run started with the same pointer was stopped and rerun, and its aborted partial results are not reported.

## Limits

- One model (Codex `gpt-5.6-luna`, medium reasoning); other agents may differ.
- Small samples: 3 to 4 runs per cell. Read anything under 8 runs per arm as provisional.
- One repository for A and B (Click, about 25 modules); a synthetic pair for C, so the cross-repo fact is known and it is not a real service.
- A deterministic generator can vouch for structure (names, signatures, call edges), not behaviour.
- Every run also loads the author's global agent skills (a constant overhead in all arms).
- The graders and the planted drift were written by the experimenters, and the pooled flag comparisons in B were chosen after seeing the data.
- v1 and v2 were not run at the same time.

## Reproducing

`kgen okf` is not released yet. Until it is, apply the patch to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at commit `dd26ee6` (v0.4.0):

```bash
git clone https://github.com/meabs/AgentGraphWorkTree && cd AgentGraphWorkTree
git checkout dd26ee6 && git apply ../OKFExperiment/scripts/kgen-okf.patch
python .apm/skills/agent-graph/tool/kgen.py sync --repo R
python .apm/skills/agent-graph/tool/kgen.py okf --repo R --out R/okf --pointer R/AGENTS.md
```

`kgen` needs its dependencies (`tree-sitter`, `tree-sitter-java`); see that repo's README.

## Layout

| Path | What it holds |
| --- | --- |
| [`docs/`](docs/) | the write-up: [RESULTS.md](docs/RESULTS.md), [RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md) |
| [`results/`](results/) | each trial's raw report ([index](results/README.md)) |
| [`end-state/`](end-state/) | the recommended bundles and their `AGENTS.md` pointers ([guide](end-state/README.md)) |
| [`scripts/`](scripts/) | `make_a.py`, `make_b.py`, `make_c.py` build each trial's arms; `kgen-okf.patch` adds `kgen okf` to AgentGraphWorkTree (51 passing tests; see below), and `okf.py` is a copy of the emitter; `verify*.sh` run the hidden tests; `analyse_b.py` counts stale-following |
| [`hidden/`](hidden/) | the hidden tests |
| [`fixtures/`](fixtures/), [`drift/`](drift/) | the cross-repo pair and the Click refactor |
