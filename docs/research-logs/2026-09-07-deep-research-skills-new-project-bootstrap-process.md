# Deep Research Skills — New Project Bootstrap Process

**Status:** Bootstrap specification  
**Date:** 7 September 2026

## 1. Purpose

This process defines how `deep-research-skills` moves from a project idea to a **scaffolded, benchmarked, installable open-source Agent Skills repository** for evidence-led deep research.

The project should help AI agents perform research as a production discipline rather than treating research as a single search call or long-form answer.

The core production loop is expected to resemble:

```text
research need
→ question / decision framing
→ research plan
→ source strategy
→ broad discovery
→ source triage
→ evidence acquisition
→ extraction + provenance
→ contradiction / alternative analysis
→ targeted gap search
→ synthesis
→ claim / citation audit
→ decision-ready research output
→ bounded update when evidence changes
```

The exact workflow must be validated through domain research before it becomes a skill contract.

`deep-research-skills` owns reusable research production expertise: how to frame, discover, verify, triangulate, synthesise, cite and evaluate evidence. It does **not** own the downstream product, design, narrative, code, market decision or other production output that consumes the research.

This boundary is important because Deep Research is a cross-domain input to many Production Skills families.

---

## 2. Governing Sources

Use the current Production Skills bootstrap and family contracts as canonical:

- `production-skills/docs/bootstrap/README.md`
- `production-skills/docs/bootstrap/new-project-process.md`
- `production-skills/docs/bootstrap/domain-research-process.md`
- `production-skills/docs/bootstrap/shared-abstraction-process.md`
- `production-skills/docs/specs/01-production-skills-family-system.md`
- `production-skills/docs/specs/02-production-skills-project-contract.md`
- `production-skills/docs/specs/03-production-skills-evaluation-and-extension-packs.md`
- `production-skills/docs/specs/04-cross-domain-orchestration-and-integration.md`

Compare mature family implementations only after the Deep Research domain model has been independently understood:

- `video-production-skills`
- `narrative-production-skills`
- `music-production-skills`

The UI/UX bootstrap is a useful depth reference, but newer family requirements take precedence, especially:

```text
six canonical specs
5 levels × 3 primary examples
first-class Extension Packs
pack-authoring capability
core-vs-pack differential evaluation
clean external installation smoke tests
```

---

## 3. Initial Domain Evidence

The bootstrap should begin from established research practice rather than current AI product behaviour.

Useful evidence families already identified for Stage 2 include:

### Evidence synthesis

- PRISMA 2020 for transparent systematic-review reporting;
- Cochrane guidance for explicit search strategies, sensitivity, study/report deduplication, selection and traceability;
- JBI evidence-synthesis and scoping-review methods.

### Analytical tradecraft

ODNI ICD 203 provides useful research-quality concepts that generalise beyond intelligence work:

```text
source quality and credibility
uncertainty
separation of evidence from assumptions / judgement
analysis of alternatives
clear logical argumentation
contrary information
customer relevance
```

### Decision-support analysis

UK Government Analysis Function guidance reinforces:

```text
clear analytical objectives
appropriate methods
quality assurance throughout the analytical lifecycle
peer review proportional to risk / impact
retrievable evidence and documentation
triangulation and synthesis
```

### Open-source investigation

Bellingcat's research-tool practice is useful for understanding source/tool selection, limitations, cost, difficulty, ethics and investigation-specific acquisition methods.

### Current AI research systems

Current systems such as OpenAI Deep Research, Gemini Deep Research and Perplexity Research demonstrate that planning, iterative retrieval, source control, uploaded/private sources, code/data analysis and cited synthesis can be provider capabilities. They are execution candidates, not definitions of the domain workflow.

### Existing research-agent evaluation

Reference benchmark families to investigate include:

```text
BrowseComp
DeepResearch Bench
BrowseComp-Plus
ResearchRubrics
FINDER / DEFT
```

They are useful evidence for evaluation dimensions such as retrieval persistence, citation correctness, report quality, factual grounding and reasoning. They must not become the project's complete quality model.

---

## 4. Required Bootstrap Outputs

The staged process must produce:

1. a clear Deep Research goal, scope and boundary;
2. research into professional research practice across several evidence disciplines;
3. a research-question and decision-context model;
4. a source, evidence, claim and provenance model;
5. a source ecology and acquisition strategy;
6. a domain-native workflow and artifact architecture;
7. an effort / cost / stopping strategy;
8. current AI research skill, agent, tool, API and provider research;
9. an execution-layer decision and gap analysis;
10. a justified core Agent Skills set;
11. decomposed commands where useful;
12. a first-class Extension Pack architecture;
13. an initial Extension Pack catalogue strategy;
14. a domain-native Extension Pack authoring skill or equivalent workflow;
15. five progressive research example levels;
16. three complementary primary examples per level selected by capability coverage;
17. deterministic and semantic evaluation;
18. benchmark, regression and reproducibility architecture;
19. six canonical specifications;
20. a public README following the proven Video Production Skills structure;
21. an open-source repository scaffold design;
22. Agent Skills installation and selective-installation contracts;
23. local validation and clean external installation smoke tests;
24. optional Pactwright integration kept outside core research semantics;
25. cross-domain abstraction candidates only after implementation evidence;
26. evidence-based maturity and publication gates.

