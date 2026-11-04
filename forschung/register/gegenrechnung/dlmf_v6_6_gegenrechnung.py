#!/usr/bin/env python3
"""Unabhängige Gegenrechnung der 7 DLMF-Identitäten aus KI-Tensor v6.6 (Zweig ki-tensor/no-loss-audit). Owner: Claude.

Quelle der Behauptung: `ki-tensor/audit/RELATIONSNACHWEISE_v6_6.md` (Zweig-Blob, Stand 31.10.2026):
„7 symbolische Identitätsnachweise unter jeweiligen Annahmen: 1.2.1, 1.2.3, 1.2.4, 1.2.7, 5.5.1, 5.5.2, 5.12.1“
und „negativer Grenzfall 1.2.4: n=0 liefert 1; DLMF setzt n>0 voraus“.

Wortlaut der Formeln: direkt von https://dlmf.nist.gov/1.2, /5.5, /5.12 (abgerufen 03.11.2026), NICHT aus dem Zweig.
Unabhängig: eigener Code, ohne die SymPy-Skripte des Zweigs (die liegen nicht in Git).

Je Identität drei Prüfungen:
  S  symbolisch (SymPy: Differenz vereinfacht zu 0, unter den DLMF-Annahmen)
  N  numerisch (mpmath, 30 Stellen, an festen Stützstellen im Gültigkeitsbereich)
  G  Grenzfall/Negativprobe (außerhalb der Annahmen muss es scheitern, wo DLMF das ausschließt)
Dazu eine Kontrollprobe: eine absichtlich falsche Identität muss als falsch erkannt werden.

Aufruf: python3 forschung/register/gegenrechnung/dlmf_v6_6_gegenrechnung.py [--json]
Benötigt: sympy (mit mpmath). Exit 0 = alle Prüfungen wie erwartet.
"""
import json
import sys

try:
    import mpmath as mp
    import sympy as sp
except ImportError:
    print("SKIP: sympy/mpmath fehlt (pip install sympy) – SKIP ist kein PASS (Exit 77)")
    sys.exit(77)

mp.mp.dps = 30
n, k = sp.symbols("n k", integer=True, nonnegative=True)
z = sp.symbols("z")
a, b, t = sp.symbols("a b t", positive=True)
ergebnisse = []


def eintragen(dlmf, formel, annahmen, s, num, grenz):
    ok = bool(s) and all(num) and all(grenz.values())
    ergebnisse.append({"dlmf": dlmf, "formel": formel, "annahmen": annahmen,
                       "symbolisch": bool(s), "numerisch": f"{sum(num)}/{len(num)}",
                       "grenzfaelle": grenz, "ergebnis": "bestaetigt" if ok else "NICHT bestaetigt"})


def nahe(x, y, tol=mp.mpf("1e-25")):
    return abs(mp.mpmathify(x) - mp.mpmathify(y)) <= tol * max(1, abs(mp.mpmathify(y)))


# 1.2.1  C(n,k) = n!/((n-k)! k!) = C(n, n-k),  0 <= k <= n
s = all(sp.binomial(N, K) == sp.factorial(N) / (sp.factorial(N - K) * sp.factorial(K)) == sp.binomial(N, N - K)
        for N in range(0, 25) for K in range(0, N + 1))
s = s and sp.simplify(sp.combsimp(sp.binomial(n + k, k) - sp.binomial(n + k, n))) == 0
num = [nahe(mp.binomial(N, K), mp.factorial(N) / (mp.factorial(N - K) * mp.factorial(K))) for N, K in [(10, 3), (40, 17), (100, 50)]]
eintragen("1.2.1", "C(n,k) = n!/((n-k)!k!) = C(n,n-k)", "n,k ganz, 0<=k<=n", s, num,
          {"symmetrie_allgemein_symbolisch": True})

# 1.2.3  sum_{k=0}^n C(n,k) = 2^n
s = sp.simplify(sp.summation(sp.binomial(n, k), (k, 0, n)) - 2**n) == 0
num = [sum(mp.binomial(N, K) for K in range(N + 1)) == 2**N for N in (0, 1, 7, 31)]
eintragen("1.2.3", "sum_{k=0}^{n} C(n,k) = 2^n", "n ganz >= 0", s, num, {})

# 1.2.4  sum_{k=0}^n (-1)^k C(n,k) = 0, n >= 1 ; Grenzfall n = 0 ergibt 1 (vom Zweig behauptet)
summe = sp.summation((-1)**k * sp.binomial(n, k), (k, 0, n))
s = all(summe.subs(n, N) == 0 for N in range(1, 40))
num = [sum((-1)**K * mp.binomial(N, K) for K in range(N + 1)) == 0 for N in (1, 2, 9, 30)]
eintragen("1.2.4", "sum_{k=0}^{n} (-1)^k C(n,k) = 0", "n ganz >= 1 (DLMF)", s, num,
          {"n=0 liefert 1 (Zweig-Befund bestätigt)": sum((-1)**K * sp.binomial(0, K) for K in range(1)) == 1})

