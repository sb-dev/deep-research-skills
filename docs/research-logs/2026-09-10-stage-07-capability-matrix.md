# Stage 7: Capability Matrix

Date: 10 September 2026. Authority: original bootstrap section 13.

This matrix evaluates 35 investigated candidates against all 15 required fields (525 field assessments). Capability, interfaces and maintenance observations describe the inspected primary sources in the [source register](2026-09-10-stage-07-sources.md). Maturity, fit, gaps and decisions are project analysis of those observations, not independently measured product performance. No candidate was installed or benchmarked in this stage. The existing GitHub connector was used to read and publish this repository; that is not an official MCP/CLI installation test.

`USE` means reuse an existing capability when the task and authorised environment fit; it does not assert universal installation or validated integration. `ADAPT` identifies a concrete boundary conversion or control requirement. `REFERENCE` retains an investigated alternative or method without selecting it as a baseline dependency. `REJECT` identifies a specified unsuitable use. All deployment-specific promises still require the tests assigned to later stages. Prices and latency are deliberately not fabricated; operational cost drivers and unmeasured limits are recorded instead.

The readable records below are authoritative. Category membership maps to G01–G14 in the landscape; it is not an installation manifest or a fixed skill inventory. Different interfaces from one provider are not independent evidence sources.

## C01: K-Dense literature-review skill

Categories: G01.

| Field | Assessment |
|---|---|
| Capability | Planning, multi-database screening, synthesis and bibliography workflow. |
| Source | S01: inspected literature-review SKILL.md, version 1.8. |
| Licence / terms | MIT skill text; bundled tools, services and source works retain separate terms. |
| Maturity | Detailed procedural package; methodological compliance not demonstrated by installing it. |
| Installation / access | Agent Skill with Python scripts, sibling skills and Parallel CLI dependencies. |
| Research role | Planning, discovery, extraction, synthesis and reporting guidance. |
| Source control | Academic domains and database choices; no demonstrated universal source-access guard. |
| Citation behaviour | Citation scripts identify bibliographic records; claim entailment still needs review. |
| Deterministic vs generative | Generative workflow with mechanical metadata and rendering steps. |
| Provider coupling | Primary Parallel CLI and schematic-skill assumptions couple its default workflow. |
| Cost / latency | Search, model and optional figure generation consume separate resources; unmeasured here. |
| Composability | Reference selected procedures, not its whole workflow or sibling-dependent package. |
| Maintenance | Inspected version 1.8; repository activity was observed on 7 September 2026. |
| Gaps | Mandatory generated figures and fixed database minima conflict with proportionate core research. |
| Decision | REFERENCE: retain methodological comparisons; do not import blanket mandates. |

## C02: K-Dense citation-management skill

Categories: G01, G09.

| Field | Assessment |
|---|---|
| Capability | Identifier lookup, metadata enrichment, BibTeX formatting and reference validation. |
| Source | S02: citation-management SKILL.md, version 2.1; S01 licence. |
| Licence / terms | MIT skill; remote bibliographic data and optional scraping have separate restrictions. |
| Maturity | Concrete scripts and command contracts; actual script accuracy was not tested. |
| Installation / access | Agent Skill; Python 3.9+, requests; optional scholarly package. |
| Research role | Discovery, bibliographic metadata extraction and citation formatting. |
| Source control | Explicit identifiers and named academic services; scraping is an optional weaker route. |
| Citation behaviour | Checks references and manuscript keys, not whether cited evidence entails a claim. |
| Deterministic vs generative | Most metadata checks mechanical; enrichment and source selection use judgement. |
| Provider coupling | Coupled to several scholarly endpoints rather than one model vendor. |
| Cost / latency | API calls and enrichment work scale with missing metadata; latency unmeasured. |
| Composability | Potentially adapt small lookup utilities after dependency and error-path tests. |
| Maintenance | Inspected version 2.1; endpoint assumptions must be checked against current primary API docs. |
| Gaps | Missing pages or DOI can be legitimate; metadata completeness must not invent fields. |
| Decision | ADAPT: bibliographic checks only, with explicit semantic-audit separation. |

## C03: Anthropic PDF skill materials

Categories: G01, G07.

| Field | Assessment |
|---|---|
| Capability | Procedural guidance for common PDF reading, extraction and modification. |
| Source | S03: PDF SKILL.md and its adjacent LICENSE.txt. |
| Licence / terms | Proprietary licence; inspected terms restrict copying, derivatives and redistribution. |
| Maturity | Available source-visible materials are not automatically reusable open-source components. |
| Installation / access | Provider-governed skill use; not approved for vendoring in this repository. |
| Research role | Document processing guidance, not research methodology or claim verification. |
| Source control | Operates on selected documents; authority still comes from the consuming project. |
| Citation behaviour | No demonstrated claim-to-passage audit contract in the inspected excerpt. |
| Deterministic vs generative | Procedural guidance directs deterministic libraries and fallible extraction. |
| Provider coupling | Skill-material licence is tied to the provider agreement. |
| Cost / latency | Underlying processing costs vary; no runtime test or commercial clearance performed. |
| Composability | Do not copy or derive this skill; independently licensed tools remain separate candidates. |
| Maintenance | Current retrieved skill identifies its proprietary licence explicitly. |
| Gaps | Reuse rights are the decisive blocker, independent of apparent technical usefulness. |
| Decision | REJECT: no redistribution or derivative implementation from these materials. |

## C04: Tavily CLI and research Agent Skill

Categories: G01, G02.

