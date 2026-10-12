# Trial report: okf-config

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 24 | 15/15 (verified 9/9) | 139k (100k to 183k) | 1.00 | baseline | 4.7 | - | 25 |
| minimal | 24 | 15/15 (verified 9/9) | 173k (131k to 221k) | 1.42 (1.25 to 1.59) | dearer | 5.9 | 24/24 | 34 |
| nocalls | 24 | 14/15 (verified 9/9) | 155k (114k to 197k) | 1.21 (1.08 to 1.37) | dearer | 4.7 | 24/24 | 28 |
| default | 24 | 15/15 (verified 9/9) | 167k (122k to 216k) | 1.30 (1.14 to 1.47) | dearer | 5.1 | 24/24 | 32 |
| allcalls | 24 | 15/15 (verified 9/9) | 176k (126k to 228k) | 1.30 (1.18 to 1.43) | dearer | 4.9 | 24/24 | 27 |
| package | 24 | 14/15 (verified 8/9) | 167k (121k to 217k) | 1.26 (1.13 to 1.40) | dearer | 4.9 | 24/24 | 26 |
| noindex | 24 | 15/15 (verified 9/9) | 168k (117k to 225k) | 1.22 (1.08 to 1.38) | dearer | 5.3 | 24/24 | 30 |
| graph | 24 | 15/15 (verified 9/9) | 159k (110k to 216k) | 1.15 (1.03 to 1.28) | dearer | 5.1 | 23/24 | 27 |

Run-to-run spread (coefficient of variation of relative cost) is 0.29. To detect a 20% difference with 80% power you would need about **35 runs per arm** (larger differences need fewer); this trial has 24.

## Tokens by question (mean, thousands)

| question | codex/allcalls | codex/default | codex/graph | codex/minimal | codex/nocalls | codex/noindex | codex/none | codex/package |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| callers | 62k | 72k | 49k | 83k | 61k | 62k | 67k | 62k |
| complete | 96k | 84k | 111k | 114k | 101k | 90k | 85k | 123k |
| getdefault | 88k | 69k | 90k | 101k | 81k | 85k | 71k | 94k |
| inherit | 61k | 63k | 49k | 82k | 73k | 67k | 36k | 64k |
| t1 | 328k | 275k | 247k | 216k | 243k | 288k | 218k | 268k |
| t2 | 348k | 368k | 346k | 352k | 304k | 425k | 302k | 373k |
| t3 | 348k | 303k | 325k | 355k | 310k | 268k | 286k | 299k |
| where | 77k | 105k | 56k | 86k | 63k | 57k | 50k | 56k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

