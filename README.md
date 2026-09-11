# Deep Research Skills

**Conduct evidence-backed research, not isolated searches.**

Deep Research Skills coordinates **research production**: frame the question, choose an evidence strategy, inspect original sources, preserve provenance, analyse contradictions, synthesise what the evidence supports, audit material claims, and refresh only what changed.

It supports bounded fact-finding, comparisons, evidence synthesis, landscapes, source verification, research updates and research programmes that feed other Production Skills without taking over their decisions.

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

Research is bounded by evidence quality, authority and cost, not by how many sources an agent can collect.

```text
research need
→ question and decision framing
→ source strategy
→ bounded discovery and acquisition
→ evidence extraction
→ contradiction / alternative analysis
→ targeted gap search
→ synthesis
→ claim / citation audit
→ decision-ready output
→ bounded refresh
```

The governing controls are:

- **Question before retrieval.** Resolve the objective and decision context before broad search.
- **Direct evidence before repetition.** Prefer the most direct suitable source; several reports repeating one origin are not independent corroboration.
- **Source quality is multidimensional.** Directness, authority, method, transparency, recency, independence, incentives, specificity and stability remain separate concerns.
- **Contradictions stay visible.** Conflicting high-quality evidence is investigated or reported, not silently averaged away.
- **Uncertainty survives synthesis.** Source statement, observation, extracted data, inference, interpretation, forecast, recommendation, assumption and unknown remain distinguishable when the difference matters.
- **Time is part of the evidence.** Event, publication, effective, retrieved-at and valid-as-of dates are not interchangeable.
- **Use the cheapest adequate authorised operation.** Exact retrieval, metadata triage and targeted follow-up come before expensive broad research when they can resolve the uncertainty.
- **Preserve verified work.** Repair the smallest responsible evidence, claim or synthesis scope rather than regenerating everything.
- **Bound resource exposure.** Search, browser work, premium APIs, document retrieval, OCR, code execution, research engines, parallel workers and specialist review remain separate resource dimensions.
- **A cap is not sufficiency.** Hitting a resource limit can produce a limited result; it cannot turn incomplete evidence into a supported conclusion.

## Install

Install the producer and independent evaluator:

```bash
npx skills add sb-dev/deep-research-skills \
  --skill deep-research \
  --skill research-evaluate \
  --agent claude-code
```

Install the Extension Pack creator independently:

```bash
npx skills add sb-dev/deep-research-skills \
  --skill research-extension-pack-creator \
  --agent claude-code
```

Install all three:

```bash
npx skills add sb-dev/deep-research-skills \
  --skill deep-research \
  --skill research-evaluate \
  --skill research-extension-pack-creator \
  --agent claude-code
```

Inspect the available skills before installing:

```bash
npx skills add sb-dev/deep-research-skills --list
```

## Quick start — PROV Primer publication status

Start with one bounded official-source verification. The task demonstrates the core research loop:

```text
find
→ inspect
→ verify
→ cite
→ preserve temporal scope and uncertainty
```

```text
Use the installed deep-research skill with no Extension Pack. Establish exactly what publication status and date the W3C PROV Model Primer gives itself. Begin at https://www.w3.org/TR/prov-primer/ and inspect its actual header and status section. Distinguish the Primer's own label from formal PROV Recommendations it links to. Give a supported answer with a precise locator. Do not infer implementation conformance from document status or expand into a review of all provenance standards.

Use frame, extract-evidence and synthesise only as needed. Bound discovery to 3 search queries and acquisition to 8 source reads/actions across the task. Use already-authorised tools only; no purchase, new paid provider run or external communication. Record the bounds before iterative collection and reserve effort for review. Stop optional collection once the bounded proposition is supported; a cap never proves sufficiency.

Write research/l1-01/research.md with identifiable question, source/inspection record, evidence, claim, answer, temporal scope and a clearly labelled producer self-check. Preserve uncertainty and unavailable-source limits. Do not invent source text or claim an independent review. Read any existing run before changing it and retain an identifiable prior revision. Return actual created paths and the supported answer or precise unresolved need. This is not an installation or provider benchmark.
```

A first research workspace should stay small:

```text
research/
└── l1-01/
    └── research.md
```

## Learn by researching

The five levels increase research responsibility rather than merely output length. Each level contains three complementary primary examples.

### Level 1 — Find and verify one bounded answer

- **L1-01 — PROV Primer publication status** — recover one official-source fact with an exact locator and temporal scope.
- **L1-02 — Python requirement claim audit** — audit a frozen proposition against package, server and README evidence without rewriting it.
- **L1-03 — Repair-data count scope** — distinguish the published count, unit, release date and observation period.

### Level 2 — Compare a small evidence set

- **L2-01 — Scholarly metadata routes** — compare Crossref, OpenAlex and Semantic Scholar against explicit evidence-access criteria.
- **L2-02 — RULER report versions** — compare revisions of one work without counting them as independent studies.
- **L2-03 — Small numeric repair comparison** — produce a reproducible descriptive comparison while retaining denominators and sampling limits.

### Level 3 — Produce a focused decision-ready report