---

# 5. Governing Principles

Retain the Production Skills family rules and specialise them for research.

## Evidence before synthesis

Do not write the conclusion first and search for support afterwards.

The research process must preserve a visible path from question to evidence to claims to synthesis.

## Question before retrieval

Resolve the research objective, decision context, scope and success criteria before expensive browsing.

A weakly framed question can make exhaustive retrieval wasteful rather than rigorous.

## Primary evidence before repeated secondary reporting

Prefer the most direct authoritative source available for a claim.

Do not treat several secondary articles repeating one underlying source as independent corroboration.

## Source quality is multidimensional

Do not collapse source quality into one opaque score.

Useful dimensions may include:

```text
directness / primary vs secondary
authority / expertise
methodological quality
transparency
recency / temporal validity
independence
conflicts / incentives
specificity to the claim
stability / archivability
```

## Evidence and judgement remain distinguishable

Research artifacts should distinguish:

```text
source statement
observed fact
extracted data
inference
interpretation
forecast
recommendation
assumption
unknown
```

## Contradictions are first-class evidence

Conflicting high-quality evidence must be represented, investigated and explained rather than silently averaged away.

## Uncertainty must survive synthesis

The final report should not become more certain than its evidence.

Confidence should be explained by evidence quality, coverage, agreement and known gaps rather than fake numeric precision.

## Time is part of the evidence model

For changing subjects distinguish, where relevant:

```text
event date
publication date
effective date
retrieved-at date
valid-as-of date
```

A current-looking source can describe old information.

## Cheapest adequate research operation

Use the cheapest operation capable of resolving the current uncertainty.

Examples:

```text
metadata / snippet triage before full-document retrieval
source map before broad crawling
claim-source matrix before polished prose
targeted follow-up search before rerunning the whole investigation
cached evidence before reacquisition
small citation audit before complete report regeneration
```

## Search breadth and synthesis depth are separate

More sources do not automatically produce better research.

Retrieval should optimise useful coverage and independence; synthesis should optimise relevance, correctness and explanatory power.

## Preserve verified evidence

If a later step reveals one weak claim, repair that claim, its evidence or the affected synthesis. Do not discard valid verified research unnecessarily.

## Research should be reproducible enough to audit

The repository should preserve enough information to understand:

```text
what was asked
what was searched
what was included / excluded
what was retrieved
what supported each material claim
what remained uncertain
when the research was valid
```

This does not imply a universal research database or exhaustive event log.

---

# 6. Bootstrap Flow

```text
PROJECT IDEA
    ↓
1. Define Project Goal and Boundary
    ↓
2. Research Professional Deep Research Practice
    ↓
3. Define Question, Evidence, Claim and Provenance Model
    ↓
4. Define Source Ecology and Acquisition Strategy
    ↓
5. Map Workflow and Artifacts
    ↓
6. Define Effort, Cost, Fidelity and Stopping Strategy
    ↓
7. Research AI Skills, Research Agents and Tools
    ↓
8. Choose Execution Layer
    ↓
9. Gap Analysis + Over-Engineering Guardrails
    ↓
10. Design Core Skills and Commands
    ↓
11. Design Extension Packs and Pack Authoring
    ↓
12. Design Progressive Examples
    ↓
13. Design Evals, Benchmarks and Regression Fixtures
    ↓
14. Generate Six Canonical Specs
    ↓
15. Design Public README
    ↓
16. Cross-Project Review
    ↓
17. Scaffold Repository
    ↓
18. Configure Skill Installation
    ↓
19. Local Validation
    ↓
20. Publish + Clean External Install Smoke Test
    ↓
21. Optional Pactwright Integration + Registry Promotion
    ↓
22. Review Shared-Abstraction Candidates
    ↓
READY FOR IMPLEMENTATION / MATURITY PROGRESSION
```

Do not scaffold `deep-research-skills` while generating this bootstrap. Execute the stages later, one at a time.

---

# 7. Stage 1 — Define Project Goal and Boundary

## Purpose

Define Deep Research as a reusable production discipline before proposing skills.

## Resolve

```text
What research outcomes does the repository own?
Who are the intended users?
What classes of research are in scope?
What is a research deliverable?
What counts as sufficient evidence?
Which decisions remain human-owned?
Where does reusable research end and consuming-project knowledge begin?
What downstream Production Skills receive research artifacts?
What are explicit non-goals?
```

Investigate whether the core should cover, at minimum:

