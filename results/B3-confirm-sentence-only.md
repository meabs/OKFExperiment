# Trial report: okf-flags-v3

Baseline arm: **noflag_confirm**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| noflag_confirm | 20 | 19/20 | 77k (70k to 84k) | 1.00 | baseline | 3.1 | 20/20 | 17 |

## Tokens by question (mean, thousands)

| question | codex/noflag_confirm |
| --- | --- |
| callers | 65k |
| complete | 91k |
| getdefault | 68k |
| inherit | 74k |
| where | 86k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

