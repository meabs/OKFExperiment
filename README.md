# OKF Experiment

**Does generated repository knowledge help coding agents?** About 950 measured agent runs on how an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) (v0.2) bundle should be generated, flagged and shared.

Codex `gpt-5.6-luna` · Click and a Shopizer storefront/backend pair · bundles from a deterministic generator (`kgen okf`, no language model)

[Findings](#findings) · [Recommendations](#recommendations) · [Evidence](#evidence) · [Example](#what-a-bundle-looks-like) · [Conformance](#is-it-valid-okf) · [Method and limits](#method-and-limits) · [Reproduce](#reproducing) · [Layout](#repository-layout)

---

## Findings

| | Finding | Evidence |
| :-: | --- | --- |
| 1 | **For a repository the agent can search, a bundle did not help.** Accuracy was already at the ceiling with or without one, and no bundle beat having none on tokens. | Experiment A, 312 runs (Click) |
| 2 | **For a dependency the agent cannot read, a bundle is what makes the task possible.** Without the backend: **1 of 24** correct, about 785k tokens spent searching. With its bundle: **24 of 24**, about 189k tokens, the same as having the full source. | Experiment D1, 96 runs (Shopizer backend, storefront as the working repo) |
| 3 | **A stale bundle is then the worst case.** After a backend refactor, agents followed the old fact in **14 to 16 of 16** answers and found the new one in none, with no caveat. Neither "read the source to confirm" nor `stale_after` helped. | Experiment D2, 128 runs |
| 4 | **When the source is readable, one sentence stops stale-following.** "Read the source to confirm before you rely on it" took it from 8 of 12 to **0 of 12** at no extra cost; tags, banners and provenance fields did not help. | Experiments B and B3, 340 runs (Click) |
| 5 | **A readable dependency's bundle added cost, not accuracy** (about 25% more tokens). | Experiment C, 72 runs (synthetic pair) |

Findings 3 and 4 fit together: the sentence works because the agent can act on it. When the agent cannot open the source, it has nothing to confirm against, and the bundle's freshness is the only protection.

## Recommendations

What the data supports, in order of how much it matters. One model, so treat these as defaults to test on your own agent.

1. **Use a bundle where the agent cannot read the source.** A private service, a vendored dependency or another team's repository. This is where it paid off (finding 2). For a repository the agent can search, do not expect it to be cheaper.
2. **Treat a vendored bundle as a pinned snapshot and keep it fresh automatically.** Regenerate it whenever the dependency changes, and check in CI that its source digests still match. Flags did not protect agents (finding 3), so freshness is the only defence. `--stale-against` finds the concepts whose source has changed.
3. **Where the source is readable, add one sentence to the agent file:** "read the source to confirm before you rely on it." It stopped stale-following at no cost (finding 4). `kgen okf --pointer AGENTS.md` writes the text.
4. **If you generate a bundle, keep citations, links and a routing index.** The thinnest bundle (names only) was always the dearest. Per-line tags and banners added size without reducing stale-following. For an API dependency, a routes concept (every route with its handler) plus each request class's fields is what answered the questions.
5. **Do not vendor a bundle for a dependency the agent can already read.** It cost about 25% more and bought no accuracy.

The recommended configuration is the `recommended` preset: one concept per module (per package for Java), OKF-native fields, links, `path:line` citations, cross-module call edges, a routes concept and a routing index. Full reasoning: [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md).

## Evidence

Bars are measured counts and ratios. Read anything under 8 runs per arm as provisional.

### D. A complex repository as a dependency the agent cannot read

The working repository is the real Shopizer React storefront. It calls a backend (Shopizer, 1,173 Java files, 325 routes) that is not available. Eight questions each trace one storefront call to the backend handler, the request class and a field. The backend's question-relevant identifiers were renamed, so the answers cannot come from memory of a famous public repository.

**D1, backend current (96 runs, 3 per question per arm):**

| Arm | Correct | Tokens per run | Cost vs no backend |
| --- | --- | --- | --- |
| No backend | `░░░░░░░░░░░░░░░░░░░░░░░░` **1 / 24** | 785k | 1.00 |
| Backend source checked out | `████████████████████████` 24 / 24 | 181k | 0.43 (0.25 to 0.65) |
| Backend bundle, with the confirm sentence | `████████████████████████` 24 / 24 | 189k | 0.41 (0.26 to 0.61) |
| Backend bundle, without it | `████████████████████████` 24 / 24 | 169k | 0.34 (0.24 to 0.45) |

**D2, backend refactored after the bundle was generated (128 runs, 4 per question per arm, efficiency prompt).** Four renames (a handler method, a request-class field, a path variable, a request class) so four questions have a new answer; four unchanged questions are controls.

| Arm | Drift answers that gave the **old** fact | Gave the new fact | Controls correct |
| --- | --- | --- | --- |
| Backend source (refactored) | `░░░░░░░░░░░░░░░░` 0 / 16 | 16 / 16 | 16 / 16 |
| Stale bundle | `██████████████░░` **14 / 16** | 0 / 16 | 16 / 16 |
| Stale bundle + the confirm sentence | `████████████████` **16 / 16** | 0 / 16 | 16 / 16 |
| Stale bundle + the sentence + `stale_after` on the 7 changed concepts | `████████████████` **16 / 16** | 0 / 16 | 16 / 16 |

- None of the 46 stale answers carried a caveat, and none of the 32 answers in the last arm mentioned staleness, although the concepts the agent read were marked stale and the pointer explained the field.
- The bundle did not harm what had not changed: controls were 16/16 everywhere.
- Contamination, stated plainly: Codex can read the whole disk. In D1, 3 of 24 no-backend runs searched it; one found another run's bundle and answered correctly (the 1 of 24), two found backend source copies and still failed. No bundle-arm run reached outside its own workspace, in either trial.

### B. Which flags stop agents following stale claims? (Click, source readable)

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
- Tags, banners and provenance fields did not help (pooled 26/36 against 8/12, p = 0.77). `stale_after` helped a little (11/24 against 43/60, one-sided, post-hoc, p = 0.025): suggestive, and not borne out in D2.

### A. Which bundle shape? (Click: 5 questions and 3 change tasks)

Cost relative to no bundle (1.00). Accuracy was 14 or 15 of 15 on questions and 8 or 9 of 9 on change tasks in **every** arm. The v1 column had the confirm sentence in the agent file; v2 did not.

| Bundle | v1 (24 runs) | v2 (24 runs) |
| --- | --- | --- |
| Minimal: names only, no citations, links, calls or index | `██████████████` 1.42 dearer | `█████████████` 1.26 dearer |
| No call edges | `████████████` 1.21 dearer | `███████████` 1.10 |
| **Default**: citations, links, cross-module calls, routing index | `█████████████` 1.30 dearer | `███████████` **1.07** |
| Code graph only (`kg`) | `███████████` 1.15 dearer | `███████████` 1.14 |

No bundle beat having none. The best (default, v2) was level on questions (0.99) and about 21% dearer on change tasks.

### C. Does a readable dependency's bundle help? (synthetic library and consumer)

| Arm | Verified | Cost vs library installed only |
| --- | --- | --- |
| Library installed only | 12/12 | 1.00 |
| Library source location given | 12/12 | 1.28 dearer |
| Library bundle vendored under `okf/references/` | 12/12 | 1.25 dearer |
| The same with tags, banner and `verified` stamps | 12/12 | 1.25 dearer |
| Stale bundle from an older library version | 12/12 | 1.05 |
| Stale, with tags, banner and targeted `stale_after` | 12/12 | 1.10 |

Everything passed and no run hit a stale-API error: the library was readable, so the agent could always inspect it. D is the case where it was not.

**What went wrong first.** My first runs of A and B put the confirm sentence in every arm, which hid the differences between flags and inflated cost. They were kept ("v1"), rerun without it ("v2"), and a third trial (B3) tested the sentence alone. The first complex-repo attempt let the agent answer from memory of a famous repository; that was caught in a smoke test, and the backend's identifiers were renamed before any trial run. Raw reports: [results/](results/).

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

For an API, a `routes.md` concept lists every route with its handler, which is what the storefront questions were answered from:

```markdown
| POST | `/api/v1/customer/login` | [...customer](/modules/com.salesmanager.shop.store.api.v1.customer.md) `AuthenticateCustomerApi.authenticate` | `sm-shop/src/main/java/.../AuthenticateCustomerApi.java:157` |
```

The generated bundles are in [end-state/](end-state/): Click, Click after the refactors (two concepts marked stale), the synthetic cross-repo pair, and the real Shopizer backend (315 files, 325 routes).

## Is it valid OKF?

Yes. All end-state bundles are conformant with OKF v0.2 (§11), parse and validate with the reference agent's own parser, and pass [`scripts/check_okf.py`](scripts/check_okf.py), a checker written from the spec's MUST and SHOULD rules, with no findings. There is no official validator, so the checker is an interpretation of the prose.

The first version was conformant but filled four optional fields in ways the spec does not intend; those were found and fixed. What remains by design (`path:line` citations instead of footnotes, a single root index) and what it means for the experiments, whose agents read bundles generated before the fix, is in [docs/CONFORMANCE.md](docs/CONFORMANCE.md).

## Method and limits

| | Question | Target | Runs |
| --- | --- | --- | --- |
| **A** | Which generated bundle shape helps most per token? | Click at `2247b35`: 5 questions and 3 change tasks with hidden tests | 192 + 120 |
| **B** | Which confidence flags stop agents following stale claims? | Click after planted refactors ([patch](drift/click-drift.patch)) | 160 + 160 + 20 |
| **C** | Does a readable dependency's bundle help? | A synthetic pair, [`ledger-lib`](fixtures/ledger-lib) and [`invoice-service`](fixtures/invoice-service), 3 change tasks | 72 |
| **D** | Does it help when the dependency is unreadable, and what happens when it goes stale? | Shopizer storefront (working repo) and Shopizer backend (the dependency), 8 questions | 96 + 128 |

- Every hidden test in A to C was checked to fail on the unmodified repository and pass on a reference solution. D's questions have answers derived from the backend source and graded by pattern.
- Runs use [AgentTrialRig](https://github.com/meabs/AgentTrialRig), which records tokens, tool calls and whether the bundle was opened.

**Limits.**
- One model (Codex `gpt-5.6-luna`, medium reasoning); other agents may differ.
- 3 to 4 runs per cell. A and B use one small repository (Click, about 25 modules); C is a synthetic pair.
- **D uses the complex repository only as a dependency.** Whether a bundle saves cost *inside* a large repository the agent can search is untested.
- D's backend is real code with the question-relevant identifiers renamed (so it cannot be recalled) and the planted refactors applied as text edits that were not compiled. Its storefront is unmodified. The renamed backend is still recognisably Shopizer by package name.
- Codex can read the whole disk, so a run can find files outside its workspace. I counted this (3 of 24 no-backend runs in D1; none elsewhere) and stated it above.
- The graders and the planted drift were written by the experimenters, and the pooled flag comparisons in B were chosen after seeing the data.
- A deterministic generator can vouch for structure (names, signatures, call edges, routes), not behaviour.
- Every run also loads the author's global agent skills (a constant overhead in all arms), and v1 and v2 were not run at the same time.
- The agents in A to C read bundles generated before a later fix to a few optional frontmatter fields; the bundle bodies are unchanged and those experiments were not rerun.

## Reproducing

`kgen okf` is not released yet. Until it is, apply the patch to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at commit `dd26ee6` (v0.4.0):

```bash
git clone https://github.com/meabs/AgentGraphWorkTree && cd AgentGraphWorkTree
git checkout dd26ee6 && git apply ../OKFExperiment/scripts/kgen-okf.patch
python .apm/skills/agent-graph/tool/kgen.py sync --repo R
python .apm/skills/agent-graph/tool/kgen.py okf --repo R --out R/okf --pointer R/AGENTS.md
python ../OKFExperiment/scripts/check_okf.py R/okf
```

`kgen` needs `tree-sitter` and `tree-sitter-java`; see that repository. The patch includes a fix to the Java extractor (route paths were read from `produces`/`consumes`, adding spurious routes). To rerun A to C, `scripts/make_a.py`, `make_b.py` and `make_c.py` build each arm and its TOML for AgentTrialRig. To rerun D: clone [shopizer](https://github.com/shopizer-ecommerce/shopizer) at `6a4a0a6` and [shopizer-shop-reactjs](https://github.com/shopizer-ecommerce/shopizer-shop-reactjs) at `455b4bc`, run `scripts/privatize.py` on a copy of the backend (then with `--drift` on a second copy), generate the bundles, and run `scripts/make_d.py`. `scripts/leak_check.py` counts runs that reached outside their workspace; `scripts/analyse_d2.py` counts stale answers.

## Repository layout

| Path | What it holds |
| --- | --- |
| [`docs/`](docs/) | the detail behind this page: [RESULTS.md](docs/RESULTS.md), [RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md), [CONFORMANCE.md](docs/CONFORMANCE.md) |
| [`results/`](results/) | each trial's raw report ([index](results/README.md)) |
| [`end-state/`](end-state/) | the recommended bundles and their `AGENTS.md` pointers ([guide](end-state/README.md)) |
| [`scripts/`](scripts/) | trial builders, `kgen-okf.patch`, `okf.py` (emitter copy), `check_okf.py`, `privatize.py`, `verify*.sh`, analysis scripts |
| [`hidden/`](hidden/), [`fixtures/`](fixtures/), [`drift/`](drift/) | the hidden tests, the cross-repo pair, and the Click refactor |
