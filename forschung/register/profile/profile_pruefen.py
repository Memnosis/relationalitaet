#!/usr/bin/env python3
"""Validierungsprofile nach anerkannten Standards (S4, Methodenregister STD-D01/D02/D04/D05/S02). Owner: Claude.

Die Standards werden als konkrete, maschinell pruefbare Mindestkriterien fuer die Claude-Register
operationalisiert. Ein bestandenes Kriterium heisst "Mindestanforderung erfuellt", NICHT
"standardkonform" im Sinne einer Zertifizierung. Nicht automatisch pruefbare Teile stehen als
`not_assessed` im Bericht.

Aufruf (Repository-Wurzel):
    python3 forschung/register/profile/profile_pruefen.py            # alle Claude-Register + Negativprobe
    python3 forschung/register/profile/profile_pruefen.py DATEI.json # einzelne Datei
Exit 0, wenn alle Register alle Kriterien erfuellen und die Negativprobe durchfaellt.
"""
import json
import pathlib
import re
import sys

WURZEL = pathlib.Path(__file__).resolve().parents[3]
REG = WURZEL / "forschung/register"
VOK = json.loads((REG / "schema/vokabular.json").read_text(encoding="utf-8"))
CLAUDE_REGISTER = [
    "forschung/register/QUELLEN_REFERENZSET_V0_1.json",
    "forschung/register/VERSIONSMANIFEST_V0_1.json",
    "forschung/register/TESTREGISTER_V0_1.json",
    "forschung/register/PROMPT_INVENTAR_V0_1.json",
    "forschung/register/beispiele/CLAIMS_BEISPIELE_V0_1.json",
    "forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json",
    "forschung/register/PRIORITAETEN_CLAUDE_V0_1.json",
]
ID_FELDER = ("source_id", "claim_id", "test_id", "adresse", "pfad", "datei", "id")
# Primaer-ID je Listentyp (sonst wuerden z. B. Claims ueber ihre source_id gezaehlt)
PRIMAER = {"werke": "source_id", "claims": "claim_id", "tests": "test_id", "felder": "adresse"}
LISTEN = ("werke", "claims", "tests", "dateien", "felder", "eintraege")
STATUS_WERTE = {w for k in ("quellenstatus", "evidenz", "redaktion", "vertraulichkeit", "fachliche_pruefung",
                            "prompt_freigabe", "prompt_ausfuehrung") for w in VOK[k]["werte"]}


def datensaetze(d):
    for k in LISTEN:
        if isinstance(d.get(k), list):
            return k, d[k]
    return None, []


def kriterien(d):
    """Liefert {kriterium: (ok, hinweis)}."""
    erg = {}
    meta_ok = all(k in d for k in ("schema_version",)) and any(k in d for k in ("erzeugt_am", "stand"))
    erg["FAIR-F2 Metadaten (schema_version, Zeitpunkt)"] = (meta_ok, "schema_version und erzeugt_am/stand")
    liste_name, liste = datensaetze(d)
    if liste:
        felder = (PRIMAER[liste_name],) if liste_name in PRIMAER else ID_FELDER
        mit_id = [r for r in liste if isinstance(r, dict) and any(r.get(f) for f in felder)]
        ids = [next(r.get(f) for f in felder if r.get(f)) for r in mit_id]
        erg["FAIR-F1 eindeutige IDs je Datensatz"] = (len(mit_id) == len(liste) and len(set(ids)) == len(ids),
                                                      f"{len(mit_id)}/{len(liste)} mit ID, {len(set(ids))} eindeutig")
    else:
        erg["FAIR-F1 eindeutige IDs je Datensatz"] = (False, "keine Datensatzliste gefunden")
    text = json.dumps(d, ensure_ascii=False)
    erg["FAIR-R1.2 / PROV wasDerivedFrom (Quelle mit Hash, DOI oder Commit)"] = (
        bool(re.search(r'"(source_commit|quelle_sha256|quelle_doi|sha256|quelle_commit)"', text)), "Herkunftsanker")
    erg["PROV wasAttributedTo (owner)"] = ("owner" in d or "erzeugt_von" in d, "owner/erzeugt_von")
    erg["PROV wasGeneratedBy (Werkzeug oder Methode)"] = (
        any(k in d for k in ("werkzeug", "methode", "quelle", "regel", "geltung")), "werkzeug/methode")
    werte = set(re.findall(r'"(?:status|stufe|redaktion|vertraulichkeit|public_release|prompt_execution_status|'
                           r'datei_zugang|belegpruefung|fachliche_pruefung)":\s*"([^"]+)"', text))
    unbekannt = sorted(w for w in werte if w not in STATUS_WERTE)
    erg["FAIR-I1 Statuswerte aus gemeinsamem Vokabular"] = (not unbekannt, f"unbekannt: {unbekannt}" if unbekannt else "ok")
    lizenz_noetig = liste_name == "werke"
    erg["FAIR-R1.1 Lizenz bei Quellen"] = (
        (not lizenz_noetig) or all(v.get("lizenz") for w in liste for v in w.get("versionen", [])), "lizenz je Version")
    sv = str(d.get("schema_version", ""))
    erg["SemVer: schema_version name/MAJOR.MINOR[.PATCH]"] = (bool(re.fullmatch(r"[a-z0-9-]+/\d+\.\d+(\.\d+)?", sv)), sv)
    erg["DCAT intern/oeffentlich getrennt (keine internen Datensaetze in main)"] = (
        '"vertraulichkeit": "intern"' not in text, "kein Datensatz mit vertraulichkeit=intern")
    return erg


def pruefe(pfad):
    d = json.loads(pathlib.Path(pfad).read_text(encoding="utf-8"))
    return kriterien(d)


NEGATIVPROBE = {"werke": [{"titel": "ohne ID", "versionen": [{"doi": "x"}]}, {"source_id": "A"}, {"source_id": "A"}],
                "status": "verifiziert_irgendwie", "vertraulichkeit": "intern", "schema_version": "v1"}


def main(argv):
    dateien = argv[1:] or CLAUDE_REGISTER
    alle_ok, bericht = True, {}
    for p in dateien:
        erg = pruefe(WURZEL / p if not pathlib.Path(p).is_absolute() else p)
        bericht[p] = {k: {"ok": ok, "hinweis": h} for k, (ok, h) in erg.items()}
        fehl = [k for k, (ok, _) in erg.items() if not ok]
        alle_ok &= not fehl
        print(f"{'OK    ' if not fehl else 'LUECKE'} {p}" + (f"  -> {fehl}" if fehl else ""))
    if not argv[1:]:
        neg = kriterien(NEGATIVPROBE)
        durchgefallen = [k for k, (ok, _) in neg.items() if not ok]
        print(f"Negativprobe: {len(durchgefallen)}/{len(neg)} Kriterien korrekt nicht erfuellt")
        alle_ok &= len(durchgefallen) >= 6
    print("not_assessed: SHACL (keine RDF-Daten), FAIR-A1 Abrufbarkeit externer Links (Netzpruefung), "
          "ISO/IEC 25010, NIST AI RMF (nicht maschinell pruefbar)")
    print("Ergebnis:", "OK" if alle_ok else "LUECKEN")
    return 0 if alle_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
