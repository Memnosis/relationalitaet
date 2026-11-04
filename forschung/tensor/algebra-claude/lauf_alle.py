#!/usr/bin/env python3
"""Führt die typisierte Algebra über alle verfügbaren Fachtensoren aus und schreibt die Ergebnisakte. Owner: Claude.
Aufruf: python3 forschung/tensor/algebra-claude/lauf_alle.py [--json]
Eingabe: TENSOREN_PUBLIKATIONEN_V0_1.json (aus extrakt_tensoren.py). Ausgabe: ALGEBRA_LAUF_V0_1.json
"""
import collections
import importlib.util
import json
import pathlib
import sys

H = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("typalgebra", H / "typalgebra.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)

d = json.loads((H / "TENSOREN_PUBLIKATIONEN_V0_1.json").read_text(encoding="utf-8"))
T = d["tensoren"]
erg = ta.lauf(T)
typk = {t["id"]: ta.typpruefung(t) for t in T}
klassen = collections.Counter(e["vergleich"]["klasse"] for e in erg)
alle_k = [k for e in erg for k in e["ueberlagerung"]]
neu = [k for k in alle_k if k["gilt_als_neue_beziehung"]]
neu_folgen = sorted({tuple(k["verkettung"]) for k in neu})
umlauf = [k for k in neu if k["geschlossener_umlauf"]]
hyst = [k for k in neu if k.get("hysterese")]
# Regel U auf ALLE Hysterese-Verkettungen (auch bereits bekannte) anwenden
u_pruef = []
for k in alle_k:
    if k.get("hysterese"):
        r = ta.invertierbarkeit(k["verkettung"]); r["aus"] = k["aus"]; u_pruef.append(r)
u_uniq = {json.dumps(x, sort_keys=True, ensure_ascii=False): x for x in u_pruef}
u_pruef = sorted(u_uniq.values(), key=lambda x: (x["start"], x["ende"], x["aus"]))
out = {"schema_version": "algebra-lauf/0.1", "owner": "claude", "algebra": "typalgebra.py v0.1",
       "eingabe_sha256": ta.kanon(d), "tensoren": [{"id": t["id"], "felder": t["anzahl_felder"], "pfade": len(t["pfade"]),
                                                     "typkonflikte": typk[t["id"]], "mehrfachtypen": ta.mehrfachtypen(t)} for t in T],
       "typ_konsistenz_autor": ta.typ_konsistenz(T),
       "paare": len(erg), "klassen": dict(klassen), "verkettungskandidaten": len(alle_k),
       "neue_beziehungen_P1_P2_P3eigen": len(neu), "neue_beziehungen_verschiedene_folgen": [list(x) for x in neu_folgen], "davon_geschlossene_umlaeufe": len(umlauf), "davon_hysterese": len(hyst), "regel_U_umkehrbarkeit": u_pruef,
       "ergebnis_sha256": ta.kanon(erg), "ergebnisse": erg}
(H / "ALGEBRA_LAUF_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
if "--json" in sys.argv:
    print(json.dumps({k: v for k, v in out.items() if k != "ergebnisse"}, ensure_ascii=False, indent=1))
else:
    for t in out["tensoren"]:
        print(f"{t['id']:10} Felder {t['felder']:2d} Pfade {t['pfade']:2d} Typkonflikte {len(t['typkonflikte'])}")
    print("Typkonsistenz (Autor):", {k: f"{v['erfuellt']}/{v['gesamt']}" for k, v in out["typ_konsistenz_autor"].items()})
    print("Paare:", out["paare"], "Klassen:", out["klassen"])
    print("Verkettungskandidaten:", len(alle_k), "· neue Beziehungen (P1+P2+P3 eigen):", len(neu), "· verschiedene Folgen:", len(neu_folgen), "· davon geschlossene Umläufe:", len(umlauf), "· davon Hysterese:", len(hyst))
    print("Regel U (Zyklus-Matrix):", [f"{x['start']}→{x['ende']} Klasse {x['klasse_start']} erwartet {x['erwartet']}: {'erfüllt' if x['erfuellt'] else 'VERLETZT'}" for x in u_pruef])
    print("Ergebnis-SHA256:", out["ergebnis_sha256"][:16])
    print("Gesamt: OK")
