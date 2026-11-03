#!/usr/bin/env python3
"""Tests für die Abwesenheitserkennung R7 (synthetische Commits, keine Git-Abhängigkeit)."""
import datetime as dt
import importlib.util
import pathlib
import unittest

P = pathlib.Path(__file__).resolve().parents[1] / "werkzeuge/abwesenheit.py"
spec = importlib.util.spec_from_file_location("abwesenheit", P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
T0 = dt.datetime(2026, 11, 3, 12, tzinfo=dt.timezone.utc)


def c(ki, stunden, betreff=None):
    return {"sha": f"{ki}{stunden:05.1f}".ljust(40, "0"), "zeit": T0 + dt.timedelta(hours=stunden), "ki": ki,
            "betreff": betreff or f"schritt {ki} {stunden}"}


def liste(*cs):
    return sorted(cs, key=lambda x: x["zeit"], reverse=True)


class T(unittest.TestCase):
    def test_zuordnung(self):
        self.assertEqual(m.zuordnen("x\n\nClaude-Session: https://…"), "claude")
        self.assertEqual(m.zuordnen("x\n\nCo-Authored-By: Claude Opus <n@a.com>"), "claude")
        self.assertEqual(m.zuordnen("web: fix\n\nKI: gpt"), "gpt")
        self.assertEqual(m.zuordnen("web: fix"), "gpt")
        self.assertEqual(m.zuordnen("web: fix", streng=True), "unbekannt")

    def test_beide_aktiv(self):
        e = m.bewerten(liste(c("claude", 0), c("gpt", 1), c("claude", 2)), T0 + dt.timedelta(hours=3), 12, 25, {})
        self.assertFalse(e["claude"]["abwesend"])
        self.assertFalse(e["gpt"]["abwesend"])

    def test_zeit_ausloeser(self):
        e = m.bewerten(liste(c("gpt", 0), c("claude", 1)), T0 + dt.timedelta(hours=14), 12, 25, {"gpt": ["REV-009"]})
        self.assertTrue(e["gpt"]["abwesend"])
        self.assertEqual(e["gpt"]["ausloeser"], ["zeit", "pruefbitte"])
        self.assertEqual(e["gpt"]["offene_pruefbitten"], ["REV-009"])
        self.assertFalse(e["claude"]["abwesend"])

    def test_zeit_ohne_aktivitaet_der_anderen_ist_keine_abwesenheit(self):
        e = m.bewerten(liste(c("claude", 0), c("gpt", 1)), T0 + dt.timedelta(hours=40), 12, 25, {})
        self.assertFalse(e["gpt"]["abwesend"])
        self.assertTrue(e["claude"]["abwesend"])  # GPT war nach Claudes letztem Commit aktiv

    def test_schritte_ausloeser(self):
        cs = [c("claude", 0)] + [c("gpt", 0.1 * i) for i in range(1, 27)]
        e = m.bewerten(liste(*cs), T0 + dt.timedelta(hours=3), 12, 25, {})
        self.assertTrue(e["claude"]["abwesend"])
        self.assertEqual(e["claude"]["ausloeser"], ["schritte"])
        self.assertEqual(e["claude"]["arbeitsschritte_der_anderen_ki_seitdem"], 26)

    def test_dateicommits_mit_gleichem_betreff_sind_ein_schritt(self):
        cs = [c("claude", 0)] + [c("gpt", 0.1 * i, "web: eine Änderung") for i in range(1, 40)]
        e = m.bewerten(liste(*cs), T0 + dt.timedelta(hours=5), 12, 25, {})
        self.assertFalse(e["claude"]["abwesend"])
        self.assertEqual(e["claude"]["commits_der_anderen_ki_seitdem"], 39)
        self.assertEqual(e["claude"]["arbeitsschritte_der_anderen_ki_seitdem"], 1)

    def test_offene_pruefbitte_frueher_ausloeser(self):
        e = m.bewerten(liste(c("gpt", 0), c("claude", 1)), T0 + dt.timedelta(hours=4), 12, 100, {"gpt": ["REV-010"]})
        self.assertEqual(e["gpt"]["ausloeser"], ["pruefbitte"])
        e = m.bewerten(liste(c("gpt", 0), c("claude", 1)), T0 + dt.timedelta(hours=2), 12, 100, {"gpt": ["REV-010"]})
        self.assertFalse(e["gpt"]["abwesend"])


if __name__ == "__main__":
    unittest.main()
