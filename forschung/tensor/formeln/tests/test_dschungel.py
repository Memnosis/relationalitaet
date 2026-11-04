#!/usr/bin/env python3
"""Tests für dschungel.py an einem synthetischen Bestand mit bekannter Bezugsstruktur. Nur Standardbibliothek."""
import json
import pathlib
import subprocess
import sys
import tempfile

H = pathlib.Path(__file__).resolve().parents[1]
FEHLER = []


def pruefe(name, bed):
    print(("ok   " if bed else "FEHL ") + name)
    if not bed:
        FEHLER.append(name)


def f(i, ex, typ_tex="x=y"):
    return {"id": i, "name_de": i, "name_en": None, "formel_tex": typ_tex, "formeln_tex": [typ_tex], "symbole": [],
            "groessen": [k[2:] for k in ex], "konstanten": [], "stelligkeit": len(ex), "trinitaer": len(ex) == 3,
            "parse": "ok", "ausdruck": "Eq(x, y)", "exponenten": {k: str(v) for k, v in ex.items()}, "skelett": None}


# Bezugsraum: Operatoren m (Masse), n (Stoffmenge); Schließung M = m/n (molare Masse)
# Zeilen: Energie E, Entropie S, Wärmekapazität C: e = E/m, E_n = E/n; zwei Zeilen vollständig, eine mit Lücke
F = [f("SM", {"G_QM": 1, "G_Qm": -1, "G_Qn": 1})]                          # M·n/m = 1
for X in ("E", "S", "C"):
    F.append(f(f"Qs{X}", {f"G_Qs{X}": 1, f"G_Q{X}": -1, "G_Qm": 1}))         # s = X/m
    F.append(f(f"Qn{X}", {f"G_Qn{X}": 1, f"G_Q{X}": -1, "G_Qn": 1}))         # x_n = X/n
for X in ("E", "S"):
    F.append(f(f"v{X}", {f"G_Qn{X}": 1, f"G_Qs{X}": -1, "G_QM": -1}))       # x_n = M·s (vorhanden)
# Störformeln ohne Struktur
F += [f("R1", {"G_Qa": 1, "G_Qb": 1, "G_Qc": -1}), f("R2", {"G_Qd": 2, "G_Qb": -1, "G_Qe": 1}),
      {**f("A1", {}), "groessen": ["u", "v", "w"], "stelligkeit": 3, "trinitaer": True, "exponenten": None, "ausdruck": "Eq(G_Qu, G_Qv + G_Qw)"}]
G = {"groessen": {"Q" + q: {"de": q, "en": None, "dimension": None, "konstante": False, "vorkommen": 1}
                  for q in ["M", "m", "n", "E", "S", "C", "sE", "sS", "sC", "nE", "nS", "nC", "a", "b", "c", "d", "e", "u", "v", "w"]},
     "quelle": "synthetisch", "abgerufen_am": "-"}
with tempfile.TemporaryDirectory() as t:
    t = pathlib.Path(t)
    (t / "formelbestand_v0_1.jsonl").write_text("\n".join(json.dumps(x) for x in F) + "\n")
    (t / "groessen_v0_1.json").write_text(json.dumps(G))
    r = subprocess.run([sys.executable, str(H / "dschungel.py"), "--datensatz", str(t), "--permutationen", "20"],
                       capture_output=True, text=True)
    pruefe("Lauf ohne Fehler", r.returncode == 0 and "Gesamt: OK" in r.stdout)
    erg = json.loads((t / "DSCHUNGEL_ERGEBNIS_V0_1.json").read_text())["zusammenfassung"]
    bt = json.loads((t / "bezugstensoren_v0_1.json").read_text())
    pruefe("additive Trinität erkannt", erg["trinitaetstypen"].get("additiv") == 1)
    pruefe("Signatur 1:1:2 erkannt", "1:1:2" in erg["signaturen_multiplikativ"])
    haupt = [x for x in bt if x["schliessung_formel"] == "SM"]
    pruefe("Bezugstensor über Schließung M = m/n gefunden", len(haupt) == 1)
    if haupt:
        pruefe("drei Zeilen (E, S, C)", haupt[0]["anzahl_zeilen"] == 3)
        pruefe("zwei Zeilen vollständig", haupt[0]["zeilen_vollstaendig"] == 2)
    erg_csv = (t / "ergaenzungen_v0_1.csv").read_text()
    pruefe("Ergänzung sC → nC über M vorhergesagt (parallel)", ("sC,nC,M," in erg_csv or "nC,sC,M," in erg_csv) and ",parallel," in erg_csv)
    pruefe("keine Ergänzung aus Störformeln", "a," not in erg_csv.split("\n", 1)[1])
# Veröffentlichter Datensatz: jede Vorhersage hat ein fachliches Urteil
import csv  # noqa: E402
D = H / "datensatz"
if (D / "ergaenzungen_v0_1.csv").exists():
    erg = {(r["von"], r["nach"], r["ueber"]) for r in csv.DictReader((D / "ergaenzungen_v0_1.csv").open(encoding="utf-8"))}
    rp = {(r["von"], r["nach"], r["ueber"]) for r in csv.DictReader((D / "rollenpruefung_v0_1.csv").open(encoding="utf-8"))}
    pruefe("Rollenprüfung deckt alle Vorhersagen des Datensatzes ab", erg == rp)
print("OK" if not FEHLER else f"FEHLER: {FEHLER}")
sys.exit(1 if FEHLER else 0)
