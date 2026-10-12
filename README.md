# OKF Experiment: Do coding agents benefit from generated knowledge?

Coding agents have to understand code before they can change it. When the code is in front of them they can search it. When the change depends on another repository they cannot read, such as a private service or a vendored dependency, they have to be given the facts or guess them.

We tested what helps. We generated a **guide** from source code with a script (no language model): a folder of markdown files, one per module or package, listing classes, functions, routes and calls, each with the file and line it came from. The format is [OKF](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) (Open Knowledge Format), which calls such a folder a *bundle*; this README says *guide*. We compared guides with nothing, with an API contract, with a short hand-written note and with the real source.

Every run used one agent, OpenAI's Codex (`gpt-5.6-luna`, medium reasoning). The agent answered questions or made changes that hidden tests graded, and we recorded whether it was right and how many tokens it used. There were about 1,480 runs in eight experiments (A to H).

| Experiment | Setting | Runs |
| --- | --- | --- |
| A, B | Small library (Click), agent can read it: guide shapes, then out-of-date guides | 312, 340 |
| C | Invoicing service with a readable ledger library | 72 |
| D, E | Storefront and a 1,173-file Java backend the agent cannot read: questions; wrong confidence entries | 224, 112 |
| F, G | The same pair: small, then harder cross-repository changes | 60, 80 |
| H | Guide against an OpenAPI contract, a note and the source (H1 changes, H2 questions, H3 a small service) | 280 |

The central message: **coding agents do not necessarily need more documentation. They need the right information, at the right time, from a trustworthy source.**

## Key findings

1. **Knowledge about a repository the agent can already read did not improve accuracy.** It added tokens, and when it was out of date it misled the agent (A, B, C).
2. **Where the agent cannot read a dependency, facts about it made a large difference.** Cross-repository changes passed in 3 of 20 runs with nothing, and in 18 or 19 of 20 with a guide (F, G).
3. **For changes that depend on an interface, a contract or a 3 KB note did about as well as a guide, and cost less** (H1).
4. **For questions about internal call relationships, only the guide and the source worked** (21 of 24, against 8 for the contract and 0 for the note). This measured answering questions, not making better changes (H2).
5. **Out-of-date knowledge produced confident wrong answers.** An out-of-date guide of something the agent could not read was repeated as fact in 14 to 16 of 16 answers, with no hedging (D2).

**Conclusion.** Where the source is inaccessible, give the agent an authoritative, versioned contract first, and add structural knowledge only for tasks the contract cannot support. Whatever you give it, check that it matches the version of the dependency in use. The experiments do not show that a guide is needed everywhere, and they do not show that it improves software changes beyond what a contract gives.

## When the agent can read the repository

Evidence: A (Click, 312 runs), B (340 runs), C (72 runs). Details: [docs/DETAILS.md](docs/DETAILS.md) and [docs/RESULTS.md](docs/RESULTS.md).

**Accuracy did not change.** With or without a guide, agents answered 14 or 15 of 15 questions and made 8 or 9 of 9 changes correctly. In C all 72 changes passed.

**Cost went up or stayed level.** The recommended guide cost 1.30 times the tokens of no guide in one run (reliably more) and 1.07 in a rerun (no clear difference). The thinnest guide, with names only, was reliably the most expensive (1.26 to 1.42). Copying in a guide for a readable library cost 1.25 times (C, reliably more).

**An out-of-date guide misled the agent.** After we changed Click three ways, 8 of 12 answers repeated the old fact with a guide and 0 of 12 without. Confidence labels, a warning banner and OKF's own trust fields did not prevent it. One sentence in the agent's instructions, "read the source to confirm before you rely on it", did: 0 of 12 (B).

A guide is a substitute for reading the code, so it adds little where the code can be read. We did not test whether that holds for a very large repository the agent can read; a preregistered test is described in [docs/EXPERIMENT_I.md](docs/EXPERIMENT_I.md).

## When the agent cannot read a dependency

Here an agent has to change one repository (a web storefront) using facts that live in another (a Java backend) that is not in its workspace. This is the common case for services owned by other teams. Without help the agent guesses names, and mostly guesses wrong. We hid the backend's real identifiers by renaming, so none could be recalled from memory.

