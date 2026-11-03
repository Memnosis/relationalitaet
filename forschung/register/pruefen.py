#!/usr/bin/env python3
"""Validator fuer Claude-Register (K1, Zyklus KI-2026-11-03-001). Owner: Claude.

Prueft Aussagen (Claims) gegen die Regeln aus schema/claim.schema.json und schema/vokabular.json
sowie die Referenzen auf das Zenodo-Quellenregister. Nur Standardbibliothek; wenn das Paket
`jsonschema` installiert ist, wird zusaetzlich formal gegen das JSON-Schema geprueft.

Aufrufe (aus dem Repository-Wurzelordner):
    python3 forschung/register/pruefen.py                 # Selbsttest: Beispiele gueltig, Negativfaelle ungueltig
    python3 forschung/register/pruefen.py DATEI.json ...  # beliebige Claim-Dateien pruefen
Exit-Code 0 = alles wie erwartet, 1 = Fehler.
"""
import json
import os
import pathlib
import re
import sys

BASIS = pathlib.Path(__file__).resolve().parent
VOK = json.loads((BASIS / "schema/vokabular.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((BASIS / "schema/claim.schema.json").read_text(encoding="utf-8"))
# Oeffentliches Referenzset; ein privates Gesamtregister kann per Umgebungsvariable QUELLEN_REGISTER
# (Pfad ausserhalb des Repositorys) zusaetzlich angegeben werden.
ZENODO = BASIS / "QUELLEN_REFERENZSET_V0_1.json"


def bekannte_quellen():
    ids = set()
    for pfad in (ZENODO, pathlib.Path(os.environ["QUELLEN_REGISTER"]) if os.environ.get("QUELLEN_REGISTER") else None):
        if pfad and pfad.exists():
            ids |= {w["source_id"] for w in json.loads(pfad.read_text(encoding="utf-8"))["werke"]}
    return ids


def werte(kategorie):
    return set(VOK[kategorie]["werte"])


def pruefe_claim(c, quellen):
    """Gibt eine Liste von Fehlermeldungen zurueck (leer = gueltig)."""
    f = []
    for feld in SCHEMA["required"]:
        if feld not in c:
            f.append(f"Pflichtfeld fehlt: {feld}")
    erlaubt = set(SCHEMA["properties"])
    for feld in c:
        if feld not in erlaubt:
            f.append(f"unbekanntes Feld: {feld}")
    if f:
        return f
    if not re.fullmatch(r"CLM-[A-Z0-9]+(-[A-Z0-9]+)*", c["claim_id"]):
        f.append("claim_id hat falsches Format")
    if quellen and c["source_id"] not in quellen:
        f.append(f"source_id nicht im Quellenregister: {c['source_id']}")
    if c["aussageart"] not in werte("aussageart"):
        f.append("aussageart unbekannt")
    if not c.get("fundstelle"):
        f.append("fundstelle leer")

    q = c["quellenstatus"]
    st = q.get("status")
    if st not in werte("quellenstatus"):
        f.append(f"quellenstatus unbekannt oder nicht ASCII: {st!r}")
    if st == "digital_verifiziert":
        for k in ("pruefer", "datum", "nachweis"):
            if not q.get(k):
                f.append(f"digital_verifiziert verlangt {k}")
        pm = q.get("pruefmethode")
        if pm is not None and set(pm) <= {"maschinell"}:
            f.append("digital_verifiziert nicht allein auf maschineller Extraktion (Regel GPT_DISKUSSION_05 §4)")
    if st == "digital_nicht_erreichbar":
        zv = q.get("zugriffsversuch") or {}
        if not all(zv.get(k) for k in ("datum", "methode", "ergebnis")):
            f.append("digital_nicht_erreichbar verlangt dokumentierten zugriffsversuch (datum, methode, ergebnis)")
    if st == "handpruefung_noetig" and not q.get("grund"):
        f.append("handpruefung_noetig verlangt grund")

    e = c["evidenz"]
    stufe = e.get("stufe")
    if stufe not in werte("evidenz"):
        f.append(f"evidenz unbekannt: {stufe!r}")
    if stufe in ("D", "F", "O") and not e.get("nachweis_refs"):
        f.append(f"evidenz {stufe} verlangt nachweis_refs")

    if c["redaktion"] not in werte("redaktion"):
        f.append("redaktion unbekannt")
    if c["vertraulichkeit"] not in werte("vertraulichkeit"):
        f.append("vertraulichkeit unbekannt")
    if c["public_release"] is True and (c["redaktion"] != "freigegeben" or c["vertraulichkeit"] != "oeffentlich"):
        f.append("public_release=true verlangt redaktion=freigegeben und vertraulichkeit=oeffentlich")
    return f


def formal_pruefen(c):
    try:
        import jsonschema
    except ImportError:
        return None
    v = jsonschema.Draft202012Validator(SCHEMA)
    return [e.message for e in v.iter_errors(c)]


def pruefe_datei(pfad, quellen):
    daten = json.loads(pathlib.Path(pfad).read_text(encoding="utf-8"))
    claims = daten["claims"] if isinstance(daten, dict) else daten
    fehler, ids = 0, set()
    for c in claims:
        msg = pruefe_claim(c, quellen)
        if c.get("claim_id") in ids:
            msg.append("claim_id doppelt")
        ids.add(c.get("claim_id"))
        formal = formal_pruefen(c)
        if formal:
            msg += [f"JSON-Schema: {m}" for m in formal]
        if msg:
            fehler += 1
            print(f"  UNGUELTIG {c.get('claim_id')}: " + "; ".join(msg))
    return len(claims), fehler


def selbsttest(quellen):
    ok = True
    n, fehler = pruefe_datei(BASIS / "beispiele/CLAIMS_BEISPIELE_V0_1.json", quellen)
    print(f"Positivbeispiele: {n}, davon ungueltig: {fehler} (erwartet 0)")
    ok &= fehler == 0
    neg = json.loads((BASIS / "beispiele/CLAIMS_NEGATIV_V0_1.json").read_text(encoding="utf-8"))
    for fall in neg["faelle"]:
        msg = pruefe_claim(fall["claim"], quellen)
        formal = formal_pruefen(fall["claim"])
        if formal is not None and fall["erwartet"] != "unbekannte source_id":
            # Das JSON-Schema kennt das Quellenregister nicht; alle anderen Faelle muss es ebenfalls ablehnen.
            if not formal:
                msg_schema = "JSON-Schema akzeptiert faelschlich"
                print(f"  FEHLER Negativfall '{fall['erwartet']}': {msg_schema}")
                ok = False
        abgelehnt = bool(msg)
        print(f"Negativfall '{fall['erwartet']}': {'abgelehnt (richtig)' if abgelehnt else 'AKZEPTIERT (FALSCH)'}"
              + (f" -> {msg[0]}" if msg else ""))
        ok &= abgelehnt
    return ok


def main(argv):
    quellen = bekannte_quellen()
    print(f"Quellenregister: {len(quellen)} Werke; jsonschema: {'ja' if formal_pruefen({}) is not None else 'nein'}")
    if len(argv) > 1:
        gesamt_fehler = 0
        for p in argv[1:]:
            n, fe = pruefe_datei(p, quellen)
            print(f"{p}: {n} Aussagen, {fe} ungueltig")
            gesamt_fehler += fe
        return 1 if gesamt_fehler else 0
    ok = selbsttest(quellen)
    print("Ergebnis: " + ("OK" if ok else "FEHLER"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
