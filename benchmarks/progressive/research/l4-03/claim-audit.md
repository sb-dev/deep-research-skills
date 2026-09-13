# L4-03 — Cross-source claim audit, producer r2

This is producer analysis of two explicit claims. Separate parent diagnosis is at evaluation/diagnosis.md; separate final audit remains parent-owned.

## C1 — “Playwright CLI and Playwright MCP independently validate two browser engines”

**Rejected. Narrow supported claim:** the two repositories expose different CLI/MCP interfaces and declare the same underlying Playwright engine dependencies at the inspected refs.

The [CLI README](https://github.com/microsoft/playwright-cli/blob/655530f6d0dc71a0d6bf46ae165877d3c7311099/README.md#L1-L11) and [MCP README](https://github.com/microsoft/playwright-mcp/blob/8a13ef8e9f7385a0f89477922127f31cbfde9761/README.md#L1-L15) explicitly frame their interface roles. [CLI package dependencies](https://github.com/microsoft/playwright-cli/blob/655530f6d0dc71a0d6bf46ae165877d3c7311099/package.json#L24-L30) and [MCP package dependencies](https://github.com/microsoft/playwright-mcp/blob/8a13ef8e9f7385a0f89477922127f31cbfde9761/package.json#L39-L42) both identify playwright and playwright-core at 1.63.0-alpha-2026-08-31. Four files therefore describe two interfaces sharing an implementation dependency, not four independent measurements or two independent browser implementations.

Evidence support is static package/maintainer documentation. It does not prove identical runtime code paths, installed package bytes, failure rates, token efficiency or equal feature coverage. No new engine repository or performance benchmark was followed. Relevant consequence: choose interface on integration needs and audit shared-engine failure conditions once while retaining interface-specific tests.

## C2 — “Locally run research and evaluation tools keep all prompts and evidence local”

**Rejected as a universal claim.** This is the most material unresolved first-pass claim because a mistaken privacy interpretation could change which data is eligible for processing.

Open Deep Research's [README configuration](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/README.md#L64-L79) describes OpenAI model defaults and Tavily search. Promptfoo's [README](https://github.com/promptfoo/promptfoo/blob/7b404ae0492a4f19e3fa406ab3c9c77109dce278/README.md#L29-L47) requires provider credentials for most models, while its [privacy feature wording](https://github.com/promptfoo/promptfoo/blob/7b404ae0492a4f19e3fa406ab3c9c77109dce278/README.md#L75-L81) says prompts never leave the machine. These are first-party configuration/marketing statements, not independent observed privacy tests.

**Targeted follow-up performed:** fetch only Promptfoo's pinned [src/providers/openai/chat.ts](https://github.com/promptfoo/promptfoo/blob/7b404ae0492a4f19e3fa406ab3c9c77109dce278/src/providers/openai/chat.ts#L460-L484). Its callApi request path invokes fetchWithCache with POST to appendOpenAiApiPath(this.getApiUrl(), 'chat/completions'), JSON request body, optional bearer authorization, request timeout and retry configuration. The file constructs model messages in the request body earlier in the method. This substantiates a provider HTTP processing path, not a universal local-only boundary.

Reconciled interpretation: the harness can run locally; data residency depends on selected model/retriever/endpoint, request contents and storage/telemetry settings. The source contradiction is retained rather than silently rewriting the README. The follow-up resolves the universal-claim rejection, **not** a full audit of all local providers, endpoints, telemetry, caches, model assets or deployments. No actual private-data transfer or runtime leak was observed; no all-local configuration was tested. Adopt only after an explicit processor inventory and authorised outbound-traffic test.

## D1 — GROBID documentation locator repair

The first-pass [README.md locator](https://github.com/grobidOrg/grobid/blob/befaa302d2336aae83971d4700b25de02144109a/README.md) returned GitHub NOT_FOUND/404, while same-SHA metadata and build.gradle succeeded. This was access failure, not negative evidence about GROBID capability. The frozen provisional package records that distinction.

A same-ref root-directory read identified [Readme.md](https://github.com/grobidOrg/grobid/blob/befaa302d2336aae83971d4700b25de02144109a/Readme.md); a subsequent direct file read succeeded. Its description at line 19 establishes the documented scholarly PDF-to-XML/TEI role; [build.gradle](https://github.com/grobidOrg/grobid/blob/befaa302d2336aae83971d4700b25de02144109a/build.gradle#L153-L158) provides the original Java toolchain configuration, and its application block at 414–421 defines the service entry point. The GROBID documentary coverage gap is repaired at the same source revision; extraction fidelity remains unexecuted.

No other repository support record or C1 finding changed. C2 was independently narrowed by its provider follow-up. See change-record.md for preserved inputs and affected rechecks.

