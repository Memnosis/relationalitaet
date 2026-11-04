#!/usr/bin/env python3
"""Prüfung der 103 historischen Tensorgerüste (KI-Tensor v10.7) mit den Werkzeugen der typisierten Algebra. Owner: Claude.
Eingabe: docs/data/tensor-inventar-v10_7.json (veröffentlicht von GPT, Commit ce74166). Ausgabe: ANALYSE_103_V0_1.json

Was geprüft werden KANN (die Gerüste haben 3 Achsen × 3 Rollen, Modell, Formelanker, Messgröße, aber KEINE Pfade):
  S1  Achsenregel A1 (Achsenunabhängigkeit) je Gerüst: identische Achsen / gemeinsame Rollen zwischen Achsen
  S2  Formeltypen der Formelanker (Dynamik/ODE, logarithmisch, exponentiell, Verhältnis, Bilanz, Potenzgesetz, linear/Matrix)
  S3  Brückenkandidaten: Gerüste mit gleicher Zustandsgröße unter der Zeitableitung (z. B. dc/dt) oder gleichem Formeltyp
  S4  Achsen-Neutralität: Gerüste, deren Achsen die neutrale Sprache (Rel0/Rel-Rel/Rel1, Struktur/Funktion/Relation) tragen
Was NICHT geprüft werden kann: Pfadmuster M1–M9 und Regel U (keine Pfade im Inventar) → offen, nicht „bestätigt“.
"""
import collections
import importlib.util
import itertools
import json
import pathlib
import re
import sys

W = pathlib.Path(__file__).resolve().parents[3]
H = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("typalgebra", H / "typalgebra.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)
d = json.loads((W / "docs/data/tensor-inventar-v10_7.json").read_text(encoding="utf-8"))
T = d["tensors"]

FORMELTYPEN = [
    ("dynamik_ode", re.compile(r"\bd\s*([A-Za-zα-ωΑ-Ω_]\w*)\s*/\s*d\s*t|∂\s*\w+\s*/\s*∂\s*t|\bd/dt|\\dot|ẋ|ṡ")),
    ("logarithmisch", re.compile(r"\bln\b|\blog\b")),
    ("exponentiell", re.compile(r"\bexp\b|e\^|e\s*\^")),
    ("summe_bilanz", re.compile(r"Σ|∑|\bsum\b")),
    ("potenzgesetz", re.compile(r"\^\s*[-0-9(]|²|³|∝")),
    ("linear_matrix", re.compile(r"\b[A-Z]\s*[xv]\b|\bdet\b|Matrix|\bAx\b")),
    ("verhaeltnis", re.compile(r"/")),
]


def formeltypen(f):
    if not f:
        return []
    return [n for n, rx in FORMELTYPEN if rx.search(f)]


def zustandsgroesse(f):
    m = re.search(r"\bd\s*([A-Za-zα-ωΑ-Ω_]\w*)\s*/\s*d\s*t", f or "")
    return m.group(1) if m else None


NEUTRAL = {("rel0", "rel-rel", "rel1"), ("struktur", "funktion", "relation"), ("kern", "kreislauf", "öffnung")}
erg = {"a1": [], "a1_teil": [], "formeltypen": {}, "ohne_formel": [], "brueckenkandidaten": [], "neutrale_achsen": []}
for t in T:
    achsen = [{"dimension": f"A{a['n']}", "rollen": a["elements"]} for a in t["axes"]]
    for v in ta.achsen_pruefung(achsen):
        (erg["a1"] if v["regel"] == "A1" else erg["a1_teil"]).append({"tensor": t["id"], "name": t["name"], **v})
    ft = formeltypen(t.get("formula_anchor"))
    erg["formeltypen"][t["id"]] = ft
    if not t.get("formula_anchor"):
        erg["ohne_formel"].append(t["id"])
    for a in t["axes"]:
        if tuple(x.strip().lower() for x in a["elements"]) in NEUTRAL:
            erg["neutrale_achsen"].append({"tensor": t["id"], "achse": a["n"], "rollen": a["elements"]})

# Brückenkandidaten: gleiche Zustandsgröße unter d/dt
nach_groesse = collections.defaultdict(list)
for t in T:
    g = zustandsgroesse(t.get("formula_anchor"))
    if g:
        nach_groesse[g].append(t)
for g, ts in sorted(nach_groesse.items()):
    for a, b in itertools.combinations(ts, 2):
        erg["brueckenkandidaten"].append({"art": "gleiche_zustandsgroesse", "groesse": g, "paar": [a["id"], b["id"]],
                                          "namen": [a["name"], b["name"]], "formeln": [a["formula_anchor"], b["formula_anchor"]]})
typ_zaehlung = collections.Counter(x for v in erg["formeltypen"].values() for x in v)
zusammenfassung = {"gerueste": len(T), "achsen": sum(len(t["axes"]) for t in T),
                   "a1_identische_achsen": len(erg["a1"]), "a1_teilueberschneidungen": len(erg["a1_teil"]),
                   "formelanker_vorhanden": len(T) - len(erg["ohne_formel"]), "formeltypen": dict(typ_zaehlung.most_common()),
                   "brueckenkandidaten_gleiche_zustandsgroesse": len(erg["brueckenkandidaten"]),
                   "neutrale_achsen": len(erg["neutrale_achsen"]),
                   "pfade_im_inventar": 0, "M1_M9_pruefbar": False,
                   "hinweis": "Keine Pfade im Inventar: Pfadmuster und Regel U sind an den 103 Gerüsten NICHT prüfbar. Lexikalische und Formelbefunde sind Kandidaten, keine Belege."}
out = {"schema_version": "analyse-103/0.1", "owner": "claude", "quelle": "docs/data/tensor-inventar-v10_7.json",
       "quelle_commit": "ce74166", "zusammenfassung": zusammenfassung, **erg}
(H / "ANALYSE_103_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
if "--json" in sys.argv:
    print(json.dumps(zusammenfassung, ensure_ascii=False, indent=1))
else:
    for k, v in zusammenfassung.items():
        print(f"{k}: {v}")
    print("A1 identisch:", [(x["tensor"], x["name"], x["rollen"]) for x in erg["a1"]])
    print("A1 teilweise:", [(x["tensor"], x["name"], x["gemeinsam"]) for x in erg["a1_teil"]][:12])
    print("Brücken (gleiche Zustandsgröße):", [(b["groesse"], b["paar"], b["formeln"]) for b in erg["brueckenkandidaten"]][:15])
    print("Gesamt: OK")
