#!/usr/bin/env python3
"""Tests PM-Status aus Nachweisen. Ausführen: python3 forschung/register/tests/test_pm_status.py"""
import importlib.util, json, pathlib, unittest
W = pathlib.Path(__file__).resolve().parents[3]
s = importlib.util.spec_from_file_location("pm", W / "forschung/register/werkzeuge/pm_status.py"); pm = importlib.util.module_from_spec(s); s.loader.exec_module(pm)
L = lambda p: json.loads((W / p).read_text(encoding="utf-8"))
REG = L("forschung/register/oeffentlich/EVIDENZREGELN_PM_V0_1.json")
STATUS = {"acknowledgements": {"gpt_reviewed": False, "gpt_partial_review_delivered": True}}


class PMStatus(unittest.TestCase):
    def run_(self, testreg=None, repro="", status=STATUS, n=0):
        return {t["task_id"]: t["stages"] for t in pm.berechne(REG, testreg or L("forschung/register/TESTREGISTER_V0_1.json"), repro, status, n)}

    def test_echte_nachweise(self):
        r = self.run_()
        self.assertEqual(r["PM-DATA-01"]["implementation"], 1.0)
        self.assertEqual(r["PM-DATA-01"]["testing"], 1.0)
        self.assertEqual(r["PM-DATA-01"]["peer_review"], 0.5)   # nur Teilprüfung GPT
        self.assertEqual(r["PM-DATA-02"]["implementation"], 0.5)  # Achsen-Crosswalk fehlt
        self.assertEqual(r["PM-THESIS-01"]["implementation"], 0.0)

    def test_ohne_tests_keine_teststufe(self):
        leer = {"tests": []}
        self.assertEqual(self.run_(testreg=leer)["PM-DATA-01"]["testing"], 0.0)

    def test_manuelles_checked_wird_ignoriert(self):
        fake = {"tests": [{"test_id": "TST-LS-01", "ergebnis": "checked"}]}
        self.assertEqual(self.run_(testreg=fake)["PM-DATA-01"]["testing"], 0.0)

    def test_release_nie_ohne_freigabe(self):
        r = self.run_(n=0)
        self.assertTrue(all(v["release"] == 0.0 for v in r.values()))
        self.assertEqual(self.run_(n=3)["PM-DATA-01"]["release"], 1.0)

    def test_volle_gegenpruefung_hebt_stufe(self):
        st = {"acknowledgements": {"gpt_reviewed": True}}
        self.assertEqual(self.run_(status=st)["PM-DATA-01"]["peer_review"], 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