### Making changes across repositories

Passed, with hidden tests. "Not tested" means that arm was not part of that experiment.

| Experiment | Tasks | Nothing | Contract | Note | Guide | Source |
| --- | --- | --- | --- | --- | --- | --- |
| F | 4 small tasks, 20 runs per arm | 3 | not tested | not tested | 19 | not tested |
| G | 4 harder tasks, 20 runs per arm | 3 | not tested | not tested | 18 | 18 |
| H1 | the G tasks again, 16 runs per arm | 4 | 13 | 14 | 14 | 14 |

A guide reliably beat nothing in every experiment. In H1 the contract, note, guide and source all beat nothing and did not differ reliably from each other. That does not show they are equivalent: with 16 runs per arm, differences under about 30 points cannot be separated.

The cost was not the same. In H1 the note used 128k tokens per run and the contract 192k, both reliably less than nothing (277k). The guide used 282k, no clear difference from nothing, and the source 334k, reliably more. In F the guide's saving over nothing (242k against 482k) was not reliable, and in G the token counts were level.

Two cautions. The hardest task, the checkout request, split the arms: contract 1 of 4, guide 2 of 4, note 4 of 4, source 4 of 4. And the note was written by us knowing the tasks, which favours it, while the contract was generated from the source by our script, not by a running Spring application. The passes with nothing were mostly on tasks whose answer can be guessed, such as using the product's SKU as its identifier.

The checkout task is also where a guide went wrong: the backend has two classes called `PersistableOrder`, and some guide runs used the older one.

### Understanding internal dependencies

H2 asked six questions of the form "which method handles this request, and which class does it call?". A contract describes an interface, not what a handler calls inside.

| Arm | Correct (of 24) | Tokens per run |
| --- | --- | --- |
| Nothing | 1 | 447k |
| Contract | 8 | 464k |
| Note | 0 | 476k |
| **Guide** | **21** | **170k** |
| Source | 21 | 207k |

The guide matched the source and beat the contract and the note (p<0.001), at under half the tokens of the arms that had to search. **This shows that a guide answers structural questions. It does not show that those answers lead to better software changes**, which is a separate claim we have not tested.

Two qualifications. The network was on, and 56 of the 120 H2 runs cloned the public Shopizer repository (19 of 24 in the nothing arm, 18 in contract, 19 in note, none in guide or source). Renaming mostly stopped this helping, but all 8 contract passes were among those runs; without the network runs, nothing scored 1 of 5, the contract 0 of 6 and the note 0 of 5. And H3, a small runnable service, was contaminated (see Limits), so we make no claim from it about behaviour, except one clear case: the contract listed `201` as the only success code, and agents trusted it, so the retry task failed in 0 of 4 runs.

### What happens when knowledge is out of date?

In D2 we renamed four things in the backend after the guide was made. Four questions had a new answer; four did not.

| The agent had | Gave the old answer (of 16) | Gave the new answer |
| --- | --- | --- |
| The changed source | 0 | 16 |
| The out-of-date guide | 14 | 0 |
| The guide plus "read the source to confirm" | 16 | 0 |
| The guide plus an expiry date on the changed files | 16 | 0 |

None of the 46 wrong answers hedged. The sentence could not help, because there was no source to check against, and not one answer mentioned the expiry date. Facts that had not changed stayed correct, so the harm was confined to what had drifted.

**Confidence labels did not make agents more accurate.** A label says how a fact was found, not whether it is still true. With an instruction to disclose guesses, agents said they relied on a `[medium]` entry in 6 of 8 wrong answers, against 0 without it, so a reader is warned. A wrong entry labelled `[high]` was trusted every time (E).

This is why provenance and version alignment matter. Each guide file records the SHA-256 of the source it was made from, and [`scripts/check_references.py`](scripts/check_references.py) compares a copied-in guide with the dependency's current files. Nothing placed inside the guide protected the agent; a check outside it can. We tested these checks on small examples, not in a real CI pipeline or at the scale of the backend.

## What should engineers use?

The "Basis" column separates what we measured from what we recommend.

