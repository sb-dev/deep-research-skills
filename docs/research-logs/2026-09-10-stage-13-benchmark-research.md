# Stage 13: External Benchmark Investigation

Date: 10 September 2026. Authority: bootstrap section 19, external benchmark references. This is primary-source research and a reuse decision, not a measurement of this project's agents.

## Method and source boundaries

All five named benchmark families were investigated. Discovery queried their exact names with research/evaluation terms, followed author pages, papers and repositories, then inspected the evaluation-method sections. Search hits for unrelated uses of FINDER and similarly named deep-research benchmarks were excluded. The paper identities below resolve those ambiguities. The accepted Stage 7 landscape supplied candidate leads, not substitute evidence for this investigation.

HTML originals were used. No unread PDF chart supplies a conclusion. No benchmark task/answer collection, dataset, evaluator package or model was downloaded or executed. Source descriptions and project decisions are separated. The comparison is purposive and covers the five required families; it is not an exhaustive evaluation survey.

## S01: BrowseComp

Original: OpenAI, [BrowseComp: a benchmark for browsing agents](https://openai.com/index/browsecomp/), 10 April 2025. Inspected the task-design, evaluation and limitations discussion on 10 September 2026.

**Source finding.** BrowseComp uses difficult-to-locate information with short, readily checkable answers. It highlights persistent browsing, query reformulation and verification. Its authors distinguish this setting from broad real-world research and discuss its limited representativeness. The release asks that plaintext benchmark examples not be distributed publicly.

**Decision: REFERENCE.** Adopt the hard-discovery/easy-check distinction for independently authored known-source cases. Keep retrieval traces separate from final-answer correctness. Do not reproduce its questions or answers, inherit an unlimited attempt budget, or treat answer accuracy as report quality. The repository does not need to run the whole external benchmark to test a missing original-source regression.

## S02: DeepResearch Bench

Original: Du et al., [DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents](https://arxiv.org/html/2506.11763), 2025; inspected RACE, FACT and their evaluation-method discussion. Author implementation: [Ayanami0730/deep_research_bench](https://github.com/Ayanami0730/deep_research_bench). Current README lines 1–48 were read; blob `2b96b70617f236e77555c8d1fa40c8942950b8c4`.

**Source finding.** RACE assesses report generation using task-adapted criteria and references. FACT separately extracts claim/URL relationships, removes repetitions and checks citation support. The inspected README documents a May 2026 evaluator migration, so historical and newer judge results are not automatically comparable. Its badge is not licence clearance for code or data.

**Decision: REFERENCE/ADAPT criteria, not scores.** Separate report assessment from citation support and record judge configuration. Inspect the actual proposition and supporting passage, not just citation counts. Do not inherit relative leaderboard scores as release thresholds or assume that a reference report is infallible. No upstream code/data is vendored here; any later reuse requires exact-file terms and data permissions.

## S03: BrowseComp-Plus

Original: [BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent](https://arxiv.org/html/2508.06600), inspected HTML v1, 8 August 2025; sections 3.2–3.3 and 4.3–4.4. Author project: [BrowseComp-Plus](https://texttron.github.io/BrowseComp-Plus/).

**Source finding.** A controlled corpus and verified evidence make retrieval conditions more inspectable. The method distinguishes useful evidence from answer-string occurrence and measures document retrieval and end-to-end behaviour separately. Corpus construction, distractors and the evidence returned to the agent matter to interpretation.

**Decision: ADAPT experimental separation.** Freeze our own permitted source representations and gold evidence for replay cases, while keeping a different live-source mode. Record corpus identity, result truncation and query/call bounds. Evidence recall is interpretable only within a defined gold set; do not invent global web recall. We do not redistribute the original corpus or its benchmark answers.

## S04: ResearchRubrics

Original: [ResearchRubrics: A Benchmark of Prompts and Rubrics for Evaluating Deep Research Agents](https://arxiv.org/html/2511.07685), inspected HTML v1, 10 November 2025; sections 3.1–3.4. Author repository discovered: [scaleapi/researchrubrics](https://github.com/scaleapi/researchrubrics); repository execution is not claimed.

**Source finding.** Expert task-specific rubrics express report requirements, including mandatory, optional and negative criteria, with graded satisfaction and aggregation. These requirements reach beyond factual lookup into structure and reasoning.

**Decision: ADAPT atomic, source-bearing criteria.** Preserve mandatory and disallowed behaviour explicitly, with inspectable reasons. Reject averaging a mandatory unsupported claim away through optional presentation points. Our acceptance statuses remain PASS, FAIL, BLOCKED and justified NOT APPLICABLE; explanatory partial support must not become a mandatory PASS. The paper's broader architectural interpretations are not adopted as established impossibility claims.

## S05: FINDER / DEFT

Original: Zhang et al., [How Far Are We from Genuinely Useful Deep Research Agents?](https://arxiv.org/html/2512.01948), inspected methods and failure-taxonomy sections. The displayed HTML version and body dating were inconsistent; no precise revision date beyond the identified work is used for a substantive claim. Author [FINDER_DEFT README](https://github.com/OPPO-PersonalAI/FINDER_DEFT/blob/main/README.md) was read in full, blob `6cd7b15cdbe733cb89f4f1fa16d92432200a56d4`.

**Source finding.** FINDER uses explicit report checklists. DEFT classifies reasoning, retrieval and generation failures. The repository accepts question/article records and exposes model-assisted taxonomy and checklist evaluation procedures.

**Decision: REFERENCE.** Use fine-grained requirements and diagnosable failure categories. Do not infer an agent's actual causal failure path from its final prose alone: inspect source and operation evidence before assigning root cause. Retain our accepted Stage 2 taxonomy rather than silently replacing it. A generated taxonomy or model verdict is not independent ground truth. No toolkit execution is claimed.

## Comparative decision

| Required family | Useful contribution | Missing production responsibility retained here |
|---|---|---|
| BrowseComp | Hard discovery and answer verification. | Complete research deliverables, authority, repair and useful stopping. |
| DeepResearch Bench | Distinct report and citation assessments. | Fixed-input review, source-access fidelity and non-compensable release gates. |
| BrowseComp-Plus | Controlled evidence/corpus comparisons. | Honest live-source updates, licensed snapshots and consumer-specific scope. |
| ResearchRubrics | Explicit fine-grained report requirements. | Preserved mandatory failures, grounded review and permission constraints. |
| FINDER / DEFT | Requirement compliance and failure diagnosis. | Trace-supported causes, smallest repair and continuity of accepted evidence. |

The adopted architecture combines these lessons with the existing research contracts. It does not combine their numbers into a universal score, copy their task sets, install several competing harnesses or require an external leaderboard submission. The previously selected optional Inspect integration remains a harness opportunity; the domain owns criteria and evidence.

## Additional primary sources for independent research cases

**S06.** Fielding, Nottingham and Reschke, [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), June 2022, section 15.4.5. The actual status-code section was inspected. It distinguishes a bodyless 304 response from reuse of a stored representation. Used only for the bounded HTTP research case, not proof of server implementation behaviour.

**S07.** Frictionless Data, [Table Schema, Data Package v1](https://specs.frictionlessdata.io/table-schema/), “Physical and Logical Representation”, “Constraints” and “Missing Values”; accessed 10 September 2026. The inspected v1 page specifies conversion of designated physical missing strings before type-specific conversion and logical constraint checking. This is a version-specific method source, not an assertion about every library or newer specification.

These two topics are disjoint from the fifteen teaching examples. Their original prompts and evaluation contracts are in the companion cases file. Source-backed expectations were established without executing a candidate research agent. Because these are public authored cases, they are hold-outs from development examples, not secret or contamination-proof evaluations.

## Exit

All five mandated benchmark families have an inspected primary basis, a concrete adoption decision and a transfer limit. Findings justify separate retrieval, evidence, citation and synthesis checks, fixed submissions, controlled replays, independent research cases and trace-based diagnosis. No unresolved access requirement prevents this design. Operational benchmark results and clean installed execution remain separate later-stage obligations.
