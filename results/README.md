# Raw reports

> **Terms.** A *bundle* is OKF's name for a generated guide to a codebase: a folder of markdown files, one per module or package, listing what it contains and where each fact came from. The [main README](../README.md) calls it a *guide*.

Each file is the unedited report AgentTrialRig produced for one trial. "Relative cost" is each run's tokens divided by the no-bundle (or stated baseline) mean for the same question; 1.00 means equal, lower is cheaper. The write-up that interprets them is [../docs/RESULTS.md](../docs/RESULTS.md).

| File | Trial | Runs | Notes |
| --- | --- | --- | --- |
| [A-v1-pointer-told-agent-to-confirm.md](A-v1-pointer-told-agent-to-confirm.md) | A: bundle shape, 8 arms | 192 | The agent-file pointer told the agent to confirm in the source. |
| [A2-no-confirm-sentence.md](A2-no-confirm-sentence.md) | A: bundle shape, 5 arms | 120 | Rerun without that sentence. |
| [B-v1-pointer-told-agent-to-confirm.md](B-v1-pointer-told-agent-to-confirm.md) | B: confidence flags, 8 arms | 160 | Same sentence in every arm, so the flags could not be compared. The report's own "correct" column does not count stale-following; see RESULTS.md. |
| [B2-no-confirm-efficiency-prompt.md](B2-no-confirm-efficiency-prompt.md) | B: confidence flags, 8 arms | 160 | No sentence, and an efficiency prompt. The stale-following counts come from `scripts/analyse_b.py`, not from this report. |
| [B3-confirm-sentence-only.md](B3-confirm-sentence-only.md) | B: the sentence alone | 20 | The "no flags" bundle with the sentence added; same prompt as B2. Its baseline is that arm. |
| [C2-cross-repo.md](C2-cross-repo.md) | C: cross-repo, 6 arms | 72 | Change tasks only, so there is no "correct" column; the verified count is in the first column. |
| [D1-cross-repo-fresh-shopizer.md](D1-cross-repo-fresh-shopizer.md) | D: unreadable dependency, bundle current, 4 arms | 96 | Storefront as the working repo, backend renamed. `scripts/leak_check.py` found 3 of 24 no-backend runs that searched the disk. |
| [D2-cross-repo-stale-shopizer.md](D2-cross-repo-stale-shopizer.md) | D: unreadable dependency, bundle stale, 4 arms | 128 | The report's "correct" column mixes drift and control questions; the stale-following counts come from `scripts/analyse_d2.py`. Efficiency prompt. |
| [E-confidence-labels-crossrepo-questions.md](E-confidence-labels-crossrepo-questions.md) | E: cross-repo questions with wrong entries, 4 conditions | 112 | The report's "correct" column counts true answers; followed-wrong and disclosure counts come from `scripts/analyse_e.py`. |
| [F-crossrepo-change-tasks.md](F-crossrepo-change-tasks.md) | F: cross-repo change tasks, 3 conditions | 60 | The "verified" count is the number of changes that passed their hidden test. |
| [G-harder-crossrepo-change-tasks.md](G-harder-crossrepo-change-tasks.md) | G: harder cross-repo change tasks, 4 conditions | 80 | Includes a condition where the backend source is readable. The per-task counts are in `docs/RESULTS.md`. |
| [H1-contract-vs-okf-changes.md](H1-contract-vs-okf-changes.md) | H1: the G changes with five arms (none, contract, note, guide, source) | 80 | Network on. Two `none` runs cloned the public repository. |
| [H2-contract-vs-okf-questions.md](H2-contract-vs-okf-questions.md) | H2: six call-structure questions, five arms | 120 | Network on. 56 runs cloned the public Shopizer repository; the report repeats the table without them. |
| [H3-runnable-service.md](H3-runnable-service.md) | H3: four changes against a runnable FastAPI service, five arms | 80 | Contaminated: 15 non-source runs opened the service, the tests or other arms' files. The report repeats the table for clean runs only. An earlier, more contaminated run of this part is not reported. |

A first cross-repo run used the v1 pointer and was stopped part-way; it is not reported.

To count stale-following yourself: `python scripts/analyse_b.py <results folder>` (B) `python scripts/analyse_d2.py <results folder>` (D2) or `python scripts/analyse_e.py <results folder>` (E); for H, `python scripts/analyse_h.py <results folder> [--exclude REGEX]` and `python scripts/net_check.py <results folder>`. To count runs that reached outside their own workspace: `python scripts/leak_check.py <results folder>`.

| `archive/H3-first-run-contaminated.tgz` | First H3 run (service in a findable folder; 14 of 64 non-source runs opened it). Kept for the record, not reported. |
