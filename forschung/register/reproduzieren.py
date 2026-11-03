#!/usr/bin/env python3
"""Ein-Befehl-Reproduktion aller Claude-Prüfungen (für GPTs Gegenprüfung, R4/D06). Owner: Claude.

Aufruf (Repository-Wurzel):  python3 forschung/register/reproduzieren.py [--bericht DATEI.md]
Benötigt: Python 3.10+; optional `jsonschema` (sonst werden Schema-Teilprüfungen übersprungen und so gemeldet).
NICHT enthalten (benötigen private Dateien): Zenodo-Download/MD5 (zenodo_register.py --pruefen),
Logik-PDF-Extraktion (logik10_extrakt.py braucht die PDF), Versionsmanifest mit privatem Gesamtregister.
Für diese drei steht im Bericht, wie sie mit der öffentlichen Zenodo-PDF nachvollzogen werden können.
"""
import argparse
import datetime as dt
import hashlib
import pathlib
import platform
import subprocess
import sys

W = pathlib.Path(__file__).resolve().parents[2]
SCHRITTE = [
    ("Validator Claims (6 positiv, 7 negativ)", ["forschung/register/pruefen.py"], "Ergebnis: OK"),
    ("Logik-Aussagenregister (48)", ["forschung/register/pruefen.py", "forschung/tensor/logik-claude/LOGIK_CLAIMREGISTER_V0_1.json"], "0 ungueltig"),
    ("Standard-Profile (FAIR/PROV/SemVer/DCAT) + Negativprobe", ["forschung/register/profile/profile_pruefen.py"], "Ergebnis: OK"),
    ("Formale Tests K4 (8)", ["forschung/tensor/logik-claude/tests/test_formal_k4.py"], "OK"),
    ("Probelauf LOGIK-PROMPT-02 (8)", ["forschung/tensor/logik-claude/tests/test_logik_prompt02.py"], "OK"),
    ("Lesesicht v0.2 (5)", ["forschung/register/tests/test_lesesicht.py"], "OK"),
    ("PM-Status aus Nachweisen (5)", ["forschung/register/tests/test_pm_status.py"], "OK"),
    ("GPT-Gegenlauf LOGIK-PROMPT-02 (Kontrolle)", ["scripts/gpt_logic02_independent.py"], "PASS"),
]


def sha(p):
    return hashlib.sha256((W / p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bericht")
    a = ap.parse_args()
    commit = subprocess.run(["git", "-C", str(W), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    zeilen = [f"# Reproduktionsbericht Claude-Prüfungen", "",
              f"- Zeit: {dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()}",
              f"- Commit: `{commit}`", f"- Python: {platform.python_version()}", "",
              "| Prüfung | Skript (SHA-256, 12 Zeichen) | Exit | Erwartetes Signal gefunden |", "|---|---|---|---|"]
    alle_ok = True
    for name, cmd, signal in SCHRITTE:
        r = subprocess.run([sys.executable, "-I", *cmd], cwd=W, capture_output=True, text=True)
        text = r.stdout + r.stderr
        ok = r.returncode == 0 and signal in text
        alle_ok &= ok
        zeilen.append(f"| {name} | `{cmd[0]}` `{sha(cmd[0])[:12]}` | {r.returncode} | {'ja' if ok else 'NEIN'} |")
        print(f"{'OK    ' if ok else 'FEHLER'} {name}")
    zeilen += ["", f"**Gesamt: {'alle Prüfungen bestanden' if alle_ok else 'mindestens eine Prüfung fehlgeschlagen'}**", "",
               "## Nur mit öffentlicher Zenodo-PDF nachvollziehbar", "",
               "1. `Logik-Tensor_1_0.pdf` von https://doi.org/10.5281/zenodo.19282895 laden, MD5 laut Zenodo prüfen.",
               "2. `python3 forschung/tensor/logik-claude/werkzeuge/logik10_extrakt.py <pdf>` → erwartet `felder 27, felder_gefunden 27, axiome 5, systeme 7, begriffe_kap8 34, abgleich_2_1 27/27`.",
               "3. Sichtprüfung: Seiten 3–6 und 14–20 der PDF gegen `LOGIK_TENSOR_1_0_EXTRAKT_V0_1.md`."]
    if a.bericht:
        pathlib.Path(a.bericht).write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    print("Gesamt:", "OK" if alle_ok else "FEHLER")
    return 0 if alle_ok else 1


if __name__ == "__main__":
    sys.exit(main())
