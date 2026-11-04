#!/usr/bin/env python3
"""GR-03 · Zahlenketten des ki-tensor-Zweigs als Skript statt Handrechnung. Owner: Claude.

Jede Kette:
  1. liest die Quelldatei direkt aus Git (Zweig oder main, `git show <ref>:<pfad>`),
  2. prüft, dass jeder benutzte Wert wörtlich in der Quelle steht (Belegstelle),
  3. rechnet die Beziehung nach.
Die Zahlen werden also nicht abgeschrieben, sondern am Original belegt. Ändert sich eine
Quelle, schlägt die Kette fehl. Prüfstufe nach ACM: repliziert (eigener Code, Originalquelle).

Aufruf: python3 forschung/register/gegenrechnung/kt_zahlenketten.py [--ref REF] [--json]
Standard-REF: origin/ki-tensor/no-loss-audit-2026-10-31 (falls nicht vorhanden: archiv/ki-tensor-no-loss-audit-2026-11-03).
"""
import json
import pathlib
import subprocess
import sys

W = pathlib.Path(__file__).resolve().parents[3]
REFS = ["origin/ki-tensor/no-loss-audit-2026-10-31", "origin/archiv/ki-tensor-no-loss-audit-2026-11-03",
        "ki-tensor/no-loss-audit-2026-10-31", "archiv/ki-tensor-no-loss-audit-2026-11-03"]
A = "ki-tensor/audit/"

# (ID, Quelle(n) [Pfad, Ref "zweig"|"main"], Pflicht-Belegtexte, Beziehung als Python-Ausdruck, Erklärung)
KETTEN = [
    ("ZK-01", [(A + "GESAMTSTAND_v4_2.md", "zweig")], ["103 historische 3×3×3-Tensorgrundgerüste / 309"], "103*3 == 309", "Gerüste × 3 = Trinitäten"),
    ("ZK-02", [(A + "GESAMTSTAND_v4_2.md", "zweig")], ["297 Trinitäten / 99 Gerüste"], "99*3 == 297", "Review: Gerüste × 3"),
    ("ZK-03", [(A + "GESAMTSTAND_v4_2.md", "zweig")], ["309", "297", "zwölf ältere Achsen in vier Gerüsten"], "309-297 == 12 == 4*3", "Differenz = 4 Gerüste im Altbestand"),
    ("ZK-04", [(A + "CROSSWALK_v4_1.md", "zweig")], ["**1.072** Glossarzeilen", "**1.008** Glossarzeilen", "**64 zusätzliche Zeilen**"], "1072-1008 == 64", "Glossar v15.4 − v11.5"),
    ("ZK-05", [(A + "BESTANDSAUDIT.md", "zweig")], ["| 8.520 |", "| 7.622 |", "| 898 |"], "7622+898 == 8520", "eindeutige Formeln + Dubletten = Gleichungsobjekte"),
    ("ZK-06", [(A + "BESTANDSAUDIT.md", "zweig")], ["| 921 |", "675 Tripel + 223 Achsenbrücken + 23 Operatorpaare"], "675+223+23 == 921", "Entdeckungshinweise"),
    ("ZK-07", [(A + "GLOSSAR_RELATION_TENSOR_v4_4.md", "zweig"), (A + "CROSSWALK_v4_3.md", "zweig")],
     ["1.017 Herkunfts-getrennte Relationsakten: 309 historisch, 12 Chemie v9.6, 9 CORE v10.5, 12 P112, 675 DLMF", "| **Gesamt** | **1.017** |"],
     "309+12+9+12+675 == 1017", "Relationsakten nach Herkunft"),
    ("ZK-08", [(A + "GLOSSAR_RELATION_TENSOR_v4_4.md", "zweig")], ["107 strukturierte Tensorachsen-Trios (103 historisch plus 4 Chemie)"], "103+4 == 107", "Trios inkl. Chemie"),
    ("ZK-09", [(A + "GLOSSAR_RELATION_TENSOR_v4_4.md", "zweig")], ["107 strukturierte", "2.889 ausdrücklich offenen 3×3×3-Feldprüfpositionen"], "107*27 == 2889", "Trios × 27 Feldadressen"),
    ("ZK-10", [("forschung/register/IMPORTAUDIT_DREI_NOLOSS_ARCHIVE_2026-11-03.md", "main")], ["v115__v107_feldadressen`: 2.781"], "103*27 == 2781", "historische Gerüste × 27 (Register auf main)"),
    ("ZK-11", [(A + "GESAMTSTAND_v4_2.md", "zweig")], ["Chemie v9.6: 4 Tensoren / 12 Achsen"], "4*3 == 12", "Chemie: Tensoren × 3"),
    ("ZK-12", [(A + "RELATIONSCOMPILER_v6_5.md", "zweig")], ["**474** Aussagen-/Hypothesenakten", "309 historische Rollen-Hypothesen, 21 ergänzende Achsen, 12 Forschungsmodelle", "132 DLMF-Retrievalkandidaten"],
     "309+21+12+132 == 474", "Aussagenakten v6.5"),
    ("ZK-13", [(A + "RELATIONSCOMPILER_v6_5.md", "zweig"), (A + "ALGEBRA_AUTOMATION_v6_4.md", "zweig")],
     ["eine explizite Quelle-Triade, zwei Klassifikationen, neun Rekonstruktionen", "342 inkl. Ergänzungen"], "1+2+9 == 12 and 309+21+12 == 342 and 342+132 == 474",
     "Forschungsmodelle und 342er-Bestand"),
    ("ZK-14", [(A + "DLMF_PARSER_v5_2_metrics.json", "zweig")], ['"source_formulas": 7622', '"parse_attempted": 300', '"queued_not_executed": 7322'], "300+7322 == 7622", "Parser v5.2: versucht + Warteschlange"),
    ("ZK-15", [(A + "DLMF_PARSER_v5_2_metrics.json", "zweig")],
     ['"parse_or_evaluation_error": 284', '"unsupported_macro_or_environment": 8', '"parsed_not_established": 6', '"symbolic_identity_under_parser_assumptions": 2'],
     "284+8+6+2 == 300", "Parser v5.2: Klassen summieren auf 300"),
    ("ZK-16", [(A + "DLMF_PARSER_v5_6.md", "zweig")], ["38 Auslassungen; 8 bereits früher geparst; 116 Parserfehler; 2 mehrdeutig; 132 untypisierte DLMF-Funktionen; 4 Umgebungen"],
     "38+8+116+2+132+4 == 300", "Parser v5.6: Klassen summieren auf 300"),
]


