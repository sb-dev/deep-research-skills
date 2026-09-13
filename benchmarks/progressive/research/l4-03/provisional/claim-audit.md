# Provisional r1 — frozen before repair

Source access: 36 GitHub connector reads, 0 searches. One latest-commit metadata record and README.md plus one code/configuration file attempted per each of the exact twelve repositories. 23 successful file representations, 12 commit records, one failed file locator.

Observed defect D1: https://github.com/grobidOrg/grobid/blob/befaa302d2336aae83971d4700b25de02144109a/README.md returned NOT_FOUND (GitHub API 404). The repository and revision exist: commit metadata and build.gradle succeeded. GROBID documentation support is unavailable through that locator; do not treat it as inspected.

Cross-source claim C1 under audit: Playwright CLI and Playwright MCP are separate access interfaces to shared Playwright browser capability, not two independent browser engines. Both package.json files declare playwright and playwright-core at 1.63.0-alpha-2026-08-31; corresponding READMEs distinguish CLI from MCP.

Cross-source claim C2 under audit: locally run research/evaluation tools keep all research data local. This is unsupported: Open Deep Research README configures hosted model and search APIs; Promptfoo README says prompts never leave the machine while also requiring model provider API keys. Targeted code follow-up is required before interpreting that privacy statement.

Repair boundary: D1 only affects GROBID documentary support and its map row; preserve the other eleven repository records. C2 follow-up is a separate evidence-gap operation, not a reason to regenerate unrelated evidence.
