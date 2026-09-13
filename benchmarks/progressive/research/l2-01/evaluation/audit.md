# L2-01 — Fixed-input audit A1

2026-09-13. Primary assistant acting separately from the producer agent, using actual research-evaluate/audit contract0.1. Target: research/l2-01/research.md, fixed producer P1, beginning “Blocked for a complete provider comparison”. Input not edited. All nine audit scopes assessed below; no human expertise or installed integration asserted.

**Review acquisitions.** Producer used14/18sourceactions and4/6queries. Reviewer used remaining2queries (`site:help.openalex.org API works pagination abstract_inverted_index title authorship publication_date`; `site:help.openalex.org authentication API pricing February 2026`), which returned irrelevant results and supplied no evidence. Four final source actions, all2026-09-13:

1. [OpenAlex access index](https://help.openalex.org/access/): official navigation recovered.
2. [Semantic Scholar Graph schema](https://api.semanticscholar.org/graph/v1/swagger.json): ordinary unauthenticated Python urllib GET, HTTP200,123200bytes; APIversion1.0; inspected info, paper lookup/search descriptions and BasePaper/FullPaper fields. Schema documents identifier lookup, selected fields, publicationDate, authors, possible missing abstracts and openAccessPdf with licence/disclaimer. A documentation fetch is not a metadata-workflow execution.
3. [OpenAlex API reference](https://help.openalex.org/api/), overview/response format: explicitly permits introductory keyless access, documents list/singleton distinction, selected fields and page/per_page envelope. Detailed continuation and work-object pages were linked but not acquired.
4. [OpenAlex pricing overview](https://help.openalex.org/access/pricing/), free tier and dated footer: updated2026-08-11, describes a free keyed daily budget and separate paid services. This resolves part of current-policy access, but neither operational enforcement nor full-text rights is established.

The full task ceiling is now6queries/18sourceactions. No additional acquisition or silent extension. Native web, Python3 standard library and local file tools; source-checkout implementation proof only.

| Audit scope | Verdict | Evidence / implication |
|---|---|---|
| Source quality | PASS for obtained provider passages; BLOCKED for uninspected details | P1 distinguishes provider authority from PyAlex/deprecated docs. Current originals recovered above are authoritative only for their actual passages. |
| Source independence | PASS | Provider pages share origins; wrappers not independent policy confirmation. |
| Coverage | BLOCKED for complete provider selection | P1 C2/C3/G1–G3 retain missing field/update/continuation details, especially Crossref/OpenAlex. Budget completion does not resolve these questions. |
| Claims | PASS for qualified direct claims; recommendation remains conditional | P1 does not infer measured latency, current enforcement or full-text permission. R1 is explicitly evidence-availability dependent; it must not become an overall provider ranking. |
| Citations | PASS for traceable support inspected; BLOCKED for open criteria | Locators and inspected passages are identified. A page shell was not cited as schema proof. New schema access does not retroactively support unseen P1 assertions. |
| Freshness | BLOCKED for operational policy conclusions | P1 records dynamic/unpinned limitations. Newly recovered OpenAlex originals narrow its access gap; old wrapper credit claims are not current official enforcement evidence. |
| Contradictions | PASS | Deprecated rate example versus current policy, wrapper qualifications and source-date ambiguity preserved. |
| Uncertainty | PASS | Missing criteria remain unknown; installation and actual service behaviour untested. |
| Reproducibility | BLOCKED for full replay; PASS for bounded access account | Exact query/action log and pinned submission exist, but live sources/wrapper branches are not frozen service responses. |

**Diagnosis and outcome.** This was an actual bounded comparison with incomplete coverage, not evidence that the providers' documentation is universally unavailable. Several reads followed moved paths or returned shells; further schema/navigation acquisition partly repaired access. The smallest next research action would be the still-uninspected official work-field/pagination pages if additional effort is authorised. Preserve P1 and this review. No report-wide PASS, completed integration, or approved provider selection is claimed. The audit operation is complete; affected research conclusions remain BLOCKED. Stage-level acceptance must retain this distinction.