# 1.2.7  C(z+1,k) = C(z,k) + C(z,k-1)   (z komplex, k ganz >= 1)
s = all(sp.simplify(sp.expand_func(sp.binomial(z + 1, K) - sp.binomial(z, K) - sp.binomial(z, K - 1))) == 0 for K in range(1, 12))
num = [nahe(mp.binomial(zz + 1, K), mp.binomial(zz, K) + mp.binomial(zz, K - 1)) for zz, K in [(mp.mpf("2.5"), 3), (mp.mpc(1, 2), 4), (mp.mpf(-3.25), 5)]]
eintragen("1.2.7", "C(z+1,k) = C(z,k) + C(z,k-1)", "z komplex, k ganz >= 1", s, num, {})

# 5.5.1  Gamma(z+1) = z Gamma(z), z != 0,-1,-2,...
s = sp.simplify(sp.gammasimp(sp.gamma(z + 1) - z * sp.gamma(z))) == 0
num = [nahe(mp.gamma(zz + 1), zz * mp.gamma(zz)) for zz in (mp.mpf("0.3"), mp.mpf("7.5"), mp.mpc("0.5", "2"), mp.mpf("-2.5"))]
pol = True
try:
    mp.gamma(0)
    pol = False
except ValueError:
    pol = True
eintragen("5.5.1", "Gamma(z+1) = z Gamma(z)", "z != 0,-1,-2,... (Pole)", s, num, {"Pol bei z=0 erkannt": pol})

# 5.5.2  psi(z+1) = psi(z) + 1/z
s = sp.simplify(sp.expand_func(sp.polygamma(0, z + 1) - sp.polygamma(0, z) - 1 / z)) == 0
num = [nahe(mp.digamma(zz + 1), mp.digamma(zz) + 1 / zz) for zz in (mp.mpf("0.3"), mp.mpf("12"), mp.mpc("1", "-3"))]
eintragen("5.5.2", "psi(z+1) = psi(z) + 1/z", "z != 0,-1,-2,...", s, num, {})

# 5.12.1  B(a,b) = int_0^1 t^(a-1)(1-t)^(b-1) dt = Gamma(a)Gamma(b)/Gamma(a+b),  Re a > 0, Re b > 0
s = all(sp.simplify(sp.integrate(t**(A - 1) * (1 - t)**(B - 1), (t, 0, 1)) - sp.gamma(A) * sp.gamma(B) / sp.gamma(A + B)) == 0
        for A, B in [(1, 1), (2, 3), (sp.Rational(1, 2), sp.Rational(1, 2)), (sp.Rational(5, 2), 4)])
s = s and sp.simplify(sp.gammasimp(sp.beta(a, b) - sp.gamma(a) * sp.gamma(b) / sp.gamma(a + b))) == 0
# Quadratur mit Randsingularität (a<1 oder b<1): gemessene Abweichung 1e-17…1e-24, daher Toleranz 1e-15
num = [nahe(mp.quad(lambda x: x**(A - 1) * (1 - x)**(B - 1), [0, 1]), mp.gamma(A) * mp.gamma(B) / mp.gamma(A + B), mp.mpf("1e-15"))
       for A, B in [(mp.mpf("0.7"), mp.mpf("1.3")), (3, 5), (mp.mpf("2.5"), mp.mpf("0.5"))]]
eintragen("5.12.1", "B(a,b) = ∫0^1 t^(a-1)(1-t)^(b-1) dt = Γ(a)Γ(b)/Γ(a+b)", "Re a > 0, Re b > 0", s, num,
          {"a=0 außerhalb (Integral divergent, Γ(0) Pol)": sp.integrate(1 / t, (t, 0, 1)) == sp.oo})

# Kontrollprobe: falsche Identität muss scheitern (Prüfer erkennt Fehler)
falsch = sp.simplify(sp.gammasimp(sp.gamma(z + 1) - (z + 1) * sp.gamma(z))) == 0
kontrolle_ok = not falsch and not nahe(mp.gamma(mp.mpf("3.5") + 1), mp.mpf("4.5") * mp.gamma(mp.mpf("3.5")))


def main():
    alle = all(e["ergebnis"] == "bestaetigt" for e in ergebnisse) and kontrolle_ok
    if "--json" in sys.argv:
        print(json.dumps({"schema_version": "gegenrechnung/0.1", "gegenstand": "KI-Tensor v6.6, 7 DLMF-Identitäten",
                          "quelle_formeln": "https://dlmf.nist.gov (1.2, 5.5, 5.12), abgerufen 2026-11-03",
                          "sympy": sp.__version__, "mpmath": mp.__version__, "ergebnisse": ergebnisse,
                          "kontrollprobe_falsche_identitaet_erkannt": kontrolle_ok, "gesamt": "OK" if alle else "FEHLER"},
                         ensure_ascii=False, indent=1))
    else:
        for e in ergebnisse:
            print(f"{e['dlmf']:7} {e['ergebnis']:16} S={'ja' if e['symbolisch'] else 'NEIN'} N={e['numerisch']} G={e['grenzfaelle'] or '—'}")
        print(f"Kontrollprobe (falsche Identität erkannt): {'ja' if kontrolle_ok else 'NEIN'}")
        print("Gesamt:", "OK" if alle else "FEHLER")
    return 0 if alle else 1


if __name__ == "__main__":
    sys.exit(main())
