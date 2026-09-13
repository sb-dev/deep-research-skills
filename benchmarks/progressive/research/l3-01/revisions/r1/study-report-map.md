# L3-01 study, report and implementation map

Revision **L3-01-r1**, accessed 2026-09-13. This is the single compact source/action record for the producer. Interpret with `research.md`; not an independent audit.

## Units and official status

| Work/study programme | Related reports and official record | Actual synthesis boundary |
|---|---|---|
| W1 Hsieh et al., RULER | [arXiv history](https://arxiv.org/abs/2404.06654): v1 2024-04-09, v2 2024-04-11, v3 2024-08-06. v3 records COLM 2024; its PDF masthead agrees. [OpenReview](https://openreview.net/forum?id=kIoBbc76Sy) access hit a verification page. | One programme, with changed model population. Inspected v2 and v3 are related reports, not two independent studies; v1 history only, not full text. COLM status has arXiv/PDF corroboration, not direct OpenReview verification. |
| W2 Liu et al., Lost in the Middle | [arXiv history](https://arxiv.org/abs/2307.03172): v1 2023-07-06, v2 2023-07-31, v3 2023-11-20; v3 says accepted TACL 2023. [Published record](https://aclanthology.org/2024.tacl-1.9/): TACL 12 (2024), 157–173, DOI 10.1162/tacl_a_00638. PDF front matter says published February 2024. | Acceptance year and publication year differ legitimately. Published PDF is the methods/results representation used; preprint history is metadata only. Several task experiments remain within one programme. |
| W3 Bai et al., original LongBench | [arXiv history](https://arxiv.org/abs/2308.14508): v1 2023-08-28, v2 2024-06-19, ACL 2024. [ACL record](https://aclanthology.org/2024.acl-long.172/), DOI 10.18653/v1/2024.acl-long.172; author repository citation identifies pp. 3119–3137, August 2024. | Versioned v2 HTML supplies methods; publisher PDF retrieval failed. LongBench-E is a within-programme resampling. Original LongBench and later named LongBench v2 are distinct benchmark generations; the latter is not an arXiv v2 revision of 2308.14508. No byte identity between publisher PDF and arXiv is claimed. |
| W4 Li et al., Retrieval Augmented Generation or Long-Context LLMs? | [arXiv record](https://arxiv.org/abs/2407.16833); inspected [v1 HTML](https://arxiv.org/html/2407.16833v1), dated 2024-07-23. | One additional comparative programme, sharing LongBench inputs with W3. Pinned preprint findings only; later publication/version correspondence unverified. |

Four work/study programmes are included, not four independent replications and not one study per URL, dataset, model or report. W1/W3/W4 share upstream benchmark/data origins; reuse is not extra independent confirmation. Title/author/identifier relationships and original code links establish report linkage, without claiming identical underlying experimental populations across revisions.

## What is measured — producer classification from inspected designs

| Work | In-context retrieval | Multi-hop use | Position sensitivity | Whole research workflow |
|---|---|---|---|---|
| W1 | Yes | Variable-chain proxy; QA category | Placement is controllable; not a workflow audit | No |
| W2 | Explicit controlled task | Not a general multi-hop benchmark | Explicit controlled intervention | No; includes a bounded retrieval/reader case |
| W3 | Synthetic retrieval and compression | Multi-document QA tasks | Mixed placement; no universal controlled position guarantee | No |
| W4 | Explicit RAG versus LC | Included QA datasets | Not the primary causal intervention | No |

## Relevant original implementations

| Original author repository | Actual inspected implementation evidence | Limit |
|---|---|---|
| [NVIDIA/RULER](https://github.com/NVIDIA/RULER) (paper's older link is hsiehjackson/RULER) | README identifies `scripts/data/template.py`, `scripts/synthetic.yaml`, `scripts/config_tasks.sh` and configurable needle/chain/aggregation/QA generation. Current README distinguishes newer `rulerv1-ns` and `rulerv2-ns` pipelines and marks older instructions deprecated. | README inspection only; no immutable commit pinned, source code executed, or current leaderboard substituted for original-paper results. |
| [nelson-liu/lost-in-the-middle](https://github.com/nelson-liu/lost-in-the-middle) | README links original paper, QA data, UUID format, and `scripts/make_qa_data_from_retrieval_results.py` / `scripts/make_kv_retrieval_data.py`; QA generation varies the gold index. | Mutable main README; scripts not run or code internals audited. A copied QA description under the KV heading is not used as KV methodology; the paper and actual UUID-format explanation control. |
| [THUDM/LongBench](https://github.com/THUDM/LongBench) | The original paper links this repository. Current root README describes LongBench v2 and separately cites original LongBench. | Original implementation location/ref remains unresolved: raw root/subdirectory README attempts failed. Current `pred.py`/`retrieve.py` directions are for v2 and must not be claimed as original implementation verification. |

## Actual source action ledger

Every numbered action counts once, including reopens and errors. All sources are primary author/publisher/repository representations, except the challenge/error bodies, which supply no substantive evidence. Included sources are represented above; failed routes are unavailable, not excluded studies.

| Actions | Exact source/representation and actual extent | Supports / access result |
|---|---|---|
| 1, 8 | Cached `/workspace/scratch/b99193148918/l2-02-source-cache/ruler-v3.txt`, from [2404.06654v3 PDF](https://arxiv.org/pdf/2404.06654v3): lines 1–250, then 280–430 | Masthead, abstract, §§1/3/4; C1. Existing text extraction inspected; no other case answer used. |
| 2 | [RULER arXiv abstract/history](https://arxiv.org/abs/2404.06654) | Version/status metadata, not new methods |
| 3 | [Lost arXiv abstract/history](https://arxiv.org/abs/2307.03172) | Version/acceptance metadata |
| 4 | [LongBench arXiv abstract/history](https://arxiv.org/abs/2308.14508) | Version/venue metadata |
| 5 | [Lost ACL record](https://aclanthology.org/2024.tacl-1.9/) | Published status, volume/pages/DOI |
| 6 | [LongBench ACL record](https://aclanthology.org/2024.acl-long.172/) | Record resolved; details also corroborated by author repository citation |
| 7 | [RULER OpenReview](https://openreview.net/forum?id=kIoBbc76Sy) | Browser-verification barrier; no forum content inspected |
| 9 | Cached `/workspace/scratch/b99193148918/l2-02-source-cache/ruler-v2.txt`, from [v2 PDF](https://arxiv.org/pdf/2404.06654v2): lines 1–50 and 295–370 in one inspection | Version masthead, population, methods and beginning of Table 3; historical C1 distinction |
| 10 | [Lost published PDF](https://aclanthology.org/2024.tacl-1.9.pdf) | Extracted text, pp. 157–163, including §§2–3 and introductory descriptions of §§4–5; C2. The later sections were not independently re-opened. |
| 11 | [LongBench publisher PDF](https://aclanthology.org/2024.acl-long.172.pdf) | Internal retrieval error; no text |
| 12, 20 | [RULER repository](https://github.com/NVIDIA/RULER), root then scoped README lines 217–332 | Implementation routes and current/original pipeline distinction |
| 13 | [Lost repository](https://github.com/nelson-liu/lost-in-the-middle) | Root identity |
| 14, 22 | [LongBench repository](https://github.com/THUDM/LongBench), root then README lines 180–255 | Current v2 instructions and separate original citation |
| 15, 19, 23 | [LongBench 2308.14508v2 HTML](https://arxiv.org/html/2308.14508v2), initial then lines 66–111 and 115–225 | Original methods, Tables 1–4 and comparison; C3. Material numerical comparison is not reconstructed from images. |
| 16 | [RULER raw README attempt](https://raw.githubusercontent.com/NVIDIA/RULER/main/README.md) | Internal error |
| 17, 21 | [Lost raw main README](https://raw.githubusercontent.com/nelson-liu/lost-in-the-middle/main/README.md), initial then lines 0–140 | Actual data/generation interface descriptions |
| 18 | [LongBench subdirectory raw README attempt](https://raw.githubusercontent.com/THUDM/LongBench/main/LongBench/README.md) | Internal error; no assertion that this path exists |
| 24 | [LongBench raw root README attempt](https://raw.githubusercontent.com/THUDM/LongBench/main/README.md) | Internal error |
| 25 | [Li arXiv record](https://arxiv.org/abs/2407.16833) | Record resolved; not a verified later-version map |
| 26, 27 | [Li 2407.16833v1 HTML](https://arxiv.org/html/2407.16833v1), initial then lines 38–154 | §§3–5 methods, results and countercase; C4. Narrative/table inconsistency preserved; no numeric synthesis. |

The ledger records 27 source actions; four search queries are separately listed in `research.md`. Repeated representations are not additional studies. All source transformations used text extraction/HTML normalization and paraphrase. No replication, source-code test, exhaustive integrity comparison, current leaderboard audit or specialist approval occurred.
