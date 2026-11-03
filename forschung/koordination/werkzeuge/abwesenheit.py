#!/usr/bin/env python3
"""Abwesenheitserkennung Claude/GPT (Regel R7). Owner: Claude. Nur lesend.

Vorgabe Nils (03.11.2026): „abwesend ist, wenn auf 10 Beiträge einer KI kein Feedback oder
keine Analyse kommt“.

Messung aus Git (versionsfest, nicht von Hand):
- Beitrag = ein Arbeitsschritt = eine eindeutige Commit-Betreffzeile einer KI
  (GPT legt eine Änderung oft als mehrere Datei-Commits mit gleichem Betreff ab).
- Feedback/Analyse von KI Y = ein Commit von Y, der
  (1) den Trailer `Analyse-von: <sha>[..<sha>]` oder `Feedback-zu: <ID>` trägt (bevorzugt, R8), oder
  (2) eine Feedback-Datei anlegt/ändert: unter forschung/koordination/ eine Datei mit
      DISKUSSION, ANTWORT, REVIEW, ANALYSE, NACHHOL, VERGLEICH oder EINGANGSKONTROLLE im Namen,
      oder REVIEW_QUEUE_V2.json.
- Abwesend ist Y, wenn X seit dem letzten Feedback von Y mindestens SCHWELLE (Standard 10)
  Beiträge gemacht hat. Gibt es noch gar kein Feedback von Y, zählt alles im Zeitfenster.
- Zuordnung (R8): Trailer `KI: claude` / `Claude-Session:` / `Co-Authored-By: Claude` → claude;
  Trailer `KI: gpt` → gpt; Trailer `KI: nils` → nils (zählt nicht); ohne Kennung → gpt
  (vorläufig; mit --streng → unbekannt, zählt nicht).

Aufruf: python3 forschung/koordination/werkzeuge/abwesenheit.py [--schwelle 10] [--tage 14] [--streng] [--json]
Exit 0 = niemand abwesend, 3 = Pflicht nach R7 ausgelöst (für CI lesbar).
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys

W = pathlib.Path(__file__).resolve().parents[3]
FEEDBACK_DATEI = re.compile(r"^forschung/koordination/(.*/)?[^/]*(DISKUSSION|ANTWORT|REVIEW|ANALYSE|NACHHOL|VERGLEICH|EINGANGSKONTROLLE)[^/]*$|^forschung/koordination/REVIEW_QUEUE_V2\.json$")
TRAILER_FEEDBACK = re.compile(r"^(analyse-von|feedback-zu):\s*\S+", re.I | re.M)


def zuordnen(text, streng=False):
    t = text.lower()
    if re.search(r"^ki:\s*nils\s*$", t, re.M):
        return "nils"
    if "claude-session:" in t or "co-authored-by: claude" in t or re.search(r"^ki:\s*claude\s*$", t, re.M):
        return "claude"
    if re.search(r"^ki:\s*gpt\s*$", t, re.M):
        return "gpt"
    return "unbekannt" if streng else "gpt"


def ist_feedback(text, dateien):
    return bool(TRAILER_FEEDBACK.search(text)) or any(FEEDBACK_DATEI.match(d) for d in dateien)


def commits(tage=14, streng=False):
    out = subprocess.run(["git", "-C", str(W), "log", f"--since={tage} days ago", "--name-only",
                          "--format=\x1e%H\x1f%cI\x1f%B\x1f"], capture_output=True, text=True, check=True).stdout
    liste = []
    for block in out.split("\x1e"):
        if not block.strip():
            continue
        h, zeit, text, rest = block.split("\x1f", 3)
        dateien = [z for z in rest.splitlines() if z.strip()]
        liste.append({"sha": h, "zeit": dt.datetime.fromisoformat(zeit), "ki": zuordnen(text, streng),
                      "betreff": text.split("\n", 1)[0], "feedback": ist_feedback(text, dateien)})
    return liste  # neueste zuerst


def bewerten(liste, schwelle=10):
    erg = {}
    for ki, andere in (("claude", "gpt"), ("gpt", "claude")):
        fb = next((c for c in liste if c["ki"] == ki and c["feedback"]), None)
        grenze = fb["zeit"] if fb else None
        fremd = [c for c in liste if c["ki"] == andere and (grenze is None or c["zeit"] > grenze)]
        schritte = list(dict.fromkeys(c["betreff"] for c in fremd))
        erg[ki] = {
            "letztes_feedback": fb["sha"][:7] if fb else None,
            "letztes_feedback_zeit": grenze.isoformat() if grenze else None,
            "unbeantwortete_beitraege_der_anderen_ki": len(schritte),
            "bereich": f"{fremd[-1]['sha'][:7]}..{fremd[0]['sha'][:7]}" if fremd else None,
            "abwesend": len(schritte) >= schwelle,
        }
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schwelle", type=int, default=10)
    ap.add_argument("--tage", type=int, default=14)
    ap.add_argument("--streng", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    erg = bewerten(commits(a.tage, a.streng), a.schwelle)
    if a.json:
        print(json.dumps({"stand": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(), "schwelle": a.schwelle, "ki": erg}, ensure_ascii=False, indent=1))
    else:
        for ki, e in erg.items():
            zustand = "ABWESEND → Pflichten R7" if e["abwesend"] else "aktiv"
            print(f"{ki:6} {zustand:24} letztes Feedback {e['letztes_feedback']}; seitdem "
                  f"{e['unbeantwortete_beitraege_der_anderen_ki']} Beiträge der anderen KI ohne Feedback ({e['bereich'] or '—'})")
    return 3 if any(e["abwesend"] for e in erg.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
