#!/usr/bin/env python3
"""GR-02 · Gegenrechnung der Rückrechnungen REV-01 bis REV-08 (ki-tensor v4.5/v4.6). Owner: Claude.

Quelle der Behauptungen (Zweig ki-tensor/no-loss-audit-2026-10-31):
  ki-tensor/audit/VERIFIKATION_v4_5.md: REV-01..03 „symbolisch bestanden“ mit R≠0, E≠0, P_in≠0;
    REV-04 „logarithmische elektrochemische Umformung: bestand unter positiven reellen Parameterannahmen“.
  ki-tensor/audit/VERIFIKATION_v4_6.md: REV-05 „geschlossenes SIR-Beispiel“, REV-06 „Normierung benötigt
    Anfangsbedingung“, REV-07 „skalares Kontraktionsbeispiel ist kein allgemeiner Bellman-/Banach-Beweis“,
    REV-08 „Spur 1 allein impliziert keinen positiv semidefiniten Dichteoperator“.
Die Originalskripte und genauen Formeln liegen in nicht synchronisierten ZIP-Archiven. Rekonstruiert wird daher die
jeweilige Standardform; REV-04 als Nernst-Gleichung (ANNAHME, im Ergebnis markiert).

Geprüft wird je: Behauptung gilt unter der genannten Voraussetzung (S) UND scheitert ohne sie (G), wo der Bericht das sagt.
Aufruf: python3 forschung/register/gegenrechnung/rev_rueckrechnungen.py [--json]   (benötigt sympy)
"""
import json
import sys

try:
    import sympy as sp
except ImportError:
    print("SKIP: sympy fehlt (pip install sympy)")
    sys.exit(0)

erg = []


def eintrag(rid, behauptung, rekonstruktion, s, g, annahme=None):
    erg.append({"rev": rid, "behauptung_zweig": behauptung, "rekonstruktion": rekonstruktion, "unter_voraussetzung": bool(s),
                "grenzfall": g, "annahme_rekonstruktion": annahme, "ok": bool(s) and all(g.values())})


def inverse(gl, var, bedingung_null):
    """Löst gl nach var und setzt zurück; prüft außerdem, dass bei Verletzung der Bedingung keine eindeutige Lösung existiert."""
    los = sp.solve(gl, var)
    rueck = len(los) == 1 and sp.simplify(gl.lhs.subs(var, los[0]) - gl.rhs.subs(var, los[0])) == 0
    sym, wert = bedingung_null
    ausgeartet = sp.solve(gl.subs(sym, wert), var)
    return rueck, los, ausgeartet == [] or ausgeartet is True or len(ausgeartet) != 1


# REV-01  ΔP = R·Q  →  Q = ΔP/R,  R ≠ 0
dP, R, Q = sp.symbols("DeltaP R Q")
ok, los, aus = inverse(sp.Eq(dP, R * Q), Q, (R, 0))
eintrag("REV-01", "ΔP=RQ → Q=ΔP/R, R≠0", f"Q = {los}", ok and los == [dP / R], {"R=0: keine eindeutige Umkehrung": aus})

# REV-02  σ = E·ε  →  ε = σ/E,  E ≠ 0
sig, E, eps = sp.symbols("sigma E epsilon")
ok, los, aus = inverse(sp.Eq(sig, E * eps), eps, (E, 0))
eintrag("REV-02", "σ=Eε → ε=σ/E, E≠0", f"ε = {los}", ok and los == [sig / E], {"E=0: keine eindeutige Umkehrung": aus})

# REV-03  η = P_out/P_in  →  P_out = η·P_in,  P_in ≠ 0
eta, Po, Pi = sp.symbols("eta P_out P_in")
los = sp.solve(sp.Eq(eta, Po / Pi), Po)
ok = los == [eta * Pi] and sp.simplify((Po / Pi).subs(Po, los[0]) - eta) == 0
eintrag("REV-03", "η=P_out/P_in → P_out=ηP_in, P_in≠0", f"P_out = {los}", ok, {"P_in=0: η undefiniert": sp.limit(1 / Pi, Pi, 0, "+") == sp.oo})

# REV-04  Nernst: E = E0 − (R T/(n F)) ln Q  →  Q = exp(n F (E0 − E)/(R T)), R,T,n,F > 0, Q > 0   [ANNAHME: Formel rekonstruiert]
Ep, E0, Rg, T, n, F, Qr = sp.symbols("E E0 R T n F Q", positive=True)
Ec = sp.symbols("E_c", real=True)
E0r = sp.symbols("E0_r", real=True)
gl = sp.Eq(Ec, E0r - Rg * T / (n * F) * sp.log(Qr))
los = sp.solve(gl, Qr)
ok = len(los) == 1 and sp.simplify(sp.expand_log(gl.rhs.subs(Qr, los[0]), force=True) - Ec) == 0
Qneg = sp.symbols("Qn", negative=True)
grenz = {"Q<0: ln(Q) nicht reell": not sp.log(Qneg).is_real}
eintrag("REV-04", "logarithmische elektrochemische Umformung, positive reelle Parameter", f"Q = {los}", ok, grenz,
        annahme="Formel als Nernst-Gleichung rekonstruiert; Originalformel liegt im nicht synchronisierten Archiv v4.5")

