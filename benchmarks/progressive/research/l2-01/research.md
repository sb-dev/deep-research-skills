# L2-01 — Scholarly metadata routes

Fixed producer submission **P1**, 2026-09-13. **Blocked for a complete provider comparison; ready for a fixed-input audit of this limitations result.** OpenAlex's current policy/schema and Semantic Scholar's endpoint schema were not obtained within the producer allocation. This document does not claim an installed integration, measured latency or observed enforcement. P0 was an unissued plan, read before replacement; no earlier accepted output existed.

Exact task authority: `examples/level-2-scholarly-metadata-routes/README.md`, Exact prompt, repository revision `b9d262b4bd2ffa73d35b520f98629e7eae0b7da7`. Source-checkout execution is authorised; no Extension Pack, installation, paid calls, credentials, provider runs or external communications.

## Brief and criterion-led plan

Compare Crossref, OpenAlex and Semantic Scholar for identifier resolution; title/author/date fields; discovery versus lookup; transparent pagination; abstracts versus full text; publication/update status; access/authentication/restrictions; documented limits; missing data; and reproducibility. Official API documentation has authority over service policy; wrapper documentation/code is evidence of the wrapper's own implementation view.

| Criterion | Evidence sought | Adequate bounded answer |
|---|---|---|
| Discovery / identifier lookup | Official endpoint and identifier documentation | Distinguish search from exact retrieval and identifier absence |
| Metadata and status | Official response schema | Identify title, authors, dates and update/retraction fields without promising completeness |
| Pagination | Official page/cursor contract | Explain continuation and documented result limits |
| Authentication / limits | Current official access documentation | Cite actual documented policy, preserving contradictory wrapper wording and enforcement uncertainty |
| Abstracts / full text | Official field/access descriptions | Separate available metadata, abstract representation, content links and licensed content |
| Missingness / reproducibility | Schema and documented access/response conditions | Preserve null/absent/error distinctions; recommend dated query and response capture as implementation judgment |

Method: targeted official-service discovery followed by original documentation acquisition; inspect relevant wrapper originals as a separate view. Include adverse or conflicting passages. Exclude comparison blogs, search snippets as substantive proof, live API runs, and assumptions from remembered limits. No exhaustive coverage claim.

Total ceiling: 6 discovery queries and 18 source acquisition actions. Producer allocation: at most 4 initial queries and 14 source actions; 4 source actions reserved for the separate evaluator. Retain remaining query capacity for a discriminating gap or evaluator and finalisation time for synthesis. Each URL opened/clicked/refetched, including a failed retrieval, counts once; search queries are tracked separately. Local skill/file reads and drafting are not external source acquisitions. Start: 2026-09-13T07:42:03Z. Stop collection once the comparison can be qualified honestly; unused allowance is not a retrieval target.

## Actual searches and effort

The four queries below were run together on 2026-09-13 using the native web search tool. Each is one query; there was no continuation or exhaustive result screening.

| Query | Exact text | Triage outcome |
|---|---|---|
| Q1 | `site.crossref.org documentation REST API rate limits pagination metadata` | Selected canonical Crossref documentation; retained deprecated repository as contrary/version context |
| Q2 | `site.docs.openalex.org API authentication rate limits works abstract inverted index` | Found migration/current-policy candidates; no search excerpt treated as acquired official policy |
| Q3 | `site.semanticscholar.org product api documentation API key rate limit graph paper fields` | Selected official product and Graph reference; excluded measured-rate commentary and third-party guides |
| Q4 | `pyalex API key optional documentation habanero Semantic Scholar Python API key optional` | Selected PyAlex and semanticscholar wrapper documentation as implementation views; excluded unrelated results |

Acquisition ledger: **14/18 source actions consumed by the producer, 4 reserved for the evaluator; 4/6 queries consumed, 2 remain.** Twelve distinct requested locators; five yielded substantive inspected passages (S1–S5). Repeated attempts, failed retrievals, redirects and shells all count. No further producer acquisition is authorised within this allocation. A local Python attempt failed at an unavailable `bs4` import before networking and consumed no source action; the successful fallback used only standard-library HTML stripping. No packages were installed.

