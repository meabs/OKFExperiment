# Trial report: rename-in-big-repo

Baseline arm: **plain**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| plain | 32 | - (verified 22/32) | 267k (234k to 302k) | 1.00 | baseline | 7.4 | - | 42 |
| guide | 32 | - (verified 24/32) | 318k (278k to 360k) | 1.22 (1.07 to 1.37) | dearer | 7.2 | 32/32 | 45 |

Run-to-run spread (coefficient of variation of relative cost) is 0.38. To detect a 20% difference with 80% power you would need about **56 runs per arm** (larger differences need fewer); this trial has 32.

## Tokens by question (mean, thousands)

| question | codex/guide | codex/plain |
| --- | --- | --- |
| i1_rename_findOne | 305k | 302k |
| i2_rename_cart_save | 421k | 292k |
| i3_rename_config_save | 275k | 291k |
| i4_rename_toLocale | 269k | 182k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.


## Analysis (`python scripts/analyse_i.py`)

```
plain: passed 22 of 32; tokens 267k; network runs 0; runs naming a path outside the workspace 0; runs with a blocked access 6
guide: passed 24 of 32; tokens 318k; network runs 0; runs naming a path outside the workspace 3; runs with a blocked access 5
overall plain 22/32 against guide 24/32: p = 0.782

| Task | plain | guide |
| --- | --- | --- |
| i1_rename_findOne | 8/8 | 7/8 |
| i2_rename_cart_save | 2/8 | 3/8 |
| i3_rename_config_save | 5/8 | 6/8 |
| i4_rename_toLocale | 7/8 | 8/8 |
```