| Field | Assessment |
|---|---|
| Capability | CLI wraps search, extract, map, crawl and research; research returns report and job identity. |
| Source | S04: Tavily CLI docs, research SKILL.md and MIT licence; S05 endpoint. |
| Licence / terms | MIT skill materials; CLI/service terms and retrieved-work rights require separate checks. |
| Maturity | Documented commands and result polling; no installed CLI or account test here. |
| Installation / access | tvly CLI with account authentication; optional selective Agent Skill installation. |
| Research role | Retrieval and optional multi-step research execution beneath domain control. |
| Source control | Research include_domains is a preference, not a strict allowlist. |
| Citation behaviour | Report citations and structured output are available; supporting passages require audit. |
| Deterministic vs generative | CLI transport is mechanical; research generation and synthesis are generative. |
| Provider coupling | Tavily account and API semantics; preserve ordinary source identifiers at handoff. |
| Cost / latency | Research jobs and suboperations consume allowance; vendor timings are not measurements. |
| Composability | Use native commands behind an evidence-return contract; check sibling-skill dependencies. |
| Maintenance | Current CLI and endpoint docs inspected; do not inherit old defaults blindly. |
| Gaps | Soft inclusion, outstanding jobs and report-only evidence can violate strict source/budget needs. |
| Decision | ADAPT: optional execution wrapper, never a replacement for research authority. |

## C05: OpenAI deep research Responses API

Categories: G02.

| Field | Assessment |
|---|---|
| Capability | Iterative research using configured web, file-search or remote MCP sources. |
| Source | S06: official deep-research API guide, sources and max_tool_calls sections. |
| Licence / terms | Hosted proprietary service; account, processing and source-content terms apply separately. |
| Maturity | Documented API; end-to-end research quality and account compatibility untested here. |
| Installation / access | Responses API with a supported deep-research model and authorised credentials. |
| Research role | Broad retrieval, analysis and draft synthesis execution. |
| Source control | Configured tools and corpora constrain access; a prompt alone is not an enforced boundary. |
| Citation behaviour | Citation annotations and exposed operation records can seed the evidence register. |
| Deterministic vs generative | Generative orchestration and synthesis; tool results have distinct execution properties. |
| Provider coupling | Responses objects and model/tool versions require a provider-specific adapter. |
| Cost / latency | Token/tool charges and call bounds apply; reserve audit capacity and reconcile jobs. |
| Composability | Submit an already-framed brief; import evidence and audit the generated report. |
| Maintenance | Current guide inspected; API omits ChatGPT-style clarification/prompt rewriting. |
| Gaps | No demonstrated guarantee for independence, contradiction completeness or local retention policy. |
| Decision | ADAPT: optional broad-research engine; retain all domain acceptance gates. |

## C06: Gemini Deep Research Interactions API

Categories: G02.

| Field | Assessment |
|---|---|
| Capability | Background research with built-in retrieval, document inputs and compatible remote MCP. |
| Source | S07: current deep-research guide, preview model and limitations. |
| Licence / terms | Hosted service and grounding/retention terms; no new processing authority is implied. |
| Maturity | Preview integration; documentation is not proof of deployed-client compatibility. |
| Installation / access | Interactions API, not generate_content; background execution and stored interaction required. |
| Research role | Extended retrieval, analysis and report generation. |
| Source control | Built-in source configuration and compatible MCP; verify actual allowed data destinations. |
| Citation behaviour | Cited report output; no promised schema-valid evidence ledger. |
| Deterministic vs generative | Generative engine, potentially multimodal; preserve inspected versus generated distinctions. |
| Provider coupling | Interactions lifecycle, preview agent identity and retained run state are vendor-specific. |
| Cost / latency | Bound work through available controls; documented maximum duration is not a delivery promise. |
| Composability | Optional adapter must recover run state and convert output into auditable records. |
| Maintenance | Guide updated 26 August 2026; preview contracts may change. |
| Gaps | No structured output or custom function calling in inspected limitations; MCP is separate. |
| Decision | REFERENCE: viable preview alternative, not the baseline execution dependency. |

## C07: Perplexity Agent API presets and legacy Sonar

Categories: G02.

| Field | Assessment |
|---|---|
| Capability | Current configurable research presets; separate legacy Sonar deep-research interface. |
| Source | S08: Agent API presets and Sonar deep-research model documentation. |
| Licence / terms | Proprietary services with account and retrieved-content constraints; no blanket reuse grant. |
| Maturity | Documented services; mutable presets prevent assuming stable behaviour from a name alone. |
| Installation / access | Agent API configuration or legacy Sonar endpoint; record which was actually invoked. |
| Research role | Search-grounded analysis and report production. |
| Source control | Tool configuration and supported endpoint controls; no strict allowlist inferred from citations. |
| Citation behaviour | Legacy output exposes citations/search results; inspect the chosen Agent API output contract. |
| Deterministic vs generative | Generative multi-step research with provider search operations. |
| Provider coupling | Preset aliases, defaults and response formats introduce substantial vendor coupling. |
| Cost / latency | Token/search/reasoning charges vary by interface; no comparative cost or latency test. |
| Composability | Optional engine only after freezing configuration and proving source/evidence export. |
| Maintenance | Current names fast/low/medium/high/xhigh replace older search/research preset names. |
| Gaps | Name-only reproducibility, cross-interface assumptions and opaque intermediate support. |
| Decision | REFERENCE: alternative engine; do not implement from obsolete preset examples. |

## C08: LangChain Open Deep Research

Categories: G02.

| Field | Assessment |
|---|---|
| Capability | Configurable research supervisor, retrieval, compression and final-report generation. |
| Source | S09: README, configuration.py and MIT licence at inspected revision. |
| Licence / terms | MIT code; model/search services and third-party evidence have separate terms. |
| Maturity | Runnable open-source design with upstream evaluations; not installed or benchmarked here. |
| Installation / access | Python/LangGraph service; uv setup and provider/search/MCP configuration. |
| Research role | Optional self-hosted iterative research execution. |
| Source control | Configurable search backend and MCP tool list; verify constraints at underlying tools. |
| Citation behaviour | Source-bearing intermediate material can be compressed; retain original support outside summaries. |
| Deterministic vs generative | Generative supervisor/research/compression; deterministic configuration and transport. |
| Provider coupling | Multiple providers supported, but LangGraph and its data structures remain implementation coupling. |
| Cost / latency | Concurrency and iteration/tool-call controls exist; defaults are not a complete cash budget. |
| Composability | Adapt as an engine endpoint; do not make its graph the domain lifecycle. |
| Maintenance | Inspected HEAD 1b7d2e8, 10 August 2026 dependency update; 2025 benchmark claims remain historical. |
| Gaps | Compression fidelity, aggregate spending, domain review and repair semantics remain to prove. |
| Decision | ADAPT: preferred self-hosted engine candidate, subject to bounded integration tests. |

