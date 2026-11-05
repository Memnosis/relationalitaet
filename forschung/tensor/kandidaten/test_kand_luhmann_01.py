#!/usr/bin/env python3
"""Executable structural and semantic-guard tests for KAND-LUHMANN-01.
Run: python -m unittest forschung/tensor/kandidaten/test_kand_luhmann_01.py -v
These tests do NOT demonstrate a validated Luhmann theory or intertheory isomorphism.
"""
import json
import unittest
from pathlib import Path

SOURCE = Path(__file__).with_name("KAND-LUHMANN-01_v0_1.json")
M = ["NM", "ZM", "UM"]
K = ["I", "II", "III"]
S = ["α", "β", "γ"]

def parse_address(address):
    m, k, s = address.split("-")
    return (M.index(m), K.index(k), S.index(s))

def encode_address(position):
    i, j, k = position
    return f"{M[i]}-{K[j]}-{S[k]}"

def shift(position, delta):
    return tuple((a+b) % 3 for a, b in zip(position, delta))

def coords_to_plane(position):
    """Injectively encode three indices into a 3-D Euclidean coordinate tuple."""
    return tuple(float(v) for v in position)

def translate(p, d):
    return tuple(a+b for a, b in zip(p, d))

class LuhmannTransferChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = json.loads(SOURCE.read_text(encoding="utf-8"))
        cls.cells = cls.doc["cells"]

    def test_01_complete_unique_addresses(self):
        self.assertEqual(len(self.cells), 27)
        self.assertEqual(len({c["address"] for c in self.cells}), 27)

    def test_02_address_roundtrip(self):
        for c in self.cells:
            self.assertEqual(encode_address(parse_address(c["address"])), c["address"])

    def test_03_all_three_axes_present(self):
        for axis in ("M", "K", "S"):
            self.assertEqual(len(self.doc["basis"]["indexes"][axis]), 3)

    def test_04_geometry_encoding_injective(self):
        coords = [coords_to_plane(parse_address(c["address"])) for c in self.cells]
        self.assertEqual(len(set(coords)), 27)

    def test_05_translation_is_reversible(self):
        d = (7.0, -2.0, 0.5)
        for c in self.cells:
            p = coords_to_plane(parse_address(c["address"]))
            self.assertEqual(translate(translate(p,d),tuple(-x for x in d)),p)

    def test_06_geometric_composition(self):
        a,b=(1.0,0.0,2.0),(0.0,-2.0,3.0)
        for c in self.cells:
            p=coords_to_plane(parse_address(c["address"]))
            self.assertEqual(translate(translate(p,a),b),
                             translate(p,tuple(x+y for x,y in zip(a,b))))

    def test_07_coordinate_projection_loses_information(self):
        coords=[parse_address(c["address"]) for c in self.cells]
        self.assertEqual(len({c[:2] for c in coords}),9)
        self.assertLess(9,len(coords))

    def test_08_same_geometric_rotation_is_not_same_semantic_role(self):
        # The project may rotate coordinates, but may NOT infer that an
        # Information role has become a factual/time/social dimension role.
        p=(0,1,2)
        rotated=(p[1],p[2],p[0])
        self.assertNotEqual(p,rotated)
        self.assertNotEqual(self.doc["basis"]["indexes"]["M"][p[0]],
                            self.doc["basis"]["indexes"]["M"][rotated[0]])

    def test_09_all_cells_are_unverified_questions(self):
        self.assertTrue(all(c["claim_status"]=="unverified_research_question"
                            and not c["evidence_ids"] for c in self.cells))

    def test_10_five_luhmann_modules_preserved(self):
        ids={"LU-01","LU-02"}|{x["id"] for x in self.doc["modules"]}
        self.assertEqual(ids,{"LU-01","LU-02","LU-03","LU-04","LU-05"})

    def test_11_three_cyclic_index_shifts_return(self):
        for c in self.cells:
            p=parse_address(c["address"])
            q=p
            for _ in range(3):
                q=shift(q,(1,1,1))
            self.assertEqual(q,p)

    def test_12_source_is_not_a_geometric_semantics_proof(self):
        self.assertTrue(self.doc["not_historical_tensor"])
        self.assertIn("No mathematical isomorphism",
                      " ".join(self.doc["transfer_key"]["limitations"]))

if __name__=="__main__":
    unittest.main()
