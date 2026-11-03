#!/usr/bin/env python3
"""Validate reciprocal AI discussion register against actual Git files.
A missing peer reply or source is always reported. --strict blocks release.
Static file check only; no automatic peer acknowledgements are inferred.
"""
from pathlib import Path
import argparse
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"forschung/koordination/zyklen/KI-2026-11-03-001"
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--strict",action="store_true")
    args=parser.parse_args()
    errors=[]
    source=BASE/"DISKUSSIONS_EINGANGSKONTROLLE.json"
    data=json.loads(source.read_text(encoding="utf-8"))
    registered=set()
    for item in data["items"]:
        idx=item["id"]
        registered.add(idx)
        name=item.get("source")
        reply=item.get("response")
        state=item.get("state","")
        if not name:
            errors.append(f"discussion {idx}: source missing or location unknown (not answered)")
        elif not (BASE/name).is_file():
            errors.append(f"discussion {idx}: original source not found: {name}")
        if not reply or not (BASE/reply).is_file():
            errors.append(f"discussion {idx}: GPT response or documented blocker missing")
        if name and reply and state not in ("gpt_responded_peer_ack_pending","peer_confirmed","completed"):
            errors.append(f"discussion {idx}: reply state not acknowledged in register")
    for f in BASE.glob("CLAUDE_DISKUSSION_*.md"):
        import re
        m=re.search(r"CLAUDE_DISKUSSION_(\d+)",f.name)
        if m and m.group(1) not in registered:
            errors.append(f"unregistered incoming discussion: {f.name}")
    for r in data.get("peer_reviews",[]):
        if not (ROOT/r["source"]).is_file():
            errors.append("missing review input: "+r["source"])
        if not (BASE/r["response"]).is_file():
            errors.append("missing review response: "+r["response"])
    if data.get("cycle_closed") and any(x["state"]!="completed" for x in data["items"]):
        errors.append("cycle marked completed while a discussion has not completed")
    print("AI discussion gate:",len(data["items"]),"tracked;",len(errors),"open blockers")
    for err in errors: print("BLOCKER:",err)
    if args.strict and errors:
        sys.exit(1)
if __name__=="__main__":
    main()
