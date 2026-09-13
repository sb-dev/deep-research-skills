# L5-03 handoff to Software Engineering — R1 stable, 2026-09-13

**Decision to retain:** a small traceable-record prototype is plausible; production reliability is unproven. Read [research.md](research.md) C03/C06–C09/C13. Producer review only; independent evaluation pending. No implementation, paid API or deployment commitment is authorised by this handoff.

Minimum proposed records: source URL/version/observed date/access/rights; evidence passage or page/context/transformation; claim text/support/counterevidence/uncertainty; reviewer and exact brief revision. Keep source identity separate from proposition support. A dependency list can map one source to affected claims and handoffs. Preserve failed reads as failed and unresolved claims as unresolved.

Sources provide building blocks, not a complete verified system: PROV for provenance, Annotation selectors for locators, conditional HTTP requests for representation checks. A changed ETag does not say which claims changed; an unchanged representation does not prove truth. Rights may favour locators over stored text; offsets can break under edits. Auto-sync documented for Drive (C03) does not prove safe claim-level refresh.

Proposed engineering experiment: two claims on different originals, with one later original or correction introduced; read prior state, record exact delta, reopen dependent claim/review, and confirm the unrelated record is byte-identical. Distinguish a real observed delta from a synthetic injection and record failures. Add a lost-locator case before production. Success requires no silent stale claim, explicit unknowns and preserved context; no benchmark score is promised. The research package's AP update exercises this manually only.

Return to Business total labour/maintenance uncertainty and to Editorial original locators, scope of affected claims and source-use restrictions. You own storage, parsers, access control, tests, operations and failure recovery. Prefer the simplest local record representation until a real need justifies a service or engine.