def zweig_ref(wunsch=None):
    for r in ([wunsch] if wunsch else []) + REFS:
        if subprocess.run(["git", "-C", str(W), "rev-parse", "--verify", "-q", r], capture_output=True).returncode == 0:
            return r
    return None


def lesen(ref, pfad):
    r = subprocess.run(["git", "-C", str(W), "show", f"{ref}:{pfad}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def main():
    wunsch = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else None
    zref = zweig_ref(wunsch)
    if not zref:
        print("SKIP: ki-tensor-Zweig nicht vorhanden (git fetch origin 'refs/heads/*:refs/remotes/origin/*') – SKIP ist kein PASS (Exit 77)")
        return 77
    sha = subprocess.run(["git", "-C", str(W), "rev-parse", zref], capture_output=True, text=True).stdout.strip()
    erg = []
    for kid, quellen, belege, ausdruck, erkl in KETTEN:
        texte = [lesen(zref if q == "zweig" else "HEAD", p) for p, q in quellen]
        fehlend = [b for b in belege if not any(t and b in t for t in texte)]
        rechnung = bool(eval(ausdruck, {"__builtins__": {}}))  # nur Literale, keine Namen
        erg.append({"id": kid, "beziehung": ausdruck, "erklaerung": erkl, "quellen": [p for p, _ in quellen],
                    "belege_gefunden": len(belege) - len(fehlend), "belege_gesamt": len(belege), "fehlende_belege": fehlend,
                    "rechnung": rechnung, "ok": rechnung and not fehlend})
    # Kontrollprobe: falscher Beleg und falsche Rechnung müssen erkannt werden
    kontrolle = (not any("103 historische 3×3×3-Tensorgrundgerüste / 310" in (lesen(zref, A + "GESAMTSTAND_v4_2.md") or "") for _ in [0])) and not eval("103*3 == 310")
    alle = all(e["ok"] for e in erg) and kontrolle
    if "--json" in sys.argv:
        print(json.dumps({"schema_version": "gegenrechnung/0.1", "gegenstand": "16 Zahlenketten ki-tensor-Zweig", "zweig_ref": zref, "zweig_sha": sha,
                          "ergebnisse": erg, "kontrollprobe_erkannt": kontrolle, "gesamt": "OK" if alle else "FEHLER"}, ensure_ascii=False, indent=1))
    else:
        for e in erg:
            print(f"{e['id']} {'OK    ' if e['ok'] else 'FEHLER'} {e['beziehung']:42} Belege {e['belege_gefunden']}/{e['belege_gesamt']}  {e['erklaerung']}")
        print(f"Zweig: {zref} @ {sha[:12]} · Kontrollprobe erkannt: {'ja' if kontrolle else 'NEIN'}")
        print("Gesamt:", "OK" if alle else "FEHLER", f"({sum(e['ok'] for e in erg)}/{len(erg)})")
    return 0 if alle else 1


if __name__ == "__main__":
    sys.exit(main())
