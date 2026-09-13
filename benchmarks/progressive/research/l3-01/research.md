# Long context versus retrieval for evidence-led research

Producer revision: **L3-01-r2**, 2026-09-13. Conditional decision report; proposed evaluation only. Separate fixed-input audit is pending at `evaluation/audit.md`; this producer has not authored that audit or claimed its result.

## Decision and scope

Do not remove retrieval from an evidence-led research workflow on the strength of these benchmarks. Test long-context reading as an alternative for a bounded, already acquired corpus, and retain retrieval or a hybrid route as a comparison. This is a **transfer inference**, not a reported production result. The distinction matters: retrieving information *inside an input* does not establish the ability to discover authoritative sources, resolve versions, substantiate citations, handle contradictory evidence, or maintain a research record.

For a software team, the conditional choice is:

| Situation | Proposed decision | What could reverse it |
|---|---|---|
| Complete, stable evidence packet fits the usable input budget | Evaluate full-context reading alongside retrieval over that same packet | Missing evidence, position failures, weak citation support, or unacceptable measured cost/latency |
| Evidence corpus exceeds the window or must be refreshed | Retain an acquisition/retrieval stage; test long-context reading over selected documents | A demonstrated alternative that preserves coverage and refresh correctness within actual constraints |
| Questions require dispersed support or global comparison | Include full-context and hybrid candidates; measure all required evidence, not merely answer strings | Retrieval with tuned chunking and multi-step acquisition performs better on the team's tasks |
| No representative, adjudicated test set exists | Keep the architectural decision provisional | The task-specific evaluation below supplies sufficiently precise comparative evidence |

The team owns acceptable error rates and operating constraints. These are evaluation recommendations, with the value assumption that traceable evidence and omission detection matter more than a benchmark leaderboard position. No current model, procurement, deployment, or universal production-suitability verdict is established.

## Actual method and authority

The exact example prompt was read before work. Its installed-skill wording is qualified by the actual environment: this run applied the checked-out `skills/deep-research/SKILL.md`, core contract **0.1**, and explicitly selected `extension-packs/scholarly-evidence` **0.1.0** after reading `pack.json`, `PACK.md`, and `references/method.md`. This is an actual use of that production draft profile; no installation, previous demonstration, or specialist acceptance is claimed. The profile's recorded status flags were designed=true and procedure_demonstrated/installed_tested/behaviourally_evaluated=false. `research-evaluate` belongs to the separate parent audit operation.

Frame, plan, discover, extract-evidence, analyse-evidence and synthesise command contracts were read and applied. Before collection, the plan selected original scholarly works, official status records and author implementations; appraised experimental design and transfer; counted works/study programmes while linking reports and versions; and reserved nine of 36 source actions for separate audit. No existing L3-01 producer directory was present to revise.

Eligibility: the three named originals are mandatory. Add a primary comparison only to close a material LC-versus-retrieval gap. Retain unfavorable, favorable and null findings; exclude secondary explainers, surveys and unrelated benchmark expansion from synthesis. This is a focused, question-led appraisal, not systematic screening, a meta-analysis, dual review, or exhaustive coverage of the literature through 2026. Access occurred on 2026-09-13; empirical observations remain tied to the studies' 2023–2024 configurations.

## What the inspected evidence supports

