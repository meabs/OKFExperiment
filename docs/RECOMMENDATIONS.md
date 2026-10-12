# OKF recommendations

What the data supports, in order of how much it matters. Every claim points at a table in [RESULTS.md](RESULTS.md). All of it was measured on one model (Codex `gpt-5.6-luna`) and small repositories, so treat these as defaults to test on your own agent, not as laws.

## 1. Put one sentence in the agent file: "read the source to confirm before you rely on it"

This was the only thing that stopped agents following stale claims. With the same bundle and the same efficiency pressure, the sentence took stale-following from 8 of 12 to 0 of 12, at no extra token cost (B3). Per-line tags, banners, OKF-native provenance fields and a trust-tier sentence did not (B2). Without the sentence, an unflagged bundle was worse than no bundle at all (8 of 12 against 0 of 12).

`kgen okf --pointer AGENTS.md` writes the text with the sentence in it.

## 2. Do not expect a bundle to make a small, searchable repository cheaper

On Click, accuracy was already at the ceiling without a bundle, and no bundle beat having none on tokens (A). The best configuration was level on questions and about 21% dearer on change tasks. A bundle is worth building when the repository is too large or too unfamiliar to search quickly, not as a default. Measure on yours first (AgentTrialRig).

## 3. If you generate one, use the default shape

The `recommended` preset: one concept per module, OKF-native fields (`generated`, `sources`, `status`), markdown links between concepts, `path:line` citations on every line, cross-module call edges, and a routing index with one line per module.

- Thin bundles (names only, no citations, links or call edges) were the dearest in both runs (1.42 and 1.26): the agent still searches, so the bundle is extra reading.
- Per-package concepts, no index and full intra-module call edges were no better than the default.
- Per-line `[high]/[medium]` tags and banners added size and cost without reducing stale-following. Leave them out unless you have a reason.

## 4. Keep it fresh instead of flagging it

Regenerate on change (it is deterministic and takes seconds). When you cannot, mark only the concepts whose source changed with a past `stale_after` (`kgen okf --stale-against <checkout>`), and keep the sentence from item 1. Targeted `stale_after` was the only flag that moved stale-following (5/12 against 8/12; suggestive, not settled), and marking every concept was no better (6/12).

A renamed symbol is the drift agents follow most (they answer from the bundle without searching for the new name), so a stale check that catches renames is worth the most.

## 5. Do not vendor another repository's bundle by default

In the cross-repo pair, every arm passed, including with no bundle, because the library was installed and readable. The vendored bundle cost about 25% more tokens and bought no accuracy (C). Vendor one when the agent genuinely cannot read the dependency (a private service, a binary), and test that case. If you do:

- Mirror it under `okf/references/<name>/` and rewrite its bundle-relative links so they stay inside the mirror (`kgen okf --reference name=path` does). The spec does not say how a vendored bundle should be linked.
- Regenerate it when the dependency changes; a stale copy was harmless here only because the agent also read the library.

## 6. For the OKF spec

- Say how a bundle copied into another bundle should be linked. Bundle-relative links break silently.
- Allow a producer to say what it can vouch for. A deterministic generator vouches for structure, not behaviour; `verified` cannot express that, so it stays empty.
- A `stale_after` the producer cannot know in advance (it depends on when the source changes) is only useful if a tool sets it when the source changes. Consider a defined source digest per concept and a way to compare it (the emitter puts a digest in `sources[].id`, which the spec defines as an attribution key, not a digest).

## What was not tested

Other agents or models; large repositories; dependencies the agent cannot read; real (not planted) drift; a language-model-written bundle (excluded by design); human review (`verified` by a person).

## The end state

[`../end-state/`](../end-state/) has the recommended bundles, generated:

- `click/` is Click at the pinned commit.
- `click-after-drift/` is the same bundle after the three refactors, with `stale_after` on the two concepts whose source changed.
- `ledger-lib/` and `invoice-service/` are the cross-repo pair, with the library's bundle mirrored under `invoice-service/okf/references/ledger-lib/`.

Each folder has its `AGENTS.md` pointer. To reproduce one: sync with `kgen sync --repo R`, then `kgen okf --repo R --out R/okf --pointer R/AGENTS.md` (add `--stale-against CHECKOUT` or `--reference NAME=BUNDLE` as needed).
