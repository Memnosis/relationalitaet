#!/usr/bin/env python3
"""Read-only regression check for the research preview; does not certify mathematical tensorhood."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INVENTORY = ROOT / "docs/data/tensor-inventar-v10_7.json"
ATLAS = ROOT / "docs/data/tensoratlas-forschung-v0_1.json"

def norm(text):
    # Mirrors the JS generation procedure for existing German role names.
    import unicodedata
    return " ".join(unicodedata.normalize("NFKC", text).strip().lower().split())

def main():
    raw = json.loads(INVENTORY.read_text(encoding="utf-8"))
    data = json.loads(ATLAS.read_text(encoding="utf-8"))
    rows = raw["tensors"]
    assert len(rows) == 103, "historical inventory size changed"
    assert len(data["tensors"]) == len(rows), "missing or added tensor without audit"
    assert all(len(x["axes"]) == 3 and all(len(a["elements"]) == 3 for a in x["axes"]) for x in rows)
    assert all(len(x["fields"]) == 27 for x in data["tensors"])
    assert len({x["id"] for x in data["tensors"]}) == len(rows)
    assert all(len({f["address"] for f in x["fields"]}) == 27 for x in data["tensors"])
    assert all(f["calculations"] == "not_run" and f["evidence"] == "not_verified"
               for t in data["tensors"] for f in t["fields"]), "do not advertise unverified results"
    for source, derived in zip(rows, data["tensors"]):
        assert source["id"] == derived["id"]
        for f in derived["fields"]:
            i,j,k = (int(n)-1 for n in f["address"].split("-"))
            assert f["original_roles"] == [source["axes"][0]["elements"][i],
                                            source["axes"][1]["elements"][j],
                                            source["axes"][2]["elements"][k]]
    expected = {}
    hist = {str(i):0 for i in range(4)}
    for a,b in itertools.combinations(rows,2):
        left = [{norm(z) for z in axis["elements"]} for axis in a["axes"]]
        right = [{norm(z) for z in axis["elements"]} for axis in b["axes"]]
        best = (-1,-1,(),())
        for p in itertools.permutations(range(3)):
            matched = tuple(len(left[i] & right[p[i]]) for i in range(3))
            coverage = sum(n > 0 for n in matched)
            score = sum(matched)
            if (coverage,score) > best[:2]:
                best = coverage,score,p,matched
        coverage,score,p,matched = best
        hist[str(coverage)] += 1
        if coverage:
            expected[(a["id"],b["id"])] = (coverage,score,list(p),list(matched))
    observed = {(x["a"],x["b"]):(x["axis_coverage"],x["matched_role_count"],
                x["axis_permutation"],x["per_axis"]) for x in data["lexical_overlap_pairs"]}
    assert expected == observed, "overlay output differs from recomputation"
    assert data["counts"]["axis_coverage_histogram"] == hist
    assert hist == {"0":5104,"1":144,"2":5,"3":0}
    assert len(observed) == 149
    assert sum(bool(x["formula_anchor"]) for x in rows) == 100
    assert data["counts"]["registered_task_families"] == 44
    assert data["counts"]["verified_exact_100_message_sequence"] is False
    print("PASS: 103 structures; 2781 addresses; 5253 lexical comparisons; 149 matches (144+5).")
    print("NOT CHECKED: mathematical field calculations, independent proofs, chemistry imports or editorial approval.")

if __name__ == "__main__":
    main()