```text
fact finding
landscape research
comparative research
case-study research
evidence synthesis
trend research
source verification
research updates / refreshes
```

Do not assume all specialist methods belong in core.

## Outputs

- project charter;
- boundary map;
- intended user / use-case map;
- quality definition;
- human decision points;
- non-goals.

## Key boundary hypothesis

```text
Deep Research
→ produces evidence, synthesis, uncertainty and traceable research artifacts

Consuming domain
→ interprets that research inside its own production responsibility
```

## Exit

A defensible domain boundary exists without a proposed skill count.

---

# 8. Stage 2 — Research Professional Deep Research Practice

## Purpose

Understand how strong researchers work before designing AI workflows.

## Research streams

Study several complementary traditions rather than treating one discipline as universal:

```text
systematic / scoping review
research synthesis
market / competitive intelligence
technology landscape research
investigative / OSINT research
journalistic verification
analytical tradecraft
policy / decision-support analysis
historical / archival research where useful
```

For each stream capture:

```text
roles
terminology
research protocol
source discovery
inclusion / exclusion
source appraisal
evidence extraction
deduplication
triangulation
contradiction handling
uncertainty
analysis / synthesis
review / QA
reporting
update behaviour
failure modes
repair strategies
```

## Questions

- When is exhaustive search required versus purposive coverage?
- How do experts decide a source is sufficiently direct and credible?
- How is source independence assessed?
- How are multiple reports of the same underlying study/event handled?
- How are negative, null or contradictory findings preserved?
- What research can be safely accelerated and what needs specialist review?
- What makes a report decision-ready rather than merely comprehensive?

## Outputs

- professional-practice research log;
- research-method comparison matrix;
- terminology glossary;
- domain failure taxonomy draft;
- candidate quality dimensions.

## Provisional

No single research tradition becomes the core workflow yet.

## Exit

The production model is grounded in real research practice rather than AI provider features.

---

# 9. Stage 3 — Define Question, Evidence, Claim and Provenance Model

## Purpose

Define the intellectual objects the skills must preserve.

## Model at least

### Research brief

```text
research objective
decision / downstream use
scope
out-of-scope
questions / subquestions
required freshness
source restrictions
quality threshold
budget / effort constraints
output form
```

### Source record

Candidate fields:

```text
source identity
source type
URL / DOI / repository reference
publisher / author
publication date
retrieved-at
primary / secondary relationship
methodology where relevant
included / excluded
exclusion reason
quality observations
known limitations
```

### Evidence item

```text
what the source directly supports
location / passage / data reference
source link
claim relevance
contradictions
confidence notes
```

### Claim

```text
claim text
claim type
supporting evidence
contrary evidence
inference level
temporal validity
confidence rationale
```

## Required distinctions

Do not collapse:

```text
source ≠ evidence ≠ claim ≠ synthesis ≠ recommendation
```

Do not require one universal knowledge graph. Start with the smallest artifacts that preserve traceability.

## Outputs

- research information model;
- provenance rules;
- source-quality dimensions;
- uncertainty model;
- temporal-validity rules;
- evidence-to-claim traceability contract.

## Exit

A final report can be traced back to evidence without forcing all research into one rigid schema.

---

# 10. Stage 4 — Define Source Ecology and Acquisition Strategy

## Purpose

Model where evidence comes from and how different source classes are acquired.

## Source classes to investigate

```text
official websites and documentation
scholarly literature
books / reports / PDFs
news and trade press
company / regulator filings
GitHub repositories, issues, releases and code
standards and specifications
datasets and APIs
social / community sources
archives and historical snapshots
uploaded / private project files
connected applications / internal sources
images, video and other multimodal evidence
```

## Acquisition paths to compare

```text
search engine
site-restricted search
provider deep-research agent
browser / browser automation
specialist API
GitHub API
Crossref / OpenAlex / Semantic Scholar / PubMed-like scholarly APIs
RSS / feeds
archive services
direct document retrieval
MCP / connector
local file search
code / data analysis
```

For each path record:

```text
coverage
precision
cost
latency
rate limits
authentication
licence / terms
reproducibility
data quality
freshness
multimodal support
failure modes
```

## Required behaviour

The system should be able to choose source and acquisition paths based on the question rather than always using general web search.

## Outputs

- source ecology;
- retrieval-path matrix;
- source-selection heuristics;
- fallback strategy;
- access / cost / licence constraints.

## Exit

The project knows how research requirements map to evidence sources and execution paths.

---

# 11. Stage 5 — Map Workflow and Artifacts

## Purpose

Derive the smallest credible end-to-end Deep Research workflow.

## Candidate workflow

```text
brief
→ frame questions
→ plan research
→ define source strategy
→ discover broadly
→ triage
→ retrieve
→ extract evidence
→ deduplicate underlying sources/events/studies
→ map evidence to questions / claims
→ analyse contradictions and alternatives
→ identify gaps
→ run targeted follow-up research
→ synthesise
→ audit material claims and citations
→ produce deliverable
→ record unresolved gaps / valid-as-of state
```

