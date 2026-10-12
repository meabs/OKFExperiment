# End-state bundles

> **Terms.** A *bundle* is OKF's name for a generated guide to a codebase: a folder of markdown files, one per module or package, listing what it contains and where each fact came from. The [main README](../README.md) calls it a *guide*.

The recommended output, generated with `kgen okf --preset recommended` (see [../docs/RECOMMENDATIONS.md](../docs/RECOMMENDATIONS.md)). Each folder has the bundle (`okf/`) and the `AGENTS.md` pointer that goes beside it. The pointer's last sentence ("read the source to confirm before you rely on it") is the part the experiments found to matter.

| Folder | What it is |
| --- | --- |
| [`click/`](click/) | Click at the pinned commit `2247b35`. 33 concept files, one per module. |
| [`click-with-confidence/`](click-with-confidence/) | The same Click guide with confidence labels: each line ends with `[high]` (stated in the source) or `[medium]` (a heuristic guess, such as a call target), and the agent-instruction file asks the reader to say when its answer relies on a `[medium]` entry. |
| [`click-after-drift/`](click-after-drift/) | The same bundle checked against the refactored Click (`kgen okf --stale-against`): the two concepts whose source changed (`click.core`, `click.shell_completion`) carry a past `stale_after`, and the pointer says what that means. |
| [`ledger-lib/`](ledger-lib/) | The library repository of the cross-repo pair. |
| [`shopizer/`](shopizer/) | The real Shopizer backend (Java, 1,173 source files): 315 files, one concept per package, a `routes.md` with all 325 routes and their handlers, and each type's fields. About 4 MB. The experiment used a copy with the question-relevant identifiers renamed; this one is unmodified. |
| [`invoice-service/`](invoice-service/) | The consuming repository, with the library's bundle mirrored under `okf/references/ledger-lib/` and its links rewritten to stay inside the mirror. |

## Reading a concept

Open `okf/index.md`, then a module such as [`click/okf/modules/click.core.md`](click/okf/modules/click.core.md). The frontmatter follows OKF v0.2 (`type`, `title`, `description`, `resource`, `tags`, `generated`, `sources`, `status`), and every body line ends with the `path:line` it came from. All four bundles pass [`scripts/check_okf.py`](../scripts/check_okf.py) with no findings; see [CONFORMANCE.md](../docs/CONFORMANCE.md) for what that means and the deviations that remain.

## Reproducing one

```bash
kgen sync --repo R
kgen okf --repo R --out R/okf --pointer R/AGENTS.md
# optionally:  --source-url 'https://github.com/OWNER/REPO/blob/COMMIT/{path}'   (default: read from git origin)
#              --stale-against CHECKOUT   or   --reference NAME=BUNDLE_DIR
python scripts/check_okf.py R/okf        # from this repository
```

`kgen okf` is not released yet. The change is in [`../scripts/kgen-okf.patch`](../scripts/kgen-okf.patch), which applies to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at `dd26ee6`; the steps are in the [main README](../README.md#reproducing).
