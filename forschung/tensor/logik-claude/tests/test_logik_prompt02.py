#!/usr/bin/env python3
"""Probelauf LOGIK-PROMPT-02 (Korrektheit und Vollstaendigkeit) · maschinelle Pruefungen. Owner: Claude.

Ausfuehren:  python3 forschung/tensor/logik-claude/tests/test_logik_prompt02.py
Nur Standardbibliothek. Belegt nur die genannten Aussagen ueber den Kalkuel H und die Goedel-Logik G3.

Kalkuel H (Hilbert-System, Lukasiewicz/Mendelson): Junktoren ¬, →; Regel Modus ponens;
  A1  φ → (ψ → φ)
  A2  (φ → (ψ → χ)) → ((φ → ψ) → (φ → χ))
  A3  (¬ψ → ¬φ) → (φ → ψ)

TST-LP02-01  A1, A2, A3 sind klassische Tautologien (Schema-Ebene, Wahrheitstafel).
TST-LP02-02  Modus ponens erhaelt Wahrheit unter jeder Belegung.
TST-LP02-03  Beweispruefer akzeptiert eine korrekte 5-Zeilen-Herleitung von p → p.
TST-LP02-04  Beweispruefer lehnt eine fehlerhafte Herleitung ab (Negativfall).
TST-LP02-05  Korrektheit: jede gepruefte Herleitungszeile ist eine Tautologie.
TST-LP02-06  Vergleich G3: A1, A2 gelten, A3 gilt NICHT; Tertium non datur und Peirce gelten NICHT.
TST-LP02-07  Ungueltiger Schluss (Bejahung des Konsequens) hat ein klassisches Gegenmodell.
TST-LP02-08  Eine unzulaessige Regel „aus φ → ψ und ψ folgt φ“ ist nicht korrekt (Gegenmodell).
"""
import itertools
import unittest
from fractions import Fraction

# Formeln: ('v','p') | ('not',A) | ('imp',A,B) | ('or',A,B)
V = lambda n: ("v", n)
N = lambda a: ("not", a)
I = lambda a, b: ("imp", a, b)
O = lambda a, b: ("or", a, b)


def atome(f):
    if f[0] == "v":
        return {f[1]}
    return set().union(*(atome(x) for x in f[1:]))


def klassisch(f, b):
    t = f[0]
    if t == "v":
        return b[f[1]]
    if t == "not":
        return not klassisch(f[1], b)
    if t == "imp":
        return (not klassisch(f[1], b)) or klassisch(f[2], b)
    if t == "or":
        return klassisch(f[1], b) or klassisch(f[2], b)


def tautologie(f):
    a = sorted(atome(f))
    return all(klassisch(f, dict(zip(a, w))) for w in itertools.product((False, True), repeat=len(a)))


def gegenmodell(praemissen, konklusion):
    a = sorted(set().union(*(atome(x) for x in praemissen + [konklusion])))
    for w in itertools.product((False, True), repeat=len(a)):
        b = dict(zip(a, w))
        if all(klassisch(p, b) for p in praemissen) and not klassisch(konklusion, b):
            return b
    return None


# Goedel-Logik G3: Wahrheitswerte 0, 1/2, 1; ausgezeichnet ist nur 1
G = (Fraction(0), Fraction(1, 2), Fraction(1))


def g3(f, b):
    t = f[0]
    if t == "v":
        return b[f[1]]
    if t == "imp":
        x, y = g3(f[1], b), g3(f[2], b)
        return Fraction(1) if x <= y else y
    if t == "not":
        return Fraction(1) if g3(f[1], b) == 0 else Fraction(0)
    if t == "or":
        return max(g3(f[1], b), g3(f[2], b))


def g3_gueltig(f):
    a = sorted(atome(f))
    return all(g3(f, dict(zip(a, w))) == 1 for w in itertools.product(G, repeat=len(a)))


