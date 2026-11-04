#!/usr/bin/env python3
"""Abruf des Formelbestands aus Wikidata (CC0) – reproduzierbarer Erzeuger des Rohdatensatzes.

Auswahl: alle Items mit definierender Formel (P2534) UND mindestens einem Symbol (P7235) mit
Qualifikator „Symbol steht für“ (P9758). Für jede referenzierte Größe werden Bezeichnungen (de, en)
und, soweit vorhanden, die ISQ-Dimension (P4020, über SPARQL) geladen.
Ergänzung eines vorhandenen Rohabrufs um Dimensionen:  python3 abruf_wikidata.py --dimensionen-ergaenzen <wikidata_roh.json>

Aufruf:  python3 abruf_wikidata.py <zielordner>
Ausgabe: <zielordner>/wikidata_roh.json  {"abgerufen_am", "items": {QID: {...}}, "groessen": {QID: {...}}}
Netzwerk nötig; ohne Netz: SKIP (Exit 77).
"""
import datetime
import json
import re
import pathlib
import sys
import time
import urllib.parse
import urllib.request

SPARQL = "https://query.wikidata.org/sparql"
API = "https://www.wikidata.org/w/api.php"
UA = "relationalitaet-formelbestand/0.1 (https://github.com/Memnosis/relationalitaet)"
ABFRAGE = """SELECT DISTINCT ?item WHERE {
  ?item wdt:P2534 ?formel .
  ?item p:P7235 ?st . ?st pq:P9758 ?groesse .
}"""


