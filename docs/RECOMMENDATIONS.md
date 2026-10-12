# OKF recommendations

What the data supports, in order of how much it matters. Every claim points at a table in [RESULTS.md](RESULTS.md). All of it was measured on one model (Codex `gpt-5.6-luna`), so treat these as defaults to test on your own agent, not as laws.

The five experiments fit one picture: **a bundle's value depends on whether the agent can read the source it describes.**

| The agent can read the source | The agent cannot read the source |
| --- | --- |
| A bundle did not help (accuracy at the ceiling, cost level or higher). | A bundle is what makes the task possible (1 of 24 correct without it, 24 of 24 with it). |
| A stale bundle is dangerous, and one sentence fixes it. | A stale bundle is dangerous, and nothing we tried fixes it. |

## 1. Use a bundle where the agent cannot read the source

A private service, a vendored dependency, another team's repository. This is where it paid off. In D1 the storefront agent could not see the backend: it answered 1 of 24 questions correctly and spent about 785k tokens searching. With the backend's bundle it answered 24 of 24 for about 189k tokens, the same as having the full source (181k).

What answered the questions: a **routes concept** (every route with its handler), each concept's **handlers with their parameter types**, and each request class's **fields**. All of it carries the `path:line` it came from.

For a repository the agent can search, do not expect a bundle to be cheaper (A). The best configuration was level on questions and about 21% dearer on change tasks.

## 2. Treat a vendored bundle as a pinned snapshot and keep it fresh automatically

In D2 the backend changed after the bundle was generated. Agents followed the old fact in 14 to 16 of 16 answers and found the new one in none, with no caveat (none of 46 stale answers hedged). The confirm sentence did not help, because there was no source to confirm against. A past `stale_after` on exactly the seven changed concepts did not help either: not one of 32 answers mentioned staleness, though the concepts the agent read were marked stale and the pointer explained the field.

So flags are not a defence for an unreadable dependency; freshness is. Regenerate the bundle whenever the dependency changes, and check in CI that its `sources[].sha256` values still match the dependency (`kgen okf --stale-against CHECKOUT` finds the concepts that differ). A bundle you cannot keep current is worse than none: unchanged facts stayed correct (controls 16/16), but every changed fact was wrong.

## 3. Where the source is readable, add one sentence to the agent file

"Read the source to confirm before you rely on it." With the same bundle and the same efficiency pressure, it took stale-following from 8 of 12 to 0 of 12 at no extra token cost (B3). Per-line tags, banners, OKF-native provenance fields and a trust-tier sentence did not (B2). Without the sentence, an unflagged bundle was worse than no bundle (8 of 12 against 0 of 12).

`kgen okf --pointer AGENTS.md` writes the text. It works because the agent can act on it; recommendation 2 is for when it cannot.

## 4. If you generate a bundle, use the default shape

The `recommended` preset: one concept per module (per package for Java), OKF-native fields (`generated`, `sources`, `status`), markdown links between concepts, `path:line` citations on every line, cross-module call edges, a routes concept where there are routes, and a routing index with one line per module.

- Thin bundles (names only, no citations, links or call edges) were the dearest in both A runs (1.42 and 1.26): the agent still searches, so the bundle is extra reading.
- Per-package concepts, no index and full intra-module call edges were no better than the default (A, v1).
- Per-line `[high]/[medium]` tags and banners added size and cost without reducing stale-following. Leave them out unless you have a reason.
- At scale, drop getter and setter calls and group calls per target, or the concepts become too large to read (Shopizer: 168 KB for one package before, 85 KB after).

## 5. Do not vendor a bundle for a dependency the agent can already read

In C every arm passed, including with no bundle, because the library was installed and readable. The vendored bundle cost about 25% more tokens and bought no accuracy. If you do vendor one, mirror it under `okf/references/<name>/` and rewrite its bundle-relative links so they stay inside the mirror (`kgen okf --reference name=path` does), and give it a `--source-url` so its `resource` fields are URLs, not paths that point into the wrong repository.

## 6. For the OKF spec

Checked against the spec text and the reference parser, the output is conformant; the details and the choices that remain are in [CONFORMANCE.md](CONFORMANCE.md). Suggestions for the spec:

- Say how a bundle copied into another bundle should be linked. Bundle-relative links break silently.
- Allow a producer to say what it can vouch for. A deterministic generator vouches for structure, not behaviour; `verified` cannot express that, so it stays empty.
- Define a source digest per concept and how a consumer compares it to the source. A `stale_after` the producer cannot know in advance is only useful if a tool sets it when the source changes, and D2 shows agents do not act on it even when set; a digest a consumer can check would be actionable (the emitter puts one in `sources[].sha256`, an extension key).

## What was not tested

- Other agents or models.
- A bundle inside a **large repository the agent can search** (the complex repository was only used as a dependency, so whether a bundle saves cost on a big codebase is open).
- Real (not planted) drift; a dependency the agent cannot read *and* cannot be told is stale by any mechanism other than freshness checks.
- An agent that is told, by a harness, to refuse stale concepts; the pointer explained `stale_after` and the agent did not act on it.
- A language-model-written bundle (excluded by design); human review (`verified` by a person).

## The end state

[`../end-state/`](../end-state/) has the recommended bundles, generated:

- `click/` is Click at the pinned commit.
- `click-after-drift/` is the same bundle after the three refactors, with `stale_after` on the two concepts whose source changed.
- `ledger-lib/` and `invoice-service/` are the cross-repo pair, with the library's bundle mirrored under `invoice-service/okf/references/ledger-lib/`.
- `shopizer/` is the real Shopizer backend: 315 files, a routes concept with all 325 routes, and each type's fields.

Each folder has its `AGENTS.md` pointer. To reproduce one, see [the end-state guide](../end-state/README.md).
