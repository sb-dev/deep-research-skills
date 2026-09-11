# Stage 16 — Deep Research Public README Contract

**Status:** Accepted target public-surface contract  
**Date:** 11 September 2026  
**Applies to:** root `README.md`

## Purpose

This contract defines the public README shape that future Deep Research scaffold and implementation work must preserve.

The root README is for somebody deciding whether to install and use Deep Research Skills. Bootstrap execution state, maturity evidence, verification receipts and unfulfilled stage gates belong in `docs/research-logs/`.

## Required order

```text
# Deep Research Skills
positioning
Research capabilities
Research effort and evidence control
Install
Quick start — PROV Primer publication status
Learn by researching
  Level 1 — exactly 3 primary examples
  Level 2 — exactly 3 primary examples
  Level 3 — exactly 3 primary examples
  Level 4 — exactly 3 primary examples
  Level 5 — exactly 3 primary examples
Project structure grows with the research
Skills
  deep-research
  research-evaluate
  research-extension-pack-creator
Extension Packs
Execution
Evaluation and benchmarks
Documentation
Project boundary
Contributing
Licence
```

## Domain control model

`Research effort and evidence control` is the Deep Research domain-control section.

It must keep visible the distinctions that govern reliable research:

```text
question before retrieval
source ≠ evidence ≠ claim ≠ synthesis ≠ recommendation
direct evidence before repeated reporting
contradictions remain visible
uncertainty survives synthesis
temporal validity is explicit
resource limits do not imply sufficiency
verified work is preserved during repair
```

## Quick start

The README must contain the complete accepted L1-01 prompt inline.

The prompt must retain:

- the W3C PROV Primer source URL;
- the distinction between the Primer's own status and linked formal Recommendations;
- a precise locator requirement;
- bounded discovery and acquisition;
- explicit authority/cost limits;
- `research/l1-01/research.md`;
- temporal scope and uncertainty;
- producer self-check labelled as such;
- no claim of independent review.

A research-log link is not a substitute for the prompt.

## Learn by researching

The accepted fifteen-example identity set is immutable unless a later explicit product decision reopens it:

```text
L1-01 L1-02 L1-03
L2-01 L2-02 L2-03
L3-01 L3-02 L3-03
L4-01 L4-02 L4-03
L5-01 L5-02 L5-03
```

At Stage 16, before the production scaffold creates `examples/`, the README may list these entries without links.

Stage 18 must create stable public example surfaces and mechanically convert the entries to `examples/...` links. Public onboarding must not route through `docs/research-logs/`.

## Skills

Every core skill receives its own substantive section.

### `deep-research`

Explain:

- end-to-end evidence-producing research responsibility;
- when it should be used;
- source/evidence/claim preservation;
- authority and resource bounds;
- bounded refresh/repair.

### `research-evaluate`

Explain:

- fixed-input independent audit;
- when it should be used;
- dimensions it can audit;
- no silent producer-input repair.

### `research-extension-pack-creator`

Explain:

- catalogue-first qualification;
- when a specialist profile is justified;
- core-vs-pack differential evidence;
- rejection/reuse as valid outcomes.

A compact responsibility table may supplement these sections later but must not replace them.

## Extension Packs

The public README may describe the accepted initial profiles:

```text
scholarly-evidence
open-source-ecosystem
```

It should explain what a research pack changes and what outranks it. Do not narrate pack implementation status through bootstrap-stage language.

## Execution

Keep provider/tool execution below the research contract.

The README should explain that Deep Research owns research semantics while authorised tools may perform search, browsing, exact retrieval, scholarly/API access, document inspection, multimodal analysis and local computation.

Do not present one provider or runtime as mandatory unless the architecture is explicitly changed.

## Evaluation

Explain layered evaluation without collapsing quality into one number.

The public surface may link to canonical benchmark/evaluation documentation. Measured claims are governed by the internal public claims ledger and final publication reconciliation.

## Documentation

The public Documentation section should link the six canonical product specifications.

Bootstrap research logs are not primary product onboarding and must not appear as a public "Bootstrap evidence" navigation section.

## Contributing and licence

Keep both public sections.

Before scaffold files exist, the target README may refer to `CONTRIBUTING.md` and `LICENSE` as repository product surfaces without linking to nonexistent files. Stage 18 adds the actual files and links mechanically.

Do not choose or imply a specific licence unless that owner decision exists.

## Prohibited public leakage

The root README must not contain public-facing text such as:

```text
Stage 15
Stage 16
Stage N
feat/bootstrap
bootstrap progress
bootstrap sequence
production scaffold
maturity promotion
completion SHA
verification count
not-run
"not yet scaffolded"
"implemented later"
```

A genuine product limitation may be stated when users need it, but in product terms rather than bootstrap-schedule terms.

## Scaffold preservation

Stage 18 may change the README only to:

- link real `LICENSE` and `CONTRIBUTING.md`;
- create and link stable public example surfaces;
- correct repository paths introduced by scaffolding.

It must not:

- change positioning;
- replace/shorten the quick-start prompt;
- alter the 5 × 3 progression;
- collapse skill sections;
- introduce bootstrap/maturity prose;
- point examples back to research logs.

## Publication reconciliation

The target README can describe intended product capability during bootstrap.

Before public release/merge, Stage 23 reconciles the internal claims ledger against actual implementation and evaluation evidence. Unsupported claims are narrowed, completed or removed without exposing the bootstrap schedule.