# Deep Research Skills

**Status:** Bootstrap design complete through the public README stage. The canonical architecture is specified, but production skill packages have not yet been scaffolded or installation-tested.

**Conduct evidence-backed research, not isolated searches.**

Deep Research Skills coordinates **research production**: frame the question, choose an evidence strategy, inspect original sources, preserve provenance, analyse contradictions, synthesise what the evidence supports, audit material claims, and refresh only what changed.

It is designed for bounded fact-finding, comparisons, evidence synthesis, landscapes, source verification, research updates and research programmes that feed other Production Skills without taking over their decisions.

## Research capabilities

The production model covers:

- **Question and decision framing** — define the actual evidence need, scope, exclusions, freshness and downstream use before expensive retrieval.
- **Source strategy and discovery** — match the question to appropriate source classes and acquisition paths rather than defaulting every task to broad web search.
- **Evidence extraction and provenance** — preserve the inspected representation, locator, access depth, context and material transformations.
- **Claim analysis** — separate evidence from inference, identify source dependence, preserve contrary findings and expose unresolved gaps.
- **Synthesis** — answer the research need without becoming more certain than the evidence.
- **Evaluation** — audit source quality, independence, coverage, claims, citations, freshness, contradictions, uncertainty and reproducibility against fixed inputs.
- **Repair and refresh** — diagnose the owning defect, preserve unaffected verified work, and update only the necessary evidence and dependent synthesis.
- **Cross-domain handoff** — provide evidence packages to engineering, design, creative, business and specialist domains while leaving their production decisions with them.

## Research effort and evidence control

Research is bounded by evidence quality, authority and cost — not by how many sources an agent can collect.

- **Question before retrieval.** Resolve the objective and decision context before broad search.
- **Direct evidence before repetition.** Prefer the most direct suitable source; several reports repeating one origin are not independent corroboration.
- **Source quality is multidimensional.** Directness, authority, method, transparency, recency, independence, incentives, specificity and stability remain separate concerns.
- **Contradictions stay visible.** Conflicting high-quality evidence is investigated or reported, not silently averaged away.
- **Uncertainty survives synthesis.** Source statement, observation, extracted data, inference, interpretation, forecast, recommendation, assumption and unknown remain distinguishable when the difference matters.
- **Time is part of the evidence.** Event, publication, effective, retrieved-at and valid-as-of dates are not interchangeable.
- **Use the cheapest adequate authorised operation.** Exact retrieval, metadata triage and targeted follow-up come before expensive broad research when they can resolve the uncertainty.
- **Preserve verified work.** Repair the smallest responsible evidence, claim or synthesis scope rather than regenerating everything.
- **Bound resource exposure.** Search, browser work, premium APIs, document retrieval, OCR, code execution, research engines, parallel workers and specialist review are tracked as separate resource dimensions.
- **A cap is not sufficiency.** Hitting a budget or search limit can produce a limited result; it cannot turn incomplete evidence into a supported conclusion.

## Installation

The intended Agent Skills installation contract is defined, but the production skill directories do **not** exist yet and these commands have **not** passed local or clean external installation testing.

Producer + evaluator — intended form to validate later:

```bash
npx skills add sb-dev/deep-research-skills \
  --skill deep-research \
  --skill research-evaluate \
  --agent claude-code
```

Pack creator only — intended selective-install form:

```bash
npx skills add sb-dev/deep-research-skills \
  --skill research-extension-pack-creator \
  --agent claude-code
```

All three — intended form:

```bash
npx skills add sb-dev/deep-research-skills \
  --skill deep-research \
  --skill research-evaluate \
  --skill research-extension-pack-creator \
  --agent claude-code
```

These are **specified installation contracts, not current installation instructions**. Installation becomes a product claim only after the later scaffold, local-validation and clean-consumer smoke-test stages pass.

## Quick start — PROV Primer publication status

The selected Level 1 quick start is deliberately small, public and keyless. It demonstrates:

```text
find
→ verify
→ cite
→ report uncertainty if necessary
```

Once the `deep-research` skill is actually scaffolded and installed, the exact example prompt is:

```text
Use the installed deep-research skill with no Extension Pack. Establish exactly what publication status and date the W3C PROV Model Primer gives itself. Begin at https://www.w3.org/TR/prov-primer/ and inspect its actual header and status section. Distinguish the Primer's own label from formal PROV Recommendations it links to. Give a supported answer with a precise locator. Do not infer implementation conformance from document status or expand into a review of all provenance standards.

Use frame, extract-evidence and synthesise only as needed. Bound discovery to 3 search queries and acquisition to 8 source reads/actions across the task. Use already-authorised tools only; no purchase, new paid provider run or external communication. Record the bounds before iterative collection and reserve effort for review. Stop optional collection once the bounded proposition is supported; a cap never proves sufficiency.

Write research/l1-01/research.md with identifiable question, source/inspection record, evidence, claim, answer, temporal scope and a clearly labelled producer self-check. Preserve uncertainty and unavailable-source limits. Do not invent source text or claim an independent review. Read any existing run before changing it and retain an identifiable prior revision. Return actual created paths and the supported answer or precise unresolved need. This is not an installation or provider benchmark.
```

