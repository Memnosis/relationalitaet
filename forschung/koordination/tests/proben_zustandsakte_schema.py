#!/usr/bin/env python3
"""Negativproben gegen GPTs Entwurf der Zustandsakte (Schema v0.1, Zweig proposal/zustandsakte-v01-2026-11-04).
Owner: Claude (Gegenlesung). Liest das Schema per `git show` aus dem Vorschlagszweig; ändert nichts.

Jede Probe prüft genau eine im Entwurf (ZUSTANDSAKTE_ENTWURF_V0_1) genannte Regel. Erwartung = Regel greift
(Dokument wird abgelehnt). Ergebnis „nicht erzwungen“ heißt: Das Schema lässt es durch; dann muss der Reducer
die Regel prüfen, oder das Schema wird ergänzt. Das ist ein Befund, kein Fehler im Skript.

Aufruf: python3 forschung/koordination/tests/proben_zustandsakte_schema.py [--ref REF]   (benötigt jsonschema)
"""
import copy
import json
import pathlib
import subprocess
import sys

W = pathlib.Path(__file__).resolve().parents[3]
REF = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "origin/proposal/zustandsakte-v01-2026-11-04"
PFAD = sys.argv[sys.argv.index("--pfad") + 1] if "--pfad" in sys.argv else "forschung/koordination/schema/zustandsakte-proposal-v0_1.schema.json"
try:
    import jsonschema
except ImportError:
    print("SKIP: jsonschema fehlt (pip install jsonschema) – SKIP ist kein PASS")
    sys.exit(77)
r = subprocess.run(["git", "-C", str(W), "show", f"{REF}:{PFAD}"], capture_output=True, text=True)
if r.returncode:
    print(f"SKIP: {REF}:{PFAD} nicht vorhanden (git fetch origin proposal/zustandsakte-v01-2026-11-04)")
    sys.exit(77)
S = json.loads(r.stdout)
sha = subprocess.run(["git", "-C", str(W), "rev-parse", REF], capture_output=True, text=True).stdout.strip()
v = jsonschema.Draft202012Validator(S)
jsonschema.Draft202012Validator.check_schema(S)

BASIS = {"schema_version": S.get("properties", {}).get("schema_version", {}).get("const", "zustandsakte/0.1-proposal"), "snapshot_id": "a", "source_commit": "0" * 40, "input_manifest_sha256": "0" * 64,
         "visibility": "public_projection",
         "entities": [{"id": "CLM-X", "type": "claim", "owner": "claude", "work": "delivered", "validation": "owner_tested", "science": "unresolved",
                       "exchange": "responded", "release": "published", "cycle": "open", "evidence_ids": ["TST-X"]}],
         "events": [{"event_id": "EV-001", "entity_id": "CLM-X", "kind": "test_run", "actor": "claude", "source_commit": "0" * 40, "evidence_refs": ["x"]}]}


def gueltig(d):
    return not list(v.iter_errors(d))


def probe(nr, regel, quelle, aendern, abgelehnt_erwartet=True):
    d = copy.deepcopy(BASIS)
    aendern(d)
    abgelehnt = not gueltig(d)
    return {"nr": nr, "regel": regel, "quelle_im_entwurf": quelle, "erzwungen": abgelehnt == abgelehnt_erwartet}


if "0.1" not in BASIS["schema_version"]:  # ab v0.2: Pflichtfelder, die v0.1 nicht kennt
    BASIS["snapshot_id"] = "a" * 64
    BASIS["entities"][0].update(confidentiality="public", decision_ref="DEC-BEISPIEL")
    BASIS["events"][0].update(exit_code=0, input_sha256="b" * 64, script_sha256="c" * 64, outcome="passed")
if not gueltig(BASIS):
    print("Basisdokument ungültig gegen dieses Schema – Proben nicht aussagekräftig:")
    for e in list(v.iter_errors(BASIS))[:8]: print(" -", list(e.path), e.message[:160])
    sys.exit(2)
P = [
    probe("P1", "öffentliche Projektion enthält keinen privaten Eintrag", "Publikationsschutz: „Nie ein öffentliches Full-Snapshot mit private-Flags“",
          lambda d: d["entities"][0].update(release="private")),
    probe("P2", "Wert ‚skipped‘ existiert (SKIP ist eigener Status)", "Evidenzregeln + T05",
          lambda d: d["entities"][0].update(validation="skipped"), abgelehnt_erwartet=False),
    probe("P3", "doppelte event_id wird abgelehnt", "T02", lambda d: d["events"].append(copy.deepcopy(d["events"][0]))),
    probe("P4", "Ereignis zu unbekannter Entität wird abgelehnt", "T03 (dangling)", lambda d: d["events"][0].update(entity_id="GIBT-ES-NICHT")),
    probe("P5", "snapshot_id ist ein Hash (für denselben Snapshot in Website und DOCX)", "Q6, T12", lambda d: d.update(snapshot_id="x")),
    probe("P6", "test_run verlangt Exitcode, Skript- und Eingabe-SHA", "Evidenzregeln: „tatsächlicher Lauf mit Exitcode, Input-/Skript-SHA …“",
          lambda d: [d["events"][0].pop(k, None) for k in ("exit_code", "input_sha256", "script_sha256", "outcome")]),
    probe("P7", "peer_tested/reproduced/replicated verlangt Nachweis-IDs", "T03: „kein peer_review=1“ ohne Beleg",
          lambda d: d["entities"][0].update(validation="replicated", evidence_ids=[])),
]
erg = {"schema_ref": REF, "schema_pfad": PFAD, "schema_commit": sha, "basis_gueltig": True, "proben": P,
       "erzwungen": sum(p["erzwungen"] for p in P), "gesamt": len(P)}
if "--json" in sys.argv:
    print(json.dumps(erg, ensure_ascii=False, indent=1))
else:
    for p in P:
        print(f"{p['nr']} {'erzwungen    ' if p['erzwungen'] else 'NICHT erzwungen'} {p['regel']}")
    print(f"Schema {REF} @ {sha[:12]}: {erg['erzwungen']}/{erg['gesamt']} Regeln im Schema erzwungen")
sys.exit(0)
