# RULER v2 and v3: bounded comparison

Producer revision R1, fixed for separate evaluation on 2026-09-13 UTC. This is a comparison of two reports of one research work. Independent audit is pending; this file is the producer submission, not an issued audit or a replication.

## Brief, authority and method

The question is how versions 2 and 3 differ in model population, task coverage, effective-context definition and applicability to a research workflow. The historical versions are the temporal target; retrieval in 2026 does not make their results a current model ranking.

Executed from the authorised production source checkout at revision `b9d262b4bd2ffa73d35b520f98629e7eae0b7da7`, using `skills/deep-research/SKILL.md` and its frame, plan, discover, extract-evidence, analyse-evidence and synthesise contracts. No Extension Pack was used. This records source-checkout execution, not installation or installed-skill performance. The immutable [exact L2-02 prompt](https://github.com/sb-dev/deep-research-skills/blob/b9d262b4bd2ffa73d35b520f98629e7eae0b7da7/examples/level-2-ruler-report-versions/README.md#exact-prompt) supplies the research and audit requirements.

Before collection, the plan reserved at least four of the 18 source actions for the separate evaluator and capped searches at six. It assigned identity/history to official arXiv metadata, version-specific findings to the two versioned PDFs, and decisive tables to visual inspection. Inclusion required an official representation of the requested work/version. The intended synthesis was a version comparison, with separate denominators, contrary passages and unresolved limitations. No purchases, model benchmark execution, new private access or external publication were authorised or performed.

## Work, reports and inspected sources

The work is *RULER: What's the Real Context Size of Your Long-Context Language Models?*, by Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang and Boris Ginsburg; arXiv:2404.06654 [cs.CL], DOI 10.48550/arXiv.2404.06654. The [official record, title/authors and Submission history](https://arxiv.org/abs/2404.06654) establishes v1 on 9 April 2024, v2 on 11 April, and v3 on 6 August. This run did not inspect the v1 original.

| Source | Bibliographic identity and representation | Actual inspected scope |
|---|---|---|
| W | [Official arXiv work record](https://arxiv.org/abs/2404.06654); retrieved 2026-09-13 | Title, authors, identifier, DOI, abstract, version links and Submission history. |
| V2 | [arXiv:2404.06654v2 original PDF](https://arxiv.org/pdf/2404.06654v2); submitted 2024-04-11 23:53:59 UTC; 23 pages; preprint under review | Text on printed pp. 1–6, 9, beginning of 10, 14–15; original page images inspected on pp. 6, 14, 15. |
| V3 | [arXiv:2404.06654v3 original PDF](https://arxiv.org/pdf/2404.06654v3); submitted 2024-08-06 21:48:58 UTC; 27 pages; marked as a COLM 2024 conference paper | Text on printed pp. 1, 4–7, 10, 17–18; original page images inspected on pp. 7, 17, 18. |

All locators below use printed page numbers, which match one-based PDF page numbers. Both complete PDFs were acquired; inspection was selective as recorded above. Native PDF text and locally extracted text are representations of the respective original, not additional sources or studies. The official version history establishes V3 as a revision of V2 within one work. Repeated results therefore do not provide independent corroboration.

These are primary author reports, authoritative for their own versioned contents. Their benchmark results remain author-reported and unreplicated here. Synthetic-task design and creator-selected criteria limit applicability; versioned originals improve traceability, not external validity. No source independence is inferred from URL count.

## Evidence and claim analysis

**C1 — revised population; supported extraction and explicit set comparison.** The authors' main populations are 10 (nine open models plus GPT-4) in V2 and 17 (15 open models plus GPT-4/Gemini) in V3. Appendix A's broader totals are 30 and 37, respectively; those are different denominators. [V2 §4/Table 3, p. 6; Appendix A/Table 4, p. 14](https://arxiv.org/pdf/2404.06654v2#page=6), [V3 §4, p. 6; Table 3, p. 7; Appendix A/Table 4, p. 17](https://arxiv.org/pdf/2404.06654v3#page=7).

| Membership in main comparison | Models, retaining version-specific variants |
|---|---|
| Shared: 7 | GPT-4; Yi-34B; Mistral-7B/v0.2; LWM-7B; Together-7B; LongChat-7B; LongAlpaca-13B |
| V2 only: 3 | Command-R-35B; Mixtral-8x7B; ChatGLM-6B |
| V3 only: 10 | Gemini-1.5-Pro; Llama3.1-70B; Llama3.1-8B; Qwen2-72B; Command-R-plus-104B; GLM4-9B; GradientAI/Llama3-70B; Mixtral-8x22B; Phi3-medium-14B; DBRX |

The membership mapping uses the visually inspected [V2 Table 4, p. 14](https://arxiv.org/pdf/2404.06654v2#page=14) and [V3 Table 4, p. 17](https://arxiv.org/pdf/2404.06654v3#page=17): Mistral resolves to the same v0.2 checkpoint and GPT-4 to `gpt-4-1106-preview`. Each version's population uses its shared and version-only rows; the Llama2 baseline is excluded. Similar family names do not identify the same evaluated model.

**C2 — stable task coverage; supported comparison.** Both retain 13 configurations: eight retrieval (three single-NIAH, three multi-key, one multi-value, one multi-query), one variable-tracking, two aggregation (CWE/FWE), and two QA (SQuAD/HotpotQA). The configuration tables agree. [V2 Appendix B/Table 5, p. 15](https://arxiv.org/pdf/2404.06654v2#page=15), [V3 Appendix B/Table 5, p. 18](https://arxiv.org/pdf/2404.06654v3#page=18).

**C3 — stable effective-context rule; supported, benchmark-qualified.** Effective length is the maximum tested length whose 13-task mean exceeds 85.6%, the Llama2-7B-chat 4K baseline. Both use 500 examples/task/length, recall-based scoring and 4K/8K/16K/32K/64K/128K evaluations. Weighted ranking is separate. [V2 §4/Table 3, p. 6](https://arxiv.org/pdf/2404.06654v2#page=6), [V3 §4, p. 6 and Table 3, p. 7](https://arxiv.org/pdf/2404.06654v3#page=6).

**C4 — changed headline; supported recount, qualified interpretation.** V2's abstract reports four passing at 32K; V3 says approximately half. Counting Table 3's 32K entries above 85.6 gives **4/10 versus 10/17**. [V2 abstract, p. 1 and Table 3, p. 6](https://arxiv.org/pdf/2404.06654v2#page=6), [V3 abstract, p. 1 and Table 3, p. 7](https://arxiv.org/pdf/2404.06654v3#page=7). This is a changed-population comparison, not a longitudinal improvement estimate.

**C5 — unresolved limits and contrary cells.** V3 labels Gemini >128K but reports tests only through 128K. Table 3/Table 4 context metadata disagree: V2 ChatGLM 128K/128M; V3 Mixtral-8x22B 64K/32K and DBRX 32K/1M. [V2 pp. 6, 14](https://arxiv.org/pdf/2404.06654v2#page=14), [V3 pp. 7, 17](https://arxiv.org/pdf/2404.06654v3#page=17). The labels and disagreements are established; their corrections and performance beyond the tested boundary remain unverified.

**C6 — revised transfer caveats; supported extraction.** V3 adds limitations covering unvalidated proxy–realistic-task correlation, position-depth reporting, short-context coverage and prompt robustness. V2 has no dedicated limitations section. [V3 §8, p. 10](https://arxiv.org/pdf/2404.06654v3#page=10), [V2 §7, p. 9, followed by references on p. 10](https://arxiv.org/pdf/2404.06654v2#page=9).

## Synthesis for a research workflow

**C7 — qualified inference and recommendation, not an observed workflow result.** C1–C6 support using these historical results as inputs to a model-screening discussion. They do not establish an acceptance rule for research. The decision owner should define criteria on the actual document collection and workflow: finding relevant evidence, retaining provenance, citing faithfully, handling contradictions and producing a supported synthesis. Test the intended model version, prompts, input lengths and tool access against those criteria. This recommendation assumes those are the workflow's objectives; no such assessment was executed here.

Stable task coverage and a stable benchmark cutoff make the version comparison interpretable, but neither supplies the missing transfer evidence. Do not apply 85.6% as a universal quality gate, infer a verified maximum beyond the evaluated range, or combine the two populations as independent studies. The scope of support is the inspected reports and benchmark conditions.

Open gaps are the actual maximum beyond the reported grid, correction of conflicting context metadata, and external validation for the intended research workflow. None was silently closed. Resolving metadata would require targeted authoritative clarification; validating workflow transfer would require separately authorised evaluation. No correction search or benchmark was performed because the existing evidence supports a bounded comparison with these explicit limits. The separate fixed-input audit remains required before issue.

## Actual execution, budget and producer self-check

Runtime: ChatGPT Work Mode on Linux; native `web.run`; Python 3.12.14 with `urllib`; Poppler `pdftotext`/`pdftoppm` 24.02.0; `view_image`. Operations performed: frame → plan → discover → extract-evidence → analyse-evidence → synthesise, with producer support checks. No hosted broad-research engine or model benchmark was used.

| Actual source operation | Count | Scope/result |
|---|---:|---|
| Search | 1 | Exact query: `site:arxiv.org "RULER: What's the Real Context Size"`; one returned result set. Selected the official work; current GitHub leaderboard, aggregators, v1 snippets and social results were not used as evidence for this comparison. |
| Official work open | 1 | Identity and version history. |
| Initial versioned PDF opens | 2 | Both originals resolved; native extraction exposed different text extents. |
| Targeted native PDF reads | 2 | V2 around line 263; V3 around line 264, covering task context and §4. |
| Direct original-PDF downloads | 2 | Both HTTP 200, application/pdf; V2 658,037 bytes, V3 682,955 bytes. Local parsing addressed incomplete native text exposure. |
| Original page-image inspections | 6 | V2 pp. 6/14/15 and V3 pp. 7/17/18, rendered at 180 dpi; Tables 3, 4 and 5 inspected with headings, row labels, units and captions. |

**Consumed: 1/6 searches and 13 non-search source reads/actions. Conservatively charging the query as an action too gives 14/18, leaving four actions reserved for the evaluator.** There are no outstanding jobs, failed source actions or source-access blockers. No additional acquisition is needed to finalise this producer submission. Local skill/task reads, deterministic processing of retained content and report edits are operational work, not fresh external acquisitions; page-image inspections are nevertheless charged individually above.

The full PDFs and inspection PNGs are retained as temporary support in `/workspace/scratch/b99193148918/l2-02-source-cache/`. Text extraction used `pdftotext -layout`; PNGs were generated directly from the original PDFs with `pdftoppm`. Transformations were paraphrase, model-identity matching using Table 4, set comparison, and a local recount of the transcribed Table 3 32K scores. The recount reproduced 4/10 and 10/17, with seven shared model identities. These computations did not run an inference experiment. Original figures and other appendix results were not visually audited and do not support additional quantitative claims here.

Producer self-check: verified version stamps and official lineage; separated work, reports and representations; visually checked all decisive tables; checked membership and task-count arithmetic, baseline/denominator context, citation locators, contrary cells, and inference wording. Identity and direct extraction are supported by original access; benchmark truth is not independently replicated, and workflow transfer is unvalidated. These are producer checks, not an independent or specialist audit.

The requested output was absent before this run. The initial brief/plan was read and reconciled into R1; no prior accepted report was replaced. This file is now fixed for the parent's separate `research-evaluate` operation. The producer did not create or claim `evaluation/audit.md`. Changes after audit submission require a revised report and review of the affected claims. The actual producer deliverable is `research/l2-02/research.md`; issue awaits the separate audit.
