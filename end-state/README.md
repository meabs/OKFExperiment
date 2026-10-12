# End-state bundles

The recommended output, generated with `kgen okf --preset recommended` (see [../docs/RECOMMENDATIONS.md](../docs/RECOMMENDATIONS.md)). Each folder has the bundle (`okf/`) and the `AGENTS.md` pointer that goes beside it. The pointer's last sentence ("read the source to confirm before you rely on it") is the part the experiments found to matter.

| Folder | What it is |
| --- | --- |
| [`click/`](click/) | Click at the pinned commit `2247b35`. 33 concept files, one per module. |
| [`click-after-drift/`](click-after-drift/) | The same bundle checked against the refactored Click (`kgen okf --stale-against`): the two concepts whose source changed (`click.core`, `click.shell_completion`) carry a past `stale_after`, and the pointer says what that means. |
| [`ledger-lib/`](ledger-lib/) | The library repository of the cross-repo pair. |
| [`invoice-service/`](invoice-service/) | The consuming repository, with the library's bundle mirrored under `okf/references/ledger-lib/` and its links rewritten to stay inside the mirror. |

## Reading a concept

Open `okf/index.md`, then a module such as [`click/okf/modules/click.core.md`](click/okf/modules/click.core.md). The frontmatter follows OKF v0.2 (`type`, `title`, `description`, `resource`, `generated`, `sources`, `status`), and every body line ends with the `path:line` it came from.

## Reproducing one

```bash
kgen sync --repo R
kgen okf --repo R --out R/okf --pointer R/AGENTS.md
# optionally:  --stale-against CHECKOUT   or   --reference NAME=BUNDLE_DIR
```

`kgen okf` is not released yet. The change is in [`../scripts/kgen-okf.patch`](../scripts/kgen-okf.patch), which applies to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at `dd26ee6`; the steps are in the [main README](../README.md#reproducing).
