# L4-01 — Access-policy history

Revision R1, frozen retrospective report, created 2026-09-13. Source-checkout implementation exercise; not an installed consumer run. Requested current-documentation revision is pending separate evaluator diagnosis.

The baseline reconstructs what Crossref and OpenAlex officially announced and later reported, rather than assuming announcement dates equal enforcement dates. H1–H4 and their exact temporal limits are fixed in [baseline.md](baseline.md). Crossref offers a dated later report of implementation; the OpenAlex February original states policy in present tense but does not establish the actual February 13 switch. No service enforcement test was performed.

## Source and evidence register

All representations retrieved 2026-09-13. Provider sources are authoritative about their own documented policy, but are neither independent corroborators of themselves nor independent enforcement measurements. Web pages are mutable; publication and last-updated labels do not prove byte identity with earlier dates. sources/ contains parsed text for S1/S2/S6/S7/S8 and concise locatable extraction notes for native-web sources.

| ID | Source / exact locator | Version and inspected scope | Use |
|---|---|---|---|
| S1 | [Crossref announcement](https://www.crossref.org/blog/announcing-changes-to-rest-api-rate-limits/), introduction, two pool tables, Who will be affected | Martyn Rittman / Luis Montilla, 2025-11-05; DOI 10.64000/wadve-3tj60; full HTML text acquired, policy passages inspected | H1, primary original |
| S2 | [Crossref annual report](https://www.crossref.org/blog/highlights-of-a-very-busy-year-our-2025-annual-report/), Metadata API and services improvements | 2025-12-18; DOI 10.64000/hsdpk-8cm70; full HTML acquired, relevant section inspected | H2, same provider's retrospective report |
| S9 | [OpenAlex January message](https://groups.google.com/g/openalex-users/c/rI1GIAySpVQ), What's changing / Credit-based limits | Jason Priem original, 2026-01-13; full rendered message inspected | H3, primary dated original linked by S3 |
| S3 | [OpenAlex February blog](https://blog.openalex.org/openalex-api-new-features-and-usage-based-pricing/), API keys / Usage-based pricing | Jason, 2026-02-24; full rendered original inspected | H4, primary dated original |
| S4 | [OpenAlex Authentication](https://help.openalex.org/api/authentication/), opening / Rate limits | Updated 2026-08-19; full rendered page inspected | Current refresh trigger only in R1 |
| S5 | [OpenAlex Pricing](https://help.openalex.org/access/pricing/), free daily usage | Updated 2026-08-11; full rendered page inspected | Current refresh trigger only in R1 |
| S10 | [OpenAlex Example costs](https://help.openalex.org/access/example-costs/), operation costs / free budget | Updated 2026-08-09; full rendered page inspected | Current refresh trigger only in R1 |
| S6 | [Crossref access documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/), Request limits | Updated label 2025-10-16; full HTML acquired, policy passages inspected | Current retrieval with old update label; freshness unresolved |
| S7 | [openalexR](https://docs.ropensci.org/openalexR/), API Key (Required) | Displayed 3.1.0.9000, no page publication date established; policy section inspected | Wrapper documentation secondary to provider for policy; not service test |
| S8 | [rcrossref](https://docs.ropensci.org/rcrossref/), Register for the Polite Pool | Displayed 1.2.1, no page publication date established; full page inspected | Wrapper documents crossref_email configuration, not enforcement |

The wrapper requirement is met by inspecting documentation for both clients; their code was not executed or inspected at an immutable commit. S7 repeats February 13 and 100/100,000 daily credits; it cannot independently prove that rollout or map provisional historical credits to current prices. S8 documents sharing an email to enter Crossref's polite pool, consistent with S1's documented access advice.

## Scope and gaps

The reconstruction intentionally leaves inaccessible/unobtained earlier states open. No archival original proving earlier complete policy was obtained. Current source conflicts and changing applicability are in [change-record.md](change-record.md). [temporal-table.md](temporal-table.md) separates dates and enforcement status. Current use requires the separately labelled R2 refresh and revision-specific evaluation; R1 is usable only as retrospective source attribution.

Producer self-check: claim/source links and historical modality inspected locally. Independent audit belongs to parent evaluator; not yet received. Execution/source record: one consolidated continuation record in change-record.md; frozen inherited budget remains charged. No external service request test, credentials, installation or paid work.
