#!/usr/bin/env python3
"""Tensor website observer: static repository and PM consistency checks."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DOCS=ROOT/"docs"
ERRORS=[]; METRICS={}
pages=sorted(DOCS.glob("*.html"))
METRICS["pages"]=len(pages)
METRICS["token_pages"]=0
METRICS["visual_pages"]=0
for p in pages:
 s=p.read_text(encoding="utf-8")
 if re.search(r"courseware|Forschungs-Forschungsplattform",s,re.I):ERRORS.append(f"{p.name}: prohibited editorial text")
 if len(re.findall(r"<h1\b",s))!=1:ERRORS.append(f"{p.name}: requires exactly one h1")
 if "<main" not in s:ERRORS.append(f"{p.name}: missing main landmark")
 METRICS["token_pages"]+=("tensor-design.css" in s)
 METRICS["visual_pages"]+=bool(re.search(r"<svg\b|<img\b|mermaid",s,re.I))
 for rel in re.findall(r'''(?:href|src)=[\"'](\./[^"'#]+)''',s):
  target=(p.parent/rel).resolve()
  if not target.is_file():ERRORS.append(f"{p.name}: missing {rel}")
tasks=json.loads((ROOT/"forschung/minimal-ki/beobachter-v0_1/TASKKARTEN.json").read_text(encoding="utf-8"))["tasks"]
METRICS["tasks"]=len(tasks)
ids=[x["id"] for x in tasks]
if len(ids)!=len(set(ids)):ERRORS.append("duplicate task IDs")
for t in tasks:
 for field in ("id","goal","status","milestone_id","meta_prompt","reference_urls","definition_of_done","acceptance"):
  if not t.get(field):ERRORS.append(f"{t.get('id','?')}: missing {field}")
 for url in t.get("reference_urls",[]):
  if not url.startswith("https://"):ERRORS.append(f"{t['id']}: non-absolute source URL")
  if url not in t.get("meta_prompt",""):ERRORS.append(f"{t['id']}: source URL not copied in prompt")
print(json.dumps({"metrics":METRICS,"errors":ERRORS,"result":"PASS" if not ERRORS else "FAIL"},ensure_ascii=False,indent=2))
sys.exit(1 if ERRORS else 0)