| Situation | Suggested approach | Basis |
| --- | --- | --- |
| Agent can read the repository | Source code and existing tooling; add "read the source to confirm before you rely on it" to its instructions | Measured (A, B, C) |
| Agent needs another service's API | Versioned API contract | Measured for field names and paths (H1) |
| Agent needs a few additional facts | Small authoritative reference | Measured, with a note written knowing the tasks (H1) |
| Agent needs internal call relationships | Targeted structural knowledge, potentially a generated guide | Measured for questions only (H2). Not shown for changes |
| Agent needs business behaviour or invariants | Authoritative behavioural specifications and tests | Recommendation. No generated artefact held behaviour in H3, which was contaminated |
| Generated knowledge may be stale | Validate against the consumed dependency version before use | Harm measured (B, D2). The checks are a recommendation |

Nothing here means a guide must be used. If you do generate one, include file-and-line references, links between files, calls between modules and an index; the thinnest guide was always the most expensive. Use confidence labels only to make guesses visible, and mark `[high]` only what the source states.

## Limits

- **One agent and one reasoning setting.** Other models may behave differently.
- **Few tasks and repetitions.** Experiments A to G had 3 to 5 runs per question per condition, H had 16 to 24 per arm. Small differences are not reliable, and equal pass rates are not proof of equivalence.
- **We wrote the questions, hidden tests and planted changes.** Some comparisons in B were chosen after seeing the data.
- **The backend is Shopizer with names changed** and changes applied as uncompiled text edits. The H1 contract is generated by our script from its source.
- **H2 had network access, and 56 of 120 runs cloned the public repository.** Results are reported with and without those runs.
- **H3 was contaminated.** Agents without the source searched the disk and found the service, the tests and other arms' material in 15 of 64 runs, and the sandbox cannot restrict reads. No pair of arms differed reliably (smallest p=0.08), and the price-rule task could not be tested fairly.
- **Large readable codebases are not evaluated.** The large backend was used only as something the agent could not read.
- **There is no evidence here for an enterprise-wide knowledge platform.** The experiments compare ways of giving an agent facts about one dependency.
- **A generator that reads source states structure, not what the code does.**

The first runs of A and B told the agent to verify in every condition, which hid differences, so we reran them without it. The first version of D let the agent answer from memory, so we renamed the backend's names before the real runs. The first H3 run is archived in [`results/archive/`](results/archive/) and not reported.

## Reproducing and exploring

| What | Where |
| --- | --- |
| **Long-form detail**: the four conditions, recommended guide layout, each experiment, the full analysis, an example file, rerun commands | [docs/DETAILS.md](docs/DETAILS.md) |
| Results for each experiment, with tables | [docs/RESULTS.md](docs/RESULTS.md) |
| Plans written before the runs (H, and I in progress) | [docs/EXPERIMENT_H.md](docs/EXPERIMENT_H.md), [docs/EXPERIMENT_I.md](docs/EXPERIMENT_I.md) |
| Raw trial reports | [results/](results/) ([index](results/README.md)) |
| Advice in more detail | [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md) |
| Does the output meet OKF v0.2? | [docs/CONFORMANCE.md](docs/CONFORMANCE.md) |
| Example guides (Click, invoicing pair, the Shopizer backend) | [end-state/](end-state/) |
| Validity and freshness checks | [`scripts/check_okf.py`](scripts/check_okf.py), [`scripts/check_fresh.sh`](scripts/check_fresh.sh), [`scripts/check_references.py`](scripts/check_references.py) |
| Test builders and analysis | [scripts/](scripts/), [harness/](harness/), [hidden/](hidden/), [fixtures/](fixtures/), [drift/](drift/) |

The generator, `kgen okf`, is in [AgentGraphWorkTree](https://github.com/meabs/AgentGraphWorkTree) from commit `aa98666` on `main`; `scripts/kgen-okf.patch` applies the same change to the older base `dd26ee6`. The tests run through [AgentTrialRig](https://github.com/meabs/AgentTrialRig). The commands to generate a guide and the steps to rerun each experiment (clone Shopizer at `6a4a0a6` and its React storefront at `455b4bc`, then follow `scripts/make_*.py`) are in [docs/DETAILS.md](docs/DETAILS.md#reproducing-in-detail).
