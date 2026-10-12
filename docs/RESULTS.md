# Results

The README organises everything around four conditions: **1. No OKF**, **2. OKF**, **3. OKF with confidence labels** (every fact marked `[high]`, stated in the source, or `[medium]`, a heuristic guess, with an instruction to say when relying on `[medium]`) and **4. cross-repo change with OKF**. Tests A and B use the same repository, C to G cross repositories; F and G are the cross-repo change tests (G the harder one), E the confidence-label test.

> **Terms.** A *bundle* is OKF's name for a generated guide to a codebase: a folder of markdown files, one per module or package, listing what it contains and where each fact came from. The [main README](../README.md) calls it a *guide*.

Codex `gpt-5.6-luna` (medium reasoning), AgentTrialRig 0.6.1. Bundles come from `kgen okf` (deterministic, no language model; [how to get it](../README.md#reproducing)). Raw reports are in [`../results/`](../results/). Read anything under 8 runs per arm as provisional; intervals are 95%.

## A. Which bundle shape? (Click, 5 questions and 3 change tasks)

**Accuracy was at the ceiling in every arm** (questions 14 or 15 of 15, change tasks 8 or 9 of 9 verified, with or without a bundle). So the question is cost.

| arm (what it contains) | v1: pointer told the agent to confirm in source (24 runs/arm) | v2: no such sentence (24 runs/arm) |
| --- | --- | --- |
| none | 1.00 | 1.00 |
| minimal (types and function names only; no citations, links, call edges or index) | 1.42 (1.25-1.59) dearer | 1.26 (1.14-1.39) dearer |
| no call edges | 1.21 (1.08-1.37) dearer | 1.10 (0.97-1.25) no clear difference |
| default (citations, links, cross-module calls, routing index) | 1.30 (1.14-1.47) dearer | 1.07 (0.99-1.16) no clear difference |
| all calls / one concept per package / no index | 1.30 / 1.26 / 1.22, all dearer | not rerun |
| code graph only (`kg`) | 1.15 (1.03-1.28) dearer | 1.14 (0.99-1.32) no clear difference |

Relative cost = tokens divided by the no-bundle mean for the same question (1.00 = equal).

- No bundle beat having none on tokens. The best (default, v2) was level on questions (0.99) and about 21% dearer on change tasks.
- The thinnest bundle was always the dearest: without citations and links the agent still has to search, so the bundle is extra reading.
- Per-package concepts, a missing index and full call edges did not beat the default (v1 only).
- **The "read the source to confirm" sentence moved the cost**: the default arm fell from 1.30 to 1.07 when it was removed. The two runs were not simultaneous, so treat the size as indicative.
- The graph is dearer here because most of these are one-hop lookups, which matches earlier results (it pays off on multi-level callers).

## B. Confidence flags (Click after three planted refactors; the bundle is from before them)

Drifts: a renamed function (`_resolve_context` to `_resolve_completion_context`), a new intermediate base class (`PositionalParameter`) and a call moved behind a helper (`_ordered_params`). Two further questions were unchanged (controls). 12 drift answers per arm (3 questions x 4 runs). "Followed stale" = the answer gives the old fact and not the new one.

**v1 (the pointer told the agent to confirm in source): 1 of 84 drift answers followed a stale claim across all seven bundle arms.** The flags could not be compared, because every arm already had a verification instruction.

**v2 (that sentence removed, and an efficiency prompt: "use the repository knowledge ... avoid unnecessary file reads"):**

| arm | followed stale (of 12) | correct on the 2 control questions | relative cost |
| --- | --- | --- | --- |
| no bundle | 0 | 7/8 | 1.00 |
| bundle, no flags | **8** | 7/8 | 1.42 |
| + OKF-native fields (`generated`, `sources`, `status`) and a trust-tier sentence | 9 | 8/8 | 1.25 |
| + per-line `[high]/[medium]` tags | 8 | 7/8 | 1.31 |
| + banner telling the reader to check the source | 10 | 6/8 | 1.28 |
| + tags, banner and `verified` stamps | 8 | 8/8 | 1.32 |
| + `stale_after` only on concepts whose source changed | 5 | 8/8 | 1.29 |
| + `stale_after` on every concept | 6 | 8/8 | 1.34 |

- An unflagged bundle is harmful under efficiency pressure: 8/12 against 0/12 with no bundle (Fisher exact, two-sided p about 0.001).
- Tags, banners and OKF-native provenance did not help (pooled 26/36 against 8/12, p = 0.77). The banner arm was the worst.
- `stale_after` helped a little: 11/24 against 43/60 for the arms without it (one-sided, post-hoc pooled, p = 0.025). Targeted against no flags was 5/12 against 8/12 (p = 0.21). Suggestive, not settled.
- The renamed function was followed most often: agents answered from the bundle without searching for the new name.

**B3, the clean test of the sentence** (same bundle as "no flags", same efficiency prompt, one sentence added to the pointer: "read the source to confirm before you rely on it"): **0 of 12 followed stale, against 8 of 12 without it** (p about 0.001), at the same cost (77k against 79k tokens). Nothing else changed.

## C. Cross-repo (synthetic: `ledger-lib` and `invoice-service`, 3 change tasks, 12 runs per arm)

| arm | verified | relative cost |
| --- | --- | --- |
| library installed only (nothing said) | 12/12 | 1.00 |
| library source location given | 12/12 | 1.28 (1.11-1.47) dearer |
| library bundle vendored under `okf/references/` | 12/12 | 1.25 (1.09-1.40) dearer |
| the same with tags, banner and `verified` stamps | 12/12 | 1.25 (1.11-1.39) dearer |
| library bundle from an older version (stale) | 12/12 | 1.05 (0.96-1.12) |
| stale, with tags, banner and targeted `stale_after` | 12/12 | 1.10 (0.96-1.25) |

- Everything passed, and no run hit a stale-API error in any arm (0 of 12 each). The library was installed and readable, so the agent could always inspect it, and the other repo's bundle added cost without adding accuracy.
- This does **not** show that cross-repo bundles never help. A dependency the agent cannot read (a private service, a binary) is untested, and the pair is synthetic.

## D. A complex repository as a dependency the agent cannot read

The working repository is the real [Shopizer React storefront](https://github.com/shopizer-ecommerce/shopizer-shop-reactjs). It calls a backend, [Shopizer](https://github.com/shopizer-ecommerce/shopizer) (1,173 Java files, 325 routes), that is **not available** to the agent. Eight questions each trace one storefront call to the backend: the controller method, the request class, and a field or path variable. Examples: the cart POST in `cartActions.js`, the login request in `LoginRegister.js`, the search request, the config request.

**The backend's question-relevant identifiers were renamed** (`scripts/privatize.py`), so the answers cannot come from memory of a famous public repository. A first attempt without this let the agent answer from memory (it found `AuthenticateCustomerApi` unaided); that was caught in a smoke test before any trial run.

### D1. Backend current (96 runs: 8 questions x 4 arms x 3 runs)

| Arm | Correct | Tokens per run (95% CI) | Cost vs no backend |
| --- | --- | --- | --- |
| No backend | **1 / 24** | 785k (513k to 1118k) | 1.00 |
| Backend source checked out (read-only) | 24 / 24 | 181k (155k to 212k) | 0.43 (0.25 to 0.65) |
| Backend bundle, with the confirm sentence | 24 / 24 | 189k (161k to 219k) | 0.41 (0.26 to 0.61) |
| Backend bundle, without it | 24 / 24 | 169k (138k to 208k) | 0.34 (0.24 to 0.45) |

- A bundle gave the same accuracy as the full source at the same cost, and a fraction of what searching blind cost. The "no backend" cost is the cost of failing.
- The intervals on the ratios are wide (the no-backend runs vary from 55k to 3.0M tokens, median 722k); the accuracy gap is not in doubt.
- **Contamination.** Codex can read the whole disk. 3 of 24 no-backend runs searched it. One found another run's bundle in its work folder and answered correctly (the 1 of 24), so the no-backend arm is, if anything, flattered. Two found copies of the backend source and still answered wrongly. No bundle-arm run reached outside its own workspace (`scripts/leak_check.py`); the source arm was given the path.

### D2. Backend refactored after the bundle was generated (128 runs: 8 questions x 4 arms x 4 runs)

Four renames on the backend (a handler method, a request-class field, a path variable, a request class): four questions have a new answer, four are controls. The bundle is from before the refactor. Efficiency prompt ("use the repository knowledge ... avoid unnecessary file reads"), as in B2.

| Arm | Gave the **old** fact | Gave the new fact | Controls correct | Tokens per run |
| --- | --- | --- | --- | --- |
| Backend source (refactored) | 0 / 16 | 16 / 16 | 16 / 16 | 148k |
| Stale bundle | **14 / 16** | 0 / 16 | 16 / 16 | 157k |
| Stale bundle + the confirm sentence | **16 / 16** | 0 / 16 | 16 / 16 | 158k |
| Stale bundle + the sentence + `stale_after` on the 7 changed concepts | **16 / 16** | 0 / 16 | 16 / 16 | 156k |

- Every drift answer from a bundle arm was wrong, and none of the 46 stale answers carried a caveat.
- The confirm sentence could not help: there was no backend source to confirm against.
- `stale_after` did not help either. The seven marked concepts included the routes concept and the packages the questions touched, the pointer explained the field, and still not one of 32 answers in that arm mentioned staleness.
- Unchanged facts stayed correct (controls 16/16 in every arm), so the harm is exactly the drifted facts.
- No run in D2 reached outside its own workspace.

## E. Cross-repo questions where the guide has wrong `[medium]` entries (112 runs)

**Question tested:** does marking each fact with a confidence level (and telling the agent to say when it relies on a guess) change what an agent does when some entries are wrong and it cannot check the source?

**Setup.** The working repository is the storefront; the backend's guide is copied in; the backend source is not available. Each of 7 questions starts from a storefront request, asks which backend handler serves it (a `[high]` entry: a route and a declared method), and asks what that handler calls (a `[medium]` entry: a call target the generator resolves heuristically). In four questions we made the call entry wrong on purpose, using a plausible name from elsewhere in the same guide (for example, the login handler "calling" `CustomerFacade.registerCustomer`). Three questions are unchanged controls. 4 runs per question per condition.

| Condition | Followed the wrong entry (of 16) | True answer | Something else | Said it relied on a `[medium]` guess |
| --- | --- | --- | --- | --- |
| 2. OKF, no labels | **11** | 4 | 1 | 0 |
| OKF with labels, no instruction | 10 | 4 | 2 | 0 |
| **3. OKF with labels and the instruction** | **8** | 3 | 5 | **6** |
| Labels and instruction, but the wrong entries marked `[high]` | 10 | 5 | 1 | 0 |

- Wrong answers fell only a little (11 to 8 of 16; Fisher exact p≈0.47, not reliable). Disclosure rose clearly: 6 of 16 against 0 of 16 (p≈0.02). Of the 8 wrong answers in condition 3, 6 said the answer rested on a `[medium]` entry.
- Mislabelling the wrong entries `[high]` removed all disclosure: agents trusted the label.
- Controls (three unchanged questions, 12 answers per condition): 10, 8, 8 and 9 correct; the agent hedged on 0, 0, 2 and 3 of them. Labels cost a little over-caution.
- "Disclosure" is a keyword match on the answer ("medium", "heuristic", "guess", "unverified", "inferred", and similar); a sample of the matches was read and they were genuine.
- No run reached outside its own workspace (`scripts/leak_check.py`; one flagged path was the author's global skill file, the constant overhead noted under Limits).

## F. Cross-repo change tasks (60 runs)

**Question tested:** when the agent must change the storefront using facts that only the backend states, how much does the backend's guide help, and do confidence labels change that?

**Setup.** Four tasks, each "create this small ES module in the storefront", each checked by a hidden Node test that was shown to fail on the unchanged storefront and pass on a reference solution:
1. `buildAddToCartRequest`: add the backend's field for a discount code (`voucher`, renamed from the real name).
2. `buildSearchRequest`: use the backend's names for page size and offset (`size`, `offset`).
3. `buildReviewsRequest`: use the path the backend declares (`product/{id}/reviews`; the storefront's own code uses `products/...`).
4. `canPurchaseOnline`: read the backend's purchase flag from its public config response (`purchasingEnabled`).

5 runs per task per condition.

| Condition | Passed (of 20) | f1 | f2 | f3 | f4 | Tokens per run (95% CI) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. No OKF | **3** | 3 | 0 | 0 | 0 | 482k (301k to 681k) |
| 2. OKF | **19** | 5 | 5 | 4 | 5 | 242k (203k to 286k) |
| 3. OKF with confidence labels | **15** | 5 | 3 | 2 | 5 | 235k (205k to 270k) |

- No OKF against OKF: 3 against 19 of 20 (p<0.001), at about half the tokens. The 3 passes without a guide were all on task 1, where the backend's field name (`voucher`) is a common word an agent can guess.
- OKF against OKF with labels: 19 against 15 of 20 (p≈0.18), not a reliable difference at this size. The labelled condition's five failures were two wrong paging field names (`start`/`startIndex` for `offset`) and three on the reviews path, one of which added a `/api/v1` prefix that the task did not clearly rule out. The plain guide failed once, on the same task. The task wording should have been clearer about the prefix.
- One task (4) was ambiguous in the first draft: the backend has an internal setting and a public response field with similar meanings. The wording was fixed before any real run.

## G. Cross-repo change, harder tasks (80 runs)

**Question tested:** does the guide still help when the change needs several backend facts, edits the storefront's existing code, or depends on fields defined in the backend's parent classes? And how does it compare with the agent being able to read the backend's source?

**Setup.** A second variant of the backend (`scripts/privatize.py --extra`) additionally renames six fields reached through inheritance, so none can be guessed from memory: `PersistableOrder.shippingQuote` to `quoteId`, `Order.customerAgreement` to `termsAccepted`, `Order.comments` to `orderNote`, `PersistablePayment.paymentToken` to `cardToken`, `PaymentEntity.paymentModule` to `processor`, and `ReadableList`'s `totalPages`, `recordsTotal`, `number` to `pageCount`, `totalRecords`, `itemsOnPage`. The backend has two classes called `PersistableOrder` (older and newer); the checkout handler uses the newer.

Four tasks, each checked by a hidden Node test that runs the storefront's own modules with only the network (axios) and browser globals stubbed (`harness/`). Each test failed on the unchanged storefront and passed on a reference solution (`scripts/solve_g.py`):

1. `g1_delete_item`: fix `deleteFromCart` in the storefront's `cartActions.js`. The backend's route identifies the cart line by its SKU (`/cart/{code}/product/{sku}`); the code sent the numeric id. The prompt only says that removing an item does nothing.
2. `g2_add_voucher`: add an optional last parameter `promoCode` to `addToCart`, sent in the backend's field (`voucher`) for both create and update.
3. `g3_checkout_request`: write `buildCheckoutRequest` using six backend field names, some defined in parent classes.
4. `g4_orders_list`: write `normalizeOrderList` reading the backend's list response, whose paging fields are in a parent class.

Conditions: no OKF; the backend's source readable at a path (an upper reference); OKF (the backend's guide); OKF with confidence labels. 5 runs per task per condition.

| Task | No OKF | Backend source | OKF | OKF + labels |
| --- | --- | --- | --- | --- |
| g1 delete fix | 3 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| g2 voucher | 0 / 5 | 4 / 5 | 5 / 5 | 5 / 5 |
| g3 checkout | 0 / 5 | 4 / 5 | 3 / 5 | 2 / 5 |
| g4 orders list | 0 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| **Total** | **3 / 20** | **18 / 20** | **18 / 20** | **17 / 20** |
| Tokens per run (95% CI) | 294k (235k to 366k) | 333k (284k to 389k) | 301k (257k to 351k) | 308k (267k to 353k) |
| Seconds per run | 42 | 45 | 38 | 38 |

- A guide matched the readable source (18 against 18 of 20, p=1.0). Both beat no guide (p<0.001).
- The 3 passes without a guide were all on `g1`, where the agent guessed the SKU. Where the name was not guessable, no-guide agents passed 0 of 15 here (0 of 30 across F and G).
- `g3` was hardest in every condition. In the one failure inspected, the agent searched the guide for the original field names and used the older `PersistableOrder`.
- Tokens were level across conditions: without a guide the agent usually gave up early with a wrong answer.
- No run reached outside its own workspace (`scripts/leak_check.py`, ignoring the constant global-skills overhead).
- Labelled against plain, pooled with F: 32 against 37 of 40 (p≈0.19), not reliable.

## Spec findings from building it

- Bundle-relative links (`/modules/x.md`) point at the bundle root, so a bundle copied under `references/<name>/` has every internal link broken unless they are rewritten. The emitter rewrites them; the spec does not say how a vendored bundle should be linked.
- A deterministic generator can vouch for structure (names, signatures, call edges, citations), not behaviour. The spec's `verified` field cannot express that, and most concepts contain medium-confidence call edges, so `verified` stamps rarely applied.

## Limits

One model; one repository for A and B (Click, about 25 modules); a synthetic pair for C; 3 to 4 runs per cell; graders and drift written by the experimenters; a constant overhead from the author's global agent skills in every run; v1 and v2 not run simultaneously. The pooled B comparisons were chosen after seeing the data. The bundles the agents read were generated before a later fix to a few optional frontmatter fields (`resource`, `sources[].id`, `last_modified`; see [CONFORMANCE.md](CONFORMANCE.md)); concept bodies were unchanged and nothing was rerun. A language-model arm was excluded by design. D uses the complex repository only as a dependency: whether a bundle saves cost *inside* a large repository the agent can search was not tested. D's backend is real code with the question-relevant identifiers renamed and the planted refactors applied as text edits that were not compiled; it is still recognisably Shopizer by package name.
