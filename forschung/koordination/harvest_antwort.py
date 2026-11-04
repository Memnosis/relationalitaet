#!/usr/bin/env python3
"""FPP-01: explicit answer/analysis harvesting, lossless and draft-only.

Input must be an explicitly exported UTF-8 Markdown file, not an invisible ChatGPT
conversation feed. The tool has NO background access to conversations.
Usage:
  python3 forschung/koordination/harvest_antwort.py --input antwort.md --actor gpt --out entwuerfe/
  python3 forschung/koordination/harvest_antwort.py --input analyse.md --actor claude --out entwuerfe/
Writes a lossless capture and a candidate impact route; NEVER edits canon papers,
sources or glossary and NEVER publishes a chat.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib
import re
from datetime import datetime, timezone

HERE = pathlib.Path(__file__).resolve().parent
ROUTE = HERE / "FPP_01_ROUTING_PROPOSAL_V0_1.json"
# Multi-axis indexes are organizational FACETS, not a proved tensor.
TAGS = {
    "algebra": ("algebra", "formel", "gleichung", "operator", "umform", "invariante",
                "elimination", "isomorph", "sympy", "beweis", "relation"),
    "tensor": ("tensor", "trinit", "feldakte", "27 felder", "achsen"),
    "skill": ("skill", "werkzeug", "funktion", "api", "code", "parser", "automatis"),
    "source": ("quelle", "doi", "provenienz", "citation", "ro-crate", "prov-o", "fair"),
    "glossary": ("glossar", "definition", "begriff", "skos", "ontologie"),
    "method": ("methode", "prozess", "prüfung", "gegenprobe", "reprodu", "validierung"),
    "publication": ("paper", "publikation", "manuskript", "kapitel", "redaktion"),
    "website": ("website", "dashboard", "seite", "navigation", "design"),
}
ROUTES = {
    "algebra": ["tensor_algebra", "harvesting_page"],
    "tensor": ["affected_tensors", "tensor_foundations", "tensor_public_data"],
    "skill": ["skill_public_data", "mini_ai"],
    "source": ["source_register", "glossary"],
    "glossary": ["glossary"],
    "method": ["relevant_methods_paper", "harvesting_page"],
    "publication": ["publication_routes"],
    "website": ["affected_site"],
}
def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
def sections(markdown: str):
    lines = markdown.splitlines(keepends=True)
    pieces, heading, bucket = [], "Preamble", []
    for line in lines:
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if m and bucket:
            pieces.append({"heading": heading, "text": "".join(bucket)})
            bucket = []
        if m:
            heading = m.group(1).strip()
        bucket.append(line)
    if bucket:
        pieces.append({"heading": heading, "text": "".join(bucket)})
    assert "".join(p["text"] for p in pieces) == markdown
    return pieces
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p.add_argument("--actor", choices=["gpt", "claude", "human", "other"], required=True)
    p.add_argument("--source-url", default="")
    a = p.parse_args()
    raw = a.input.read_text(encoding="utf-8")
    if not raw.strip():
        raise SystemExit("ERROR: no content supplied")
    a.out.mkdir(parents=True, exist_ok=True)
    digest = sha(raw)
    sid = "ANA-" + digest[:16].upper()
    parts = sections(raw)
    rows = []
    for i, sec in enumerate(parts, 1):
        low = (sec["heading"] + " " + sec["text"]).lower()
        facets = sorted(k for k, clues in TAGS.items() if any(token in low for token in clues))
        if not facets:
            facets = ["unclassified"]
        route = sorted({x for k in facets for x in ROUTES.get(k, [])})
        rows.append({
            "id": sid + "-S" + str(i).zfill(3),
            "heading": sec["heading"],
            "content_sha256": sha(sec["text"]),
            "content": sec["text"],  # NO LOSS: retains original section text
            "facet_candidates": facets,
            "candidate_destinations": route,
            "evidence_status": "not_assessed",
            "domain_status": "not_assessed",
            "publication_status": "draft_unreleased",
            "review_requirement": "verify scientific and paper routing manually"
        })
    obj = {
        "schema_version": "answer-harvest/0.1",
        "capture_id": sid,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "original_source_file": str(a.input),
        "source_url": a.source_url or None,
        "actor": a.actor,
        "source_sha256": digest,
        "raw_text": raw,  # lossless primary source; NEVER auto-publish
        "sections": rows,
        "routing_method": "deterministic keyword candidate only; not truth or paper ownership",
        "next_steps": ["review facets", "resolve canonical ids and duplicate findings",
                       "validate formulas and semantic roles", "create FPP events",
                       "prepare impacts to algebra, glossary, sources, papers",
                       "manual mathematical/editorial approval before merge"],
    }
    dest = a.out / (sid + ".json")
    dest.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"file": str(dest), "capture_id": sid, "sections": len(rows),
                      "sha256": digest, "status": "draft_only"}, ensure_ascii=False))
if __name__ == "__main__":
    main()
