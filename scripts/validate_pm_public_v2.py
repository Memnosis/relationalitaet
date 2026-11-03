#!/usr/bin/env python3
"""Check that the active project-management website uses a redacted public view."""
import json,sys
from pathlib import Path
r=Path(__file__).resolve().parents[1]
d=json.loads((r/"docs/data/projektmanagement-public-v2.json").read_text(encoding="utf-8"))
old=json.loads((r/"docs/data/projektmanagement-v1.json").read_text(encoding="utf-8"))
errors=[]
if d.get("schema_version")!="pm-public-curated/0.2":errors.append("unsupported public PM schema")
if len(d.get("tasks",[]))+d["internal_summary"]["count"]!=len(old["tasks"]):errors.append("public + aggregate must reconcile to source")
if any(t.get("owner")=="claude" for t in d["tasks"]):errors.append("internal Claude task leaked as individual card")
if any(t.get("meta_prompt") for t in d["tasks"]):errors.append("raw prompt present")
ids={t["id"] for t in d["tasks"]}
if len(ids)!=len(d["tasks"]):errors.append("duplicate public tasks")
for t in d["tasks"]:
    if any(x not in ids for x in (t.get("requires",[])+t.get("enables",[]))):errors.append("private task ID referenced by "+t["id"])
    for k,v in t.get("stage_evidence",{}).items():
        if v.get("path") and not (r/v["path"]).is_file():errors.append(t["id"]+" broken stage evidence "+k)
source=old["tasks"]
if {x["id"] for x in d["tasks"]}!={x["id"] for x in source if x.get("owner")!="claude"}:errors.append("public task loss")
print("PM public v2:",len(d["tasks"]),"public task cards;",d["internal_summary"]["count"],"aggregated internal")
for e in errors:print("ERROR:",e)
if errors:sys.exit(1)
print("PASS static public-task separation; this does not make old Git history private")
