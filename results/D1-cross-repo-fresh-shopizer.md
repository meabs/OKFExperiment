# Trial report: shopizer-crossrepo-fresh

Baseline arm: **none**. Relative cost is each run's tokens divided by the baseline's mean for the same question; 1.00 means equal, lower is cheaper.

## codex

| arm | runs | correct | tokens per run (95% CI) | relative cost (95% CI) | verdict | turns | used tool | seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | 24 | 1/24 | 785k (513k to 1118k) | 1.00 | baseline | 4.2 | - | 60 |
| source | 24 | 24/24 | 181k (155k to 212k) | 0.43 (0.25 to 0.65) | cheaper | 4.4 | 24/24 | 24 |
| bundle_sent | 24 | 24/24 | 189k (161k to 219k) | 0.41 (0.26 to 0.61) | cheaper | 4.9 | 24/24 | 22 |
| bundle_nosent | 24 | 24/24 | 169k (138k to 208k) | 0.34 (0.24 to 0.45) | cheaper | 4.5 | 24/24 | 21 |

Run-to-run spread (coefficient of variation of relative cost) is 1.08. To detect a 20% difference with 80% power you would need about **461 runs per arm** (larger differences need fewer); this trial has 24.

## Tokens by question (mean, thousands)

| question | codex/bundle_nosent | codex/bundle_sent | codex/none | codex/source |
| --- | --- | --- | --- | --- |
| x1_cart_add | 157k | 187k | 1613k | 178k |
| x2_cart_update | 140k | 189k | 683k | 169k |
| x3_cart_delete | 90k | 142k | 576k | 148k |
| x4_login | 172k | 119k | 393k | 182k |
| x5_search | 160k | 172k | 575k | 104k |
| x6_config | 202k | 242k | 1631k | 214k |
| x7_reviews | 93k | 152k | 103k | 167k |
| x8_shipping | 339k | 310k | 704k | 284k |

Token totals are not comparable between agents (see adapters.py). Treat a verdict as evidence only when the interval excludes 1.00, and as provisional below 8 runs per arm.

