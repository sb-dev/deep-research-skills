# Stage 4: Retrieval-Path Comparison

The comparison covers all thirteen acquisition paths and all twelve dimensions required by bootstrap §10. **E** labels documented capability; **A** labels project analysis or a proposed operating rule. Combined labels separate the small documented premise from its design consequence. None is a measured precision, latency, cost or reliability comparison. Sources are identified in the [source register](2026-09-10-stage-04-sources.md).

Paths are composable rather than exclusive. A provider agent can call a search API; a connector can expose GitHub retrieval; a browser can download a PDF that needs parsing. Retain the underlying source and operation rather than counting wrappers as independent evidence. This is an acquisition model, not a provider shortlist or runtime design.

## A01: Search engine

Primary evidence basis: S01, S02, S03. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E: Retrieves from the service’s accessible index; it is not a census of the web or private repositories. S01–S02 define this access boundary. |
| D02 Precision | A: Query terms, dates and operators can focus leads. Ranking and a matching snippet do not establish relevance to the exact claim or source independence. |
| D03 Cost | E/A: An API may meter requests and storage by plan; read the actual allowance before collection. Include subsequent original-source retrieval, not only search-call cost. [S02–S03.] |
| D04 Latency | A: One search can be cheaper than a research-agent run, but total latency includes pagination and source inspection. No response-time measurement was made. |
| D05 Rate limits | E: Use the selected service’s quota/reset headers and throttling guidance. An example quota or another provider’s limit is not transferable. [S03.] |
| D06 Authentication | A: An interactive public search and an authenticated API are different access modes. Use only the configured authorised mode; do not acquire a paid account by implication. |
| D07 Licence / terms | E: Brave explicitly distinguishes API-result storage rights from rights to the linked third-party content. Assess both before caching or republication. [S02.] |
| D08 Reproducibility | A: Retain exact query, filters, search time, returned source locators and consequential exclusions. Repeating a query need not reproduce the same index or ranking. |
| D09 Data quality | A: Treat titles/snippets as discovery material, preserve their origin, then inspect the actual supporting passage. Several hits can reproduce one underlying source. |
| D10 Freshness | A: Index discovery may lag or surface old pages. Read the source’s publication/effective/version context rather than equating recent retrieval with current evidence. |
| D11 Multimodal support | A: An engine may expose image/video results or metadata; this does not verify the represented content. Retrieve the authorised original and inspect the relevant region or time interval. |
| D12 Failure modes | A: Empty or repetitive results, misleading snippets, wrong entity/version and index gaps require targeted reformulation or a different source path, not a universal absence claim. |

## A02: Site-restricted search

Primary evidence basis: S01. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E: A domain, URL or prefix constraint limits indexed discovery, not all documents that the site holds. Missing indexed results do not establish missing records. [S01.] |
| D02 Precision | A: Useful when the responsible publisher is known. Check host, path, edition and applicability; a restrictive query can exclude relevant renamed or differently hosted material. |
| D03 Cost | A: Uses the underlying search route’s costs; it can reduce irrelevant retrieval but does not confer free access to the resulting material. No cost saving was measured. |
| D04 Latency | A: Fewer irrelevant results may reduce review work; latency still depends on the search service and follow-up. Do not attach a guaranteed speed advantage. |
| D05 Rate limits | A: Inherits the search service’s limits and the destination site’s retrieval limits; the site operator is not an independent rate-limit exemption. |
| D06 Authentication | A: Search authentication follows its service. Opening a hit may require separate source authorization; an indexed private-looking title is not authority to access or disclose it. |
| D07 Licence / terms | A: Search access does not override the destination’s terms, copyright or privacy boundary. Use a permitted locator and approved content access. |
| D08 Reproducibility | A: Record the exact domain/prefix, query, filters and timestamp. Preserve which authoritative host was intended so a later repair can diagnose an overly narrow scope. |
| D09 Data quality | A: Official-domain results still need claim-relative appraisal. Navigation pages, obsolete copies and extracted snippets must not be treated as current normative text. |
| D10 Freshness | E/A: The index is a distinct access layer; verify the publisher’s current edition or update history after discovery. Operator coverage is explicitly limited. [S01.] |
| D11 Multimodal support | A: filetype/image-related operators can identify candidate material, but acquisition and inspection of its actual format remain separate operations. |
| D12 Failure modes | A: Zero hits may reflect indexing, query wording or moved content. Try the publisher’s native catalogue/navigation or direct known identifier before broadening to unrelated reporting. |

