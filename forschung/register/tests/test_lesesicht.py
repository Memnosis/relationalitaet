#!/usr/bin/env python3
"""Tests Lesesicht (Positiv-/Negativfälle). Ausführen: python3 forschung/register/tests/test_lesesicht.py"""
import copy, importlib.util, json, pathlib, unittest
W = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("ls", W / "forschung/register/werkzeuge/lesesicht.py"); ls = importlib.util.module_from_spec(spec); spec.loader.exec_module(ls)
REF = json.loads((W / "forschung/register/QUELLEN_REFERENZSET_V0_1.json").read_text(encoding="utf-8"))
ZU = json.loads((W / "forschung/register/oeffentlich/SEITENZUORDNUNG_V0_1.json").read_text(encoding="utf-8"))
REG = json.loads((W / "forschung/tensor/logik-claude/LOGIK_CLAIMREGISTER_V0_1.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((W / "forschung/register/schema/web-lesesicht.schema.json").read_text(encoding="utf-8"))


def mit(claims, tmp):
    p = tmp / "c.json"; p.write_text(json.dumps({"claims": claims}, ensure_ascii=False), encoding="utf-8"); return str(p)


class Lesesicht(unittest.TestCase):
    def setUp(self):
        import tempfile; self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.c = copy.deepcopy(next(c for c in REG["claims"] if c["claim_id"] == "CLM-LOGIK10-FELD-UM-I-A"))

    def test_heute_nichts_freigegeben(self):
        out = ls.erzeuge(["forschung/tensor/logik-claude/LOGIK_CLAIMREGISTER_V0_1.json"], ZU, REF, "abc1234")
        self.assertEqual(out["eintraege"], [])

    def test_freigegebener_claim_erscheint(self):
        self.c["public_release"] = True; self.c["redaktion"] = "freigegeben"
        out = ls.erzeuge([mit([self.c], self.tmp)], ZU, REF, "abc1234")
        self.assertEqual(len(out["eintraege"]), 1)
        e = out["eintraege"][0]
        self.assertEqual((e["page_id"], e["section_id"], e["version_doi"], e["license"]), ("tensor-paper", "logik-forschungsstand", "10.5281/zenodo.19282895", "cc-by-4.0"))
        self.assertIn("S. 5", e["pinpoint"])

    def test_intern_nie_auch_wenn_freigegeben(self):
        self.c["public_release"] = True; self.c["vertraulichkeit"] = "intern"
        self.assertEqual(ls.erzeuge([mit([self.c], self.tmp)], ZU, REF, "abc1234")["eintraege"], [])

    def test_quelle_ausserhalb_referenzset_ausgeschlossen(self):
        self.c["public_release"] = True; self.c["source_id"] = "SRC-ZEN-18725587"  # nicht freigegebenes Werk
        self.assertEqual(ls.erzeuge([mit([self.c], self.tmp)], ZU, REF, "abc1234")["eintraege"], [])

    def test_schema_gueltig(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema fehlt")
        self.c["public_release"] = True
        out = ls.erzeuge([mit([self.c], self.tmp)], ZU, REF, "abc1234")
        jsonschema.Draft202012Validator(SCHEMA).validate(out)
        out["eintraege"][0]["intern_feld"] = "x"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SCHEMA).validate(out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
