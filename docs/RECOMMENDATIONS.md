# OKF recommendations

> **Terms.** A *bundle* is OKF's name for a generated guide to a codebase: a folder of markdown files, one per module or package, listing what it contains and where each fact came from. The [main README](../README.md) calls it a *guide*.

What the data supports, in order of how much it matters. Every claim points at a table in [RESULTS.md](RESULTS.md). All of it was measured on one model (Codex `gpt-5.6-luna`), so treat these as defaults to test on your own agent, not as laws.

The six tests fit one picture, and the README organises them as four conditions: **1. No OKF**, **2. OKF**, **3. OKF with confidence labels** and **4. a cross-repo change with OKF**.

**A guide's value depends on whether the agent can read the source it describes. Confidence labels do not make the agent more accurate; with an instruction they make it say when it is leaning on a guess.**

| | The agent can read the source | The agent cannot read the source |
| --- | --- | --- |
| **OKF against no OKF** | No gain: accuracy was already at the ceiling and cost was level or higher (test A). | The guide is what makes the task possible: questions 1 of 24 against 24 of 24 (D); cross-repo changes 3 of 20 against 19 of 20 at half the tokens (F). |
| **A guide that is out of date** | Dangerous (8 of 12 repeated an old fact), and one sentence fixes it (B). | Dangerous (14 to 16 of 16), and nothing we tried fixes it (D). |
| **Confidence labels** | Did not help against out-of-date facts, as expected: they say how a fact was derived, not whether it is current (B). | With an instruction, 6 of 8 wrong answers said they relied on a guess, against 0 without; wrong answers fell only from 11 to 8 of 16 (E). |

## 1. Use a bundle where the agent cannot read the source

A private service, a vendored dependency, another team's repository. This is where it paid off. In D1 the storefront agent could not see the backend: it answered 1 of 24 questions correctly and spent about 785k tokens searching. With the backend's bundle it answered 24 of 24 for about 189k tokens, the same as having the full source (181k).

What answered the questions: a **routes concept** (every route with its handler), each concept's **handlers with their parameter types**, and each request class's **fields**. All of it carries the `path:line` it came from.

