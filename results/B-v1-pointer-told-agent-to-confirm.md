# Trial report: okf-flags

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 20 | 20/20 | 62k (53k to 74k) | 1.00 | baseline | 2.4 | - | 14 |
| noflag | 20 | 19/20 | 68k (60k to 77k) | 1.15 (0.98 to 1.32) | no clear difference | 2.7 | 20/20 | 16 |
| native | 20 | 19/20 | 65k (58k to 74k) | 1.09 (0.95 to 1.24) | no clear difference | 2.5 | 20/20 | 17 |
| tags | 20 | 20/20 | 73k (64k to 84k) | 1.23 (1.04 to 1.44) | dearer | 2.8 | 20/20 | 17 |
| banner | 20 | 19/20 | 73k (65k to 82k) | 1.22 (1.07 to 1.40) | dearer | 2.8 | 20/20 | 16 |
| all | 20 | 20/20 | 67k (61k to 72k) | 1.14 (0.97 to 1.34) | no clear difference | 2.6 | 20/20 | 16 |
| targeted | 20 | 20/20 | 76k (69k to 83k) | 1.30 (1.12 to 1.49) | dearer | 3.0 | 20/20 | 20 |
| blanket | 20 | 19/20 | 71k (65k to 77k) | 1.21 (1.05 to 1.40) | dearer | 2.7 | 20/20 | 16 |

Run-to-run spread (coefficient of variation of relative cost) is 0.34. To detect a 20% difference with 80% power you would need about **46 runs per arm** (larger differences need fewer); this trial has 20.

## Tokens by question (mean, thousands)

| question | codex/all | codex/banner | codex/blanket | codex/native | codex/noflag | codex/none | codex/tags | codex/targeted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| callers | 55k | 62k | 59k | 55k | 63k | 75k | 63k | 60k |
| complete | 80k | 93k | 78k | 91k | 80k | 66k | 99k | 85k |
| getdefault | 70k | 90k | 75k | 71k | 58k | 77k | 70k | 81k |
| inherit | 67k | 62k | 68k | 56k | 52k | 38k | 63k | 70k |
| where | 60k | 61k | 74k | 55k | 87k | 55k | 70k | 84k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