Expected research output after a real run: `research/l1-01/research.md`.

The full example contract is [L1-01 in the progressive example design](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l1-01-prov-primer-publication-status).

## Learn by researching

The five levels increase **research responsibility**, not merely output length. The fifteen primary examples and their complete prompts are already specified, but they have not yet been executed through installed production skills.

### Level 1 — Find and verify one bounded answer

- **L1-01 — [PROV Primer publication status](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l1-01-prov-primer-publication-status)** — recover one official-source fact with an exact locator and temporal scope.
- **L1-02 — [Python requirement claim audit](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l1-02-python-requirement-claim-audit)** — audit a frozen proposition against package, server and README evidence without rewriting it.
- **L1-03 — [Repair-data count scope](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l1-03-repair-data-count-scope)** — distinguish the published count, unit, release date and observation period.

### Level 2 — Compare a small evidence set

- **L2-01 — [Scholarly metadata routes](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l2-01-scholarly-metadata-routes)** — compare Crossref, OpenAlex and Semantic Scholar against explicit evidence-access criteria.
- **L2-02 — [RULER report versions](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l2-02-ruler-report-versions)** — compare revisions of one work without counting them as independent studies.
- **L2-03 — [Small numeric repair comparison](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l2-03-small-numeric-repair-comparison)** — produce a reproducible descriptive comparison while retaining denominators and sampling limits.

### Level 3 — Produce a focused decision-ready report

- **L3-01 — [Long-context research evidence](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l3-01-long-context-research-evidence)** — use the `scholarly-evidence` profile to assess what benchmark evidence does and does not justify.
- **L3-02 — [Repair-software opportunity evidence](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l3-02-repair-software-opportunity-evidence)** — separate observed repair activity from untested market demand and willingness to pay.
- **L3-03 — [Optional research-engine adoption](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l3-03-optional-research-engine-adoption)** — use the `open-source-ecosystem` profile to distinguish documentary capability, static inspection and tests still required.

### Level 4 — Handle contested, scaled and changing evidence

- **L4-01 — [API-policy reconstruction and refresh](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l4-01-api-policy-reconstruction-and-refresh)** — reconstruct dated policy states and update only affected claims.
- **L4-02 — [Longitudinal repair-data reconciliation](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l4-02-longitudinal-repair-data-reconciliation)** — reconcile large snapshots without double-counting or hiding schema drift.
- **L4-03 — [Multi-repository evidence audit](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l4-03-multi-repository-evidence-audit)** — trace capability evidence across a bounded repository set and repair only the affected evidence chain.

### Level 5 — Run a research programme that feeds production