## A03: Provider deep-research agent

Primary evidence basis: S10, S11. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E: Providers document combinations of public search, supplied/uploaded sources and compatible connectors. Coverage is configuration-specific, not all of a provider’s possible sources. [S10–S11.] |
| D02 Precision | A: A precise brief and allowed-source scope constrain discovery; multi-step retrieval can still miss the decisive source or drift to an adjacent question. Audit against the brief. |
| D03 Cost | E/A: Account/model/tool usage and possibly storage contribute to cost. Documented call bounds can limit work; paid expansion requires authority, not an assumed unlimited run. [S10.] |
| D04 Latency | A: Planning, retrieval and synthesis add dependent operations. Provider-reported limits are not measured completion times; inspect progress/results and use a bounded execution contract. |
| D05 Rate limits | A: Check both the provider project/model allowance and downstream tool quotas. Parallel agents must not be used to circumvent either constraint. |
| D06 Authentication | E/A: Provider credentials and separate source permissions are required as applicable. A configured read interface cannot grant access to a new private corpus. [S10–S11.] |
| D07 Licence / terms | A: Validate retention, disclosure and source-use terms for the chosen mode. A provider configuration requiring preapproval does not waive the researcher’s permission checks. |
| D08 Reproducibility | E/A: Retain prompt, source restrictions, engine/configuration, run identifiers and returned source/call records where exposed. Citation annotations help locate support but are not semantic verification. [S10.] |
| D09 Data quality | A: A generated report is synthesis to audit, not primary evidence. Resolve provider citation tokens to inspected sources; label hidden or inaccessible evidence honestly. |
| D10 Freshness | A: A new run can still use stale indexed or cached material. Require the same publication/effective/retrieval distinctions as other routes. |
| D11 Multimodal support | E/A: Check the chosen engine’s supported input/source types. Tool names or uploaded-file support do not imply full image/video understanding or unrestricted custom tools. [S11.] |
| D12 Failure modes | A: Missing original sources, opaque coverage, scope drift, truncated output and tool failure require bounded follow-up on affected claims. Do not rerun the entire investigation by default. |

## A04: Browser / browser automation

Primary evidence basis: S12, S26. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | A: Appropriate for permitted material whose rendered page, interaction or download is not adequately exposed through a direct/native route. Only accessible states are covered. |
| D02 Precision | A: Inspect the exact page, selected version, filter state and visible context. A successful click or DOM match is not proof that the correct evidence was captured. |
| D03 Cost | A: Browser actions, rendering, downloads and review consume resources; remote browsers may add service fees. Use only when simpler authorised retrieval cannot answer the question. |
| D04 Latency | A: Navigation, waits, dynamic content and interaction can dominate time. No timing benchmark was run; record actual timeout/failure rather than assuming an instantaneous page. |
| D05 Rate limits | A: Respect the destination’s limits and access policy. Automating a browser is not permission for unrestricted concurrency or evasion of bot/access controls. |
| D06 Authentication | E: Playwright documents isolated contexts and reusable authentication state; stored cookies/headers are sensitive. Never commit reusable session state or treat it as a public artefact. [S12.] |
| D07 Licence / terms | A: Tool-code licensing and website access/content terms are separate. Neither browser automation nor a saved session authorises a new disclosure or bypass. |
| D08 Reproducibility | A: Retain URL, acquisition time, relevant navigation/filter state, selected document version and precise supporting region. Preserve traces only where permitted and scrub credentials. |
| D09 Data quality | E/A: Rendered layout can resolve extraction ambiguity, but downloads can still lose reading order or context in parsing. Inspect the supporting representation rather than trusting a flattened extraction. [S26.] |
| D10 Freshness | A: A current session can show cached, locale-specific or outdated content. Preserve the actual displayed state and distinguish it from a claimed global current state. |
| D11 Multimodal support | A: Rendering enables inspection of page regions and downloadable media; authentication of the depicted event, transcription and media provenance remain separate checks. |
| D12 Failure modes | A: Expired sessions, changed selectors, blocked pages, incomplete loads and unintended navigation need diagnosis. Return to authorised direct/native retrieval or state the access gap; do not bypass restrictions. |

## A05: Specialist API

