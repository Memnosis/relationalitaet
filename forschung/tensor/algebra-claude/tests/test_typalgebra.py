#!/usr/bin/env python3
"""Tests der typisierten Tensoralgebra mit konstruierten Fällen je Klasse und Negativproben."""
import importlib.util
import pathlib
import unittest

H = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("typalgebra", H / "typalgebra.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)
ALLE = [f"{m}-{k}-{s}" for m in ("NM", "ZM", "UM") for k in ("I", "II", "III") for s in ("α", "β", "γ")]


def T(i, pfade, felder=None):
    return {"id": i, "felder": felder if felder is not None else {a: f"{i}:{a}" for a in ALLE},
            "pfade": [{"adressen": p, "typ": t} for p, t in pfade]}


PRJ = (["NM-I-γ", "ZM-II-γ", "UM-III-γ"], "PRJ")
PRJ2 = (["NM-I-γ", "ZM-II-γ", "UM-II-γ"], "PRJ")
RST = (["UM-II-β", "ZM-I-β", "NM-I-β"], "RST")
CYC = (["ZM-II-α", "ZM-II-β", "ZM-II-γ"], "CYC")
AUF = (["NM-II-β", "ZM-II-β", "UM-II-β"], None)


class Typen(unittest.TestCase):
    def test_signaturen(self):
        self.assertEqual(ta.signatur(PRJ[0]), "auf")
        self.assertEqual(ta.signatur(RST[0]), "ab")
        self.assertEqual(ta.signatur(CYC[0]), "schicht")
        self.assertEqual(ta.signatur(["NM-I-α", "UM-I-α", "ZM-I-α"]), "gemischt")

    def test_T1_cyc_ausserhalb_klasse_II(self):
        k = ta.typpruefung(T("X", [(["NM-I-β", "ZM-I-β", "UM-I-β"], "CYC")]))
        self.assertEqual([x["regel"] for x in k], ["T1"])

    def test_cyc_in_klasse_II_auch_ueber_schichten_erlaubt(self):
        self.assertEqual(ta.typpruefung(T("X", [(AUF[0], "CYC")])), [])

    def test_T1_prj_mit_modus_wechsel(self):
        k = ta.typpruefung(T("X", [(["NM-I-α", "ZM-II-β", "UM-III-γ"], "PRJ")]))
        self.assertEqual([x["regel"] for x in k], ["T1"])

    def test_T2_nur_bei_regelverletzung_sonst_mehrfachtyp(self):
        x = T("X", [(AUF[0], "REC"), (AUF[0], "CYC")])
        self.assertEqual(ta.typpruefung(x), [])
        self.assertEqual(len(ta.mehrfachtypen(x)), 1)
        y = T("Y", [(AUF[0], "REC"), (AUF[0], "RST")])
        self.assertIn("T2", [k["regel"] for k in ta.typpruefung(y)])

    def test_korrekte_typen_ohne_konflikt(self):
        self.assertEqual(ta.typpruefung(T("X", [PRJ, RST, CYC])), [])


class Vergleich(unittest.TestCase):
    def test_gleich(self):
        self.assertEqual(ta.vergleich(T("A", [PRJ, RST]), T("B", [RST, PRJ]))["klasse"], "gleich")

    def test_spezialfall(self):
        self.assertEqual(ta.vergleich(T("A", [PRJ]), T("B", [PRJ, RST]))["klasse"], "spezialfall_t1_in_t2")

    def test_variante_ein_endpunkt_anders(self):
        v = ta.vergleich(T("A", [PRJ]), T("B", [PRJ2]))
        self.assertEqual(v["klasse"], "variante")
        self.assertEqual(len(v["varianten"]), 1)

    def test_unabhaengig(self):
        self.assertEqual(ta.vergleich(T("A", [CYC]), T("B", [PRJ]))["klasse"], "unabhaengig")

    def test_ohne_pfade_unbestimmt(self):
        self.assertEqual(ta.vergleich(T("A", []), T("B", [PRJ]))["klasse"], "unbestimmt")


class Ueberlagerung(unittest.TestCase):
    def test_hysterese_neu_und_alle_pruefungen(self):
        e = ta.lauf([T("A", [AUF]), T("B", [RST])])[0]
        k = [x for x in e["ueberlagerung"] if x["hysterese"]]
        self.assertEqual(len(k), 1)
        self.assertTrue(k[0]["gilt_als_neue_beziehung"])
        self.assertEqual(k[0]["hysterese_abweichung"]["klasse"], ["II", "I"])

    def test_echte_umkehr_ist_keine_hysterese(self):
        zurueck = (list(reversed(AUF[0])), "RST")
        e = ta.lauf([T("A", [AUF]), T("B", [zurueck])])[0]
        k = [x for x in e["ueberlagerung"] if x["verkettung"][0] == "NM-II-β"]
        self.assertTrue(k and not k[0]["hysterese"] and k[0]["geschlossener_umlauf"])

    def test_P1_scheitert_bei_typkonflikt(self):
        e = ta.lauf([T("A", [(AUF[0], "PRJ"), (AUF[0], "RST")]), T("B", [RST])])[0]
        self.assertTrue(all(not x["P1_aussageerhalt"] for x in e["ueberlagerung"]))

    def test_P1_scheitert_bei_fehlenden_feldern(self):
        e = ta.lauf([T("A", [AUF], felder={}), T("B", [RST])])[0]
        self.assertTrue(all(not x["P1_aussageerhalt"] for x in e["ueberlagerung"]))

    def test_P2_nicht_neu_wenn_schon_im_eigenen_tensor(self):
        verkettet = (AUF[0] + RST[0][1:], None)
        e = ta.lauf([T("A", [AUF, verkettet]), T("B", [RST])])[0]
        k = [x for x in e["ueberlagerung"] if x["verkettung"] == verkettet[0]]
        self.assertTrue(k and not k[0]["P2_neu"])

    def test_P2_nicht_neu_wenn_dritter_tensor_es_schon_enthaelt(self):
        dritter = T("C", [AUF, RST])  # enthält beide Bausteine selbst
        e = [x for x in ta.lauf([T("A", [AUF]), T("B", [RST]), dritter]) if x["paar"] == ["A", "B"]][0]
        k = [x for x in e["ueberlagerung"] if x["hysterese"]][0]
        self.assertTrue(k["P2_neu"] and not k["P2_neu_korpus"])
        self.assertEqual(k["bereits_enthalten_in"], ["C"])
        self.assertFalse(k["gilt_als_neue_beziehung"])

    def test_P3_deterministisch_bei_vertauschter_reihenfolge(self):
        a, b = T("A", [AUF, PRJ]), T("B", [RST, PRJ2])
        self.assertEqual(ta.kanon(ta.lauf([a, b])), ta.kanon(ta.lauf([b, a])))


if __name__ == "__main__":
    unittest.main()
