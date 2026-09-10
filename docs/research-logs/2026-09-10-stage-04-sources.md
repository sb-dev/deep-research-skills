# Stage 4: Source Register

Access date: 10 September 2026. This register identifies the primary material actually used. An opened document means the named sections were inspected, not every navigation link, example or linked standard. Three entries explicitly rely on official search-exposed text after direct access failed. All provider capabilities are documentary claims, not performance measurements.

## Source entries

### S01: Overview of Google search operators
**Publisher:** Google Search Central. **Edition/date:** Updated 10 December 2025.  
**Original:** [Overview of Google search operators](https://developers.google.com/search/docs/monitor-debug/search-operators). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Search-operator definition and indexing/retrieval limitations.
**Evidence used:** site/filetype constraints refine discovery; operator results remain limited by the index and retrieval.
**Limits:** No site-completeness test was run.

### S02: Brave Search API
**Publisher:** Brave. **Edition/date:** Undated page; accessed 10 September 2026.  
**Original:** [Brave Search API](https://brave.com/search/api/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Product and FAQ sections on index, storage and third-party rights.
**Evidence used:** Search access, permission to store API results and rights to retrieved third-party pages are distinct.
**Limits:** Provider description, not a measured search-quality or coverage comparison.

### S03: Rate limiting
**Publisher:** Brave. **Edition/date:** Undated documentation; accessed 10 September 2026.  
**Original:** [Rate limiting](https://api-dashboard.search.brave.com/documentation/guides/rate-limiting). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Quota, response headers and billing guidance.
**Evidence used:** Inspect the applicable account quota and response headers; example headers are not this project’s allowance.
**Limits:** No API key, billing account or live quota was tested.

### S04: REST API
**Publisher:** Crossref. **Edition/date:** Page labels last update 8 April 2020; current text inspected.  
**Original:** [REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Metadata scope, access, endpoints and copyright qualification.
**Evidence used:** Public metadata access does not require sign-up; some included abstracts may remain copyrighted.
**Limits:** Deposited metadata is not full-text inspection or independent methodological appraisal.

### S05: Refining REST API limits for improved stability and reliability
**Publisher:** Crossref / Martyn Rittman. **Edition/date:** 21 July 2026; changes announced effective that day.  
**Original:** [Refining REST API limits for improved stability and reliability](https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Staff announcement, request-type limits and polite-pool handling.
**Evidence used:** Single-record public/polite limits are 5/10 requests per second; list limits are 1/3. Current headers and response status must be checked.
**Limits:** Staff announcement is the rate-policy source; unrelated user replies are not corroboration.

### S06: Authentication
**Publisher:** OpenAlex. **Edition/date:** Updated 19 August 2026.  
**Original:** [Authentication](https://help.openalex.org/api/authentication/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Keyless/key access, rate limits, pagination and usage headers.
**Evidence used:** Basic keyless queries are documented; a free key raises the budget; cursor paging is required beyond the basic paging limit.
**Limits:** Documentation changes older access assumptions; no account or throughput test was performed.

### S07: Pricing Overview
**Publisher:** OpenAlex. **Edition/date:** Updated 11 August 2026.  
**Original:** [Pricing Overview](https://help.openalex.org/access/pricing/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Free allowance, paid service distinction and data licensing.
**Evidence used:** The page separates CC0 metadata from metered delivery services; an account has $1 of API usage per day free, as documented.
**Limits:** Not a claim that every linked full-text work has the metadata’s licence. No purchase or current account entitlement was checked.

### S08: Academic Graph API tutorial
**Publisher:** Semantic Scholar. **Edition/date:** Undated tutorial; current page accessed.  
**Original:** [Academic Graph API tutorial](https://webflow.semanticscholar.org/product/api/tutorial). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Endpoints, API keys, rate guidance, batch/bulk requests and dataset downloads.
**Evidence used:** Graph, recommendation and dataset surfaces differ; authenticated default guidance is 1 request per second; dataset readmes carry usage information.
**Limits:** API documentation, not a recall benchmark or validation of linked papers.

### S09: E-utilities usage guidelines and API key
**Publisher:** NCBI. **Edition/date:** Online reference edition accessed 10 September 2026.  
**Original:** [E-utilities usage guidelines and API key](https://www.ncbi.nlm.nih.gov/sites/books/NBK25497/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Usage guidelines, API-key rates, identification and batch/history guidance.
**Evidence used:** Default limits are 3 requests per second without a key and 10 with a key; batch/history patterns reduce repeated retrieval.
**Limits:** Entrez/PubMed metadata access is not universal full-text access or a clinical-method endorsement.

### S10: Deep research API guide
**Publisher:** OpenAI. **Edition/date:** Current online guide accessed 10 September 2026.  
**Original:** [Deep research API guide](https://developers.openai.com/api/docs/guides/deep-research). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Data sources, citation annotations, operation records and max_tool_calls.
**Evidence used:** The provider documents public web, uploaded sources and connector/MCP retrieval, with output citation annotations and bounded tool calls.
**Limits:** No provider research run. Supported sources, retention and tool contract must be checked for the chosen configuration; this is not a provider selection.

### S11: Gemini Deep Research
**Publisher:** Google. **Edition/date:** Updated 26 August 2026.  
**Original:** [Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Built-in tools, source extension and stated limitations.
**Evidence used:** Provider tools can be constrained or extended using the documented interfaces; current guide lists limitations including structured output and custom function tooling.
**Limits:** No agent execution, measured duration, general multimodal guarantee or account-support claim.

### S12: Authentication
**Publisher:** Microsoft Playwright. **Edition/date:** Current online documentation accessed.  
**Original:** [Authentication](https://playwright.dev/docs/auth). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Contexts, storage state and security warning.
**Evidence used:** Saved browser state can contain sensitive cookies and headers and must not be committed to repositories.
**Limits:** Browser documentation, not successful login or permission to reuse any session.

### S13: EDGAR Application Programming Interfaces
**Publisher:** US SEC. **Edition/date:** Reviewed/updated 8 April 2025.  
**Original:** [EDGAR Application Programming Interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Submissions, XBRL, public access and bulk updates.
**Evidence used:** Public data endpoints do not require API authentication; filings/submission metadata and extracted facts have different interpretation needs.
**Limits:** Not filer-account authentication, investment advice, or independent confirmation of the filed assertions.

### S14: Developer Resources
**Publisher:** US SEC. **Edition/date:** Reviewed/updated 10 March 2025.  
**Original:** [Developer Resources](https://www.sec.gov/about/developer-resources). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Fair access, feeds and historical indexes.
**Evidence used:** EDGAR fair access limits a user to 10 requests per second across machines; feeds and index files provide alternative discovery routes.
**Limits:** A limit is not a throughput promise; no SEC download workload was run.

### S15: Developer guidelines
**Publisher:** Companies House. **Edition/date:** Undated documentation accessed.  
**Original:** [Developer guidelines](https://developer.company-information.service.gov.uk/developer-guidelines/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Request limits and error behaviour.
**Evidence used:** The documented limit is 600 requests in five minutes; a 429 requires respecting the restriction.
**Limits:** No live key or account quota was inspected.

### S16: API authentication
**Publisher:** Companies House. **Edition/date:** Undated documentation accessed.  
**Original:** [API authentication](https://developer.company-information.service.gov.uk/authentication). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Key authentication and distinct OAuth functionality.
**Evidence used:** API/stream-key basic authentication and OAuth-protected functions are separate access mechanisms.
**Limits:** No registration, credentials, authorised company access or write operation was attempted.

### S17: Rate limits for the REST API
**Publisher:** GitHub. **Edition/date:** Current online documentation accessed.  
**Original:** [Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Public/authenticated limits, special buckets and secondary limits.
**Evidence used:** Public unauthenticated guidance is 60 requests per hour; typical authenticated guidance is 5,000, with other classes and secondary limits.
**Limits:** The connected GitHub app may have different limits; generic figures are not its measured allowance.

### S18: Best practices for using the REST API
**Publisher:** GitHub. **Edition/date:** Current online documentation accessed.  
**Original:** [Best practices for using the REST API](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Conditional requests, rate-limit handling and request patterns.
**Evidence used:** Use documented pagination and rate/conditional-request behaviour rather than repeated uncontrolled requests.
**Limits:** No new GitHub client or performance benchmark was implemented.

### S19: Troubleshooting the REST API
**Publisher:** GitHub. **Edition/date:** Current online documentation accessed.  
**Original:** [Troubleshooting the REST API](https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Permission, missing-result and failure diagnosis.
**Evidence used:** Permission failures and unavailable results need diagnosis before treating them as absent public content.
**Limits:** Specific repository contents are established by the connector, not this documentation.

### S20: RFC 4287: The Atom Syndication Format
**Publisher:** IETF / RFC Editor. **Edition/date:** December 2005; identified RFC edition.  
**Original:** [RFC 4287: The Atom Syndication Format](https://www.rfc-editor.org/rfc/rfc4287.html). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Entry identity, updated/published dates, content and links.
**Evidence used:** Atom entry identity, publication and modification meanings are different; content may be external or partial.
**Limits:** An identified format reference, not a claim that every feed implements it or that this is the only relevant later standard.

### S21: RSS 2.0 specification
**Publisher:** RSS Advisory Board. **Edition/date:** Current published specification accessed.  
**Original:** [RSS 2.0 specification](https://www.rssboard.org/rss-specification). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Item identifiers, dates, enclosure and optional TTL.
**Evidence used:** Feed metadata and enclosures need interpretation; a feed item need not contain the complete originating work.
**Limits:** No polling run or feed-completeness measurement.

### S22: Wayback Machine APIs
**Publisher:** Internet Archive. **Edition/date:** Page says updated 24 September 2013.  
**Original:** [Wayback Machine APIs](https://archive.org/help/wayback_api.php). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Availability API, timestamp selection and CDX pointer.
**Evidence used:** Availability selects an available capture; no returned capture can mean no archive or current inaccessibility.
**Limits:** Older official API overview; no live archive query or guarantee of current quotas, complete assets or complete historical coverage.

### S23: What is not online?
**Publisher:** The National Archives. **Edition/date:** Date not established.  
**Original:** [What is not online?](https://www.nationalarchives.gov.uk/help-with-your-research/start-here/whats-not-online/). **Access:** primary-search-excerpt on 2026-09-10.

**Inspected scope:** Official text retrieved through search; direct page open failed.
**Evidence used:** Not all archive records are online; other access/copy routes exist.
**Limits:** SEARCH EXCERPT ONLY. No full-page reading, archive visit, paid copy or unseen record inspection claimed.

### S24: What can I use Discovery for?
**Publisher:** The National Archives. **Edition/date:** Date not established.  
**Original:** [What can I use Discovery for?](https://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/what-can-i-use-discovery-for/). **Access:** primary-search-excerpt on 2026-09-10.

**Inspected scope:** Official text retrieved through search; direct page open failed.
**Evidence used:** Catalogue description search is different from searching words inside the records themselves.
**Limits:** SEARCH EXCERPT ONLY. Claim limited to that explicit access distinction.

### S25: Using the Books API
**Publisher:** Google Books. **Edition/date:** Updated 28 August 2025.  
**Original:** [Using the Books API](https://developers.google.com/books/docs/v1/using). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Volume identifiers, authorization, pagination, accessInfo and visibility filters.
**Evidence used:** Book discovery and content access differ; API keys/OAuth and territory/access fields constrain the route.
**Limits:** No user library or book download was accessed.

### S26: Text extraction recipes
**Publisher:** Artifex / PyMuPDF. **Edition/date:** Current online documentation accessed.  
**Original:** [Text extraction recipes](https://pymupdf.readthedocs.io/en/latest/recipes-text.html). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Plain-text ordering, block/word locators and table discussion.
**Evidence used:** Extracted text may not follow reading order; coordinate/context-aware inspection can be necessary.
**Limits:** No PDF parsed in this stage and no vendor speed/accuracy benchmark adopted.

### S27: OCR recipes
**Publisher:** Artifex / PyMuPDF. **Edition/date:** Current online documentation accessed.  
**Original:** [OCR recipes](https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Optional OCR and reuse of recognised text.
**Evidence used:** OCR is an additional operation rather than an assumption that scanned files already contain reliable text.
**Limits:** No OCR was executed; resulting fidelity depends on the actual source and check.

### S28: License and Copyright
**Publisher:** Artifex / PyMuPDF. **Edition/date:** Page updated 3 September 2026; documentation identifies version 1.28.2.  
**Original:** [License and Copyright](https://pymupdf.readthedocs.io/en/latest/about.html). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** License section only used as evidence.
**Evidence used:** The project documents AGPL and commercial licensing alternatives; tool licensing needs explicit review.
**Limits:** No legal clearance, package selection or redistribution approval is inferred.

### S29: Microsoft Search API overview
**Publisher:** Microsoft. **Edition/date:** Current online documentation accessed.  
**Original:** [Microsoft Search API overview](https://learn.microsoft.com/en-us/graph/search-concept-overview). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Indexed cloud entities and connector-provided external content.
**Evidence used:** Search operates over supported indexed Microsoft cloud and connected content, not an assumed complete organisational corpus.
**Limits:** No Microsoft account, tenant permissions or private content was queried.

### S30: Search OneDrive and SharePoint content with Microsoft Search API
**Publisher:** Microsoft. **Edition/date:** Current online documentation accessed.  
**Original:** [Search OneDrive and SharePoint content with Microsoft Search API](https://learn.microsoft.com/en-us/graph/search-concept-files). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** File/drive/list search examples and scope.
**Evidence used:** File-search routes have entity/query scope; index discovery must be followed by authorised item retrieval.
**Limits:** No tenant-specific completeness, ACL correctness or runtime behaviour was measured.

### S31: MCP 2026-07-28 release
**Publisher:** Model Context Protocol maintainers. **Edition/date:** 28 July 2026.  
**Original:** [MCP 2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Release identity and version boundary.
**Evidence used:** The current published release identified in this inquiry is 2026-07-28, not the older 2025-11-25 text initially surfaced.
**Limits:** Publication does not establish deployment support in any particular client.

### S32: Resources, specification 2026-07-28
**Publisher:** Model Context Protocol maintainers. **Edition/date:** Version 2026-07-28.  
**Original:** [Resources, specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/resources). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Resource identifiers, listing and read interface.
**Evidence used:** Resources are an explicit capability surface; listing or reading them is not automatically a complete search of an application.
**Limits:** No generic MCP runtime was implemented or conformance tested.

### S33: Tools, specification 2026-07-28
**Publisher:** Model Context Protocol maintainers. **Edition/date:** Version 2026-07-28.  
**Original:** [Tools, specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Tool contracts, discovery and invocation semantics.
**Evidence used:** Tool discovery exposes declared contracts; a client must respect the specific tool and resulting content constraints.
**Limits:** Not all hosts implement this revision or every tool capability.

### S34: Authorization, specification 2026-07-28
**Publisher:** Model Context Protocol maintainers. **Edition/date:** Version 2026-07-28.  
**Original:** [Authorization, specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Authorization scope and transport-specific requirements.
**Evidence used:** Protocol authorization is distinct from task permission; transport and endpoint audience constrain credential use.
**Limits:** No account authorization was performed; this design retains explicit user/source-owner authority.

### S35: API throttles
**Publisher:** Stack Exchange. **Edition/date:** Current online documentation accessed.  
**Original:** [API throttles](https://api.stackexchange.com/docs/throttle). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Quota, caching and dynamic backoff.
**Evidence used:** Backoff can be returned dynamically for methods; client behaviour must respect it and the actual quota.
**Limits:** One community-platform exemplar, not a representative-population or content-quality claim.

### S36: GNU grep manual
**Publisher:** GNU. **Edition/date:** Search text identified manual 3.12.  
**Original:** [GNU grep manual](https://www.gnu.org/s/grep/manual/grep.html). **Access:** primary-search-excerpt on 2026-09-10.

**Inspected scope:** Official search-exposed text on recursive scope, binary/text and locale behaviour.
**Evidence used:** Exact local text matching is scoped by files/options/encoding; binary handling can affect matches.
**Limits:** SEARCH EXCERPT ONLY: direct full manual access failed. No installed grep version or benchmark checked.

### S37: csv: CSV File Reading and Writing
**Publisher:** Python Software Foundation. **Edition/date:** Online Python 3.14 documentation accessed.  
**Original:** [csv: CSV File Reading and Writing](https://docs.python.org/3/library/csv.html). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Dialects, newline handling, reader values and conversion behaviour.
**Evidence used:** Parsing settings and explicit value interpretation matter before calculations can be reproduced.
**Limits:** Not a statistical-method validation, production-code selection or new data-analysis experiment.

### S38: About the Indicators API Documentation
**Publisher:** World Bank. **Edition/date:** Current online overview accessed.  
**Original:** [About the Indicators API Documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Indicators API overview and documented navigation.
**Evidence used:** A specialist indicator service is a distinct acquisition route from a search-result summary.
**Limits:** Only overview inspected; no numeric quota, authentication mode or dataset completeness inferred here.

### S39: Summary Terms of Use
**Publisher:** World Bank. **Edition/date:** Current online terms accessed.  
**Original:** [Summary Terms of Use](https://data.worldbank.org/summary-terms-of-use). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Default data terms and indicator-specific qualifications.
**Evidence used:** CC BY 4.0 is a default subject to dataset/indicator-specific terms; metadata must be checked.
**Limits:** No general legal advice or blanket clearance for every linked item.

### S40: C2PA and Content Credentials Explainer
**Publisher:** C2PA. **Edition/date:** Explicit version 2.2; not claimed latest.  
**Original:** [C2PA and Content Credentials Explainer](https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Core provenance concepts and §7.2.2.
**Evidence used:** Provenance can expose history/integrity but cannot alone establish that represented content is true.
**Limits:** Conceptual reference, not signature verification of an actual media asset.

### S41: Get Started / access levels
**Publisher:** Guardian Open Platform. **Edition/date:** Undated page; live opened 10 September 2026.  
**Original:** [Get Started / access levels](https://open-platform.theguardian.com/access/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Developer/commercial access distinction and quotas.
**Evidence used:** Developer access is non-commercial and documented at 1 call per second/500 per day; commercial uses require the appropriate arrangement.
**Limits:** No key obtained, commercial eligibility decided or content retrieved. Third-party wrapper quotas were not accepted.

### S42: Documentation overview
**Publisher:** Guardian Open Platform. **Edition/date:** Undated overview accessed.  
**Original:** [Documentation overview](https://open-platform.theguardian.com/documentation/). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Official overview and documentation entry points.
**Evidence used:** A publisher-native content API can be selected when that publisher’s corpus matches the question.
**Limits:** Overview only; no unsupported endpoint or coverage guarantee taken from it.

### S43: Register RSS/Atom Feeds
**Publisher:** The Register. **Edition/date:** Undated page; accessed 10 September 2026.  
**Original:** [Register RSS/Atom Feeds](https://www.theregister.com/design/page/feeds). **Access:** opened-selected-sections on 2026-09-10.

**Inspected scope:** Publisher feed directory and topic categories.
**Evidence used:** The technology trade publisher exposes a general feed and topic-specific feed routes.
**Limits:** Directory inspection only, not a feed polling run or permission to republish full articles.

## Discovery and source conflicts

The inquiry followed the thirteen paths named in bootstrap §10. General and site-restricted discovery led to official service, format and security documentation. Further reads filled gaps for news content, company authentication, metadata rights, current scholarly limits and multimodal provenance. Provider examples were investigated to understand a path, not to select the Stage 7 tool shortlist.

Currentness was checked at the level of the specific claim, not the newest date anywhere on a page. Crossref’s REST overview still shows an older maintenance label; the July 2026 staff announcement governs the cited rate change. OpenAlex’s August 2026 help pages were used instead of older surfaced guides that conflicted about keyless access and quotas. MCP was checked against the published 2026-07-28 release and matching specification URLs; compatibility with a deployed client is still unknown until checked. C2PA 2.2 is deliberately an identified conceptual reference, not a latest-version claim. [S04–S07, S31–S34, S40.]

The Guardian query `site.open-platform.theguardian.com access developer key non commercial content API terms` surfaced wrapper and directory entries with higher quotas than the publisher’s access page. Only the publisher’s page was used for the operating constraint. Its separately surfaced general terms page was not used as a full contract review. [S41–S42.]

Direct attempts to read the National Archives pages and GNU grep manual failed; their official search text supports only the narrow distinctions recorded in S23, S24 and S36. Bluesky rate documentation and DuckDB documentation returned unusable/empty redirect content in this environment and were not adopted as evidence. Community-source access is instead grounded in the inspected Stack Exchange API guidance; local parsing/analysis is grounded in GNU’s bounded excerpt and opened Python documentation. No values were reconstructed from memory to fill those failed pages.

Search-result snippets from third-party aggregators, AI-tool directories, Wikipedia and user comments were not accepted as primary operating authority. A provider’s own capability statement was not promoted to an independent benchmark. A mirror, revised page or several chapters from one institution were not counted as independent corroboration.

No paid service, API account, private tenant, source purchase, browser login, PDF OCR, model research run, feed subscription or archive visit was executed for Stage 4. Existing GitHub connector reads establish this repository’s inspected content only. The container’s GitHub DNS failure is recorded in the stage log; it is not evidence that the public GitHub API or other services are generally unavailable.
