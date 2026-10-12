# Trial report: h2-contract-vs-okf-questions

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 24 | 1/24 | 447k (385k to 509k) | 1.00 | baseline | 7.2 | - | 53 |
| contract | 24 | 8/24 | 464k (401k to 535k) | 1.10 (0.91 to 1.29) | no clear difference | 7.9 | 24/24 | 57 |
| notes | 24 | 0/24 | 476k (413k to 550k) | 1.13 (0.93 to 1.37) | no clear difference | 7.8 | 24/24 | 52 |
| okf | 24 | 21/24 | 170k (155k to 186k) | 0.40 (0.35 to 0.46) | cheaper | 4.6 | 24/24 | 22 |
| source | 24 | 21/24 | 207k (181k to 234k) | 0.47 (0.42 to 0.52) | cheaper | 5.3 | 23/24 | 28 |

Run-to-run spread (coefficient of variation of relative cost) is 0.66. To detect a 20% difference with 80% power you would need about **169 runs per arm** (larger differences need fewer); this trial has 24.

## Tokens by question (mean, thousands)

| question | codex/contract | codex/none | codex/notes | codex/okf | codex/source |
| --- | --- | --- | --- | --- | --- |
| h2_e1_login | 305k | 487k | 337k | 146k | 214k |
| h2_e2_search | 450k | 254k | 500k | 166k | 136k |
| h2_e3_cart_delete | 443k | 472k | 487k | 148k | 156k |
| h2_e4_cart_add | 569k | 484k | 421k | 196k | 265k |
| h2_e5_shipping | 514k | 515k | 692k | 198k | 272k |
| h2_e7_register | 501k | 471k | 421k | 164k | 201k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.


## Pass counts and pairwise tests (scripts/analyse_h.py)

**All 120 runs**

| Arm | Passed | Tokens per run | Against `none` |
| --- | --- | --- | --- |
| `none` | 1 of 24 | 447k | 1.00 |
| `contract` | 8 of 24 | 464k | 1.04 |
| `notes` | 0 of 24 | 476k | 1.07 |
| `okf` | 21 of 24 | 170k | 0.38 |
| `source` | 21 of 24 | 207k | 0.46 |

Pairs (two-sided Fisher exact):

- `contract` 8/24 against `okf` 21/24: p = 0.000 (reliable)
- `notes` 0/24 against `okf` 21/24: p = 0.000 (reliable)
- `okf` 21/24 against `source` 21/24: p = 1.000
- `contract` 8/24 against `notes` 0/24: p = 0.004 (reliable)
- `none` 1/24 against `contract` 8/24: p = 0.023 (reliable)
- `none` 1/24 against `okf` 21/24: p = 0.000 (reliable)

Per task (passed of runs):

| Task | `none` | `contract` | `notes` | `okf` | `source` |
| --- | --- | --- | --- | --- | --- |
| h2_e1_login | 0/4 | 3/4 | 0/4 | 4/4 | 4/4 |
| h2_e2_search | 1/4 | 1/4 | 0/4 | 4/4 | 4/4 |
| h2_e3_cart_delete | 0/4 | 2/4 | 0/4 | 4/4 | 4/4 |
| h2_e4_cart_add | 0/4 | 0/4 | 0/4 | 1/4 | 3/4 |
| h2_e5_shipping | 0/4 | 0/4 | 0/4 | 4/4 | 2/4 |
| h2_e7_register | 0/4 | 2/4 | 0/4 | 4/4 | 4/4 |

Runs that used the network: 56 of 120 {'contract': 18, 'notes': 19, 'none': 19}

**Without the 56 network runs**

| Arm | Passed | Tokens per run | Against `none` |
| --- | --- | --- | --- |
| `none` | 1 of 5 | 259k | 1.00 |
| `contract` | 0 of 6 | 368k | 1.42 |
| `notes` | 0 of 5 | 351k | 1.35 |
| `okf` | 21 of 24 | 170k | 0.65 |
| `source` | 21 of 24 | 207k | 0.80 |

Pairs (two-sided Fisher exact):

- `contract` 0/6 against `okf` 21/24: p = 0.000 (reliable)
- `notes` 0/5 against `okf` 21/24: p = 0.000 (reliable)
- `okf` 21/24 against `source` 21/24: p = 1.000
- `contract` 0/6 against `notes` 0/5: p = 1.000
- `none` 1/5 against `contract` 0/6: p = 0.455
- `none` 1/5 against `okf` 21/24: p = 0.007 (reliable)