P, Q, R = V("p"), V("q"), V("r")
A1 = I(P, I(Q, P))
A2 = I(I(P, I(Q, R)), I(I(P, Q), I(P, R)))
A3 = I(I(N(Q), N(P)), I(P, Q))


def passt(schema, f, belegung):
    """Schema-Abgleich: Metavariablen p, q, r werden konsistent durch Teilformeln ersetzt."""
    if schema[0] == "v":
        if schema[1] in belegung:
            return belegung[schema[1]] == f
        belegung[schema[1]] = f
        return True
    return schema[0] == f[0] and len(schema) == len(f) and all(passt(s, x, belegung) for s, x in zip(schema[1:], f[1:]))


def ist_axiom(f):
    return any(passt(s, f, {}) for s in (A1, A2, A3))


def pruefe_herleitung(zeilen):
    """zeilen: Liste (formel, begruendung); begruendung = 'Ax' oder ('MP', i, j) mit j: φ, i: φ→ψ."""
    for k, (f, beg) in enumerate(zeilen):
        if beg == "Ax":
            if not ist_axiom(f):
                return False, k
        else:
            _, i, j = beg
            if not (i < k and j < k and zeilen[i][0] == I(zeilen[j][0], f)):
                return False, k
    return True, None


PP = I(P, P)
HERLEITUNG_P_P = [
    (I(I(P, I(I(P, P), P)), I(I(P, I(P, P)), I(P, P))), "Ax"),  # A2 mit φ=p, ψ=p→p, χ=p
    (I(P, I(I(P, P), P)), "Ax"),                                     # A1 mit φ=p, ψ=p→p
    (I(I(P, I(P, P)), I(P, P)), ("MP", 0, 1)),
    (I(P, I(P, P)), "Ax"),                                           # A1 mit φ=p, ψ=p
    (PP, ("MP", 2, 3)),
]


class LogikPrompt02(unittest.TestCase):
    def test_01_axiome_tautologien(self):
        for ax in (A1, A2, A3):
            self.assertTrue(tautologie(ax))

    def test_02_mp_erhaelt_wahrheit(self):
        for a, i in itertools.product((False, True), repeat=2):
            imp = (not a) or i
            if a and imp:
                self.assertTrue(i)

    def test_03_herleitung_p_p_korrekt(self):
        ok, fehler = pruefe_herleitung(HERLEITUNG_P_P)
        self.assertTrue(ok, f"Zeile {fehler}")
        self.assertEqual(HERLEITUNG_P_P[-1][0], PP)

    def test_04_fehlerhafte_herleitung_abgelehnt(self):
        falsch = HERLEITUNG_P_P[:2] + [(PP, ("MP", 0, 1))]  # Abkuerzung: MP liefert hier nicht p→p
        self.assertFalse(pruefe_herleitung(falsch)[0])
        self.assertFalse(pruefe_herleitung([(I(P, Q), "Ax")])[0])  # kein Axiom

    def test_05_korrektheit_jeder_zeile(self):
        for f, _ in HERLEITUNG_P_P:
            self.assertTrue(tautologie(f))

    def test_06_vergleich_goedel_g3(self):
        self.assertTrue(g3_gueltig(A1))
        self.assertTrue(g3_gueltig(A2))
        self.assertFalse(g3_gueltig(A3))
        self.assertTrue(tautologie(O(P, N(P))))
        self.assertFalse(g3_gueltig(O(P, N(P))))
        peirce = I(I(I(P, Q), P), P)
        self.assertTrue(tautologie(peirce))
        self.assertFalse(g3_gueltig(peirce))

    def test_07_bejahung_des_konsequens(self):
        self.assertEqual(gegenmodell([Q, I(P, Q)], P), {"p": False, "q": True})

    def test_08_unzulaessige_regel(self):
        # Regel „aus φ→ψ und ψ folgt φ“ ist nicht wahrheitserhaltend
        self.assertIsNotNone(gegenmodell([I(P, Q), Q], P))


if __name__ == "__main__":
    unittest.main(verbosity=2)