- **L5-01 — [Archival-research domain programme](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l5-01-archival-research-domain-programme)** — research a new Production Skills domain before architecture and qualify whether a new Extension Pack is justified.
- **L5-02 — [Watershed system for production](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l5-02-watershed-system-for-production)** — hand scientific mechanisms to game, world and narrative production without treating simulation as empirical proof.
- **L5-03 — [Evidence-linked briefing opportunity](docs/research-logs/2026-09-10-stage-12-progressive-examples.md#l5-03-evidence-linked-briefing-opportunity)** — combine market, technical and editorial evidence while leaving business, engineering and publication commitments with their owners.

## Project structure grows with the research

The research workspace should stay as small as the task permits. These are consumer-workspace patterns, not production directories that currently exist in this repository.

**One bounded answer**  
A compact `research.md` can hold the brief, source inspection, evidence, claim, answer and producer self-check when that remains unambiguous.

**A comparison needs separate review**  
Add a fixed-input `evaluation/audit.md` when independent evaluation is part of the task.

**Evidence volume or ownership starts to scale**  
Split source, evidence, claim and analysis records only when separate updates, access restrictions or reviewer ownership make the separation useful.

**A calculation or refresh is material**  
Add explicit calculation inputs/outputs or a `change-record.md` so the transformation and affected dependencies remain inspectable.

**A research programme feeds other domains**  
Add explicit handoff artefacts for the receiving production disciplines. The handoff carries evidence, uncertainty and unresolved owner decisions; it does not take over their work.

Keep the structure lean:

- logical research responsibilities do not require one physical file each;
- one authoritative value should not be duplicated across several records;
- historical issued research is preserved rather than silently overwritten;
- restricted evidence is referenced only within its permitted retention and audience boundary;
- a file hash can identify bytes but does not prove the underlying claim is true.

## Skills

### `deep-research`

Owns evidence-led research production from framing through discovery, extraction, claim analysis, synthesis, bounded follow-up and refresh.

Commands:

```text
frame
plan
discover
extract-evidence
analyse-evidence
follow-up-search
synthesise
refresh
```

### `research-evaluate`

Audits fixed research inputs and diagnoses failures without silently repairing the submission.

Commands:

```text
audit
diagnose-research-failure
```

### `research-extension-pack-creator`

Qualifies, designs, compares and revises reusable specialist research profiles.

Command:

```text
create-pack
```

The three skills are specified as independently installable. Their production packages have not yet been scaffolded.

## Extension Packs

Extension Packs specialise research behaviour without bloating the core. They may change source ecology, search strategy, eligibility, appraisal, method, synthesis, quality criteria and reporting conventions.

Precedence is:

```text
explicit research instructions
→ approved / locked research decisions
→ selected Extension Pack
→ core Deep Research defaults
```

The initial **design catalogue** contains:

- **`scholarly-evidence`** — publication/report/version handling and method-specific appraisal for bounded scholarly research.
- **`open-source-ecosystem`** — revision-bound repository evidence, licence/setup distinctions and separation of documented, statically inspected, executed and unknown capability.

Both have source-backed procedural demonstrations and differential design evidence. Neither is yet a production pack bundle or clean-install-validated product.

A project-specific brief is not an Extension Pack.

## Execution

The skills decide **what research work is needed**. Existing authorised tools execute it.

Execution may use:

- host-native web search and browsing;
- exact GitHub/file retrieval;
- specialist scholarly or structured-data APIs when the question requires them;
- document/PDF parsing;
- visual or multimodal inspection;
- local code/statistical analysis;
- optional hosted or self-hosted broad-research engines.

The core does not require one provider, one search API, one browser, one vector database or one orchestration framework.

Every executor remains below the research contract:

```text
research question
→ research semantics
→ bounded executor operation
→ evidence intake
→ claim / contradiction analysis
→ synthesis and review
→ authorised handoff
```

A provider report is evidence to inspect, not an automatic accepted answer.

## Evaluation / benchmarks

Evaluation is layered so different failure modes remain independently detectable:

1. structural integrity;
2. retrieval behaviour;
3. source and evidence quality;
4. citation and claim support;
5. synthesis quality;
6. preservation, diagnosis and repair;
7. temporal refresh;
8. Extension Pack behaviour;
9. end-to-end progressive research;
10. clean external installation.

The Stage 13 design includes regression fixtures for duplicate-source inflation, snippet/full-source disagreement, stale versus current official sources, retractions/corrections, report/study duplication, inaccessible primary evidence, contradictory high-quality evidence, unsupported synthesis, adjacent-but-non-entailing citations, missing subquestions and wasteful continued search.

Reference/design checks have been executed. Live installed-agent scores, clean installation and benchmarked-product status have **not** yet been established.

External benchmark work informs the architecture without defining it: BrowseComp, DeepResearch Bench, BrowseComp-Plus, ResearchRubrics and FINDER/DEFT contribute retrieval, citation, controlled-corpus, rubric and failure-diagnosis lessons.

## Documentation

### Canonical specifications

- [01 — Deep Research Skills System Specification](docs/01-deep-research-skills-system-spec.md)
- [02 — Workflows and Artifacts Specification](docs/02-deep-research-skills-workflows-and-artifacts-spec.md)
- [03 — Repository and Contracts Specification](docs/03-deep-research-skills-repository-and-contracts-spec.md)
- [04 — Testing and Benchmark Specification](docs/04-testing-and-benchmark-spec.md)
- [05 — Customisation and Extension Packs Specification](docs/05-deep-research-skills-customisation-packs-spec.md)
- [06 — Extension Pack Catalogue](docs/06-deep-research-skills-extension-pack-catalogue.md)

### Bootstrap evidence

- [Deep Research Skills bootstrap process](docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md)
- [Progressive example design — all 15 exact prompts](docs/research-logs/2026-09-10-stage-12-progressive-examples.md)
- [Evaluation architecture and regression fixtures](docs/research-logs/2026-09-10-stage-13-evaluation-design.md)
- [Bootstrap progress](docs/research-logs/bootstrap-progress.md)

## Project boundary

Deep Research Skills owns reusable **research production intelligence**: how to frame, discover, verify, triangulate, synthesise, cite, evaluate, repair and refresh evidence.

It does **not** own:

- the downstream product or strategy decision;
- software architecture or deployment;
- product design or unperformed user research;
- story, visual, music or game production;
- legal, medical, financial or other regulated professional judgement;
- rights clearance;
- business commitment, procurement or publication authority;
- a universal research runtime, evidence database or provider router.

Research can inform these domains. It does not inherit their authority.

## Contributing

The repository is still in its bootstrap sequence. A production `CONTRIBUTING.md` will be added only when the repository scaffold is created.

Until then, contributions to this branch should preserve the accepted canonical specifications, evidence/claim distinctions, stage boundaries and truthful implementation status rather than adding unvalidated production surfaces early.

## Licence

A project `LICENSE` file has not yet been added because repository scaffolding is a later bootstrap stage.

Do not infer project redistribution or reuse rights from the licences of referenced sources, tools or sibling repositories. Public licence wording belongs in this README only after the repository's own licence exists.
