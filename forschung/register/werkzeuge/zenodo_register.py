#!/usr/bin/env python3
"""Zenodo-Quellenregister fuer die Werke von Nils Sautter erzeugen (K2, Zyklus KI-2026-11-03-001).

Owner: Claude (Daten-KI). Nur Standardbibliothek.

Ablauf:
1. Zenodo-API abfragen (alle Versionen) und Records mit Autor "Sautter, Nils" sammeln.
2. Optional (--pruefen DIR): jede Datei nach DIR herunterladen, Groesse und MD5 gegen
   Zenodo pruefen, eigenen SHA-256 berechnen. DIR liegt ausserhalb des Repositorys;
   es werden keine Werkdateien nach Git kopiert.
3. Repository-Dateien per SHA-256 mit den Zenodo-Dateien abgleichen (bytegleich).
4. Register als JSON schreiben.

Aufruf (aus dem Repository-Wurzelordner):
    python3 forschung/register/werkzeuge/zenodo_register.py --pruefen /tmp/zenodo \
        --aus forschung/register/QUELLEN_ZENODO_V0_1.json

Statusbedeutung (siehe forschung/register/schema/vokabular.json):
- datei_zugang = digital_verifiziert: Datei wurde abgerufen, Groesse und MD5 stimmen.
- belegpruefung = pruefung_ausstehend: einzelne Aussagen (Claims) im Werk sind NICHT geprueft.
- fachliche_pruefung = nicht_geprueft: Veroeffentlichung ist kein fachlicher Nachweis.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.parse
import urllib.request

API = "https://zenodo.org/api/records"
AUTOR = "Sautter, Nils"
SCHEMA_VERSION = "quellen-zenodo/0.1"


def hole(url, versuche=4):
    for i in range(versuche):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # Netzwerkfehler: mit Pause erneut versuchen
            if i == versuche - 1:
                raise
            time.sleep(2 ** (i + 1))


def records_holen():
    q = urllib.parse.quote(f'"{AUTOR}"')
    gesammelt, seite, gesamt = {}, 1, None
    while True:
        d = hole(f"{API}?q={q}&all_versions=true&sort=mostrecent&size=25&page={seite}")
        gesamt = d["hits"]["total"]
        treffer = d["hits"]["hits"]
        if not treffer:
            break
        for r in treffer:
            if any(AUTOR in (c.get("name") or "") for c in r["metadata"].get("creators", [])):
                gesammelt[r["id"]] = r
        seite += 1
    return list(gesammelt.values()), gesamt


def datei_pruefen(record_id, f, ordner):
    ziel = pathlib.Path(ordner) / str(record_id) / f["key"]
    ziel.parent.mkdir(parents=True, exist_ok=True)
    if not (ziel.exists() and ziel.stat().st_size == f.get("size")):
        subprocess.run(["curl", "-sS", "-L", "-m", "300", "--retry", "3", "-o", str(ziel),
                        f["links"]["self"]], check=False)
    daten = ziel.read_bytes() if ziel.exists() else b""
    md5 = hashlib.md5(daten).hexdigest()
    return {
        "groesse_ok": len(daten) == f.get("size"),
        "md5_ok": "md5:" + md5 == f.get("checksum"),
        "sha256_eigener_download": hashlib.sha256(daten).hexdigest(),
    }


def repo_hashes(wurzel):
    dateien = subprocess.run(["git", "-C", str(wurzel), "ls-files"], capture_output=True,
                             text=True, check=True).stdout.splitlines()
    out = {}
    for p in dateien:
        pfad = pathlib.Path(wurzel) / p
        if pfad.is_file():
            out.setdefault(hashlib.sha256(pfad.read_bytes()).hexdigest(), []).append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pruefen", help="Download-Ordner ausserhalb des Repos; ohne Angabe nur Metadaten")
    ap.add_argument("--aus", required=True, help="Ausgabedatei JSON")
    a = ap.parse_args()

    wurzel = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                                         text=True, check=True).stdout.strip())
    commit = subprocess.run(["git", "-C", str(wurzel), "rev-parse", "--short", "HEAD"], capture_output=True,
                            text=True).stdout.strip()
    jetzt = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    records, gesamt = records_holen()
    git_sha = repo_hashes(wurzel)

    werke = {}
    for r in sorted(records, key=lambda r: (r["metadata"].get("publication_date", ""), r["id"])):
        m = r["metadata"]
        konzept = str(r.get("conceptrecid") or r["id"])
        w = werke.setdefault(konzept, {
            "source_id": f"SRC-ZEN-{konzept}",
            "concept_doi": r.get("conceptdoi"),
            "titel": m.get("title"),
            "autoren": [c.get("name") for c in m.get("creators", [])],
            "versionen": [],
            "status": {
                "datei_zugang": "pruefung_ausstehend",
                "belegpruefung": "pruefung_ausstehend",
                "fachliche_pruefung": "nicht_geprueft",
            },
        })
        dateien = []
        for f in r.get("files", []):
            eintrag = {"name": f["key"], "groesse_bytes": f.get("size"),
                       "md5_zenodo": (f.get("checksum") or "").replace("md5:", "")}
            if a.pruefen:
                p = datei_pruefen(r["id"], f, a.pruefen)
                eintrag.update(p)
                eintrag["in_git_bytegleich"] = git_sha.get(p["sha256_eigener_download"], [])
            dateien.append(eintrag)
        w["versionen"].append({
            "record_id": r["id"],
            "doi": r.get("doi"),
            "version": m.get("version"),
            "veroeffentlicht": m.get("publication_date"),
            "lizenz": (m.get("license") or {}).get("id"),
            "zugang": m.get("access_right"),
            "sprache": m.get("language"),
            "dateien": dateien,
        })

    for w in werke.values():
        alle = [d for v in w["versionen"] for d in v["dateien"]]
        if a.pruefen and alle and all(d.get("md5_ok") and d.get("groesse_ok") for d in alle):
            w["status"]["datei_zugang"] = "digital_verifiziert"
            w["status"]["datei_zugang_nachweis"] = {"methode": "zenodo_api_download_md5", "datum": jetzt,
                                                   "pruefer": "claude"}

    register = {
        "schema_version": SCHEMA_VERSION,
        "erzeugt_am": jetzt,
        "erzeugt_von": "claude",
        "source_commit": commit,
        "quelle": {"api": API, "abfrage": f'"{AUTOR}", all_versions=true', "treffer_gesamt": gesamt},
        "hinweis": ("Veroeffentlicht heisst nicht fachlich geprueft. datei_zugang bezieht sich nur auf "
                    "Abruf und Integritaet der Dateien; einzelne Aussagen sind pruefung_ausstehend."),
        "zaehlung": {
            "werke_konzepte": len(werke),
            "records_alle_versionen": len(records),
            "dateien": sum(len(v["dateien"]) for w in werke.values() for v in w["versionen"]),
            "werke_mit_mehreren_versionen": sum(1 for w in werke.values() if len(w["versionen"]) > 1),
        },
        "werke": sorted(werke.values(), key=lambda w: w["versionen"][0]["veroeffentlicht"] or ""),
    }
    if a.pruefen:
        alle = [d for w in werke.values() for v in w["versionen"] for d in v["dateien"]]
        register["zaehlung"]["dateien_md5_ok"] = sum(1 for d in alle if d.get("md5_ok") and d.get("groesse_ok"))
        register["zaehlung"]["dateien_in_git_bytegleich"] = sum(1 for d in alle if d.get("in_git_bytegleich"))
    pathlib.Path(a.aus).write_text(json.dumps(register, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(register["zaehlung"], ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
