#!/usr/bin/env python3
"""Top-100-Formeln auf trinitäre und tensorale Strukturen analysieren. Owner: Claude. Ausgabe: TOP100_ERGEBNIS_V0_1.json
Die Liste FORMELN_TOP100_V0_1.json ist von Claude kuratiert (bekannte Formeln aus Schul- und Grundstudium), keine amtliche Rangliste.
Aufruf: python3 forschung/tensor/formeln/top100_lauf.py   (benötigt sympy; sonst SKIP Exit 77)
"""
import importlib.util
import json
import pathlib
import sys

try:
    import sympy  # noqa: F401
except ImportError:
    print("SKIP: sympy fehlt – Exit 77")
    sys.exit(77)
H = pathlib.Path(__file__).resolve().parent
W = H.parents[2]
spec = importlib.util.spec_from_file_location("fs", H / "formel_struktur.py")
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)
d = json.loads((H / "FORMELN_TOP100_V0_1.json").read_text(encoding="utf-8"))
inv = json.loads((W / "docs/data/tensor-inventar-v10_7.json").read_text(encoding="utf-8"))["tensors"]
erg = [fs.analysiere(f) for f in d["formeln"]]
b = fs.bestand(erg, inv)
out = {"schema_version": "top100-ergebnis/0.1", "owner": "claude", "quelle": "FORMELN_TOP100_V0_1.json",
       "zusammenfassung": {k: b[k] for k in ("formeln", "auswertbar", "trinitaer", "stelligkeit", "triadentypen", "dynamik",
                                              "tensorkeime_anzahl", "keimformen")},
       "familien": b["familien"], "hubs": b["hubs"], "dreiecke": b["dreiecke"], "tensorkeime_stark": b["tensorkeime_stark"],
       "wiederfindung_103": b["wiederfindung_103"], "einzeln": erg}
(H / "TOP100_ERGEBNIS_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in out["zusammenfassung"].items():
    print(f"{k}: {v}")
print("Familien:", [(len(v), v) for _, v in b["familien"][:5]])
print("Hubs:", b["hubs"])
print("Gesamt: OK")