## C09: GPT Researcher

Categories: G01, G02.

| Field | Assessment |
|---|---|
| Capability | Python research engine for web/local/hybrid sources with configurable retrievers and report writing. |
| Source | S10: README, .claude/SKILL.md and Apache-2.0 licence. |
| Licence / terms | Apache-2.0 code; provider, extraction and source licences remain separate. |
| Maturity | Packaged engine with documented API; quality claims and source-count slogans are unverified. |
| Installation / access | Python 3.11+ package or server; optional development Agent Skill. |
| Research role | Retrieval and draft synthesis; its supplied skill principally helps developers integrate it. |
| Source control | Web/local/hybrid mode and retriever/MCP configuration require explicit scope checks. |
| Citation behaviour | Cited reports and tracked sources; publication-level support is not claim entailment. |
| Deterministic vs generative | Generative planning/reporting with parallel retrieval operations. |
| Provider coupling | Configurable model/search providers but engine-specific configuration and objects. |
| Cost / latency | Model, crawler and parallel-worker costs; no actual workload cost or speed measured. |
| Composability | Alternative engine adapter; do not install its development helper as a complete research method. |
| Maintenance | Current master README/skill inspected; no deployment reliability or release cadence audit. |
| Gaps | Whole-source coverage claims, strict access enforcement and evidence-level repair need testing. |
| Decision | REFERENCE: credible engine alternative; avoid maintaining two baseline engine stacks. |

## C10: Brave Search API

Categories: G03.

| Field | Assessment |
|---|---|
| Capability | Indexed web discovery with search result metadata and original-page locators. |
| Source | S11: official API overview, rate guide and service terms. |
| Licence / terms | Plan-specific storage and use permissions; linked third-party content rights remain separate. |
| Maturity | Documented production API surface; recall, ranking and availability not measured here. |
| Installation / access | Authenticated search API under the consuming project account. |
| Research role | Broad discovery and targeted source finding, not original-source verification. |
| Source control | Query/filter controls constrain results only as documented; inspect originals and index limits. |
| Citation behaviour | URLs support retrieval; snippets do not prove the full cited proposition. |
| Deterministic vs generative | Search/ranking service, not a deterministic replay of the changing web. |
| Provider coupling | Provider-specific queries and results; original URLs are portable. |
| Cost / latency | Metered requests and plan quotas; cache only under applicable permissions. |
| Composability | Use an already-authorised search surface rather than building an index. |
| Maintenance | Current official access/rate material inspected; exact account entitlement not observed. |
| Gaps | Index gaps, stale snippets, result-storage restrictions and no claim audit. |
| Decision | USE: general discovery option when its rights and scope fit. |

## C11: Tavily Search / Extract / Crawl APIs

Categories: G03, G08.

| Field | Assessment |
|---|---|
| Capability | Search, selected URL extraction and bounded site acquisition are separate operations. |
| Source | S12: Search/Crawl endpoint docs; S04 CLI; S05 Research comparison. |
| Licence / terms | API plan and content-processing terms; returned text is not a republication licence. |
| Maturity | Documented API and SDK/CLI access; no live extraction accuracy test. |
| Installation / access | Authenticated REST operations or Tavily CLI/SDK. |
| Research role | Discovery and acquisition before domain extraction/appraisal. |
| Source control | Search include/exclude controls differ from Research soft inclusion; inspect endpoint semantics. |
| Citation behaviour | URLs and extracted text enable locators; automatic answers do not replace source checks. |
| Deterministic vs generative | Retrieval/extraction with optional generated answers or summaries. |
| Provider coupling | Tavily request parameters, credit charging and output formats. |
| Cost / latency | Automatic depth selection can raise credits; explicitly bound depth and crawl scope. |
| Composability | Compose search then exact extraction; do not launch whole-site crawling for a known passage. |
| Maintenance | Current endpoint docs inspected; distinguish changes across similarly named products. |
| Gaps | Extraction omissions, source dependence and endpoints with different restriction strength. |
| Decision | ADAPT: optional acquisition service with endpoint-specific controls. |

## C12: Exa Search and Contents

Categories: G03, G08.

| Field | Assessment |
|---|---|
| Capability | Filtered discovery with text/highlights and optional summarised or structured content. |
| Source | S13: current Search reference; compared with older coding-agent guide. |
| Licence / terms | Commercial API/content terms; access and reuse clearance remain operation-specific. |
| Maturity | Documented hosted API; no measured coverage or latency ranking. |
| Installation / access | x-api-key authenticated search/content requests and supported SDK. |
| Research role | Discovery and focused content acquisition. |
| Source control | Current includeDomains accepts domain/path constraints; crawl-date filters are deprecated and ignored. |
| Citation behaviour | Original URLs and text/highlights are distinct from generated summaries. |
| Deterministic vs generative | Mixed retrieval/ranking and optional generative transformations. |
| Provider coupling | Query/filter/output semantics require a small service-specific adapter. |
| Cost / latency | Plan and request options affect charges; avoid adopting vendor latency claims as measurements. |
| Composability | Optional constrained-discovery candidate; preserve explicit publication-date and source checks. |
| Maintenance | Live endpoint reference conflicts with older helper guidance on filters. |
| Gaps | Ignored freshness controls can silently admit stale material; result filtering is not truth verification. |
| Decision | ADAPT: use only supported controls and test them before claiming enforcement. |

## C13: Playwright CLI and MCP

Categories: G01, G04, G13.

