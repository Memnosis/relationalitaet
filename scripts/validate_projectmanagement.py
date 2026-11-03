#!/usr/bin/env python3
"""Validate public project-management dataset (not science or browser UX)."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/data/projektmanagement-v1.json"
errors = []
try:
    data = json.loads(DATA.read_text(encoding="utf-8"))
except (OSError, ValueError) as exc:
    sys.exit("Invalid or missing PM JSON: " + str(exc))
if data.get("schema_version") != "pm-public-curated/0.1":
    errors.append("unknown schema_version")
tasks = data.get("tasks", [])
stages = data.get("stages", [])
if not isinstance(tasks, list) or not tasks:
    errors.append("missing task records")
if not isinstance(stages, list) or len(stages) != 6:
    errors.append("expected six evidence stages")
keys = [s.get("key") for s in stages if isinstance(s, dict)]
ids = [t.get("id") for t in tasks if isinstance(t, dict)]
if len(ids) != len(set(ids)):
    errors.append("duplicate task IDs")
known = set(ids)
required_scales = ["urgency", "architecture", "leverage", "unblocks", "risk", "readiness", "effort"]
for t in tasks:
    tid = t.get("id", "<missing>")
    if t.get("priority") not in ("P0", "P1", "P2"):
        errors.append(tid + ": invalid priority")
    if t.get("owner") not in ("gpt", "claude", "both"):
        errors.append(tid + ": invalid owner")
    if not isinstance(t.get("title"), str) or not t["title"]:
        errors.append(tid + ": missing title")
    for stage in keys:
        if t.get("stage", {}).get(stage) not in (0, 1):
            errors.append(tid + ": invalid evidence stage " + str(stage))
    for key in required_scales:
        score = t.get("scores", {}).get(key)
        if type(score) is not int or not 0 <= score <= 3:
            errors.append(tid + ": scale " + key + " must be integer 0..3")
    if not isinstance(t.get("domains"), list) or not t["domains"]:
        errors.append(tid + ": no affected research domains")
    for key in ("requires", "enables"):
        if not isinstance(t.get(key), list):
            errors.append(tid + ": " + key + " must be list")
            continue
        for dep in t[key]:
            if dep not in known:
                errors.append(tid + ": unresolved " + key + " task " + str(dep))
            if dep == tid:
                errors.append(tid + ": self-dependency")
    source = t.get("evidence", "")
    if not isinstance(source, str) or source.startswith("/") or ".." in Path(source).parts:
        errors.append(tid + ": unsafe source path")
    elif not (ROOT / source).is_file():
        errors.append(tid + ": evidence source not present at " + source)
for t in tasks:
    tid = t.get("id")
    for dep in t.get("enables", []):
        target = next((other for other in tasks if other.get("id") == dep), None)
        if target and tid not in target.get("requires", []):
            # Not necessarily logically wrong: enables can mean beneficial, not a strict prerequisite.
            pass
print("PM dataset:", len(tasks), "tasks /", len(stages), "stages /", len(errors), "errors")
print("Owner counts:", {owner: sum(t.get("owner") == owner for t in tasks) for owner in ("gpt", "claude", "both")})
print("Priorities:", {p: sum(t.get("priority") == p for t in tasks) for p in ("P0", "P1", "P2")})
for e in errors:
    print("ERROR:", e)
if errors:
    sys.exit(1)
