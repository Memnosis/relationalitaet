#!/usr/bin/env python3
"""Validate reciprocal review capacity and redacted public workflow inventory.
This is a static audit, not a prompt trial or author release.
"""
from collections import Counter
from pathlib import Path
import json
import sys

root=Path(__file__).resolve().parents[1]
queue=json.loads((root/"forschung/koordination/REVIEW_QUEUE_V2.json").read_text())
public=json.loads((root/"docs/data/workflow-stand-v1.json").read_text())
inventory=json.loads((root/"forschung/register/PROMPT_ARCHITEKTUR_INVENTAR_V0_1.json").read_text())
crosswalk=json.loads((root/"forschung/register/PROMPT_CROSSWALK_V0_1.json").read_text())
errors=[]
if queue.get("schema_version")!="two-ai-review-queue/2.0":errors.append("unknown review queue schema")
open_request=[x for x in queue["requests"] if x["status"]=="awaiting_response"]
for owner,count in Counter(x["target"] for x in open_request).items():
    if count>queue["capacity_per_target"]:errors.append(f"{owner} exceeds three open review requests: {count}")
if len(set(x["id"] for x in queue["requests"]))!=len(queue["requests"]):errors.append("duplicate request IDs")
for item in queue["requests"]:
    src=root/item["source"]
    if not src.is_file():errors.append("missing review source "+item["source"])
    if item.get("response") and not (root/item["response"]).is_file():
        errors.append("missing review response "+item["response"])
if public.get("schema_version")!="public-workflow/1.0":errors.append("unknown public schema")
p=public["prompt_overview"]
counts=[int(g["count"]) for g in p["labels"]]
actual=inventory["zaehlung"]
if sum(counts)!=actual["objekte_gesamt"] or p["unique_ids"]!=crosswalk["zaehlung"]["eindeutige_ids"]:
    errors.append("public distinct prompt count disagrees with source inventory")
if p["objects"]!=crosswalk["zaehlung"]["vorkommen"]:
    errors.append("public occurrence count disagrees with crosswalk")
if p["overlapping_occurrences"]!=actual["doppelt_gefuehrt"]:errors.append("overlap count disagrees with source inventory")
if p["mutually_tested"]!=actual["wechselseitig_getestet"]:errors.append("mutual tested count disagrees with source inventory")
if p.get("unique_count_verified") is not True:errors.append("unique IDs must be tied to the source crosswalk")
if public["cycle_overview"]["verified"]!=0:errors.append("cycle closure needs separate status evidence")
if public.get("public_privacy")!="aggregate_only":errors.append("public UI must use aggregate-only projection")
raw_terms=("meta_prompt","raw_prompt","private_manuscript","credential")
for key in raw_terms:
    if key in json.dumps(public,ensure_ascii=False):errors.append("raw/internal field in public projection: "+key)
print(f"Workflow v2: {len(queue['requests'])} requests; {len(open_request)} awaiting response; {p['objects']} prompt occurrences, {p['overlapping_occurrences']} overlaps")
for error in errors:print("ERROR:",error)
if errors:sys.exit(1)
print("PASS static data/queue consistency; model execution and browser tests separate")
