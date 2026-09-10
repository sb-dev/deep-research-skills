#!/usr/bin/env python3
"""Validate the Stage 2 snapshot; not an agent/research-quality benchmark.
Run from that snapshot: python3 docs/research-logs/2026-09-10-stage-02-verification.py
Add --negative-controls to execute three mutations, restore, then validate again.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "docs/research-logs"
PREFIX = "2026-09-10-stage-02-"
NAMES = ["professional-practice", "method-comparison", "glossary", "failure-taxonomy", "quality-dimensions", "sources"]
M_NAMES = ["Systematic and scoping reviews", "Research synthesis", "Market and competitive intelligence", "Technology landscape research", "Investigative and OSINT research", "Journalistic verification", "Analytical tradecraft", "Policy and decision support research", "Historical and archival research"]
D_NAMES = ["Roles", "Terminology", "Research protocols", "Source discovery", "Inclusion and exclusion", "Source appraisal", "Evidence extraction", "Deduplication", "Triangulation", "Contradiction handling", "Uncertainty", "Analysis and synthesis", "Review and QA", "Reporting", "Update behaviour", "Failure modes", "Repair strategies"]
BASELINE = {
 "README.md": "bf998f74284b23bdc844b46182ec637b67391948",
 "docs/research-logs/README.md": "e3b4e986caea3914fdf0f1ee67de407fafc53f0c",
 "docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md": "8ff62c92bada2861ece3684a9e73a83da75d9d94",
 "docs/research-logs/2026-09-10-stage-01-project-goal-and-boundary.md": "5ed2d242400486be81d0acc3f371c4564873012e",
 "docs/research-logs/2026-09-10-stage-01-verification.py": "777146e7273db7f05043b0f8b70db3429975677f",
 "docs/research-logs/2026-09-10-stage-01-verification.json": "8516b3234363346d06062883d31aad6cd6e9da3d",
}
EXPECTED = {f"docs/research-logs/{PREFIX}{n}.md" for n in NAMES} | {f"docs/research-logs/{PREFIX}verification.py", f"docs/research-logs/{PREFIX}verification.json", "docs/research-logs/bootstrap-progress.md"}
REPORT = DIR / f"{PREFIX}verification.json"

def blob(data: bytes) -> str:
 return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def assess() -> list[dict]:
 checks = []
 def record(name, ok, detail):
  checks.append({"check": name, "result": "PASS" if ok else "FAIL", "evidence": detail})
 texts = {n: (DIR / f"{PREFIX}{n}.md").read_text() if (DIR / f"{PREFIX}{n}.md").is_file() else "" for n in NAMES}
 record("five complete output files plus source register", all(texts.values()), {n: len(s) for n,s in texts.items()})
 profiles = re.split(r"^## M(\d): (.+)$", texts["method-comparison"], flags=re.M)
 headings = [(profiles[i], profiles[i+1]) for i in range(1, len(profiles), 3)]
 record("exact nine named traditions", headings == [(str(i),n) for i,n in enumerate(M_NAMES,1)], headings)
 dims = {}
 good = len(headings) == 9
 for i in range(1,len(profiles),3):
  rows = re.findall(r"^\| (D\d{2}) \| ([^|]+?) \| (.+) \|$", profiles[i+2], flags=re.M)
  dims[f"M{profiles[i]}"] = len(rows)
  good &= [(r[0],r[1]) for r in rows] == [(f"D{k:02}",n) for k,n in enumerate(D_NAMES,1)]
  good &= all(re.search(r"\b[EA]:",r[2]) and re.search(r"\bS\d{2}\b",r[2]) for r in rows)
 record("all 153 dimension cells with evidence/adaptation labels and sources", good, dims)
 questions = re.findall(r"^### (Q\d):", texts["professional-practice"], flags=re.M)
 record("seven governing questions answered", questions == [f"Q{i}" for i in range(1,8)], questions)
 sources = re.findall(r"^## (S\d{2})$", texts["sources"], flags=re.M)
 sections = re.split(r"^## S\d{2}$", texts["sources"], flags=re.M)[1:]
 record("42 source entries retain URL, inspected scope and access limits", sources == [f"S{i:02}" for i in range(1,43)] and all(all(x in s for x in ("Source:", "Inspected scope:", "Access and limits:")) and "https://" in s for s in sections), sources)
 unknown = sorted(set(re.findall(r"\bS\d{2}\b", "\n".join(texts.values()))) - set(sources))
 record("all cited source identifiers resolve", not unknown, unknown)
 counts = {}
 for name,letter,expected in (("failure-taxonomy","F",20),("quality-dimensions","K",16)):
  ids = re.findall(rf"^\| ({letter}\d{{2}}) \|",texts[name],flags=re.M)
  counts[name] = len(ids)
  record(f"declared {name} inventory complete", ids == [f"{letter}{i:02}" for i in range(1,expected+1)], ids)
 terms = [x for x in texts["glossary"].splitlines() if x.startswith("| ")][1:]
 record("declared 32-term glossary complete", len(terms) == 32, len(terms))
 conf = texts["professional-practice"].split("## Conformance review",1)[-1]
 ids = re.findall(r"^\| (R\d{2}) .+ \| PASS \|$",conf,flags=re.M)
 record("all fourteen semantic conformance entries recorded", ids == [f"R{i:02}" for i in range(1,15)],ids)
 files = {p.relative_to(ROOT).as_posix():p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts}
 actual_delta = (set(files)-set(BASELINE)) | {REPORT.relative_to(ROOT).as_posix()}
 record("exact research-log-only Stage 2 delta", actual_delta == EXPECTED, {"expected":sorted(EXPECTED),"actual":sorted(actual_delta)})
 target_results = []
 for n,text in list(texts.items()) + [("bootstrap-progress", (DIR/"bootstrap-progress.md").read_text() if (DIR/"bootstrap-progress.md").exists() else "")]:
  for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)",text):
   if target.startswith(("http://","https://","#")):continue
   resolved=(DIR/unquote(target.split("#",1)[0])).resolve()
   try: relative=resolved.relative_to(ROOT).as_posix()
   except ValueError: relative="OUTSIDE_ROOT"
   target_results.append({"from":n,"target":target,"found":relative in set(files)|set(BASELINE)|EXPECTED})
 record("relative file links resolve locally or in inspected baseline", all(t["found"] for t in target_results),target_results)
 table_errors=[]
 table_count=0
 for name,text in texts.items():
  columns=None
  for number,line in enumerate(text.splitlines(),1):
   if line.startswith("|"):
    width=len(re.split(r"(?<!\\)\|",line))-2
    if columns is None:columns=width;table_count+=1
    if width!=columns:table_errors.append({"file":name,"line":number,"expected":columns,"actual":width})
   else:columns=None
 record("Markdown table columns are consistent", table_count>0 and not table_errors, {"tables":table_count,"errors":table_errors})
 observed={p:blob(files[p].read_bytes()) for p in BASELINE if p in files}
 if observed:
  record("locally present accepted files are unchanged", all(BASELINE[p]==h for p,h in observed.items()), observed)
 return checks

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument("--negative-controls",action="store_true")
 args=parser.parse_args()
 negative=[]
 if args.negative_controls:
  path=DIR/f"{PREFIX}method-comparison.md"
  original=path.read_bytes()
  mutations=[("missing dimension", lambda s:re.sub(r"^\| D17 .+\n","",s,count=1,flags=re.M),"all 153 dimension cells with evidence/adaptation labels and sources"),("unknown source",lambda s:s.replace("[S05]","[S99]",1),"all cited source identifiers resolve")]
  try:
   for name,fn,expected in mutations:
    path.write_text(fn(original.decode()))
    failed=[c["check"] for c in assess() if c["result"]=="FAIL"]
    negative.append({"mutation":name,"expected_failure":expected,"actual_failures":failed,"result":"PASS" if expected in failed else "FAIL"})
    path.write_bytes(original)
  finally:path.write_bytes(original)
  rogue=ROOT/"skills/unjustified-stage-02.txt"
  if rogue.exists():raise RuntimeError("Refusing to overwrite negative-control path")
  created_dir=not rogue.parent.exists()
  try:
   rogue.parent.mkdir(exist_ok=True);rogue.write_text("synthetic validator negative control\n")
   failed=[c["check"] for c in assess() if c["result"]=="FAIL"]
   expected="exact research-log-only Stage 2 delta"
   negative.append({"mutation":"premature production file","expected_failure":expected,"actual_failures":failed,"result":"PASS" if expected in failed else "FAIL"})
  finally:
   rogue.unlink(missing_ok=True)
   if created_dir:rogue.parent.rmdir()
 checks=assess()
 failed=[c for c in checks+negative if c["result"]=="FAIL"]
 report={"stage":2,"generated_at":datetime.now(timezone.utc).isoformat(),"basis":"Original bootstrap section 8; substantive review in professional-practice log.","parent_revision":"650207611ac2ad0e7f988df530f85317573026ae","checks":checks,"negative_controls":negative,"summary":{"passed":sum(c["result"]=="PASS" for c in checks),"failed":sum(c["result"]=="FAIL" for c in checks),"negative_controls_passed":sum(c["result"]=="PASS" for c in negative)},"checked_file_blobs":{p:blob((ROOT/p).read_bytes()) for p in sorted(EXPECTED) if (ROOT/p).is_file() and (ROOT/p)!=REPORT},"limitations":["Document structure, inventory and reference checks are not empirical research-quality or installed-agent benchmarks.","Full source access and semantic support are assessed in the source register and manual conformance review, not proven by this script.","No container clone/network validation is claimed; known baseline links and unchanged accepted files require remote tree verification before progression. Unmounted baseline files are not counted as locally verified.","Run against this historical stage snapshot, not a later repository with subsequent stages."]}
 REPORT.write_text(json.dumps(report,indent=2)+"\n")
 print(json.dumps(report["summary"]))
 if failed:raise SystemExit(1)

if __name__=="__main__":main()
