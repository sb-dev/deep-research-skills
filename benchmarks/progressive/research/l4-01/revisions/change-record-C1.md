# L4-01 — Change record C1

Frozen on 2026-09-13 with baseline B1, research R1 and temporal table T1. No refresh has yet executed. Parent evaluator must independently audit those inputs and diagnose the affected claims before producer creates R2. The evidence below is an actually observed trigger, not a fictional future event or a defective baseline fabricated for testing.

## Observed triggers and proposed dependency scope

- **U01/U02, OpenAlex:** S9's January proposal uses 100/100,000 daily credits with explicitly provisional operation costs; S3's February blog uses monetary pricing and a production-key rule with a demo exception. Current official S4 (updated August 19) permits basic keyless use, S10 (August 9) states $0.10/day keyless and $1/day free-keyed, and S5 (August 11) describes monetary budgets. S7 wrapper version 3.1.0.9000 still repeats the earlier credit wording. H3/H4 remain historically supported; present applicability and wrapper interpretation require a distinct current claim and review. This is documentation change, not measured enforcement or a proven credit conversion.
- **U02, Crossref:** The live S6 page carries an October 16, 2025 update label and a pool-only rate table. A current provider original was obtained at [Crossref July forum post](https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137), S11. The forum JSON records creation and update at 2026-07-21T08:34:42.861Z, author mrittman. The first post says implementation starts July 21, gives single/list differentiation and email-address aggregation. This is newer eligible evidence relative to B1, and a temporal challenge to any inference that S2 independently proves every subtype limit fully operative on December 1. H1 remains an announcement; H2's attribution to the annual report remains true. Exact staged rollout remains unresolved.

S11 exact source representation is sources/S11-crossref-july.txt, acquired from the same topic's `.json` URL by unauthenticated urllib, first post's cooked HTML inspected. Relevant headings: Rate limiting based on the type of request; Rate limiting based on email address. The dated forum statement is primary for the provider's own stated implementation plan, not an independent measurement. It links S6 and prior late-2025 changes; it does not supply measured enforcement observations.

## Execution/source record

Read existing B0 before all writes; preserve its text at the start of baseline.md. Actual producer skill implementation: local deep-research SKILL.md plus common, discover, extract-evidence, analyse-evidence, synthesise, refresh and relevant evidence/repair references. Evaluator audit/diagnosis contracts read only to respect write separation. No private oracles read; no install, provider research run, service test, paid access, credentials, git writes or external communications.

**Budget at C1 freeze: 12 of 20 discovery queries and 31 of 64 source actions, including inherited 6 queries / 10 actions.** Independent parent review retains 12 reserved actions, leaving at most 21 producer actions and 8 queries before review consumption. There are no pending retrievals. Local library-import failures occurred before networking and consumed no source action; no packages installed.

Continuation discovery queries (6, including one forum discovery request):

1. `site.crossref.org blog 2025 REST API rate limits December 1 2025`
2. `site.blog.openalex.org API key 2026 February 13 pricing`
3. `site.crossref.org/blog "December 2025" "limits"`
4. `site.blog.openalex.org "February 13" "2026"` (low relevance results; no inference of absence)
5. `"Crossref" "Refining REST API limits"`
6. Official forum `search.json?q=Refining REST API limits` (also charged as a source action).

Continuation source actions (21): three native opens of S3/S4/S5; eight urllib attempts for S1–S8 (S1/S2/S6/S7/S8 succeeded and saved; S3/S4/S5 failed, with exact errors unavailable after combined output truncation); three further native opens of S3/S4/S5 exposing complete relevant passages; one failed guessed Crossref blog locator `/blog/refining-rest-api-limits-for-improved-stability-and-reliability/` (native tool non-retryable unsafe URL result, not proof page absent); two native clicks obtaining S9 and S10; four ordinary urllib forum requests (homepage, latest.json, search.json and S11 topic JSON). Homepage/latest did not find the desired update; search found topic 16137; topic acquisition succeeded. Inherited acquisitions remain charged but their individual trace was not present in the prior B0 file and is not reconstructed from guesses.

Official sources were preferred; non-provider search hits, proxies and reprints were not adopted as primary policy evidence. Wrapper originals are secondary policy views. Search snippets located candidates and did not substitute for original-message inspection. All retrievals occurred 2026-09-13; current web representations are not claimed to be archived historical versions. Parsed text and concise notes preserve exact locator and material transformation rather than inventing checksums.

Producer self-check: coherent B1/R1/T1 frozen, S11 observed independently of baseline writing and registered here; current findings deliberately await real evaluator diagnosis before refresh. Independent verdict pending.
