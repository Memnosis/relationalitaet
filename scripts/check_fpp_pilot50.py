#!/usr/bin/env python3
"""Static pilot50, provenance and FPP event crosswalk tests; no scientific approval."""
import json
import pathlib
import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))
base="forschung/tensor/formeln/pilot50/"
corpus=load(base+"FORMELN50_KORPUS_V0_1.json")
struct=load(base+"PILOT50_STRUKTURERGEBNIS_V0_1.json")
motifs=load(base+"PILOT50_GRAPHMUSTER_V0_1.json")
algebra=load("forschung/tensor/algebra-claude/FORMELN50_GPT_RELATIONEN_V0_1.json")
fpp=load("forschung/koordination/FPP_50_FORMELN_EVENTS_IMPACTS_V0_1.json")
ids={f["id"] for f in corpus["formeln"]}
assert len(ids)==len(corpus["formeln"])==50
assert struct["summary"]["formulas"]==50
assert struct["summary"]["ternary_candidates"]==21
assert struct["summary"]["graph_edges"]==39
assert motifs["summary"]["triples"]==33
assert sum(motifs["summary"][k] for k in ("stars","strict_triangles","mixed"))==33
assert all(set(x["ids"])<=ids for x in motifs["motifs"])
assert len(algebra["confirmed_known_relations"])==5
assert len(algebra["negative_findings"])==6
assert len(fpp["events"])==12 and len(fpp["impacts"])==57
assert all(e["visibility"]!="public_released" for e in fpp["events"])
assert all(i["automatic_merge"] is False for i in fpp["impacts"])
try:
    import jsonschema
except ImportError:
    print("SKIP schema validation: jsonschema missing; no PASS for FPP envelope")
    sys.exit(77)
schema=load("forschung/koordination/FPP_01_EVENT_SCHEMA_V0_1.json")
for e in fpp["events"]:
    jsonschema.Draft202012Validator(schema,format_checker=jsonschema.FormatChecker()).validate(e)
print("OK: 50 originals, 21 raw triads, 39 label edges, 33 motifs, 12 review events, 57 unmerged impacts")
