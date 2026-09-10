# Stage 11: Performed core-versus-pack comparisons

Date: 10 September 2026. These four outputs were produced in this continuation by applying the [recorded protocol](2026-09-10-stage-11-comparison-protocol.md) and [profile rules](2026-09-10-stage-11-profiles.json) to the real sources in the [source register](2026-09-10-stage-11-sources.md). They are generated research outputs, not invented source documents or simulated benchmark runs. The source-access phase was shared and cached; it was not performed four separate times. No installed skill, external agent process or independent human reviewer was used.

Known facts were available to both conditions, including the RULER version difference and the repository exception branch. The core outputs retain these cautions. The comparison tests added specialist handling, not whether a deliberately weakened baseline can be made wrong.

## SCH core

### Answer

An advertised window is not enough evidence of reliable use. RULER provides a reason to evaluate the operations a research assistant actually needs, rather than treating successful retrieval from a long input as complete long-context competence. This is a bounded design inference, not a conclusion that any current product fails.

### Source observations

SCH-C1: The arXiv record identifies v3 dated 6 August 2024. Its abstract reports seventeen models and thirteen tasks; the earlier v2 abstract reports ten models. These are revisions of the same named work, not independent confirmation. [S01, submission history/abstract; S02, abstract.]

SCH-C2: The work goes beyond simple retrieval. Its effective-context definition uses the Llama2-7B 4K result, 85.6%, as the comparison threshold. That is this benchmark's operational definition, not a universal acceptance standard. [S03, sections 3–4 and Table 3 caption.]

### Analysis

A research assistant may need to combine evidence, preserve qualifications and answer a particular question. Passing a limited retrieval test cannot logically establish all those capabilities. Conversely, a decline on the paper's selected tasks does not establish failure on every application. The justified next decision is to define the application's required behaviours and test those, not to substitute a published context number for such evidence.

### Limits and next check

This is a focused reading of one work, not an exhaustive review or a new model evaluation. No current ranking or deployment approval follows. Next check: specify representative application tasks, output-quality requirements and permitted input lengths before an authorised test. Consumer acceptance remains the team's decision. Self-check: version distinctions, source support and these limits were retained; no independent review is claimed.

## SCH pack

### Answer and preserved findings

Preserve SCH-C1 and SCH-C2: advertised capacity alone does not establish application reliability, and this is one named research work with multiple representations. No current model ranking or product approval is justified. The selected scholarly-evidence profile adds explicit publication-unit handling and an applicability decision, not a different factual verdict.

### Work and representation handling

SCH-P1: Register one research-work identity, W-RULER. Link S01 as its metadata record, S02 as report version v2 and S03 as report version v3. Thus this supplied corpus has two report versions but one research-work identity. Do not sum the ten-model and seventeen-model descriptions into twenty-seven independent models/studies. Select v3 for the latest version of this named paper found in the inspected history, while preserving v2's count as historical. Individual empirical runs within the work are not counted by this publication linkage. [S01–S03, identity/abstracts.]

### Design-specific appraisal

SCH-P2: The 85.6% threshold is tied to a reference model, task suite and length. Its use supports an internally defined comparison; it supplies no evidence that this value is an acceptable research-assistant error rate. Keep the proposed product acceptance criterion unset rather than copying that threshold into a release gate. [S03, effective-context definition; inference explicitly limited to that definition.]

SCH-P3: Separate benchmark task performance from the application's evidence-handling responsibilities. The follow-up specification must name the actual research tasks and define how support, contradiction, uncertainty and long-range integration will be judged. A test of a retrieval-only operation is not evidence for an untested synthesis operation. This is the design-specific transfer check, not a new benchmark result.

### Eligibility, status and limits

Include both representations because version change is relevant; do not discard v2 as useless or treat it as current. The inspected arXiv record showed no retraction notice, but a single record check is not exhaustive publication-status clearance. The metadata's COLM 2024 comment is an attributed record statement, not independent verification of review quality. [S01.]

The source-backed unit/applicability assessment is complete for the stated corpus. It is not a systematic review, installed-skill test or an independent experiment. Required next evidence remains an authorised application-specific test. The core findings and consumer authority remain unchanged; the pack has made the counting and acceptance-boundary decisions explicit and reusable.

## OSS core

### Answer

At the specified revision, Open Deep Research is a candidate to investigate as an optional engine, not a demonstrated ready-to-deploy dependency. Keep its execution behind the research skill's source, provenance, budget and review boundaries.

### Source observations

OSS-C1: The README describes configurable models/search and a LangGraph development setup. The package and server files declare environment details, while the licence file provides an MIT notice for the code. These are documentation and static-source observations, not a completed installation or permission assessment for every dependency or service. [S11–S13, S16.]

OSS-C2: The inspected supervisor code includes a caught-exception condition ending in `or True` and returns END. A non-token exception entering that branch can therefore end that research phase. This static observation justifies a targeted failure-path test; it does not prove a particular production failure or its frequency. [S15, supervisor_tools exception branch.]

OSS-C3: The configuration exposes bounded-looking iteration, tool-call and concurrency settings. Those declarations do not by themselves prove a complete aggregate resource cap or preserve every intermediate result. [S14; analysis of what the inspected declarations do not establish.]

