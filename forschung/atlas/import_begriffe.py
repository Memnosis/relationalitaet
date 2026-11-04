#!/usr/bin/env python3
"""Begriffsatlas · Import der Begriffslisten aus den Grundlagenwerken (Null · Eins · Zyklus · Trinität). Owner: Claude.

Quelle: Markdown-Fassungen der veröffentlichten Zenodo-Werke (pdftotext -layout). Die Tabellen sind Spaltentext mit
umbrochenen Zellen; der Importer richtet jede Zeile an den Spaltenanfängen der jeweils letzten Kopfzeile aus
(Token = Folge ohne doppelte Leerzeichen; Zuordnung zur nächstlinken Spalte) und fügt umbrochene Zellen zusammen.

Aufruf:  python3 forschung/atlas/import_begriffe.py <md_korpus_ordner> [<ausgabeordner>]
Ausgabe: begriffe_v0_1.jsonl (ein Begriff je Zeile), IMPORT_BERICHT_V0_1.json (Zählungen, Lücken, Dubletten, Querbezüge)
Ohne Korpusordner: SKIP (Exit 77).
"""
import collections
import json
import pathlib
import re
import sys

if len(sys.argv) < 2 or not pathlib.Path(sys.argv[1]).is_dir():
    print("SKIP: Korpusordner fehlt – Exit 77")
    sys.exit(77)
KORPUS = pathlib.Path(sys.argv[1])
AUS = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(__file__).resolve().parent / "daten"
AUS.mkdir(parents=True, exist_ok=True)

WERKE = [
    {"werk": "null_matrix_v1", "titel": "Null-Matrix (18.02.2026)", "doi": "10.5281/zenodo.18683755", "datei": "*null-matrix_r18683755.md",
     "pol": "Rel0", "sprache": "de", "prefix": r"[A-Z]{2,5}", "kopf": r"^\s*ID\s+Term\s+Disziplin",
     "spalten": [("ID", "id"), ("Term", "begriff"), ("Disziplin", "domaene"), ("Quelle", "quelle"), ("Jahr", "jahr"),
                 ("Kern-Aspekt", "beschreibung"), ("Klasse", "klasse"), ("Sub", "subklasse")]},
    {"werk": "null_matrix_v2", "titel": "Null-Matrix (25.02.2026, DE)", "doi": "10.5281/zenodo.18776422", "datei": "*null-matrix_r18776422.md",
     "pol": "Rel0", "sprache": "de", "prefix": r"P", "kopf": r"^\s*P-ID\s+Terminus",
     "spalten": [("P-ID", "id"), ("Terminus", "begriff"), ("Domäne", "domaene"), ("S-Klasse", "subklasse"), ("Kern-Definition", "beschreibung")]},
    {"werk": "null_matrix_v3", "titel": "Null-Matrix (25.02.2026, EN)", "doi": "10.5281/zenodo.18776702", "datei": "*null-matrix_r18776702.md",
     "pol": "Rel0", "sprache": "en", "prefix": r"P", "kopf": r"^\s*P-ID\s+Terminus\s+Domain",
     "spalten": [("P-ID", "id"), ("Terminus", "begriff"), ("Domain", "domaene"), ("Category", "subklasse"), ("Core Definition", "beschreibung")]},
    {"werk": "einheits_matrix", "titel": "EINheits-Matrix (12.03.2026)", "doi": "10.5281/zenodo.18981188", "datei": "*einheits-matrix*_r18981188.md",
     "pol": "Rel1", "sprache": "de", "prefix": r"U", "kopf": r"^\s+Terminus\s+Domäne\s+(Sub-)?Klasse\s+Relationaler",
     "spalten": [("@0", "id"), ("Terminus", "begriff"), ("Domäne", "domaene"), (("Sub-Klasse", "Klasse"), "subklasse"), ("Relationaler", "beschreibung")]},
    {"werk": "einheits_matrix_quellen", "titel": "EINheits-Matrix · Quellentabelle", "doi": "10.5281/zenodo.18981188", "datei": "*einheits-matrix*_r18981188.md",
     "pol": "Rel1", "sprache": "de", "prefix": r"U", "kopf": r"^\s*ID\s+Terminus\s+Primärquelle",
     "spalten": [("ID", "id"), ("Terminus", "begriff"), ("Primärquelle", "quelle"), ("Referenz", "referenz")], "nur_quellen": True},
    {"werk": "trinitaets_matrix", "titel": "Matrix der Trinität (12.03.2026)", "doi": "10.5281/zenodo.18978939", "datei": "*matrix-der-trinit*_r18978939.md",
     "pol": "Trinität", "sprache": "de", "prefix": r"M", "kopf": r"^\s*ID\s+Nr\.\s+Dualismus",
     "spalten": [("ID", "id"), ("Nr.", "nr"), ("Dualismus", "begriff"), ("B (Baseline)", "pol_baseline"), ("I (Identität)", "pol_identitaet"),
                 ("E (Emergenz)", "pol_emergenz"), ("Auflösung", "beschreibung")]},
    {"werk": "trinitaets_matrix_themen", "titel": "Matrix der Trinität · Themen mit Status", "doi": "10.5281/zenodo.18978939",
     "datei": "*matrix-der-trinit*_r18978939.md", "pol": "Trinität", "sprache": "de", "prefix": r"M", "kopf": r"^\s*ID\s+Nr\.\s+Thema",
     "spalten": [("ID", "id"), ("Nr.", "nr"), ("Thema", "begriff"), ("B (Baseline)", "pol_baseline"), ("I (Identität)", "pol_identitaet"),
                 ("E (Emergenz)", "pol_emergenz"), ("Status", "beschreibung")]},
    {"werk": "trinitaets_matrix_struktur", "titel": "Matrix der Trinität · Strukturelle Erweiterung", "doi": "10.5281/zenodo.18978939",
     "datei": "*matrix-der-trinit*_r18978939.md", "pol": "Trinität", "sprache": "de", "prefix": r"M", "kopf": r"^\s*ID\s+Nr\.\s+Klassen-Typ",
     "spalten": [("ID", "id"), ("Nr.", "nr"), ("Klassen-Typ", "begriff"), ("Kern-Struktur", "pol_baseline"), ("Zusatz-Dimension", "pol_emergenz"),
                 ("Erkenntnis", "beschreibung")]},
]
ZYKLUS = {"werk": "zyklus_matrix", "titel": "Zyklus-Matrix (20.03.2026)", "doi": "10.5281/zenodo.19124879", "datei": "*zyklus-matrix*_r19124879.md",
          "pol": "Rel-Rel", "sprache": "de"}