def hole(url, daten=None, versuche=8):
    for i in range(versuche):
        try:
            req = urllib.request.Request(url, data=daten, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as ex:  # noqa: BLE001
            if i == versuche - 1:
                raise
            warte = 2 ** (i + 1)
            if getattr(ex, "code", None) == 429:  # Ratenbegrenzung respektieren
                warte = max(30, int((ex.headers or {}).get("Retry-After") or 30))
            time.sleep(warte)
            print(f"  Wiederholung {i + 1}: {type(ex).__name__}", file=sys.stderr)


def entitaeten(ids, props):
    aus = {}
    for i in range(0, len(ids), 50):
        teil = ids[i:i + 50]
        q = urllib.parse.urlencode({"action": "wbgetentities", "ids": "|".join(teil), "props": props,
                                    "languages": "de|en", "format": "json"})
        aus.update(hole(API + "?" + q).get("entities", {}))
        time.sleep(1.0)
    return aus


ZEICHEN = {"𝖫": "L", "𝖬": "M", "𝖳": "T", "𝖨": "I", "Θ": "Θ", "&#x0398;": "Θ", "𝚯": "Θ", "𝛩": "Θ", "𝖭": "N", "𝖩": "J",
           "L": "L", "M": "M", "T": "T", "I": "I", "N": "N", "J": "J"}


def dimension_aus_mathml(m):
    """ISQ-Dimension (P4020, im SPARQL-Ergebnis als MathML) → normierte Form „L^2 M T^-3“; „1“ = dimensionslos; None = unlesbar."""
    m = re.sub(r"</?(?:math|mrow|mstyle)[^>]*>", "", m).replace("&#x2212;", "-").replace("−", "-")
    m = re.sub(r"<mo[^>]*>\s*-\s*</mo>\s*<mn>", "<mn>-", m)
    teile = []
    for sup, basis, exp, einzel in re.findall(r"(<msup><mi[^>]*>([^<]+)</mi><mn>([^<]+)</mn></msup>)|<mi[^>]*>([^<]+)</mi>", m):
        b = ZEICHEN.get((basis or einzel).strip())
        if b is None:
            return None
        teile.append(f"{b}^{exp}" if sup else b)
    rest = re.sub(r"<msup>.*?</msup>|<mi[^>]*>[^<]+</mi>", "", m).strip()
    if not teile:
        return "1" if re.fullmatch(r"<mn>1</mn>", rest) else None
    return " ".join(teile) if not rest else None


def dimensionen(qids):
    """ISQ-Dimensionen über den SPARQL-Endpunkt (nicht die API, deren Ratenbegrenzung bei Massenabrufen greift)."""
    aus = {}
    for i in range(0, len(qids), 300):
        werte = " ".join("wd:" + q for q in qids[i:i + 300])
        q = f"SELECT ?q ?d WHERE {{ VALUES ?q {{ {werte} }} ?q wdt:P4020 ?d }}"
        r = hole(SPARQL, daten=urllib.parse.urlencode({"query": q, "format": "json"}).encode())
        for b in r["results"]["bindings"]:
            aus.setdefault(b["q"]["value"].rsplit("/", 1)[1], dimension_aus_mathml(b["d"]["value"]))
        time.sleep(1.0)
    return aus


def labels_sparql(qids):
    """Bezeichnungen (de, en) über SPARQL – für Größen, deren Bezeichnung im API-Abruf fehlt."""
    aus = {}
    for i in range(0, len(qids), 300):
        werte = " ".join("wd:" + q for q in qids[i:i + 300])
        q = (f"SELECT ?q ?de ?en WHERE {{ VALUES ?q {{ {werte} }} "
             f"OPTIONAL {{ ?q rdfs:label ?de FILTER(LANG(?de)='de') }} OPTIONAL {{ ?q rdfs:label ?en FILTER(LANG(?en)='en') }} }}")
        r = hole(SPARQL, daten=urllib.parse.urlencode({"query": q, "format": "json"}).encode())
        for b in r["results"]["bindings"]:
            aus[b["q"]["value"].rsplit("/", 1)[1]] = {"de": (b.get("de") or {}).get("value"), "en": (b.get("en") or {}).get("value")}
        time.sleep(1.0)
    return aus


def wert(snak):
    return (snak.get("datavalue") or {}).get("value")


def main():
    if len(sys.argv) < 2:
        print("Aufruf: abruf_wikidata.py <zielordner>  |  abruf_wikidata.py --dimensionen-ergaenzen <wikidata_roh.json>")
        sys.exit(2)
    if sys.argv[1] == "--dimensionen-ergaenzen":
        pfad = pathlib.Path(sys.argv[2])
        roh = json.loads(pfad.read_text(encoding="utf-8"))
        dims = dimensionen(sorted(roh["groessen"]))
        for q, x in roh["groessen"].items():
            x["dimension"] = dims.get(q)
        ohne = sorted({s["groesse"] for it in roh["items"].values() for s in it["symbole"] if s.get("groesse")}
                      - {q for q, x in roh["groessen"].items() if x.get("de") or x.get("en")})
        for q, lab in labels_sparql(ohne).items():
            roh["groessen"].setdefault(q, {"dimension": None}).update(lab)
        nd = dimensionen(ohne)
        for q in ohne:
            if q in roh["groessen"] and roh["groessen"][q].get("dimension") is None:
                roh["groessen"][q]["dimension"] = nd.get(q)
        print(f"Bezeichnungen nachgeladen: {len(ohne)}")
        roh["dimensionen_abgerufen_am"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        pfad.write_text(json.dumps(roh, ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Dimensionen: {sum(1 for v in dims.values() if v)} lesbar, {sum(1 for v in dims.values() if not v)} unlesbar, "
              f"{len(roh['groessen']) - len(dims)} ohne P4020")
        return
    ziel = pathlib.Path(sys.argv[1])
    ziel.mkdir(parents=True, exist_ok=True)
    try:
        r = hole(SPARQL + "?" + urllib.parse.urlencode({"query": ABFRAGE, "format": "json"}))
    except Exception as ex:  # noqa: BLE001
        print(f"SKIP: kein Netz/Endpunkt ({type(ex).__name__}) – Exit 77")
        sys.exit(77)
    ids = sorted({b["item"]["value"].rsplit("/", 1)[1] for b in r["results"]["bindings"]})
    print(f"Items: {len(ids)}")
    roh = entitaeten(ids, "labels|claims")
    items, groessen_ids = {}, set()
    for qid, e in roh.items():
        if "missing" in e:
            continue
        cl = e.get("claims", {})
        formeln = [wert(c["mainsnak"]) for c in cl.get("P2534", []) if wert(c["mainsnak"])]
        symbole = []
        for c in cl.get("P7235", []):
            for q in c.get("qualifiers", {}).get("P9758", []):
                v = wert(q)
                if v and wert(c["mainsnak"]):
                    symbole.append({"symbol": wert(c["mainsnak"]), "groesse": v["id"]})
                    groessen_ids.add(v["id"])
        lab = e.get("labels", {})
        items[qid] = {"de": lab.get("de", {}).get("value"), "en": lab.get("en", {}).get("value"),
                      "formeln": formeln, "symbole": symbole}
    print(f"Größen: {len(groessen_ids)}")
    g = entitaeten(sorted(groessen_ids), "labels|claims")
    groessen = {}
    for qid, e in g.items():
        if "missing" in e:
            continue
        lab = e.get("labels", {})
        groessen[qid] = {"de": lab.get("de", {}).get("value"), "en": lab.get("en", {}).get("value"), "dimension": None}
    dims = dimensionen(sorted(groessen))
    for q, x in groessen.items():
        x["dimension"] = dims.get(q)
    out = {"quelle": "Wikidata (CC0)", "abgerufen_am": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "auswahl": ABFRAGE, "items": items, "groessen": groessen}
    (ziel / "wikidata_roh.json").write_text(json.dumps(out, ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    print(f"geschrieben: {ziel / 'wikidata_roh.json'}  ({len(items)} Items, {len(groessen)} Größen)")


if __name__ == "__main__":
    main()
