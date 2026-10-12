# OKF experiment

How should a repository's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (v0.2) bundle be generated, flagged and shared across repositories so that coding agents do better work with it?

**Status: complete.** Start with [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md), then [docs/RESULTS.md](docs/RESULTS.md). The recommended bundles, generated, are in [end-state/](end-state/).

Headline: with Codex on small repositories, accuracy was at the ceiling with or without a bundle, no bundle beat having none on tokens, an unflagged bundle made agents follow stale claims (8 of 12 against 0 of 12 with none), and the one thing that stopped it was a sentence in the agent file telling it to confirm in the source (0 of 12, no extra cost). Tags, banners and OKF-native provenance fields did not help.

## Three experiments

| | Question | Target | Arms |
| --- | --- | --- | --- |
| A | Which auto-generated bundle shape helps most per token? | [Click](https://github.com/pallets/click) at `2247b35`, 5 questions + 3 change tasks with hidden tests | none, minimal, no call edges, cross-module calls, all calls, package-level, no index, code graph only |
| B | Which confidence flags stop agents following stale claims without making them distrust correct ones? | Click after three planted refactors (`drift/click-drift.patch`); the bundle is generated before them | none, no flags, OKF-native fields, per-line tags, banner, tags + banner + attest, targeted `stale_after`, blanket `stale_after` |
| C | Does another repository's bundle help an agent change this repository? | a synthetic pair, `fixtures/ledger-lib` and `fixtures/invoice-service`, 3 change tasks with hidden tests | library installed only, library source pointed at, fresh bundle, fresh tagged bundle, stale bundle, stale tagged bundle |

Bundles come from a deterministic generator (`kgen okf`, no language model): every line is derived from the source and carries its file and line. There is no language-model arm by design.

## What makes a result believable here

- Every hidden test was checked to fail on the unmodified repository and pass on a reference solution (`scripts/solve*.py`), on both the original and the drifted Click.
- The planted Click refactors keep Click's own 2261 tests passing.
- Each arm differs from its neighbour by one switch, so a difference can be assigned to it.
- Runs use AgentTrialRig, which records tokens, tool calls and whether the bundle was opened.

## Known limits (stated before the results)

- One model: Codex `gpt-5.6-luna`, medium reasoning. Other agents may differ.
- Small samples (3 to 4 runs per cell). Intervals are reported; read anything under 8 runs per arm as provisional.
- The cross-repo pair is synthetic, so the cross-repo fact is known; it is not a real service.
- A deterministic generator can vouch for structure (names, signatures, call edges), not behaviour.
- Every run also loads the author's global agent skills (a constant overhead in all arms).
- The graders and the planted drift were written by the experimenters.

## Method notes

Two of the original runs (A and B, "v1") had a pointer that told the agent to confirm in the source in every arm, which hid the differences between flags and may have inflated cost. They were kept, reported next to the reruns without that sentence ("v2"), and a third run (B3) tested the sentence alone. See `results/` for each report.

## Layout

- `scripts/make_a.py`, `make_b.py`, `make_c.py` build each trial's arms and TOML.
- `scripts/okf.py` is a snapshot of the bundle emitter (it lives in `kgen`, with 51 passing tests).
- `hidden/` holds the hidden tests; `scripts/verify*.sh` run them.
- `fixtures/` and `drift/` hold the cross-repo pair and the Click refactor.
- `results/` holds each trial's report; `docs/` the write-up; `end-state/` the recommended bundles.
- `scripts/chain.sh` and `analyse_b.py` ran the reruns and counted stale-following.
