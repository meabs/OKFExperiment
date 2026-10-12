# Trial report: okf-crossrepo-v2

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 12 | - (verified 12/12) | 146k (122k to 174k) | 1.00 | baseline | 5.3 | - | 40 |
| source | 12 | - (verified 12/12) | 182k (157k to 211k) | 1.28 (1.11 to 1.47) | dearer | 5.8 | 11/12 | 51 |
| fresh | 12 | - (verified 12/12) | 175k (159k to 191k) | 1.25 (1.09 to 1.40) | dearer | 5.9 | 12/12 | 55 |
| fresh_tags | 12 | - (verified 12/12) | 183k (152k to 217k) | 1.25 (1.11 to 1.39) | dearer | 6.4 | 12/12 | 39 |
| stale | 12 | - (verified 12/12) | 151k (132k to 172k) | 1.05 (0.96 to 1.12) | no clear difference | 5.3 | 12/12 | 38 |
| stale_tags | 12 | - (verified 12/12) | 157k (135k to 183k) | 1.10 (0.96 to 1.25) | no clear difference | 5.4 | 12/12 | 31 |

Run-to-run spread (coefficient of variation of relative cost) is 0.23. To detect a 20% difference with 80% power you would need about **22 runs per arm** (larger differences need fewer); this trial has 12.

## Tokens by question (mean, thousands)

| question | codex/fresh | codex/fresh_tags | codex/none | codex/source | codex/stale | codex/stale_tags |
| --- | --- | --- | --- | --- | --- | --- |
| c1 | 185k | 153k | 144k | 210k | 154k | 156k |
| c2 | 180k | 254k | 190k | 195k | 185k | 185k |
| c3 | 159k | 142k | 104k | 141k | 115k | 131k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