### Analysis, limits and next check

The candidate can reduce the need to build broad retrieval orchestration, but its returned report still needs evidence and claim review. Before adoption, test the selected environment and the error path with authorised inputs; verify that incomplete research is not reported as complete. Source restrictions, API credentials, dependency terms and operational cost remain separate obligations. No engine execution, spend, security certification or deployment approval was performed. Self-check used the actual source locators; independent review is not claimed.

## OSS pack

### Answer and preserved findings

Retain OSS-C1–C3: this is a candidate optional engine with unexecuted deployment and error-handling checks. The open-source-ecosystem profile adds cross-file environment reconciliation and an evidence-to-verification ledger. It does not conceal the core's already-known code warning or turn popularity into suitability.

### Cross-file reconciliation

OSS-P1: Package metadata declares Python >=3.10; the supplied LangGraph server configuration selects Python 3.11, also used by the documented server launch. These are compatible statements at different scopes, not proof that the server path has been tested on every allowed package interpreter. For a server-path smoke test, start with the documented/configured 3.11 environment and record the resolved dependency versions. A separate library-only test may investigate other supported environments. [S11, S13, S16.]

### Evidence-to-verification ledger

| Record | Evidence kind and finding | Unmet adoption evidence / bounded next check |
|---|---|---|
| OSS-P2 | Inspected code licence: MIT notice. [S12.] | Resolve relevant dependency/model/service terms for the actual deployment; the parent licence does not cover them automatically. No legal clearance claimed. |
| OSS-P3 | Package dependency ranges and source configuration. [S13–S14.] | Create a resolved environment and execute the chosen entry point only when authorised. A declared dependency is not an installed or compatible one. |
| OSS-P4 | Static exception-to-END path already identified in OSS-C2. [S15.] | Inject a controlled non-token worker failure in a permitted test environment; inspect retained evidence, returned status and report gate. Reject an integration that treats the resulting partial output as sufficient research without review. This test was not executed here. |
| OSS-P5 | Distinct concurrency/iteration/call settings. [S14.] | Trace a bounded sample's actual operations and reconcile total consumption; do not multiply or interpret defaults as a proved global cap. |
| OSS-P6 | The inspected commit is a dependency update dated 10 August 2026. [S17.] | Maintenance responsiveness and meaningful task tests remain unassessed; one bot update cannot establish either. No broad issue/CI sample is claimed. |

### Handoff and limits

Provide the exact repository revision and source paths with this ledger to the consuming engineer. Preserve the four statuses: documented capability, statically inspected fact, executed result and unknown. There are no executed engine results in this assessment. A later source change should reopen only affected records and dependent tests, while the historical assessment retains this revision.

The added behaviour is concrete: reconcile two environment scopes and translate existing risks into specific missing evidence and acceptance conditions. The verdict remains conditional. No repository was modified, no credentials supplied, no expense incurred through a new service, and no deployment or security approval issued.

## Performed review

This is the assistant's substantive review of the four fixed outputs, with the shared-session limitation stated in the protocol. It is not independent human assurance. Output integrity and recognised fact guards are checked separately by the verifier.

| Criterion | SCH core / SCH pack | OSS core / OSS pack | Result and evidence |
|---|---|---|---|
| Same research question and bounded source universe | Both answer advertised-capacity applicability using S01–S03. | Both assess the same pinned engine using S11–S17. | PASS. Neither condition changes the intended downstream decision. |
| Known evidence preserved in baseline | Version counts and threshold caveat appear in SCH-C1/C2. | Exception warning and unexecuted status appear in OSS-C1–C3. | PASS. No artificially defective baseline. |
| Pack effect beyond a label or heading | SCH-P1 makes unit selection/counting explicit; SCH-P2 refuses threshold transfer to an application gate. | OSS-P1 reconciles environment scopes; P2–P6 assign specific verification obligations. | PASS for bounded procedural demonstration, not causal superiority. |
| Evidence and inference distinguished | Attributed counts/definitions; applicability conclusions labelled inference. | Source declarations, static code and proposed tests separated. | PASS. No new empirical result invented. |
| No regression in authority or uncertainty | No model run, current ranking, exhaustive review or approval. | No install, code edit, paid job or deployment approval. | PASS. |
| Publication/version and temporal fidelity | Earlier version retained as historical, not extra corroboration. | Exact commit fixed; one dated update not general health. | PASS. |
| Actual installed or isolated behaviour | Not performed. | Not performed. | NOT APPLICABLE to this design demonstration; mandatory later installation gates remain distinct. |
| Independent review / general performance advantage | Shared assistant and context only. | Shared assistant and context only. | NOT APPLICABLE as a present claim; no reliability or improvement estimate is made. |

The comparison supports retaining both profiles as designed, procedure-demonstrated catalogue candidates. It does not justify claiming they are installed-tested or universally better than core. The relevant specialist handling was explicitly exercised on real evidence; the same conclusion in both modes is not a failure when the intended change concerns method and assurance, but extra formatting alone would have failed the prespecified test.