This is a hypothesis to validate in Stages 2–4.

## Candidate artifacts

```text
research/
├── brief.md
├── plan.md
├── sources/
│   └── source-register.*
├── evidence/
├── claim-source-matrix.*
├── contradictions.md
├── gaps.md
├── synthesis.md
├── report.md
├── provenance.*
└── evaluation/
```

Only add artifacts that improve traceability, reuse, evaluation or repair.

For every artifact define:

```text
purpose
creator
consumer
authoritative fields
update behaviour
approval / review behaviour
retention
smallest repair scope
```

## Outputs

- workflow map;
- artifact contracts;
- state / decision semantics where needed;
- handoff contracts;
- repair routes.

## Exit

A realistic research workflow can be executed without inventing missing semantics during implementation.

---

# 12. Stage 6 — Define Effort, Cost, Fidelity and Stopping Strategy

## Purpose

Translate cheap-first production into research effort management.

## Investigate effort levels

A likely progression is:

```text
question framing
→ metadata / quick-source scan
→ source map
→ focused retrieval
→ evidence table
→ targeted verification
→ full synthesis
→ specialist / exhaustive research only when justified
```

## Stopping criteria

Research must not use an unbounded "keep searching" loop.

Investigate criteria such as:

```text
all required subquestions have evidence
material claims have adequate direct support
major source classes are represented
new searches yield diminishing relevant evidence
important contradictions are explained or explicitly unresolved
freshness requirement is satisfied
budget / time ceiling reached with limitations reported
```

## Cost controls

Model:

```text
search calls
browser actions
premium API usage
full-document retrieval
OCR / multimodal analysis
code execution
provider deep-research runs
parallel agents
human specialist review
```

## Outputs

- research effort tiers;
- escalation rules;
- stopping rules;
- budget controls;
- refresh / incremental-update policy.

## Exit

The system can decide when deeper research is justified and when research is sufficient.

---

# 13. Stage 7 — Research AI Skills, Research Agents and Tools

## Purpose

Find reusable execution capability before implementing native tooling.

## Search categories

```text
Agent Skills for research / browsing / literature review / fact checking
provider deep-research agents
search APIs
browser automation
academic search APIs
GitHub research tools
PDF / document extraction
web extraction / crawling
citation tooling
reference managers
data analysis / code sandboxes
knowledge / note tools
MCPs and connectors
benchmark / eval frameworks
```

At minimum investigate current provider and open-source approaches including their APIs / integration surfaces where available.

## Candidate evaluation record

| Field | Meaning |
|---|---|
| Capability | What it actually does |
| Source | Repository/provider |
| Licence / terms | Reuse constraints |
| Maturity | Production readiness |
| Installation / access | Skill, CLI, API, MCP, app |
| Research role | Planning, retrieval, extraction, synthesis, evaluation |
| Source control | What evidence sources can be constrained |
| Citation behaviour | Claim/source traceability |
| Deterministic vs generative | Execution character |
| Provider coupling | Lock-in risk |
| Cost / latency | Operational implications |
| Composability | Fit beneath Production Skills |
| Maintenance | Current state |
| Gaps | Missing behaviour |
| Decision | USE / ADAPT / REFERENCE / REJECT |

## Important test

A provider feature that already performs broad iterative research should usually be treated as an execution engine unless it also provides the reusable production semantics this project must own.

## Outputs

- AI/tool landscape;
- shortlist;
- capability matrix;
- integration decisions;
- explicit gaps.

## Exit

The project knows what it should orchestrate rather than rebuild.

---

# 14. Stage 8 — Choose the Execution Layer

## Purpose

Separate Deep Research production intelligence from provider/tool execution.

## The repository should own

```text
question framing
research planning semantics
source strategy
quality / provenance rules
evidence extraction semantics
triangulation
contradiction handling
uncertainty
claim support
synthesis requirements
research repair
research-quality evaluation
```

## Existing tools should execute where suitable

```text
web search
browsing
specialist database search
GitHub retrieval
PDF retrieval / parsing
OCR / multimodal inspection
code / statistical analysis
provider deep-research runs
citation metadata lookup
archiving
```

## Outputs

- execution architecture;
- tool-selection policy;
- provider-boundary rules;
- fallback behaviour;
- offline / local opportunities where relevant.

## Exit

Deep Research remains provider-independent at the production layer without building a universal provider framework.

---

# 15. Stage 9 — Gap Analysis and Over-Engineering Guardrails

## Purpose

Compare the required research workflow with available execution capabilities.

## Classify

```text
covered
partially covered
missing
```

Pay particular attention to gaps in:

```text
source independence
primary-source preference
claim-level provenance
citation entailment
contradiction handling
uncertainty calibration
temporal validity
inclusion / exclusion traceability
research stopping criteria
incremental refresh
smallest-sufficient repair
cross-source deduplication
research benchmarkability
```

## Defer unless evidence proves necessary

Flag these as likely early over-engineering:

```text
custom general web crawler
custom search engine
universal provider registry
universal research workflow DSL
persistent cross-project evidence database
universal knowledge graph
vector database by default
multi-agent swarm by default
fully automated numeric source-quality score
continuous research daemon
universal citation format converter
research orchestration platform separate from Agent Skills
```

Each may become valid later, but only after real examples and benchmarks demonstrate the need.

## Outputs

- gap matrix;
- native capability shortlist;
- reuse decisions;
- deferred-improvement register;
- proof required before adding expensive architecture.

## Exit

The project owns only meaningful research gaps and has explicit protection against premature infrastructure.

---

# 16. Stage 10 — Design Core Skills and Commands

## Purpose

Derive the smallest installable skill set capable of the workflow.

Do not begin with a fixed number of skills.

## Lean starting hypothesis

Investigate whether the domain can initially be expressed as:

```text
deep-research
research-evaluate
research-extension-pack-creator
```

This is provisional until Stages 1–9 validate it.

### Possible `deep-research` commands

```text
frame
plan
build-source-strategy
discover
triage-sources
retrieve
extract-evidence
deduplicate
triangulate
analyse-contradictions
identify-gaps
follow-up-search
synthesise
refresh
```

### Possible `research-evaluate` commands

```text
audit-source-quality
audit-source-independence
audit-coverage
audit-claims
audit-citations
audit-freshness
audit-contradictions
audit-uncertainty
audit-reproducibility
diagnose-research-failure
```

Commands should exist only where isolated execution and evaluation improve the system.

## Skill design questions

- Is planning sufficiently distinct to justify its own installable skill?
- Should discovery and synthesis remain one skill to preserve the full research context?
- Which evaluation operations must remain independent to prevent self-grading?
- What state must survive between commands without creating a workflow runtime?
- Can selected commands be used independently by other Production Skills?

## Outputs

- skill responsibility map;
- command contracts;
- self-containment rules;
- skill dependency rules;
- initial SKILL.md outlines.

## Exit

Every installable skill has a coherent research responsibility and every command has an evaluation reason to exist.

---

# 17. Stage 11 — Design Extension Packs and Pack Authoring

## Purpose

Make specialist research modes first-class without bloating the core.

## Pack qualification rule

A pack should exist only when a reusable context materially changes:

```text
source ecology
search strategy
inclusion / exclusion rules
source appraisal
research methods
synthesis structure
quality criteria
reporting conventions
```

A project-specific research brief is not a pack.

## Candidate initial pack families

Research and narrow a catalogue from candidates such as:

```text
scholarly-evidence
market-intelligence
technology-landscape
open-source-ecosystem
trend-and-signal
creative-reference-research
investigative-osint          # likely later / specialist if complexity is high
```

These are hypotheses, not committed catalogue entries.

## Examples of material specialisation

### Scholarly evidence

May alter:

```text
source databases
query expansion
study/report deduplication
methodological appraisal
citation metadata
retraction / publication-status checks
reporting expectations
```

### Open-source ecosystem

May alter:

```text
GitHub discovery
repo / release / issue evidence
maintenance signals
licence checks
installation verification
popularity vs suitability interpretation
```

### Trend and signal

May alter:

```text
time windows
source freshness
signal vs noise treatment
leading / lagging indicators
longitudinal comparisons
confidence in emerging evidence
```

## Pack precedence

Retain the family expectation:

```text
explicit research instructions
→ approved / locked research decisions
→ selected Extension Pack
→ core Deep Research defaults
```

## Pack authoring workflow

The repository should eventually provide `research-extension-pack-creator` or equivalent:

```text
inspect catalogue
→ determine whether new pack is justified
→ research specialist method / source ecology
→ define boundaries and production grammar
→ define changed core behaviour
→ define pack-aware evaluation
→ implement
→ create showcase
→ include exact generation prompt
→ compare core vs core+pack
→ validate
→ catalogue
```

## Required differential evaluation

Every catalogue pack must demonstrate:

```text
core
vs
core + pack
```

The comparison must show changed research behaviour, not only pack metadata.

## Outputs

- pack semantics;
- pack format / packaging;
- initial catalogue strategy;
- pack authoring contract;
- showcase contract;
- pack evaluation plan.

## Exit

The project can explain what a valid research pack is and prove that it changes research appropriately.

---

# 18. Stage 12 — Design Five Progressive Example Levels

## Purpose

Teach and benchmark progressively broader research responsibility.

Target:

```text
5 levels × 3 primary examples = 15 primary examples
```

Do not lock the examples by intuition. For each level:

1. derive required capabilities;
2. research a broad candidate pool;
3. map candidates to a capability-coverage matrix;
4. remove redundant examples;
5. select the strongest complementary three;
6. verify coverage across all 15 examples.

Every primary example must contain the complete copyable generation prompt.

## Proposed level semantics

### Level 1 — Find and verify one bounded answer

Demonstrate:

```text
question framing
source selection
primary-source recovery
citation correctness
freshness
bounded verification
```

Candidate example classes:

```text
verify a technical/product fact against primary documentation
trace a public claim to its original source
resolve a current repository/licence/release fact
```

### Level 2 — Compare a small evidence set

Demonstrate:

```text
multiple source classes
comparison criteria
source independence
contradictions
small synthesis
```

Candidate example classes:

```text
compare three tools/providers for a defined production need
compare competing technical approaches
mini case-study comparison
```

### Level 3 — Produce a decision-ready research report

Demonstrate complete responsibility over a focused research question.

Candidate example classes should span distinct evidence ecologies, for example:

```text
scholarly evidence synthesis
market / competitive landscape
technology / open-source landscape
```

### Level 4 — Handle ambiguity, scale and contested evidence

Demonstrate:

```text
large source set
multi-hop retrieval
conflicting evidence
source duplication
longitudinal evidence
research repair
incremental follow-up
```

Candidate example classes:

```text
trend analysis with changing evidence
contested claim investigation
multi-source ecosystem / due-diligence study
```

### Level 5 — Run a research programme that feeds production

Demonstrate the complete project thesis and cross-domain handoff.

Candidate example classes:

```text
research a new Production Skills domain before architecture design
research a real-world system to feed game/world/narrative production
research a strategic opportunity combining market, technical and evidence constraints
```

The handoff should preserve evidence rather than replacing downstream domain judgement.

## Coverage matrix dimensions

Across the 15 examples cover:

```text
core skills
commands
source classes
acquisition paths
primary / secondary sources
fresh vs stable evidence
PDF / web / code / data / GitHub sources
contradiction handling
uncertainty
citation / provenance
research repair
Extension Packs
cross-domain handoffs
cost / stopping behaviour
installation paths
```

## Outputs

- five domain-native levels;
- candidate pool per level;
- capability matrix;
- selected 15 primary examples;
- exact prompts;
- expected artifacts;
- benchmark mappings.

## Exit

The examples demonstrate complementary research capability rather than repeated variants of one search pattern.

---

# 19. Stage 13 — Design Evals, Benchmarks and Regression Fixtures

## Purpose

Define quality evidence before large implementation.

## Evaluation layers

### Deterministic repository / artifact validation

Test where practical:

```text
required research metadata
source identities and timestamps
citation target resolution
claim-to-source references
missing source records
invalid artifact structure
duplicate identifiers
selective-installation integrity
skill self-containment
```

### Retrieval behaviour

Evaluate:

```text
source recall for known-answer cases
search reformulation
persistence
source diversity
primary-source recovery
specialist-source selection
avoidance of obvious duplicates
```

BrowseComp-like cases can inform this layer but are not sufficient alone.

### Source and evidence quality

Evaluate:

```text
directness
authority / methodology where relevant
independence
freshness
temporal validity
inclusion / exclusion reasoning
contrary evidence
```

### Citation / claim support

Evaluate:

```text
citation existence
citation correctness / entailment
citation completeness for material claims
citation placement
source-to-claim mismatch
unsupported inference
```

### Synthesis quality

Evaluate independently:

```text
question coverage
logical argument
cross-source integration
contradiction handling
uncertainty calibration
alternative explanations
scope discipline
decision relevance
clarity without evidence loss
```

### Preservation, diagnosis and repair

Test that the system can:

```text
identify the weak claim or missing evidence
preserve verified unaffected evidence
rerun only necessary retrieval
update dependent synthesis
avoid full-report regeneration when unnecessary
```

### Temporal / refresh evaluation

Create cases where:

```text
old authoritative source conflicts with newer official source
publication date differs from event/effective date
cached evidence remains valid for some claims but not others
```

### Extension Pack evaluation

Test:

```text
activation
non-activation
precedence
changed source strategy
changed research criteria
core-vs-pack differential behaviour
pack-aware quality evaluation
```

### End-to-end evaluation

Use progressive examples and independent held-out research cases.

### External installation evaluation

Run from clean consumer projects with no source-checkout assumptions.

## Failure fixtures to prioritise

```text
three articles repeating one original source presented as triangulation
search-result snippet contradicts full source
stale official page versus current official page
high-ranking SEO summary versus primary documentation
retracted / corrected scholarly source
multiple reports of one study treated as several studies
paywalled primary source with accessible secondary reporting
conflicting high-quality sources
unsupported confident synthesis
citation supports adjacent fact but not stated claim
broad report that misses one required subquestion
research loop that keeps searching after diminishing returns
```

