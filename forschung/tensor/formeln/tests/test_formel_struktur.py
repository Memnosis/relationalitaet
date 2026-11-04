#!/usr/bin/env python3
"""Tests Konzept 2 (Formelreduktion, Ministrukturen, Keime, Dreiecke). Owner: Claude. Ohne sympy: SKIP (Exit 77)."""
import importlib.util
import json
import pathlib
import sys

try:
    import sympy as sp
except ImportError:
    print("SKIP: sympy fehlt – Exit 77")
    sys.exit(77)

H = pathlib.Path(__file__).resolve().parents[1]


def lade(name, datei):
    spec = importlib.util.spec_from_file_location(name, H / datei)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


fs = lade("fs", "formel_struktur.py")
FEHLER = []


def pruefe(name, bed):
    print(("ok   " if bed else "FEHL ") + name)
    if not bed:
        FEHLER.append(name)


def sk(f, k=()):
    eq = fs.parse(f, k)
    return fs.skelett(eq, fs.variablen(eq, k), k)


# 1 gleiche Ministruktur über Fachgrenzen
pruefe("F=m·a, U=R·I, p=m·v gleiches Skelett", sk("Eq(F, m*a)") == sk("Eq(U, R_*I_)") == sk("Eq(p, m*v)"))
# 2 Konstanten werden zu k: E=m c² und F=m a NICHT gleich, E = m c² und E_k = ½ m v²: verschieden (2 vs 3 Variablen)
pruefe("E=mc² (c Konstante) ≠ F=ma", sk("Eq(E, m*c**2)", ["c"]) != sk("Eq(F, m*a)"))
# 3 Umbenennungs- und Vorzeicheninvarianz
pruefe("Skelett invariant unter Umbenennung", sk("Eq(a, b/c)") == sk("Eq(z, x/y)"))
# 4 Triadentyp
eq = fs.parse("Eq(F, m*a)")
pruefe("F=m·a ist Potenzgesetz", fs.triadentyp(eq, fs.variablen(eq)) == "potenzgesetz")
eq = fs.parse("Eq(s, s0 + v*t)")
pruefe("s=s0+v·t hat 4 Größen (nicht trinitär)", len(fs.variablen(eq)) == 4)
eq = fs.parse("Eq(U, U1 + U2)")
pruefe("U=U1+U2 additiv", fs.triadentyp(eq, fs.variablen(eq)) == "additiv")
# 5 Bestand: Dreieck erkannt
probe = [{"id": "A", "formel": "Eq(W, F*s)", "groessen": {"W": "Arbeit", "F": "Kraft", "s": "Weg"}, "gebiet": "Mechanik", "name": "A"},
         {"id": "B", "formel": "Eq(P, W/t)", "groessen": {"P": "Leistung", "W": "Arbeit", "t": "Zeit"}, "gebiet": "Mechanik", "name": "B"},
         {"id": "C", "formel": "Eq(v, s/t)", "groessen": {"v": "Geschwindigkeit", "s": "Weg", "t": "Zeit"}, "gebiet": "Mechanik", "name": "C"}]
b = fs.bestand([fs.analysiere(x) for x in probe])
pruefe("Dreieck Arbeit/Leistung/Geschwindigkeit erkannt", len(b["dreiecke"]) == 1 and b["dreiecke"][0]["verbindungen"] == ["Arbeit", "Weg", "Zeit"])
# 6 Top-100-Lauf: Kennzahlen stabil
d = json.loads((H / "FORMELN_TOP100_V0_1.json").read_text(encoding="utf-8"))
b = fs.bestand([fs.analysiere(f) for f in d["formeln"]])
pruefe("Top-100: 100 auswertbar", b["auswertbar"] == 100)
pruefe("Top-100: 3 Dreiecke", len(b["dreiecke"]) == 3)
# 7 Ableitung aus dem Dreieck: P = F·v, reproduzierbar; Scheindreieck Pendel/Kepler/BMI wird abgelehnt
dr = json.loads((H / "DREIECKE_V0_1.json").read_text(encoding="utf-8"))["ergebnisse"]
erste = dr[0]
pruefe("Ableitung P = F·v", erste["abgeleitet"] == ["Geschwindigkeit*Kraft - Leistung"] and erste["P3_reproduzierbar"])
pruefe("Pendel–Kepler–BMI unzulässig (P1)", any(x["formeln"] == ["F055", "F066", "F088"] and x["urteil"] == "unzulaessige_verknuepfung" for x in dr))
pruefe("ρ = c·M nur Spezialfall", any(x["formeln"] == ["F044", "F080", "F081"] and x["urteil"] == "spezialfall_gueltig" for x in dr))
print("OK" if not FEHLER else f"FEHLER: {FEHLER}")
sys.exit(1 if FEHLER else 0)
