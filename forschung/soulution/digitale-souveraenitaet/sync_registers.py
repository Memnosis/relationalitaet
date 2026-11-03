#!/usr/bin/env python3
"""Validate/rebuild Inkubator source atlas and shared reference crosswalk.
This is a deterministic registry sync, NOT an external API installation or run.
Usage: python forschung/soulution/digitale-souveraenitaet/sync_registers.py --check
       python forschung/soulution/digitale-souveraenitaet/sync_registers.py --write
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "forschung/soulution/digitale-souveraenitaet/INKUBATOR_QUELLENREGISTER_V1.json"
CROSSWALK = ROOT / "forschung/soulution/digitale-souveraenitaet/INKUBATOR_SKILL_API_SYNC_V1.json"
WEB = ROOT / "docs/data/inkubator-quellenregister.json"
SKILLS = ROOT / "forschung/soulution/shared/skills-v0.1.json"
TASKS = ROOT / "forschung/website/MITMACH_TASKS.json"
INC = ROOT / "forschung/soulution/digitale-souveraenitaet/SCHROEDINGERS_INKUBATOR_REGISTER_V01.json"

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def expected_web(src):
    keys=("id", "kind", "title", "url", "abstract", "topic",
          "source_read_status", "incubator_module_ids", "license_review",
          "implementation_status", "last_checked")
    return {
        "schema": src["schema"], "as_of": src["as_of"], "scope": src["scope"],
        "quality_policy": src["quality_policy"], "quality_counts": src["quality_counts"],
        "alias_map": src.get("alias_map", {}), "audit": src.get("audit", {}),
        "sources": [{k: item[k] for k in keys} for item in src["sources"]],
    }

def expected_crosswalk(src, old):
    out = json.loads(json.dumps(old))
    known = src["sources"]
    modmap = {m["module_id"]: m for m in out["modules"]}
    for mid, module in modmap.items():
        module["source_ids"] = [s["id"] for s in known if mid in s.get("incubator_module_ids", [])]
    kinds = {"identity", "federation", "workflows", "erp_framework", "security",
             "security_library", "reverse_engineering", "standard"}
    out["external_interface_candidates"] = [
        {"source_id": s["id"], "api_or_interface_name": s["title"], "source_url": s["url"],
         "type": s["kind"], "source_read_status": s["source_read_status"],
         "access_test": "not_run", "auth_test": "not_run", "license_test": "not_run",
         "version_pin": "missing", "status": "external_candidate"}
        for s in known if s["kind"] in kinds
    ]
    out["checks"]["source_count"] = len(known)
    out["checks"]["external_interface_candidates"] = len(out["external_interface_candidates"])
    out["checks"]["source_aliases"] = src.get("alias_map", {})
    out["checks"]["source_registry_version"] = src["schema"]
    out["checks"]["all_links_exist"] = True
    out["checks"]["actual_api_tests"] = 0
    return out

def validate(src, sync, skills, tasks, inc):
    errs=[]
    sources=src["sources"]
    ids=[s["id"] for s in sources]
    if len(set(ids))!=len(ids):errs.append("Duplicate source IDs")
    for key, value in src.get("alias_map", {}).items():
        if value not in ids:errs.append("Broken alias target: "+key)
    for s in sources:
        if not s.get("url","").startswith(("https://","http://")):errs.append("Non-HTTP source URL: "+s["id"])
        if not s.get("source_read_status"):errs.append("Missing source review state: "+s["id"])
        if s.get("implementation_status")!="not_tested":errs.append("Unexpected implementation state: "+s["id"])
    ski={x["id"] for x in skills["items"]};tsk={x["id"] for x in tasks["tasks"]};mod={x["id"] for x in inc["modules"]}
    for m in sync["modules"]:
        if m["module_id"] not in mod:errs.append("Unknown module "+m["module_id"])
        for sid in m["existing_skill_ids"]:
            if sid not in ski:errs.append("Missing skill "+sid)
        for tid in m["related_task_ids"]:
            if tid not in tsk:errs.append("Missing task "+tid)
        for ref in m["source_ids"]:
            if ref not in ids:errs.append("Missing source "+ref)
    if len(sync["task_records"])!=len(tsk):errs.append("Task count mismatch")
    if len(sync["existing_skill_records"])!=len(ski):errs.append("Skill count mismatch")
    return errs

def main():
    ap=argparse.ArgumentParser()
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args=ap.parse_args()
    src, cur, skills, tasks, inc = (read(p) for p in (SOURCE,CROSSWALK,SKILLS,TASKS,INC))
    err=validate(src,cur,skills,tasks,inc)
    if err:
        for e in err:print("ERROR:",e,file=sys.stderr)
        return 2
    exp_web=expected_web(src);exp_sync=expected_crosswalk(src,cur)
    if args.write:
        write(WEB,exp_web);write(CROSSWALK,exp_sync)
        print("Updated source atlas and crosswalk from existing canonical registers")
        return 0
    found=[]
    if read(WEB)!=exp_web:found.append("docs/data/inkubator-quellenregister.json needs sync")
    for old,new in zip(cur["modules"],exp_sync["modules"]):
        if old["source_ids"]!=new["source_ids"]:found.append("Module "+old["module_id"]+" needs source sync")
    if cur["external_interface_candidates"]!=exp_sync["external_interface_candidates"]:
        found.append("External interface candidates need sync")
    if found:
        for e in found:print("OUT OF SYNC:",e,file=sys.stderr)
        return 1
    print(f"OK: {len(src['sources'])} sources, {len(skills['items'])} skills, "
          f"{len(tasks['tasks'])} tasks, {len(inc['modules'])} modules; "
          "external API execution remains untested")
    return 0

if __name__=="__main__":
    sys.exit(main())