- **L3-01 — Long-context research evidence** — use the `scholarly-evidence` profile to assess what benchmark evidence does and does not justify.
- **L3-02 — Repair-software opportunity evidence** — separate observed repair activity from untested market demand and willingness to pay.
- **L3-03 — Optional research-engine adoption** — use the `open-source-ecosystem` profile to distinguish documentary capability, static inspection and tests still required.

### Level 4 — Handle contested, scaled and changing evidence

- **L4-01 — API-policy reconstruction and refresh** — reconstruct dated policy states and update only affected claims.
- **L4-02 — Longitudinal repair-data reconciliation** — reconcile large snapshots without double-counting or hiding schema drift.
- **L4-03 — Multi-repository evidence audit** — trace capability evidence across a bounded repository set and repair only the affected evidence chain.

### Level 5 — Run a research programme that feeds production

- **L5-01 — Archival-research domain programme** — research a new Production Skills domain before architecture design and qualify whether a new Extension Pack is justified.
- **L5-02 — Watershed system for production** — hand scientific mechanisms to game, world and narrative production without treating simulation as empirical proof.
- **L5-03 — Evidence-linked briefing opportunity** — combine market, technical and editorial evidence while leaving business, engineering and publication commitments with their owners.

## Project structure grows with the research

**One bounded answer**  
Keep the brief, source inspection, evidence, claim, answer and producer self-check together when one compact research file remains unambiguous.

**A comparison needs separate review**  
Add `evaluation/audit.md` when a fixed-input independent audit is part of the work.

**Evidence volume or ownership starts to scale**  
Split source, evidence, claim and analysis records only when separate updates, access restrictions or reviewer ownership make that useful.

**A calculation or refresh is material**  
Add explicit calculation inputs/outputs or a `change-record.md` so transformations and affected dependencies remain inspectable.

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

Use it when a task needs an evidence-producing workflow rather than one isolated lookup. It preserves source/evidence/claim distinctions, explicit authority and resource bounds, and existing verified work during repair.

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

Use it when research needs an independent pass over source quality, independence, coverage, claims, citations, freshness, contradictions, uncertainty or reproducibility. Evaluation writes a new review rather than mutating the producer's evidence.

Commands:

```text
audit
diagnose-research-failure
```

### `research-extension-pack-creator`

Qualifies, designs, compares and revises reusable specialist research profiles.

Use it when a recurring research context materially changes source ecology, method, eligibility, appraisal, synthesis or quality criteria. It checks the existing catalogue first and requires core-vs-pack differential evidence rather than creating cosmetic profiles.

Command:

```text
create-pack
```

## Extension Packs

Extension Packs specialise research behaviour without bloating the core. Explicit research instructions and accepted project decisions outrank pack defaults.

Initial research profiles:

- **`scholarly-evidence`** — publication/report/version handling and method-specific appraisal for bounded scholarly research.
- **`open-source-ecosystem`** — revision-bound repository evidence, licence/setup distinctions and separation of documented, statically inspected, executed and unknown capability.

A project-specific brief is not an Extension Pack. A valid pack must materially change research behaviour and remain independently testable against core-only research.

## Execution

The skills decide **what research work is needed**. Existing authorised tools execute it.

Execution may use:

- host-native web search and browsing;
- exact GitHub/file retrieval;
- specialist scholarly or structured-data APIs when the question requires them;
- document and PDF parsing;
- visual or multimodal inspection;
- local code/statistical analysis;
- optional hosted or self-hosted broad-research engines.

The core does not require one provider, one search API, one browser, one vector database or one orchestration framework.

```text
research question
→ research semantics
→ bounded executor operation
→ evidence intake
→ claim / contradiction analysis
→ synthesis and review
→ authorised handoff
```

A provider report is evidence to inspect, not an automatically accepted answer.

## Evaluation and benchmarks

Evaluation keeps different failure modes independently detectable:

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

Regression fixtures should cover duplicate-source inflation, snippet/full-source disagreement, stale versus current official sources, retractions/corrections, report/study duplication, inaccessible primary evidence, contradictory high-quality evidence, unsupported synthesis, adjacent-but-non-entailing citations, missing subquestions and wasteful continued search.

External benchmark families such as BrowseComp, DeepResearch Bench, BrowseComp-Plus, ResearchRubrics and FINDER/DEFT can inform individual evaluation dimensions without defining the complete quality model.

See [Testing and Benchmark Specification](docs/04-testing-and-benchmark-spec.md).

## Documentation

- [01 — Deep Research Skills System Specification](docs/01-deep-research-skills-system-spec.md)
- [02 — Workflows and Artifacts Specification](docs/02-deep-research-skills-workflows-and-artifacts-spec.md)
- [03 — Repository and Contracts Specification](docs/03-deep-research-skills-repository-and-contracts-spec.md)
- [04 — Testing and Benchmark Specification](docs/04-testing-and-benchmark-spec.md)
- [05 — Customisation and Extension Packs Specification](docs/05-deep-research-skills-customisation-packs-spec.md)
- [06 — Extension Pack Catalogue](docs/06-deep-research-skills-extension-pack-catalogue.md)

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

Contributions should preserve source/evidence/claim distinctions, independent evaluation boundaries, temporal validity, explicit authority and smallest-sufficient repair. Repository contribution guidance is defined in `CONTRIBUTING.md`.

## Licence

The repository licence is declared in `LICENSE`. Source documents, datasets, models, APIs and other third-party material retain their own licences and terms.