#!/usr/bin/env python3
"""Extrahiert Fachtensoren (Feldbegriffe je Adresse) und deklarierte Pfade aus Nils Sautters veröffentlichten Werken.
Owner: Claude. Quelle: Markdown-Fassungen der Open-Access-PDFs (Zenodo, CC BY 4.0), privat bei Claude bzw. Nils.
Ausgabe: forschung/tensor/algebra-claude/TENSOREN_PUBLIKATIONEN_V0_1.json (nur kurze Feldbegriffe + Fundstelle + DOI).

Aufruf: python3 extrakt_tensoren.py <md_korpus_ordner> [--aus DATEI]
Grenzen: maschinelle Extraktion aus PDF-Konvertierungen; jede Akte trägt `qualitaet` und muss stichprobenartig
an der Originalseite gegengeprüft werden (Sichtprüfung), bevor ein Feldbegriff als Beleg gilt.
"""
import hashlib
import json
import pathlib
import re
import sys

W = pathlib.Path(__file__).resolve().parents[3]
ADR = r"(NM|ZM|UM)[-‑ ](III|II|I)[-‑ ](α|β|γ)"
RE_ADR = re.compile(r"(?<![A-Za-z])" + ADR + r"(?![A-Za-z])")
RE_PFAD = re.compile(r"((?:" + ADR.replace("(", "(?:") + r")(?:\s*(?:→|->)\s*(?:" + ADR.replace("(", "(?:") + r"))+)")
RE_TYP = re.compile(r"\b(PRJ|CYC|RST|REC|RES|PAR|PAT|TRV|ADP|CON)\b")
RE_PRAEFIX = re.compile(r"\b(HM|ZM|LM|TM|BF|SOZ|NM)\s*:\s*(PRJ|CYC|RST|REC|RES|PAR|PAT|TRV|ADP|CON)\s*:")
PRAEFIX_TENSOR = {"HM": "T-HOLO", "ZM": "T-ZYKLUS", "LM": "T-LOGIK", "SOZ": "T-SOZ19", "BF": "T-BF", "TM": "T-TM"}
RE_SIG = re.compile(r"SIG\[([^\]]+)\]\s*=?\s*(\{[^}]*\})?")
NEUTRAL = re.compile(r"^(Baseline|Emergen|Identit|Emergence|Identity)[-\s]", re.I)

WERKE = [  # (id, Datei-Muster, Titel, Konzept-DOI, Seite/Abschnitt-Hinweis)
    ("T-NEUTRAL", "tensor-basics-grundlagen", "Tensor Basics / Grundlagen", "10.5281/zenodo.19152183", "Abschnitt 12, Tabellen"),
    ("T-HOLO", "holographie-matrix", "Holographie-Matrix", "10.5281/zenodo.19133278", "Feldtabellen und Achsen"),
    ("T-ZYKLUS", "zyklus-matrix", "Zyklus-Matrix (Rel-Rel)", "10.5281/zenodo.19124879", "ZM-Felder"),
    ("T-SOZ", "soziation-assoziation-dissoziation", "Soziation – Assoziation/Dissoziation als Komplementäre", "10.5281/zenodo.19406996", "Tabelle SM-*"),
    ("T-SOZ19", "soziation-1-9", "Soziation 1.9", "10.5281/zenodo.21660268", "Feld- und Pfadabschnitte"),
    ("T-FELD", "tensor-field-theory", "Tensor Field Theory / Feld-Theorie", "10.5281/zenodo.19153910", "Kodierungsbeispiele"),
]


def norm_adr(m):
    return f"{m[0]}-{m[1]}-{m[2]}"


def begriff_aus_zeile(z, adr):
    """Ersten plausiblen Fachbegriff nach der Adresse in derselben Zeile finden."""
    z = z.replace("**", "").replace("`", "")
    i = z.find(adr.split("-")[0])
    rest = z[i:]
    rest = RE_ADR.sub("", rest, count=1)
    teile = [p.strip(" :·—–-*|\t") for p in re.split(r"\||·|—|:(?=\s)", rest)]
    for p in teile:
        p = re.sub(r"\s+", " ", p).strip()
        if 3 <= len(p) <= 90 and not RE_ADR.search(p) and not NEUTRAL.match(p) and not p.startswith(("←", "*")):
            return p
    return None


