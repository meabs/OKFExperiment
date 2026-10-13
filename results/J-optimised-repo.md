# Trial report: optimised-repo

> **Read this first.** The trialrig table below counts j7 with the first grader (0 of 8 in each arm). That grader missed four AspectJ pointcut strings that every run had correctly updated, so the reported j7 figures are the re-scored ones in the analysis at the end (plain 4 of 8, optimised 6 of 8; changes 28 and 29 of 32). See Deviations in docs/EXPERIMENT_J.md.

Baseline arm: **plain**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| plain | 56 | 16/24 (verified 24/32) | 297k (219k to 388k) | 1.00 | baseline | 5.9 | - | 45 |
| optimised | 56 | 19/24 (verified 23/32) | 401k (304k to 511k) | 1.48 (1.38 to 1.60) | dearer | 8.8 | 56/56 | 68 |

Run-to-run spread (coefficient of variation of relative cost) is 0.29. To detect a 20% difference with 80% power you would need about **33 runs per arm** (larger differences need fewer); this trial has 56.

## Tokens by question (mean, thousands)

| question | codex/optimised | codex/plain |
| --- | --- | --- |
| j1_rename_payment_method | 188k | 117k |
| j2_add_param_to_overload | 359k | 235k |
| j3_remove_unused_param | 277k | 231k |
| j4_overload_callers | 186k | 98k |
| j5_shipping_chain | 220k | 150k |
| j6_checkout_path | 297k | 203k |
| j7_rename_entity_delete | 1278k | 1046k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.


## Analysis (`python scripts/analyse_j.py`, with j7 re-scored by `scripts/regrade_j.py`)

```
## changes
plain 28/32 (407k tokens); optimised 29/32 (526k, 1.29 times); p = 1.000
| Task | plain | optimised | tokens plain | tokens optimised |
| --- | --- | --- | --- | --- |
| j1_rename_payment_method | 8/8 | 8/8 | 117k | 188k |
| j2_add_param_to_overload | 8/8 | 7/8 | 235k | 359k |
| j3_remove_unused_param | 8/8 | 8/8 | 231k | 277k |
| j7_rename_entity_delete | 4/8 | 6/8 | 1046k | 1278k |

## questions
plain 16/24 (150k tokens); optimised 19/24 (234k, 1.56 times); p = 0.517
| Task | plain | optimised | tokens plain | tokens optimised |
| --- | --- | --- | --- | --- |
| j4_overload_callers | 1/8 | 3/8 | 98k | 186k |
| j5_shipping_chain | 7/8 | 8/8 | 150k | 220k |
| j6_checkout_path | 8/8 | 8/8 | 203k | 297k |

Adoption in the optimised arm (56 runs): ran kg 56; opened okf/ 56; read navigate 55, change 32, check 34; read no skill 0
plain: network runs 0; runs with a refused access 4
optimised: network runs 0; runs with a refused access 6
optimised runs that used kg: passed 48 of 56; did not: 0 of 0
```
