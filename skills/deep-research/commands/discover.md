# discover

Apply the [common command contract](../references/command-contract.md).

**Purpose.** Discover and triage candidate sources within the agreed method. Discovery and eligibility recording remain coupled so filtered-out evidence does not disappear.

**Inputs and preconditions.** Authorised A01/A02, existing A03 and an explicit query/corpus or recorded gap. For new discovery, a bounded acquisition route is available and passes the local source and authority eligibility checks. A supplied-candidates triage focus can operate on existing records without a new acquisition call; record that no new search was performed. A known exact source may be resolved directly without broad rediscovery.

**Operation.** Run the selected discovery operation, or inspect only the supplied candidate set when triage is the requested focus. Inspect returned scope and continuation, and record actual queries/filters and consequential exclusions where applicable. Register candidates, identifiable duplicate records and access state. Assess relevance against declared criteria; do not exclude null or adverse evidence because of its polarity. Use only legitimate, bounded fallbacks.

**Outputs and write scope.** Update actual-search portions of A02 and candidate/selection portions of A03; add A07 coverage/access gaps. Leave claims and report text unchanged. A hit, snippet or abstract retains its actual access depth.

**Completion and review.** The specified discovery batch is accounted for, including incomplete or zero-result scope. Every retained candidate has a resolvable identity or explicit identity gap and a selection disposition. A completed batch is not proof of global completeness or sufficiency.

**Failure and smallest repair.** Handle capped lists through real continuation; handle empty or failed queries as bounded observations, not non-existence. Correct the query, corpus or eligibility decision; retain valid candidates and their history.

**Independent use and evaluation reason.** A consuming discipline can obtain an inspectable source map. Test exact-source routing, truncated pagination, duplicate records, adverse eligible results and inaccessible originals; the expected selection rule comes from the brief, not the generated shortlist.

**Example invocation.** Use deep-research, operation discover. Execute the next authorised batch in research/plan.md. Update the source register with inclusion, exclusion and actual access states. Do not turn search snippets into verified findings.
