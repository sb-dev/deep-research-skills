# Stage 16 — Public README Conformance Repair

**Date:** 11 September 2026  
**Repository:** `sb-dev/deep-research-skills`  
**Branch:** `feat/bootstrap`  
**Historical parent:** Stage 15 completion at `18376f74db7e10b4a3a6363e8bca9c0c8e2c8977`

## Stage

Stage 16 — Public README Conformance Repair

## Completion requires

- preserve completed Stages 1–15 unchanged;
- adopt the current Production Skills public README separation rule;
- repair the root README into a public product/onboarding surface;
- remove bootstrap state, maturity narration and future-stage caveats from public copy;
- preserve the complete accepted L1-01 quick-start prompt;
- preserve exactly five levels × three accepted primary examples;
- preserve substantive sections for all three accepted skills;
- stop routing public example navigation through research logs;
- create the Deep Research README contract;
- create the internal public claims ledger;
- convert the branch bootstrap path into an active wrapper that preserves the immutable original specification and points future execution to the amendment;
- amend the future stage sequence to add missing implementation/progressive execution and final claims reconciliation;
- verify the repaired README deterministically;
- update the durable bootstrap progress record;
- publish as one Stage 16 commit directly on Stage 15.

## Why the repair is additive

Stage 15 is complete and remotely verified. Its research log, verifier and publication receipt are historical evidence and are not rewritten.

The defect is in the public-surface interpretation: Stage 15 deliberately made current scaffold/install/maturity state visible in the root README. The current Production Skills family README contract now separates:

```text
README.md
→ public product surface

docs/research-logs/
→ bootstrap state, maturity evidence and verification
```

The repair therefore supersedes the root README while retaining Stage 15's evidence as the record of the prior decision.

The branch bootstrap path is also converted into a migration wrapper. It links the immutable original specification for historical Stages 1–15 and makes the amendment authoritative for Stage 16 onward.

## Public README repair

The new README:

- opens with the product promise rather than bootstrap status;
- retains the accepted research-production positioning;
- retains the research effort/evidence control model;
- presents installation as the product installation surface rather than a schedule of later validation;
- preserves the complete L1-01 prompt inline;
- retains exactly L1-01 through L5-03, three per level;
- lists examples as product-facing entries without linking into `docs/research-logs/`;
- retains substantive sections for `deep-research`, `research-evaluate` and `research-extension-pack-creator`;
- explains the two accepted initial Extension Pack profiles without design/maturity bookkeeping;
- removes public Stage references and benchmark/install execution-status narration;
- removes the public Bootstrap evidence navigation section;
- makes Contributing and Licence product surfaces rather than explanations of when scaffold files will appear.

Public example links are deliberately deferred until the scaffold creates stable `examples/...` paths. The README uses plain product entries instead of temporary research-log links.

## Future-stage repair

The original future sequence jumped from scaffold to installation/validation without explicit implementation proof.

The new amendment preserves old responsibilities but inserts:

```text
16 Public README Conformance Repair
19 Implement and Prove Core Vertical
20 Expand Progressive Coverage and Extension Packs
```

and shifts the old future responsibilities accordingly through Stage 25.

This is necessary so later clean-install and maturity gates have actual implemented behaviour to validate.

## Verification performed

The Stage 16 README verifier checks:

- required public section order;
- complete L1-01 prompt markers;
- exactly five levels;
- exactly three primary examples per level;
- exactly the accepted fifteen example IDs;
- substantive sections for all three skills;
- all six canonical specification links;
- absence of `Stage <n>`, `feat/bootstrap`, bootstrap-progress narration, scaffold/maturity narration, `not-run` and `docs/research-logs/` links;
- installation and Extension Pack surfaces.

Negative controls verify that the checker detects:

1. injected stage-number leakage;
2. a research-log example link;
3. removal of one primary example;
4. removal of one core skill section.

The executed result is recorded in `2026-09-11-stage-16-verification.json`.

## Conformance

| Requirement | Evidence | Result |
|---|---|---|
| Preserve Stages 1–15 | no completed-stage research log/spec is edited | PASS |
| Product-facing README | repaired root README | PASS |
| Complete inline L1-01 prompt | root README | PASS |
| 5 × 3 progression | root README + verifier | PASS |
| Three substantive skills | root README + verifier | PASS |
| No research-log public example routing | root README + verifier | PASS |
| Internal claims separated | public claims ledger | PASS |
| Future sequence has implementation proof | governing amendment | PASS |
| Scaffold preservation defined | governing amendment + README contract | PASS |
| Final claims reconciliation defined | governing amendment + claims ledger | PASS |
| Deterministic negative controls | verification result | PASS |

## Exit assessment

The public README now represents the intended Deep Research product rather than the current bootstrap checkpoint.

Bootstrap execution state remains available under `docs/research-logs/`. Stage 17 is the next authorised stage under the amended sequence.