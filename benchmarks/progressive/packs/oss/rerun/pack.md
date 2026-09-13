# Revision-bound optional-engine assessment — pack case

Report revision: oss-rerun-pack-r1. Produced 2026-09-13. Scope: `langchain-ai/open_deep_research@1b7d2e80db9faa586165c60e09096dbbfd483a64`.

**Assessment:** This revision is a plausible optional orchestration engine for further verification: the inspected implementation connects clarification, research-brief generation, supervisor/researcher loops, compression and final reporting. It does not establish readiness for an evidence-led skill's source, budget, provenance or review contract. Keep the skill responsible for evidence acceptance; treat any engine output as an input requiring inspection. This is a qualified research conclusion, not deployment approval.

## Brief, method and execution record

The requested decision is candidate task fit, with capabilities, setup, licence scope, important limitations and the next verification step. Only the six named repository files and Git commit metadata were eligible. No search, linked documentation, other revision, issue, benchmark experiment, dependency source, authentication implementation or helper implementation was acquired. No installation, engine run, engine test, code change, spending, maintainer contact or deployment occurred.

Executed the core research workflow by reading and applying source-checkout instructions at `/workspace/scratch/b99193148918/deep-research-skills`; `git rev-parse HEAD` returned `b9d262b4bd2ffa73d35b520f98629e7eae0b7da7`. Read `skills/deep-research/SKILL.md`, common command, evidence, source/execution, effort/repair and pack-precedence contracts, and frame, plan, discover, extract-evidence, analyse-evidence and synthesise commands. This is source-checkout procedure execution, not evidence that a skill was installed or that the candidate engine executed. No model identifier or model-runtime version was supplied to this worker; none is inferred.

Explicit profile: `open-source-ecosystem` **0.1.1**, compatible core contract **0.1**, for this whole investigation. Read its `PACK.md`, `pack.json` and `references/method.md`; no other profile. The selected pack is an untracked local extension in this checkout, not claimed to be part of the pinned core commit. SHA-256 content identities:

| Pack file | SHA-256 |
|---|---|
| PACK.md | `4a3d938a9fa86ddc775f390eabe7ea32d7d7d7af64e4f5b532648f0371ca297a` |
| pack.json | `a5511dbaa7165fe1108eddcf993f5136c6710d37f41e20a3fa66b2dbcde58111` |
| references/method.md | `9b18bb39c1ec4b3d589723d0830a4979b02b2d0600e87119e333fda40a8dc0b7` |

Method: reconcile same-revision documentation, package and deployment settings; trace consequential settings into code branches; tie static risks to discriminating, unexecuted verification designs. Pack method links were not followed. Supplied baseline leads—Python versions and broad exception termination—were checked against originals.

The finite collection envelope was eight source actions. Actual: six `github_fetch_file` calls with the exact SHA (one per file, concurrent independent retrieval), followed by one `github_fetch_commit` call. All seven succeeded. **Consumed 7/8; unused 1; outstanding 0.** No retries or broad discovery. Full text responses were held in memory; subsequent display of selected cached passages and line numbering resolved combined-output truncation without further source calls. These were cache rereads, not independent corroboration. Local instruction reads, Git identity/status inspection, content hashing and report writing were procedural work, not engine tests.

At finalisation, the shared checkout HEAD was `d91625916c183ee810c4f7f303bd54b055fb6a14`. A scoped Git diff showed no changes under `skills/deep-research` from the initially inspected `b9d262b4bd2ffa73d35b520f98629e7eae0b7da7`; this run therefore used the unchanged core instructions identified above. The selected pack has its separately recorded content hashes. This checkout movement did not change the target engine revision or source acquisitions.

## Actual source and evidence register

All sources retrieved 2026-09-13 through the existing GitHub plugin. File responses carried the requested immutable URL, UTF-8 content and blob SHA. These are six related primary repository documents plus one same-project commit record, not seven independent sources. Repository sources are strong evidence of declarations and visible code, weak evidence of runtime success or independent quality.

