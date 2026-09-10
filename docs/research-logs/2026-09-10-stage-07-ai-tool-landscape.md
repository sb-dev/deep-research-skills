# Stage 7: AI Skills, Research Agents and Tools

Date: 10 September 2026. Branch: `feat/bootstrap`. Repository maturity remains a bootstrap workspace.

## Authority and accepted inputs

The acceptance contract is [original bootstrap section 13](2026-09-07-deep-research-skills-new-project-bootstrap-process.md#13-stage-7--research-ai-skills-research-agents-and-tools), re-read on `main`, together with sections 1, 2, 5 and the applicable section 29 research-quality gates. Its blob remains `8ff62c92bada2861ece3684a9e73a83da75d9d94`. The family main revision remains `d109b1f5f085f9493711803c0c801b9812427d57`.

The remote branch was verified at `18b0c365d0e845bdcdf22308606c2cfe1fa76bca`, the Stage 6 publication receipt. Its tree `5c327e300ebda2a2276ff70d6758d9970403ad37` contains 33 files and no Stage 7 outputs. The [progress record](bootstrap-progress.md) confirms Stages 1–6 complete. Contradictory local recovery receipts were not used to reset this accepted state. Earlier same-execution Stage 7 source inspections were retained as evidence, not treated as completed deliverables.

Relevant accepted inputs were re-read from this revision:

| Input | Constraint retained in this stage |
|---|---|
| [Stage 1 boundary](2026-09-10-stage-01-project-goal-and-boundary.md) | Research integrity remains here; consumer decisions, private project knowledge and specialist authority do not transfer to tools. |
| [Stage 2 professional practice](2026-09-10-stage-02-professional-practice.md) | Method-relative discovery, independent origins, honest access and qualified appraisal precede provider selection. |
| [Stage 3 information model](2026-09-10-stage-03-question-evidence-claim-model.md) | Source, evidence, claim, synthesis and recommendation remain distinguishable; locators and temporal context survive integration. |
| [Stage 4 source ecology](2026-09-10-stage-04-source-ecology.md) | Select paths by the question; native known-source retrieval precedes general rediscovery; rights and access depth remain explicit. |
| [Stage 5 workflow](2026-09-10-stage-05-workflow-and-artifacts.md) | W01–W08, exact-report review, targeted repair and readback after uncertain writes remain domain responsibilities. |
| [Stage 6 effort policy](2026-09-10-stage-06-effort-and-stopping.md) | Tiers do not weaken quality; resource reservations, hard limits and finalisation capacity constrain execution. |

### Stage-specific acceptance checklist

| ID | Required completion condition | Original authority |
|---|---|---|
| R01 | Verify original stage, global constraints and accepted earlier outputs. | Execution instructions section 3; bootstrap sections 2, 5, 13, 29. |
| R02 | Actually investigate every one of the 14 search categories. | Section 13 Search categories. |
| R03 | Investigate current provider and open-source approaches, including available integration surfaces. | Section 13 minimum investigation. |
| R04 | Complete all 15 evaluation fields for every retained candidate. | Section 13 Candidate evaluation record. |
| R05 | Compare and distinguish production semantics from execution engines. | Section 13 Important test. |
| R06 | Produce the AI/tool landscape and a justified shortlist. | Section 13 Outputs. |
| R07 | Produce the complete capability matrix. | Section 13 Outputs. |
| R08 | Record integration decisions and explicit gaps. | Section 13 Outputs. |
| R09 | Retain inspected source identity, access limits, dates, conflicts and evidence/judgement distinction. | Section 5; execution instructions sections 4 and 6. |
| R10 | Verify substantive completeness, references, preservation and stage-only changes; record conformance. | Section 13 Exit; execution instructions section 5. |
| R11 | Commit the completed stage and verify remote publication before progressing. | Execution instructions sections 7–8. |

The specification fixes 14 categories, 15 fields per candidate and five output responsibilities. It does not fix the number of candidates, require every candidate to be installed, or require measured comparative performance in Stage 7. The investigated pool contains 35 candidates and 525 field assessments; the supporting register contains 36 source bundles. These actual inventories are verified, not presented as externally mandated sample sizes. Tool selection architecture, formal gap classification, skills, packs, examples, evaluations and installation remain assigned to Stages 8–20; this stage does not claim their execution.

## Investigation method and evidence limits

The inquiry used three passes. First, the Stage 1–6 contracts and Stage 4 acquisition categories supplied evidence needs and candidate families. Second, original skill files, API references, package documentation and adjacent licences were inspected, with supplementary searches to fill gaps in note tools, fact-checking guidance, citation rendering and current hosted interfaces. Third, conflicts and integration assumptions were challenged before selecting a shortlist.

Material discovery routes included official provider/API navigation, repository README-to-SKILL/configuration/licence inspection, and queries such as `Agent Skills fact checking source verification SKILL.md GitHub` and `site:github.com/K-Dense-AI/scientific-agent-skills scientific critical thinking SKILL.md`. Search directories and third-party summaries were leads, not operating authority. Reading a skill did not activate its instructions or authorize installation, network transmission, mandatory illustration or credential sharing.

The [primary source register](2026-09-10-stage-07-sources.md) gives the original locations and inspected scope. Most findings come from opened original documentation or connector-returned files. Limited official search passages are labelled, especially Brave service terms, selected Tavily acquisition fields and an E2B SDK reference. A failed full-page open was not reconstructed from memory. A temporary web failure was retried successfully for Zotero, Pandoc and Trafilatura; no claim of general service unavailability follows from that failure.

The evidence establishes documented capability and constraints, not actual retrieval precision, operational reliability, model quality, account entitlement or legal clearance. No paid provider run, tool installation, browser login, private library access, benchmark execution or third-party data transfer occurred for this landscape. Local document checks and GitHub publication verification are separately observable work. Maintainer benchmark scores and popularity counts are not used to rank the shortlist.

### Material findings and conflicts

| Finding | Evidence and resulting decision |
|---|---|
| A source preference is not an enforced boundary. | Tavily Research's inclusion list is soft, unlike its documented response exclusion list. A strict source-limited task cannot be routed there solely on a matching parameter name. S05; C04/C11. |
| A parameter may be accepted but ignored. | Exa's current reference marks crawl-date fields deprecated/ignored and differs from older helper guidance on domain/path constraints. Validate the actual endpoint contract rather than copying a stale wrapper. S13; C12. |
| A provider alias is not a reproducible configuration. | Perplexity renamed presets and distinguishes dynamic presets from frozen configurations. Retain resolved configuration and interface identity. S08; C07. |
| A published API can have unsuitable lifecycle or output constraints. | Gemini's preview Interactions/background/storage requirements and missing structured-output/custom-function support constrain integration. Do not infer compatibility from its general research capability. S07; C06. |
| A source-visible skill can be non-reusable. | The Anthropic PDF skill has explicit proprietary restrictions. Reject copying it rather than inferring permission from public visibility. S03; C03. |
| A research-branded skill may instead be a developer helper. | GPT Researcher's supplied .claude skill mainly documents development/integration; distinguish it from the underlying engine. S10; C09. |
| Some existing skills do supply production semantics. | Scientific-writing includes evidence binding, confidentiality and approval separation. It is not merely an engine, but its manuscript-specific human-verification contract cannot be claimed satisfied by this AI bootstrap. S36; C35. |
| Similar skills within one repository can have different mandates. | Literature-review requires generated figures; scientific-critical-thinking makes them optional. Do not generalise a repository-wide workflow from one SKILL.md. S01/S35; C01/C34. |
| Bibliographic correctness is not semantic support. | Crossref, citation-management, Pandoc and Zotero handle different identity/formatting tasks; none alone validates the proposition attributed to a source. S02/S16/S25/S26. |
| Maintenance and licence signals can contradict convenience labels. | Notion warns its local MCP package is no longer actively maintained. DeepResearch Bench's actual Apache-2.0 licence conflicts with its MIT badge. Prefer exact authoritative files/notices and preserve the discrepancy. S30/S33. |
| Benchmark results depend on evaluator and data rights. | Both inspected research benchmarks changed judges in 2026; Bench II also records per-task source licences. Old scores and a blanket dataset licence cannot silently carry forward. S33/S34. |

These findings narrow reuse decisions without reopening accepted domain principles. No current source conflict remains silently resolved through model memory.

## 1. AI/tool landscape

The categories are responsibilities, not 14 required installed packages. One candidate can cover several categories; several wrappers around one service are not additional independent evidence. Provider engines, narrow tools, procedural skills and consumer applications are compared separately.

| Category | Required search category | Investigated candidates and coverage result |
|---|---|---|
| G01 | Agent Skills for research / browsing / literature review / fact checking | C01, C02, C03, C04, C09, C13, C14, C34, C35. Actual SKILL.md inspection distinguishes conduct guidance, browser access, bibliographic validation, scientific claim appraisal and development help. No inspected skill is declared a universal fact-checking oracle. |
| G02 | Provider deep-research agents | C04, C05, C06, C07, C08, C09. Hosted APIs and self-hosted generative engines are assessed with their source/output/budget boundaries. |
| G03 | Search APIs | C10, C11, C12, C23. Index discovery, source filters, extracted content and generated summaries differ. |
| G04 | Browser automation | C13, C14. Direct CLI/MCP control is distinguished from an additional autonomous browser agent. |
| G05 | Academic search APIs | C15, C16, C17, C18. DOI deposits, broad scholarly entities, recommendations and biomedical records are complementary rather than equivalent. |
| G06 | GitHub research tools | C19. Native API/connector, CLI and official MCP are access alternatives; actual connected reads do not prove all clients work. |
| G07 | PDF / document extraction | C03, C20, C21. Non-reusable skill materials are separated from independently licensed general and scholarly parsers. |
| G08 | Web extraction / crawling | C11, C12, C22, C23. Lightweight HTML extraction is compared with hosted/interactive acquisition. |
| G09 | Citation tooling | C02, C15, C21, C24, C25, C35. Identity, citation contexts, formatting and evidence-bound drafting remain distinct. |
| G10 | Reference managers | C25. Existing library ownership and local/Web access boundaries are preserved. |
| G11 | Data analysis / code sandboxes | C26, C27. Local analysis and remote isolation solve different problems; neither validates the analytical method. |
| G12 | Knowledge / note tools | C28, C29. Consumer-owned note access does not imply a mandatory knowledge database. |
| G13 | MCPs and connectors | C13, C19, C20, C29. Concrete host, toolset, OAuth, format and maintenance constraints replace generic “MCP compatible” assumptions. |
| G14 | Benchmark / eval frameworks | C30, C31, C32, C33. Generic harnesses and domain benchmark designs are complementary; stock scores are not the full quality contract. |

## 2. Shortlist and selection rationale

The shortlist is a set of role-specific reuse candidates, not a requirement to install every entry. Core research must remain useful through an already-capable host. A new dependency is justified only by a diagnosed gap and the later installation/evaluation gates.

| Role | Shortlisted candidates | Why retained; alternative not selected as baseline |
|---|---|---|
| Known repository evidence | C19 | Existing native GitHub access already exposes exact revisions. Do not rebuild a crawler or require a second MCP installation. |
| General discovery | C10, C12 | Brave supplies an index-oriented route; Exa offers explicit constrained discovery/content options. Keep existing authorised host search when adequate; no paid service is selected automatically. |
| Scholarly lookup/discovery | C15, C16, C18 | Distinct identifier, broad-corpus and biomedical responsibilities. C17 remains a useful gap-specific alternative, not another mandatory database. |
| Ordinary HTML extraction | C22 | Small local component with explicit input/output. C23 is retained as an alternative for demonstrated acquisition gaps, not default infrastructure. |
| Dynamic browser fallback | C13 | Direct bounded actions fit existing agents. C14 adds autonomous planning and remains conditional on a navigation need. |
| Advanced documents | C20 | General local structured conversion with optional pipelines. C21 remains specialist for scientific references/coordinates; C03 is rejected for vendoring. |
| Optional broad research engine | C05, C08 | One hosted API candidate and one self-hosted configurable alternative. Choose according to authorised environment, not a fabricated quality ranking. C06/C07/C09 remain documented alternatives. |
| Bibliographic checks/rendering | C02, C24 | Separate record validation from final presentation. C01/C34/C35 provide useful comparisons but do not replace this project's full method. |
| Local calculations | C26 | Reuse a pinned analytical tool only when simpler available computation is inadequate. C27 is not needed merely to execute a small calculation. |
| Behavioural evaluation harness | C30 | Extensible task/scorer model fits later trace-oriented evaluation. C31 remains an alternative rather than an additional mandatory harness. |

Consumer tools C25/C28/C29 are intentionally not baseline dependencies. C32/C33 remain benchmark references. A rejection or non-selection does not assert a product is generally poor; it identifies the mismatch with this repository's boundaries and evidence needs.

## 3. Capability matrix

The [complete capability matrix](2026-09-10-stage-07-capability-matrix.md) contains C01–C35, each with the exact 15 field labels required by section 13. All 525 assessments are substantive, including source control, citation behaviour, execution character, coupling, maturity, maintenance, operating implications and a justified USE/ADAPT/REFERENCE/REJECT decision.

The matrix is the authoritative candidate record. This landscape references it rather than maintaining a competing configuration catalogue. A licence notice, dated API page, provider capability claim and project recommendation remain different kinds of evidence. Unknown account-specific cost, actual latency or integration maturity is explicitly unmeasured, not replaced by zero or a passing label.

## 4. Integration decisions

| ID | Decision | Required boundary at later implementation |
|---|---|---|
| I01 | Reuse the host's adequate native tools first. | Keep the approved brief, source strategy and effort envelope outside provider prompts. Inspect the actual tool contract and result extent. |
| I02 | Treat C05/C08 and other broad engines as optional execution engines. | Submit a framed bounded request; preserve run/configuration and source results; audit all material output before acceptance. No engine owns downstream approval. |
| I03 | Do not erase useful procedural semantics in existing skills. | Compare C01/C34/C35 with the accepted method. Adapt only justified concepts, respecting licence, specialist scope and human authority; do not wholesale copy a domain-incompatible pipeline. |
| I04 | Keep source control explicit and endpoint-specific. | Distinguish preferred sources, returned-result filters, tool-access restrictions and disclosure permissions. A soft filter or ignored parameter cannot satisfy a hard requirement. |
| I05 | Adapt outputs, not the entire application stack. | Translate source identities, representation/access scope, locators, transformations, uncertainty and dates into the accepted Stage 3/5 records. No universal provider schema is required. |
| I06 | Separate citation services by responsibility. | C15/C02 identify and validate records; C21 can recover citation contexts; C24/C25 render references. Semantic entailment and contradiction review remain separate tasks. |
| I07 | Make privacy a routing precondition. | Local parsing/analysis is an option, not an automatic guarantee. Confirm actual pipeline/network behaviour; do not send private material to a remote parser, model, connector or judge without authority. |
| I08 | Preserve bounded execution and uncertain-result recovery. | Record configured bounds and outstanding jobs; inspect the provider/destination before retrying a lost response. Defaults and parallelism do not replace the aggregate budget. |
| I09 | Reuse evaluation harnesses without outsourcing acceptance. | Use domain fixtures and separately scored retrieval, evidence, citations, synthesis, repair and permissions. Calibrate model judges; do not inherit an upstream leaderboard threshold. |
| I10 | Keep app integration optional and read-scoped. | Existing Zotero/Obsidian/Notion content remains consumer-owned; restrict research to intended sources and record access limitations. Avoid unmaintained default components. |
| I11 | Install selectively and pin meaningful versions. | Inspect SKILL.md, licences, scripts and transitive/sibling dependencies. Run clean installation and task tests at their assigned stages before claiming working capability. |

The important engine test is therefore answered in both directions: broad iterative providers usually execute research operations, whereas some procedural skills already define useful production rules. Neither fact transfers the full Stage 1–6 contract or removes the need to evaluate what an integration actually preserves.

## 5. Explicit gaps

These are evidenced gaps or unverified obligations against the accepted workflow, not a final Stage 9 implementation plan.

| ID | Gap | Consequence and owner of the missing responsibility |
|---|---|---|
| X01 | Independent-origin assessment is not supplied by URL counts or citation graphs. | Domain research must link reports/observations and challenge false corroboration. |
| X02 | Identity/format checks do not establish claim entailment. | Domain evaluation must inspect the actual proposition, source passage and qualifiers. |
| X03 | Strict source constraints vary across interfaces. | Execution selection must reject unsuitable routes or enforce real boundaries before acquisition; prompts alone are insufficient. |
| X04 | Original evidence can be lost through summaries/compression. | Preserve actual access scope and meaningful transformations; repair missing support rather than trust polished prose. |
| X05 | Currentness cannot be inferred from request date or accepted filter parameters. | Recheck the relevant version/effective period and expose ignored/deprecated controls. |
| X06 | Generic report engines do not prove complete contradiction/gap coverage. | The research skill owns contrary evidence, alternatives and method-relative coverage. |
| X07 | Per-worker limits do not establish aggregate spend or safe retries. | Preserve Stage 6 reservations, finalisation capacity and outstanding job reconciliation. |
| X08 | Optional tool state can exceed authorised disclosure/retention. | Source/processor/audience checks precede remote execution; app permissions do not grant blanket task authority. |
| X09 | Deployment readiness is not established by these documents. | Clean installation, representative real tasks, failure paths and integration tests must be executed in their assigned stages. This is not marked working. |
| X10 | Existing benchmarks omit some production behaviours and change judges/data terms. | Add project-specific repair, access, source-control and traceability fixtures; retain evaluator/data versions and lawful use scope. |
| X11 | Dependency and licence boundaries can be misleading. | Inspect exact files and selected packages, not repository badges or similarly named skills. |
| X12 | Consumer knowledge tools do not own research truth or lifecycle. | Keep authoritative evidence/support records portable and avoid a mandatory new graph, note service or database. |

## Rejected alternatives and bounded stopping

Reject selecting a single “best” provider from marketing, stars or old leaderboard scores. Reject mandatory installation of every category. Reject rebuilding an index, crawler, browser agent, PDF engine, citation processor, sandbox or evaluator before the inspected alternatives are considered. Reject the opposite shortcut of declaring all domain semantics already solved by a provider's cited report.

Investigation stopped after all 14 categories had concrete inspected candidates, all 35 retained candidates had all 15 fields, the consequential interface/licence conflicts were bounded, and the five required outputs could be completed. The late scientific-critique/writing search filled a real appraisal/production-semantics gap and expanded the pool rather than substituting metadata checks for fact checking. Further general catalogue expansion is not needed to answer Stage 7's orchestration-versus-rebuild question. This is a purposive landscape, not an exhaustive census of every available research tool.

## Verification and conformance

The original section 13 was re-read for the final review. The semantic review checked actual candidate roles and inspected evidence, not only filenames: soft versus enforced source restrictions; current versus obsolete configuration; parser output versus observation; metadata versus entailment; proprietary versus open materials; provider engine versus procedural semantics; and documentary capability versus measured performance. The review corrected an overbroad draft licence statement about Tavily CLI materials: only the inspected skill-material licence is established.

The [validator](2026-09-10-stage-07-verification.py) checks the actual document set and candidate/field/category/source inventories, references, shortlist closure, decision labels, required output sections, known constraint guards and stage-only paths. Its [executed result](2026-09-10-stage-07-verification.json) records the real run and deliberately corrupted controls. Structural success is not a claim that external integrations were executed or that an automated test proved semantic truth.

Executed on 10 September 2026: `python3 docs/research-logs/2026-09-10-stage-07-verification.py --baseline-manifest <inspected-parent-inventory.json> --parent-progress <verified-parent-progress.md> --negative-controls`. The run returned exit status 0: all 16 checks and all 10 negative controls passed. The controls changed category/field/identity/source/decision/shortlist data, strengthened a soft filter falsely, broke a link, damaged an accepted progress section and added a premature production file. Each intended defect was detected; no mutation was retained. A full Git checkout can run the same verifier with `--negative-controls` alone against this stage snapshot.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 | Sections 2/5/13/29; execution section 3 | Authority and accepted inputs | Read original stage/globals, prior outputs, current ref/progress and 33-file tree. | PASS |
| R02 | Section 13 categories | G01–G14 and C01–C35 | Match all 14 categories and actual primary-source investigation. | PASS |
| R03 | Section 13 minimum | Provider/open-source records and sources | Inspect API/CLI/MCP/skill/app surfaces and relevant constraints. | PASS |
| R04 | Section 13 candidate record | Complete matrix | Inspect all 525 fields, including decisions and substantive gaps. | PASS |
| R05 | Section 13 important test | I02/I03 and C35 comparison | Distinguish engines from existing production semantics without transferring authority. | PASS |
| R06 | Section 13 outputs | Sections 1–2 | Review complete landscape and role-specific selection/rejection rationale. | PASS |
| R07 | Section 13 outputs | Section 3 and companion matrix | Verify every retained candidate and all required field labels. | PASS |
| R08 | Section 13 outputs | I01–I11 and X01–X12 | Review integration decisions and concrete missing obligations. | PASS |
| R09 | Section 5; execution section 6 | Source register and conflicts | Check originals, selected scope, dates, limitations and evidence/analysis distinctions. | PASS |
| R10 | Section 13 exit; execution section 5 | Validator/results and semantic review | Execute actual checks/negative controls; inspect stage-only delta and unchanged baseline. | PASS |

R11 is the separate publication gate: only the completed content and executed verification are committed; the subsequent receipt records the observed commit, parent, branch and file integrity. Stage 8 cannot begin on an assumed write result. No Stage 7 deliverable asserts its own future commit SHA.

### Exit assessment

The research establishes what should be orchestrated instead of rebuilt and which production obligations remain with this repository. All five Stage 7 content outputs are complete. No unresolved Stage 7 content decision requires user input. The final publication gate is verified from GitHub before progression.

Stage 8 consumes the shortlist, interface constraints, evidence handoff requirements and explicit gaps to choose an execution architecture. It must not interpret USE/ADAPT as already installed, convert a source preference into enforced access, or transfer the research lifecycle to a provider. No implementation, installation, benchmark score, release or maturity promotion is claimed here.
