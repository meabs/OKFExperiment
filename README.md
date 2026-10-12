# OKF Experiment

**Does giving a coding agent a generated description of a codebase help it?**

An **OKF bundle** is a folder of markdown files that describes a codebase: one file per module or package, listing its classes, functions, routes and what it calls, with the file and line each fact came from. [OKF](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) (Open Knowledge Format) is the file format. We generated bundles from source code with a script (no language model) and gave them to a coding agent, OpenAI's Codex (`gpt-5.6-luna`), while it answered questions about code and made code changes. About 950 runs in total.

[What we tested](#what-we-tested) · [Results](#results) · [What to do](#what-to-do) · [Example](#what-a-bundle-looks-like) · [Is it valid OKF?](#is-it-valid-okf) · [Limits](#limits) · [Reproduce](#reproducing) · [Files](#repository-layout)

---

## The short version

- **If the agent can read and search the code itself, a bundle did not help.** It answered correctly with or without one, and the bundle only added reading.
- **If the agent cannot read the code, a bundle makes the difference:** 1 of 24 questions answered correctly without it, 24 of 24 with it, at about a quarter of the cost of searching blindly.
- **A bundle that is out of date is dangerous.** Agents repeated its old facts as if they were true. If the agent can read the code, one sentence in its instructions ("read the source to confirm before you rely on it") stops this. If it cannot read the code, nothing we tried helped, so the bundle has to be kept current automatically.

## What we tested

Four tests. In each we compared the agent with and without a bundle (or with different kinds of bundle) and measured two things: **was the answer right**, and **how many tokens did it use** (the text the agent reads and writes, a stand-in for cost and time).

| Test | What the agent had to do | What we compared |
| --- | --- | --- |
| **1. Does a bundle help on a codebase the agent can search?** | Answer 5 questions about [Click](https://github.com/pallets/click) (a Python library) and make 3 code changes, each checked by a hidden test. | No bundle, against 6 kinds of bundle (thin to thick, with and without links, call lists and an index), and against a code-graph tool. |
| **2. If the code changes, does the agent repeat the bundle's old facts?** | Answer questions about Click after we changed the code in three ways: renamed a function, added a base class, moved a call. The bundle was made *before* the changes, so it was out of date. | No bundle, a plain bundle, and bundles with warnings added (labels on each line, a banner, "last verified" fields, an expiry date, one instruction sentence). |
| **3. Does a bundle of a *readable* dependency help?** | Change a small invoicing service that depends on a separate ledger library. Three tasks, hidden tests. | The library installed as normal, its source location given, or its bundle copied in (current and out of date). |
| **4. Does a bundle help when the agent *cannot* read the dependency?** | Answer 8 questions in a real web storefront ([Shopizer's React shop](https://github.com/shopizer-ecommerce/shopizer-shop-reactjs)) that need facts from its backend, a separate Java system with 1,173 source files ([Shopizer](https://github.com/shopizer-ecommerce/shopizer)) that the agent has no access to. For example: "Which backend method handles the login request, and what class does it take?" | No backend at all, the backend source, or the backend's bundle (current, and then out of date after we renamed things in the backend). |

## Results

### Test 1. On a codebase the agent can search, a bundle did not help

Every setup answered nearly everything correctly (14 or 15 of 15 questions, 8 or 9 of 9 code changes), with or without a bundle. So the comparison is cost. The table shows tokens used compared with no bundle (1.00 = the same; higher = more).

| Bundle | Tokens vs no bundle |
| --- | --- |
| Thinnest (names only, no file references, links or call lists) | 1.26 to 1.42 (always the most expensive) |
| Without call lists | 1.10 to 1.21 |
| **Recommended** (file references, links, calls between modules, an index) | **1.07 to 1.30** |
| Code graph tool instead of a bundle | 1.14 to 1.15 |

The recommended bundle was level with no bundle on questions and about 21% more expensive on code changes. Nothing beat having no bundle. The two numbers per row are two runs of the same test, with and without the "read the source to confirm" sentence in the agent's instructions; with the sentence the same bundles looked more expensive, which suggests it makes the agent read more (the two runs were not at the same time, so the size of the effect is only indicative).

### Test 2. Out-of-date bundles made the agent repeat old facts, and one sentence fixed it

After the code changed, we counted how many of 12 answers repeated the old fact.

| Setup | Repeated an old fact (of 12) |
| --- | --- |
| No bundle | **0** |
| Plain bundle | **8** |
| + labels on every line saying how reliable it is | 8 |
| + a banner telling the reader to check | 10 |
| + "last verified" and generated-by fields (OKF's own trust fields) | 8 to 9 |
| + an expiry date on only the files that had changed | 5 |
| **Plain bundle + one sentence in the agent's instructions: "read the source to confirm before you rely on it"** | **0** (same cost) |

A plain bundle was clearly worse than no bundle (8 against 0). Labels, banners and trust fields did not help. The expiry date on changed files helped somewhat (suggestive, but it did not hold up in test 4). The one sentence stopped the problem completely. Renamed functions were repeated most often: the agent trusted the bundle and never searched for the new name.

### Test 3. A readable dependency's bundle added cost and no accuracy

All 72 runs passed, with or without a bundle, including with an out-of-date one. The ledger library was installed, so the agent could always read it. Copying in its bundle cost about 25% more tokens.

### Test 4. When the agent cannot read the dependency, a bundle makes the difference, and an out-of-date one is the worst case

**Bundle current** (96 runs):

| Agent had | Correct | Tokens per run |
| --- | --- | --- |
| No access to the backend | **1 of 24** | about 785,000 |
| The backend's source code | 24 of 24 | about 181,000 |
| The backend's bundle | **24 of 24** | about 189,000 |

Without the backend the agent searched for a long time and still could not answer. With the bundle it matched having the full source, at about a quarter of the cost of failing. What answered the questions: a list of every route with its handler, each handler's parameter types, and each request class's fields.

**Bundle out of date** (128 runs). We renamed four things in the backend after the bundle was made. Four questions now had a new answer; four did not.

| Agent had | Gave the **old** answer | Gave the new answer | Unchanged questions right |
| --- | --- | --- | --- |
| The backend's (changed) source | 0 of 16 | 16 of 16 | 16 of 16 |
| The out-of-date bundle | **14 of 16** | 0 of 16 | 16 of 16 |
| + the "read the source to confirm" sentence | **16 of 16** | 0 of 16 | 16 of 16 |
| + the sentence, and an expiry date on the 7 changed files | **16 of 16** | 0 of 16 | 16 of 16 |

Every changed fact was wrong and none of the 46 wrong answers hedged. The sentence could not help because there was no source to check against. The expiry date did not help either: not one answer mentioned it, even though the files the agent read carried it and the instructions explained it. Facts that had not changed stayed correct.

## What to do

In order of importance. This is one model and a limited set of tests, so try it on your own agent before relying on it.

1. **Use a bundle where the agent cannot read the code**: a private service, a copied-in dependency, another team's repository. That is where it earned its keep. For code the agent can search, do not expect it to save anything.
2. **Keep a copied-in bundle current automatically.** Regenerate it whenever the dependency changes, and have your build check that the source files it was made from have not changed (each file records a SHA-256 hash for this). Warnings and labels did not protect the agent, so an out-of-date bundle for something the agent cannot read is worse than no bundle.
3. **Where the agent can read the code, put one sentence in its instructions:** "read the source to confirm before you rely on it." It cost nothing and stopped the agent repeating old facts.
4. **If you generate a bundle, include file-and-line references, links between files, calls between modules and an index.** The thinnest bundle was always the most expensive. Per-line labels and banners made it bigger without making agents more careful. For a web API, a single file listing every route with its handler, plus each request class's fields, is what answered the questions.
5. **Do not copy in a bundle for something the agent can already read.** It cost about 25% more and gained no accuracy.

The generator's `recommended` setting does item 4. Detail: [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md) and [docs/RESULTS.md](docs/RESULTS.md).

## What a bundle looks like

A real file from the Click bundle. The header is OKF metadata; every line below it ends with the file and line number it came from.

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

## Functions and methods
- `Context.get_parameter_source(name: str) -> ParameterSource | None`  `src/click/core.py:970`

## Calls
- `Parameter.consume_value` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value`  `src/click/core.py:2718`
```

For a web API there is also one file listing every route, which is what test 4's questions were answered from:

```markdown
| POST | `/api/v1/customer/login` | [...customer](/modules/com.salesmanager.shop.store.api.v1.customer.md) `AuthenticateCustomerApi.authenticate` | `sm-shop/src/main/java/.../AuthenticateCustomerApi.java:157` |
```

Generated bundles you can browse are in [end-state/](end-state/): Click, Click after the changes, the invoicing pair, and the real Shopizer backend (315 files, 325 routes).

## Is it valid OKF?

Yes. All the bundles in `end-state/` meet OKF v0.2's conformance rules, load and validate in the format's own reference parser, and pass [`scripts/check_okf.py`](scripts/check_okf.py), a checker we wrote from the spec's rules, with no findings. There is no official validator, so that checker is our reading of the spec. The first version of the generator was valid but filled in four optional fields in ways the spec does not intend; those were found and fixed. The choices that remain on purpose, and what they mean for the earlier tests, are in [docs/CONFORMANCE.md](docs/CONFORMANCE.md).

## Limits

- **One agent** (Codex `gpt-5.6-luna`, medium reasoning). Other agents may behave differently.
- **Small samples:** 3 to 4 runs per question per setup, so differences under about 20% are not reliable. Tests 1 and 2 use one small library (Click); test 3 uses a made-up pair of repositories.
- **The large repository (test 4) was only used as the thing the agent could not read.** We did not test whether a bundle saves cost *inside* a large repository the agent can search.
- **Test 4's backend is real code, with a few names changed** so the agent could not answer from memory of a well-known project, and with the planted changes applied as text edits that were not compiled. It is still recognisable as Shopizer from its package names.
- **The agent can read the whole disk**, so a run can wander outside its workspace. We counted: 3 of 24 runs without the backend did, one of them found another run's bundle and got the answer right; no run with a bundle did.
- **We wrote the questions, the hidden tests and the planted changes ourselves**, and some comparisons in test 2 were chosen after seeing the data.
- A generator that reads source can state structure (names, signatures, who calls whom, routes), not what the code does.
- **We made mistakes along the way and kept the evidence.** The first runs of tests 1 and 2 told the agent to verify in every setup, which hid the differences; we reran them without it and ran a third test of that sentence alone. The first version of test 4 let the agent answer from memory; we caught that in a trial run and renamed the backend's names before the real runs. All reports are in [results/](results/).

## Reproducing

The generator command `kgen okf` is not released yet. Until it is, apply the patch to [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) at commit `dd26ee6`:

```bash
git clone https://github.com/meabs/AgentGraphWorkTree && cd AgentGraphWorkTree
git checkout dd26ee6 && git apply ../OKFExperiment/scripts/kgen-okf.patch
python .apm/skills/agent-graph/tool/kgen.py sync --repo R
python .apm/skills/agent-graph/tool/kgen.py okf --repo R --out R/okf --pointer R/AGENTS.md
python ../OKFExperiment/scripts/check_okf.py R/okf
```

`kgen` needs `tree-sitter` and `tree-sitter-java`. The patch includes a fix for a bug where the Java extractor listed spurious routes. To rerun tests 1 to 3, `scripts/make_a.py`, `make_b.py` and `make_c.py` build each setup for [AgentTrialRig](https://github.com/meabs/AgentTrialRig). To rerun test 4: clone Shopizer at `6a4a0a6` and its React storefront at `455b4bc`, run `scripts/privatize.py` on a copy of the backend (and again with `--drift` on a second copy), generate the bundles, then run `scripts/make_d.py`. `scripts/leak_check.py` counts runs that left their workspace, and `scripts/analyse_d2.py` counts old answers.

## Repository layout

| Path | What it holds |
| --- | --- |
| [`docs/`](docs/) | the detail: [RESULTS.md](docs/RESULTS.md), [RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md), [CONFORMANCE.md](docs/CONFORMANCE.md) |
| [`results/`](results/) | each test's raw report ([index](results/README.md)) |
| [`end-state/`](end-state/) | the recommended bundles and their agent-instruction files ([guide](end-state/README.md)) |
| [`scripts/`](scripts/) | test builders, the generator patch, the validity checker, analysis scripts |
| [`hidden/`](hidden/), [`fixtures/`](fixtures/), [`drift/`](drift/) | the hidden tests, the invoicing pair, and the Click changes |
