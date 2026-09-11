# Deep Research Skills Bootstrap Amendment — Public README and Implementation Sequence

**Status:** Governing amendment for `feat/bootstrap` after completed Stage 15  
**Date:** 11 September 2026  
**Applies to:** original bootstrap stages 16 onward

## 1. Reason for this amendment

Stages 1–15 of the original Deep Research bootstrap have already been executed and remain immutable historical work.

The completed Stage 15 README design mixed two concerns that the current Production Skills family contract now keeps separate:

```text
README.md
→ public product and onboarding surface

docs/research-logs/
→ bootstrap state
→ maturity evidence
→ verification
→ unresolved implementation and publication gates
```

The original future sequence also moved directly from repository scaffolding to installation configuration and validation without explicit stages to implement and prove the core research vertical or expand progressive examples and Extension Packs.

This amendment repairs those future responsibilities without rewriting completed stages.

## 2. Historical preservation rule

Do not modify, renumber or reinterpret completed Stages 1–15 as though they had been executed under this amendment.

Stage 15 remains the historical record of the original README-design decision. Stage 16 supersedes its **public surface**, not its evidence record.

The Stage 14 canonical specifications also remain historical accepted outputs. Where they refer to old future stage numbers, use the mapping in this amendment instead of editing those completed specifications merely to change numbering.

## 3. Superseded future sequence

The original future sequence was:

```text
16 Cross-Project Review
17 Scaffold Repository
18 Configure Skill Installation
19 Local Validation
20 Publish + Clean External Install Smoke Test
21 Optional Pactwright Integration + Registry Promotion
22 Review Shared-Abstraction Candidates
```

It is replaced by:

```text
16 Public README Conformance Repair
17 Cross-Project Review
18 Scaffold Repository and Preserve Public README
19 Implement and Prove Core Vertical
20 Expand Progressive Coverage and Extension Packs
21 Configure Skill Installation
22 Local Validation and Public README Conformance
23 Publish + Clean External Install Smoke Test + Claims Reconciliation
24 Optional Pactwright Integration + Registry Promotion
25 Review Shared-Abstraction Candidates
```

Mapping of unchanged original responsibilities:

| Original stage | Amended stage | Responsibility |
|---|---:|---|
| 16 | 17 | Cross-Project Review |
| 17 | 18 | Scaffold Repository |
| 18 | 21 | Configure Skill Installation |
| 19 | 22 | Local Validation |
| 20 | 23 | Publish + Clean External Install Smoke Test |
| 21 | 24 | Optional Pactwright Integration + Registry Promotion |
| 22 | 25 | Review Shared-Abstraction Candidates |

New responsibilities are Stages 16, 19 and 20.

## 4. Stage 16 — Public README Conformance Repair

### Purpose

Adopt the current Production Skills public README contract without rewriting Stage 15 history.

### Required outputs

1. corrected root `README.md`;
2. Deep Research README contract;
3. internal public claims ledger;
4. this future-stage amendment;
5. deterministic Stage 16 README verification;
6. updated bootstrap progress record.

### Public-surface rules

The README is a product surface. It must not narrate:

```text
stage numbers
bootstrap branch names
bootstrap progress
scaffold or maturity state
completion SHAs
verification counts
not-run bookkeeping
"implemented later" scheduling
```

The README must keep:

```text
positioning
research capabilities
research effort / evidence control
installation
complete inline Level 1 quick-start prompt
5 × 3 Learn by Researching
project structure that grows with the work
substantive sections for all core skills
Extension Packs
execution
evaluation / benchmarks
canonical documentation
project boundary
contributing
licence
```

At this pre-scaffold repair point, the fifteen public examples may be listed without links rather than pointing users into `docs/research-logs/`. Stage 18 creates their stable `examples/...` surfaces and mechanically adds those links.

### Exit

The root README is product-facing, the internal claims ledger is separate, and future scaffold work has an explicit preservation contract.

## 5. Stage 17 — Cross-Project Review

Retain the original Cross-Project Review responsibility and add the public-surface check.

Compare the independently derived Deep Research model with relevant Production Skills projects and family contracts.

In addition to the original architecture review, verify:

- the Stage 16 README contract still matches the current Production Skills public pattern;
- bootstrap/maturity evidence remains in research logs;
- the claims ledger remains internal;
- the complete quick-start prompt is preserved;
- the 5 × 3 progression remains intact;
- all three skills retain substantive public sections;
- no sibling-domain pattern reintroduces implementation-state narration into the README.

**Exit:** useful family patterns are reused without distorting Deep Research semantics or the public README contract.

## 6. Stage 18 — Scaffold Repository and Preserve Public README

Create only useful production surfaces justified by the accepted specifications.

The scaffold should establish, as needed:

```text
README.md
LICENSE
CONTRIBUTING.md
CHANGELOG.md
docs/
skills/
examples/
benchmarks/
tests/
tools/
extension-packs/
integrations/
.github/
```

Do not create empty directories merely for symmetry.

### README handoff

Adopt the Stage 16 README and Stage 17 review findings. Scaffold-time README changes are limited to mechanical publication work:

```text
link the selected repository licence
link CONTRIBUTING.md
create and link stable public example paths
correct factual repository paths created by scaffolding
```

Do not independently:

```text
change positioning
replace or shorten the Level 1 prompt
change the 5 × 3 progression
collapse skill sections into a table
add bootstrap/maturity narration
route public onboarding through research logs
```

### Public example surface

Create one stable public README for each primary example:

```text
examples/level-1-<example>/README.md
...
examples/level-5-<example>/README.md
```

Each may initially contain the accepted problem, exact prompt, expected artefacts and evaluation contract without pretending the example has already run.

