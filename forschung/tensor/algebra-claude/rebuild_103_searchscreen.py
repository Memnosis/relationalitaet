#!/usr/bin/env python3
"""Recompute three-class SCREEN of historical 103 sketches, without proving classes.
Usage from root: python forschung/tensor/algebra-claude/rebuild_103_searchscreen.py
This is a deliberately conservative screening baseline, not a semantic classifier.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
inventory=json.loads((ROOT/"docs/data/tensor-inventar-v10_7.json").read_text(encoding="utf8"))
audit=json.loads((ROOT/"forschung/tensor/algebra-claude/ANALYSE_103_V0_1.json").read_text(encoding="utf8"))
STATIC={"verhaeltnis","potenzgesetz","summe_bilanz","logarithmisch","exponentiell"}
records=[]
for t in inventory["tensors"]:
    tags=audit["formeltypen"].get(t["id"],[])
    families=[]
    if set(tags)&STATIC: families.append("H1_GLEICHUNG_BEDINGUNG")
    if "dynamik_ode" in tags: families.append("H2_ENTWICKLUNG_PROZESS")
    if "linear_matrix" in tags: families.append("H3_OPERATOR_ABBILDUNG")
    records.append({"tensor_id":t["id"],"name":t["name"],
                    "source_formula":t.get("formula_anchor"),"raw_tags":tags,
                    "families":families,"inverse_type":"unknown",
                    "full_tensor_math":"not_verified"})
freq={}
for n in (0,1,2,3):freq[str(n)]=sum(len(t["families"])==n for t in records)
summary={"total":len(records),"tagged":sum(bool(x["raw_tags"]) for x in records),
         "unclassified":freq["0"],"membership":freq,
         "family_counts":{k:sum(k in x["families"] for x in records) for k in [
             "H1_GLEICHUNG_BEDINGUNG","H2_ENTWICKLUNG_PROZESS","H3_OPERATOR_ABBILDUNG"]}}
assert summary=={"total":103,"tagged":44,"unclassified":59,
   "membership":{"0":59,"1":37,"2":6,"3":1},
   "family_counts":{"H1_GLEICHUNG_BEDINGUNG":42,"H2_ENTWICKLUNG_PROZESS":7,"H3_OPERATOR_ABBILDUNG":3}}
print(json.dumps({"schema":"tensor103-three-screen/0.1","summary":summary,
                  "records":records,"conclusion":"not a disjoint scientific taxonomy"},
                 ensure_ascii=False,indent=2))
