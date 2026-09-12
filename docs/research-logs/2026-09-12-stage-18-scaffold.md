# Stage 18 — Scaffold Repository and Preserve Public README

Date: 12 September 2026. Repository: `sb-dev/deep-research-skills`. Branch: `feat/bootstrap`.

Accepted parent: `5e2a4dcee7b93fb2e65e16149fa1861774640558`. Last completed stage: Stage 17 at `7b01cf7b07f51169b5624454e5c5b3448f55bfbb`. The parent adds only the continuation contract after that completion. Both GitHub ref readback and local Git history confirmed this chain before changes.

## Goal and governing authority

Create useful production packages and navigable public tasks while preserving the accepted research architecture and public README.

Requirement references used below:

- **A6:** active [amendment §6](2026-09-11-deep-research-bootstrap-stage-amendment.md#6-stage-18--scaffold-repository-and-preserve-public-readme).
- **E:** [execution contract](2026-09-12-bootstrap-execution-contract.md), especially §§1–5, 13–17.
- **O23/O29:** immutable [original specification](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md), original scaffold responsibility §23 and research-specific quality gates §29. The amendment maps original Stage 17 to active Stage 18.
- **R16:** accepted [README contract](2026-09-11-stage-16-public-readme-contract.md).
- **R17:** accepted [cross-project review](2026-09-12-stage-17-cross-project-review.md), including the Stage 18 preservation contract, and its machine-readable review/verification records.
- **C01–C06:** the six accepted canonical specifications under `docs/`.
- **S10/S12/S13:** accepted skill outlines and full command contracts; progressive example definitions; evaluation-design coverage map.

Stages 1–17 and the six canonical specifications remain unchanged. Old future-stage numbers in those historical files are interpreted through the amendment.

## Acceptance checklist extracted before implementation

| Required concern | Stage-specific obligation | Authority |
|---|---|---|
| Purpose and active section | Useful production scaffold with preserved public onboarding | A6; O23 |
| Historical quality gates | Preserve question/source/evidence/claim distinctions, provenance, temporal validity, honest review, bounded effort and repair; do not claim later behaviour from structure | O29; E §4; C01–C05 |
| Inputs | Active specification, complete amendment, progress, R16/R17, canonical specs, S10 full commands/outlines, S12 all selected prompts and S13 coverage | E §3; R17 |
| Prerequisites | Verify parent and accepted Stage 17 boundary; execute the historical Stage 16 checker against its accepted README; preserve earlier files | E §§2–3; R16 |
| Questions and decisions | Resolve repository licence with owner; preserve all prior architecture/example decisions | R16 licence section; Stage 16 claims ledger; E §2 |
| Research and sources | Inspect accepted domain material; retrieve the standard selected licence text and pin the CI checkout action | A6; C03 §§2, 13; E §14 |
| Implementation | Three self-contained packages, eleven accepted operations and the outlined local references; useful contribution/change/CI/check surfaces | R17 item 4; S10; C03 §§2–7 |
| Execution | Actually run deterministic README, example, package, link and history checks plus negative controls and skill-format validation | A6 deterministic protection; E §§1,13 |
| Comparisons and candidate discovery | No new domain/candidate study is required: consume accepted Stage 17 decisions and Stage 12 selected identities | A6; R17; E §3 |
| Analysis | Review owning write boundaries, shared evidence invariants, navigation, exact prompt identity and public/private separation | R16/R17; C03 §§5–7 |
| Deliverables and paths | `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, existing `docs/`, `skills/<name>/`, exactly 15 `examples/level-<n>-<slug>/README.md`, `tests/`, useful `.github/` workflow; no empty directories | A6; O23; C03 §2 |
| Exact counts/distribution/names | `deep-research`, `research-evaluate`, `research-extension-pack-creator`; 8/2/1 owned commands; 5 levels × 3 primary examples with L1-01 through L5-03 identity | R16/R17; S10/S12 |
| Prompts and examples | Every complete accepted prompt, problem, expected artefact and evaluation contract in its stable public README; complete L1-01 also inline at root | A6; R16; S12/S13 |
| Runtime evidence | Record actual commands, Python/platform identities, exit codes/stdout/stderr and explicit limits | E §§4,14 |
| Extension Packs | Package optional activation/precedence/authoring contracts; no pack implementation or comparison in this stage | R17; A6 versus amendment §8 |
| Tests and measurements | Exact structural checks and mutation detection; separate these observations from semantic research measurements | A6; E §13; C04 §2 |
| Installation | No local or external installation claim. Those are distinct Stages 21 and 23 | amendment §§9,11; E §§8,10 |
| Evaluation | Verify actual current-stage content and structure against governing requirements; preserve evaluator fixed-input boundary | E §13; R17 item 5 |
| README conformance | Required section order, unabridged prompt, 5 × 3 identity, substantive three-skill sections, public link closure and no process leakage; only authorised mechanical changes | A6; R16 |
| Claims ledger | Supplement internal evidence for licence, contribution, navigation and packages without changing the historical Stage 16 snapshot or making later claims | E §§3,14; R16 publication reconciliation |
| Research log | Record inputs, decisions, actual failures/repairs, conformance, exit and next-stage handoff | E §14 |
| Commit/remote gate | Stage-scoped commit only after checks pass; verify remote ref, parent, changed paths and immutable file identities | E §15 |
| Explicitly deferred | L1 execution/independent audit: Stage 19; all 15 runs, packs and authoring: Stage 20; installation: 21/23; broader validation: 22; promotion/integration: 24; abstractions: 25 | amendment §§7–13 |

## Inputs, provenance and decisions

The current branch, active contract and earlier evidence were read through the GitHub plugin and a clone of the same authorised branch. No rejected or unrelated branch was used as a source. `tests/fixtures/accepted-history.json` records SHA-256 identities for all 95 immutable input files at the accepted parent. The public contract fixture separately records the accepted README identity and all fifteen prompt hashes, output paths and evaluation requirements.

The accepted Stage 16 verifier ran against the original root README before editing: PASS, with all four of its negative controls detected. It remains unchanged. Its old exact-line negative fixture is historical; the new repository checker tests the permitted linked public format and stricter full-prompt preservation.

**Owner decision:** after the prior turn stopped at the explicit licence gate, the owner answered **“MIT”**. `LICENSE` uses the standard [Choose a License MIT text](https://github.com/github/choosealicense.com/blob/gh-pages/_licenses/mit.txt), retrieved through GitHub, with year 2026 and copyright holder Samir Benzenine. The licence text is also copied inside each independent skill package so selective distribution retains the notice. This is the only newly required owner decision.

The workflow pins `actions/checkout` v4.2.2 at `11bd71901bbe5b1630ceea73d27597364c9af683`, resolved through its GitHub tag ref. It requests read-only contents access, disables credential persistence and runs the same deterministic Python checks. Local execution is recorded; a configured workflow is not a claim that remote CI already ran.

## Production surfaces and materialisation

- `README.md`: exactly seventeen link substitutions, preserving all other bytes, including the complete Level 1 prompt and positioning.
- `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`: owner-selected licence, practical contributor workflow and an unreleased record of concrete changes.
- `skills/`: three entrypoints, eleven complete command contracts, fourteen local references and per-package licence notices. Commands remain semantic operations, with no new binary, runtime, provider router or shared store.
- `examples/`: exactly fifteen public pages. Prompts were extracted verbatim from S12; all expected paths were enumerated; evaluation text and S13 coverage/negative contracts were retained. Output paths are expectations, not claims that research has run.
- `tests/`: standard-library-only public/package/history checker, accepted-contract fixtures and mutation controls.
- `.github/workflows/validate.yml`: useful deterministic CI. `.gitignore` excludes Python bytecode created by these checks.

`benchmarks/`, `tools/`, `extension-packs/` and `integrations/` were not created because this stage has no implemented material for them. Contribution guidance identifies their responsibilities. This follows the explicit “as needed” and no-empty-directory rule; it does not defer a mandatory current-stage behaviour.

Package derivation:

| Production content | Accepted source and scope |
|---|---|
| Entrypoints | S10 skill outlines, including activation, dispatch, intake, review, output and repair |
| Commands | S10 full command sections and common invocation contract; historical stage references replaced with the equivalent bundled guidance |
| Evidence contract | C02 §§2–12, identical local copies in producer and evaluator |
| Source/execution | C01 §§6–7,10 |
| Effort/repair | C01 §§8–9; C02 §§13–15; accepted Stage 6 U01–U06 trigger table |
| Audit | C04 §§2,4–5,9–13; S10 audit focus semantics |
| Pack use/evaluation | Applicable C05 activation, precedence, composition, path and evaluation sections |
| Pack authoring | C05 §§2–17 as routed local references; C04 case/submission contracts |

Each local reference includes the actual applicable knowledge; no installed operation has to recover a historical log or sibling package. External catalogue snapshots named by a task remain explicit consumer inputs. The L5-01 prompt's historical catalogue URL is preserved exactly as an explicit research input, not used as public onboarding navigation.

## Failures and repairs

1. The first skill-format check rejected the optional `compatibility` frontmatter key in all three packages. The available skill-creator validator accepts name, description, licence, metadata and allowed-tools but not that key. The production packaging repair moved the same compatibility sentence into each skill body. No historical outline or compatibility meaning changed. All three reruns passed; the validator was not weakened.
2. Inspection found one copied “Stage 5 dependency rules” reference. It was replaced in the new local reference with “local evidence-contract dependency rules”; the complete dependency semantics are bundled. No accepted source was edited.

The deterministic checker and all mutation tests passed. These are structural results. No research execution, installed-host support, pack effect or general quality score is inferred.

## Conformance table

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| Correct parent and prerequisites | E §3; R16/R17 | GitHub ref, local parent chain, accepted Stage 16 checker | Readback and actual historical checker execution | PASS |
| Earlier evidence intact | E §2; amendment §2 | 95-file frozen manifest | Byte/content identity checks, including six canonical specifications | PASS |
| Useful scaffold and ownership | A6; O23; C03 §2 | Contribution map and actual nonempty surfaces | File/content inspection; unused directories absent | PASS |
| Owner-selected licence | R16 licence; E §2 | Explicit “MIT”; root and package notices | Actual licence text and resolving root link | PASS |
| Three self-contained skill packages | R17 item 4; C03 §§3–7 | Three entrypoints, eleven commands, fourteen references | Format checks; command ownership; complete semantic fields; package-local link checks | PASS |
| Core evidence/review boundaries | O29; R17 item 5; C01–C05 | Local evidence, effort, authority, pack and evaluator contracts | Content review; identical producer/evaluator evidence reference; write-scope mutation detection | PASS |
| Exactly fifteen public examples, 5 × 3 | A6; S12 | All `examples/level-*/README.md` pages and contract fixture | Exact paths, IDs, distribution, duplicates/missing/extra controls | PASS |
| All exact prompts, expected artefacts and evaluation contracts | A6; S12/S13 | Public task pages | All fifteen prompt hashes; output lists; retained evaluation text and negative criteria | PASS |
| Mechanical README preservation | A6; R16/R17 | Root README and accepted SHA-256 | Undo only seventeen permitted links; compare exact accepted bytes | PASS |
| Required sections and complete inline quick start | A6 deterministic protection; R16 | Root README | Heading order, substantive skills, exact prompt hash and shortening controls | PASS |
| Public and local link closure | A6 | Root, example, package, contribution and canonical-doc links | Target/anchor resolution; broken link/anchor and package escape controls | PASS |
| No public process leakage | A6; R16 | Root README | Rejected stage/branch/maturity/SHA/not-run/research-log route mutations | PASS |
| Executed validators and negative controls | A6; E §13 | Verification JSON and test output | Repository checker, 22 unittest methods including per-prompt and leakage subcases, three skill-format checks, diff check | PASS |
| Internal claims evidence updated honestly | E §§3,14; R16 | Stage 18 claims supplement | Claims map to actual scaffold evidence; historical ledger unchanged | PASS |
| Current-stage source/runtime evidence | E §14 | This log and verification JSON | Actual source identities, commands, outputs and runtime limits recorded | PASS |
| Additional candidate/domain research | E §3; A6 | Existing accepted S10/S12/R17 inputs | NOT APPLICABLE: current stage materialises accepted designs; no new selection required | NOT APPLICABLE |
| Research execution, pack comparisons and installation | amendment §§7–11 | Explicit later-stage handoff | NOT APPLICABLE: these are separate mandatory later stages, not Stage 18 exits | NOT APPLICABLE |
| Stage-scoped publication preparation | E §15 | Stage 18 files and explicit post-commit gate | Changed scope inspected; remote ref/parent/tree/blob verification is performed after commit creation as described below | PASS |

## Exit assessment and handoff

Stage 18 content and deterministic conformance are complete. The [verification record](2026-09-12-stage-18-verification.json) contains actual local execution evidence. The remote publication gate is performed after the containing commit exists and is recorded in a subsequent receipt; the conformance row is satisfied only after that readback succeeds, before continuation.

No unresolved Stage 18 owner question remains. Next is Stage 19: read the governing contracts again, use the actual packaged producer on the exact L1-01 prompt, preserve actual sources/runtime/output, freeze the submission and run the actual evaluator separately. Diagnose and repair only an observed owning defect, then re-evaluate changed scope. Stage 18 is not the L1 execution or installation proof.
