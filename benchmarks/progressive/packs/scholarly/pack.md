# RULER: bounded scholarly evidence package — PACK condition

Revision P1, 2026-09-13. Producer draft for the parent’s separate exact-wording review. Executed from the authorised source checkout using `skills/deep-research/SKILL.md`, its common contract and frame/plan/discover/extract-evidence/analyse-evidence/synthesise commands, with explicitly selected `scholarly-evidence` 0.1.0, core contract 0.1. This records application of the procedure, not installation, independent evaluation or general effectiveness of the pack.

## Brief and method

Question: what does RULER establish, and not establish, about relying on an advertised context window for a research assistant? The exact PACK prompt in `extension-packs/scholarly-evidence/examples/showcase.md` governs this run. Output is a supported, historically bounded answer and a proposed verification step; product selection and approval remain outside scope. The supplied baseline facts—different v2/v3 populations and context-dependent thresholds—were available before retrieval.

Before acquisition, selected a focused supplied-corpus appraisal: one underlying RULER work, two eligible paper revisions, and the arXiv identity/status record. A model/configuration result is an observation within that work, not an independent study. Both revisions are eligible for historical findings and method comparison; v2’s earlier status does not justify excluding its results. Exclude v1, linked repositories, cited literature and all other sources. No broad search, model execution, paid processing, installation or credential use is authorised or performed.

Planned appraisal: inspect each revision’s population, task configurations, scoring denominator, threshold and failure modes; check consequential tables visually; reconcile like model/configuration rows before synthesis; distinguish benchmark validity from transfer to research work. Eight source actions were the ceiling, with the final actions reserved for fidelity/gap checks; local synthesis and producer review require no additional acquisition. No outstanding jobs or reservations remain.

## Sources and actual access

All source inspection occurred on 2026-09-13. This was a focused single-producer review, not exhaustive literature retrieval, dual screening or an independent replication.

