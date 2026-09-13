# L4-01 — Access-policy history

Revision R2, current-documentation refresh, created 2026-09-13 after independent A1/D1 audit and diagnosis. Source-checkout implementation exercise; not an installed consumer run. Frozen R1 is retained at revisions/research-R1.md; retrospective B1 remains unchanged. R2 requires its own independent revision audit in evaluation/audit.md.

The baseline reconstructs what Crossref and OpenAlex officially announced and later reported, rather than assuming announcement dates equal enforcement dates. H1–H4 and their exact temporal limits are fixed in [baseline.md](baseline.md). Crossref offers a dated later report of implementation; the OpenAlex February original states policy in present tense but does not establish the actual February 13 switch. No service enforcement test was performed.

## Source and evidence register

All representations retrieved 2026-09-13. Provider sources are authoritative about their own documented policy, but are neither independent corroborators of themselves nor independent enforcement measurements. Web pages are mutable; publication and last-updated labels do not prove byte identity with earlier dates. sources/ contains parsed text for S1/S2/S6/S7/S8 and concise locatable extraction notes for native-web sources.

| ID | Source / exact locator | Version and inspected scope | Use |
|---|---|---|---|
| S1 | [Crossref announcement](https://www.crossref.org/blog/announcing-changes-to-rest-api-rate-limits/), introduction, two pool tables, Who will be affected | Martyn Rittman / Luis Montilla, 2025-11-05; DOI 10.64000/wadve-3tj60; full HTML text acquired, policy passages inspected | H1, primary original |
| S2 | [Crossref annual report](https://www.crossref.org/blog/highlights-of-a-very-busy-year-our-2025-annual-report/), Metadata API and services improvements | 2025-12-18; DOI 10.64000/hsdpk-8cm70; full HTML acquired, relevant section inspected | H2, same provider's retrospective report |
| S9 | [OpenAlex January message](https://groups.google.com/g/openalex-users/c/rI1GIAySpVQ), What's changing / Credit-based limits | Jason Priem original, 2026-01-13; full rendered message inspected | H3, primary dated original linked by S3 |
| S3 | [OpenAlex February blog](https://blog.openalex.org/openalex-api-new-features-and-usage-based-pricing/), API keys / Usage-based pricing | Jason, 2026-02-24; full rendered original inspected | H4, primary dated original |
| S4 | [OpenAlex Authentication](https://help.openalex.org/api/authentication/), opening / Rate limits | Updated 2026-08-19; full rendered page inspected | Current evidence for C2/C3 in R2 |
| S5 | [OpenAlex Pricing](https://help.openalex.org/access/pricing/), free daily usage | Updated 2026-08-11; full rendered page inspected | Current evidence for C2/C3 in R2 |
| S10 | [OpenAlex Example costs](https://help.openalex.org/access/example-costs/), operation costs / free budget | Updated 2026-08-09; full rendered page inspected | Current evidence for C2/C3 in R2 |
| S6 | [Crossref access documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/), Request limits | Updated label 2025-10-16; full HTML acquired, policy passages inspected | Current retrieval with old update label; freshness unresolved |
| S7 | [openalexR](https://docs.ropensci.org/openalexR/), API Key (Required) | Displayed 3.1.0.9000, no page publication date established; policy section inspected | Wrapper documentation secondary to provider for policy; not service test |
| S8 | [rcrossref](https://docs.ropensci.org/rcrossref/), Register for the Polite Pool | Displayed 1.2.1, no page publication date established; full page inspected | Wrapper documents crossref_email configuration, not enforcement |
| S11 | [Crossref July update](https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137), first post, two rate-limiting headings | mrittman, forum JSON created/updated 2026-07-21T08:34:42.861Z; first post cooked HTML inspected | Primary documented subtype and email policy, C1/C4 |

The wrapper requirement is met by inspecting documentation for both clients; their code was not executed or inspected at an immutable commit. S7 repeats February 13 and 100/100,000 daily credits; it cannot independently prove that rollout or map provisional historical credits to current prices. S8 documents sharing an email to enter Crossref's polite pool, consistent with S1's documented access advice.

## Current-documentation findings — R2 only

These are provider-documented rules in the inspected sources, not measured service results. The policy claim valid-as-of dates are the source dates below; September 13 retrieval establishes the inspected representation, not an enforcement date or complete absence of subsequent changes.

| Claim | Current-documentation finding | Evidence and temporal limit | Support / review |
|---|---|---|---|
| C1 | Crossref lists single-record rates of 5 public / 10 polite requests per second and list-record rates of 1 public / 3 polite requests per second. | S11, Rate limiting based on the type of request, 2026-07-21 statement; H1 numbers preserved historically | Supported as provider policy; R2 needs recheck |
| C2 | OpenAlex permits basic keyless use with $0.10/day; a free account/key receives $1/day. | S4 opening (2026-08-19), S10 free budget (2026-08-09), S5 daily budget (2026-08-11) | Supported as current documentation; no independent enforcement measurement; R2 needs recheck |
| C3 | OpenAlex's documented per-1,000-call costs are: singleton free, list/filter $0.10, keyword or semantic search $1, content download $10. | S10 operation-cost table, updated 2026-08-09; source's categories retained | Supported as current documentation; R2 needs recheck |
| C4 | Crossref's July update says it will aggregate rate limiting by mailto email address, so users sharing a default email can share the limit across IPs. | S11, Rate limiting based on email address, 2026-07-21 | Supported as announced rule; actual rollout unmeasured; R2 needs recheck |

The later Crossref original adds subtype specificity missing from S6's generic pool table. It also complicates the chronology: S2 retrospectively reports a December revision, whereas S11 describes subtype implementation starting in July. The evidence supports those two attributed statements, without establishing whether rollout was staged, partial or reimplemented. **Do not infer all list-specific limits were enforced from December 1.** No concurrency change is inferred from S11's silence; H1's concurrency table remains a historical announced value.

OpenAlex's August wording provides more specific present guidance than the January proposal or the wrapper's repeated credit totals. Historical credit values and current monetary prices are different dated representations; no cross-period exchange rate is inferred. The February blog's small demo exception and August keyless budget need not represent an absolute ban reversed overnight; the observed change is in policy detail and applicability, with the precise transition unresolved.

Recommendation for a consumer implementing against these documents: budget OpenAlex calls by the current documented operation and use a free key for work beyond the smaller keyless allowance. For Crossref, distinguish singleton from list requests and account for a genuinely shared email's aggregate traffic. Both providers document response-header monitoring and backoff for rate limiting (S4 Rate limits / Best practices; S11 type-of-request section). These are source-based implementation recommendations, not validation of a wrapper, authorization to create credentials or guarantees of live thresholds.

The independent A1/D1 diagnosis reviewed B1/R1/T1/C1 and identified temporal applicability as the repair target. Its historical H1–H4 support remains relevant; its checks do not approve the new C1–C4 wording or recommendation. Those changed dependencies and T2 rows require the parent's separate R2 audit.

## Scope and gaps

The reconstruction intentionally leaves inaccessible/unobtained earlier states open. No archival original proving earlier complete policy was obtained. Current source conflicts and changing applicability are in [change-record.md](change-record.md). [temporal-table.md](temporal-table.md) separates dates and enforcement status. R2 supplies the separately labelled current-documentation interpretation; deployment behavior and precise rollout dates remain outside the inspected evidence. Inherited collection trace is incomplete, so exact replay of all earlier discovery remains blocked even though the retained claim sources are locatable.

Producer self-check: C1–C4 and recommendation checked against already acquired S4/S5/S10/S11; historical paragraph and B1 claims retained. This is not independent approval of R2. Execution/source record: R2 implements A1/D1 through a local evidence/interpretation delta, with zero new queries or source acquisitions. Aggregate budget before revision audit is 12/20 queries and 35/64 actions, including four conservatively charged parent baseline-review inspections; eight review actions remain reserved. See change-record.md for the exact preserved revisions and acquisition record. No service test, credentials, installation or paid work.
