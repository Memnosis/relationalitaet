#!/usr/bin/env python3
"""Formale Tests K4 (Schritt S3, P0-X4 wissenschaftlicher Teil). Owner: Claude. Nur Standardbibliothek.

Ausfuehren:  python3 forschung/tensor/logik-claude/tests/test_formal_k4.py
Jeder Test prueft eine klar begrenzte mathematische Aussage. Ein bestandener Test belegt
NUR diese Aussage, nicht eine Tensor- oder Feldtheorie.

TST-K4-MP-001   Modus ponens ist in der klassischen Aussagenlogik semantisch gueltig ({P, P->Q} |= Q).
TST-K4-MP-002   Gegenmodell: {P->Q} |/= Q (Belegung P=Q=falsch).
TST-K4-MP-003   Fehlschluss "Bejahung des Konsequens" {Q, P->Q} |/= P hat ein Gegenmodell.
TST-K4-G-001    P3 x P3 x P3 (Flaechennachbarschaft) hat 27 Knoten und 54 Kanten.
TST-K4-G-002    K3 x K3 x K3 (Hamming-Nachbarschaft) hat 27 Knoten und 81 Kanten.
TST-K4-G-003    Im Pfadmodell trennt die Mittelschicht (x=1) die Schichten x=0 und x=2; im Hammingmodell nicht.
TST-K4-G-004    Das Zentrum (1,1,1) allein ist in beiden Modellen kein Schnittknoten.
TST-K4-ALG-001  Z27 und (Z3)^3 haben 27 Elemente, sind aber nicht isomorph (maximale Elementordnung 27 bzw. 3).
"""
import itertools
import unittest
from math import gcd


def impl(a, b):
    return (not a) or b


def folgt(praemissen, konklusion, variablen=("P", "Q")):
    """Semantische Folgerung durch vollstaendige Wahrheitstafel; gibt (gilt, gegenmodell) zurueck."""
    for werte in itertools.product((False, True), repeat=len(variablen)):
        b = dict(zip(variablen, werte))
        if all(p(b) for p in praemissen) and not konklusion(b):
            return False, b
    return True, None


KNOTEN = list(itertools.product(range(3), repeat=3))


def kanten(nachbar):
    return {frozenset((u, v)) for u in KNOTEN for v in KNOTEN if u < v and nachbar(u, v)}


def pfad_nachbar(u, v):  # Flaechennachbarschaft: genau eine Koordinate um 1 verschieden
    d = [abs(a - b) for a, b in zip(u, v)]
    return sorted(d) == [0, 0, 1]


def hamming_nachbar(u, v):  # genau eine Koordinate verschieden (beliebiger Wert)
    return sum(a != b for a, b in zip(u, v)) == 1


def zusammenhaengend(knoten, ks):
    knoten = set(knoten)
    if not knoten:
        return True
    start = next(iter(knoten))
    gesehen, stapel = {start}, [start]
    while stapel:
        x = stapel.pop()
        for k in ks:
            if x in k:
                (y,) = k - {x}
                if y in knoten and y not in gesehen:
                    gesehen.add(y)
                    stapel.append(y)
    return gesehen == knoten


def ohne(ks, entfernt):
    return {k for k in ks if not (k & entfernt)}


class Logik(unittest.TestCase):
    def test_mp_001_modus_ponens_gueltig(self):
        gilt, gm = folgt([lambda b: b["P"], lambda b: impl(b["P"], b["Q"])], lambda b: b["Q"])
        self.assertTrue(gilt)
        self.assertIsNone(gm)

    def test_mp_002_ohne_zweite_praemisse_gegenmodell(self):
        gilt, gm = folgt([lambda b: impl(b["P"], b["Q"])], lambda b: b["Q"])
        self.assertFalse(gilt)
        self.assertEqual(gm, {"P": False, "Q": False})

    def test_mp_003_bejahung_des_konsequens_ungueltig(self):
        gilt, gm = folgt([lambda b: b["Q"], lambda b: impl(b["P"], b["Q"])], lambda b: b["P"])
        self.assertFalse(gilt)
        self.assertEqual(gm, {"P": False, "Q": True})


class Graph(unittest.TestCase):
    def test_g_001_pfadmodell(self):
        self.assertEqual(len(KNOTEN), 27)
        self.assertEqual(len(kanten(pfad_nachbar)), 54)

    def test_g_002_hammingmodell(self):
        self.assertEqual(len(kanten(hamming_nachbar)), 81)

    def test_g_003_mittelschicht(self):
        mitte = {v for v in KNOTEN if v[0] == 1}
        rest = [v for v in KNOTEN if v[0] != 1]
        self.assertFalse(zusammenhaengend(rest, ohne(kanten(pfad_nachbar), mitte)),
                         "Pfadmodell: ohne Mittelschicht muessen x=0 und x=2 getrennt sein")
        self.assertTrue(zusammenhaengend(rest, ohne(kanten(hamming_nachbar), mitte)),
                        "Hammingmodell: 0 und 2 sind direkt benachbart, Mittelschicht trennt nicht")

    def test_g_004_zentrum_kein_schnitt(self):
        z = {(1, 1, 1)}
        rest = [v for v in KNOTEN if v not in z]
        for nb in (pfad_nachbar, hamming_nachbar):
            self.assertTrue(zusammenhaengend(rest, ohne(kanten(nb), z)))


class Algebra(unittest.TestCase):
    def test_alg_001_z27_nicht_isomorph_z3hoch3(self):
        ordnung_z27 = [27 // gcd(a, 27) for a in range(27)]
        ordnung_z3_3 = [1 if v == (0, 0, 0) else 3 for v in KNOTEN]
        self.assertEqual(len(ordnung_z27), 27)
        self.assertEqual(len(ordnung_z3_3), 27)
        self.assertEqual(max(ordnung_z27), 27)
        self.assertEqual(max(ordnung_z3_3), 3)
        # Isomorphismen erhalten Elementordnungen; die Verteilungen unterscheiden sich
        self.assertNotEqual(sorted(ordnung_z27), sorted(ordnung_z3_3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