| ID | Source, identity and eligibility | Access and limits |
|---|---|---|
| S0 | Authors’ [arXiv record 2404.06654](https://arxiv.org/abs/2404.06654), Hsieh et al.; included for identity/status | Direct web open: title, authors, abstract, submission history. Record lists v2 dated 11 April 2024, v3 dated 6 August 2024 and COLM 2024. This is only the inspected status channel. |
| S2 | [v2 paper](https://arxiv.org/pdf/2404.06654v2), 11 April 2024; earlier representation, retained | Author-original PDF and existing extracted text supplied in `/workspace/scratch/b99193148918/l2-02-source-cache/`; inspected selected text pages and cached PDF-page image. Page 1 identifies v2 and “Preprint. Under review.” No fresh download or full-paper visual inspection. |
| S3 | [v3 paper](https://arxiv.org/pdf/2404.06654v3), 6 August 2024; later representation, retained | Same supplied-cache route. Page 1 identifies v3 and publication at COLM 2024; bounded text inspection plus Table 3 page image. Neither version is counted as a separate independent study. |

Actual source-action ledger (8/8; no search queries):

1. Open S0 directly at its exact URL.
2. Read S2 extracted text, PDF pages 1–7, 14–15. Tool output partially truncated; rely only on visible passages and subsequently checked Table 3.
3. Read S3 extracted text, pages 1, 5–9, 17–18. Tool output partially truncated; rely only on visible passages and subsequently checked Table 3.
4. Visually inspect supplied `ruler-v2-p6.png`, Table 3 and §4.
5. Visually inspect supplied `ruler-v3-p7.png`, Table 3 and adjacent prose.
6. Read S3 text pages 10 and 19: limitations and task-selection method.
7. Read S2 text pages 10 and 16: page 10 was references, page 16 supplied task-selection method.
8. Read S3 text page 11 to check for continued limitations; it was references and added no substantive evidence. No referenced external source was opened.

Transformations: selected page ranges from existing PDF-to-text derivatives; visual cross-check of the two consequential result tables; paraphrase and manual counting of table rows above 85.6 at 32K. The original cache creation and byte-level download identity were not independently revalidated in this run. No unseen graph values or truncated passages supply claims.

## Evidence and linkage

| Evidence | Inspected locator | Bounded extraction |
|---|---|---|
| E1: work/report linkage | S0 submission history; S2/S3 p.1 | Same arXiv work identifier, title and author team; v3 is a later revision of v2. Status changes from under-review preprint to stated conference publication. This does not create another independent experiment or invalidate all earlier findings. |
| E2: shared measurement design | S2 p.6 §4, p.15 Table 5, p.16 App. C; S3 p.6 §4, p.18 Table 5, p.19 App. C | Thirteen configurations span retrieval, variable tracking, aggregation and QA. Each task/length uses 500 generated examples; tested main-table lengths are 4K, 8K, 16K, 32K, 64K, 128K. Recall-based accuracy checks target output presence after answer-prefix prompting; Table 3 averages the 13 task accuracies. Both Table 5s retain the same stated configurations, including four-value/query retrieval, one chain/four hops, and SQuAD/HotpotQA with distractors. Selection used correlation clustering of 18 configurations on eight models, not demonstrated validation against research-assistant outcomes. |
| E3: v2 findings retained | S2 pp.6–7 §4/Table 3; p.14 App. A | Ten main-table long-context models, excluding the Llama2 baseline. Four exceed 85.6 at 32K: GPT-4, Command-R, Yi-34B and Mixtral-8x7B. Mixtral reaches its claimed 32K at 85.9 and thus is an eligible exception to any blanket claim that all models fail at their advertised length. GPT-4 scores 87.0 at 64K, 81.2 at 128K; Yi scores 87.5 at 32K, 83.2 at 64K. Appendix A specifies GPT-4 as `gpt-4-1106-preview`. |
| E4: v3 findings and reconciliation | S3 pp.6–7 §4/Table 3; p.17 App. A; compare E3 | Seventeen main-table models. A manual count of its 32K column gives 10/17 above 85.6; the abstract’s “only half” is qualitative. Seven model rows persist from v2; Command-R, Mixtral-8x7B and ChatGLM leave the main table and ten others enter. Command-R-plus and Mixtral-8x22B are different configurations, not longitudinal replacements that demonstrate an improvement. Shared GPT-4 and Yi rows retain their displayed values. Gemini-1.5-Pro scores 94.4 at 128K and is labelled `>128K`; the table actually tests only through 128K, not the advertised 1M. |
| E5: threshold and transfer limits | Both Table 3 captions/§4; S3 p.10 §8 | “Effective” length is an operational classification against Llama2-7B’s 4K score, 85.6%, on this task aggregate. S3 explicitly reports missing realistic-task correlation, depth-level/position analysis, comprehensive prompt-robustness study and more demanding short-context evaluation. The 500-example denominator and aggregate do not provide a research-assistant error probability. Table 3 supplies no uncertainty interval for crossing the threshold. |
| E6: eligible adverse observations | S2 p.7 §5; S3 pp.7–9 §5 | Yi’s examined configurations show distractor confusion, incomplete retrieval and copying; S3 also describes tracking failures and QA degradation toward the no-context baseline. These are source-reported failure modes of examined settings, not established frequencies in a deployed research assistant. |

The synthesis unit is one work. The two main-table denominators (10 and 17) are distinct revision-specific model samples; do not pool them as 27 independent models or treat their agreement as two replications. Identical shared table rows establish repeated reporting, not proof that the authors reran those experiments. Run-level independence is unknown. V2’s Mixtral result remains valid for that representation even though its model configuration is absent from v3’s main table.

Method-specific appraisal also found internal source discrepancies: S3 Table 3 lists Mixtral-8x22B’s claimed length as 64K and DBRX’s as 32K, whereas Appendix A lists 32K and 1M respectively. S2 Table 3 lists ChatGLM as 128K while Appendix A prints 128M. These unresolved metadata conflicts preclude silently harmonising those advertised-length comparisons; the central conclusion uses the explicitly located table results and unaffected examples. Both §4 descriptions also blanket-describe local vLLM/GPU execution despite including API models; exact closed-model serving details are not established here.

## Claims and answer

| Claim | Type and support | Qualification / uncertainty |
|---|---|---|
| C1: Advertised capacity and a successful simple retrieval test do not establish reliable performance across long-context behaviors. | Qualified synthesis, E2–E6 | Direct results demonstrate failures in selected historical configurations; transfer to a research assistant is an inference, not a measured application failure rate. |
| C2: A later population changes the headline without erasing eligible earlier findings. | Supported observation, E1/E3/E4 | 4/10 and 10/17 describe different samples within one work. No pooled estimate or independent corroboration claim. |
| C3: RULER’s effective length cannot be adopted as an application acceptance cutoff without further evidence. | Supported methodological inference, E2/E5 | Assumes the assistant needs faithful real-document synthesis, citations and robust prompting; those outcomes are not validated by the benchmark metric. |
| C4: Verification should use the actual intended assistant configuration and research tasks. | Conditional recommendation, C1/C3/E6 | Proposed only; no test executed or product approved. Application owner chooses acceptable error and completeness levels. |

**Answer (exact producer wording).** RULER supports treating an advertised context window as insufficient evidence that a research assistant will use that whole input reliably. Its controlled tasks test retrieval, tracing, aggregation and QA, and expose degradation that simple needle retrieval can miss. That is an inference for assistant design from benchmark findings, not a measured reliability guarantee or failure rate for your assistant. [v2 §4–5, pp.6–7](https://arxiv.org/pdf/2404.06654v2); [v3 §4–5, pp.6–9](https://arxiv.org/pdf/2404.06654v3).

The historical findings need their versions. V2’s 32K threshold is exceeded by four of ten models, including Mixtral-8x7B at its advertised 32K. V3 changes the tested population and its table yields ten of seventeen above the same threshold at 32K. Its Gemini result stays above threshold through the tested 128K; the `>128K` label does not demonstrate performance at 1M. The revisions represent one work, with shared findings, not two independent confirmations. [v2 Table 3, p.6](https://arxiv.org/pdf/2404.06654v2); [v3 Table 3, p.7](https://arxiv.org/pdf/2404.06654v3); [arXiv history](https://arxiv.org/abs/2404.06654).

The effective length is the largest tested length passing an aggregate benchmark threshold of 85.6%, chosen from Llama2-7B at 4K. It is not an established limit for every task or an acceptance criterion for research quality. The authors acknowledge unverified correlation with realistic tasks, missing position-level analysis and limited prompt robustness testing. Therefore RULER does not establish completeness of evidence synthesis, citation correctness, or reliable behavior on your documents, prompts and model version. [v3 §4, Table 3 and §8, pp.6–7,10](https://arxiv.org/pdf/2404.06654v3).

The next justified step is to define a small verification set for the exact intended assistant: real research questions with known supporting passages, distractors and multi-document dependencies, tested at short and intended long input lengths and varied evidence positions. Score omitted evidence, unsupported conclusions, citation correctness and task completion against criteria chosen by the application owner; vary representative prompts and repeat cases to examine variability. RULER can supply additional diagnostic tasks. This is a proposed application test derived from the observed failure modes and transfer gaps; it has not been run. [v3 §5 and §8, pp.7–10](https://arxiv.org/pdf/2404.06654v3).

These findings concern paper representations dated April and August 2024. Checking the arXiv record on 13 September 2026 does not update their model-performance observations or establish current product rankings. Reassess when the intended model/configuration, workload, acceptance criteria or eligible source revision changes. [arXiv submission history](https://arxiv.org/abs/2404.06654).

## Producer self-check and handoff

Checked P1 wording against the above evidence: distinct brief/source/evidence/claim/answer semantics; exact version and page locators; explicit denominators and threshold; preserved adverse and favorable exceptions; linked work/report units; no pooling, statistical precision claim, universal threshold, current ranking, exhaustive-review claim or product approval. Source bibliography/status is adequate within this channel; substantive transfer remains qualified. Internal metadata discrepancies and unvalidated deployment applicability remain open under the authorised source boundary.

Actual specialised conduct was configuration-level reconciliation before synthesis, preservation of an earlier eligible exception, checking the metric against intended research outcomes, and tracing those gaps to the proposed verification. This is a producer self-check only. P1 is written locally for parent review; the separate review is pending and this producer has neither written nor claimed it. Collection stopped at 8/8 actions with the bounded draft answered; any issue decision awaits that review. No other-condition answer, historical comparison or oracle was read; no installed-pack test or independent-evaluation result is asserted.
