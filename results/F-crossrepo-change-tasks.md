# Trial report: crossrepo-change

Baseline arm: **no_okf**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no_okf | 20 | - (verified 3/20) | 482k (301k to 681k) | 1.00 | baseline | 5.0 | - | 48 |
| okf | 20 | - (verified 19/20) | 242k (203k to 286k) | 0.80 (0.51 to 1.15) | no clear difference | 5.2 | 20/20 | 27 |
| okf_confidence | 20 | - (verified 15/20) | 235k (205k to 270k) | 0.74 (0.51 to 1.02) | no clear difference | 5.2 | 20/20 | 30 |

Run-to-run spread (coefficient of variation of relative cost) is 0.87. To detect a 20% difference with 80% power you would need about **296 runs per arm** (larger differences need fewer); this trial has 20.

## Tokens by question (mean, thousands)

| question | codex/no_okf | codex/okf | codex/okf_confidence |
| --- | --- | --- | --- |
| f1_cart_request | 652k | 165k | 193k |
| f2_search_request | 357k | 221k | 242k |
| f3_reviews_request | 130k | 247k | 210k |
| f4_store_config | 790k | 335k | 294k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