| Field | Assessment |
|---|---|
| Capability | Browser control, snapshots, selected interactions and screenshots through CLI or MCP. |
| Source | S14: both project READMEs and Apache-2.0 licences. |
| Licence / terms | Apache-2.0 tooling; website access, sessions and downloaded-content terms are separate. |
| Maturity | Documented concrete commands; research-specific browser fixtures not run here. |
| Installation / access | Node tooling, browser runtime; CLI skill installation or MCP host. |
| Research role | Dynamic-source acquisition and visual inspection when simpler retrieval is inadequate. |
| Source control | Explicit navigation/interaction plan; restrict destinations and actions outside source instructions. |
| Citation behaviour | Snapshots/regions aid locators; accessibility text is not full visual evidence. |
| Deterministic vs generative | Deterministic actions against changing pages; agent navigation choices are generative. |
| Provider coupling | Low model coupling; browser/session and client interfaces still require compatibility. |
| Cost / latency | Rendering/actions consume resources; CLI token-saving claims not benchmarked here. |
| Composability | Use CLI for suitable coding hosts, MCP where host/state needs it; do not require both. |
| Maintenance | Current docs distinguish CLI and MCP and warn about state/authentication handling. |
| Gaps | Changing pages, missing visuals, session secrets and unauthorized interaction risks. |
| Decision | USE: bounded browser fallback, not the default route for every source. |

## C14: Browser Use

Categories: G01, G04.

| Field | Assessment |
|---|---|
| Capability | Autonomous browser agent, CLI/skill and hosted or local browser execution. |
| Source | S15: README and MIT licence. |
| Licence / terms | MIT repository; hosted cloud/model and destination-site permissions remain separate. |
| Maturity | Available packages and demonstrations; benchmark images are not this project evidence. |
| Installation / access | Python library, CLI skill or cloud API with relevant credentials. |
| Research role | Complex permitted navigation beyond direct browser commands. |
| Source control | Task and browser configuration; hard destination/action enforcement must be tested. |
| Citation behaviour | Agent history and final answers need conversion to source/region evidence. |
| Deterministic vs generative | Generative browser planning over browser actions. |
| Provider coupling | Local model choice reduces model lock-in; hosted browser adds service coupling. |
| Cost / latency | Browser/model jobs and possible cloud fees; stop controls must bound aggregate work. |
| Composability | Alternative escalation layer; avoid nesting another autonomous agent without a diagnosed need. |
| Maintenance | Current README distinguishes cloud, CLI and library; operational health untested. |
| Gaps | Action safety, over-navigation, evidence export and variable session outcomes. |
| Decision | REFERENCE: reserve for demonstrated navigation gaps. |

## C15: Crossref REST API

Categories: G05, G09.

| Field | Assessment |
|---|---|
| Capability | DOI/deposit metadata, reference identifiers and deposited update/licence fields. |
| Source | S16: REST guide and 21 July 2026 request-limit announcement. |
| Licence / terms | Public metadata access; some abstracts and linked full works retain separate rights. |
| Maturity | Established documented metadata service; deposit accuracy remains source-dependent. |
| Installation / access | Public REST requests; identified polite-pool access where appropriate. |
| Research role | Scholarly discovery, identifier resolution and bibliographic checks. |
| Source control | Exact DOI or documented query/filter/cursor; not a full-text search guarantee. |
| Citation behaviour | Resolves bibliographic identity, not claim-to-passage entailment. |
| Deterministic vs generative | Structured metadata lookup; evolving deposits prevent timeless replay. |
| Provider coupling | Low coupling when retaining DOI plus actual returned fields/date. |
| Cost / latency | No signup for public metadata; single/list limits differ; downstream full-text costs remain. |
| Composability | USE lookup rather than writing a DOI database; preserve ambiguous matches. |
| Maintenance | July policy refines older overview limits; use response headers at execution. |
| Gaps | Missing deposits, incorrect fields, report/study duplication and inaccessible originals. |
| Decision | USE: bibliographic primitive, never evidence sufficiency by itself. |

## C16: OpenAlex API

Categories: G05.

| Field | Assessment |
|---|---|
| Capability | Scholarly works and linked entity discovery through structured queries. |
| Source | S17: current authentication and pricing guidance. |
| Licence / terms | CC0 metadata does not license all linked papers; serving quotas/prices are separate. |
| Maturity | Documented scholarly service; entity resolution and recall unmeasured here. |
| Installation / access | Keyless basic access; optional API key and cursor-based larger retrieval. |
| Research role | Corpus discovery, citation chaining and source mapping. |
| Source control | Filters and identifiers limit queries; eligibility and full-text access still need checks. |
| Citation behaviour | Work identifiers and links seed provenance, not inspected scientific results. |
| Deterministic vs generative | Structured service with inferred entities/metadata; not a deterministic truth database. |
| Provider coupling | OpenAlex identifiers and field schema; retain DOI/original source alongside them. |
| Cost / latency | Free and metered service allowances vary; inspect current budget headers. |
| Composability | Optional academic discovery alongside complementary databases, not universal coverage. |
| Maintenance | August 2026 documentation changed older keyless/key assumptions. |
| Gaps | Entity merges, deposit lag, incomplete methods and missing original access. |
| Decision | USE: scholarly discovery where its corpus fits the method. |

## C17: Semantic Scholar Academic Graph / Datasets

Categories: G05.

| Field | Assessment |
|---|---|
| Capability | Academic graph search, recommendations and separate dataset interfaces. |
| Source | S18: official API tutorial, key, batch and dataset sections. |
| Licence / terms | API and dataset readme terms; linked article content needs its own rights check. |
| Maturity | Documented services and data releases; no recall or metadata accuracy test here. |
| Installation / access | Graph API, batch requests and key-dependent dataset access. |
| Research role | Discovery, related-paper exploration and bibliographic metadata. |
| Source control | Identifiers, query and selected fields; recommendations are leads, not eligibility decisions. |
| Citation behaviour | Paper links and citation relationships do not verify cited claims. |
| Deterministic vs generative | Retrieval/recommendation system with nontrivial ranking and entity resolution. |
| Provider coupling | Service-specific graph schema; store original identifiers and release identity. |
| Cost / latency | Documented authenticated rate guidance and batch routes; account allowance untested. |
| Composability | Complementary scholarly source, not a new mandatory database or citation graph. |
| Maintenance | Current tutorial inspected; future account-specific quota requires checking. |
| Gaps | Coverage gaps, recommendation bias and confusion between graph edges and evidence. |
| Decision | REFERENCE: add when it fills a defined scholarly discovery gap. |

## C18: NCBI E-utilities / PubMed-like access

Categories: G05.

