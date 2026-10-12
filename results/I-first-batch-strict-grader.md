# Experiment I, first batch (discarded: exact whole-file grader)

Graded with a rule that counted a removed blank line at the end of a file as a wrong edit; task i1 failed in all 16 runs for that reason. See Deviations in docs/EXPERIMENT_I.md. Kept for the record; the reported results are in I-rename-in-large-repo.md.

# Trial report: rename-in-big-repo

Baseline arm: **plain**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| plain | 32 | - (verified 15/32) | 251k (226k to 276k) | 1.00 | baseline | 7.2 | - | 44 |
| guide | 32 | - (verified 14/32) | 327k (293k to 364k) | 1.32 (1.20 to 1.45) | dearer | 7.5 | 32/32 | 49 |

Run-to-run spread (coefficient of variation of relative cost) is 0.28. To detect a 20% difference with 80% power you would need about **32 runs per arm** (larger differences need fewer); this trial has 32.

## Tokens by question (mean, thousands)

| question | codex/guide | codex/plain |
| --- | --- | --- |
| i1_rename_findOne | 379k | 243k |
| i2_rename_cart_save | 384k | 334k |
| i3_rename_config_save | 307k | 237k |
| i4_rename_toLocale | 240k | 190k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

