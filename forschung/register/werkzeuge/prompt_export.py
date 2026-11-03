#!/usr/bin/env python3
"""Inventar und bereinigter Export der Prompt-Texte in oeffentlichen Aufgaben-Registern. Owner: Claude.

Hintergrund: Review W07 (CLAUDE_REVIEW_WEBSITE.md) und GPT-Changelog `86fb9db`. Mehrere
oeffentliche JSON-Dateien auf `main` enthalten vollstaendige `meta_prompt`-Texte ohne Freigabe.
Ausblenden in der Website schuetzt die Rohdaten nicht.

Dieses Werkzeug AENDERT KEINE Originaldatei.
  --inventar AUS.json      schreibt nur Kennzahlen und Hashes (keine Prompt-Inhalte)
  --export ORDNER          schreibt bereinigte Kopien ausserhalb des Repositorys:
                           jedes Prompt-Feld wird durch einen Verweis ersetzt
                           {"entfernt": true, "sha256": <Hash des Originaltexts>,
                            "public_release": "not_approved", "prompt_execution_status": "not_run"},
                           ausser der Eintrag hat public_release = approved UND
                           prompt_execution_status = passed.
Ob die bereinigten Fassungen die Originale auf `main` ersetzen, entscheidet Nils (DEC-PROMPT-01).

Aufruf (Repository-Wurzel):
    python3 forschung/register/werkzeuge/prompt_export.py --inventar forschung/register/PROMPT_INVENTAR_V0_1.json
    python3 forschung/register/werkzeuge/prompt_export.py --export /privat/export
"""
import argparse
import datetime as dt
import hashlib
import json
import pathlib
import subprocess
import sys

WURZEL = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                                     check=True).stdout.strip()).resolve()
DATEIEN = ["forschung/website/MITMACH_TASKS.json", "forschung/website/GEOKI_INTEROP_MEILENSTEINE.json",
           "forschung/minimal-ki/beobachter-v0_1/TASKKARTEN.json"]


def eintraege(daten):
    if isinstance(daten, list):
        return daten
    return next(v for v in daten.values() if isinstance(v, list))


def freigegeben(e):
    return e.get("public_release") == "approved" and e.get("prompt_execution_status") == "passed"


def prompt_felder(e):
    return [k for k in e if "prompt" in k.lower() and k not in ("public_release", "prompt_execution_status")
            and isinstance(e[k], str)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventar")
    ap.add_argument("--export")
    a = ap.parse_args()
    if not (a.inventar or a.export):
        ap.error("--inventar oder --export angeben")
    commit = subprocess.run(["git", "-C", str(WURZEL), "rev-parse", "--short", "HEAD"], capture_output=True,
                            text=True).stdout.strip()
    inventar = []
    for rel in DATEIEN:
        roh = (WURZEL / rel).read_bytes()
        daten = json.loads(roh)
        liste = eintraege(daten)
        info = {"datei": rel, "sha256": hashlib.sha256(roh).hexdigest(), "eintraege": len(liste),
                "mit_prompt_text": 0, "freigegeben_und_getestet": 0, "prompt_zeichen": 0, "ids_mit_prompt": []}
        for e in liste:
            felder = prompt_felder(e)
            if felder:
                info["mit_prompt_text"] += 1
                info["ids_mit_prompt"].append(e.get("id"))
                info["prompt_zeichen"] += sum(len(e[k]) for k in felder)
            if freigegeben(e):
                info["freigegeben_und_getestet"] += 1
            elif a.export:
                for k in felder:
                    e[k] = {"entfernt": True, "sha256": hashlib.sha256(e[k].encode("utf-8")).hexdigest(),
                            "public_release": e.get("public_release", "not_approved"),
                            "prompt_execution_status": e.get("prompt_execution_status", "not_run")}
        inventar.append(info)
        if a.export:
            ziel = pathlib.Path(a.export).resolve()
            if ziel == WURZEL or WURZEL in ziel.parents:
                sys.exit("Abbruch: Export nur ausserhalb des Repositorys (Entscheidung DEC-PROMPT-01 steht aus).")
            (ziel / rel).parent.mkdir(parents=True, exist_ok=True)
            (ziel / rel).write_text(json.dumps(daten, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if a.inventar:
        pathlib.Path(a.inventar).write_text(json.dumps({
            "schema_version": "prompt-inventar/0.1", "owner": "claude", "source_commit": commit,
            "erzeugt_am": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "hinweis": "Nur Kennzahlen und Hashes, keine Prompt-Inhalte. Originale unveraendert.",
            "dateien": inventar}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps([{k: i[k] for k in ("datei", "eintraege", "mit_prompt_text", "freigegeben_und_getestet")}
                      for i in inventar], ensure_ascii=False))


if __name__ == "__main__":
    main()