Convert the root README's plain example entries to these public links.

### Deterministic README protection

Add repository checks for:

- required public sections and order;
- complete inline Level 1 prompt;
- five levels × exactly three primary examples;
- public example-link closure;
- substantive sections for all three skills;
- local link closure;
- absence of bootstrap-stage/maturity leakage.

**Exit:** the production scaffold exists, public examples are navigable, and the accepted README is preserved rather than redesigned around implementation state.

## 7. Stage 19 — Implement and Prove Core Vertical

Implement the minimum production packages and commands required for one real end-to-end research path.

Use L1-01 as the first proving vertical:

```text
research need
→ frame
→ source strategy / bounded plan
→ exact source inspection
→ evidence extraction
→ claim analysis
→ synthesis
→ fixed-input evaluation
→ bounded repair when needed
```

The proof must:

- use the actual `deep-research` implementation;
- produce the documented research artefact;
- preserve source/evidence/claim distinctions and temporal scope;
- run `research-evaluate` against fixed producer output;
- record actual inputs, outputs, tool/runtime identity and failures;
- correct only the owning layer if a defect is found;
- avoid treating the producer's self-check as independent evaluation.

A source-checkout or temporary local package path may be used for implementation proof. Clean external installation remains a later independent gate.

**Exit:** core producer and evaluator behaviour is demonstrated end to end on L1-01.

## 8. Stage 20 — Expand Progressive Coverage and Extension Packs

Expand from the proven vertical to the accepted progressive suite and initial specialist profiles.

### Progressive coverage

Execute all fifteen primary examples at their required fidelity. Preserve:

- exact accepted prompts;
- actual source/tool inputs;
- produced artefacts;
- evidence and citation review;
- limitations;
- any bounded repair.

Do not substitute prompt existence, filenames or structural validation for executed research behaviour.

### Extension Packs

Implement and evaluate the accepted initial profiles:

```text
scholarly-evidence
open-source-ecosystem
```

For each prove:

```text
core works without pack
core + pack materially changes intended research behaviour
explicit task instructions and accepted research decisions outrank pack defaults
pack-aware evaluation recognises intentional specialisation
core-vs-pack comparison uses comparable substantive inputs
```

Exercise `research-extension-pack-creator` on at least one valid catalogue/revision case and one rejection/reuse case so pack authoring is demonstrated rather than merely specified.

**Exit:** the main research progression and initial specialisation mechanism are demonstrated with real execution evidence.

## 9. Stage 21 — Configure Skill Installation

Retain the original installation responsibility after implementation exists.

Validate documented project-local installation for:

```text
deep-research
research-evaluate
research-extension-pack-creator
producer + evaluator
producer + selected pack where applicable
all three skills
```

Record the exact installer version, repository revision and target host for each supported claim.

Verify selective installation, skill-local references/commands and absence of undocumented source-checkout dependencies.

**Exit:** the installation contract is concrete and testable; this stage does not replace the clean external consumer test.

## 10. Stage 22 — Local Validation and Public README Conformance

Before publication validate:

```text
repository structure
SKILL.md contracts
command/reference closure
deterministic validators
benchmark fixtures
implemented Extension Pack structure
all fifteen public example prompts
local selective installation
README structure and local links
```

The README checker must reject public-facing process leakage such as:

```text
Stage <number>
feat/bootstrap
bootstrap progress
production scaffold
maturity promotion
completion SHAs
not-run bookkeeping
research-log links as the primary example route
```

The checker proves structure and leakage rules only. It does not prove research quality or the truth of public product claims.

Update the internal claims ledger with evidence gathered so far.

**Exit:** the source repository is internally coherent and its public surface conforms to the accepted contract.

## 11. Stage 23 — Publish, Clean External Install and Reconcile Public Claims

From a clean consumer project:

1. install the documented skill selection from GitHub;
2. verify discovery by each claimed host;
3. run the Level 1 quick-start;
4. verify documented research artefacts;
5. run fixed-input evaluation;
6. confirm no source-checkout-relative dependencies;
7. test selective installation;
8. test at least one implemented Extension Pack;
9. record exact revisions, installer versions and observed results.

Then reconcile every material README claim against the internal public claims ledger:

```text
supported
→ keep

partially supported
→ narrow to demonstrated scope

unsupported but required for release
→ finish the owning work or block publication

unsupported and non-essential
→ remove
```

README corrections at this gate remain product-facing. Do not expose the bootstrap schedule as an explanation for unsupported claims.

**Exit:** the repository works as an external Agent Skills product and every retained public claim has an identified evidence basis.

## 12. Stage 24 — Optional Pactwright Integration and Registry Promotion

Retain the original Pactwright boundary.

Any integration remains optional and must not move research semantics into Pactwright.

Promote maturity only from actual evidence. In particular:

- `working` requires the proven end-to-end installed research path;
- `benchmarked` requires meaningful regressions to be detectable;
- `mature` requires the full family contract, progressive execution, implemented Extension Packs, pack authoring, benchmark coverage and clean external installation.

## 13. Stage 25 — Review Shared-Abstraction Candidates

Retain the original shared-abstraction rule after implementation evidence exists.

Potential candidates may include:

```text
research-to-production handoff metadata
source provenance conventions
valid-as-of semantics
citation evidence packages
```

Do not centralise a research runtime, evidence database, claim graph, source-quality score, provider router or universal pack interpreter without repeated independent domain evidence.

## 14. Unchanged acceptance model

The original research-specific quality gates remain in force. This amendment changes the public-surface and implementation sequence; it does not weaken evidence, provenance, contradiction, uncertainty, temporal-validity, repair or evaluation requirements.