| Field | Assessment |
|---|---|
| Capability | Entrez bibliographic search and linked record retrieval with batch/history operations. |
| Source | S19: NCBI usage guideline and API-key reference. |
| Licence / terms | Public access guidance; abstracts, full text and individual databases have distinct reuse terms. |
| Maturity | Documented established service; biomedical focus is not cross-domain completeness. |
| Installation / access | HTTP E-utilities with tool/contact identification and optional API key. |
| Research role | Scholarly discovery and retrieval of identified biomedical records. |
| Source control | Database, complete query, IDs and history constrain the actual search. |
| Citation behaviour | PMID/record metadata locates reports; PubMed is not equivalent to full-text PMC access. |
| Deterministic vs generative | Structured retrieval; query translation and index changes need provenance. |
| Provider coupling | Low model coupling; Entrez query/database conventions remain specific. |
| Cost / latency | Key-dependent rate limits and batching; full-text inspection/review costs separate. |
| Composability | Use for biomedical evidence needs without imposing a biomedical protocol on every project. |
| Maintenance | Current online usage guidance inspected; default limits are not measured throughput. |
| Gaps | Missing full methods, record/report duplication and unsuitable corpus for unrelated questions. |
| Decision | USE: specialist scholarly route when appropriate. |

## C19: GitHub native API / CLI / official MCP

Categories: G06, G13.

| Field | Assessment |
|---|---|
| Capability | Exact repository content, revisions, issues and releases through supported endpoints. |
| Source | S20: official MCP README/readonly toolsets, licences and GitHub API guidance. |
| Licence / terms | MIT MCP/CLI code; each target repository and asset has its own licence. |
| Maturity | Native connector reads/writes observed here; official MCP/CLI installation not tested. |
| Installation / access | Already-authorised connector or REST; CLI/MCP when installed and scoped. |
| Research role | Repository-source acquisition and publication verification. |
| Source control | Exact owner/repo/path/commit and read-only toolsets for research; enforce permissions separately. |
| Citation behaviour | Immutable commit/path/locator supports provenance; issues and README claims are not executed facts. |
| Deterministic vs generative | Structured retrieval and Git object operations, not generative interpretation. |
| Provider coupling | GitHub resource model; portable Git hashes reduce long-term source ambiguity. |
| Cost / latency | Primary/search/secondary quotas differ; known-object reads avoid wasteful rediscovery. |
| Composability | USE existing native access; no custom GitHub crawler or mandatory MCP server. |
| Maintenance | Current API/MCP docs inspected; connected app capabilities must be discovered, not assumed. |
| Gaps | Partial pagination, permission-related absence, binary access and mutable refs. |
| Decision | USE: default for known GitHub evidence, resolving refs before citation. |

## C20: Docling

Categories: G07, G13.

| Field | Assessment |
|---|---|
| Capability | Multiformat document conversion with structured representation and optional OCR/VLM processing. |
| Source | S21: project README, formats, interfaces and licence section. |
| Licence / terms | MIT code; model weights and source documents have separate licences. |
| Maturity | Packaged CLI/library and service interfaces; extraction fidelity not tested here. |
| Installation / access | Python package, CLI, optional docling-serve API or MCP. |
| Research role | Layout-sensitive acquisition/extraction for documents and selected multimodal inputs. |
| Source control | Exact local files or permitted URLs; select pipeline and preserve input identity. |
| Citation behaviour | Structured content can retain location context; Markdown export alone may lose precision. |
| Deterministic vs generative | Mixed parsing, ML layout/OCR and optional generative models. |
| Provider coupling | Low provider coupling for local pipelines; optional remote models add coupling. |
| Cost / latency | Model downloads, memory, OCR and review add cost; avoid for trivial plain text. |
| Composability | ADAPT conversion outputs to source/evidence locators without making its schema universal. |
| Maintenance | Current README includes service/MCP and newer formats; coming-soon features not claimed implemented. |
| Gaps | Pipeline-dependent fidelity, model licences and precise source-location export need validation. |
| Decision | ADAPT: preferred advanced local document candidate after fidelity fixtures. |

## C21: GROBID

Categories: G07, G09.

| Field | Assessment |
|---|---|
| Capability | Scientific PDF structuring, bibliographic parsing, citation contexts and coordinates. |
| Source | S22: README, documented interfaces and separate code/data licence statements. |
| Licence / terms | Apache-2.0 code; documentation CC0 and annotated data CC BY as stated. |
| Maturity | Upstream reports production deployments; their accuracy results are not our validation. |
| Installation / access | Docker/web service or Java integration; model/runtime requirements depend on configuration. |
| Research role | Scholarly document and reference extraction. |
| Source control | Chosen PDF corpus and model configuration; no broad source discovery guarantee. |
| Citation behaviour | Reference/callout linking and coordinates help provenance but do not establish entailment. |
| Deterministic vs generative | ML sequence/layout processing; outputs remain fallible extractions. |
| Provider coupling | Local service avoids model-vendor lock-in; TEI and model configuration are integration coupling. |
| Cost / latency | Server/model resources and warm-up; no reproduced throughput comparison. |
| Composability | Specialist alternative to general conversion when references and coordinates matter most. |
| Maintenance | Current README and interface descriptions inspected; release/runtime compatibility untested. |
| Gaps | Non-scholarly formats, scans and context-sensitive inference lie beyond its demonstrated role. |
| Decision | REFERENCE: specialist parser option, not a second mandatory document stack. |

## C22: Trafilatura

Categories: G08.

| Field | Assessment |
|---|---|
| Capability | HTML main-text, metadata and optional comments/tables extraction; URL/feed discovery. |
| Source | S23: official 2.2.0 documentation and Apache-2.0 licence. |
| Licence / terms | Current package Apache-2.0; versions before 1.8 used GPLv3+; source rights separate. |
| Maturity | Documented modular CLI/library; publisher benchmarks not independently reproduced. |
| Installation / access | Python package/CLI, live URL or previously downloaded HTML input. |
| Research role | Lightweight web text acquisition and cleanup. |
| Source control | Explicit URLs/files and extraction options; avoid expanding crawling without a source need. |
| Citation behaviour | Metadata/original URL help attribution; retained HTML provides stronger passage recovery. |
| Deterministic vs generative | Rule-based extraction and metadata inference, not generative report writing. |
| Provider coupling | Low external-provider coupling; selected version/options determine transformations. |
| Cost / latency | Local compute and downloads; cheaper candidate than browser/model processing for ordinary HTML. |
| Composability | USE extraction behind a preserved-original contract; no database required. |
| Maintenance | Inspected documentation identifies 2.2.0 and current maintenance context. |
| Gaps | Boilerplate removal can discard decisive qualifiers; dynamic pages may need another route. |
| Decision | USE: lightweight HTML extractor where existing native reading is insufficient. |

