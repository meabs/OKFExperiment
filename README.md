# OKF Experiment

**Does giving a coding agent a generated guide to a codebase help it, and does marking each fact with a confidence level help more?**

A coding agent has to work out a codebase before it can change it. We generated a **guide** from source code with a script (no language model): a folder of markdown files, one per module or package, listing its classes, functions, routes and what it calls, with the file and line each fact came from. The file format is [OKF](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) (Open Knowledge Format), which calls such a folder a *bundle*; this page says *guide*. We gave guides to OpenAI's Codex (`gpt-5.6-luna`) while it answered questions about code and made code changes. About 1,100 runs in total.

[The four conditions](#the-four-conditions) · [Results at a glance](#results-at-a-glance) · [What to do](#what-to-do) · [Each test](#each-test) · [Example](#what-a-guide-looks-like) · [Is it valid OKF?](#is-it-valid-okf) · [Limits](#limits) · [Reproduce](#reproducing) · [Files](#repository-layout)

---

## The four conditions

Every test compares the agent in some of these situations:

| | Condition | What the agent has |
| :-: | --- | --- |
| **1** | **No OKF** | Only what it can read and search itself. |
| **2** | **OKF** | The same, plus the generated guide. |
| **3** | **OKF with confidence labels** | The guide, where every fact is marked with how it was derived: `[high]` means stated directly in the source (a class, a field, a route); `[medium]` means a heuristic guess (for example, which method a call refers to). The agent is also told: *"Entries marked `[medium]` are heuristic guesses. When your answer relies on one, say so."* This is the generator's **confidence graph**: every fact is an edge (class extends class, method calls method, route handled by method) carrying a confidence level. |
| **4** | **Cross-repo change with OKF** | The agent works in one repository (a web storefront) and must change it using facts that live in another repository (the backend) that it **cannot read**. It has the backend's guide, with or without confidence labels, or nothing. |

## Results at a glance

| What the agent did | 1. No OKF | 2. OKF | 3. OKF with confidence labels |
| --- | --- | --- | --- |
| **Same repo it can search**: answer questions and make changes (Click) | all correct | all correct, **7 to 30% more tokens** | not separately tested for cost |
| **Same repo, guide out of date**: repeated an old fact | 0 of 12 | **8 of 12** | 8 of 12 (labels alone) |
| &nbsp; and with one instruction sentence ("read the source to confirm") | | **0 of 12** | |
| **Cross-repo questions**, guide current | **1 of 24** correct | **24 of 24** correct | not run |
| **Cross-repo questions**, guide out of date | cannot answer | repeated the old fact in **14 to 16 of 16** | not run |
| **Cross-repo questions**, guide has wrong `[medium]` entries | cannot answer | followed the wrong entry **11 of 16** | followed it **8 of 16**, and **said so in 6** (labels alone: 10 of 16, said so in 0) |
| **4. Cross-repo change** (4 tasks, hidden tests) | **3 of 20** pass, 482k tokens | **19 of 20** pass, 242k tokens | **15 of 20** pass, 235k tokens |

The headline: **where the agent cannot read the code, a guide takes cross-repo changes from 3 of 20 to 19 of 20 at half the tokens. Where it can read the code, a guide adds cost and no accuracy. Confidence labels did not make agents more accurate; with an instruction they made agents say when they were leaning on a guess.**

## What to do

In order of importance. One model and limited tests, so try it on your own agent before relying on it.

1. **Use a guide where the agent cannot read the code**: a private service, a copied-in dependency, another team's repository. Cross-repo changes went from 3 of 20 to 19 of 20 and used half the tokens (test F). Where the agent can search the code, do not expect it to save anything (test A).
2. **Keep a copied-in guide current automatically.** Regenerate it whenever the dependency changes, and have your build check that the source files it was made from have not changed (each file records a SHA-256 hash for this). Out-of-date guides were repeated as fact in 14 to 16 of 16 answers, and neither warnings nor an expiry date helped (test D).
3. **Use confidence labels to make the agent disclose guesses, not to make it right.** With the instruction, agents said they were relying on a `[medium]` guess in 6 of 8 wrong answers; without it, in none. Labels alone changed nothing. Only mark `[high]` what is truly stated in the source: a wrong fact labelled `[high]` was trusted every time (test E).
4. **Where the agent can read the code, add one sentence to its instructions:** "read the source to confirm before you rely on it." It stopped the agent repeating old facts (8 of 12 down to 0 of 12) at no extra cost (test B).
5. **If you generate a guide, include file-and-line references, links between files, calls between modules and an index.** The thinnest guide was always the most expensive. For a web API, one file listing every route with its handler, plus each request class's fields, is what answered the questions.
6. **Do not copy in a guide for something the agent can already read.** It cost about 25% more and gained no accuracy (test C).

The generator's `recommended` setting does item 5; adding `--line-tags` gives condition 3. Detail: [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md) and [docs/RESULTS.md](docs/RESULTS.md).

## Each test

Two measures throughout: **was the answer right (or did the change pass its hidden test)**, and **how many tokens did the agent use** (the text it reads and writes, a stand-in for cost and time). Tests A to C use the small Python library [Click](https://github.com/pallets/click) or a made-up pair of repositories; tests D to F use a real web storefront ([Shopizer's React shop](https://github.com/shopizer-ecommerce/shopizer-shop-reactjs)) that depends on a real 1,173-file Java backend ([Shopizer](https://github.com/shopizer-ecommerce/shopizer)) which the agent cannot read.

| Test | Conditions | The agent | Runs |
| --- | --- | --- | --- |
| **A** Same repo, can search | 1 vs 2 (six kinds of guide, and a graph tool) | answers 5 questions and makes 3 changes in Click | 312 |
| **B** Same repo, guide out of date | 1, 2, 3 | answers questions after we changed Click three ways (renamed a function, added a base class, moved a call) | 340 |
| **C** Cross-repo, dependency readable | 1 vs 2 (current and out of date) | makes 3 changes in a small invoicing service that uses a separate ledger library | 72 |
| **D** Cross-repo questions, dependency unreadable | 1 vs 2 (current and out of date) | answers 8 storefront questions that need backend facts, e.g. "which backend method handles the login request, and what class does it take?" | 224 |
| **E** Cross-repo questions, wrong confidence-tier entries | 2 vs 3 (and 3 with a mislabelled entry) | answers 7 questions where four of the guide's `[medium]` call entries were made wrong on purpose | 112 |
| **F** Cross-repo **change** | 1, 2, 3 | writes 4 small functions in the storefront whose correct field names and paths exist only in the backend; a hidden test checks each | 60 |

### Test A. Same repo, can search: a guide did not help

Every setup answered nearly everything (14 or 15 of 15 questions, 8 or 9 of 9 changes), with or without a guide. So the comparison is cost: tokens compared with no guide (1.00 = the same; higher = more).

| Guide | Tokens vs no guide |
| --- | --- |
| Thinnest (names only, no file references, links or call lists) | 1.26 to 1.42 (always the most expensive) |
| Without call lists | 1.10 to 1.21 |
| **Recommended** (file references, links, calls between modules, an index) | **1.07 to 1.30** |
| Code graph tool instead of a guide | 1.14 to 1.15 |

The recommended guide was level on questions and about 21% more expensive on changes. The two numbers per row are two runs, with and without the "read the source to confirm" sentence; with the sentence the same guides looked more expensive (the runs were not at the same time, so the size of that effect is only indicative).

### Test B. Same repo, guide out of date: a guide made agents repeat old facts, and one sentence fixed it

After the code changed, how many of 12 answers repeated the old fact:

| Condition | Repeated an old fact (of 12) |
| --- | --- |
| 1. No OKF | **0** |
| 2. OKF | **8** |
| 3. OKF with confidence labels (`[high]`/`[medium]` on each line) | 8 |
| OKF + a banner telling the reader to check | 10 |
| OKF + "last verified" and generated-by fields (OKF's own trust fields) | 8 to 9 |
| OKF + an expiry date on only the files that had changed | 5 |
| **OKF + one sentence in the agent's instructions: "read the source to confirm before you rely on it"** | **0** (same cost) |

Confidence labels did not help here, and that is expected: the labels say how a fact was *derived*, not whether it is *current*. A fact that was stated directly in the source a month ago is still labelled `[high]` after the source changes. The expiry date helped somewhat (suggestive, but it did not hold up in test D). The one sentence stopped the problem completely.

### Test C. Cross-repo, dependency readable: a guide added cost, no accuracy

All 72 runs passed, with or without a guide, including an out-of-date one. The ledger library was installed, so the agent could always read it. Copying in its guide cost about 25% more tokens.

### Test D. Cross-repo questions, dependency unreadable: a guide makes the difference, and an out-of-date one is the worst case

**Guide current** (96 runs):

| Condition | Correct | Tokens per run |
| --- | --- | --- |
| 1. No OKF (no access to the backend) | **1 of 24** | about 785,000 |
| Backend source code (for comparison) | 24 of 24 | about 181,000 |
| 2. OKF (the backend's guide) | **24 of 24** | about 189,000 |

Without the backend the agent searched for a long time and still could not answer. With the guide it matched having the full source, at about a quarter of the cost of failing. What answered the questions: a list of every route with its handler, each handler's parameter types, and each request class's fields.

**Guide out of date** (128 runs). We renamed four things in the backend after the guide was made. Four questions had a new answer; four did not.

| The agent had | Gave the **old** answer | Gave the new answer | Unchanged questions right |
| --- | --- | --- | --- |
| The backend's (changed) source | 0 of 16 | 16 of 16 | 16 of 16 |
| The out-of-date guide | **14 of 16** | 0 of 16 | 16 of 16 |
| + the "read the source to confirm" sentence | **16 of 16** | 0 of 16 | 16 of 16 |
| + the sentence, and an expiry date on the 7 changed files | **16 of 16** | 0 of 16 | 16 of 16 |

Every changed fact was wrong and none of the 46 wrong answers hedged. The sentence could not help because there was no source to check against. The expiry date did not help either: not one answer mentioned it. Facts that had not changed stayed correct.

### Test E. Cross-repo questions with wrong `[medium]` entries: labels make the agent disclose a guess, not avoid it

Each question starts from a storefront request, crosses into the backend (which the agent cannot read), and asks which handler serves it (a `[high]` entry) and what that handler calls (a `[medium]` entry). In four of the seven questions we made the `[medium]` call entry wrong on purpose. 16 answers per condition on those four.

| Condition | Followed the wrong entry | Gave the true answer | Something else | Said it relied on a `[medium]` guess |
| --- | --- | --- | --- | --- |
| 2. OKF (no labels) | **11** | 4 | 1 | 0 |
| OKF with labels, no instruction | 10 | 4 | 2 | 0 |
| **3. OKF with labels and the instruction** | **8** | 3 | 5 | **6** |
| Labels and instruction, but the wrong entries marked `[high]` | 10 | 5 | 1 | 0 |

- Labels cut wrong answers only a little (11 to 8 of 16; not a reliable difference, p≈0.5). What changed is disclosure: with the instruction, agents said they were relying on a `[medium]` guess in 6 of 16 planted answers, against 0 in the others (p≈0.02), so a reader is warned. Example: *"The facade call is marked `[medium]` in the generated guide, meaning heuristic."*
- When a wrong entry was labelled `[high]`, agents trusted it and said nothing (0 disclosures). A label is only as good as the generator's honesty about it.
- "Something else" covers answers that matched neither the true nor the planted entry. In a trial run we saw an agent decline a login handler that "called" `registerCustomer` and answer with a different handler instead.
- On the three unchanged questions, 8 to 10 of 12 were right in every condition, and labels caused a little over-hedging (2 to 3 of 12 hedged). The cost of labels was small.

### Test F. Cross-repo change: with a guide, changes pass; without it, they do not

The agent works in the storefront and writes four small functions. Each one's correct field name or path is stated only in the backend, and a hidden test checks the file the agent wrote. For example: build the add-to-cart request, including the backend's field for a discount code; build the search request, using the backend's names for page size and offset; build the reviews request, using the path the backend declares.

| Condition | Changes that passed (of 20) | Tokens per run |
| --- | --- | --- |
| 1. No OKF | **3** | 482k |
| 2. OKF | **19** | 242k |
| 3. OKF with confidence labels | **15** | 235k |

- A guide took cross-repo changes from 3 of 20 to 19 of 20 (p<0.001) at half the tokens. Without the backend, agents had to guess the field names. The 3 passes were all on the discount-code task, where a common name happened to match.
- The labelled condition passed 15 of 20, against 19 of 20 for the plain guide. That difference is not reliable (p≈0.18, 5 runs per task). Its five failures were two wrong paging field names (`start` for `offset`) and three on the reviews path, one of which added a `/api/v1` prefix our task did not clearly rule out; the plain guide failed once, on the same task.

## What a guide looks like

A real file from the Click guide. The header is OKF metadata; every line below it ends with the file and line number it came from.

```markdown
---
type: Code Module
title: "click.core"
resource: "https://github.com/pallets/click/blob/2247b35.../src/click/core.py"
generated: { by: "kgen/0.4.0", at: "2026-10-04T15:19:53-07:00" }
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35.../src/click/core.py"
    sha256: "26307e89b7b2..."
status: stable
---

## Types
- `Option` (class) extends `click.core.Parameter`  `src/click/core.py:3057`

## Calls
- `Parameter.consume_value` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value`  `src/click/core.py:2718`
```

With confidence labels (condition 3), each line ends with its level. A declared class is `[high]`; a call target, which the generator works out by matching names and types, is `[medium]`:

```markdown
- `Option` (class) extends `click.core.Parameter`  `src/click/core.py:3057` `[high]`
- `Parameter.consume_value` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value`  `src/click/core.py:2718` `[medium]`
```

For a web API there is also one file listing every route, which is what the cross-repo questions were answered from:

```markdown
| POST | `/api/v1/customer/login` | [...customer](/modules/com.salesmanager.shop.store.api.v1.customer.md) `AuthenticateCustomerApi.authenticate` | `sm-shop/src/main/java/.../AuthenticateCustomerApi.java:157` |
```

Generated guides you can browse are in [end-state/](end-state/): Click, Click with confidence labels, Click after the changes, the invoicing pair, and the real Shopizer backend (315 files, 325 routes).

## Is it valid OKF?

Yes. All the guides in `end-state/` meet OKF v0.2's conformance rules, load and validate in the format's own reference parser, and pass [`scripts/check_okf.py`](scripts/check_okf.py), a checker we wrote from the spec's rules, with no findings. There is no official validator, so that checker is our reading of the spec. OKF has no field for per-fact confidence, so the confidence labels are an extension: a `[high]`/`[medium]` mark at the end of each line. The first version of the generator was valid but filled in four optional fields in ways the spec does not intend; those were found and fixed. Details: [docs/CONFORMANCE.md](docs/CONFORMANCE.md).

## Limits

- **One agent** (Codex `gpt-5.6-luna`, medium reasoning). Other agents may behave differently.
- **Small samples:** 3 to 5 runs per question per condition, so differences under about 20% are not reliable. Tests A to C use one small library or a made-up pair.
- **Confidence labels were tested against one kind of `[medium]` fact**, call targets, and in conditions where the agent could not verify anything (E, F) or where we measured out-of-date facts (B), which labels do not address. Whether labels help where the agent can partly verify them is untested.
- **The large repository was only used as the thing the agent could not read.** We did not test whether a guide saves cost *inside* a large repository the agent can search.
- **The backend is real code with a few names changed** so the agent could not answer from memory of a well-known project, and with planted changes applied as text edits that were not compiled. It is still recognisable as Shopizer from its package names.
- **The agent can read the whole disk**, so a run can wander outside its workspace. We counted: 3 of 24 runs without the backend did in test D, one of which found another run's guide; none did in E or F.
- **We wrote the questions, the hidden tests and the planted changes ourselves**, and some comparisons in test B were chosen after seeing the data. Test E's disclosure count is a keyword match on the answer text.
- A generator that reads source can state structure (names, signatures, who calls whom, routes), not what the code does.
- **We made mistakes along the way and kept the evidence.** The first runs of tests A and B told the agent to verify in every condition, which hid the differences; we reran them without it and ran a third test of that sentence alone. The first version of test D let the agent answer from memory; we caught that in a trial run and renamed the backend's names before the real runs. One test F task was ambiguous about which of two purchase flags it meant; we fixed the wording before the real runs.

## Reproducing

The generator command `kgen okf` is not released yet. Until it is, apply the patch to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at commit `dd26ee6`:

```bash
git clone https://github.com/meabs/AgentGraphWorkTree && cd AgentGraphWorkTree
git checkout dd26ee6 && git apply ../OKFExperiment/scripts/kgen-okf.patch
python .apm/skills/agent-graph/tool/kgen.py sync --repo R
python .apm/skills/agent-graph/tool/kgen.py okf --repo R --out R/okf --pointer R/AGENTS.md              # condition 2
python .apm/skills/agent-graph/tool/kgen.py okf --repo R --out R/okf --pointer R/AGENTS.md --line-tags  # condition 3
python ../OKFExperiment/scripts/check_okf.py R/okf
```

`kgen` needs `tree-sitter` and `tree-sitter-java`. The patch includes a fix for a bug where the Java extractor listed spurious routes. To rerun tests A to C, `scripts/make_a.py`, `make_b.py` and `make_c.py` build each condition for [AgentTrialRig](https://github.com/meabs/AgentTrialRig). To rerun D to F: clone Shopizer at `6a4a0a6` and its React storefront at `455b4bc`, run `scripts/privatize.py` on a copy of the backend (and again with `--drift` on a second copy), generate the guides, and run `scripts/make_d.py`, `make_e.py` and `make_f.py` (copy `hidden/` next to them). `scripts/leak_check.py` counts runs that left their workspace; `analyse_d2.py` and `analyse_e.py` count old and wrong answers.

## Repository layout

| Path | What it holds |
| --- | --- |
| [`docs/`](docs/) | the detail: [RESULTS.md](docs/RESULTS.md), [RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md), [CONFORMANCE.md](docs/CONFORMANCE.md) |
| [`results/`](results/) | each test's raw report ([index](results/README.md)) |
| [`end-state/`](end-state/) | the recommended guides and their agent-instruction files ([readme](end-state/README.md)) |
| [`scripts/`](scripts/) | test builders, the generator patch, the validity checker, analysis scripts |
| [`hidden/`](hidden/), [`fixtures/`](fixtures/), [`drift/`](drift/) | the hidden tests, the invoicing pair, and the Click changes |
