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
RE_TYP = re.compile(r"\b(PRJ|CYC|RST|REC|RES|PAR|PAT)\b")
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
        for pm in RE_PFAD.finditer(z):
            seq = [norm_adr(x) for x in RE_ADR.findall(pm.group(1))]
            typ = RE_TYP.search(z)
            if not typ:  # Typ steht in PDF-Konvertierungen oft auf der Zeile davor („SOZ : CYC :“)
                vorher = next((zeilen[j] for j in range(i - 1, max(i - 3, -1), -1) if zeilen[j].strip()), "")
                if re.search(r":\s*(PRJ|CYC|RST|REC|RES|PAR|PAT)\s*:?\s*$", vorher):
                    typ = RE_TYP.search(vorher)
            if len(seq) >= 2:
                pfade.append({"adressen": seq, "typ": typ.group(1) if typ else None, "zeile": z.strip()[:160]})
        treffer = RE_ADR.findall(z)
        if len(treffer) != 1 or "→" in z or "->" in z:
            continue
        a = norm_adr(treffer[0])
        b = begriff_aus_zeile(z, a)
        if b:
            kandidaten.setdefault(a, []).append(b)
    for a, ks in kandidaten.items():
        felder[a] = ks[0]
    # Duplikate von Pfaden entfernen (gleiche Folge + Typ)
    seen, uniq = set(), []
    for p in pfade:
        k = (tuple(p["adressen"]), p["typ"])
        if k not in seen:
            seen.add(k)
            uniq.append(p)
    return felder, uniq, {a: len(k) for a, k in kandidaten.items()}


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
        felder, pfade, mehrfach = extrahiere(f.read_text(encoding="utf-8"))
        tensoren.append({"id": tid, "titel": titel, "konzept_doi": doi, "fundstelle_hinweis": hinweis,
                         "quelle_md_sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                         "felder": dict(sorted(felder.items())), "anzahl_felder": len(felder), "pfade": pfade,
                         "qualitaet": "maschinell aus PDF-Konvertierung; Sichtprüfung ausstehend",
                         "mehrfach_belegt": {a: n for a, n in mehrfach.items() if n > 1}})
    lf, lp = logik_aus_repo()
    tensoren.append({"id": "T-LOGIK", "titel": "Relationale Logik – der Logik-Tensor 1.0", "konzept_doi": "10.5281/zenodo.19282894",
                     "fundstelle_hinweis": "S. 3–6 (Felder), S. 7 (Pfade)", "quelle": "forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json",
                     "felder": dict(sorted(lf.items())), "anzahl_felder": len(lf), "pfade": lp,
                     "qualitaet": "maschinell + Sichtprüfung S. 3–6, 14–20 (digital_verifiziert)", "mehrfach_belegt": {}})
    out = {"schema_version": "tensoren-publikationen/0.1", "owner": "claude", "erzeugt_am": "2026-11-04",
           "lizenz_quellen": "CC BY 4.0 (Zenodo), Autor Nils Sautter", "hinweis": "Nur kurze Feldbegriffe und Pfade mit DOI; keine Volltexte.",
           "tensoren": tensoren}
    aus.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for t in tensoren:
        print(f"{t['id']:10} Felder {t['anzahl_felder']:2d}/27  Pfade {len(t['pfade']):2d}  {t['titel'][:50]}")


if __name__ == "__main__":
    main()