## C23: Firecrawl

Categories: G03, G08.

| Field | Assessment |
|---|---|
| Capability | Hosted/open-source search, scrape, map, crawl and interactive extraction surfaces. |
| Source | S24: README and actual AGPL-3.0 licence file. |
| Licence / terms | AGPL-3.0 repository; hosted service, SDK and source-content rights require separate review. |
| Maturity | Documented endpoints and clients; marketing coverage/latency figures not validated here. |
| Installation / access | Hosted API/SDK/CLI or separately assessed self-host deployment. |
| Research role | Web acquisition for complex pages and bounded site collections. |
| Source control | URL/crawl scope and supported filters; agent prompts do not replace access controls. |
| Citation behaviour | HTML/Markdown/screenshots and metadata can support locators; generated extraction requires checking. |
| Deterministic vs generative | Mixed deterministic retrieval/rendering and optional generative agent/structured extraction. |
| Provider coupling | Endpoint and deployment differences; hosted and self-host capability parity not assumed. |
| Cost / latency | Credits, rendering and bulk jobs; vendor P95 claims are not project measurements. |
| Composability | Optional service rather than rebuilding browser/crawl orchestration. |
| Maintenance | Current README documents evolving interact/agent surfaces; pin the chosen version. |
| Gaps | Terms, deployment parity, extraction fidelity and broad-crawl overreach. |
| Decision | REFERENCE: acquisition alternative when native/Trafilatura/browser paths are inadequate. |

## C24: Pandoc citeproc

Categories: G09.

| Field | Assessment |
|---|---|
| Capability | Renders citations and bibliographies from supplied bibliographic records and CSL styles. |
| Source | S25: official citation-rendering manual and COPYING.md. |
| Licence / terms | GPL licence in inspected copying file; style and input-source licences remain separate. |
| Maturity | Documented CLI feature; no claim of executing a conversion in this stage. |
| Installation / access | Pandoc CLI with --citeproc, bibliography and optional CSL inputs. |
| Research role | Final citation formatting and document rendering, after support review. |
| Source control | Explicit files; remote bibliography/style URLs are separate network operations. |
| Citation behaviour | Formats records and references, not source authenticity or claim support. |
| Deterministic vs generative | Deterministic transformation for fixed version, inputs and style. |
| Provider coupling | Low provider coupling; CSL and bibliography formats are portable. |
| Cost / latency | Local processing; additional PDF engines are optional costs, not required for Markdown. |
| Composability | USE only when the chosen output needs managed bibliography formatting. |
| Maintenance | Current manual inspected; lock renderer/style versions for reproducible output. |
| Gaps | Incorrect metadata renders neatly; remote style fetches and broken citation keys need checks. |
| Decision | USE: optional presentation primitive, never the semantic citation evaluator. |

## C25: Zotero reference manager and APIs

Categories: G10, G09.

| Field | Assessment |
|---|---|
| Capability | Library items/collections, metadata, exports and incremental version-aware retrieval. |
| Source | S26: official Web API v3 basics and project COPYING. |
| Licence / terms | AGPLv3 desktop code; online service, attachments and publisher content have separate terms. |
| Maturity | Documented desktop and online interfaces; user-library integration not executed. |
| Installation / access | Desktop local API or Web API; private online libraries require scoped credentials. |
| Research role | Consumer-owned source library and bibliography exchange. |
| Source control | Library/collection/item identity plus query; Web/local result semantics may differ. |
| Citation behaviour | Item keys, versions and bibliographic exports retain references; attachments still need inspection. |
| Deterministic vs generative | Mechanical library retrieval and rendering; source appraisal remains domain judgement. |
| Provider coupling | Zotero item/version model; exported CSL/BibTeX reduces lock-in. |
| Cost / latency | Local reads versus hosted storage/API constraints; no account usage measured. |
| Composability | Optional import/export adapter; never require migration into a new central library. |
| Maintenance | API page updated 29 July 2026; current local/Web differences explicitly documented. |
| Gaps | Saved-search metadata is not saved-search results; attachment access and version identity matter. |
| Decision | REFERENCE: support existing libraries without owning their project knowledge. |

## C26: DuckDB

Categories: G11.

| Field | Assessment |
|---|---|
| Capability | Local SQL analysis of structured data, including directly queried CSV and Parquet. |
| Source | S27: README and inspected MIT licence. |
| Licence / terms | MIT code; input datasets and extensions retain independent terms. |
| Maturity | Packaged analytical engine; workload-specific correctness/performance not tested here. |
| Installation / access | CLI or language client; use a pinned local version. |
| Research role | Bounded transformations, comparisons and reproducible calculations. |
| Source control | Explicit files/tables, selected rows and columns; network/extensions need separate authority. |
| Citation behaviour | Preserve query, input revision, units and outputs; computed results are derived evidence. |
| Deterministic vs generative | Deterministic computation where inputs, settings and functions are deterministic. |
| Provider coupling | Low provider coupling; SQL dialect/extensions create limited engine dependence. |
| Cost / latency | CPU/memory/storage; use simpler existing computation when sufficient. |
| Composability | USE as an optional calculation tool, not the universal evidence database. |
| Maintenance | Current README and versioned licence inspected; no latest-release claim. |
| Gaps | Type inference, missing values, bad joins and unsupported causal conclusions remain risks. |
| Decision | USE: local analysis for questions that genuinely require it. |

## C27: E2B sandbox infrastructure

Categories: G11.