def extrahiere(text):
    felder, kandidaten = {}, {}
    pfade = []
    zeilen = text.split("\n")
    for i, z in enumerate(zeilen):
        if "SIG[" in z or re.search(r"\bAX\s*=", z):
            continue  # Signaturzeilen: Hauptachse wird separat als Signatur erfasst, nicht als eigener Pfad
        for pm in RE_PFAD.finditer(z):
            seq = [norm_adr(x) for x in RE_ADR.findall(pm.group(1))]
            typ = RE_TYP.search(z)
            if not typ:  # Typ steht in PDF-Konvertierungen oft auf der Zeile davor („SOZ : CYC :“)
                vorher = next((zeilen[j] for j in range(i - 1, max(i - 3, -1), -1) if zeilen[j].strip()), "")
                if re.search(r":\s*(PRJ|CYC|RST|REC|RES|PAR|PAT|TRV|ADP|CON)\s*:?\s*$", vorher):
                    typ = RE_TYP.search(vorher)
            if len(seq) >= 2:
                pm2 = RE_PRAEFIX.search(z) or (RE_PRAEFIX.search(vorher) if not RE_TYP.search(z) and 'vorher' in dir() else None)
                if pm2 is None:
                    vz = next((zeilen[j] for j in range(i - 1, max(i - 3, -1), -1) if zeilen[j].strip()), "")
                    pm2 = RE_PRAEFIX.search(vz)
                pfade.append({"adressen": seq, "typ": typ.group(1) if typ else None, "zeile": z.strip()[:160],
                              "praefix": pm2.group(1) if pm2 else None})
        treffer = RE_ADR.findall(z)
        if len(treffer) != 1 or "→" in z or "->" in z:
            continue
        a = norm_adr(treffer[0])
        b = begriff_aus_zeile(z, a)
        if b:
            kandidaten.setdefault(a, []).append(b)
    for a, ks in kandidaten.items():
        felder[a] = ks[0]
    signaturen = []
    for i, z in enumerate(zeilen):
        m = RE_SIG.search(z)
        if not m or "Thema" in m.group(1):
            continue
        block = " ".join(x.strip() for x in zeilen[i:i + 4])
        typen = re.search(r"SIG\[[^\]]+\]\s*=?\s*\{([^}]*)\}", block)
        ax = re.search(r"AX\s*=\s*\{([^}]*)\}", block)
        dom = re.search(r"DOM\s*=\s*\{([^}]*)\}", block)
        signaturen.append({"name": m.group(1).strip(), "typen": [x.strip() for x in typen.group(1).split(",")] if typen else [],
                           "ax": [norm_adr(x) for x in RE_ADR.findall(ax.group(1))] if ax else [], "ax_text": ax.group(1).strip() if ax else None,
                           "dom": [x.strip() for x in dom.group(1).split(",")] if dom else []})
    # Duplikate von Pfaden entfernen (gleiche Folge + Typ)
    seen, uniq = set(), []
    for p in pfade:
        k = (tuple(p["adressen"]), p["typ"], p.get("praefix"))
        if k not in seen:
            seen.add(k)
            uniq.append(p)
    sig_uniq = {json.dumps(s, sort_keys=True, ensure_ascii=False): s for s in signaturen}
    return felder, uniq, {a: len(k) for a, k in kandidaten.items()}, list(sig_uniq.values())


def logik_aus_repo():
    d = json.loads((W / "forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json").read_text(encoding="utf-8"))
    felder = {}
    for f in d["felder"]:
        a = f.get("feld") or f.get("adresse") or f.get("id")
        felder[a.replace("‑", "-")] = f.get("begriff") or f.get("term") or f.get("name")
    pfade = []
    for p in d.get("lm_pfade", []):
        seq = [norm_adr(x) for x in RE_ADR.findall(p["code"])]
        pfade.append({"adressen": seq, "typ": p.get("typ"), "zeile": p["code"], "seiten": p.get("seiten")})
    return felder, pfade