| Action | Requested original locator | Actual access and source identity |
|---|---|---|
| A01 | [Crossref access](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/) | S1: parsed official page, substantive sections inspected |
| A02 | [CrossRef/rest-api-doc](https://github.com/CrossRef/rest-api-doc) | S2: rendered `master` README; explicit deprecation notice; no immutable source commit acquired |
| A03 | [OpenAlex developers](https://developers.openalex.org/) | Redirect to `https://help.openalex.org/`; homepage only |
| A04 | [Semantic Scholar API overview](https://www.semanticscholar.org/product/api) | Native web internal error; no content |
| A05 | [Semantic Scholar Graph reference](https://api.semanticscholar.org/api-docs/graph) | Parsed page only three lines, not endpoint evidence |
| A06 | [Semantic Scholar API overview](https://www.semanticscholar.org/product/api) | S3: direct unauthenticated documentation GET, HTTP 200; HTML text inspected, including API-key section |
| A07 | [OpenAlex help](https://help.openalex.org/) | Direct documentation GET returned HTTP 403; no bypass attempted |
| A08 | [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | S4: official parsed page, API overview/endpoints inspected |
| A09 | [PyAlex](https://github.com/J535D165/pyalex) | S5: rendered `main` README, authentication/abstract/content examples inspected; no commit/version pin acquired |
| A10 | [semanticscholar API endpoints](https://semanticscholar.readthedocs.io/en/stable/api.html) | Wrapper index page obtained, but substantive endpoint passages not exposed in returned excerpt; no endpoint/schema claim extracted |
| A11 | [Legacy OpenAlex authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication) | Followed actual PyAlex link; redirected to help homepage, not policy |
| A12 | [Legacy OpenAlex work object](https://docs.openalex.org/api-entities/works/work-object) | Followed actual PyAlex link; redirected to help homepage, not schema |
| A13 | [Semantic Scholar Graph reference](https://api.semanticscholar.org/api-docs/graph) | Direct documentation GET, HTTP 200; HTML shell inspected. It points to `/graph/v1/swagger.json`; that schema was **not** retrieved |
| A14 | [Candidate OpenAlex authentication path](https://help.openalex.org/access/authentication) | Native tool non-retryable open error; candidate path not verified |

All acquisitions occurred on **2026-09-13**, within the execution interval beginning 07:42:03Z and ending the collection at 07:44:39Z (2m36s). This is documentation-retrieval runtime, not service latency. Final drafting followed collection. Temporary direct-GET HTML was used for local extraction; the durable audit basis is the bounded passages, original locators and access limits below. No provider deep-research run, service API metadata call, payment, credential request or external communication occurred.

## Source and evidence records

Publication/update dates below are the page's displayed dates, not inferred publication times for its current bytes. Retrieved-at is 2026-09-13 for every source. Sources from one provider share an origin and are not independent corroboration. Dynamic pages and branch READMEs were not reconstructed at historical revisions.

| Source | Authority, version and source date | Evidence and precise locator |
|---|---|---|
| S1 | Crossref; primary policy documentation. Live HTML; displayed `Last updated: 2025-October-16`, maintainer Martyn Rittman | **E1**, “Access and authentication” and “Request limits”, parsed lines 111–141: public/polite/Plus options; email identification for polite; rate/concurrency headers; table values public 5/1, polite 10/3, Plus 150/None. Table's rate column itself omits the interval unit. **E2**, “Best practice”, lines 142–147: caching, identification and response handling |
| S2 | Crossref; primary for its deprecated documentation, unsuitable current-policy authority. `master` README; no publication date or commit acquired | **E3**, “DEPRECATION NOTICE”, lines 173–178: documentation deprecated and current API documentation elsewhere. “Rate limits”, lines 287–299: 50 requests/second is explicitly an example interpreting headers, not a measured/current allowance |
| S3 | Ai2 / Semantic Scholar; primary API product documentation. Live HTML; no page publication/update date exposed | **E4**, “Do I need an API Key?”: most endpoints documented as public; shared unauthenticated allowance 1,000 requests/second, additional throttling possible; some endpoints need keys; introductory key allowance 1 request/second. **E5**, “Why use Semantic Scholar API?”: Academic Graph, Recommendations and Datasets are distinct services. Marketing testimonials are not performance evidence |
| S4 | Crossref; primary REST documentation. Live HTML; displayed `Last updated: 2020-April-08`, maintainer Martyn Rittman | **E6**, “REST API”, lines 111–115: member/trusted-source metadata, abstracts and post-publication updates; abstracts may be copyrighted. **E7**, “Endpoints”, lines 125–145: `/works` list, `/works/{doi}` singleton, `/works/{doi}/agency` registration agency. The early example contains an extra `/doi/`; the endpoint table and deprecated overview give the ordinary singleton route. No route was executed |
| S5 | J535D165/PyAlex maintainers; primary for wrapper documentation, secondary for provider policy. `main` README; current commit and publication date unknown | **E8**, “Rate limits and authentication [Changed!]”, lines 224–245: says a key is required starting February 13, 2026, while also documenting a 100-credit/day no-key testing route, 100,000 free-key credits/day, free singletons and 1-credit list requests. These are wrapper assertions, not obtained official current policy. **E9**, “Get abstract” / “Fetch content in PDF and TEI format”, lines 279–330: derived plaintext only when the inverted index is not `None`; content conditional on availability/licensing |

## Claim register and comparison

Each claim is producer-checked for the limited support below; none has independent review yet. Qualified and unresolved states must remain attached to downstream use.

| ID / criterion | Crossref | OpenAlex | Semantic Scholar | Support state |
|---|---|---|---|---|
| C1 Discovery versus identifier lookup | `/works` discovery/list differs from Crossref DOI singleton and agency lookup (E7) | Wrapper demonstrates work ID/DOI lookup and search; official endpoint contract unavailable (S5) | Official overview establishes graph discovery scope; precise lookup identifier contract unavailable (E5) | Crossref supported as documented; others qualified/incomplete |
| C2 Title, author, date and publication/update status | Metadata and post-publication updates documented (E6); exact title/author/date/status schema not acquired | Official fields and update semantics unassessed | Official fields and update semantics unassessed | Mandatory field-level comparison remains open |
| C3 Transparent pagination | Current cursor/page contract not acquired | Wrapper lists pagination support; official continuation contract not acquired | Reference shell cannot establish continuation contract | Unassessed; no route qualifies on this criterion yet |
| C4 Access and limits | Public access without signup and polite identification supported. Table values need interval headers for operational interpretation (E1) | E8 is internally qualified and conflicts with any blanket inference of required authentication with no exception; current official policy unavailable | Public access is endpoint-dependent and shared-throttled; key default is introductory, not guaranteed capacity (E4) | Provider statements supported for Crossref/Semantic Scholar; OpenAlex unresolved |
| C5 Abstracts versus full text | Abstract metadata can be present and copyrighted; this does not establish article full-text access (E6; inference boundary) | Wrapper describes reconstruction and conditional PDF/TEI retrieval (E9); no official access contract verified | No acquired official abstract/full-text field or rights passage | Qualified/incomplete; metadata access cannot be promoted to full-text permission |
| C6 Missing-data handling | Schema-level null/absent conventions not inspected | Wrapper condition `abstract_inverted_index is not None` supports only its abstract conversion behavior (E9) | Schema-level null/absent conventions not inspected | No completeness guarantee supported |
| C7 Reproducibility | Cache/identify/handle responses recommended (E2); live record/version guarantee not verified | Moving documentation links and unpinned wrapper prevent a reproducible policy snapshot | Undated live overview; endpoint schema still missing | Documentation reproducibility is limited for all three |

## Conflicts, gaps and role-specific recommendation

**X1 — rate example versus policy.** E3's 50/second example cannot replace E1's current displayed table or its interval headers. The sources support different propositions. **X2 — wrapper authentication qualification.** E8 juxtaposes a required-key announcement and a no-key testing allowance. Preserve both; neither proves current OpenAlex enforcement. A search excerpt suggesting later pricing changes was a discovery lead only and is not promoted to contrary official evidence. **X3 — source dates.** S4's 2020 update label appears on a live page with later-looking examples; the label does not date every sentence. Historical claims from that label are withheld. **X4 — header/route wording.** S1 lists `Crossref-Plus-API-Token`, while its test example uses `crossref-api-key`; S4's singleton quick example differs from its endpoint table. These documentation inconsistencies were retained and not experimentally resolved.

The mandatory gaps are **G1** current OpenAlex policy and field/pagination originals, **G2** Semantic Scholar schema and applicable content-use restrictions, and **G3** current Crossref schema/pagination. They are attempted/open, not resolved by wrappers or the hard cap. **G4**, actual enforcement under a particular account/request, is unmeasured and out of this documentation-only run; no accepted request parameter or documentation GET can establish it. Independent audit is **G5** and blocks issue.

**Recommendation R1 (conditional producer judgment).** For the implementer of a small DOI-led metadata workflow, Crossref is the best-supported *starting candidate in this obtained evidence* because its exact DOI route and public-access option have primary support (C1/C4). This is not a completed ranking or integration approval: verify C2/C3 before implementing the required workflow. For the literature researcher seeking wider discovery or abstracts, defer selection between OpenAlex and Semantic Scholar until G1/G2 are resolved. For the workflow owner, do not authorise a credentials-dependent or paid route on this incomplete table.

**Recommended handling design, not observed API behavior:** retain requested identifier, returned provider identifier, selected fields, raw response, response date and documented source version; distinguish absent, explicit null, lookup failure, access denial and not-requested fields. Keep publication date, record-update date and retrieval date separate. Preserve pagination tokens and query filters when the official contract is obtained. Do not interpret missing abstract or missing full-text link as proof that the work has no abstract or lawful copy.

## Producer self-check and handoff

Frame, plan, discover, extract-evidence, analyse-evidence and synthesise were applied from the authorised production source checkout. The exact prompt remains the immutable repository locator above. Producer self-check: bounds and primary/wrapper distinctions preserved; incomplete coverage disclosed; no current rate guessed from memory; no measurements or independent review fabricated. **The required complete comparison is blocked by mandatory source access within the remaining allocation.**

Fixed input for the separate evaluator: `research/l2-01/research.md`, revision P1. Expected evaluator-owned output: `research/l2-01/evaluation/audit.md`; it has not been created by the producer. The evaluator has four reserved source actions and two remaining queries; audit findings must not silently edit this submission. Currentness is limited to the documentation actually inspected on 2026-09-13, with displayed source dates as recorded. No historical version or later enforcement claim follows from that retrieval date.
