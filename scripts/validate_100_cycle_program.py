#!/usr/bin/env python3
"""No-loss static checks for the 100-cycle programme.
This is NOT a completed live study or a prompt execution test.
"""
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"forschung/koordination/PROGRAMM_100_ZYKLEN_MANIFEST.json"
d=json.loads(p.read_text(encoding="utf-8"))
issues=[]
if d.get("target_full_cycles")!=100:issues.append("target must equal 100")
if d.get("verified_full_cycles")!=0:issues.append("initial verified cycle count unsupported without completion evidence")
slots=d.get("focus_slots",[])
m=[x for x in slots if x.get("focus")=="mitmachen"]
i=[x for x in slots if x.get("focus")=="internal_completion"]
if len(slots)!=20 or len(m)!=12 or len(i)!=8:issues.append("focus allocation must be 20 = 12+8 in this revision")
if len({x.get("slot") for x in slots})!=len(slots):issues.append("duplicate slot IDs")
if any(x.get("assigned_cycle") is not None for x in slots):issues.append("reservations cannot be declared completed before assignment")
if any(x.get("status")!="reserved_not_started" for x in slots):issues.append("unexpected focus completion")
sources=d.get("mitmach_inventory",{}).get("sources",[])
source_ids={}
for src in sources:
    sp=ROOT/src["path"]
    if not sp.is_file():
        issues.append("missing source "+src["path"]);continue
    data=json.loads(sp.read_text(encoding="utf-8"))
    ids=[x["id"] for x in data.get("tasks",[])]
    if len(ids)!=src["count"]:issues.append("count mismatch "+src["path"])
    for id in ids:
        if id in source_ids:issues.append("duplicate source task "+id)
        source_ids[id]=src["path"]
actions=d["mitmach_inventory"]["actions"]
ids=[x["action_id"] for x in actions]
if len(actions)!=38 or len(set(ids))!=len(actions):issues.append("expected 38 unique source actions")
if set(source_ids)!=set(ids):issues.append("missing or phantom source action IDs")
slot_ids=[id for x in m for id in x.get("task_ids",[])]
if len(slot_ids)!=len(set(slot_ids)) or set(slot_ids)!=set(ids):
    issues.append("action-to-slot mapping not complete or unique")
for a in actions:
    if source_ids.get(a["action_id"])!=a["source_path"]:issues.append("source pointer mismatch "+a["action_id"])
    if a["reserved_slot"] not in [x["slot"] for x in m]:issues.append("bad focus slot "+a["action_id"])
    if a.get("release")=="approved" and a.get("actual_functional_test")!="passed":
        issues.append("approved untested action "+a["action_id"])
if set(d["study_export_contract"]["private_fields"])&set(d["study_export_contract"]["public_fields"]):
    issues.append("public export overlaps private field")
print("100-cycle programme: target",d["target_full_cycles"],"focus slots",len(slots),"action objects",len(actions))
for error in issues:print("ERROR:",error)
if issues:sys.exit(1)
print("PASS: static inventory coverage only; runtime and trials still outstanding")
