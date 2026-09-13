# RULER and reliance on an advertised context window — core condition

Revision: core-r1, 2026-09-13. Supported historical answer, with producer self-check; separate parent audit pending. Source-checkout implementation proof using the actual `skills/deep-research/SKILL.md` at checkout HEAD `b9d262b4bd2ffa73d35b520f98629e7eae0b7da7`; no installed-skill or Extension Pack claim.

**RULER establishes that accepting a long input, or retrieving one easy needle from it, is insufficient evidence that a model will use that input reliably across more demanding tasks.** For a research assistant, the justified inference is to verify the particular workload before relying on its advertised window. RULER does not establish a universally safe token limit, measure the reliability of a complete research assistant, or approve a current product.

## Direct findings and version boundaries

The authors' [arXiv record](https://arxiv.org/abs/2404.06654), submission history, dates v2 to April 11, 2024 and v3 to August 6, 2024. The originals identify v2 as a preprint under review and v3 as a COLM 2024 conference paper. These are revisions of one author-origin work, not independent replications.

| Evidence | v2 original | v3 original | What survives the comparison |
|---|---|---|---|
| Main population | 10 models: GPT-4 and nine open-source models; Appendix A describes 30 across evaluation and analysis | 17 models: GPT-4, Gemini-1.5-Pro and 15 open-source models; Appendix A describes 37 overall | Keep main-comparison and total-analysis denominators separate. The later population changes; proportions are not longitudinal improvement estimates. |
| Main outcome | Four exceed the 85.6% baseline at 32K: GPT-4, Command-R, Yi-34B, Mixtral-8x7B | Abstract says about half; counting Table 3's 32K scores strictly above 85.6 gives 10/17 | Both versions show a gap between advertised size and satisfactory benchmark performance for many evaluated models. Preserve the table count alongside the later abstract's broad wording. |
| Important exceptions | Mixtral-8x7B passes at its claimed 32K: 85.9%; its 64K score is 72.4%, below this threshold | Gemini-1.5-Pro scores 94.4% at 128K; table labels effective length `>128K` against claimed 1M | Do not say every model fails at its advertised size. Gemini passes through the maximum main-test length; these measurements do not demonstrate success beyond 128K or at 1M. |
| Shared concrete result | GPT-4: claimed 128K, effective 64K, 87.0% at 64K and 81.2% at 128K | Same scores and effective-length label | This result remains valid for the tested model and setup in both representations. Appendix A identifies `gpt-4-1106-preview`; this is not a finding about all later GPT-4 offerings. |

