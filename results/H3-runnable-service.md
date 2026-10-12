# Trial report: h3-contract-vs-okf-service

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 16 | - (verified 11/16) | 486k (247k to 900k) | 1.00 | baseline | 10.5 | - | 84 |
| contract | 16 | - (verified 11/16) | 303k (219k to 403k) | 0.78 (0.65 to 0.93) | cheaper | 9.1 | 16/16 | 59 |
| notes | 16 | - (verified 10/16) | 255k (168k to 390k) | 0.67 (0.54 to 0.78) | cheaper | 7.7 | 16/16 | 48 |
| okf | 16 | - (verified 15/16) | 345k (244k to 465k) | 0.90 (0.73 to 1.10) | no clear difference | 10.2 | 16/16 | 71 |
| source | 16 | - (verified 16/16) | 173k (155k to 192k) | 0.60 (0.44 to 0.75) | cheaper | 6.1 | 16/16 | 37 |

Run-to-run spread (coefficient of variation of relative cost) is 0.45. To detect a 20% difference with 80% power you would need about **81 runs per arm** (larger differences need fewer); this trial has 16.

## Tokens by question (mean, thousands)

| question | codex/contract | codex/none | codex/notes | codex/okf | codex/source |
| --- | --- | --- | --- | --- | --- |
| h3_1_fetch_all | 205k | 269k | 178k | 179k | 154k |
| h3_2_retry | 237k | 223k | 175k | 243k | 180k |
| h3_3_errors | 183k | 220k | 186k | 288k | 190k |
| h3_4_preview | 586k | 1233k | 481k | 668k | 168k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.


## Pass counts and pairwise tests (scripts/analyse_h.py)

**All 80 runs**

| Arm | Passed | Tokens per run | Against `none` |
| --- | --- | --- | --- |
| `none` | 11 of 16 | 486k | 1.00 |
| `contract` | 11 of 16 | 303k | 0.62 |
| `notes` | 10 of 16 | 255k | 0.52 |
| `okf` | 15 of 16 | 345k | 0.71 |
| `source` | 16 of 16 | 173k | 0.36 |

Pairs (two-sided Fisher exact):

- `contract` 11/16 against `okf` 15/16: p = 0.172
- `notes` 10/16 against `okf` 15/16: p = 0.083
- `okf` 15/16 against `source` 16/16: p = 1.000
- `contract` 11/16 against `notes` 10/16: p = 1.000
- `none` 11/16 against `contract` 11/16: p = 1.000
- `none` 11/16 against `okf` 15/16: p = 0.172

Per task (passed of runs):

| Task | `none` | `contract` | `notes` | `okf` | `source` |
| --- | --- | --- | --- | --- | --- |
| h3_1_fetch_all | 3/4 | 4/4 | 4/4 | 3/4 | 4/4 |
| h3_2_retry | 4/4 | 0/4 | 4/4 | 4/4 | 4/4 |
| h3_3_errors | 1/4 | 4/4 | 0/4 | 4/4 | 4/4 |
| h3_4_preview | 3/4 | 3/4 | 2/4 | 4/4 | 4/4 |

Runs that used the network: 1 of 80 {'none': 1}

**Without the 1 network runs**

| Arm | Passed | Tokens per run | Against `none` |
| --- | --- | --- | --- |
| `none` | 11 of 15 | 487k | 1.00 |
| `contract` | 11 of 16 | 303k | 0.62 |
| `notes` | 10 of 16 | 255k | 0.52 |
| `okf` | 15 of 16 | 345k | 0.71 |
| `source` | 16 of 16 | 173k | 0.36 |

Pairs (two-sided Fisher exact):

- `contract` 11/16 against `okf` 15/16: p = 0.172
- `notes` 10/16 against `okf` 15/16: p = 0.083
- `okf` 15/16 against `source` 16/16: p = 1.000
- `contract` 11/16 against `notes` 10/16: p = 1.000
- `none` 11/15 against `contract` 11/16: p = 1.000
- `none` 11/15 against `okf` 15/16: p = 0.172

## Clean runs only (runs that opened the service, tests or other arms were removed)

15 of 80 runs touched paths matching /pricing-service|scratchpad/h|pricing/rules|pricing/app|OKFExperiment|hidden/h|stash|svc_okf|svc_openapi/ {'contract': 4, 'okf': 4, 'notes': 2, 'none': 5}; kept the rest

**All 65 runs**

| Arm | Passed | Tokens per run | Against `none` |
| --- | --- | --- | --- |
| `none` | 7 of 11 | 219k | 1.00 |
| `contract` | 8 of 12 | 210k | 0.96 |
| `notes` | 8 of 14 | 172k | 0.79 |
| `okf` | 11 of 12 | 237k | 1.08 |
| `source` | 16 of 16 | 173k | 0.79 |

Pairs (two-sided Fisher exact):

- `contract` 8/12 against `okf` 11/12: p = 0.317
- `notes` 8/14 against `okf` 11/12: p = 0.081
- `okf` 11/12 against `source` 16/16: p = 0.429
- `contract` 8/12 against `notes` 8/14: p = 0.701
- `none` 7/11 against `contract` 8/12: p = 1.000
- `none` 7/11 against `okf` 11/12: p = 0.155

Per task (passed of runs):

| Task | `none` | `contract` | `notes` | `okf` | `source` |
| --- | --- | --- | --- | --- | --- |
| h3_1_fetch_all | 2/3 | 4/4 | 4/4 | 3/4 | 4/4 |
| h3_2_retry | 4/4 | 0/3 | 4/4 | 4/4 | 4/4 |
| h3_3_errors | 1/4 | 4/4 | 0/4 | 4/4 | 4/4 |
| h3_4_preview | - | 0/1 | 0/2 | - | 4/4 |

Runs that used the network: 0 of 65 {}
