"""Reproduzierbare synthetische Tests zum GII-XML-Adapter."""
import unittest
from bki_gii_adapter import extract, ImportErrorWithContext

URL = "https://www.gesetze-im-internet.de/bmg/BMG.xml"
VALID = b'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE dokumente SYSTEM "https://www.gesetze-im-internet.de/dtd/1.01/gii-norm.dtd">
<dokumente><norm><metadaten><jurabk>BMG</jurabk><enbez>\\xc2\\xa7 18</enbez>
<titel>Meldebescheinigung</titel></metadaten><textdaten><text><Content><P>Eine Meldebescheinigung.</P></Content></text></textdaten></norm></dokumente>'''.replace(b'\\xc2\\xa7', '§'.encode('utf-8'))

class AdapterTests(unittest.TestCase):
    def test_extract_with_provenance(self):
        r = extract(VALID, "bmg", URL, "2026-11-04")
        self.assertEqual(r["provisions"][0]["provision_id"], "BMG-§18")
        self.assertFalse(r["legal_validity_checked"])
        self.assertFalse(r["local_authority_checked"])
        self.assertEqual(len(r["source_sha256"]), 64)

    def test_duplicate_norm_rejected(self):
        start = VALID.index(b"<norm>")
        end = VALID.index(b"</norm>") + len(b"</norm>")
        bad = VALID.replace(b"</dokumente>", VALID[start:end] + b"</dokumente>")
        with self.assertRaisesRegex(ImportErrorWithContext, "Doppelte"):
            extract(bad, "bmg", URL, "2026-11-04")

    def test_invalid_source(self):
        with self.assertRaisesRegex(ImportErrorWithContext, "Original"):
            extract(VALID, "bmg", "https://example.org/a.xml", "2026-11-04")

    def test_entity_declaration_rejected(self):
        bad = b'<!DOCTYPE dokumente [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>' + VALID
        with self.assertRaises(ImportErrorWithContext):
            extract(bad, "bmg", URL, "2026-11-04")

    def test_missing_norm(self):
        with self.assertRaises(ImportErrorWithContext):
            extract(b"<root/>", "bmg", URL, "2026-11-04")

    def test_mismatch_law(self):
        with self.assertRaises(ImportErrorWithContext):
            extract(VALID, "gewo", "https://www.gesetze-im-internet.de/gewo/GewO.xml", "2026-11-04")

if __name__ == "__main__":
    unittest.main()