## External benchmark references

Investigate using or adapting lessons from:

```text
BrowseComp                  → hard retrieval
DeepResearch Bench          → report + citation quality
BrowseComp-Plus             → controlled retrieval / corpus effects
ResearchRubrics             → realistic fine-grained report rubrics
FINDER / DEFT               → report requirements and failure taxonomy
```

Do not optimise the project narrowly to external benchmarks.

## Regression rule

```text
escaped research defect
→ diagnose owning layer
→ create smallest reproducible fixture
→ add deterministic or semantic eval
→ preserve as regression protection
```

## Outputs

- benchmark architecture;
- test taxonomy;
- domain quality dimensions;
- case format;
- progressive-example coverage map;
- pack differential suite;
- regression policy;
- release gates.

## Exit

The project can detect meaningful retrieval, evidence, citation and synthesis regressions separately.

---

# 20. Stage 14 — Generate Six Canonical Specifications

Generate:

```text
docs/
├── 01-deep-research-skills-system-spec.md
├── 02-deep-research-skills-workflows-and-artifacts-spec.md
├── 03-deep-research-skills-repository-and-contracts-spec.md
├── 04-testing-and-benchmark-spec.md
├── 05-deep-research-skills-customisation-packs-spec.md
└── 06-deep-research-skills-extension-pack-catalogue.md
```

## 01 — System

Owns:

```text
mission
scope and boundaries
principles
core skills
execution architecture
source/tool boundary
effort / cost / stopping policy
human review / commitment points
build order
system acceptance
```

## 02 — Workflows and Artifacts

Owns:

```text
research workflow
research brief
source register
evidence model
claim model
provenance
contradictions / gaps
synthesis
refresh semantics
failure taxonomy
repair routes
cross-domain handoffs
```

## 03 — Repository and Contracts

Owns:

```text
repository structure
SKILL.md contracts
command contracts
references / scripts / evals
self-containment
installation
selective installation
tooling
CI
technical acceptance
```

## 04 — Testing and Benchmark

Owns:

```text
evaluation layers
benchmark suites
case contracts
quality dimensions
citation / provenance eval
retrieval eval
synthesis eval
progressive-example coverage
pack evaluation
regression policy
release gates
measured evidence
```

## 05 — Customisation / Extension Packs

Owns:

```text
research-pack model
pack dimensions
activation and precedence
source / method specialisation
core-skill effects
pack packaging
pack-aware evaluation
pack-authoring workflow
boundaries
```

## 06 — Extension Pack Catalogue

Owns:

```text
curated initial packs
research production profiles
selection rationale
showcases
exact generation prompts
pack-specific evaluation
maturity / implementation state
```

## Exit

Implementation can proceed without inventing research architecture in code.

---

# 21. Stage 15 — Design the Public README

Follow the proven public structure of `video-production-skills`, adapted to research.

Target structure:

```text
# Deep Research Skills

positioning
research capabilities
research effort / evidence control
installation
quick start — strong Level 1 example

## Learn by researching
### Level 1 — 3 examples
### Level 2 — 3 examples
### Level 3 — 3 examples
### Level 4 — 3 examples
### Level 5 — 3 examples

## Project structure grows with the research
## Skills
## Extension Packs
## Execution
## Evaluation / benchmarks
## Documentation
## Project boundary
## Contributing
## Licence
```

## README positioning requirement

The README should make clear that the project coordinates **research production**, not merely browsing.

A useful positioning direction to test:

> Conduct evidence-backed research, not isolated searches.

Do not finalise public wording until examples prove what the repository actually does.

## Quick-start requirement

Choose a Level 1 example that visibly demonstrates:

```text
find
→ verify
→ cite
→ report uncertainty if necessary
```

without requiring specialist credentials or expensive APIs.

## Exit

The intended public product surface is clear before repository scaffolding.

---

# 22. Stage 16 — Cross-Project Review

Only now compare the independently derived Deep Research model with:

```text
video-production-skills
narrative-production-skills
music-production-skills
ui-ux-design-skills
software-engineering-skills when available
game-development-skills when available
```

Look for proven family patterns such as:

```text
cheap representation before expensive work
selection / approval semantics
artifact preservation
smallest-sufficient repair
skill-local commands
Extension Pack packaging
progressive examples
evaluation layering
clean installation
```

Record, but do not prematurely promote, candidates such as:

```text
source / provenance handoff contract
research brief handoff
valid-as-of metadata
cross-domain evidence package
```

Apply the family extraction rule:

> Share abstractions only after at least two independent production domains need substantially the same concept.

## Exit

Useful family patterns are reused without making Deep Research conform to another domain's workflow.

---

# 23. Stage 17 — Scaffold the Repository

Create only useful surfaces justified by the specs.

A likely baseline:

```text
deep-research-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── 01-deep-research-skills-system-spec.md
│   ├── 02-deep-research-skills-workflows-and-artifacts-spec.md
│   ├── 03-deep-research-skills-repository-and-contracts-spec.md
│   ├── 04-testing-and-benchmark-spec.md
│   ├── 05-deep-research-skills-customisation-packs-spec.md
│   ├── 06-deep-research-skills-extension-pack-catalogue.md
│   └── research-logs/
├── skills/
├── examples/
├── benchmarks/
├── tests/
├── tools/                    # only when justified
├── extension-packs/          # once packs are implemented
├── integrations/             # optional
└── .github/
```

Do not create empty directories merely to mirror another repository.

## Exit

A contributor can understand where production logic, examples, packs and evaluations belong.

---

# 24. Stage 18 — Configure Skill Installation

The project must be usable through the Agent Skills installation model.

Validate canonical installation such as:

```bash
npx skills add sb-dev/deep-research-skills   --skill deep-research   --skill research-evaluate   --agent claude-code
```

The exact skill names remain provisional until Stage 10.

Also test:

```text
selective installation
multiple supported agents where intended
skill-local references
skill-local commands
no undocumented repository-relative dependencies
```

## Exit

The intended installation contract is documented and testable.

---

# 25. Stage 19 — Local Validation

Before publication validate:

```text
repository structure
SKILL.md frontmatter / contracts
command discovery
required references
artifact validators
benchmark fixtures
Extension Pack structure when implemented
example prompt completeness
README claims
selective installation from local checkout / package
```

Keep this gate distinct from external installation.

## Exit

The source repository is internally coherent.

---

# 26. Stage 20 — Publish and Clean External Install Smoke Test

From a clean consumer project:

1. install the skills from GitHub using the documented command;
2. verify selected skills are discoverable;
3. run the Level 1 quick-start research task;
4. verify sources / evidence / report artifacts are produced as documented;
5. run evaluation;
6. confirm no source-checkout-relative dependencies exist;
7. test selective installation;
8. test at least one pack when packs are implemented.

## Exit

The repository works as an external Agent Skills product.

---

# 27. Stage 21 — Optional Pactwright Integration and Registry Promotion

If useful, add:

```text
integrations/pactwright.yml
```

It may describe compatibility and capability bindings only.

It must not move research workflow semantics into Pactwright.

Promote maturity only with evidence:

```text
proposed
→ researching
→ specified
→ scaffolded
→ working
→ benchmarked
→ mature
```

`working` requires a real installed end-to-end research example.

`benchmarked` requires meaningful retrieval/evidence/synthesis regressions to be detectable.

`mature` requires the family contract, including six spec responsibilities, progressive examples, Extension Packs, pack authoring, benchmark coverage and clean external installation.

---

# 28. Stage 22 — Review Shared-Abstraction Candidates

After implementation evidence exists, apply `shared-abstraction-process.md`.

Potential future candidates may include:

```text
research-to-production handoff metadata
source provenance conventions
valid-as-of semantics
citation evidence packages
```

Do not promote them merely because Deep Research is cross-domain.

In particular, avoid creating centrally shared:

```text
research runtime
universal evidence database
universal claim graph
universal source-quality score
universal provider router
universal research pack interpreter
```

without repeated independent domain evidence.

---

# 29. Research-Specific Acceptance Gates

Before `deep-research-skills` can be considered mature, evidence should demonstrate all of the following.

## Research behaviour

- questions are framed before expensive retrieval;
- source strategy responds to the question;
- primary/direct evidence is preferred where appropriate;
- duplicate secondary reporting is not mistaken for independent corroboration;
- material claims can be traced to evidence;
- contradictory evidence is represented;
- uncertainty is explicit;
- changing facts retain temporal context;
- synthesis answers the requested decision/research need;
- stopping behaviour is bounded;
- refreshes preserve still-valid evidence.

## Evaluation behaviour

- retrieval, evidence quality, citation support and synthesis can fail independently;
- approved / verified evidence is preserved during repair;
- smallest-sufficient research repair is possible;
- known failures become regression fixtures;
- packs materially change research behaviour and are differentially evaluated.

## Product behaviour

- core skills work without Extension Packs;
- 15 primary progressive examples exist with exact prompts;
- six canonical specification responsibilities exist;
- the README exposes implemented capability accurately;
- skills are self-contained;
- local validation passes;
- clean external installation passes;
- quality claims are backed by measured evidence or explicitly marked unmeasured.

---

# 30. Success Criterion

This bootstrap succeeds if a later session can execute each stage without redesigning the project from first principles.

The resulting `deep-research-skills` repository should make AI research:

```text
more systematic
more source-aware
more traceable
more temporally correct
more explicit about uncertainty
more resistant to duplicated / weak evidence
more efficient to update and repair
more useful to downstream production domains
```

while remaining a lean Agent Skills project rather than growing into a universal research platform before the need is proven.