In the harder test G (edits to the storefront's real code, six renamed fields, two same-named classes) the guide matched having the backend's actual source, 18 of 20 each against 3 of 20 with nothing. In test F the agent had to change a storefront using facts that only the backend states: 3 of 20 changes passed without the guide and 19 of 20 with it, at about half the tokens (482k against 242k). For a repository the agent can search, do not expect a bundle to be cheaper (A). The best configuration was level on questions and about 21% dearer on change tasks.

## 2. Treat a vendored bundle as a pinned snapshot and keep it fresh automatically

In D2 the backend changed after the bundle was generated. Agents followed the old fact in 14 to 16 of 16 answers and found the new one in none, with no caveat (none of 46 stale answers hedged). The confirm sentence did not help, because there was no source to confirm against. A past `stale_after` on exactly the seven changed concepts did not help either: not one of 32 answers mentioned staleness, though the concepts the agent read were marked stale and the pointer explained the field.

So flags are not a defence for an unreadable dependency; freshness is. Regenerate the bundle whenever the dependency changes, and check in CI that its `sources[].sha256` values still match the dependency (`kgen okf --stale-against CHECKOUT` finds the concepts that differ). A bundle you cannot keep current is worse than none: unchanged facts stayed correct (controls 16/16), but every changed fact was wrong.

## 3. Use confidence labels to make the agent disclose guesses, not to make it right

Mark each fact with how it was derived: `[high]` for what the source states directly (a class, a field, a route, a declared signature), `[medium]` for a heuristic inference (in this generator, which method a call refers to). Add one instruction: "entries marked `[medium]` are heuristic guesses; when your answer relies on one, say so."

What it did (test E, the guide contained four wrong `[medium]` call entries and the agent could not check the source):

- **Labels alone changed nothing.** 10 of 16 answers still followed a wrong entry (11 without labels), and none said so.
- **Labels plus the instruction changed what agents said.** 8 of 16 followed a wrong entry (not a reliable drop from 11, p≈0.5), but 6 of those 8 said the answer rested on a `[medium]` entry. A reader is warned.
- **A wrong fact labelled `[high]` was trusted completely** (10 of 16 followed it, none said anything). The labels are only worth what the generator's honesty about them is worth.
- The cost was small: on unchanged questions the agent hedged on 2 to 3 of 12 where there was nothing to doubt.

In the cross-repo **change** test (F), the labelled condition passed 15 of 20 against 19 of 20 for the plain guide. That is not a reliable difference (p≈0.18); the failures were two wrong field names and three on one path task. Expect labels to be roughly neutral for accuracy and useful for transparency, and measure on your own agent.

Labels say nothing about whether a fact is *current*. They did not help against an out-of-date guide (test B). That needs freshness (recommendation 2).

## 4. Where the source is readable, add one sentence to the agent file

"Read the source to confirm before you rely on it." With the same bundle and the same efficiency pressure, it took stale-following from 8 of 12 to 0 of 12 at no extra token cost (B3). Per-line tags, banners, OKF-native provenance fields and a trust-tier sentence did not (B2). Without the sentence, an unflagged bundle was worse than no bundle (8 of 12 against 0 of 12).

`kgen okf --pointer AGENTS.md` writes the text. It works because the agent can act on it; recommendation 2 is for when it cannot.

## 5. If you generate a bundle, use the default shape

The `recommended` preset (add `--line-tags` for confidence labels): one concept per module (per package for Java), OKF-native fields (`generated`, `sources`, `status`), markdown links between concepts, `path:line` citations on every line, cross-module call edges, a routes concept where there are routes, and a routing index with one line per module.

- Thin bundles (names only, no citations, links or call edges) were the dearest in both A runs (1.42 and 1.26): the agent still searches, so the bundle is extra reading.
- Per-package concepts, no index and full intra-module call edges were no better than the default (A, v1).
- Per-line `[high]/[medium]` tags and banners added size and cost without reducing stale-following. Leave them out unless you have a reason.
- At scale, drop getter and setter calls and group calls per target, or the concepts become too large to read (Shopizer: 168 KB for one package before, 85 KB after).

## 6. Do not vendor a bundle for a dependency the agent can already read

In C every arm passed, including with no bundle, because the library was installed and readable. The vendored bundle cost about 25% more tokens and bought no accuracy. If you do vendor one, mirror it under `okf/references/<name>/` and rewrite its bundle-relative links so they stay inside the mirror (`kgen okf --reference name=path` does), and give it a `--source-url` so its `resource` fields are URLs, not paths that point into the wrong repository.

## 7. For the OKF spec

Checked against the spec text and the reference parser, the output is conformant; the details and the choices that remain are in [CONFORMANCE.md](CONFORMANCE.md). Suggestions for the spec:

- Say how a bundle copied into another bundle should be linked. Bundle-relative links break silently.
- Allow a producer to say what it can vouch for. A deterministic generator vouches for structure, not behaviour; `verified` cannot express that, so it stays empty.
- Define a source digest per concept and how a consumer compares it to the source. A `stale_after` the producer cannot know in advance is only useful if a tool sets it when the source changes, and D2 shows agents do not act on it even when set; a digest a consumer can check would be actionable (the emitter puts one in `sources[].sha256`, an extension key).

## What was not tested

- Other agents or models.
- A bundle inside a **large repository the agent can search** (the complex repository was only used as a dependency, so whether a bundle saves cost on a big codebase is open).
- Confidence labels against more than one kind of `[medium]` fact (only call targets were tested), and where the agent can partly verify them.
- Real (not planted) drift; a dependency the agent cannot read *and* cannot be told is stale by any mechanism other than freshness checks.
- An agent that is told, by a harness, to refuse stale concepts; the pointer explained `stale_after` and the agent did not act on it.
- A language-model-written bundle (excluded by design); human review (`verified` by a person).

## The end state

[`../end-state/`](../end-state/) has the recommended bundles, generated:

- `click/` is Click at the pinned commit.
- `click-after-drift/` is the same bundle after the three refactors, with `stale_after` on the two concepts whose source changed.
- `ledger-lib/` and `invoice-service/` are the cross-repo pair, with the library's bundle mirrored under `invoice-service/okf/references/ledger-lib/`.
- `click-with-confidence/` is the Click guide with `[high]`/`[medium]` labels and the instruction that goes with them.
- `shopizer/` is the real Shopizer backend: 315 files, a routes concept with all 325 routes, and each type's fields.

Each folder has its `AGENTS.md` pointer. To reproduce one, see [the end-state guide](../end-state/README.md).