Primary evidence basis: S13, S14, S15, S16, S38, S39, S41, S42. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E: Examples include filings/submissions, company records, economic indicators and a publisher’s own content. Their corpora and units differ; no one specialist API covers the entire research question. [S13, S38, S42.] |
| D02 Precision | A: Stable identifiers and field filters can target a defined entity, filing, indicator or period. Check aliases, definitions, pagination and amendments rather than trusting a familiar name. |
| D03 Cost | A: Public data access can avoid per-query fees, but licensing, commercial tiers, storage, acquisition and review still cost. Check the specific service and use case before collection. |
| D04 Latency | A: Structured retrieval may avoid browser interaction; bulk jobs and complex requests add delay. No common latency figure applies across the compared services. |
| D05 Rate limits | E: SEC documents 10 requests per second across machines; Companies House documents 600 per five minutes. Those are separate policies, not interchangeable generic defaults. [S14–S15.] |
| D06 Authentication | E: SEC’s public data API needs no API key; Companies House documents key authentication and separate OAuth functionality. Do not confuse public retrieval with filing/write authority. [S13, S16.] |
| D07 Licence / terms | E/A: World Bank’s default data terms have dataset exceptions. Guardian separates non-commercial developer access from commercial arrangements. Check both endpoint and underlying content rights. [S39, S41.] |
| D08 Reproducibility | A: Retain service/version, endpoint, parameters, entity IDs, pagination, response date, data edition and relevant raw fields or authorised snapshot. Exclude credentials from logs. |
| D09 Data quality | A: Structured fields do not remove filing errors, definition mismatches, missing values or reporting-period differences. Follow the relevant original record and methodology for material claims. |
| D10 Freshness | E/A: SEC documents distinct live-data and bulk-update routes. Preserve retrieval time and underlying reporting/effective period rather than treating every response as a new observation. [S13.] |
| D11 Multimodal support | A: Some specialist services expose document/media links or commercial media access; others return only text/numbers. Verify the actual response and permitted media retrieval. |
| D12 Failure modes | A: Wrong identifiers, incomplete pages, changed schemas, amended records, suppressed fields and quotas require service-specific diagnosis. General search is a discovery fallback, not an equivalent structured dataset. |

## A06: GitHub API

Primary evidence basis: S17, S18, S19. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | A: Covers repositories and supported metadata/content endpoints within the connected identity’s permissions. A repository tree, code search, issues and releases are distinct surfaces. |
| D02 Precision | A: Known repository/path/commit retrieval is precise for that object. Search queries can have limits; a branch label is mutable and should not stand in for a verified revision. |
| D03 Cost | A: Repository reads may fit an existing allowance; client work, large responses, private storage and downstream code review still consume resources. No new client or paid plan was selected. |
| D04 Latency | A: One known-path fetch differs from recursive discovery and paginated history. Request shape and returned size matter; current connector operation times are not a general API benchmark. |
| D05 Rate limits | E: GitHub separates primary, search and secondary limits. Typical 60/hour unauthenticated and 5,000/hour authenticated figures do not establish this app’s allowance. Inspect actual limits. [S17.] |
| D06 Authentication | A: Use the configured app/token scope and exact endpoint contract. A 404 may need permission diagnosis; do not expose private identifiers to a public search route. [S19.] |
| D07 Licence / terms | A: Read the relevant licence at the cited revision and distinguish code, documentation and bundled assets. Public visibility, stars and a repository licence label do not prove rights to every asset. |
| D08 Reproducibility | A: Preserve repository, immutable commit, exact path/lines or issue/release identifiers, pagination and retrieval time. Pin the revision used for the claim; retain later corrections separately. |
| D09 Data quality | A: README promises, issue reports and actual code/execution results are different evidence. A maintenance signal or popularity count alone cannot prove fitness or correctness. |
| D10 Freshness | A: Verify the requested branch/release state at acquisition, then cite its resolved revision. Release publication, commit date and effective behaviour need separate interpretation. |
| D11 Multimodal support | A: Trees may identify binary assets without providing an inspectable representation through the chosen connector. Retrieve permitted bytes through a compatible path when needed; do not invent binary contents. |
| D12 Failure modes | E/A: Handle incomplete responses, timeouts, permissions and throttling using documented diagnostics and bounded retries. Conditional requests can reduce repeated work when supported. [S18–S19.] |

## A07: Scholarly APIs: Crossref / OpenAlex / Semantic Scholar / PubMed-like

