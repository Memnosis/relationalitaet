#!/usr/bin/env python3
"""Mathematische Brücke F034 Reaktionskinetik ↔ F096 Verfahrenstechnik (GPT-Befund, Issue #3, 04.11.2026 01:36 UTC).
Owner: Claude (unabhängige Gegenprüfung, eigener Code). Formeln nach GPTs Angabe; die Primärakte
Gesamtinventar_v10_7.md liegt Claude NICHT vor → Formelquelle = GPT-Zitat (Vorbehalt).

  F034:  dc/dt = S·v(c)                         (S stöchiometrische Matrix, v Reaktionsratenvektor)
  F096:  V·dc/dt = F·(c_in − c) + V·r(c)          (Rührkessel/CSTR: Volumen V, Durchfluss F, Zulauf c_in, Reaktionsterm r)

Behauptung GPT: Mit F = 0 und r(c) = S·v(c) ist F034 ein Spezialfall von F096.
Geprüft: (1) Reduktion F096 → F034 unter den Bedingungen, symbolisch; (2) Bedingungen notwendig (Gegenproben);
(3) Richtung: F096 ist NICHT Spezialfall von F034 (F034 kennt keinen Zu-/Abfluss); (4) V ≠ 0 nötig.
Klasse im Sinne der Algebra: „Spezialfall (Teilstruktur)“, nicht „gleich“.
"""
import json
import sys

try:
    import sympy as sp
except ImportError:
    print("SKIP: sympy fehlt – SKIP ist kein PASS (Exit 77)")
    sys.exit(77)

t = sp.symbols("t")
V, F = sp.symbols("V F")
c = sp.Function("c")(t)
c_in = sp.symbols("c_in")
v = sp.Function("v")(c)
S = sp.symbols("S")  # skalar stellvertretend; Vektorfall siehe unten

f096 = sp.Eq(V * c.diff(t), F * (c_in - c) + V * sp.Function("r")(c))
# (1) Reduktion: F=0, r(c)=S v(c), V≠0
red = f096.subs(F, 0).subs(sp.Function("r")(c), S * v)
reduziert = sp.simplify(sp.solve(red, c.diff(t))[0] - S * v) == 0
# (1b) Vektor-/Matrixfall: 2 Spezies, 2 Reaktionen
c1, c2 = sp.Function("c1")(t), sp.Function("c2")(t)
Sm = sp.Matrix([[-1, 1], [1, -1]])
vv = sp.Matrix([sp.Function("v1")(c1, c2), sp.Function("v2")(c1, c2)])
cvec = sp.Matrix([c1, c2])
f096_vec = V * cvec.diff(t) - (F * (sp.Matrix(sp.symbols("cin1 cin2")) - cvec) + V * Sm * vv)
reduziert_vec = sp.simplify(f096_vec.subs(F, 0) / V - (cvec.diff(t) - Sm * vv)) == sp.zeros(2, 1)
# (2) Gegenproben: ohne F=0 bleibt ein Durchflussterm; ohne r=S v bleibt ein anderer Reaktionsterm
ohne_F0 = sp.simplify(sp.solve(f096.subs(sp.Function("r")(c), S * v), c.diff(t))[0] - S * v) != 0
ohne_r = sp.simplify(sp.solve(f096.subs(F, 0), c.diff(t))[0] - S * v) != 0
# (3) Umkehrung: F034 enthält keinen Zuflussparameter → kann F096 mit F≠0 nicht darstellen
umkehr_unmoeglich = not ({F, c_in} & (S * v).free_symbols)
# (4) V=0 entartet (Gleichung wird algebraisch, keine Dynamik)
v0_entartet = f096.subs(V, 0).lhs == 0

erg = {"reduktion_skalar": reduziert, "reduktion_matrix_2x2": reduziert_vec, "bedingung_F0_noetig": ohne_F0,
       "bedingung_r_gleich_Sv_noetig": ohne_r, "umkehrung_unmoeglich": umkehr_unmoeglich, "V_null_entartet": v0_entartet}
ok = all(erg.values())
urteil = {"klasse": "spezialfall_F034_in_F096" if ok else "nicht_bestaetigt",
          "bedingungen": ["F = 0 (geschlossenes System, kein Durchfluss)", "r(c) = S·v(c)", "V ≠ 0"],
          "vorbehalt": "Formeln aus GPT-Zitat; Abgleich mit der Primärakte Gesamtinventar_v10_7.md ausstehend",
          "P3": "eigen (Claude) + GPT-Befund = zwei unabhängige Wege, sobald GPT seinen Rechenweg mit SHA belegt"}
if "--json" in sys.argv:
    print(json.dumps({"ergebnisse": erg, "urteil": urteil}, ensure_ascii=False, indent=1))
else:
    for k, x in erg.items():
        print(f"{'OK ' if x else 'NEIN'} {k}")
    print("Urteil:", urteil["klasse"], "| Bedingungen:", "; ".join(urteil["bedingungen"]))
    print("Gesamt:", "OK" if ok else "FEHLER")
sys.exit(0 if ok else 1)
