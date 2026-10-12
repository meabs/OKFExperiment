# Trial report: okf-config-v2

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 24 | 14/15 (verified 9/9) | 143k (106k to 182k) | 1.00 | baseline | 4.8 | - | 28 |
| minimal | 24 | 15/15 (verified 9/9) | 181k (130k to 237k) | 1.26 (1.14 to 1.39) | dearer | 5.9 | 24/24 | 29 |
| nocalls | 24 | 15/15 (verified 9/9) | 164k (115k to 215k) | 1.10 (0.97 to 1.25) | no clear difference | 5.0 | 24/24 | 25 |
| default | 24 | 15/15 (verified 9/9) | 161k (114k to 208k) | 1.07 (0.99 to 1.16) | no clear difference | 4.8 | 24/24 | 29 |
| graph | 24 | 15/15 (verified 9/9) | 182k (120k to 252k) | 1.14 (0.99 to 1.32) | no clear difference | 5.6 | 24/24 | 31 |

Run-to-run spread (coefficient of variation of relative cost) is 0.30. To detect a 20% difference with 80% power you would need about **35 runs per arm** (larger differences need fewer); this trial has 24.

## Tokens by question (mean, thousands)

| question | codex/default | codex/graph | codex/minimal | codex/nocalls | codex/none |
| --- | --- | --- | --- | --- | --- |
| callers | 66k | 56k | 69k | 55k | 82k |
| complete | 86k | 132k | 111k | 113k | 97k |
| getdefault | 80k | 94k | 96k | 68k | 78k |
| inherit | 56k | 49k | 71k | 63k | 47k |
| t1 | 286k | 239k | 253k | 324k | 220k |
| t2 | 315k | 418k | 354k | 312k | 293k |
| t3 | 332k | 418k | 405k | 310k | 268k |
| where | 64k | 49k | 91k | 67k | 61k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