Primary evidence basis: S04, S05, S06, S07, S08, S09. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E: DOI deposits, scholarly entity graphs and biomedical records have different coverage and access depth. Use the service-specific comparison below; discovery records are not an exhaustive full-text corpus. [S04, S08–S09.] |
| D02 Precision | A: Exact identifiers and structured subject/field filters improve targeting, but entity resolution, study/report linkage and eligibility still need review. Duplicate records are not multiple studies. |
| D03 Cost | E/A: OpenAlex distinguishes free metadata from metered services; other named services document public/free access routes with limits. Include full-text acquisition and specialist screening costs. [S04, S07–S09.] |
| D04 Latency | A: Metadata batches, cursor pages and full-text retrieval have different workloads. No cross-service latency measurements were made; use smaller evidence needs before corpus-scale downloads. |
| D05 Rate limits | E: Crossref now separates single/list request limits; OpenAlex budgets and burst limits differ; Semantic Scholar and NCBI have their own key/rate rules. Recheck headers and endpoint guidance. [S05–S06, S08–S09.] |
| D06 Authentication | E: Crossref public access does not require signup; OpenAlex now documents keyless basics and optional keys; Semantic Scholar and NCBI key policies differ by access. [S04, S06, S08–S09.] |
| D07 Licence / terms | E/A: Metadata, abstracts, original papers and bulk datasets can have different licences. Open metadata does not establish reuse rights for all linked full text or media. [S04, S07–S08.] |
| D08 Reproducibility | A: Retain query syntax/filters, service, date, pagination/cursor, identifiers, selected fields, exclusion reasons and any dataset release. Record which source versions were actually inspected. |
| D09 Data quality | A: Metadata can be incomplete or inconsistent. Inspect methods/results in accessible originals for material empirical claims; check correction/retraction information without equating missing flags with no problem. |
| D10 Freshness | A: Index/deposit updates, preprints, versions and post-publication changes need separate dates. A freshly retrieved record may still describe an old or corrected report. |
| D11 Multimodal support | A: Linked figures, supplementary files and full-text locations are not themselves inspected multimodal evidence. Acquire the authorised representation and preserve passage/page/data locators. |
| D12 Failure modes | A: Metadata/full-text confusion, merged authors, duplicate study reports, quota exhaustion and incomplete paging need targeted repair. Preserve inaccessible originals as gaps or attributed secondary leads. |

## A08: RSS / feeds

Primary evidence basis: S20, S21, S14, S43. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E/A: Feeds expose what a publisher chooses to syndicate, often a changing window rather than all history. SEC’s indexes and The Register’s topic feeds provide distinct discovery scopes. [S14, S20–S21, S43.] |
| D02 Precision | A: Subscribe to a relevant source/query and inspect item identity, tags and original link. A publisher feed reduces search noise but cannot establish independent corroboration. |
| D03 Cost | A: Polling, conditional retrieval, storage and downstream inspection have costs even where the feed is public. Service terms may differ from linked article terms. |
| D04 Latency | A: Detection depends on publication, feed refresh and permitted polling. Neither a feed timestamp nor a short polling interval proves immediate discovery. |
| D05 Rate limits | E/A: Optional format hints such as RSS TTL do not replace host policy. Respect host limits, cache behaviour and failure responses; there is no universal feed quota. [S21.] |
| D06 Authentication | A: Public feeds may need no login; private feeds can contain credentials or tokenised URLs. Treat those locators as secrets and do not publish them. |
| D07 Licence / terms | A: Syndication does not imply unlimited retention or republication. Inspect content-specific rights and preserve a link/limited evidence when full copying is not authorised. |
| D08 Reproducibility | E/A: Preserve item identity, original URL, retrieval time and meaningful updates. Atom updated/published semantics differ; a changed item should not silently replace its earlier evidence. [S20.] |
| D09 Data quality | A: Summaries, truncated bodies, duplicate syndicated reports and unsupported headlines require original-source inspection. An enclosure is a pointer, not a completed media analysis. |
| D10 Freshness | A: Distinguish feed update, article publication and underlying event/effective date. Missing an item in the current window is not evidence that it was never published. |
| D11 Multimodal support | E/A: RSS enclosures and Atom content/links can identify media; actual bytes, format support and rights must be checked separately. [S20–S21.] |
| D12 Failure modes | A: Broken feeds, moved endpoints, repeated GUIDs or truncated windows require recorded source-level repair and an archive/native-index route where authorised, not silent claims of full history. |

