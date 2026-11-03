#!/usr/bin/env python3
"""Versionsmanifest aller Dateien auf `main` (K3, Schritt S2, P0-X3). Owner: Claude.

Je Datei: Pfad, Bereich, Typ, Groesse, SHA-256, Git-Blob, erster und letzter Commit,
Zahl der Commits, Sprachschaetzung (de/en/gemischt), Owner nach Zustaendigkeitsregel.
Dazu:
- bytegleiche Dateien innerhalb des Repositorys (Dubletten, z. B. DQ-003),
- Namensfamilien-KANDIDATEN (gleicher Grundname oder DE/EN-Paar); das ist eine Vermutung,
  keine Feststellung,
- Abgleich mit veroeffentlichten Fassungen: nur "bytegleich ja/nein". Die DOI wird nur genannt,
  wenn das Werk im oeffentlichen Referenzset steht (Anweisung Nils: Gesamtliste intern).
  Ein privates Gesamtregister kann per QUELLEN_REGISTER=<pfad ausserhalb des Repos> einbezogen werden.

Aufruf (Repository-Wurzel, vollstaendige Historie noetig):
    QUELLEN_REGISTER=/privat/QUELLEN_ZENODO_VOLL.json \
        python3 forschung/register/werkzeuge/versionsmanifest.py
"""
import collections
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import subprocess
import unicodedata

WURZEL = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                                     check=True).stdout.strip())
AUS = WURZEL / "forschung/register/VERSIONSMANIFEST_V0_1.json"
REF = WURZEL / "forschung/register/QUELLEN_REFERENZSET_V0_1.json"

DE = set("der die das und ist nicht mit von zu den eine ein auf für sich dem als auch wird werden oder sind".split())
EN = set("the and is not with of to a an on for which as also will be or are this that from".split())
DE_EN = {"rel": "relational", "relationale": "relational", "relationales": "relational", "zeit": "time", "sonnensystem": "solar-system",
         "soziale": "social", "operatoren": "operators", "fraktale": "fractals", "chemie": "chemistry",
         "gravitation": "gravity", "dimensionen": "dimensions", "proteinfaltung": "protein-folding",
         "information": "information", "periodensystem": "periodic-table"}


def git(*a):
    return subprocess.run(["git", "-C", str(WURZEL), *a], capture_output=True, text=True).stdout


def bereich(p):
    if "/" not in p:
        return "hauptordner_original"
    teile = p.split("/")
    if teile[0] == "docs":
        return "website"
    if teile[0] == "forschung":
        return "forschung/" + teile[1]
    return teile[0]


def owner(p):
    if p.startswith("docs/") or p.startswith("forschung/website/"):
        return "gpt"
    if p.startswith(("forschung/register/", "forschung/tensor/logik-claude/")):
        return "claude"
    if p.startswith("forschung/koordination/"):
        return "beide (je Datei)"
    if "/" not in p:
        return "nils (Original)"
    return "offen"


def sprache(text):
    w = re.findall(r"[a-zäöüß]+", text.lower())
    d, e = sum(x in DE for x in w), sum(x in EN for x in w)
    if d + e < 20:
        return "unbestimmt"
    if d > 3 * e:
        return "de"
    if e > 3 * d:
        return "en"
    return "gemischt"


def grundname(p):
    n = pathlib.PurePath(p).stem.lower()
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    n = re.sub(r"[\s_]+", "-", n)
    n = re.sub(r"\(\d+\)|\b(v?\d+([._]\d+)*)\b|(?<=[a-z])\d+$|-txt|final|audit\w*|-de$|_en$|-en$|de$", "", n)
    n = re.sub(r"[\s_]+", "-", n).strip("-")
    teile = [DE_EN.get(t, t) for t in n.split("-") if t and t not in ("de", "en")]
    return "-".join(teile)


def main():
    jetzt = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    commit = git("rev-parse", "--short", "HEAD").strip()
    oeffentlich = {}
    if REF.exists():
        for w in json.loads(REF.read_text(encoding="utf-8"))["werke"]:
            for v in w["versionen"]:
                for d in v["dateien"]:
                    oeffentlich[d.get("sha256_eigener_download")] = v["doi"]
    privat = set()
    if os.environ.get("QUELLEN_REGISTER"):
        for w in json.loads(pathlib.Path(os.environ["QUELLEN_REGISTER"]).read_text(encoding="utf-8"))["werke"]:
            for v in w["versionen"]:
                privat |= {d.get("sha256_eigener_download") for d in v["dateien"]}

    dateien = []
    for p in git("ls-files").splitlines():
        pfad = WURZEL / p
        if not pfad.is_file():
            continue
        daten = pfad.read_bytes()
        sha = hashlib.sha256(daten).hexdigest()
        log = git("log", "--follow", "--format=%h %as", "--", p).split("\n")
        log = [z for z in log if z.strip()]
        eintrag = {
            "pfad": p, "bereich": bereich(p), "owner": owner(p), "typ": pfad.suffix.lstrip(".").lower() or "ohne",
            "groesse_bytes": len(daten), "sha256": sha, "git_blob": git("rev-parse", f"HEAD:{p}").strip(),
            "erster_commit": log[-1] if log else None, "letzter_commit": log[0] if log else None,
            "commits": len(log),
        }
        if eintrag["typ"] in ("md", "html", "txt", "csv", "json"):
            eintrag["sprache"] = sprache(daten.decode("utf-8", "ignore"))
        if privat or oeffentlich:
            eintrag["veroeffentlichte_fassung_bytegleich"] = sha in privat or sha in oeffentlich
            if sha in oeffentlich:
                eintrag["doi_referenzset"] = oeffentlich[sha]
        dateien.append(eintrag)

    nach_sha = collections.defaultdict(list)
    for d in dateien:
        nach_sha[d["sha256"]].append(d["pfad"])
    dubletten = [v for v in nach_sha.values() if len(v) > 1]

    familien = collections.defaultdict(list)
    for d in dateien:
        if d["bereich"] == "hauptordner_original":
            familien[grundname(d["pfad"])].append(d["pfad"])
    familien = {k: v for k, v in familien.items() if len(v) > 1}

    zaehl = collections.Counter(d["bereich"] for d in dateien)
    manifest = {
        "schema_version": "versionsmanifest/0.1", "owner": "claude", "erzeugt_am": jetzt, "source_commit": commit,
        "geltung": "nur Dateien auf main; Zweige und externe Archive nicht enthalten",
        "zaehlung": {"dateien": len(dateien), "nach_bereich": dict(sorted(zaehl.items())),
                     "dubletten_gruppen": len(dubletten), "namensfamilien_kandidaten": len(familien),
                     "bytegleich_mit_veroeffentlichter_fassung": sum(1 for d in dateien
                                                                     if d.get("veroeffentlichte_fassung_bytegleich"))},
        "dubletten_bytegleich": dubletten,
        "namensfamilien_kandidaten": {"hinweis": "Vermutung aus Dateinamen (inkl. DE/EN-Woerterbuch); Beziehung "
                                                 "(Uebersetzung, neuere Fassung, Auszug) ist je Paar zu pruefen",
                                      "gruppen": familien},
        "dateien": dateien,
    }
    AUS.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(manifest["zaehlung"], ensure_ascii=False))
    print("Dubletten:", dubletten)
    print("Familien:", json.dumps(familien, ensure_ascii=False))


if __name__ == "__main__":
    main()