RE_KLASSE = re.compile(r"^\s*((?:I{1,3}|IV)\.?\s*(?:Klasse|Class)\b.*|(?:Klasse|Class)\s+(?:I{1,3})\b.*)$")
RE_TOKEN = re.compile(r"\S+(?: \S+)*")
STATUS = {"✅": "bestaetigt", "🚀": "innovation", "🛡️": "absicherung", "🛡": "absicherung", "⚠️": "unstimmig", "❌": "widerspruch"}


def spaltenanfaenge(kopf, spalten):
    starts = []
    for label, feld in spalten:
        if label == "@0":
            starts.append((0, feld))
            continue
        for lab in (label if isinstance(label, tuple) else (label,)):
            i = kopf.find(lab)
            if i >= 0:
                break
        if i < 0:
            return None
        starts.append((i, feld))
    return sorted(starts)


def zelle_zu(starts, pos):
    feld = starts[0][1]
    for s, f in starts:
        if pos + 2 >= s:
            feld = f
    return feld


def verbinde(teile):
    out = ""
    for t in teile:
        if not out:
            out = t
        elif out.endswith("-") and t[:1].islower():
            out = out[:-1] + t          # Silbentrennung: „Thermody-“ + „namik“
        elif out.endswith("-"):
            out = out + t               # Bindestrich-Kompositum: „Teilchen-“ + „Punkt“
        else:
            out = out + " " + t
    return out.strip()


