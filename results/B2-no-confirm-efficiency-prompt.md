# Trial report: okf-flags-v2

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 20 | 19/20 | 59k (51k to 67k) | 1.00 | baseline | 2.5 | - | 14 |
| noflag | 20 | 11/20 | 79k (68k to 91k) | 1.42 (1.23 to 1.64) | dearer | 3.4 | 20/20 | 18 |
| native | 20 | 11/20 | 69k (61k to 77k) | 1.25 (1.07 to 1.44) | dearer | 2.9 | 20/20 | 17 |
| tags | 20 | 11/20 | 70k (61k to 81k) | 1.31 (1.05 to 1.63) | dearer | 2.9 | 20/20 | 17 |
| banner | 20 | 8/20 | 72k (61k to 85k) | 1.28 (1.10 to 1.48) | dearer | 3.1 | 20/20 | 16 |
| all | 20 | 12/20 | 73k (64k to 82k) | 1.32 (1.12 to 1.56) | dearer | 3.0 | 20/20 | 19 |
| targeted | 20 | 15/20 | 71k (65k to 79k) | 1.29 (1.13 to 1.45) | dearer | 3.0 | 20/20 | 16 |
| blanket | 20 | 14/20 | 75k (67k to 86k) | 1.34 (1.17 to 1.55) | dearer | 3.1 | 20/20 | 17 |

Run-to-run spread (coefficient of variation of relative cost) is 0.36. To detect a 20% difference with 80% power you would need about **52 runs per arm** (larger differences need fewer); this trial has 20.

## Tokens by question (mean, thousands)

| question | codex/all | codex/banner | codex/blanket | codex/native | codex/noflag | codex/none | codex/tags | codex/targeted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| callers | 53k | 62k | 68k | 63k | 72k | 55k | 59k | 73k |
| complete | 70k | 52k | 78k | 51k | 57k | 74k | 51k | 81k |
| getdefault | 81k | 103k | 78k | 80k | 97k | 75k | 83k | 71k |
| inherit | 64k | 54k | 56k | 57k | 59k | 31k | 69k | 57k |
| where | 95k | 89k | 97k | 92k | 112k | 60k | 91k | 74k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

