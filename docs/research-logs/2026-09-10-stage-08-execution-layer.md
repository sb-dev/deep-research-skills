# Stage 8: Execution Layer

Date: 10 September 2026. Branch: `feat/bootstrap`. Status: architecture design; no installed integration or maturity claim.

## Authority, inputs and acceptance checklist

The contract is [original bootstrap section 14](2026-09-07-deep-research-skills-new-project-bootstrap-process.md#14-stage-8--choose-the-execution-layer), re-read on `main`, constrained by sections 1, 2, 5 and 29. The original blob is `8ff62c92bada2861ece3684a9e73a83da75d9d94`. The accepted parent is `bc5e53344104400373b84fc2183977817023f16a`, the [Stage 7 publication receipt](2026-09-10-stage-07-publication-receipt.md). Stage 7 content commit `3d687208088d102179b1e3ed35be8b95e1f1c8fd`, its parent, intended files and preserved prior files were read back before this stage began.

Inputs inspected for this decision are the [Stage 1 ownership boundary](2026-09-10-stage-01-project-goal-and-boundary.md), [Stage 2 method decisions](2026-09-10-stage-02-professional-practice.md), [Stage 3 information/provenance model](2026-09-10-stage-03-question-evidence-claim-model.md), [Stage 4 retrieval-path distinctions](2026-09-10-stage-04-retrieval-matrix.md), [Stage 5 gates and handoffs](2026-09-10-stage-05-workflow-and-artifacts.md), [Stage 6 budget and refresh rules](2026-09-10-stage-06-effort-and-stopping.md), and the [Stage 7 shortlist, integration decisions and gaps](2026-09-10-stage-07-ai-tool-landscape.md). The [Stage 7 matrix](2026-09-10-stage-07-capability-matrix.md) and [source register](2026-09-10-stage-07-sources.md) retain the exact candidate evidence. References C01–C35 below resolve there, not to a new provider catalogue.

| ID | Completion requirement | Specification reference |
|---|---|---|
| R01 | Inspect original stage, globals and accepted prerequisites; preserve branch provenance. | Execution instructions section 3; bootstrap sections 2, 5, 14, 29. |
| R02 | Assign all 12 listed production responsibilities to the repository with explicit execution boundaries. | Section 14 The repository should own. |
| R03 | Assign all 10 listed execution operations to suitable existing tools, including archiving. | Section 14 Existing tools should execute. |
| R04 | Choose an execution architecture with explicit relationships, inputs, outputs and control ownership. | Section 14 execution architecture output. |
| R05 | Define an operational tool-selection policy rather than a vendor-only preference. | Section 14 tool-selection policy output. |
| R06 | Define provider boundaries that preserve provenance, quality, authority and bounded effort. | Section 14 provider-boundary rules output; section 5. |
| R07 | Define failure-specific fallback behaviour without weakening required support or permission. | Section 14 fallback output; accepted Stages 4–6. |
| R08 | Specify useful local/offline execution and its limits. | Section 14 offline/local output. |
| R09 | Verify all five outputs and the provider-independent, non-framework exit condition. | Section 14 Exit; execution instructions section 5. |
| R10 | Persist conformance, commit only the stage and verify remote publication before progression. | Execution instructions sections 6–8. |

There are five required output responsibilities, 12 research-ownership concerns and 10 execution-operation concerns. The source prescribes no number of adapters, providers, tiers or runtime tests for this design stage. The policy cases below are executed design checks, not substitutes for the actual installation and behavioural evaluations assigned to later stages. Stage 9 owns detailed covered/partial/missing gap classification; Stage 10 owns the skill/command inventory; Stage 13 owns benchmark architecture. None of those later outputs is claimed here.

## Decision basis and alternatives

This is architectural synthesis from completed professional, information, acquisition and tool research, not another claim to have executed the 35 candidate products. Stage 7 supplies the dated documentary facts; this stage compares the consequences of those facts against the required ownership and workflow. No new account, network disclosure, paid engine run, benchmark score or software installation is needed to choose the boundary. No empirical speed or quality advantage is asserted.

| Alternative | Benefit | Consequence against the accepted contract | Decision |
|---|---|---|---|
| One mandatory hosted deep-research provider | Small integration surface for broad reports. | Makes private/offline and exact-source work dependent on that provider; report production does not establish domain acceptance. | Reject as core architecture. |
| One mandatory self-hosted research engine | More deployment control and configurable providers. | Requires an application runtime for simple research and risks moving W01–W08 semantics into its graph. | Reject as a prerequisite; retain optional engine execution. |
| Custom provider framework, router and persistent evidence platform | Uniform operational abstraction. | Requires infrastructure, storage and maintenance not justified by current independent implementation evidence. | Reject. |
| Host-native operations plus selectively enabled tools and optional engines | Uses the smallest adequate existing capability; separates execution from acceptance. | Needs explicit per-operation constraints and evidence-return checks; these are defined below. | Adopt. |

The architecture does not promise equal capabilities on every host. Provider independence means that question, evidence, review, repair and handoff semantics survive a change of executor. A host lacking a required capability must report that limitation or use an authorised alternative; it cannot claim portability by weakening the research standard.

## 1. Execution architecture

### Components and flow

```text
requester / consuming project
    supplies purpose, authority, private knowledge and intended use
        ↓
Deep Research Agent Skills in the selected host
    own W01–W08, evidence/support records, review and repair
        ↓ bounded, task-specific operation request
existing executor
    host-native tool | selected local tool | authorised connector/API
    | optional hosted or self-hosted broad research engine
        ↓ actual result, source identity, access extent, limits and status
research evidence intake
    checks returned material, preserves transformations, records gaps
        ↓
claim / contradiction / synthesis / exact-report review
        ↓
authorised consumer handoff and verified delivery
```

These are responsibilities, not required services or directories. Evidence intake can be a short procedure in a skill; it does not need a gateway. A provider adapter is only the instructions or small translation needed to invoke one interface and preserve its output. Do not add an adapter when the host's existing tool already returns usable source records. The consuming project's records remain the durable state; a provider job identifier is recorded there when necessary.

### Execution modes

**Native mode is the baseline.** Use the selected host's already-authorised search, file, repository and computation capabilities when they meet the current need. A bounded answer must not require an extra paid research engine, database or app. Host policies and tool schemas remain authoritative for permitted invocation, not example commands copied from another host.

**Local augmentation is selective.** Use C22 for ordinary HTML extraction when native reading is inadequate; C20 for a justified document-layout problem; C13 for a necessary browser interaction; C26 for an actual structured-data calculation. Existing simpler computation or parsing can remain adequate. These are chosen reuse directions, not a declaration that every package must be installed together. Inspect exact package/model licences and dependencies before installation.

**Hosted broad research is optional.** C05 is the selected integration candidate when an authorised Responses-based research environment is already appropriate. Pass the framed brief, permitted tools/data and enforceable bounds. The returned report is a draft with provenance to inspect. A need for a strict source boundary, a private processing constraint, unsupported output detail or unbounded exposure can make this mode ineligible. The shortlist does not authorise a purchase or guarantee account support.

**Self-hosted broad research is an alternative, not a second core runtime.** C08 is the selected candidate for projects that actually need and can operate that engine. Its orchestration remains behind the execution boundary. The repository does not inherit its supervisor graph, default concurrency, compression policy or deployment stack as research truth. C06/C07/C09 remain researched alternatives, not simultaneously required engines. Choosing among them later requires the same eligibility checks and an explicit reason; no numerical ranking was established in Stage 7.

C25/C28/C29 may expose a consuming project's existing library or notes. They never become required evidence stores. C30 may run later behavioural evaluations; the research criteria remain owned here. An optional Pactwright integration can bind these capabilities and delivery status, but cannot own their research semantics.

### All 12 research responsibilities

| ID | Repository-owned responsibility | Permitted executor assistance | Acceptance retained by the research skill |
|---|---|---|---|
| O01 | question framing | Suggest questions or retrieve already-authorised context. | Preserve the real objective and ask the owner about consequential ambiguity; an engine cannot silently rewrite it. |
| O02 | research planning semantics | Propose searches or task decomposition. | Select the method, coverage claim, review obligations and finite work envelope before accepting the plan. |
| O03 | source strategy | Offer search, database and connector routes. | Match evidence units, source classes, independence, access and freshness to each question. |
| O04 | quality / provenance rules | Return IDs, text, metadata and operation records. | Determine what was inspected, its locator, applicability, limitations and permitted retention. |
| O05 | evidence extraction semantics | Parse, transcribe, calculate or draft extractions. | Preserve attribution, qualifiers, units and transformations; derived text is not automatically source-reported evidence. |
| O06 | triangulation | Suggest related records or matching entities. | Establish relevant origin relationships; several wrappers or reports cannot manufacture independent support. |
| O07 | contradiction handling | Identify conflicting passages or alternative explanations. | Investigate scope/time/method differences and preserve unresolved counterevidence in the synthesis. |
| O08 | uncertainty | Supply confidence signals, missing-field warnings or model explanations. | Explain evidence strength and gaps; never substitute an opaque model score for claim-specific reasoning. |
| O09 | claim support | Locate passages and run structural reference checks. | Audit the actual proposition, inference, contrary material and citation placement, not just URL existence. |
| O10 | synthesis requirements | Generate a draft or organise supported claims. | Answer the agreed questions without adding unsupported bridges or erasing limitations. |
| O11 | research repair | Re-fetch or recompute a diagnosed unit. | Select the smallest sufficient repair, preserve valid work and recheck affected dependencies. |
| O12 | research-quality evaluation | Execute cases, assertions and model-judge calls. | Define criteria, distinguish measured from unmeasured results and retain required competent review. |

Accountable humans retain specialist review, consequential source/expense decisions and consumer commitments under Stage 1. “Repository-owned” describes the reusable method and acceptance rules; it does not falsely certify an AI as a qualified human reviewer.

### All 10 tool-execution operations

| ID | Operation | Selected route and input | Required returned evidence / boundary |
|---|---|---|---|
| E01 | web search | Adequate host search; C10/C12 when separately enabled; scoped query/filter and permitted source strategy. | Query/access context, original URLs, actual result extent and filter limitations. Hits are leads until inspected. |
| E02 | browsing | Native permitted browser or C13 for necessary rendered state/interaction. | Actual URL/state, relevant snapshot or region, actions and access limits; no credentials in logs. |
| E03 | specialist database search | Appropriate C15/C16/C18 or already-authorised specialist source from Stage 4. | Database, query/translation, IDs, continuation and access depth; metadata is not unseen full text. |
| E04 | GitHub retrieval | C19 exact repository/path/ref or documented collection query. | Resolved immutable revision or item ID, path/locator, pagination and permission limitations. |
| E05 | PDF retrieval / parsing | Native document retrieval and selective reading; C20 for a diagnosed advanced extraction need. | Actual edition/file, inspected pages, locators, extraction fidelity and missing visual context. |
| E06 | OCR / multimodal inspection | Native visual inspection first; an appropriate authorised local/remote transformation only when needed. | Original region/frame/time interval, transformation inputs and checked output; neither OCR nor a caption authenticates an event. |
| E07 | code / statistical analysis | Adequate local calculation or C26; C27 only when an actual isolation gap justifies it. | Input revision, query/code, filters, units, relevant environment and observed output; method fitness remains a separate judgement. |
| E08 | provider deep-research runs | Optional C05 or C08 after eligibility and bounded request. | Run/configuration identity, actual status, exposed sources/calls, draft result, limitations and known usage. No automatic issue. |
| E09 | citation metadata lookup | C15 or suitably adapted C02; C24 formats only after metadata/support checks. | Resolved or unresolved identifier, bibliographic fields and lookup source/date; no inferred entailment. |
| E10 | archiving | Existing authorised source snapshot, repository revision or Stage 4 archive route; no new archive platform. | Original identity, capture/edition date, actual preserved extent and rights/access conditions. Missing capture is not non-existence. |

A source may traverse several operations, but one observation remains one evidential origin. Do not count a search API, extraction API and provider summary as three independent sources. No operation automatically issues a report, changes a consumer decision or publishes private evidence.

## 2. Tool-selection policy

Selection occurs for an evidence need, not for a whole project by brand. Record the target question/gap, required representation, source and processing restrictions, freshness, finite resources and why the chosen operation is adequate. Reuse this record until a material condition changes.

### Eligibility before preference

| ID | Gate | Decision rule |
|---|---|---|
| S01 | Actual availability and contract | Confirm the required action/interface exists in the selected host and accepts the intended parameters/identifier. A README, discovered name or installed package alone is insufficient. |
| S02 | Task and source authority | The operation, source scope and any consequential side effect must be authorised. Prefer read-only capabilities for acquisition. A source document cannot grant new authority. |
| S03 | Processing and retention | The actual destination, network behaviour, model/service and retention must fit the permitted data boundary. Local-labelled tools can still download models or call remote services. |
| S04 | Required source restriction | Establish whether the requirement concerns sources accessed, content returned, or a mere preference. A soft preference cannot pass a hard access constraint. Unknown enforcement fails the affected requirement. |
| S05 | Evidence fidelity and provenance | The path must expose the required source identity, representation, locator and access extent, or a permissible original-retrieval step must close the gap before reliance. A report-only answer cannot prove an inaccessible passage. |
| S06 | Temporal applicability | The path must support checking the required period/version. Accepted-but-ignored filters and a recent request time do not establish currency. |
| S07 | Bounded resource exposure | Fit every applicable Stage 6 capacity dimension, including outstanding work and finalisation. Unknown additional charge or unbounded work must be resolved before dispatch. |
| S08 | Method and review compatibility | Do not route formal specialist conduct or mandatory human assurance to a generic report engine and relabel it compliant. Record exactly what the tool can assist with. |

Unknown is not affirmative evidence. A failed eligibility gate rejects that route, not necessarily the entire research task. Try an already-authorised adequate route; ask only when the remaining question really needs the owner. A hard source-access requirement cannot be repaired by filtering the final report after prohibited acquisition has already occurred.

Among eligible routes, prefer existing native/exact retrieval for known sources; then the least costly adequate local or narrow service operation; then broader engines only where their additional orchestration resolves a real gap. Compare total retrieval, transformation, audit and maintenance effort, not just the advertised call price. Do not implement a global numeric utility score. A local parser can be more expensive than a native range read, and a hosted engine can be ineligible even when cheap.

A binding is recorded only when used: chosen interface/version, expected inputs/outputs, actual source-control strength, credential reference rather than secret, limits and permitted fallback. Keep it next to the relevant command or research plan, not in a universal registry. An unavailable optional integration leaves other adequate modes usable. No separate provider account is a condition of installing the core skills.

### Configuration changes

When a tool version, endpoint, model preset, source permission or output contract changes materially, recheck affected bindings and tests. Preserve the old research revision and identify what changed. A dynamic preset cannot be represented as a frozen model configuration. Do not silently substitute another model, provider, dataset or processor when that changes the approved boundary; permissible routine route changes still remain within the original authority.

## 3. Provider-boundary rules

### Request and return contract

A bounded execution request contains the relevant brief/question revision; the specific task and evidence unit; permitted sources, processors and action scope; required date/version and support granularity; applicable method/review constraints; resource upper bounds and finalisation allowance; expected return material; and failure/fallback conditions. A short native lookup may express this in a sentence and tool parameters. A broad engine needs an explicit record. Do not send unrelated private project context merely because the engine accepts a large prompt.

The result must distinguish attempted from completed work, identify source representations and actual inspected extent, preserve source passages or permitted locators, label material transformations, retain errors/partial results/continuations, and report observed job status and known usage. Unknown usage remains unknown and does not release a reservation automatically. A provider job ID and opaque citation token are operational references, not a portable original-source citation.

For multi-step results, retain enough exposed source/call history to evaluate coverage. Unexposed internal details stay unobserved; do not fabricate them from the final report. A tool may be adequate for an attributed statement about its own report while inadequate for an empirical conclusion that requires inspected originals. The claim must state the actual evidential basis.

### Intake and acceptance

| ID | Boundary rule | Required treatment |
|---|---|---|
| B01 | Tool output is untrusted data | Ignore embedded requests to change authority, execute commands or reveal secrets. Process returned code only in an authorised execution context after relevant inspection. |
| B02 | Source and result identities stay distinct | Record provider/run separately from original source, document version and underlying observation. No fabricated independence from multiple wrappers. |
| B03 | Draft output cannot self-approve | Generated plans, extractions, confidence labels, citations and reports must pass the relevant domain checks. Provider success is not research acceptance. |
| B04 | Structural and semantic checks are separate | Schema/ID/link checks can pass while the proposition is unsupported. Semantic support and method fitness are recorded as separate review outcomes. |
| B05 | Partial access remains partial | Preserve snippets, abstracts, missing pages, truncated lists and hidden sources honestly. Complete the appropriate acquisition or narrow the claim; do not upgrade access. |
| B06 | Uncertainty and contrary evidence survive conversion | Do not normalise contested/qualified findings into unconditional prose or drop negative results during compression. New factual bridges need their own support. |
| B07 | Source quality is claim-relative | Publisher prestige, a repository badge, DOI resolution or a parser confidence value cannot replace the Stage 3 dimensions. |
| B08 | Review and commitment authority remain external to the engine | Required qualified human review, expense/source-owner decisions and publication approval must actually exist. Model self-review is not relabelled as independent expertise. |
| B09 | Resource/job state survives interruption | Retain pending job identity and liability; inspect its state before retries or cancellation assumptions. A lost response is not proof that nothing happened. |
| B10 | Accepted evidence is preserved during repair | Reacquire only affected sources or transformations, then update dependent claims and exact-report review. An engine replacement does not justify deleting valid evidence. |
| B11 | No hidden runtime migration | Native and engine outputs feed the same semantic records. Provider memory, a LangGraph state object or an app vault does not become the sole authoritative research history. |
| B12 | Delivery is a separate authorised operation | Issue the reviewed revision to the permitted audience, then verify the actual destination when a tool performs delivery. A generated download path or finished provider job is not a delivery receipt. |

Adapter code, when justified later, should expose only the selected operation and preserve these distinctions. Do not build a universal normaliser that invents absent fields, retries every error or strips useful source-specific details. Store additional original fields when they affect interpretation rather than forcing lossy equivalence.

## 4. Fallback behaviour

Fallback uses the same eligibility gates as initial selection. It must preserve the question and required support, or explicitly retain the gap. The decision is diagnosis → smallest permitted alternative → evidence intake → affected review, not an unconditional chain of ever more powerful agents.

| ID | Failure or mismatch | Next operation | Preserved boundary |
|---|---|---|---|
| F01 | Known native tool temporarily unavailable | Check actual failure, then an authorised direct/native equivalent for the same source. | Do not turn a local DNS error into global source non-existence or restart unrelated work. |
| F02 | Source control is soft, ignored or unknown | Use exact permitted source retrieval or a path with demonstrated required enforcement. | Do not acquire disallowed sources and later hide them from citations. |
| F03 | Abstract/snippet/report lacks decisive original support | Retrieve the authorised original range or keep an explicit access/knowledge gap. | No unseen methods/results, no automatic paid access. |
| F04 | Text extraction loses table or media context | Inspect the original page/region; selectively use an appropriate parser or transformation. | Verify the derived content; no wholesale OCR or broad crawl without need. |
| F05 | Capped list or connector pagination | Follow actual returned/documented continuation within scope and budget. | Incomplete remains incomplete; do not invent a cursor or treat unresolved folders as empty. |
| F06 | Permission, processor or retention mismatch | Use an already-permitted local/native path or ask the owner for the needed decision. | No confidential public search, alternate credentials or implicit disclosure. |
| F07 | Quota/rate/budget boundary | Respect backoff and remaining reservations; reuse adequate permitted cache or stop collection. | No parallel accounts or workers to evade the cap; review obligations survive. |
| F08 | Job/write result lost | Inspect provider/destination by actual ID and reconcile before retrying. | Keep outstanding liability and accepted records; neither failure nor success is invented. |
| F09 | Generated report is unsupported or contradicts evidence | Return the defective claim/extraction/inference to its owning W04/W05/W07 check. | Retain valid unrelated material; do not rerun the whole engine by default. |
| F10 | Current evidence unavailable offline | Preserve historical findings and state their as-of limit; reacquire later only within authority. | Do not advance valid-as-of or call cached facts current merely because code reran. |
| F11 | Required specialist method/review unavailable | Block the affected prerequisite and ask for the necessary authorised input. | A second generic model or cheaper tool cannot waive the required standard. |
| F12 | Alternative cannot satisfy the original outcome | Report the precise unresolved need and available evidence. | A limitations-only substitute is acceptable only under the existing brief or an owner decision. |

A fallback may finish at an honest unresolved finding where the brief permits that outcome. It cannot waive a mandatory bootstrap prerequisite. Reuse a verified source from cache only if representation, temporal relevance, access rights and permitted retention still fit. A source relocation can require a locator repair without changing claim truth; a retraction can require much more than changing a link.

## 5. Offline and local opportunities

| ID | Opportunity | What can be completed locally | What remains unavailable or conditional |
|---|---|---|---|
| L01 | Supplied document / repository snapshot | Scoped search, exact passages, source/evidence records and comparisons at the captured revision. | Unseen files, later commits or current live behaviour cannot be inferred. |
| L02 | Saved HTML or permitted PDF | Extraction, page/region inspection and checking against the stored representation. | Live redirects, missing assets and uncaptured dynamic state are not reconstructed. |
| L03 | Existing dataset and computation | Reproducible calculations with input identity, filters, units and explicit assumptions. | A rerun does not refresh the observation period or establish causality. |
| L04 | Evidence and report audit | Reference closure, formatting, inconsistency detection and substantive review of accessible evidence. | Metadata syntax checks cannot resolve an inaccessible DOI or certify a source not held locally. |
| L05 | Local model or parser pipeline | Drafting or extraction within an authorised offline configuration. | Confirm weights, dependencies, licences, network/telemetry and resource limits first; local-labelled is not automatically offline. |
| L06 | Existing notes/reference library | Read authorised exports/vaults and produce a bounded handoff. | Application-specific CLI requirements and private online attachments remain separate; no mandatory app migration. |

Offline capability is scoped to the available evidence, not a universal fallback for current research. Record the snapshot/corpus boundary and the date/precision actually known. Source, evidence, claim and report can remain ordinary Markdown or structured files. No vector database, graph service or synchronisation daemon is required to read a fixed collection or preserve traceability.

When online access becomes available, first identify the claims requiring currency or missing originals and perform a bounded delta check. Do not recreate the whole corpus or discard completed local work. Retention requirements can legitimately prevent keeping raw originals; preserve only permitted metadata and communicate the resulting audit limit. Model weights and downloaded packages are external acquisitions requiring their own allowed installation path.

## Design challenges and verification

The [policy cases](2026-09-10-stage-08-policy-cases.json) are explicitly synthetic records for checking the selection, intake and recovery rules. They are not observed provider results, installed-skill demonstrations or measured performance. The [verifier](2026-09-10-stage-08-verification.py) evaluates these rules and checks document/requirement coverage, references and intended file changes. Its [result](2026-09-10-stage-08-verification.json) records actual execution.

The semantic review challenges the architecture with the following contrasting paths. A known repository fact uses E04 rather than an engine. A confidential fixed-file comparison uses local permitted reading without public search. A strict source-access task rejects a soft preference before dispatch. A broad provider draft with opaque citations returns to original acquisition and support review. A lost expensive-job response triggers status inspection rather than duplicate launch. A corrected denominator reopens the affected calculation and claims while preserving unrelated evidence. These walkthroughs use the rules above; they do not claim the integrations were run.

The design preserves all accepted distinctions and does not add a central runtime. Production semantics stay invariant across executor choice; only actual capability, access, cost and fidelity vary. The original section 14 was re-read after drafting. All five required outputs, every O01–O12 responsibility and every E01–E10 operation were checked against that text. On 10 September 2026, `python3 docs/research-logs/2026-09-10-stage-08-verification.py --baseline-manifest <inspected-parent-inventory.json> --parent-progress <verified-parent-progress.md> --negative-controls` returned exit status 0: all 12 checks, 25 synthetic policy cases and 9 negative controls passed. The controls removed required coverage, introduced unknown references, falsely strengthened a soft constraint, broke a link, damaged earlier progress, changed expected policy outcomes and added an unjustified runtime file. Each intended defect was detected; no mutation was retained. The final run was repeated after recording these observed results. A checkout at this stage can run the verifier with `--negative-controls` alone.

## Conformance and exit

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 | Sections 2/5/14/29; execution section 3 | Authority and inputs | Read original/current stage and relevant accepted Stage 1–7 records; verify Stage 7 receipt. | PASS |
| R02 | Section 14 repository list | O01–O12 | Inspect every ownership assignment and retained acceptance boundary. | PASS |
| R03 | Section 14 tools list | E01–E10 | Inspect each route, input, output and source limitation, including archiving. | PASS |
| R04 | Section 14 architecture output | Section 1 and alternatives | Compare four architectures; trace request, execution, intake, review and delivery. | PASS |
| R05 | Section 14 selection output | Section 2 S01–S08 | Test eligibility before preference and preserve unknown/hard-constraint distinctions. | PASS |
| R06 | Section 14 boundary output | Section 3 B01–B12 | Check evidence return, provider draft status, authority, budgets and repair. | PASS |
| R07 | Section 14 fallback output | Section 4 F01–F12 | Review failure-specific re-entry and non-escalation of permissions. | PASS |
| R08 | Section 14 local output | Section 5 L01–L06 | Check useful local work, snapshot/currentness limits and actual offline conditions. | PASS |
| R09 | Section 14 Exit; execution section 5 | Design review and executed verification | Verify all outputs and cases; no universal provider framework or implementation claim. | PASS |

R10 is the publication gate, recorded separately after the stage-scoped commit and remote readback. Content design is complete and no unresolved Stage 8 decision requires user input. Stage 9 must classify remaining workflow coverage without treating these design choices as already implemented integrations. No release, merge, installation result or research-quality score is claimed.
