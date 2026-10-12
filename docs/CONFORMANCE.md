# Conformance with the OKF v0.2 spec

**Short answer:** the end-state bundles are conformant with OKF v0.2 as the spec defines it (§11), and they now pass a stricter check of the spec's SHOULD-level rules too. The first version did not: it was conformant, but it filled two optional fields in ways the spec does not intend, and it had one latent bug. Those were found by checking against the spec text and the reference parser, and fixed.

## What was checked, and against what

- The spec: [`SPEC.md`](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md), v0.2. The copy in `GoogleCloudPlatform/knowledge-catalog/okf/` that this work started from is a frozen snapshot (its README says the canonical home moved); the two files are identical.
- The reference agent's own parser (`reference_agent/bundle/document.py`): every concept parsed and validated, trust tiers and `stale_after` were derived with its `trust_tier` and `is_stale`.
- [`scripts/check_okf.py`](../scripts/check_okf.py), written from the spec's rules: frontmatter parses and carries a non-empty `type` (§11.1 and §11.2, MUST); reserved files follow §8 and §9 (MUST); and SHOULD-level rules for path-valued fields (§6.2), timestamps with an explicit offset (§5), actors (§7), `status` values (§5.4), `sources` entries (§5.1) and link resolution (§6.1). Run it with `python scripts/check_okf.py BUNDLE/okf`.

There is no official validator or JSON schema; the spec is prose, and the checker is an interpretation of it.

## Result for the end-state bundles

| Bundle | Concepts | MUST findings | SHOULD findings | Reference parser |
| --- | --- | --- | --- | --- |
| `click` | 32 | 0 | 0 | all parse and validate; all `unverified` |
| `click-after-drift` | 32 | 0 | 0 | the two changed concepts are stale, no others |
| `ledger-lib` | 6 | 0 | 0 | all parse and validate |
| `invoice-service` (with the mirrored library) | 8 | 0 | 0 | all parse and validate |
| `shopizer` (Java: package concepts and a routes concept) | 313 packages, 1 routes concept | 0 | 0 | not run |

## What was wrong in the first version

| Finding | Why it was a problem | Fix |
| --- | --- | --- |
| `resource` and `sources[].resource` were `repo:src/click/core.py` | §6.2 allows an absolute URL, a bundle-relative path (`/...`) or a relative path. `repo:` is none of these. | An absolute URL to the file at the synced commit (`https://github.com/<owner>/<repo>/blob/<commit>/<path>`), taken from `git remote` or `--source-url`; otherwise a relative path from `modules/`. |
| `sources[].id` held a content digest | §5.1 defines `id` as a *stable key* used for footnote attribution. A digest changes whenever the source does, and nothing in the body used it as a footnote label. | The digest moved to a producer-defined key, `sha256` (the spec allows extra keys). |
| A module named `index` or `log` would produce `modules/index.md` | §3.1: those filenames are reserved at any level and must not be concept files. | Such modules are written as `index-module.md` / `log-module.md`. |
| `sources[].last_modified` was the repository's HEAD time for every file | §5.1: when *the source itself* last changed. | Each file's own last-commit time from `git log`. |

## Deviations that remain, by design

- **Per-line citations are `path:line`, not footnotes.** §5.1 attributes claims with markdown footnotes keyed to `sources[].id`. A footnote cannot carry a line number without one label per line, and the line number is what makes a claim checkable, so each line ends with `` `path:line` `` instead. This is an extension, not a violation, but a consumer looking for footnotes will not find any.
- **The index is one root `index.md`** with a heading, one line of orientation and a flat list of `- [title](/modules/x.md) - description`. The spec allows an index in any directory and the reference agent writes one per directory, grouped by `type`; this bundle has no per-directory indexes. The spec treats the root index as optional and the format as markdown, so `-` against `*` bullets and the extra line are within it.
- **`generated.at` is the source commit time,** not the time the generator ran, so that regenerating the same commit gives byte-identical files. §5.2 describes it as the content's last meaningful change, which this is.
- **`type: Code Module`** is a producer-chosen type (the spec does not register types).
- **No `verified` entries in the recommended preset.** The optional `attest` switch writes `process:kgen-extract`, but that is the generator vouching for itself, not an independent confirmation, which is what §5.2 means by `verified`. The experiments gave it no benefit, so it is off.
- **Mirrored bundles.** The spec does not say how a bundle copied under `references/` should be linked. Bundle-relative links (`/modules/x.md`) are rewritten to stay inside the mirror. A relative `resource` path would point into the wrong repository once mirrored, so give any bundle you plan to mirror a `--source-url`.

## What this means for the experiments

The agents in the experiments read bundles produced **before** these fixes. The differences are in frontmatter only: `resource` and `sources[].resource` were `repo:` paths, `sources[].id` was a digest, and `last_modified` was the commit time. The body of each concept, which is what the agents mostly read, is unchanged. The experiments were not rerun, so a small effect from the changed frontmatter fields cannot be ruled out, though none of the fields was involved in the findings. The bundles in `end-state/` are the corrected ones.

## The older `kgen sync` documents are not conformant

`kgen sync` also writes an older set of documents under `.agent-knowledge/okf/` (used in the earlier Java experiments). Checked with the same script, they have one MUST finding (an `index.md` with frontmatter, §8) and use the v0.1 `timestamp` field (§13.1) and a custom `generation:` block. `kgen okf` is the conformant path; the older renderer has not been changed.
