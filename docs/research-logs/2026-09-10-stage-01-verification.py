#!/usr/bin/env python3
"""Check Stage 1 documentation; this is not a research-quality benchmark.

Run from the repository root:
    python3 docs/research-logs/2026-09-10-stage-01-verification.py

A connector-only workspace may contain only the new files. Baseline link
existence is then checked against the explicitly inspected remote tree below.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
LOG = "docs/research-logs/2026-09-10-stage-01-project-goal-and-boundary.md"
REPORT = "docs/research-logs/2026-09-10-stage-01-verification.json"
BASELINE_COMMIT = "80b209968b366662c01a8ded5ecb6c30bb6beb0b"
BASELINE = {
    "README.md": "bf998f74284b23bdc844b46182ec637b67391948",
    "docs/research-logs/README.md": "e3b4e986caea3914fdf0f1ee67de407fafc53f0c",
    "docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md": "8ff62c92bada2861ece3684a9e73a83da75d9d94",
}
EXPECTED_OUTPUTS = [
    "1. Project charter",
    "2. Boundary map",
    "3. Intended user and use-case map",
    "4. Quality definition and sufficient evidence",
    "5. Human decision points",
    "6. Non-goals",
]
EXPECTED_CLASSES = [
    "Fact finding", "Landscape research", "Comparative research",
    "Case-study research", "Evidence synthesis", "Trend research",
    "Source verification", "Research updates / refreshes",
]

def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    text = (ROOT / LOG).read_text(encoding="utf-8")
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, evidence: object) -> None:
        checks.append({"check": name, "result": "PASS" if passed else "FAIL", "evidence": evidence})

    outputs = re.findall(r"^## (\d\. .+)$", text, flags=re.MULTILINE)
    check("six required output responsibilities", outputs == EXPECTED_OUTPUTS, outputs)
    classes = re.findall(r"^\| C\d+ \| ([^|]+?) \|", text, flags=re.MULTILINE)
    check("eight original research classes, each once", classes == EXPECTED_CLASSES, classes)
    conformance = text.split("## Verification and conformance", 1)[1]
    ids = re.findall(r"^\| (R\d{2}) .+ \| PASS \|$", conformance, flags=re.MULTILINE)
    check("every extracted requirement has a PASS conformance row", ids == [f"R{i:02d}" for i in range(1, 16)], ids)
    sources = re.findall(r"^\| (F[1-8]) \|", text, flags=re.MULTILINE)
    check("all eight governing family inputs recorded", sources == [f"F{i}" for i in range(1, 9)], sources)
    check("governing source and approved baseline identified", BASELINE_COMMIT in text and BASELINE[next(p for p in BASELINE if p.endswith("process.md"))] in text, BASELINE_COMMIT)

    # Report is an output of this check, so its target is explicitly permitted.
    known = set(BASELINE) | {REPORT}
    known.update(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file())
    targets: list[dict[str, object]] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "#")):
            continue
        filepart = unquote(target.split("#", 1)[0])
        path = str(PurePosixPath(LOG).parent / filepart)
        targets.append({"target": target, "path": path, "exists_in_local_or_inspected_remote_tree": path in known})
    check("relative documentation file targets resolve", all(x["exists_in_local_or_inspected_remote_tree"] for x in targets), targets)

    current = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts}
    expected_delta = {
        LOG, REPORT,
        "docs/research-logs/2026-09-10-stage-01-verification.py",
        "docs/research-logs/bootstrap-progress.md",
    }
    actual_delta = (set(current) - set(BASELINE)) | {REPORT}
    check("exact Stage 1 repository delta, with no premature surfaces", actual_delta == expected_delta, {"expected": sorted(expected_delta), "actual": sorted(actual_delta)})
    baseline_checks = []
    for path, expected in BASELINE.items():
        if (ROOT / path).is_file():
            actual = git_blob((ROOT / path).read_bytes())
            baseline_checks.append({"path": path, "expected": expected, "actual": actual})
    if baseline_checks:
        check("locally available baseline files are unchanged", all(x["expected"] == x["actual"] for x in baseline_checks), baseline_checks)
    failures = [x for x in checks if x["result"] == "FAIL"]
    report = {
        "stage": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "basis": "Original bootstrap section 7; semantic review is recorded separately in the stage log.",
        "baseline_commit": BASELINE_COMMIT,
        "local_baseline_files_checked": baseline_checks,
        "remote_baseline_verification_required": True,
        "checked_log_git_blob": git_blob((ROOT / LOG).read_bytes()),
        "checks": checks,
        "summary": {"passed": len(checks) - len(failures), "failed": len(failures)},
        "limitations": [
            "No container clone or internet access was available; remote source inspection used the GitHub connector.",
            "This checks documentation structure and traceability, not professional research behaviour, external installation or benchmarks.",
            "Remote branch, parent, tree and blob verification must follow the commit; this report does not claim that later action has happened.",
            "External link content and the original heading anchor were inspected through the connector, not network-tested by this script.",
        ],
    }
    (ROOT / REPORT).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
