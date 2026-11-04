"""Projektregeleinheitstests: Originaltext darf nie in MD/JSON erscheinen."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from weisungsatlas_atomizer import extract_structure, main

MARKER = "ABSOLUT_VERBOTENER_ORIGINALSATZ_KI_BKI_787"


class ReconstructionTests(unittest.TestCase):
    def test_txt_export_never_contains_original_text(self):
        with tempfile.TemporaryDirectory() as base:
            base = Path(base)
            inp = base / "test.txt"
            inp.write_text(MARKER + " muss für alle berücksichtigt werden.\n", encoding="utf-8")
            out = base / "out"
            argv = ["atomizer", str(inp), "--id", "TEST-SRC-01",
                    "--url", "https://example.org/original", "--issuer", "Testamt",
                    "--retrieved-at", "2026-11-05", "--out", str(out)]
            with patch("sys.argv", argv):
                self.assertEqual(main(), 0)
            md = (out / "TEST-SRC-01.md").read_text(encoding="utf-8")
            data = (out / "TEST-SRC-01.source.json").read_text(encoding="utf-8")
            self.assertNotIn(MARKER, md)
            self.assertNotIn(MARKER, data)
            self.assertIn("nicht übernommen", md)
            self.assertEqual(json.loads(data)["atom_candidates"], [])
            self.assertFalse(json.loads(data)["original_text_exported"])

    def test_html_export_never_contains_original_text(self):
        with tempfile.TemporaryDirectory() as base:
            base = Path(base)
            inp = base / "test.html"
            inp.write_text("<html><p>" + MARKER + "</p></html>", encoding="utf-8")
            out = base / "out"
            argv = ["atomizer", str(inp), "--id", "TEST-SRC-02",
                    "--url", "https://example.org/original", "--issuer", "Testamt",
                    "--retrieved-at", "2026-11-05", "--out", str(out)]
            with patch("sys.argv", argv):
                self.assertEqual(main(), 0)
            self.assertNotIn(MARKER, (out / "TEST-SRC-02.md").read_text())
            self.assertNotIn(MARKER, (out / "TEST-SRC-02.source.json").read_text())

    def test_no_unverified_pdf_copy(self):
        with tempfile.TemporaryDirectory() as base:
            f = Path(base) / "fake.pdf"
            f.write_bytes(b"%PDF-0.1" + MARKER.encode("utf-8"))
            with self.assertRaises((ValueError, Exception)):
                # PDF-Parser darf fehlerhafte PDF nicht als gültig akzeptieren.
                extract_structure(f)


if __name__ == "__main__":
    unittest.main()