## A09: Archive services

Primary evidence basis: S22, S23, S24. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E: Wayback availability is about accessible captures; National Archives catalogue discovery is not full-record text search. Surviving/digitised holdings and captured URLs set different boundaries. [S22–S24.] |
| D02 Precision | A: Exact URL, capture time, collection and record reference can locate a useful item. Closest capture is not necessarily the required date or a complete representation. |
| D03 Cost | A: Public discovery may be low-cost; copies, specialist access or visits can require expense. Do not order material or commit to access costs without authority. |
| D04 Latency | A: A metadata lookup differs from acquiring an offline record or large archived object. No delivery, visit or retrieval timing was measured. |
| D05 Rate limits | A: The inspected archive overview does not establish a universal current rate quota. Check the selected service’s current guidance/response and stop rather than assume unlimited requests. |
| D06 Authentication | A: Public snapshots/catalogues and restricted collections have different access requirements. Missing access is not permission to evade restrictions or use another person’s credentials. |
| D07 Licence / terms | A: Archival availability does not remove rights, personal-data restrictions or permitted-use conditions. Preserve only what the authorised audience may access and retain. |
| D08 Reproducibility | A: Retain original URL/reference, archive service, exact capture/edition, acquisition date and inspected extent. Keep catalogue metadata separate from the acquired underlying record. |
| D09 Data quality | A: Missing assets, incomplete captures, catalogue descriptions and preservation transformations may limit inference. Distinguish what the archive shows from what the original event establishes. |
| D10 Freshness | A: Capture, original publication and event date are different. A historical snapshot can support a historical claim, not automatically a current one. |
| D11 Multimodal support | A: Some captures or holdings contain media, while others provide metadata only. Check relevant files/assets, frames, pages and time intervals rather than assuming complete replay. |
| D12 Failure modes | E/A: No capture can mean absent or inaccessible archive data. Seek a different authorised capture/holding or report the bounded gap; do not infer that the original never existed. [S22.] |

## A10: Direct document retrieval

Primary evidence basis: S25, S26, S27, S28. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | A: Best for an already identified authorised page, report, book edition, dataset file or document. It retrieves that representation, not every relevant source in the domain. |
| D02 Precision | A: Match exact identifier, edition, URL and required support location. Verify that redirects/downloads actually return the intended document rather than a login page or abstract. |
| D03 Cost | A: Transfer, storage, parsing, OCR and source access are separate costs. Read available text first; escalate extraction only where the needed evidence cannot otherwise be inspected. |
| D04 Latency | A: Document size, transfer, parser and selective page/section access drive work. No parser/throughput benchmark was run; do not adopt vendor comparative timings as project measurements. |
| D05 Rate limits | A: Respect the source host’s limits and any document-service quota. Local parsing has resource limits even when it does not call an API. |
| D06 Authentication | E/A: Public, purchased, preview and private documents have different authorization; Google Books exposes access distinctions rather than universal full-text permission. [S25.] |
| D07 Licence / terms | E/A: Separate document rights from parser licensing. PyMuPDF’s AGPL/commercial alternatives demonstrate why an available tool is not automatically approved for redistribution. [S28.] |
| D08 Reproducibility | A: Preserve version/edition, retrieval time, relevant source hash where useful, page-numbering convention and extraction transformation. Retain permitted originals or precise access references. |
| D09 Data quality | E: Plain PDF text can lose reading order; optional OCR is an additional transformation needing checks. Preserve tables, units, captions and visually essential context. [S26–S27.] |
| D10 Freshness | A: A file downloaded today can be an obsolete edition. Check source publication/update/effective context and do not fabricate a document date from its path or file metadata. |
| D11 Multimodal support | A: Pages may contain images, scans, diagrams or media links. Inspect the supporting page/region when text is incomplete; extracted prose does not authenticate unseen visuals. |
| D12 Failure modes | A: Wrong content type, encrypted/scanned material, garbled text, missing tables or blocked downloads require a compatible permitted representation or an explicit access/extraction gap. |

## A11: MCP / connector