| Field | Assessment |
|---|---|
| Capability | Cloud-isolated command execution with distinct code-interpreter and desktop SDKs. |
| Source | S28: current README, Apache-2.0 licence and limited versioned SDK passages. |
| Licence / terms | Apache-2.0 repository; cloud service charges, infrastructure and processed data terms differ. |
| Maturity | Documented SDKs and self-host route; isolation and recovery not independently tested. |
| Installation / access | Python/JavaScript SDK with account key; separate interpreter/desktop packages where needed. |
| Research role | Optional isolated execution for untrusted or resource-specific analytical tasks. |
| Source control | Explicit inputs and runtime configuration; network/secret access must be restricted deliberately. |
| Citation behaviour | Command/output artifacts aid reproducibility, but sandbox success does not validate a method. |
| Deterministic vs generative | Execution substrate; generated code and analysis may be nondeterministic or wrong. |
| Provider coupling | Sandbox lifecycle and cloud API coupling; self-host requires substantial infrastructure. |
| Cost / latency | Session/runtime charges and outstanding jobs; preserve reservations until reconciliation. |
| Composability | Optional substitute for unavailable suitable local isolation, not a mandatory hosting platform. |
| Maintenance | Current README separates SDK roles; detailed SDK opens were partly unavailable. |
| Gaps | Network isolation, timeout recovery, retention and actual account limits need deployment testing. |
| Decision | REFERENCE: use only after a concrete isolation or execution gap is established. |

## C28: Obsidian CLI and local notes

Categories: G12.

| Field | Assessment |
|---|---|
| Capability | Vault-scoped read/search and note navigation through an application CLI. |
| Source | S29: official CLI help and application terms. |
| Licence / terms | Proprietary application under its terms; local note ownership does not grant source republication rights. |
| Maturity | Documented CLI tied to installed desktop application; headless service support not established. |
| Installation / access | Compatible installer and running app; name the vault and exact path. |
| Research role | Consumer-owned note access and research handoff, not the research evidence authority itself. |
| Source control | Explicit vault/path; avoid accidentally using the active vault or write-capable commands. |
| Citation behaviour | Local links and note references can preserve locators; links are not evidence verification. |
| Deterministic vs generative | Mechanical file/app operations; no built-in claim appraisal assumed. |
| Provider coupling | Desktop application/CLI coupling; plain Markdown remains portable. |
| Cost / latency | Existing local application and indexing costs; no optional service purchase required by this design. |
| Composability | Optional read adapter; core research remains runnable without this app. |
| Maintenance | Current CLI documentation inspected; installer/application compatibility must be checked. |
| Gaps | App dependency, ambiguous vault defaults and unaudited note assertions. |
| Decision | REFERENCE: consumer integration only, not a new mandatory knowledge system. |

## C29: Notion hosted MCP and local-server alternative

Categories: G12, G13.

| Field | Assessment |
|---|---|
| Capability | Workspace search/fetch and other declared operations via hosted MCP. |
| Source | S30: supported-tools, hosted setup and open-source hosting notices. |
| Licence / terms | Hosted application/account terms; old local server licensing does not grant access to workspace content. |
| Maturity | Hosted integration documented; local notion-mcp-server is explicitly no longer actively maintained. |
| Installation / access | Hosted OAuth MCP for compatible clients; do not assume unattended bearer-token equivalence. |
| Research role | Authorised internal-source retrieval and optional consumer handoff. |
| Source control | Workspace permissions and available tool scope; connected-app search depends on entitlement. |
| Citation behaviour | Fetch exact item content after search; indexed summaries are not full original evidence. |
| Deterministic vs generative | Mechanical app access with search/index behaviour; model-driven tool choice remains separate. |
| Provider coupling | Notion/OAuth/tool contracts; scope host capabilities before use. |
| Cost / latency | Account and tool-rate limits; no tenant test or entitlement check performed. |
| Composability | Optional hosted read integration; exclude write actions from research-only execution. |
| Maintenance | Official hosting page says local issues/PRs are not actively monitored. |
| Gaps | Headless auth, sync gaps, write exposure and unmaintained local implementation. |
| Decision | REFERENCE: hosted consumer option; reject local server as a maintained baseline. |

## C30: Inspect AI

Categories: G14.

| Field | Assessment |
|---|---|
| Capability | Python evaluation framework for tasks, tools, multi-turn agents and extensible scoring. |
| Source | S31: project README and MIT licence. |
| Licence / terms | MIT framework; model services, datasets and sandbox dependencies retain their terms. |
| Maturity | Documented extensible harness; no project-specific research benchmark was executed. |
| Installation / access | Python package/CLI with selected model and optional sandbox configuration. |
| Research role | Behavioural evaluation, trace review and regression execution. |
| Source control | Explicit tasks, tool permissions, fixtures and evaluator inputs must be defined. |
| Citation behaviour | Custom scorers can inspect support; generic model grading does not prove citation correctness. |
| Deterministic vs generative | Deterministic assertions and optional generative judges require separate result labels. |
| Provider coupling | Multi-provider support; task/scorer API and logs are harness coupling. |
| Cost / latency | Model-judge/tool execution and repeated trials cost resources; bound evaluation separately. |
| Composability | ADAPT as leading behavioural-harness candidate without moving domain criteria into the framework. |
| Maintenance | Current project documentation inspected; release compatibility and maintenance responsiveness remain untested. |
| Gaps | Research-specific fixtures, judge calibration, source independence and rights controls are project work. |
| Decision | ADAPT: reuse the harness, implement and validate domain-specific evaluations. |

## C31: Promptfoo

Categories: G14.

| Field | Assessment |
|---|---|
| Capability | CLI/library for provider comparisons, assertions, model grading and red-team tests. |
| Source | S32: README and MIT licence. |
| Licence / terms | MIT code; hosted features, target models and test data have separate permissions. |
| Maturity | Documented CI-capable framework; no evaluation run performed here. |
| Installation / access | Node CLI/library; inspected README requires Node 22.22 or newer for npm usage. |
| Research role | Alternative regression/evaluation harness, including security-focused checks. |
| Source control | Configured providers, cases and assertions; sending data to a remote model still discloses it. |
| Citation behaviour | Can exercise custom checks; automatic grading is not a calibrated research truth oracle. |
| Deterministic vs generative | Mechanical assertions mixed with optional generative judges/red-team generation. |
| Provider coupling | Provider-flexible but configuration/plugin ecosystem-specific. |
| Cost / latency | Local harness does not eliminate remote model fees or review effort. |
| Composability | Alternative to Inspect; avoid two baseline harnesses without distinct demonstrated needs. |
| Maintenance | Current README inspected; runtime requirements differ from older Node guides. |
| Gaps | Local execution wording must not be interpreted as local-only model processing. |
| Decision | REFERENCE: alternative harness rather than a duplicate mandatory dependency. |

