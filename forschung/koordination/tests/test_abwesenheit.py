#!/usr/bin/env python3
"""Tests für die Abwesenheitserkennung R7: „10 Beiträge ohne Feedback/Analyse“ (synthetisch, ohne Git)."""
import datetime as dt
import importlib.util
import pathlib
import unittest

P = pathlib.Path(__file__).resolve().parents[1] / "werkzeuge/abwesenheit.py"
spec = importlib.util.spec_from_file_location("abwesenheit", P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
T0 = dt.datetime(2026, 11, 3, 12, tzinfo=dt.timezone.utc)
_n = [0]


def c(ki, stunde, feedback=False, betreff=None):
    _n[0] += 1
    return {"sha": f"{_n[0]:040d}", "zeit": T0 + dt.timedelta(hours=stunde), "ki": ki,
            "betreff": betreff or f"{ki} schritt {_n[0]}", "feedback": feedback}


def liste(*cs):
    return sorted(cs, key=lambda x: x["zeit"], reverse=True)


class T(unittest.TestCase):
    def test_zuordnung_und_kennzeichnung(self):
        self.assertEqual(m.zuordnen("x\n\nClaude-Session: https://…"), "claude")
        self.assertEqual(m.zuordnen("x\n\nKI: claude"), "claude")
        self.assertEqual(m.zuordnen("web: fix\n\nKI: gpt"), "gpt")
        self.assertEqual(m.zuordnen("docs: tippfehler\n\nKI: nils"), "nils")
        self.assertEqual(m.zuordnen("web: fix"), "gpt")
        self.assertEqual(m.zuordnen("web: fix", streng=True), "unbekannt")

    def test_feedback_erkennung(self):
        self.assertTrue(m.ist_feedback("x\n\nAnalyse-von: abc123..def456", []))
        self.assertTrue(m.ist_feedback("x\n\nFeedback-zu: REV-007", []))
        self.assertTrue(m.ist_feedback("x", ["forschung/koordination/zyklen/K/GPT_DISKUSSION_08.md"]))
        self.assertTrue(m.ist_feedback("x", ["forschung/koordination/NACHHOLANALYSE_CLAUDE_2026-11-03.md"]))
        self.assertTrue(m.ist_feedback("x", ["forschung/koordination/REVIEW_QUEUE_V2.json"]))
        self.assertFalse(m.ist_feedback("web: neue Seite", ["docs/index.html", "forschung/website/X_REVIEW.md"]))

    def test_neun_beitraege_noch_anwesend(self):
        cs = [c("claude", 0, feedback=True)] + [c("gpt", 1 + i) for i in range(9)]
        self.assertFalse(m.bewerten(liste(*cs))["claude"]["abwesend"])

    def test_zehn_beitraege_ohne_feedback_abwesend(self):
        cs = [c("claude", 0, feedback=True)] + [c("gpt", 1 + i) for i in range(10)]
        e = m.bewerten(liste(*cs))["claude"]
        self.assertTrue(e["abwesend"])
        self.assertEqual(e["unbeantwortete_beitraege_der_anderen_ki"], 10)

    def test_eigene_arbeit_ohne_feedback_setzt_nicht_zurueck(self):
        cs = [c("claude", 0, feedback=True)] + [c("gpt", 1 + i) for i in range(10)] + [c("claude", 20)]
        self.assertTrue(m.bewerten(liste(*cs))["claude"]["abwesend"])

    def test_feedback_setzt_zurueck(self):
        cs = [c("gpt", 1 + i) for i in range(12)] + [c("claude", 20, feedback=True)]
        self.assertFalse(m.bewerten(liste(*cs))["claude"]["abwesend"])

    def test_dateicommits_mit_gleichem_betreff_sind_ein_beitrag(self):
        cs = [c("claude", 0, feedback=True)] + [c("gpt", 1 + 0.01 * i, betreff="web: eine Änderung") for i in range(30)]
        self.assertEqual(m.bewerten(liste(*cs))["claude"]["unbeantwortete_beitraege_der_anderen_ki"], 1)

    def test_nils_zaehlt_nicht(self):
        cs = [c("claude", 0, feedback=True)] + [c("nils", 1 + i) for i in range(15)]
        self.assertFalse(m.bewerten(liste(*cs))["claude"]["abwesend"])


if __name__ == "__main__":
    unittest.main()
