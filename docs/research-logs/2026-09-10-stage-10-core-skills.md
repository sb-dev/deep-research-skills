# Stage 10: Core Skills and Commands

Date: 10 September 2026. Branch: `feat/bootstrap`. Scope: skill and command design; no installation or working-capability claim.

## Authority, inputs and acceptance checklist

The governing acceptance contract is [bootstrap section 16](2026-09-07-deep-research-skills-new-project-bootstrap-process.md#16-stage-10--design-core-skills-and-commands), read from `main`, blob `8ff62c92bada2861ece3684a9e73a83da75d9d94`. Sections 5 and 29 preserve evidence-first work, uncertainty, bounded effort, repair, self-containment and honest maturity. Sections 17–20 and 23–26 assign detailed packs, examples, evaluations, canonical specs, production scaffolding and installation to their own stages.

The starting parent is the remotely verified Stage 9 completion record `318e61cd55b736730f0830b26334d677228eecb7`. The [Stage 9 analysis](2026-09-10-stage-09-gap-analysis.md) and [receipt](2026-09-10-stage-09-publication-receipt.md) establish the accepted native responsibilities and deferred infrastructure. Earlier input responsibilities are the [Stage 1 boundary](2026-09-10-stage-01-project-goal-and-boundary.md), [Stage 2 method distinctions](2026-09-10-stage-02-method-comparison.md), [Stage 3 information model](2026-09-10-stage-03-question-evidence-claim-model.md), [Stage 4 source routing](2026-09-10-stage-04-source-ecology.md), [Stage 5 workflow](2026-09-10-stage-05-workflow-and-artifacts.md) and [complete artefact contracts](2026-09-10-stage-05-artifact-contracts.md), [Stage 6 effort policy](2026-09-10-stage-06-effort-and-stopping.md), [Stage 7 landscape](2026-09-10-stage-07-ai-tool-landscape.md) and [Stage 8 execution boundary](2026-09-10-stage-08-execution-layer.md). The current Stage 5 artefact contracts and Stage 8 selection/intake/repair rules were directly re-read for this packaging decision; the accepted source and research semantics are preserved, not redefined by a provider.

The current family [Project Contract](https://github.com/sb-dev/production-skills/blob/main/docs/specs/02-production-skills-project-contract.md), version 1.2, blob `c4f80ac407901b96081aa44a2d551d30a4beda84`, was read in full. Its sections 8–13 require bounded skill-local commands, self-containment and standalone use; sections 16–18 distinguish designed, working and mature capabilities.

| ID | Completion requirement | Specification reference |
|---|---|---|
| R01 | Derive packaging from accepted responsibilities, comparing alternatives rather than starting with a fixed count. | Section 16 Purpose and hypothesis. |
| R02 | Investigate all three suggested skill roles and answer all five design questions. | Section 16 hypothesis and Skill design questions. |
| R03 | Assess all fourteen production and ten evaluation command candidates; keep only justified independent operation surfaces. | Section 16 Possible commands and command rule. |
| R04 | Define coherent ownership and complete command inputs, work, outputs, authority, review, failure and evaluation reasons. | Section 16 responsibility-map/command-contract outputs and Exit. |
| R05 | Define skill self-containment and dependencies, including selective standalone use and persistent command state. | Section 16 self-containment/dependency outputs; family sections 8–13. |
| R06 | Produce initial SKILL.md outlines for every selected skill, with clear activation, dispatch and bundled-resource boundaries. | Section 16 outline output. |
| R07 | Verify all five output responsibilities and preservation of earlier decisions; record actual checks, stage-scoped publication and limitations. | Execution instructions sections 5–9; section 16 Exit. |

There is no required number of skills or final commands. The explicit candidate inventories contain 3 skill roles, 14 production commands, 10 evaluation commands and 5 questions. All are assessed below. No live installation, provider comparison, fifteen-example set, detailed pack catalogue or production directory is required in Stage 10. Initial outlines are required design artefacts, not substitutes for a current implementation requirement.

## Investigation and source basis

The method was responsibility-to-boundary comparison: start from Stage 9 N01–N06 and Stage 5 W01–W08; compare packaging alternatives; assess each proposed command against distinct inputs, write ownership and observable failure; then challenge selective installation and review separation. No mature sibling production workflow was copied; the cross-project review remains Stage 16.

Two current primary documentation checks resolved packaging assumptions, not professional research methodology:

| ID | Source actually inspected | Finding and bounded design consequence |
|---|---|---|
| N1 | Agent Skills, [Specification](https://agentskills.io/specification), directory/frontmatter, progressive-disclosure and file-reference sections; accessed 10 September 2026. No publication date asserted. | Skills use SKILL.md metadata/instructions with optional bundled resources; required name/description constraints and local reference conventions were checked. Main instructions should remain focused. The format does not itself implement research workflow or certify behaviour. |
| N2 | Anthropic, [Extend Claude with skills](https://code.claude.com/docs/en/skills), invocation, supporting-files, arguments and tool-permission sections; accessed 10 September 2026. | Skill invocation and argument handling are host-specific; supporting files need explicit navigation. The documented allowed-tools field pre-approves actions rather than restricting all available tools. Do not claim a commands directory creates universal slash commands or that frontmatter supplies a security boundary. |

Official documentation was opened after targeted searches for SKILL.md packaging and skill arguments. Third-party mirrors and directories were not used as authority. These are documented format/host behaviours, not tests of this repository’s installation. No host process, provider research job or paid service was launched. The design and synthetic checks below are generated project work, distinguished from those source claims.

## 1. Skill responsibility map

### Alternatives and selection

| Alternative | Advantage | Boundary cost / failure | Decision |
|---|---|---|---|
| One universal skill for production, evaluation and pack creation | Few installation entries. | Authoring, independent review and specialist-package changes become difficult to isolate; unrelated authoring content loads for ordinary research. | Reject as the full package boundary. |
| Two skills: production plus evaluation, with pack authoring inside production | Independent audits remain possible. | Pack authors need a separate reusable packaging/change workflow rather than ordinary research or a hidden mode that edits reusable defaults. | Reject the authoring placement, not the two research roles. |
| Three roles: research production, research evaluation, pack authoring | Distinct consumers, mutation boundaries and activation; production retains full research context. | Requires explicit portable handoffs and enough local contract knowledge in each package. | Adopt with the contracts below. |
| Split planning, discovery, extraction and synthesis into separate installed skills | Narrow activation per operation. | Repeats brief/support rules and adds required coordination without evidence of distinct installation needs. | Keep these as skill-local commands; reconsider only with observed use and evaluation evidence. |
| One skill per Stage 9 native responsibility or every command | Superficially mirrors the gap map. | Confuses responsibility coverage with packaging and magnifies dependencies. | Reject; N01–N06 are not a six-skill requirement. |

The comparison supports the original three-role hypothesis for specific ownership reasons, not because it was prescribed as a fixed count.

| Skill | Owns | Does not own | Normal output / standalone use |
|---|---|---|---|
| `deep-research` | End-to-end W01–W08 production; Stage 9 N01–N04/N06; baseline honest self-check and repair. | Independent review verdicts, qualified human authority, provider runtimes, downstream production decisions or reusable pack publication. | Supported research or the explicitly authorised limited outcome, with evidence, scope and validity. Works without another skill or pack when the task does not require separate review. |
| `research-evaluate` | N05: source/evidence/claim/report audit and diagnosis against fixed input revisions; independent findings in A11. | Editing the submission, silently changing expected outcomes, performing the proposed repair, or granting publication/professional approval. | Read-only assessment of research from any producer, including a third-party report; separate review output only. |
| `research-extension-pack-creator` | Qualification, specialist method research and creation/revision of reusable behavioural specialisations, showcases and evaluation contracts. | Project-specific research truth, automatic activation, core-default changes, catalogue publication or unperformed differential acceptance. | Existing-pack recommendation, requested pack draft, or accepted package only after required actual evidence; its local authoring contract is sufficient without sibling source checkout files. |

### End-to-end responsibility coverage

| Workflow | Production operation | Authoritative records / separate review |
|---|---|---|
| W01 | frame | A01 and genuine owner decisions; no acquired facts invented. |
| W02 | plan | A02 method/source/effort plan; source selection remains A03. |
| W03 | discover | A02 actual searches and A03 eligibility/access; coverage audit reads them. |
| W04 | extract-evidence, then analyse-evidence for origin relations | A03/A04/A10; extraction, source-quality and independence checks remain distinct. |
| W05 | analyse-evidence | A05–A07 claims, contradictions and gaps; evaluator audits without rewriting them. |
| W06 | follow-up-search | Bounded re-entry and A07 outcome; evidence and resource state are integrated, not reset. |
| W07 | synthesise plus applicable audit | A08/A09 exact draft; producer self-check and separately created A11 audit remain distinguishable. |
| W08 | synthesise for authorised issue; refresh for corrected handoff | A09 issued revision and real delivery status, with applicable A11 review. No default external side effect. |

All Stage 9 N01–N06 responsibilities are covered by this map: framing/planning; evidence intake; claim analysis; follow-up/refresh; separate evaluation; and evidence-bound synthesis/handoff. Pack authoring is the distinct reusable-specialisation responsibility required by the bootstrap, not an unfulfilled research gap disguised as another engine.

### Answers to all five design questions

**Q1: Separate planning skill?** No. Planning is independently useful but shares the brief, source policy and effort semantics with execution. The `frame` and `plan` commands provide isolated entry points and tests without another installable package. A later split requires demonstrated independent installation value, not a desire for more agents.

**Q2: Keep discovery and synthesis together?** Yes, within the production skill, with separately inspectable commands and records. One coherent context preserves how sources were selected and what they actually support. This does not force a full rerun: a caller can request discovery, extraction or synthesis only when its input contract is met.

**Q3: Which evaluation must be independent?** Claim entailment, source independence/quality, coverage, citation support, freshness, contradictions, uncertainty and reproducibility retain independently callable audit scopes and criterion-level verdicts. The reviewer reads a fixed submission, not an editable report, and does not take the author’s PASS as ground truth. An independent invocation or role does not establish independent human expertise; required human review remains literal. Core-only research performs labelled self-checks, never labels them independent acceptance, and blocks issue when the brief mandates unavailable separate review.

**Q4: What state survives?** A01 brief/authority and revisions; A02 planned/actual method, source strategy and finite resources; A03 identities/access/selection/origins; A04 inspected evidence and locators; A05 claims/support/premises; A06 contradictions; A07 gaps/attempts; A08 synthesis; A09 exact report/revision/delivery; A10 material transformations and outstanding operation IDs; A11 actual review/decision receipts. These remain consumer-owned records, often compact sections. Neither hidden model memory nor a workflow runtime is required.

**Q5: Can other families call selected commands?** Yes. They supply the required semantic input records and explicit operation, without installing a planner or provider stack. Examples include framing an engineering comparison, extracting a cited design study, auditing a market claim or refreshing one creative reference. The contract accepts a compatible caller-owned format; missing support is not invented by an adapter. Consumer decisions remain consumer-owned.

## 2. Command selection and contracts

Eight production commands, two evaluator commands and one pack-authoring command survive the boundary test. All eleven complete contracts, including one copyable invocation per command, are in [Command Contracts](2026-09-10-stage-10-command-contracts.md). These are design-level invocations, not the fifteen primary examples or executed agent outputs.

### Disposition of all fourteen production candidates

| Candidate | Selected operation | Reason |
|---|---|---|
| frame | `frame` | Independent authorised-brief output; no acquisition needed. |
| plan | `plan` | Method and bounded next action can be evaluated separately. |
| build-source-strategy | `plan` | Shares A02 authority with method and evidence needs; an isolated focus needs no separate command. |
| discover | `discover` | A source map/selection batch is a useful bounded output. |
| triage-sources | `discover` | Keep eligibility and exclusions with the actual discovery record; permit a supplied-candidate-only focus. |
| retrieve | `extract-evidence` | Use native retrieval beneath the evidence contract; do not add a command that merely wraps fetch. Cached or supplied originals remain valid inputs. |
| extract-evidence | `extract-evidence` | Locatable faithful evidence has distinct inputs and repair tests. |
| deduplicate | `analyse-evidence` | Assess representation/report/origin relations in the same support context; exact record triage can occur earlier. |
| triangulate | `analyse-evidence` | Independence affects claims, contradictions and confidence together. |
| analyse-contradictions | `analyse-evidence` | Allow focused conflict analysis without a competing store or separately authoritative verdict. |
| identify-gaps | `analyse-evidence` | Gaps are consequences of coverage/support analysis, not an ungrounded task list. |
| follow-up-search | `follow-up-search` | A discriminating bounded action and its real effect need separate evaluation. |
| synthesise | `synthesise` | Exact report wording and handoff are distinct from evidence extraction. |
| refresh | `refresh` | Delta acquisition, prior-state preservation and invalidated review need their own contract. |

### Disposition of all ten evaluation candidates

| Candidate | Selected operation / focus | Reason |
|---|---|---|
| audit-source-quality | `audit`, source-quality | Claim-relative appraisal remains separately reported, not an opaque score. |
| audit-source-independence | `audit`, source-independence | Test originating observations rather than URL counts. |
| audit-coverage | `audit`, coverage | Compare brief/method obligations with actual search and answer scope. |
| audit-claims | `audit`, claims | Assess support, inference and qualifiers without authoring changes. |
| audit-citations | `audit`, citations | Separate identifier/placement checks from source entailment. |
| audit-freshness | `audit`, freshness | Check applicability and actual validity basis, not request date alone. |
| audit-contradictions | `audit`, contradictions | Preserve eligible opposition and justified reconciliation. |
| audit-uncertainty | `audit`, uncertainty | Check faithful uncertainty wording; do not imply measured general calibration. |
| audit-reproducibility | `audit`, reproducibility | Inspect records, versions, transformations and access limitations. |
| diagnose-research-failure | `diagnose-research-failure` | Locate defect ownership and repair scope without applying the repair. |

Audit focus is explicit operation input, not nine silently registered host commands. Every focus can fail independently and can be invoked alone. The `create-pack` command is justified by distinct reusable-package authoring and acceptance, rather than being added as another report mode. The detailed specialist catalogue and differential protocol remain Stage 11 responsibilities.

## 3. Self-containment rules

Each selected skill contains its own SKILL.md dispatcher, command files and the small local references needed to interpret its inputs, permissions, output and review limits. An installed skill must not resolve `../../docs`, a sibling skill’s directory, a development workspace or this research log to perform its advertised core responsibility. Links to primary documentation may support optional further research but must not be hidden prerequisites for interpreting local records.

Keep main instructions focused and load command/reference content on demand. Local knowledge duplication is limited to the small common semantic boundary genuinely needed by each independently installable package. At build/validation time compare those invariants for drift; do not solve a few repeated contract paragraphs with a mandatory shared runtime or central evidence database. Extended production procedures remain with the producer, appraisal criteria with the evaluator, and specialisation authoring with the creator.

Caller-owned research files are explicit inputs, not missing package dependencies. Source access, credentials, optional local programs, model weights and provider accounts are declared separately and checked only when a chosen operation needs them. Core framing, existing-evidence analysis and local review require no new paid service. Missing current external evidence still limits the actual research task.

Package paths resolve from the installed skill root; research input/output paths resolve from the explicitly identified consumer workspace. Do not assume shell working directory equals skill directory. Scripts, when justified, are bundled with their declared dependencies and actionable errors. No shell interpolation of untrusted metadata, credential material or source instructions is permitted. Portable instructions do not depend on Claude-only substitutions, dynamic command injection or fork semantics; host-specific examples are labelled and tested separately.

## 4. Skill dependency rules

| Installed selection | Required local capability | Optional collaboration / limit |
|---|---|---|
| deep-research only | All eight producer commands, minimal record/authority/effort rules and truthful self-checks. | A separate evaluator or qualified reviewer may be supplied externally. Absence cannot be hidden when that review is mandatory. No pack, Pactwright or provider agent is required by installation. |
| research-evaluate only | Audit and diagnosis, input semantics, criterion/risk distinctions and separate review output. | May inspect any compatible report package. It does not require producer command files, edit the package or re-run a paid investigation automatically. |
| research-extension-pack-creator only | Catalogue qualification, authoring rules, local structural validation and evaluation protocol interpretation. | Actual differential acceptance needs a capable authorised execution/review route, which may be a caller-provided runner. No circular sibling-package import or fabricated comparison is allowed. |
| Multiple selected skills | Same explicit record revision and compatible semantic contract. | Compose through authorised handoffs; do not assume an inter-skill RPC service, shared model memory or automatic installation of dependencies. |
| Core plus a selected pack | Core behaviour remains independently usable; pack input identifies version, scope and precedence. | The pack may narrow/specialise methods but cannot grant permissions, override locked work or replace core traceability. Stage 11 defines package details. |

No mandatory dependency edge connects the three skill packages. Optional collaboration has explicit inputs and acceptance obligations. Package compatibility changes are versioned when they alter meaning; prior issued research remains tied to its actual contract/source revisions. A command’s existence does not grant a host tool or action that the environment does not provide.

## 5. Initial SKILL.md outlines

[Skill Outlines](2026-09-10-stage-10-skill-outlines.md) supplies all three initial outline files, including frontmatter, activation boundaries, operation dispatch, bundled references, failure behaviour and handoff. They are contained as design artefacts in research logs. Their named future command/reference files are packaging requirements for Stage 17, not claimed existing installation paths today.

## Design challenges and verification

The design was challenged against six concrete input situations: a framing-only request; a third-party report with no producer installation; a core-only bounded answer; a report requiring unavailable independent human review; an interrupted write with an existing remote result; and a cosmetic or duplicate pack proposal. Expected outcomes follow the contracts: frame without browsing; evaluate read-only; preserve honest self-check labels; block the required review rather than simulate it; inspect the destination before retrying; and reject or reuse rather than invent a pack.

These are explicitly synthetic design walkthroughs, not live research runs. The deterministic verifier checks actual command inventories and complete fields, all 24 candidate dispositions, all five questions, three outline frontmatters, ownership/dependency guards and documentation links. It cannot establish future installed behaviour or semantic correctness by itself. The conformance review also examines whether the split actually preserves context, avoids self-grading and keeps each selected command useful independently.

The initial verification run on 10 September 2026 returned exit status 0 with twelve passing checks and eight detected negative controls. Subsequent semantic review made the supplied-candidate triage mode explicit in the discover contract: it can assess an existing set without a new acquisition call, and cannot claim a new search occurred. No required candidate, field or acceptance condition was removed. The final run after this repair is recorded in the [executed verification](2026-09-10-stage-10-verification.json).

Reproduction from the stage snapshot:

```sh
python3 docs/research-logs/2026-09-10-stage-10-verification.py --output docs/research-logs/2026-09-10-stage-10-verification.json
```

The [verifier](2026-09-10-stage-10-verification.py) operates on the three actual design documents. Its link inventory identifies accepted parent documents that were inspected through the connector; the local working directory is a partial mirror, not a claimed full Git checkout. Remote comparison verifies the stage-only delta and preservation separately. Negative controls remove a candidate, scope, question, contract field or review rule, rename a command, invalidate an outline name and break a reference. Every control must be applied and detected; none is retained.

## Conformance and exit

The original section 16 was re-read after drafting, and its requirements were compared with the actual documents rather than a shortened interpretation.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 Derive rather than assume packaging | Section 16 Purpose and lean hypothesis | Section 1 alternatives and responsibility map | Compared five packaging alternatives against accepted native responsibilities and real mutation/review boundaries. | PASS |
| R02 Three suggested roles and five questions | Section 16 hypothesis and design questions | Selected role map; Q1–Q5 | Checked planning, contextual continuity, review independence, durable state and isolated cross-domain use explicitly. | PASS |
| R03 Every proposed command disposition | Section 16 two candidate lists and evaluation-reason rule | P01–P14, V01–V10; command index | Matched all fourteen production and ten evaluation candidates; inspected reasons for retained/merged scopes. | PASS |
| R04 Complete coherent command contracts | Section 16 map/contracts outputs and Exit | Eleven contracts, eight fields each; W01–W08 map | Checked input sufficiency, operation, write ownership, outputs, review, repair, isolated value and example invocation for every command. | PASS |
| R05 Self-containment and dependencies | Section 16 outputs; family Project Contract sections 8–13 | Sections 3–4; package-local outline resources | Checked each package alone, explicit consumer inputs, no mandatory sibling dependency, optional executor boundaries and honest review limits. | PASS |
| R06 Initial SKILL.md outlines | Section 16 outline output | Three complete initial outlines | Checked names/descriptions/frontmatter and activation, dispatch, references, failure and handoff sections against current format documentation. | PASS |
| R07 Verification and prior-decision preservation | Section 16 Exit; execution instructions sections 5–9 | Executed verifier, semantic review and subsequent remote receipt | Checked design inventories and negative controls; compared Stage 5 records, Stage 8 execution and Stage 9 gaps; remote publication is verified separately before progression. | PASS |
| Production installation, live provider evaluation and pack implementation | Assigned to subsequent bootstrap stages; not required by section 16 | No implementation or measurement claimed | Initial outlines are the required design output, not a substitute for an execution requirement. | NOT APPLICABLE |

Content acceptance: PASS. Each selected skill has a distinct coherent responsibility, and every command has an explicit isolated-use and evaluation reason. Producer self-check, separate model audit and qualified human assurance remain distinct. All eight workflow groups and the accepted evidence, effort, authority and repair boundaries remain covered without a universal workflow runtime.

No Stage 10 design decision remains unresolved. The stage is complete only after these outputs and verification are committed to the authorised branch and the remote ref, parent and intended files are checked. The subsequent publication receipt records the actual commit rather than inventing a self-referential SHA here.

Stage 11 receives the three-role responsibility map, create-pack command, optional pack interface and dependency boundaries. It must research and narrow specialist families and define the full pack qualification, precedence, authoring, compatibility and differential-evaluation contract. Stage 10 has not preselected a specialist catalogue or claimed a completed pack comparison. Stage 12 owns the fifteen progressive examples; Stage 13 owns the complete evaluation architecture; Stage 17 and later stages own production packaging and actual installation.