**C1 — Supported diagnostic warning, qualified transfer: RULER.** The inspected v3 paper describes 17 evaluated long-context models, including Gemini-1.5-Pro, GPT-4 and 15 open models, across 13 tasks. Each model/task/length setting uses 500 examples, at 4K, 8K, 16K, 32K, 64K and 128K, with recall-based accuracy and answer prefixes. Retrieval, variable tracing, aggregation and distractor-augmented QA test different demands. Its effective-length threshold is the Llama2-7B baseline's 4K score, not an application acceptance criterion. The authors report degradation with length for most models, but Gemini-1.5-Pro remains above the 85.6% threshold through the maximum tested 128K. Table 3 labels its effective length “>128K”; this is not measured performance beyond that range. The evidence does not justify universal LC failure. The earlier v2 evaluated ten models; its four-at-32K statement cannot be silently combined with v3's expanded population. Locators: [RULER v3](https://arxiv.org/pdf/2404.06654v3), §§3–4, pp. 3–7 and Table 3; [v2](https://arxiv.org/pdf/2404.06654v2), abstract and Table 3. The cached originals were inspected directly, without using another case's answer.

**C2 — Supported position effect, task-bounded: Lost in the Middle.** The TACL paper evaluates MPT-30B-Instruct, LongChat-13B-16K, GPT-3.5-Turbo/16K (0613), and Claude-1.3/100K; GPT-4 appears in a subset. Controlled QA uses 2,655 NaturalQuestions queries, one answer-bearing document among 10/20/30 passages, greedy decoding and answer-presence accuracy. Synthetic UUID retrieval uses 75/140/300 pairs, 500 examples each. QA is often worse for middle evidence, but Claude performs nearly perfectly on the synthetic task; query-aware prompting helps synthetic retrieval more than QA. These controls isolate position and distractor load, not multi-hop research. The separate open-domain retrieval case shows that increased retriever recall need not translate into commensurate answer improvement. Locators: [published paper](https://aclanthology.org/2024.tacl-1.9.pdf), §§2–5, Figs. 5/7, pp. 159–165. Neither a retrieval-only nor a full-context-only workflow is vindicated.

**C3 — Supported heterogeneous capability, not a workflow score: LongBench.** The original has 21 datasets/six categories, eight models, and different task metrics. Models are GPT-3.5-Turbo-16k, Llama2-7B-chat-4k, LongChat-v1.5-7B-32k, XGen-7B-8k, InternLM-7B-8k, ChatGLM2-6B/32k and Vicuna-v1.5-7B-16k. QA includes multi-hop datasets; summarization and code broaden coverage. Inputs exceeding each window are middle-truncated; decoding is greedy. Dataset sizes and length units vary: English/code lengths are words, Chinese lengths characters. LongBench-E resamples 13 English datasets into length bands; it is not another independent study. The compression comparison uses ada-002, Contriever or BM25, with 200×7 or 500×3 chunks. Retrieval helps some weaker-context configurations but is not uniformly beneficial. Locators: [versioned original](https://arxiv.org/html/2308.14508v2), §§3–4, Tables 1–4. Aggregating F1, ROUGE, classification/exact-match and edit-similarity scores does not yield research reliability. Truncation and model differences prevent attributing every score difference solely to context capacity.

**C4 — Eligible counterevidence: a direct LC/RAG comparison.** Li et al.'s [2407.16833v1](https://arxiv.org/html/2407.16833v1), §§3–5, compares Gemini-1.5-Pro, gpt-4o-2024-05-13 and gpt-3.5-turbo-0125 over nine English query-based datasets from LongBench and ∞Bench. Retrieval uses 300-word chunks, default top-five, with Contriever/Dragon; metrics include F1, accuracy and ROUGE. Full context has higher reported average scores, while RAG is favorable for GPT-3.5 on the two very long ∞Bench tasks. Self-Route trades input tokens against performance. The inspected HTML's narrative averages do not consistently match its Table 1; no exact advantage or saving is adopted here. Its contamination caveat remains unresolved. This is direct evidence for configuration-dependent tradeoffs, not all retrieval systems or research pipelines. Only the pinned v1 findings are used; later publication/revision equivalence and implementation were not verified.

## Claim appraisal and unresolved transfer

| Claim | Support and counterevidence | Assessment |
|---|---|---|
| Advertised capacity or a successful needle test establishes usable research capacity | C1/C2 diagnose different failure conditions; successful synthetic cases remain | Unsupported |
| LC must be inferior to retrieval | C3/C4 contain favorable LC results | Unsupported |
| Retrieval recall alone ensures a supported answer | C2 distinguishes retrieved information from its successful use | Unsupported |
| These studies measure the whole evidence-led research workflow | Their inspected tasks/output metrics do not test source discovery, report linkage, citation entailment and refresh together | Unsupported; this is a design-coverage inference |
| The software team should compare full context, retrieval and hybrid under matched conditions | C1–C4 motivate different failure mechanisms; local task distribution and objectives are unobserved | Conditional recommendation |

No pooled model ranking or aggregate independent-experiment count is calculated. The four included work/study programmes reuse datasets and, in places, model families; agreement is not four independent replications. A source's authority for its own methods or publication status does not certify application transfer. The controlled studies offer useful mechanism checks, while the realistic datasets trade experimental control for task breadth. Both directions matter.

Open gaps: (G1) representative current team tasks/model versions/corpus and acceptance values; (G2) direct end-to-end research evidence; (G4) direct RULER OpenReview access; (G5) later status/equivalence of the optional Li comparison; (G6) separate fixed-input audit. G1/G2 require the proposed evaluation or additional authorized evidence; G4/G5 limit status claims, not license guessed equivalence. G3 is resolved for the retained original LongBench implementation: parent follow-up inspected `LongBench/README.md` and `LongBench/pred.py` at commit `2e00731f8d0bff23dc4325161044d0ed8af94c1e`. That establishes the original benchmark code retained at this current commit, not historical paper-execution byte identity. See the source map. Other gaps remain open; four reserved source actions remain for parent audit.

## Collection record, actual budget and preservation

Ceilings: **12 search queries and 36 source actions for the whole task**. Producer collection: **4 queries, 27 source actions**. Parent follow-up used **5 source actions**, making the aggregate **4 queries, 32 source actions**. **4 source actions and 8 queries remain**; remaining source actions are reserved for parent audit, not optional producer collection. No outstanding jobs, paid calls, installs, model tests, credential use or communications. Finalisation used local writing/checking, not additional source collection.

Four exact queries, in order (native web search; no date filter):

1. `RULER What’s the Real Context Size of Your Long-Context Language Models arxiv COLM 2024`
2. `Lost in the Middle How Language Models Use Long Contexts TACL 2024 github`
3. `LongBench A Bilingual Multitask Benchmark for Long Context Understanding ACL 2024 github`
4. `site.aclanthology.org Retrieval Augmented Generation or Long-Context LLMs comprehensive study hybrid approach Li 2024`

Initial search results supplied candidate identities; only primary originals were selected. Query 4 also surfaced LongRAG and secondary/survey material; those were not pursued because a direct comparator sufficed for the bounded gap. Search output was not treated as inspected full text. No database pagination, systematic citation chaining or complete status/correction sweep was performed.

The single compact actual-source record is in `study-report-map.md`. Reopens, failed reads and cached inspections count separately; task instructions, local drafts and skill reads are not literature-source actions. Text extraction/HTML normalization supported paraphrase; no benchmark outputs were generated. No chart values were inferred from images. Source locators retain exact versions where available, and current repository READMEs are explicitly mutable.

## Producer self-check and handoff

Producer self-check, r1: covered the named original works, version linkage, task/model/condition distinctions, favorable LC evidence, transfer limits, conditional choices and a nonexecuted evaluation proposal. Checked that report versions were not counted as extra studies and no current-model suitability claim was made. Structural completeness of the three producer files does not certify scholarly adequacy. Implementation access and independent-review gaps remain explicit; no specialist approval is claimed.

Fixed input for parent evaluation: `research.md`, `study-report-map.md`, `evaluation-proposal.md`, all **L3-01-r2**. Parent owns `evaluation/audit.md`. Producer draft complete; independent review/issue pending. Refresh if a cited report changes materially, historical implementation equivalence is established, corpus/model/prompt/retriever changes, or team acceptance criteria become concrete. Preserve unaffected source bases and revisit affected claims rather than silently repointing them.

## r2 repair and source-action note

Parent independent reading of r1 identified the C1 tested-range overstatement and supplied original-table evidence; r2 narrows C1 to measured performance through 128K. Parent then used five reserved GitHub source actions to recover the retained original LongBench README and prediction code at an exact current commit. Their actual inspection is attributed to the parent, not claimed as a producer fetch. G3 and its dependent map/proposal wording are repaired; other evidence and limitations are preserved. The three exact r1 producer files remain under `revisions/r1/`. Producer r2 self-check verified the narrow changes and exact preservation of all three r1 files. This repair made no new source acquisitions. The three r2 files are fixed inputs for the parent’s final audit; no audit result or independent approval is claimed here.