Locators: [v2 PDF](https://arxiv.org/pdf/2404.06654v2), pp. 1, 6–7, Table 3 and Appendix A p. 14; [v3 PDF](https://arxiv.org/pdf/2404.06654v3), pp. 1, 6–7, Table 3 and Appendix A p. 17. Page numbers are printed pages and coincide with PDF page positions here. The 10/17 count is a local count of inspected Table 3 cells, not an authors' quoted count.

**The threshold is operational and context-dependent.** Main Table 3 averages 13 task scores and uses the Llama2-7B-chat score at 4K, 85.6%, as its comparator. Effective length is the maximum tested length passing that comparator, on a grid of 4K, 8K, 16K, 32K, 64K and 128K. It is not an intrinsic physical boundary or a research-quality guarantee. Appendix A distinguishes chat and base comparators. For example, v2 Appendix F uses 79.4% for the base-model 13-task average, 96.9% for aligned retrieval, 84.8% for aligned aggregation, and 49.7% for aligned QA. A main-table cutoff must not be transplanted to these task subsets. [v2](https://arxiv.org/pdf/2404.06654v2), §4 p. 6, Appendix A p. 14, Tables 12–16 pp. 22–23; [v3](https://arxiv.org/pdf/2404.06654v3), §4 p. 6, Table 3 p. 7, Appendix A p. 17.

**The evidence extends beyond simple retrieval.** The four categories cover retrieval, variable tracking, word aggregation and QA with added distractor paragraphs. The authors describe tracking and aggregation as proxies for coreference and summarization. They use 500 generated examples per task and length, model chat templates, answer prefixes and recall-based accuracy. These choices define the evaluation; an average does not promise complete, accurate citations or synthesis on every document. [v2](https://arxiv.org/pdf/2404.06654v2), §§3–4 pp. 3–6, Appendix B p. 15; [v3](https://arxiv.org/pdf/2404.06654v3), §§3.2–4 pp. 5–6, Appendix B p. 18.

Both versions retain adverse error analysis: Yi-34B can miss or duplicate requested values, retrieve distractor-associated information, copy from the demonstration, mis-track variables, and approach its no-context QA baseline as distractors increase. The authors also observe inappropriate reliance on parametric knowledge in aggregation. These are reported observations under their configurations, especially the Yi analysis extending to 256K; they are not measured error rates for every research assistant. [v2](https://arxiv.org/pdf/2404.06654v2), §5 pp. 7–8; [v3](https://arxiv.org/pdf/2404.06654v3), §5 pp. 7–9. Conversely, the v2 Appendix E simple-retrieval results remain valid evidence of strength on those easier tasks; they are not discarded because harder tasks perform worse.

## Inference, unknowns and the next verification

**Inference:** a research assistant should treat its advertised window as insufficient evidence of dependable coverage. The relevant concerns are losing a needed source detail, confusing nearby evidence, failing to connect facts, or substituting remembered information. This follows from the observed benchmark failures plus the assumption that the assistant's workload requires related operations. Transfer strength to real research is unknown: synthetic word aggregation is not a validated substitute for evaluating substantive synthesis.

**Not established:** exhaustive source review, factual and citation correctness, coverage of contradictory evidence, reliability of browsing/retrieval tools, multi-turn research behavior, present-day rankings, or a production acceptance threshold. The inspected methods report a finite synthetic benchmark and adapted QA, not those end-to-end outcomes. A 2026 retrieval date does not update the experimental validity of the 2024 models. Exact run dates and immutable snapshots behind every API identifier are not established by the inspected material.

**Next justified verification:** before committing to an assistant, pin its exact model/API revision and workflow, define acceptable omission, unsupported-claim and citation-error rates, and test representative research documents at the intended lengths. Include several relevant passages, competing claims, distractors and multi-hop synthesis; score evidence coverage and source attribution separately from answer correctness, with a shorter-context comparison. This is a proposed downstream test, requiring its own execution authority; no model was run here. Within the current source-only scope, a further authorised pass should first resolve any configuration or metadata discrepancy material to the intended reproduction, rather than guess a correction.

## Evidence cautions preserved

- v3 Appendix A/Table 4 lists Mixtral-8x22B context as 32K and DBRX as 1M, whereas main Table 3 lists 64K and 32K respectively. v2 Appendix A lists ChatGLM as 128M while main Table 3 and its API/model identifier point to 128K. These are visible source-internal discrepancies, confirmed against cached page images; no external specification was used to settle them. The broad caution does not depend on resolving them, but an exact model-by-model advertised-limit audit would.
- v2 Appendix B/Table 5 specifies UUID for the third single-needle value type; the extracted Appendix D/Table 7 template instead uses a word value. The actual experimental configuration behind this mismatch is unresolved. Avoid claiming exact reproducibility from the manuscript alone.
- v3 §4 says all models degrade, while its main-results discussion and Table 3 preserve Gemini's strong exception. Table measurements bound the conclusion. In particular, table notation `>128K` is not evidence of an actual main test beyond 128K.

## Actual access, execution and limits

Authority/intake: fixed question and source universe supplied by requester; existing read tools only, eight-source-action cap, no additional queries. Selection was the arXiv record plus v2/v3 originals. No Extension Pack, historical comparison, other report answer or oracle was read. No paid call, installation, benchmark-model run, delegation, git mutation or external communication occurred. Only this report was written.

| Action | Actual source access | Outcome / fidelity |
|---|---|---|
| 1 | `web.run` open of authors' arXiv record | Success: metadata, abstract and submission history; no broader search. |
| 2 | Python/PyMuPDF extraction of cached original v2 PDF, 23 pages | Extraction succeeded; tool output was truncated. This is not full-text review. Relevant missing main-body passages were reread in action 4. |
| 3 | Python/PyMuPDF extraction of cached original v3 PDF, 27 pages | Read pp. 1, 5–9, 17–18. Success. |
| 4 | Repeat extraction of v2 original | Read pp. 5–9, 14–15. Success; charged as a repeat source action. |
| 5–6 | `view_image` of cached original-page representations: v2 p. 6, v3 p. 7 | Visually checked main tables and their captions. |
| 7–8 | `view_image`: v2 p. 14, v3 p. 17 | Visually checked model identities, denominators and metadata discrepancies in Appendix A. |

Total: 8/8 source actions, zero failed reads, one output-truncated read, one charged repeat. No outstanding source jobs. Infrastructure/skill reads and directory-only discovery are not source actions. No fresh PDF download or independent byte comparison to remote PDFs was performed. Cached PNGs agree with the corresponding extracted table contents; their generation history was not independently reconstructed. Other figures were read through captions/prose, not digitized or exhaustively visually audited.

Cache: `/workspace/scratch/b99193148918/l2-02-source-cache/`. The original PDFs identify their arXiv version and date on p. 1. SHA-256 of v2 PDF: `b28526fc8f8478bc6f1c3c3c169f72f5944644cbe415498c91619218224d4544`; v3: `8a4bc6ca28d84570eec7f42652400c2121f4c8bc361701634e596772e396fc22`. Hashes identify inspected bytes, not experimental truth. Existing extracted `.txt` files and other reports were not used. Transformations were PDF text extraction, visual reading, paraphrase and the explicit threshold-cell count; no OCR or statistical fitting.

Tool runtime observed: source shell extraction processes reported approximately 0.20 s, 0.16 s and 0.10 s; web access and image calls completed successfully without individual wall-time telemetry. These are access-tool observations, not model benchmark runtimes. Eight-source-action exhaustion ends collection; it does not imply exhaustive review.

## Producer self-check and delivery state

Self-check against core-r1: material factual statements have versioned source locators; populations, thresholds and test-length bounds are explicit; supportive exceptions and adverse findings from both originals remain; one work is not counted as corroborating independent studies; transfer to research assistants is labelled inference; current performance and product approval remain unknown. Structural completeness and substantive support were checked by the producer only. Source-internal discrepancies remain open with bounded effects. The historical answer is supported within this access scope; exact reproduction and downstream deployment judgement are not certified.

This file is the fixed core-condition handoff for the parent's separate audit, not that audit's result and not external publication. Next operation: independent evaluation of this exact revision, with any repair confined to affected evidence and claims.
