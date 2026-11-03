#!/usr/bin/env python3
"""Abwesenheitserkennung Claude/GPT (Regel R7). Owner: Claude. Nur lesend.

Vorgabe Nils (03.11.2026): Ist eine KI über längere Zyklen abwesend, löst das eine neue
Berichts- und Analysepflicht aus.

Messung (aus Git, nicht von Hand):
- Zuordnung eines Commits: Trailer `Claude-Session:` oder `Co-Authored-By: Claude` → claude;
  Trailer `KI: gpt` → gpt; sonst → gpt (Annahme: Commits ohne Claude-Kennung stammen von
  GPT oder Nils). Grenze: Nils' eigene Commits werden mitgezählt. Abhilfe: GPT setzt
  künftig den Trailer `KI: gpt`; ab dann wird nur noch dieser gezählt (--streng).
- Abwesend ist eine KI, wenn seit ihrem letzten Commit die andere KI aktiv war und
  (a) mindestens STUNDEN Stunden (Standard 12) vergangen sind ODER
  (b) die andere KI mindestens SCHRITTE Arbeitsschritte (Standard 100) gemacht hat ODER
  (c) eine Prüfbitte an sie offen ist (REVIEW_QUEUE_V2, awaiting_response) und mindestens
      BITTE_STUNDEN Stunden (Standard 3) vergangen sind.
- Arbeitsschritt = eindeutige Commit-Betreffzeile. GPT legt oft eine Änderung als mehrere
  Datei-Commits mit gleichem Betreff ab; rohe Commits würden die Schritte überzählen.
- Volle Zyklen (PROGRAMM_100_ZYKLEN_MANIFEST) sind noch zu selten (0 verifiziert), um
  als Maß zu taugen; sobald es welche gibt, kommt (d) „ein voller Zyklus ohne Beitrag“ dazu.

Aufruf: python3 forschung/koordination/werkzeuge/abwesenheit.py [--stunden 12] [--schritte 100] [--bitte-stunden 3] [--json]
Exit 0 = niemand abwesend, 3 = Pflicht ausgelöst (für CI lesbar).
"""
import argparse
import datetime as dt
import json
import pathlib
import subprocess
import sys

W = pathlib.Path(__file__).resolve().parents[3]
QUEUE = W / "forschung/koordination/REVIEW_QUEUE_V2.json"
TRENNER = "\x1e"


def commits(seit_tage=14):
    fmt = f"%H%x1f%cI%x1f%B{TRENNER}"
    out = subprocess.run(["git", "-C", str(W), "log", f"--since={seit_tage} days ago", f"--format={fmt}"],
                         capture_output=True, text=True, check=True).stdout
    liste = []
    for block in out.split(TRENNER):
        block = block.strip("\n")
        if not block:
            continue
        h, zeit, text = block.split("\x1f", 2)
        liste.append({"sha": h, "zeit": dt.datetime.fromisoformat(zeit), "ki": zuordnen(text), "betreff": text.split("\n", 1)[0]})
    return liste  # neueste zuerst


def zuordnen(text, streng=False):
    t = text.lower()
    if "claude-session:" in t or "co-authored-by: claude" in t:
        return "claude"
    if "\nki: gpt" in t or t.startswith("ki: gpt"):
        return "gpt"
    return "unbekannt" if streng else "gpt"


def bewerten(liste, jetzt, stunden, schritte, offene, bitte_stunden=3):
    ergebnis = {}
    for ki, andere in (("claude", "gpt"), ("gpt", "claude")):
        eigene = [c for c in liste if c["ki"] == ki]
        letzte = eigene[0] if eigene else None
        grenze = letzte["zeit"] if letzte else None
        fremd = [c for c in liste if c["ki"] == andere and (grenze is None or c["zeit"] > grenze)]
        std = round((jetzt - grenze).total_seconds() / 3600, 1) if grenze else None
        aktiv_andere = bool(fremd)
        a = aktiv_andere and (std is None or std >= stunden)
        n_schritte = len({c.get("betreff", c["sha"]) for c in fremd})
        b = n_schritte >= schritte
        bitten = offene.get(ki, [])
        cc = bool(bitten) and aktiv_andere and (std is None or std >= bitte_stunden)
        ergebnis[ki] = {
            "letzter_commit": letzte["sha"][:7] if letzte else None,
            "letzter_commit_zeit": grenze.isoformat() if grenze else None,
            "stunden_seit": std,
            "commits_der_anderen_ki_seitdem": len(fremd),
            "arbeitsschritte_der_anderen_ki_seitdem": n_schritte,
            "aeltester_unbesehener_commit": fremd[-1]["sha"][:7] if fremd else None,
            "offene_pruefbitten": bitten,
            "abwesend": a or b or cc,
            "ausloeser": [x for x, w in (("zeit", a), ("schritte", b), ("pruefbitte", cc)) if w],
        }
    return ergebnis


def offene_bitten():
    if not QUEUE.is_file():
        return {}
    d = json.loads(QUEUE.read_text(encoding="utf-8"))
    o = {}
    for r in d.get("requests", []):
        if r.get("status") == "awaiting_response":
            o.setdefault(r.get("target"), []).append(r.get("id"))
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stunden", type=float, default=12)
    ap.add_argument("--schritte", type=int, default=100)
    ap.add_argument("--bitte-stunden", type=float, default=3)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    jetzt = dt.datetime.now(dt.timezone.utc)
    erg = bewerten(commits(), jetzt, a.stunden, a.schritte, offene_bitten(), a.bitte_stunden)
    if a.json:
        print(json.dumps({"stand": jetzt.replace(microsecond=0).isoformat(), "schwellen": {"stunden": a.stunden, "schritte": a.schritte, "bitte_stunden": a.bitte_stunden}, "ki": erg}, ensure_ascii=False, indent=1))
    else:
        for ki, e in erg.items():
            zustand = "ABWESEND → Pflichten R7" if e["abwesend"] else "aktiv"
            print(f"{ki:6} {zustand:24} letzter Commit {e['letzter_commit']} vor {e['stunden_seit']} h; "
                  f"{e['arbeitsschritte_der_anderen_ki_seitdem']} Schritte ({e['commits_der_anderen_ki_seitdem']} Commits) der anderen KI seitdem; offene Prüfbitten {e['offene_pruefbitten'] or '—'}")
    return 3 if any(e["abwesend"] for e in erg.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