Primary evidence basis: S29, S30, S31, S32, S33, S34, S10. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | E/A: Covers the server/connector’s declared resources and tools within application/index scope. Microsoft Search and MCP resource listing are not universal complete searches. [S29–S33.] |
| D02 Precision | A: Prefer native known-item retrieval or scope-aware search when the question concerns that application. Respect exact parameter contracts and follow returned identifiers rather than guessing URLs. |
| D03 Cost | A: Protocol availability does not imply a free service. Hosting, provider calls, indexing, seats, storage and underlying API charges depend on the actual deployment. |
| D04 Latency | A: Latency includes connector, application/index and underlying service work. No cross-connector timing was measured; retain failures and incomplete results as observable limits. |
| D05 Rate limits | A: Both connector/server and underlying application quotas can apply. Pagination and Retry-After handling remain part of acquisition, not hidden implementation details. |
| D06 Authentication | E/A: Current MCP authorization distinguishes protocol/transport concerns; application scope and task permission still apply. Client support for the published revision must be checked. [S31, S34.] |
| D07 Licence / terms | A: Approval must cover reading, processing destination and disclosure. A provider-specific preapproval mode is not authority to remove consent or send private data elsewhere. |
| D08 Reproducibility | A: Retain connector/tool identity, supported protocol/contract version, permitted scope, item IDs, versions, query, access time and meaningful continuations. Never persist tokens or reusable session state. |
| D09 Data quality | A: Search indexes, connector summaries and original records have different access depth. Fetch the relevant original range and preserve source metadata; tool output remains untrusted evidence. |
| D10 Freshness | A: Index sync time and application modification time can differ. A current query does not prove all newly changed documents were indexed; verify material known items directly. |
| D11 Multimodal support | E/A: Resources/tools may expose text or other media types, but a specific provider interface can be narrower. Verify both the connector and consuming engine’s actual support. [S10, S32–S33.] |
| D12 Failure modes | A: Permission expiry, unsupported URL form, partial lists and protocol mismatch require native diagnosis. Do not search the public web with confidential content or claim an unresolved folder is empty. |

## A12: Local file search

Primary evidence basis: S36, S26, S27, S37. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | A: Covers the authorised files/roots actually present or indexed. Exact text search, metadata discovery and a semantic index are distinct; no vector database is required by this path. |
| D02 Precision | E/A: Literal/regex matches depend on file scope, encoding and options; binary/text handling changes results. Examine the surrounding source instead of interpreting a matching token alone. [S36.] |
| D03 Cost | A: Local CPU, indexing, storage and extraction consume resources without necessarily incurring API fees. Cloud-assisted search adds a separate disclosure and service-cost boundary. |
| D04 Latency | A: File volume, format and existing indexes affect work. Search known filenames/phrases or relevant sections first; no local search speed benchmark was run. |
| D05 Rate limits | A: Pure filesystem matching has no remote provider quota, but resource ceilings apply. Network mounts, cloud indexes and materialisation can add upstream limits. |
| D06 Authentication | A: Use filesystem permissions and authorised source roots; a connector reference is not an already-mounted file. Access to one folder is not authority to scan all project data. |
| D07 Licence / terms | A: Local possession does not establish rights to publish or upload contents. Tool licences, document licences and the consuming project’s retention policy remain separate. |
| D08 Reproducibility | A: Record the searched root/file identities, revisions or hashes where useful, query/options and actual source locators. Preserve enough to distinguish missing files from zero matches. |
| D09 Data quality | E/A: Parsed/OCR text may omit layout or misrecognise words. Inspect original pages or data context where decisive and distinguish synthetic fixtures from actual project evidence. [S26–S27.] |
| D10 Freshness | A: File modification and index timestamps need not be publication/effective dates. Confirm the correct revision and index currency for changing material. |
| D11 Multimodal support | A: Binary images/audio/video are not made searchable evidence by grep. Use an authorised format-aware parser or visual/transcript inspection only when required. |
| D12 Failure modes | A: Wrong roots, absent mounts, ignored/binary files, stale indexes and truncated ranges must be diagnosed. Do not replace missing private evidence with an invented local path or a public-web approximation. |

## A13: Code / data analysis

Primary evidence basis: S37, S38, S39. Earlier Stage 3 contracts supply the traceability and authority constraints.