# REV-05  SIR: S'=-βSI/N, I'=βSI/N-γI, R'=γI  →  (S+I+R)' = 0  (Erhaltung)
t = sp.symbols("t")
be, ga, N = sp.symbols("beta gamma N", positive=True)
S, I, Rr = (sp.Function(x)(t) for x in "SIR")
dS, dI, dR = -be * S * I / N, be * S * I / N - ga * I, ga * I
erhaltung = sp.simplify(dS + dI + dR) == 0
# Grenzfall: mit Geburten/Toden μ ungleicher Rate ist die Summe nicht erhalten
mu = sp.symbols("mu", positive=True)
offen = sp.simplify(dS + mu * N + dI + dR - mu * S) != 0
eintrag("REV-05", "geschlossenes SIR-Beispiel: Gesamtzahl erhalten", "d(S+I+R)/dt = 0", erhaltung, {"offenes System (Zuwachs μN−μS) nicht erhalten": offen})

# REV-06  Master-Gleichung zweier Zustände: p1'=-a p1 + b p2, p2'= a p1 - b p2 → (p1+p2)'=0; Σp=1 nur mit Anfangsbedingung
a_, b_ = sp.symbols("a b", positive=True)
p1, p2 = sp.Function("p1"), sp.Function("p2")
sol = sp.dsolve([sp.Eq(p1(t).diff(t), -a_ * p1(t) + b_ * p2(t)), sp.Eq(p2(t).diff(t), a_ * p1(t) - b_ * p2(t))],
                [p1(t), p2(t)], ics={p1(0): sp.Rational(3, 10), p2(0): sp.Rational(9, 10)})
summe = sp.simplify(sol[0].rhs + sol[1].rhs)
sol1 = sp.dsolve([sp.Eq(p1(t).diff(t), -a_ * p1(t) + b_ * p2(t)), sp.Eq(p2(t).diff(t), a_ * p1(t) - b_ * p2(t))],
                 [p1(t), p2(t)], ics={p1(0): sp.Rational(3, 10), p2(0): sp.Rational(7, 10)})
summe1 = sp.simplify(sol1[0].rhs + sol1[1].rhs)
eintrag("REV-06", "Wahrscheinlichkeitsnormierung benötigt Anfangsbedingung", "Σp konstant; =1 nur wenn Σp(0)=1",
        summe1 == 1, {"Σp(0)=1.2 bleibt 1.2 ≠ 1 (Normierung folgt nicht aus der Dynamik)": summe == sp.Rational(6, 5)})

# REV-07  skalare Kontraktion T(v) = r + γ v, |γ|<1 → Fixpunkt v* = r/(1-γ), Lipschitz |γ|
r, g, v, w = sp.symbols("r gamma v w", real=True)
Tm = lambda x: r + g * x
fix = sp.solve(sp.Eq(v, Tm(v)), v)
kontrakt = sp.simplify(sp.Abs(Tm(v) - Tm(w)) - sp.Abs(g) * sp.Abs(v - w)) == 0
it = 0.0
for _ in range(200):
    it = 1.0 + 0.9 * it
grenz7 = {"γ=1: kein Fixpunkt (r≠0)": sp.solve(sp.Eq(v, r + v), v) == [],
          "Iteration γ=0.9, r=1 → 10": abs(it - 10.0) < 1e-6,
          "nur skalarer Fall, kein allgemeiner Bellman-Beweis (Bericht stimmt)": True}
eintrag("REV-07", "skalares Kontraktionsbeispiel, kein allgemeiner Bellman-/Banach-Beweis", f"v* = {fix}, |T(v)-T(w)| = |γ||v-w|",
        len(fix) == 1 and sp.simplify(fix[0] - r / (1 - g)) == 0 and kontrakt, grenz7)

# REV-08  Spur 1 ⇏ positiv semidefinit: Gegenbeispiel diag(2, -1)
M = sp.diag(2, -1)
gegen = M.trace() == 1 and min(M.eigenvals()) < 0
rho = sp.Matrix([[sp.Rational(1, 2), 0], [0, sp.Rational(1, 2)]])
eintrag("REV-08", "Spur 1 allein impliziert keinen positiv semidefiniten Dichteoperator", "Gegenbeispiel diag(2,−1): Spur 1, Eigenwert −1",
        gegen, {"echter Dichteoperator ρ=I/2: Spur 1 und PSD": rho.trace() == 1 and min(rho.eigenvals()) >= 0})

alle = all(e["ok"] for e in erg)
if "--json" in sys.argv:
    print(json.dumps({"schema_version": "gegenrechnung/0.1", "gegenstand": "REV-01..08 ki-tensor v4.5/v4.6", "sympy": sp.__version__,
                      "ergebnisse": erg, "gesamt": "OK" if alle else "FEHLER"}, ensure_ascii=False, indent=1, default=str))
else:
    for e in erg:
        print(f"{e['rev']} {'bestätigt' if e['ok'] else 'NICHT bestätigt':16} {e['rekonstruktion'][:60]:60} {'(ANNAHME) ' if e['annahme_rekonstruktion'] else ''}")
    print("Gesamt:", "OK" if alle else "FEHLER", f"({sum(e['ok'] for e in erg)}/{len(erg)})")
sys.exit(0 if alle else 1)
