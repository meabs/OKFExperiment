# Raw reports

Each file is the unedited report AgentTrialRig produced for one trial. "Relative cost" is each run's tokens divided by the no-bundle (or stated baseline) mean for the same question; 1.00 means equal, lower is cheaper. The write-up that interprets them is [../docs/RESULTS.md](../docs/RESULTS.md).

| File | Trial | Runs | Notes |
| --- | --- | --- | --- |
| [A-v1-pointer-told-agent-to-confirm.md](A-v1-pointer-told-agent-to-confirm.md) | A: bundle shape, 8 arms | 192 | The agent-file pointer told the agent to confirm in the source. |
| [A2-no-confirm-sentence.md](A2-no-confirm-sentence.md) | A: bundle shape, 5 arms | 120 | Rerun without that sentence. |
| [B-v1-pointer-told-agent-to-confirm.md](B-v1-pointer-told-agent-to-confirm.md) | B: confidence flags, 8 arms | 160 | Same sentence in every arm, so the flags could not be compared. The report's own "correct" column does not count stale-following; see RESULTS.md. |
| [B2-no-confirm-efficiency-prompt.md](B2-no-confirm-efficiency-prompt.md) | B: confidence flags, 8 arms | 160 | No sentence, and an efficiency prompt. The stale-following counts come from `scripts/analyse_b.py`, not from this report. |
| [B3-confirm-sentence-only.md](B3-confirm-sentence-only.md) | B: the sentence alone | 20 | The "no flags" bundle with the sentence added; same prompt as B2. Its baseline is that arm. |
| [C2-cross-repo.md](C2-cross-repo.md) | C: cross-repo, 6 arms | 72 | Change tasks only, so there is no "correct" column; the verified count is in the first column. |

A first cross-repo run used the v1 pointer and was stopped part-way; it is not reported.

To count stale-following yourself: `python scripts/analyse_b.py <results folder>`.