def main():
    korpus = pathlib.Path(sys.argv[1])
    aus = pathlib.Path(sys.argv[sys.argv.index("--aus") + 1]) if "--aus" in sys.argv else W / "forschung/tensor/algebra-claude/TENSOREN_PUBLIKATIONEN_V0_1.json"
    tensoren = []
    for tid, muster, titel, doi, hinweis in WERKE:
        dateien = sorted(korpus.glob(f"*{muster}*.md"))
        if not dateien:
            continue
        f = dateien[-1]
        felder, pfade, mehrfach, sigs = extrahiere(f.read_text(encoding="utf-8"))
        tensoren.append({"id": tid, "titel": titel, "konzept_doi": doi, "fundstelle_hinweis": hinweis,
                         "quelle_md_sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                         "felder": dict(sorted(felder.items())), "anzahl_felder": len(felder), "pfade": pfade,
                         "signaturen": sigs, "qualitaet": "maschinell aus PDF-Konvertierung; Sichtprüfung ausstehend",
                         "mehrfach_belegt": {a: n for a, n in mehrfach.items() if n > 1}})
    lf, lp = logik_aus_repo()
    lsig = []
    for s in [{"name": "LM", "typen": ["PRJ", "CYC", "RST"], "ax": ["NM-I-γ", "ZM-II-γ", "UM-II-γ"], "ax_text": "S. 7", "dom": ["γ-Relation", "II-Kreislauf", "ZM-Emergenz"]}]:
        lsig.append(s)
    tensoren.append({"id": "T-LOGIK", "signaturen": lsig, "titel": "Relationale Logik – der Logik-Tensor 1.0", "konzept_doi": "10.5281/zenodo.19282894",
                     "fundstelle_hinweis": "S. 3–6 (Felder), S. 7 (Pfade)", "quelle": "forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json",
                     "felder": dict(sorted(lf.items())), "anzahl_felder": len(lf), "pfade": lp,
                     "qualitaet": "maschinell + Sichtprüfung S. 3–6, 14–20 (digital_verifiziert)", "mehrfach_belegt": {}})
    # Pfade mit Herkunftskürzel (z. B. „HM : CYC : …“ in der Feldtheorie) dem bezeichneten Tensor zuordnen
    nach_id = {t["id"]: t for t in tensoren}
    for t in list(tensoren):
        bleiben = []
        for p in t["pfade"]:
            ziel = PRAEFIX_TENSOR.get(p.get("praefix") or "")
            if ziel and ziel != t["id"]:
                if ziel not in nach_id:
                    nach_id[ziel] = {"id": ziel, "titel": {"T-BF": "Bedeutungsformung (in Soziation 1.9)", "T-TM": "TM (Bedeutung des Kürzels offen)"}.get(ziel, ziel),
                                     "konzept_doi": None, "fundstelle_hinweis": "nur zitiert", "felder": {}, "anzahl_felder": 0, "pfade": [],
                                     "signaturen": [], "qualitaet": "nur aus Zitat in anderem Werk", "mehrfach_belegt": {}}
                    tensoren.append(nach_id[ziel])
                q = dict(p); q["zitiert_in"] = t["id"]
                nach_id[ziel]["pfade"].append(q)
            else:
                bleiben.append(p)
        t["pfade"] = bleiben
    for t in tensoren:
        seen, uniq = set(), []
        for p in t["pfade"]:
            k = (tuple(p["adressen"]), p["typ"])
            if k not in seen:
                seen.add(k); uniq.append(p)
        t["pfade"] = uniq
    out = {"schema_version": "tensoren-publikationen/0.2", "owner": "claude", "erzeugt_am": "2026-11-04",
           "lizenz_quellen": "CC BY 4.0 (Zenodo), Autor Nils Sautter", "hinweis": "Nur kurze Feldbegriffe und Pfade mit DOI; keine Volltexte.",
           "tensoren": tensoren}
    aus.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for t in tensoren:
        print(f"{t['id']:10} Felder {t['anzahl_felder']:2d}/27  Pfade {len(t['pfade']):2d}  Signaturen {len(t.get('signaturen', []))}  {t['titel'][:45]}")


if __name__ == "__main__":
    main()