def lies(spec, zeilen):
    rid = re.compile(r"^\s*(" + spec["prefix"] + r")-\s*(\d{3})?\b")
    starts, klasse, eintraege, block = None, None, [], []

    def schliessen():
        if not block or not starts:
            return
        zellen = collections.defaultdict(list)
        for nr, z in block:
            for m in RE_TOKEN.finditer(z):
                zellen[zelle_zu(starts, m.start())].append(m.group())
        roh_id = "".join(zellen.get("id", []))
        mid = re.match(r"(" + spec["prefix"] + r")-?(\d{3}(?:\.\d+)?)", roh_id.replace(" ", ""))
        if not mid:
            return
        e = {"id": f"{mid.group(1)}-{mid.group(2)}", "zeile": block[0][0], "abschnitt": klasse}
        for f, teile in zellen.items():
            if f != "id":
                e[f] = verbinde(teile)
        rest = " ".join(t for t in zellen.get("id", []) if not re.fullmatch(r"[A-Z]{1,5}-?\d{0,3}(?:\.\d+)?", t))
        if rest:
            e["begriff"] = verbinde([rest, e.get("begriff", "")])
        nummer = e["id"].split("-")[1].split(".")[0]
        if e.get("begriff", "").startswith(nummer + " "):
            e["begriff"] = e["begriff"][len(nummer) + 1:]       # umbrochene ID-Nummer ist in den Begriff gerutscht
        if re.fullmatch(r"[A-Z]{3}", (e.get("domaene") or "")[:3]) and re.match(r"^[A-Z]{3}\s+\S", e.get("domaene") or ""):
            code, rest_d = e["domaene"].split(None, 1)              # Spaltenversatz: „TEC Systemisch“ → Domäne + Subklasse
            alt_sub = e.get("subklasse")
            e["domaene"], e["subklasse"] = code, rest_d
            if alt_sub:
                e["beschreibung"] = verbinde([alt_sub, e.get("beschreibung") or ""])
            e["korrigiert"] = "spaltenversatz"
        for sym, st in STATUS.items():
            for f in list(e):
                if isinstance(e[f], str) and sym in e[f]:
                    e["status"] = st
                    e[f] = e[f].replace(sym, "").strip()
        eintraege.append(e)

    fremder_kopf = re.compile(r"^\s*(?:P-)?ID\s{2,}\S")
    for nr, z in enumerate(zeilen, 1):
        if fremder_kopf.match(z) and not re.search(spec["kopf"], z):
            schliessen()
            block, starts = [], None          # Tabelle eines anderen Typs: nicht mit alten Spalten weiterlesen
            continue
        if re.search(spec["kopf"], z):
            schliessen()
            block = []
            s = spaltenanfaenge(z, spec["spalten"])
            if s:
                starts = s
            continue
        km = RE_KLASSE.match(z)
        if km and len(z.strip()) < 120 and not rid.match(z):
            schliessen()
            block = []
            klasse = km.group(1).strip()
            continue
        if not z.strip() or z.strip() == "---" or z.startswith("Neue Relationalität") or "Seite:" in z:
            schliessen()
            block = []
            continue
        if rid.match(z) and starts:
            schliessen()
            block = [(nr, z)]
        elif block:
            block.append((nr, z))
    schliessen()
    return eintraege


def lies_zyklus(zeilen):
    out = []
    for nr, z in enumerate(zeilen, 1):
        m = re.match(r"^\|\s*(ZM-\d{3})\s*\|(.*)\|\s*$", z)
        if m:
            teile = [x.strip() for x in m.group(2).split("|")]
            if len(teile) >= 4:
                out.append({"id": m.group(1), "zeile": nr, "begriff": teile[0], "koordinate": teile[1].strip("`"),
                            "quelle": teile[2], "beschreibung": " | ".join(teile[3:])})
    return out


def normal(b):
    b = (b or "").lower()
    b = re.sub(r"\(.*?\)", "", b)
    return re.sub(r"[^a-zäöüß0-9]+", " ", b).strip()


