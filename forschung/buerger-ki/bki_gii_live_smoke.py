#!/usr/bin/env python3
"""GII Echtquellen-Rauchtest mit ZIP-Transport und Belegbericht.

Führt einen Live-Import amtlich bereitgestellter, konsolidierter Gesetzestexte aus.
Nur bei expliziter Ausführung; verwechselt Abruf nicht mit juristischer Validierung.
"""
import datetime
import json
import sys
import urllib.error
import urllib.request
from bki_gii_adapter import extract, ImportErrorWithContext

SOURCES = [
    ("bmg", "https://www.gesetze-im-internet.de/bmg/xml.zip", "BMG-§18"),
    ("gewo", "https://www.gesetze-im-internet.de/gewo/xml.zip", "GEWO-§14")
]
MAX_DOWNLOAD = 20_000_000

def main():
    date = datetime.date.today().isoformat()
    results = []
    errors = []
    for law, url, expected in SOURCES:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "BuergerKI-ResearchSourceAudit/0.2"})
            with urllib.request.urlopen(req, timeout=35) as response:
                data = response.read(MAX_DOWNLOAD + 1)
            if len(data) > MAX_DOWNLOAD:
                raise ValueError("Archiv > 20 MB")
            parsed = extract(data, law, url, date)
            matches = [p for p in parsed["provisions"] if p["provision_id"] == expected]
            if len(matches) != 1:
                raise ValueError(f"Erwartete Vorschrift {expected} nicht eindeutig gefunden")
            results.append({
                "law": law.upper(), "source_url": url, "retrieved_at": date,
                "archive_sha256": parsed["source_sha256"],
                "xml_sha256": parsed["xml_sha256"],
                "provision_count": len(parsed["provisions"]),
                "target": expected,
                "target_text_sha256": matches[0]["text_hash_sha256"],
                "legal_validity_checked": False,
                "local_authority_checked": False
            })
            print(f"OK {law}: {len(parsed['provisions'])} Paragraphen / {expected}")
        except (urllib.error.URLError, ValueError, ImportErrorWithContext, TimeoutError) as exc:
            errors.append({"law": law, "source_url": url, "error": str(exc)})
            print(f"FAIL {law}: {exc}", file=sys.stderr)
    result = {
        "schema": "bki-live-source-smoke/0.1",
        "mode": "live_remote_import",
        "validation_scope": "transport_xml_parse_and_required_provision",
        "status": "passed" if len(results) == len(SOURCES) else "failed",
        "sources": results, "errors": errors
    }
    with open("bki_gii_live_result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return 0 if result["status"] == "passed" else 1

if __name__ == "__main__":
    sys.exit(main())
