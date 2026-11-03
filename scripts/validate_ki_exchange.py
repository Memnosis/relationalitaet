#!/usr/bin/env python3
"""Validate two-AI cycle claims; does not invoke AI agents."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
cycle_root = ROOT / "forschung/koordination/zyklen"
found = sorted(cycle_root.glob("*/STATUS.json"))
errors = []
summary = ["# KI-Austausch: automatischer Integritätsbericht", "", "GitHub-Dateien werden geprüft; eine KI wird dadurch nicht selbstständig gestartet.", ""]
for status_file in found:
    base = status_file.parent
    try:
        state = json.loads(status_file.read_text(encoding="utf-8"))
    except (ValueError, OSError) as e:
        errors.append(f"{status_file}: {e}")
        continue
    ident = state.get("cycle_id")
    flags = state.get("acknowledgements", {})
    requested = ["gpt_handoff_created", "claude_received", "claude_delivered",
                 "gpt_reviewed", "claude_acknowledged_review", "cycle_report_created"]
    if not isinstance(ident, str) or ident != base.name:
        errors.append(f"{base.name}: inconsistent cycle_id")
    if any(not isinstance(flags.get(k), bool) for k in requested):
        errors.append(f"{ident}: acknowledgement fields must all be booleans")
    source_paths = state.get("files", {})
    for name, key in (("Claude receipt", "claude_received"),
                      ("Claude delivery", "claude_delivered"),
                      ("GPT review", "gpt_reviewed"),
                      ("cycle report", "cycle_report_created")):
        target = name.lower().split()[0]
        fkey = {"Claude receipt":"claude_response", "Claude delivery":"claude_response",
                "GPT review":"gpt_response", "cycle report":"report"}[name]
        path = ROOT / str(source_paths.get(fkey, ""))
        if flags.get(key) and not path.is_file():
            errors.append(f"{ident}: {key}=true but {fkey} file is missing")
    if flags.get("claude_acknowledged_review") and not flags.get("gpt_reviewed"):
        errors.append(f"{ident}: Claude cannot acknowledge review before GPT review")
    if flags.get("cycle_report_created") and not all(flags.get(k) for k in requested[:-1]):
        errors.append(f"{ident}: cycle report claims closure without complete reciprocal acknowledgements")
    if state.get("stage") == "completed" and not all(flags.get(k) for k in requested):
        errors.append(f"{ident}: completed stage without all acknowledgements")
    if flags.get("claude_received"):
        text = (ROOT / source_paths["claude_response"]).read_text(encoding="utf-8")
        if not re.search(r"(?m)^agent:\s*claude\s*$", text):
            errors.append(f"{ident}: Claude receipt lacks 'agent: claude'")
        if not re.search(r"(?m)^cycle_id:\s*"+re.escape(ident)+r"\s*$", text):
            errors.append(f"{ident}: Claude receipt lacks matching cycle_id")
    summary.append(f"## {ident}")
    summary.append(f"- Stage: \`{state.get('stage','unknown')}\`")
    for field in requested:
        summary.append(f"- {field}: {'yes' if flags.get(field) else 'no'}")
    summary.append("")
if not found:
    errors.append("No STATUS.json files found")
summary.extend(["## Prüfung", "Ergebnis: **" + ("FAILED" if errors else "OK") + "**"])
summary.extend("- " + err for err in errors)
report = "\n".join(summary) + "\n"
print(report)
output = pathlib.Path("ki_exchange_validation_report.md")
output.write_text(report, encoding="utf-8")
if errors:
    sys.exit(1)
