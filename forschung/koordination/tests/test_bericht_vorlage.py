#!/usr/bin/env python3
"""Tests für den Berichtsgenerator (R2/R3/R7): roter Rahmen, Pflicht-Anhang, Repo-Schutz."""
import json
import pathlib
import shutil
import subprocess
import tempfile
import unittest
import zipfile

V = pathlib.Path(__file__).resolve().parents[1] / "berichte/vorlage"
GEN = V / "bericht_docx.mjs"


def node(*a):
    return subprocess.run(["node", str(GEN), *map(str, a)], capture_output=True, text=True)


@unittest.skipUnless(shutil.which("node"), "node fehlt")
class T(unittest.TestCase):
    def test_beispiel_gueltig(self):
        r = node("--pruefen", V / "BEISPIEL_BERICHT.json")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_negativ_abgelehnt(self):
        r = node("--pruefen", V / "NEGATIV_BERICHT.json")
        self.assertEqual(r.returncode, 1)
        for erwartet in ("abwesenheit.ki", "Empfehlung beider KIs", "wenn_nicht", "2 bis 4 Optionen"):
            self.assertIn(erwartet, r.stderr)

    def test_ausgabe_ins_repo_verweigert(self):
        r = node(V / "BEISPIEL_BERICHT.json", V / "x.docx")
        self.assertEqual(r.returncode, 3)
        self.assertFalse((V / "x.docx").exists())

    def test_roter_rahmen_steht_vor_dem_bericht_und_anhang_hat_alle_erklaerungen(self):
        with tempfile.TemporaryDirectory() as d:
            ziel = pathlib.Path(d) / "b.docx"
            r = node(V / "BEISPIEL_BERICHT.json", ziel)
            self.assertEqual(r.returncode, 0, r.stderr)
            xml = zipfile.ZipFile(ziel).read("word/document.xml").decode("utf-8")
        rahmen = xml.find("ENTSCHEIDUNGEN UND FREIGABEN")
        self.assertGreater(rahmen, 0)
        self.assertLess(rahmen, xml.find("Ampel und Kernaussage"))
        self.assertIn('w:color="C0392B"', xml)  # roter Rahmen
        self.assertLess(xml.find("Ampel und Kernaussage"), xml.find("Anhang A · Ausführliche"))
        b = json.loads((V / "BEISPIEL_BERICHT.json").read_text(encoding="utf-8"))
        for i, e in enumerate(b["entscheidungen"], 1):
            self.assertIn(f"A{i} · {e['id']}", xml)

    def test_ohne_offene_entscheidung_bleibt_rahmen_sichtbar(self):
        b = json.loads((V / "BEISPIEL_BERICHT.json").read_text(encoding="utf-8"))
        b["entscheidungen"] = []
        with tempfile.TemporaryDirectory() as d:
            j = pathlib.Path(d) / "b.json"; j.write_text(json.dumps(b), encoding="utf-8")
            ziel = pathlib.Path(d) / "b.docx"
            self.assertEqual(node(j, ziel).returncode, 0)
            xml = zipfile.ZipFile(ziel).read("word/document.xml").decode("utf-8")
        self.assertIn("keine offen", xml)


if __name__ == "__main__":
    unittest.main()