| Concern | Assessment |
|---|---|
| D01 Coverage | A: Covers the acquired dataset, code and permitted computation. Analysis creates derived evidence from inputs; it does not acquire unseen observations or make a sample representative. |
| D02 Precision | A: Explicit filters, identifiers, units and transformations can answer a narrow analytical question. The method and input scope must fit the inference; precision of arithmetic is not causal validity. |
| D03 Cost | A: Compute, memory, storage, sandbox or specialist review costs depend on the operation. Prefer a bounded calculation before an unjustified large model or corpus-processing job. |
| D04 Latency | A: Data size, parsing, joins and algorithm choice affect work. No analysis-performance benchmark was run; retain actual command/output if a later research task executes one. |
| D05 Rate limits | A: Local computation has resource limits rather than a universal API quota. Remote data pulls or hosted sandboxes retain their service-specific constraints. |
| D06 Authentication | A: Limit code to authorised inputs and execution capabilities. No network access, secret retrieval, package installation or data disclosure is implied by permission to analyse a file. |
| D07 Licence / terms | A: Check input data terms, code/library licensing and permission to redistribute derived data. A transformation does not automatically extinguish source restrictions. [S39.] |
| D08 Reproducibility | A: Preserve input edition/hash, selection, code or explicit operation, parameters, units, relevant environment and observed output; identify randomness where it can change the answer. |
| D09 Data quality | E/A: CSV dialects and value interpretation affect parsing. Check missingness, denominators and units before calculating; record transformations rather than calling derived values source-reported. [S37.] |
| D10 Freshness | A: Results inherit the input period/version, not the execution date. A rerun on unchanged old data does not refresh the underlying evidence. |
| D11 Multimodal support | A: Analysis can process permitted image/audio features or transcripts with suitable methods; neither a computed score nor transcription alone verifies the represented event. |
| D12 Failure modes | A: Parsing/type errors, leakage, bad joins, changed schemas, unsupported models and hidden filtering need the smallest reproducible correction, followed by rechecking affected claims. |

## Named scholarly-service comparison

These are four distinct investigated routes within A07, not four claims of independent confirmation. Choose by required record type, subject coverage, access and provenance. The table states provider documentation as inspected on 10 September 2026; actual account allowances and response headers remain authoritative at execution.

| Service | Evidence role and scope | Access / current operating constraint | Reproducibility and failure boundary |
|---|---|---|---|
| Crossref | DOI/deposit metadata, identifiers, licence fields and post-publication updates when deposited; recover the corresponding original. | No sign-up for public access; polite pool uses a working contact address. Since 21 July 2026, single public/polite requests are 5/10 per second, list requests 1/3. Inspect headers. | Save DOI/query, fields, cursor and access time. Missing or incorrect metadata and copyrighted abstracts remain possible; full-text inspection is a separate task. [S04–S05.] |
| OpenAlex | Scholarly discovery and related entities; a data service rather than proof of a study’s methods. | Current August help permits keyless basic access; a free key raises the budget. The page documents a 100-request/second ceiling and budget-based 429 responses; basic paging stops at 10,000, then use a cursor. | Record version/date, IDs, filters and cursor. CC0 metadata and the priced delivery service are separate; linked full-text rights still require inspection. [S06–S07.] |
| Semantic Scholar | Academic graph, recommendations and dataset interfaces; select the needed surface rather than assuming one uniform API. | The inspected tutorial gives a default authenticated 1 request/second and explains key-dependent dataset access. Batch/bulk routes and current quotas must be checked. | Record identifiers, selected fields, query and dataset release/diff where used. Follow dataset readmes and original-paper access; ranking is not appraisal. [S08.] |
| PubMed-like / NCBI E-utilities | Biomedical bibliographic discovery and Entrez-linked record retrieval. PubMed and accessible full-text repositories are not interchangeable corpora. | The guide documents 3 requests/second without a key and a default 10 with a key, with identified tool/contact and batch/history guidance. | Retain database, complete query/translation where available, identifiers, retrieval date and history/selection. A record or abstract does not establish full-method inspection. [S09.] |

## Comparative decisions

For known source identity, prefer its permitted native or direct retrieval over an unconstrained research-agent run. For an unknown source ecology, discovery can establish the map before expensive acquisition. For changing structured facts, a native API/versioned record may answer more directly than search prose. For private content, native authorization and exact scope outrank convenience. For visual or malformed evidence, the supporting representation must be inspected rather than silently trusting extracted text. These are question-relative design choices, not measured rankings or mandatory vendors.

No common score or cheapest-provider winner is computed: the units, access scope, source rights and research purpose differ. In particular, low call cost cannot compensate for inaccessible evidence or unauthorised disclosure. The twelve dimensions remain separately inspectable in this single authoritative matrix; the stage validator checks every actual row.
