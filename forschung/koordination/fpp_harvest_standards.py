#!/usr/bin/env python3
"""FPP-01 Harvesting-Preflight. No silent writes to canonical registers.

Run from repo root:
  python3 forschung/koordination/fpp_harvest_standards.py --check
  python3 forschung/koordination/fpp_harvest_standards.py --report /tmp/fpp-impact.json

Reads standards source+glossary candidate catalog and routing proposal.
Checks source URIs, glossary candidates, duplicate candidates and registered paper
destinations. Emits an IMPACT proposal (to stdout or explicit --report).
Never merges or publishes research claims.
"""
from __future__ import annotations
import argparse
import json
import pathlib
import re
import sys
from collections import defaultdict
from datetime import date
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = ROOT / "forschung" / "koordination"
CATALOG = BASE / "FPP_01_STANDARDS_QUELLEN_GLOSSAR_V0_1.json"
ROUTING = BASE / "FPP_01_ROUTING_PROPOSAL_V0_1.json"

def load(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)

def audit(catalog, routing):
    issues = []
    sources = []
    glossary = defaultdict(lambda: {"source_ids": [], "status": "candidate_pending_historical_glossary_crosswalk"})
    affected = defaultdict(set)
    seen_uris = set()
    seen_ids = set()
    for item in catalog.get("entries", []):
        sid = item.get("id", "")
        uri = item.get("canonical_url", "")
        parsed = urlparse(uri)
        if not sid or sid in seen_ids:
            issues.append({"type": "invalid_or_duplicate_standard_id", "id": sid})
        seen_ids.add(sid)
        if parsed.scheme != "https" or not parsed.netloc:
            issues.append({"type": "invalid_standard_uri", "id": sid, "uri": uri})
        if uri in seen_uris:
            issues.append({"type": "duplicate_standard_uri", "uri": uri})
        seen_uris.add(uri)
        sources.append({"id": sid, "url": uri, "title": item.get("name"), "status": "candidate_for_canonical_source_crosswalk"})
        for term in item.get("glossary_candidates", []):
            normalized = " ".join(term.casefold().split())
            if not normalized:
                issues.append({"type": "empty_glossary_term", "id": sid})
                continue
            if sid not in glossary[normalized]["source_ids"]:
                glossary[normalized]["source_ids"].append(sid)
            glossary[normalized]["label"] = term
        for use in item.get("proposed_uses", []):
            affected[use].add(sid)
    # Validate paper manifests only when canonical files are in the repo.
    for paper in routing.get("publication_manifests", []):
        p = ROOT / paper.get("path", "")
        if not p.is_file():
            issues.append({"type": "missing_publication_target", "id": paper.get("id"), "path": paper.get("path")})
    if routing.get("status") != "proposal_not_deployed":
        issues.append({"type": "unexpected_deployment_status", "value": routing.get("status")})
    records = {
        "schema": "fpp-harvest-impact/0.1",
        "status": "draft_only_no_merge",
        "run_date": date.today().isoformat(),
        "catalog": str(CATALOG.relative_to(ROOT)),
        "routing": str(ROUTING.relative_to(ROOT)),
        "sources_found": len(sources),
        "glossary_candidates_found": len(glossary),
        "source_candidates": sources,
        "glossary_candidates": [glossary[k] for k in sorted(glossary)],
        "affected_paper_families": {k: sorted(v) for k, v in sorted(affected.items())},
        "mandatory_next_checks": [
            "merge against historical shared source register by normalized URI and provenance",
            "merge against glossary v15.4 by concept identity not spelling alone",
            "resolve canonical publication ownership and avoid new parallel registers",
            "add FPP structure-paper and algebra test impact with evidence status",
            "obtain expert review, editorial release and publish only derived projections"
        ],
        "issues": issues
    }
    return records

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Audit and return nonzero on issues")
    parser.add_argument("--report", type=pathlib.Path, help="Write draft impact JSON to chosen path")
    args = parser.parse_args()
    report = audit(load(CATALOG), load(ROUTING))
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(serialized, encoding="utf-8")
    else:
        print(serialized)
    return 1 if args.check and report["issues"] else 0

if __name__ == "__main__":
    sys.exit(main())