| ID / original source | Returned identity and access | Evidence used |
|---|---|---|
| S1 [README.md](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/README.md) | Blob `5bfa38ac55fc7a5835b3d5c9a848d71e74c68d60`; 150-line text retrieved; setup/configuration and relevant qualification inspected | E1: Quickstart L21–58; provider/model requirements L64–77; linked benchmark claims are documentary only |
| S2 [LICENSE](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/LICENSE) | Blob `82dc7c43f7ba98b72ac619ebfe7599576dc3ce7f`; all 21 lines inspected | E2: MIT grant, copyright/permission notice condition and warranty/liability disclaimer |
| S3 [pyproject.toml](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/pyproject.toml) | Blob `54b13248d368547c2b39039b184ef0cecce9bebf`; all 90 lines inspected | E3: project 0.0.16, MIT declaration, Python ≥3.10, dependency/build declarations |
| S4 [langgraph.json](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/langgraph.json) | Blob `38ea4ecce001ca4fc7101b9592eb4c041239dbcb`; all 14 lines inspected | E4: graph export, Python 3.11, .env, local package dependency, auth entry point |
| S5 [configuration.py](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/src/open_deep_research/configuration.py) | Blob `1c5bac9e9d6134b917e98ccc75cdbf862900586e`; all 252 lines inspected | E5: provider/model/limit defaults; UI metadata; loader L236–247 |
| S6 [deep_researcher.py](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/src/open_deep_research/deep_researcher.py) | Blob `279dbffd9e49e07962fb4e1cfeff79e45adc43e9`; 719-line text retrieved and workflow, limit, failure and report paths inspected | E6: supervisor L178–349; researcher/tool execution L365–509; compression L511–583; report/main graph L607–719 |
| S7 [commit metadata](https://github.com/langchain-ai/open_deep_research/commit/1b7d2e80db9faa586165c60e09096dbbfd483a64) | Exact SHA returned; connector `created_at` = `2026-08-10T18:13:29Z`; metadata inspected | E7: dependency-update commit title, dependabot author login and web-flow committer login |

S7's tool response also automatically included a `uv.lock` patch. That incidental out-of-scope payload was not used as lockfile/dependency evidence or followed to linked sources. Only commit identity, title, time and attribution support this report. The sampled commit records one change; it does not establish a maintenance cadence, security posture, review quality or current readiness. Retrieved-at date does not advance claims beyond the pinned revision.

## Findings and claim support

**C1 — Capabilities: qualified documentary and static support (E1, E5, E6).** The README describes provider-selectable LLM research, Tavily search by default, OpenAI/Anthropic native search and MCP integration. It explicitly requires suitable structured-output and tool-calling support. Configuration exposes those search choices, MCP URL/tool/auth settings, separate summarization/research/compression/report models and limits. Defaults shown agree with README: GPT-4.1-mini for summarization and GPT-4.1 for the other model roles. These are revision defaults, not current provider-availability claims.

The code statically substantiates clarification, structured brief creation, parallel delegated research, compression and final-report generation. `researcher` obtains tools through an unseen helper and raises when it gets none; it does not prove universal provider/MCP compatibility. `compress_research` returns compressed text and raw message contents; final reporting consumes notes. Useful material for an adapter is visible, but complete source snapshots, source allowlist enforcement, evidence/claim lineage and faithful citation preservation have not been established by these files. Prompts, state reducers and tool helpers are outside the authorised universe. Recommendation inference: an evidence-led consumer must verify those properties separately and retain its own acceptance and uncertainty records.

**C2 — Setup: supported declarations, runtime unknown (E1, E3, E4).** README Quickstart says to clone, create/activate a `uv` virtual environment, install with `uv sync` (or its documented `uv pip install -r pyproject.toml` alternative), copy `.env.example` to `.env`, and use:

```text
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```

That command is transcribed documentation, not a command executed here. A future reproduction would need the pinned revision rather than an unpinned clone. The package declares **Python ≥3.10**, while both this server example and `langgraph.json` select **3.11**. These are compatible but different statements: 3.10 is a declared package floor; 3.11 is the selected server/example environment. Neither establishes a successful install on either version. Dependencies include broad minimum constraints and unpinned entries, so `pyproject.toml` alone is not an exact resolved environment. The allowed evidence excludes the complete lockfile and `.env.example`; full credentials/setup requirements remain unverified.

`langgraph.json` exports `./src/open_deep_research/deep_researcher.py:deep_researcher`, reads `./.env`, depends on `.`, and points authentication to `./src/security/auth.py:auth`. Presence of that pointer is not an authentication/security assessment; its implementation was not inspected.

**C3 — Licence scope: supported text, qualified reuse interpretation (E2, E3).** The top-level licence is MIT, copyright 2025 LangChain, permitting use, modification, distribution and sale subject to preserving its copyright and permission notice in copies/substantial portions. It includes an as-is warranty and liability disclaimer. The package also declares MIT. This supports permissive reuse of the covered software/documentation subject to the notice condition; it is not clearance of dependency licences, model/data rights or search/MCP/hosted-service terms. Those terms were not inspected. No legal or deployment approval is given.

**C4 — Failure handling: static risk, not an observed incident (E6).** In `supervisor_tools` L288–342, a broad `except Exception` surrounds delegated execution/result processing. Its condition is `is_token_limit_exceeded(e, configurable.research_model) or True`. If that helper evaluates without raising, the condition is true even for non-token errors; the handler returns `END` with extracted prior notes and the brief. It does not include the caught error in that returned update. A helper failure itself remains unresolved.

The main graph connects the research-supervisor node to final-report generation (L715). Static inference: a delegated error can end research and allow subsequent report generation from whatever notes survive, without this branch explicitly marking the report incomplete. State propagation, helper extraction, cancellation of sibling work and the actual user-visible result require execution to resolve; no failure frequency or definite silent-success claim is justified. Separately, individual tool exceptions inside `execute_tool_safely` are converted to error strings (L427–432); that does not cover every error, such as tool lookup before invocation.

**C5 — Configurable limits are not a proven request budget (E5, E6).** The loader selects uppercase environment values ahead of matching `configurable` values, drops only `None`, and constructs the Pydantic model. Thus numeric zero is retained rather than falling back; a present empty environment string also wins before model validation. The inspected integer fields carry min/max in UI metadata, with no explicit `ge`/`le` field constraints. Actual coercion/rejection by the installed dependency version is untested.

For `max_react_tool_calls` (default 10), `researcher` increments `tool_call_iterations` after a model response (L413–423). `researcher_tools` executes **all** returned tool calls with `gather` (L473–479), then compares the iteration count using `>=` (L491–503). The unit is tool-calling iterations, not individual external requests. Assuming ordinary state accumulation and successful helpers, a value of 1 permits a first batch containing several tool invocations; zero still reaches that first batch before the late check. Native provider search may already occur during the model call; its count is not established here.

The separate concurrency setting defaults to 5 and slices the supervisor's research-unit list before invocation (L291–305), returning messages for overflow. This is a per-batch subresearcher limit, not a total job/spending limit or a bound on each researcher's calls. Negative integer slice semantics could also be surprising if accepted: with three units, `[: -1]` selects two. No claim of resource exhaustion observed or operational budget enforcement follows.

## Next verification step — proposed only, not executed

The next step is a narrowly scoped, separately authorised verification using fixed fake models/tools and explicit event logging, before any paid provider run. It would resolve the highest-consequence uncertainty: whether an adapter can expose failures and enforce the consumer's action budget. Current authority remains static-only; no harness, environment or test was created.

| Proposed input | Static prediction from inspected expressions | Observe / rejection condition |
|---|---|---|
| Omit `max_react_tool_calls`; no matching environment value | Default 10 selected | Record resolved model value; reject an adapter that silently substitutes a different contract |
| Configurable integer 0, 1 and 2; environment absent; fresh state; fake researcher repeatedly returns three valid tool calls | Zero retained at loader input. If accepted, first batch executes for 0 and 1; two batches for 2, assuming no early completion and ordinary counter state | Record loaded value, model responses, individual tool invocations, counter and next node. A promised “at most N requests” fails if observed invocations exceed N; a required zero-budget run fails on any invocation. This discriminates batches from requests |
| Configurable 1 plus environment `MAX_REACT_TOOL_CALLS="2"`; separately test an empty string | Environment value wins. String conversion/empty-string validation are unresolved runtime questions | Record input, selected value and validation result. Reject if adapter claims per-request config wins, silently accepts malformed values, or omits the effective budget from its record |
| Three supervisor research calls with concurrency 0, 1, 2, then -1 | If accepted, slices select 0, 1, 2, then 2 units respectively; remainder becomes overflow messages | Count started subresearchers and inspect overflow results. Consumer should reject nonpositive settings before execution rather than interpret negative slicing as a meaningful limit |
| One delegated subresearcher raises a non-token error, another would succeed; error classifier returns false | Broad handler still chooses END; its update has notes/brief and no caught-error field | Capture task outcomes, handler update, graph route and final report/status. Reject engine integration if incomplete research is accepted as completed evidence or if failed work/source loss is concealed |

After that bounded verification, environment reproduction on the documented 3.11 setup, dependency/service-rights review and source/citation-fidelity testing would remain separate work. None is reported as passed. Evidence-led suitability depends on preserving original access and partial failures and on enforcing authorised sources and budgets outside unverified engine behaviour.

## Producer self-check and handoff

Producer self-check of **oss-rerun-pack-r1**, not an independent verdict: reviewed exact claims and citations against the inspected cached passages; kept README assertions, package/config declarations, static branch predictions and proposed tests distinct. Reconciled ≥3.10 versus selected 3.11 without calling it a proved incompatibility. Preserved the exception-helper qualification, counter units, post-work enforcement, environment precedence and unexecuted state/helper assumptions. Kept top-level MIT scope separate from transitive rights. No stars, leaderboard position or single commit was used as security assurance.

Support: C1 qualified; C2 documentary/static facts supported with runtime gap; C3 text supported with scope qualification; C4–C5 static findings supported with runtime consequences conditional. Open gaps: actual install/provider behaviour, full dependency/rights resolution, auth implementation, helpers/prompts/state, source-control and provenance fidelity, runtime error visibility and budget enforcement. No independent or specialist reviewer result exists in this report; no verdict is manufactured.

Stopping reason: the bounded candidate-assessment question is answered with explicit limitations and a discriminating next step; further execution is outside scope. Report written only to `benchmarks/progressive/packs/oss/rerun/pack.md` for requester review; no external publication or deployment. Refresh affected claims if the target revision, selected environment, adapter requirements or actual test evidence changes.
