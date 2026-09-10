#!/usr/bin/env python3
"""Executable design checks for synthetic, labelled research cases.

This is a bounded reference scorer, not a browsing agent, installed skill,
statistical benchmark or general natural-language entailment implementation.
All mock source facts and response specimens below are explicitly synthetic.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Callable

STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT APPLICABLE"}
LAYERS = ("retrieval", "evidence", "citations", "synthesis")


def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def at(value: dict, path: str) -> Any:
    for part in path.split("."):
        value = value[part]
    return value


def score(case: dict, submitted: dict) -> dict:
    """Derive criterion verdicts from fixed inputs, never expected_bad labels."""
    results = {}
    for rule in case["rules"]:
        try:
            observed = at(submitted, rule["path"])
            reference = at(case["input"], rule["reference"])
            op = rule["op"]
            if op == "equal":
                ok = observed == reference
            elif op == "covers":
                ok = set(reference).issubset(set(observed))
            elif op == "origin-count":
                ok = observed == len(set(reference))
            elif op == "entails-field":
                # Exact typed field semantics in this fixture only. No claim to
                # recognise arbitrary paraphrases, causality or real-world truth.
                source = case["input"]["sources"].get(observed["source_id"])
                if source is None:
                    raise KeyError("unknown citation source")
                ok = (observed["field"] == reference["field"]
                      and source["facts"].get(observed["field"]) == reference["value"])
            elif op == "unchanged":
                ok = all(digest(observed[k]) == digest(v) for k, v in reference.items())
            elif op == "no-extra-collection":
                ok = not reference or observed == 0
            elif op == "capacity":
                ok = all(observed.get(k, float("inf")) <=
                         v["ceiling"] - v["consumed"] - v["outstanding"] - v["finalisation"]
                         for k, v in reference.items())
            else:
                raise ValueError(f"unknown operator: {op}")
            results[rule["id"]] = {"layer": rule["layer"], "status": "PASS" if ok else "FAIL",
                                   "basis": f'{op}: submitted.{rule["path"]} against input.{rule["reference"]}'}
        except KeyError as error:
            results[rule["id"]] = {"layer": rule["layer"], "status": "FAIL",
                                   "basis": f"Missing required submission/reference: {error}"}
    return results


def fixture(case_id: str, goal: str, layer: str, op: str, fixed: Any,
            good: Any, bad: Any, owner: str, *, sources: dict | None = None) -> dict:
    return {"id": case_id, "kind": "synthetic", "goal": goal,
            "input": {"reference": fixed, **({"sources": sources} if sources else {})},
            "rules": [{"id": case_id + ".1", "layer": layer, "op": op,
                       "path": "observed", "reference": "reference"}],
            "good": {"observed": good}, "bad": {"observed": bad},
            "repair_owner": owner}


FIXTURES = [
    fixture("FX01", "Three syndicated articles share one original observation; do not count three origins.",
            "evidence", "origin-count", ["study-A", "study-A", "study-A"], 1, 3, "analyse-evidence"),
    fixture("FX02", "Mock snippet says supported; inspected full passage says unsupported. Preserve negation.",
            "evidence", "equal", {"support": False, "access": "full"},
            {"support": False, "access": "full"}, {"support": True, "access": "full"}, "extract-evidence"),
    fixture("FX03", "Current official rule supersedes an old rule for the requested effective period.",
            "temporal", "equal", {"effective": "2026-07-01", "value": 12},
            {"effective": "2026-07-01", "value": 12}, {"effective": "2025-01-01", "value": 26}, "refresh"),
    fixture("FX04", "High-ranked SEO lead does not fulfil the required original-document acquisition.",
            "retrieval", "covers", ["official-original"], ["seo-lead", "official-original"], ["seo-lead"], "follow-up-search"),
    fixture("FX05", "Retraction notice makes unqualified reliance on the withdrawn finding unacceptable.",
            "evidence", "equal", {"status": "retracted", "reliance": "withheld"},
            {"status": "retracted", "reliance": "withheld"}, {"status": "active", "reliance": "unqualified"}, "analyse-evidence"),
    fixture("FX06", "Two supplementary reports describe one study and both may be retained.",
            "evidence", "equal", {"reports": ["r1", "r2"], "studies": ["study-A"]},
            {"reports": ["r1", "r2"], "studies": ["study-A"]},
            {"reports": ["r1", "r2"], "studies": ["study-A", "study-B"]}, "analyse-evidence"),
    fixture("FX07", "Only a secondary account is accessible; do not declare the paywalled original inspected.",
            "evidence", "equal", {"basis": "secondary-attribution", "original_inspected": False},
            {"basis": "secondary-attribution", "original_inspected": False},
            {"basis": "primary-verification", "original_inspected": True}, "extract-evidence"),
    fixture("FX08", "Two eligible high-quality sources disagree; preserve the unresolved dispute.",
            "evidence", "covers", ["support-A", "contrary-B"], ["support-A", "contrary-B"], ["support-A"], "analyse-evidence"),
    fixture("FX09", "An observational association cannot become an unconditional causal guarantee.",
            "synthesis", "equal", {"claim_type": "association", "uncertainty": "causal effect not established"},
            {"claim_type": "association", "uncertainty": "causal effect not established"},
            {"claim_type": "causal-guarantee", "uncertainty": "none"}, "synthesise"),
    fixture("FX10", "A valid source identity for an adjacent field does not entail the actual claim.",
            "citations", "entails-field", {"field": "package_python", "value": ">=3.10"},
            {"source_id": "S1", "field": "package_python"}, {"source_id": "S1", "field": "server_python"}, "synthesise",
            sources={"S1": {"facts": {"package_python": ">=3.10", "server_python": "3.11"}}}),
    fixture("FX11", "A long report answering Q1 must not omit required Q2.",
            "synthesis", "covers", ["Q1", "Q2"], ["Q1", "Q2"], ["Q1"], "analyse-evidence"),
    fixture("FX12", "After evidence and review are sufficient, stop optional duplicate collection.",
            "retrieval", "no-extra-collection", True, 0, 4, "follow-up-search"),
    fixture("TM02", "Publication precedes effective date; an announcement is not early implementation.",
            "temporal", "equal", {"published": "2026-05-01", "effective": "2026-07-01", "as_of": "2026-06-01", "operative": "old"},
            {"published": "2026-05-01", "effective": "2026-07-01", "as_of": "2026-06-01", "operative": "old"},
            {"published": "2026-05-01", "effective": "2026-05-01", "as_of": "2026-06-01", "operative": "new"}, "refresh"),
    fixture("TM03", "A changed current-price claim does not invalidate a stable historical release claim.",
            "preservation", "unchanged", {"historical": {"value": "released in 2024", "basis": "snapshot-A"}},
            {"historical": {"value": "released in 2024", "basis": "snapshot-A"}, "current": {"value": 12}},
            {"historical": {"value": "released in 2026", "basis": "new retrieval date"}, "current": {"value": 12}}, "refresh"),
    fixture("BG01", "Aggregate outstanding work and finalisation reserves constrain every resource dimension.",
            "authority-budget", "capacity", {"calls": {"ceiling": 10, "consumed": 3, "outstanding": 2, "finalisation": 2},
                                             "bytes": {"ceiling": 100, "consumed": 20, "outstanding": 30, "finalisation": 10}},
            {"calls": 3, "bytes": 40}, {"calls": 4, "bytes": 40}, "follow-up-search"),
    fixture("BG02", "Low yield cannot close a known decisive unresolved evidence gap.",
            "retrieval", "equal", "targeted-follow-up", "targeted-follow-up", "stop-sufficient", "follow-up-search"),
    fixture("PR01", "A corrected denominator must update its dependent claim while preserving another record.",
            "preservation", "equal", {"denominator": 20, "share": 0.5, "claim": "half of recorded cases", "unaffected": "U1"},
            {"denominator": 20, "share": 0.5, "claim": "half of recorded cases", "unaffected": "U1"},
            {"denominator": 20, "share": 1.0, "claim": "all recorded cases", "unaffected": "U1"}, "refresh"),
    fixture("AU01", "A reported success is not independent assurance when the required reviewer did not run.",
            "authority-budget", "equal", {"review_kind": "producer-self-check", "independent_review": "BLOCKED"},
            {"review_kind": "producer-self-check", "independent_review": "BLOCKED"},
            {"review_kind": "independent", "independent_review": "PASS"}, "audit"),
]


def package_errors(package: dict) -> list[str]:
    errors = []
    if not package.get("question"):
        errors.append("required-metadata")
    ids = [s.get("id") for s in package.get("sources", [])]
    if None in ids or len(ids) != len(set(ids)):
        errors.append("source-identity")
    for source in package.get("sources", []):
        try:
            date.fromisoformat(source["retrieved_at"])
        except (KeyError, TypeError, ValueError):
            errors.append("timestamp")
    for citation in package.get("citations", []):
        if citation.get("source_id") not in ids:
            errors.append("missing-source")
        if not citation.get("locator"):
            errors.append("citation-target")
    for path in package.get("bundled_paths", []):
        p = PurePosixPath(path.replace("\\", "/"))
        if p.is_absolute() or ".." in p.parts or not path or ":" in path:
            errors.append("self-containment")
    if not set(package.get("claim_refs", [])).issubset(set(ids)):
        errors.append("claim-reference")
    return sorted(set(errors))


def choose_pack(requested: str | None, available: list[str], *, explicit_disabled=False,
                locked: str | None = None, reopen=False, compatible=True, safe_paths=True) -> str:
    if not safe_paths:
        return "BLOCKED:unsafe-package"
    if explicit_disabled:
        return "core"
    if requested is None:
        return "core"
    if locked is not None and locked != requested and not reopen:
        return "BLOCKED:locked-decision"
    if requested not in available or not compatible:
        return "BLOCKED:unavailable-or-incompatible"
    return requested


def acceptance(verdicts: list[dict], required: set[str]) -> str:
    """Missing mandatory criterion never becomes an overall PASS."""
    by_id = {v["id"]: v for v in verdicts}
    if len(by_id) != len(verdicts):
        return "FAIL"
    if any(v.get("status") not in STATUSES for v in verdicts):
        return "FAIL"
    if any(v.get("status") == "NOT APPLICABLE" and not v.get("reason") for v in verdicts):
        return "FAIL"
    if any(by_id.get(key, {}).get("status") == "FAIL" for key in required):
        return "FAIL"
    if any(key not in by_id or by_id[key]["status"] == "BLOCKED" for key in required):
        return "BLOCKED"
    return "PASS"


def run() -> dict:
    original = digest(FIXTURES)
    result = {"stage": 13, "kind": "executed synthetic design/reference-scorer checks; not agent performance",
              "checked_at": datetime.now(timezone.utc).isoformat(), "fixtures_sha256": original,
              "priority_cases": [], "additional_cases": [], "orthogonality": [],
              "package_controls": [], "pack_controls": [], "acceptance_controls": [], "scorer_mutation_controls": []}
    for case in FIXTURES:
        good = score(case, copy.deepcopy(case["good"]))
        bad = score(case, copy.deepcopy(case["bad"]))
        passed = all(v["status"] == "PASS" for v in good.values()) and any(v["status"] == "FAIL" for v in bad.values())
        entry = {"case": case["id"], "goal": case["goal"], "good": good, "bad": bad,
                 "result": "PASS" if passed else "FAIL"}
        result["priority_cases" if case["id"].startswith("FX") else "additional_cases"].append(entry)
    # Four deliberately isolated defects against one otherwise identical fixture.
    common = {"id": "ORTH", "kind": "synthetic", "input": {
        "required_queries": ["broad", "reformulated"], "origins": ["one", "one", "one"],
        "proposition": {"field": "limit", "value": 12}, "questions": ["Q1", "Q2"],
        "sources": {"S1": {"facts": {"limit": 12, "adjacent": 99}}}},
        "rules": [{"id": "R", "layer": "retrieval", "op": "covers", "path": "queries", "reference": "required_queries"},
                  {"id": "E", "layer": "evidence", "op": "origin-count", "path": "origins", "reference": "origins"},
                  {"id": "C", "layer": "citations", "op": "entails-field", "path": "citation", "reference": "proposition"},
                  {"id": "S", "layer": "synthesis", "op": "covers", "path": "answers", "reference": "questions"}]}
    good = {"queries": ["broad", "reformulated"], "origins": 1,
            "citation": {"source_id": "S1", "field": "limit"}, "answers": ["Q1", "Q2"]}
    mutations = [("retrieval", "queries", ["broad", "broad"]), ("evidence", "origins", 3),
                 ("citations", "citation", {"source_id": "S1", "field": "adjacent"}), ("synthesis", "answers", ["Q1"])]
    for layer, key, value in mutations:
        damaged = copy.deepcopy(good); damaged[key] = value
        verdict = score(common, damaged)
        failures = [v["layer"] for v in verdict.values() if v["status"] == "FAIL"]
        result["orthogonality"].append({"mutation": layer, "observed_failed_layers": failures,
                                       "result": "PASS" if failures == [layer] else "FAIL"})
    package = {"question": "Synthetic question", "sources": [{"id": "S1", "retrieved_at": "2026-09-10"}],
               "citations": [{"source_id": "S1", "locator": "body/field"}], "claim_refs": ["S1"],
               "bundled_paths": ["SKILL.md", "references/evidence.md", "commands/audit.md"]}
    controls = [("required-metadata", "question", ""), ("source-identity", "sources", package["sources"] * 2),
                ("timestamp", "sources", [{"id": "S1", "retrieved_at": "2026-99-99"}]),
                ("missing-source", "citations", [{"source_id": "S9", "locator": "body"}]),
                ("citation-target", "citations", [{"source_id": "S1", "locator": ""}]),
                ("claim-reference", "claim_refs", ["S9"]),
                ("self-containment", "bundled_paths", ["../../docs/hidden.md"]),
                ("self-containment", "bundled_paths", ["/tmp/hidden.md"]),
                ("self-containment", "bundled_paths", ["..\\hidden.md"])]
    assert package_errors(package) == []
    for defect, key, value in controls:
        damaged = copy.deepcopy(package); damaged[key] = value
        observed = package_errors(damaged)
        result["package_controls"].append({"defect": defect, "input_field": key, "detected": observed,
                                           "result": "PASS" if defect in observed else "FAIL"})
    available = ["scholarly-evidence", "open-source-ecosystem"]
    for pack in available:
        other = available[1] if pack == available[0] else available[0]
        checks = [("requested", {"requested": pack}, pack), ("not-requested", {"requested": None}, "core"),
                  ("explicit-disabled", {"requested": pack, "explicit_disabled": True}, "core"),
                  ("locked-conflict", {"requested": pack, "locked": other}, "BLOCKED:locked-decision"),
                  ("explicit-reopen", {"requested": pack, "locked": other, "reopen": True}, pack),
                  ("incompatible", {"requested": pack, "compatible": False}, "BLOCKED:unavailable-or-incompatible"),
                  ("unsafe-path", {"requested": pack, "safe_paths": False}, "BLOCKED:unsafe-package"),
                  ("missing-package", {"requested": "not-installed"}, "BLOCKED:unavailable-or-incompatible")]
        for name, kwargs, expected in checks:
            observed = choose_pack(available=available, **kwargs)
            result["pack_controls"].append({"profile": pack, "case": name, "observed": observed,
                                           "expected": expected, "result": "PASS" if observed == expected else "FAIL"})
    acceptance_cases = [([], {"claims"}, "BLOCKED"),
                        ([{"id": "claims", "status": "PASS"}], {"claims", "citations"}, "BLOCKED"),
                        ([{"id": "claims", "status": "FAIL"}, {"id": "style", "status": "PASS"}], {"claims"}, "FAIL"),
                        ([{"id": "claims", "status": "NOT APPLICABLE"}], {"claims"}, "FAIL"),
                        ([{"id": "claims", "status": "PASS"}, {"id": "claims", "status": "PASS"}], {"claims"}, "FAIL"),
                        ([{"id": "claims", "status": "PASS"}], {"claims"}, "PASS")]
    for index, (verdicts, required, expected) in enumerate(acceptance_cases, 1):
        observed = acceptance(verdicts, required)
        result["acceptance_controls"].append({"case": f"AC{index:02}", "observed": observed,
                                             "expected": expected, "result": "PASS" if observed == expected else "FAIL"})
    for layer in LAYERS:
        # Mutated scorer drops FAIL in one layer. Known bad specimens must expose it.
        caught = 0
        for case in FIXTURES:
            bad = score(case, case["bad"])
            mutated = {k: {**v, "status": "PASS" if v["layer"] == layer else v["status"]} for k, v in bad.items()}
            if any(v["layer"] == layer for v in bad.values()) and all(v["status"] == "PASS" for v in mutated.values()):
                caught += 1
        result["scorer_mutation_controls"].append({"disabled_failure_layer": layer, "exposed_by_bad_cases": caught,
                                                   "result": "PASS" if caught > 0 else "FAIL"})
    result["input_preservation"] = "PASS" if digest(FIXTURES) == original else "FAIL"
    lists = ("priority_cases", "additional_cases", "orthogonality", "package_controls", "pack_controls", "acceptance_controls", "scorer_mutation_controls")
    result["counts"] = {key: len(result[key]) for key in lists}
    result["result"] = "PASS" if result["input_preservation"] == "PASS" and all(
        item["result"] == "PASS" for key in lists for item in result[key]) else "FAIL"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional new or explicitly selected result path")
    args = parser.parse_args()
    result = run()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(json.dumps({"result": result["result"], "counts": result["counts"], "input_preservation": result["input_preservation"]}))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
