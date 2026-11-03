#!/usr/bin/env python3
"""Extrakt aus Logik-Tensor 1.0 (Zenodo 10.5281/zenodo.19282895) und Abgleich mit LOGIK_TENSOR_2_1 §4.

Owner: Claude (Daten-KI), Schritt S2 / K5 / P0-X3 / DATA-001. Keine Umdeutung: nur dokumentieren,
was im Original steht, mit Seitenangabe, und mit der 2.1-Arbeitsfassung vergleichen.

Methode:
- Die 27 Feldbegriffe wurden aus dem Layout-Text (pdftotext -layout) der Seiten 3-5 abgelesen
  (Matrix x Modus-Zeile x Spalte). Jeder Begriff wird hier MASCHINELL gegen den Text der
  angegebenen Seite geprueft (Zeilenumbrueche und Silbentrennung normalisiert).
- LM-Pfade, Axiome, Logiksysteme und die Begriffstabelle (Kap. 8) werden per Regex extrahiert.
- Vor allem wird die SHA-256 der PDF gegen forschung/register/QUELLEN_REFERENZSET_V0_1.json geprueft.

Aufruf (Repository-Wurzel; PDF vorher von Zenodo laden):
    python3 forschung/tensor/logik-claude/werkzeuge/logik10_extrakt.py PFAD/Logik-Tensor_1_0.pdf
Benoetigt: pdftotext (poppler-utils).
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

WURZEL = pathlib.Path(__file__).resolve().parents[4]
AUS = WURZEL / "forschung/tensor/logik-claude"
REF = WURZEL / "forschung/register/QUELLEN_REFERENZSET_V0_1.json"
V21 = WURZEL / "forschung/tensor/LOGIK_TENSOR_2_1_FORSCHUNGS-UND_PROMPTEDITION_ENTWURF.md"
DOI = "10.5281/zenodo.19282895"

MATRIX = {"NM": ("Null-Matrix", "Rel0"), "ZM": ("Zyklus-Matrix", "Rel-Rel"), "UM": ("Einheits-Matrix", "Rel1")}
SPALTE = {"I": "Kern", "II": "Kreislauf", "III": "Öffnung"}
MODUS = {"α": "Struktur", "β": "Funktion", "γ": "Relation"}
# (Matrix, Modus) -> [I, II, III], Seite(n) der Tabellenzeile
FELDER = {
    ("NM", "α"): (["Symbolischer Trägerraum", "Syntaxgerüst", "Grenz- und Paradoxraum"], 3),
    ("NM", "β"): (["Axiomatische Setzung", "Ableitungsbereitschaft", "Entscheidungsbereitschaft"], 3),
    ("NM", "γ"): (["Relationale Vorordnung", "Semantischer Möglichkeitsraum", "Offene Geltungsspannung"], 4),
    ("ZM", "α"): (["Inferenzschritt", "Beweisgang", "Modallogische Öffnung"], 4),
    ("ZM", "β"): (["Regelanwendung", "Transformation und Umformung", "Rekursive Entscheidungsprozesse"], 4),
    ("ZM", "γ"): (["Operator der Ableitung", "Syntax-Semantik-Übergang", "Netz logischer Korrespondenzen"], 4),
    ("UM", "α"): (["Theorem", "Kalkül oder System", "Logische Theorieform"], 5),
    ("UM", "β"): (["Geltungsfunktion", "Konsistenz / Vollständigkeit", "Entscheidbarkeitsraum"], 5),
    ("UM", "γ"): (["Äquivalenz und Identität", "Modellklasse", "Offene Korrespondenz logischer Systeme"], 5),
}
SYSTEME = ["Klassische Logik", "Intuitionistische Logik", "Modale Logik", "Mehrwertige Logik",
           "Parakonsistente Logik", "Relevanzlogik", "Algebraische Logik"]


def seite(pdf, nr):
    return subprocess.run(["pdftotext", "-f", str(nr), "-l", str(nr), "-layout", str(pdf), "-"],
                          capture_output=True, text=True).stdout


def norm(t):
    t = t.replace("\u200b", "").replace("\u2010", "-")  # Trennstrich am Zeilenende bleibt erhalten (siehe enthaelt)
    return re.sub(r"\s+", " ", t).lower()


def enthaelt(text, begriff):
    """Begriff gilt als gefunden, wenn alle Woerter in Reihenfolge im (spaltenweise verteilten) Text vorkommen."""
    t = norm(text)
    pos = 0
    for wort in norm(begriff).split():
        wort = wort.strip("/")
        if not wort:
            continue
        i = t.find(wort.rstrip("-"), pos)
        if i < 0:
            # Silbentrennung am Zeilenende in Tabellenspalten: "entscheidungs-" ... "bereitschaft"
            # (dazwischen Text der Nachbarspalten). Beide Teile muessen in Reihenfolge vorkommen.
            for k in range(4, len(wort) - 3):
                a = t.find(wort[:k] + "-", pos)
                if a >= 0 and t.find(wort[k:].lstrip("-"), a) >= 0:
                    i = a
                    break
        if i < 0:
            return False
        pos = i
    return True


def main(pdf):
    pdf = pathlib.Path(pdf)
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    ref = json.loads(REF.read_text(encoding="utf-8"))
    erwartet = [d["sha256_eigener_download"] for w in ref["werke"] for v in w["versionen"] if v["doi"] == DOI
                for d in v["dateien"]]
    if sha not in erwartet:
        sys.exit(f"SHA-256 passt nicht zum Referenzset: {sha}")
    seiten = {n: seite(pdf, n) for n in range(1, 23)}
    voll = "\n".join(seiten[n] for n in sorted(seiten))

    felder = []
    for (m, mod), (begriffe, s) in FELDER.items():
        for spalte, b in zip(("I", "II", "III"), begriffe):
            gefunden = enthaelt(seiten[s], b) or (s == 4 and m == "NM" and enthaelt(seiten[3], b))
            felder.append({"adresse": f"{m}-{spalte}-{mod}", "begriff": b, "matrix": MATRIX[m][0],
                           "schicht": MATRIX[m][1], "spalte": SPALTE[spalte], "modus": MODUS[mod],
                           "seite": s, "im_seitentext_gefunden": gefunden})

    pfade = []
    for typ, rest in re.findall(r"LM\s*:\s*(PRJ|RST|CYC)\s*:\s*((?:[NZU]M-I{1,3}-[αβγ]\s*→\s*){2}[NZU]M-I{1,3}-[αβγ])",
                                voll.replace("\n", " ").replace("\u200b", "")):
        pfad = re.sub(r"\s+", " ", rest)
        seiten_nr = [n for n in seiten if pfad.split(" → ")[0] in seiten[n] and typ in seiten[n]]
        eintrag = {"code": f"LM : {typ} : {pfad}", "typ": typ, "seiten": seiten_nr}
        if eintrag["code"] not in [p["code"] for p in pfade]:
            pfade.append(eintrag)

    axiome = [{"nr": f"9.2.{n}", "titel": t.strip(), "seite": 19}
              for n, t in re.findall(r"9\.2\.(\d)\s+(Axiom[^\n]+)", seiten[19])]

    adressen = re.findall(r"[NZU]M-I{1,3}-[αβγ]", seiten[14] + seiten[15])
    systeme = [{"system": s, "dominante_felder": adressen[i * 3:i * 3 + 3], "seiten": [14, 15]}
               for i, s in enumerate(SYSTEME)] if len(adressen) == 21 else []

    block, begriffe = None, []
    for n in (16, 17, 18):
        for z in seiten[n].splitlines():
            k = re.match(r"\s*(8\.[1-4])\s+(.*)", z)
            if k:
                block = f"{k.group(1)} {k.group(2).strip()}"
                continue
            r = re.match(r"\s*(\S.*?)\s{2,}(\S.*?)\s{2,}(klar|offen|außerhalb|teilweise|unklar)\s+\[(\d+)\]\s*$", z)
            if r:
                begriffe.append({"block": block, "hinweis": "mehrzeilige Begriffsnamen nur mit erster Zeile erfasst",
                                 "begriff_erste_zeile": r.group(1).replace("\u200b", "").strip(),
                                 "kurzdefinition_erste_zeile": r.group(2).strip(), "tensorstatus": r.group(3),
                                 "quelle": f"[{r.group(4)}]", "seite": n})
    ueberschrift_100 = bool(re.search(r"8\.\s*100 Logik-Begriffe", seiten[16]))

    # Abgleich mit 2.1 §4 (Spalten Null | Zyklus | Einheit, 9 Zeilen in Spalten-Reihenfolge I(α,β,γ), II, III)
    v21 = V21.read_text(encoding="utf-8")
    tab = re.search(r"\| Null-Matrix \(Rel0\).*?\n\|---\|---\|---\|\n((?:\|.*\|\n){9})", v21)
    abgleich = []
    if tab:
        zeilen = [[c.strip() for c in z.strip().strip("|").split("|")] for z in tab.group(1).strip().splitlines()]
        reihenfolge = [(sp, mo) for sp in ("I", "II", "III") for mo in ("α", "β", "γ")]
        for i, (sp, mo) in enumerate(reihenfolge):
            for j, m in enumerate(("NM", "ZM", "UM")):
                orig = FELDER[(m, mo)][0][("I", "II", "III").index(sp)]
                neu = zeilen[i][j]
                abgleich.append({"adresse": f"{m}-{sp}-{mo}", "original_1_0": orig, "fassung_2_1": neu,
                                 "identisch": norm(orig) == norm(neu)})

    ergebnis = {
        "schema_version": "logik10-extrakt/0.1", "owner": "claude", "quelle_doi": DOI,
        "erzeugt_am": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).replace(microsecond=0).isoformat(),
        "werkzeug": "forschung/tensor/logik-claude/werkzeuge/logik10_extrakt.py",
        "quelle_sha256": sha, "methode": __doc__.split("Methode:")[1].split("Aufruf")[0].strip(),
        "felder": felder, "lm_pfade": pfade, "axiome": axiome, "logiksysteme": systeme,
        "begriffstabelle_kap8": {"ueberschrift_nennt_100": ueberschrift_100, "zeilen": len(begriffe),
                                 "nach_block": {b: sum(1 for x in begriffe if x["block"] == b)
                                                for b in dict.fromkeys(x["block"] for x in begriffe)},
                                 "eintraege": begriffe},
        "abgleich_2_1": {"datei": str(V21.relative_to(WURZEL)), "zeilen_verglichen": len(abgleich),
                         "identisch": sum(a["identisch"] for a in abgleich), "details": abgleich},
    }
    (AUS / "LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json").write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1) + "\n",
                                                             encoding="utf-8")
    print(json.dumps({"felder": len(felder), "felder_gefunden": sum(f["im_seitentext_gefunden"] for f in felder),
                      "lm_pfade": [p["code"] for p in pfade], "axiome": len(axiome), "systeme": len(systeme),
                      "begriffe_kap8": len(begriffe), "ueberschrift_100": ueberschrift_100,
                      "abgleich_2_1": f"{ergebnis['abgleich_2_1']['identisch']}/{len(abgleich)}"}, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1])