## C32: DeepResearch Bench

Categories: G14.

| Field | Assessment |
|---|---|
| Capability | Report assessment through RACE and source/claim-oriented FACT evaluation. |
| Source | S33: current README and actual LICENSE file. |
| Licence / terms | LICENSE is Apache-2.0 despite an MIT README badge; task/source rights need separate clearance. |
| Maturity | Published benchmark implementation; upstream scores are not this project results. |
| Installation / access | Python evaluation scripts, model credentials and scraping dependencies. |
| Research role | External comparison and reference for report/citation evaluation dimensions. |
| Source control | Task and evaluator configuration; retrieved webpages can change between evaluations. |
| Citation behaviour | FACT checks claim-URL pairs with retrieval and model judgement; failures can originate in either. |
| Deterministic vs generative | Generative evaluators plus mechanical extraction/aggregation. |
| Provider coupling | Judge model, scraper, task version and cleaning pipeline affect score comparability. |
| Cost / latency | Paid judges and source retrieval; no benchmark run or credential sharing authorised here. |
| Composability | Use as a reference suite after rights and configuration checks, not the complete quality model. |
| Maintenance | May 2026 evaluator migration means older Gemini-based results are not directly comparable. |
| Gaps | Licence badge conflict, judge calibration, changing pages and incomplete domain coverage. |
| Decision | REFERENCE: external benchmark, with version-specific provenance and no borrowed scores. |

## C33: DeepResearch Bench II

Categories: G14.

| Field | Assessment |
|---|---|
| Capability | Expert-report-derived rubrics separating information recall, analysis and presentation. |
| Source | S34: current README and Apache-2.0 licence file. |
| Licence / terms | Code Apache-2.0; task rights are per-source, including non-commercial exceptions. |
| Maturity | Published evaluator and task set; its construction claims are upstream descriptions. |
| Installation / access | Python evaluator over generated Markdown/DOCX reports and rubric records. |
| Research role | Fine-grained report regression design and external evaluation. |
| Source control | Task/rubric configuration and blocked-reference conditions; preserve exact versions. |
| Citation behaviour | Rubric evidence from report wording does not independently prove every source passage. |
| Deterministic vs generative | LLM scoring plus deterministic aggregation; judge disagreement remains possible. |
| Provider coupling | Rubric dataset and selected judge configuration are central dependencies. |
| Cost / latency | Batch model grading consumes allowance; no measured cost or score here. |
| Composability | Use selected licensed concepts/cases only when compatible with the project evaluation contract. |
| Maintenance | August 2026 judge migration and May per-task licence change are material current updates. |
| Gaps | Reference leakage, per-task reuse constraints and rubric-to-real-source verification. |
| Decision | REFERENCE: complementary benchmark design, not a substitute for behavioural/source tests. |

## C34: K-Dense scientific-critical-thinking skill

Categories: G01.

| Field | Assessment |
|---|---|
| Capability | Guided appraisal of scientific claims, methods, bias and inferential limits. |
| Source | S35: current scientific-critical-thinking SKILL.md, version 1.3. |
| Licence / terms | MIT skill; optional schematic service and research sources have separate terms. |
| Maturity | Procedural analytical guidance; not a validated automatic fact-checker. |
| Installation / access | Agent Skill with local references; analytical guidance does not require network access. |
| Research role | Evidence appraisal and scientific claim critique. |
| Source control | Works with supplied evidence; additional source acquisition must remain independently authorised. |
| Citation behaviour | Encourages precise source context; no demonstrated automated entailment guarantee. |
| Deterministic vs generative | Generative or human analytical judgement, not a deterministic truth test. |
| Provider coupling | Core guidance is model-neutral; optional external diagram generation is separately scoped. |
| Cost / latency | Appraisal and qualified review consume effort; optional illustrations are not required research work. |
| Composability | Reference specialist appraisal concepts without making GRADE universal or inventing expert review. |
| Maintenance | Connector reads version 1.3; an older search result still shows 1.2. |
| Gaps | Does not acquire all necessary evidence or establish reviewer competence automatically. |
| Decision | REFERENCE: useful scientific claim-evaluation guidance with specialist boundaries. |

## C35: K-Dense scientific-writing skill

Categories: G01, G09.

| Field | Assessment |
|---|---|
| Capability | Evidence-bound drafting, claim registries, consistency checks and approval separation. |
| Source | S36: scientific-writing SKILL.md version 2.1; inspected intake and workflow sections. |
| Licence / terms | MIT skill; underlying sources and venue policies remain separately governed. |
| Maturity | Concrete offline audit commands are documented; these scripts were not executed here. |
| Installation / access | Platform-neutral guidance; optional dependency-free Python 3.11+ CLIs. |
| Research role | Evidence-to-prose handoff, reporting checks and scientific manuscript review. |
| Source control | Local manifests and explicit confidentiality/processing boundaries. |
| Citation behaviour | Claim/evidence identifiers and consistency checks; source verification explicitly remains human-owned. |
| Deterministic vs generative | Mechanical local checks plus generative drafting and accountable human review. |
| Provider coupling | Low model coupling; manuscript manifests and publication policies are domain-specific. |
| Cost / latency | Local checks avoid API fees, but qualified source review remains real work. |
| Composability | Reference reusable production semantics; do not treat this as merely another execution engine. |
| Maintenance | Current version 2.1 inspected; policy dates are source-specific, not a blanket current-compliance claim. |
| Gaps | Manuscript-specific authority and mandatory human verification cannot be silently generalised or waived. |
| Decision | REFERENCE: evidence-binding comparison, not a universal research pipeline. |

