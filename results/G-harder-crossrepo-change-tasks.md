# Trial report: crossrepo-change-hard

Baseline arm: **no_okf**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no_okf | 20 | - (verified 3/20) | 294k (235k to 366k) | 1.00 | baseline | 6.3 | - | 42 |
| source | 20 | - (verified 18/20) | 333k (284k to 389k) | 1.16 (1.02 to 1.31) | dearer | 7.3 | 19/20 | 45 |
| okf | 20 | - (verified 18/20) | 301k (257k to 351k) | 1.12 (0.89 to 1.39) | no clear difference | 6.7 | 20/20 | 38 |
| okf_confidence | 20 | - (verified 17/20) | 308k (267k to 353k) | 1.10 (0.94 to 1.29) | no clear difference | 7.7 | 20/20 | 38 |

Run-to-run spread (coefficient of variation of relative cost) is 0.41. To detect a 20% difference with 80% power you would need about **66 runs per arm** (larger differences need fewer); this trial has 20.

## Tokens by question (mean, thousands)

| question | codex/no_okf | codex/okf | codex/okf_confidence | codex/source |
| --- | --- | --- | --- | --- |
| g1_delete_item | 399k | 259k | 304k | 313k |
| g2_add_voucher | 237k | 378k | 278k | 295k |
| g3_checkout_request | 342k | 292k | 381k | 490k |
| g4_orders_list | 197k | 274k | 269k | 234k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