def main():
    alle, bericht = [], {"werke": {}}
    quellen_u = {}
    for spec in WERKE + [ZYKLUS]:
        datei = next(iter(sorted(KORPUS.glob(spec["datei"]))), None)
        if not datei:
            bericht["werke"][spec["werk"]] = {"fehler": "Datei nicht gefunden"}
            continue
        zeilen = datei.read_text(encoding="utf-8").splitlines()
        eintr = lies_zyklus(zeilen) if spec is ZYKLUS else lies(spec, zeilen)
        if spec.get("nur_quellen"):
            for e in eintr:
                quellen_u[e["id"]] = {"primaerquelle": e.get("quelle"), "referenz": e.get("referenz")}
            bericht["werke"][spec["werk"]] = {"quellen_zugeordnet": len(quellen_u)}
            continue
        # Dubletten-IDs innerhalb eines Werks: erste Fundstelle behalten, weitere markieren
        gesehen = collections.Counter()
        for e in eintr:
            gesehen[e["id"]] += 1
            e.update({"werk": spec["werk"], "werk_titel": spec["titel"], "doi": spec["doi"], "pol": spec["pol"], "sprache": spec["sprache"],
                      "uid": f'{spec["werk"]}:{e["id"]}' + (f"#{gesehen[e['id']]}" if gesehen[e["id"]] > 1 else "")})
        ids = [e["id"] for e in eintr]
        nums = collections.defaultdict(set)
        for i in ids:
            p, n = i.split("-")
            nums[p].add(int(n.split(".")[0]))
        luecken = {p: [n for n in range(1, max(s) + 1) if n not in s] for p, s in nums.items()}
        bericht["werke"][spec["werk"]] = {"titel": spec["titel"], "doi": spec["doi"], "eintraege": len(eintr),
                                         "eindeutige_ids": len(set(ids)), "doppelte_ids": sorted(i for i, c in collections.Counter(ids).items() if c > 1),
                                         "praefixe": {p: len(s) for p, s in nums.items()},
                                         "luecken": {p: (l if len(l) <= 40 else f"{len(l)} Nummern") for p, l in luecken.items() if l},
                                         "ohne_begriff": sum(1 for e in eintr if not e.get("begriff"))}
        alle.extend(eintr)
    # Spaltenversatz nach links: Domänen-Code am Ende des Begriffs („Gödel’s Incompleteness MAT 0“)
    codes = {c for c, n in collections.Counter(e.get("domaene") for e in alle).items() if c and re.fullmatch(r"[A-Z]{3}", c) and n >= 3}
    for e in alle:
        d = e.get("domaene") or ""
        if d in codes:
            continue
        alle_codes = codes | {"LOG"}
        m = re.match(r"^(.*?)(?:\s|-)(" + "|".join(sorted(alle_codes)) + r")\b(.*)$", e.get("begriff") or "")
        if m and codes:
            alt_sub, alt_beschr = e.get("subklasse"), e.get("beschreibung")
            vorn, hinten = m.group(1), m.group(3).strip()
            e["begriff"] = (vorn + ("-" if (e.get("begriff") or "")[len(vorn):len(vorn) + 1] == "-" else " ") + hinten).strip(" -") if hinten else vorn
            e["domaene"], e["subklasse"] = m.group(2), d or None
            e["beschreibung"] = verbinde([x for x in (alt_sub, alt_beschr) if x])
            e["korrigiert"] = "spaltenversatz_links"
    for e in alle:
        if e["werk"] == "einheits_matrix" and e["id"] in quellen_u:
            e.update(quellen_u[e["id"]])
    # EN-Begriffe der Null-Matrix v3 an v2 hängen (gleiche P-ID)
    en = {e["id"]: e for e in alle if e["werk"] == "null_matrix_v3"}
    for e in alle:
        if e["werk"] == "null_matrix_v2" and e["id"] in en:
            e["begriff_en"] = en[e["id"]].get("begriff")
            e["beschreibung_en"] = en[e["id"]].get("beschreibung")
    # Querbezüge: derselbe Begriff in mehreren Werken / Polen
    nach = collections.defaultdict(list)
    for e in alle:
        if e["sprache"] == "de" and normal(e.get("begriff")):
            nach[normal(e["begriff"])].append(e)
    quer = [{"begriff": k, "werke": sorted({x["werk"] for x in v}), "pole": sorted({x["pol"] for x in v}), "ids": [x["uid"] for x in v]}
            for k, v in nach.items() if len({x["pol"] for x in v}) > 1]
    bericht["gesamt"] = {"eintraege": len(alle), "je_pol": dict(collections.Counter(e["pol"] for e in alle)),
                         "begriffe_eindeutig_de": len(nach), "polübergreifende_begriffe": len(quer)}
    bericht["polübergreifend"] = sorted(quer, key=lambda q: (-len(q["pole"]), q["begriff"]))[:80]
    with (AUS / "begriffe_v0_1.jsonl").open("w", encoding="utf-8") as f:
        for e in alle:
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
    (AUS / "IMPORT_BERICHT_V0_1.json").write_text(json.dumps(bericht, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in bericht.items() if k != "polübergreifend"}, ensure_ascii=False, indent=1))
    print("Polübergreifend (Auswahl):", [(q["begriff"], q["pole"]) for q in bericht["polübergreifend"][:20]])
    print("Gesamt: OK")


if __name__ == "__main__":
    main()
