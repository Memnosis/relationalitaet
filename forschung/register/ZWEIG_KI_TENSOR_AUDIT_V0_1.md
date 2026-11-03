# Prüfbericht · Zweig `ki-tensor/no-loss-audit-2026-10-31`

**Owner:** Claude (Daten-KI) · **Schritt:** S6 · **Bezug:** B5, DATA-005, Register-P0 KI-ARCH-01 · **Stand:** 2026-11-03
**Geprüfter Stand:** Zweig-Spitze `cf0bbe1` (31.10.2026, 22:52), gesichert als Archivzweig `archiv/ki-tensor-no-loss-audit-2026-11-03`.
**Art der Prüfung:** lesend und reproduzierend. Am Zweig wurde nichts verändert, nichts wurde zusammengeführt.

## E1 · Kurz erklärt

Der Zweig enthält das Prüfprotokoll einer langen Arbeitssitzung vom 31.10.: Formeln aus der DLMF-Sammlung (Digital Library of Mathematical Functions) wurden geerntet, geparst und auf Trinitäten-Kandidaten untersucht. **Er enthält Berichte und kleine Prüfprogramme, aber keine Rohdaten.** Die Berichte sind vorsichtig formuliert: Sie betonen selbst, dass Zählungen keine Beweise sind und dass bisher **0 neue Tensoren wissenschaftlich validiert** sind. Die eigenständigen Programme laufen und rechnen richtig. Inhaltlich ist der Zweig ein wertvolles, ehrliches Archiv. Er lässt sich konfliktfrei übernehmen.

## E2 · Befunde

### Umfang

| Merkmal | Wert |
|---|---|
| Eigene Commits | 48, alle am 31.10.2026 (20:16–22:52) |
| Basis | `3ec712c` (Upload vom 12.03.2026), also **nicht** der heutige `main` |
| Dateien | 48 unter `ki-tensor/`, zusammen 52.613 Bytes |
| Inhalt | `README.md`; `audit/` mit 28 Berichten (v3.9 bis v6.9) und 3 JSON-Kennzahlendateien; `pipeline/` mit 12 Python-Skripten; `codebuch/`, `daten/*`, `tests/` nur mit README (leer) |
| Überschneidung mit `main` | keine, der Ordner `ki-tensor/` existiert auf `main` nicht. Probe-Merge: konfliktfrei (KOORD-004) |
| Sensible Inhalte | keine gefunden (Suche nach Prompts, Pfaden, Zugangsdaten, Mailadressen) |

### Kennzahlen laut Zweig (`audit/kennzahlen_audit.json`, nicht nachgerechnet, Rohdaten fehlen)

8.520 DLMF-Gleichungsobjekte, davon 7.622 verschiedene Formeltexte · 1.037 Formeln mit drei annotierten Rollen · 675 verschiedene Bedeutungstripel · 6.746 Operatorschemata · 6.225 Formel–Achsen-Hypothesen · 3 Tensorhypothesen · **0 validierte neue Tensoren**.
Diese Zahlen stimmen mit den Angaben im Register auf `main` überein (`forschung/register/README.md`, `IMPORTAUDIT_*`). Die Zählstufen sind laut Zweig ausdrücklich **nicht addierbar**.

### Reproduktion der Programme

Alle Skripte liefen in einer abgetrennten Umgebung (Python 3.13, sympy 1.13.3) als unveränderte Kopie aus dem Zweig.

| Skript | Ergebnis | Bedeutung |
|---|---|---|
| `v66_verify_relations.py` | **bestanden**: 7 DLMF-Identitäten (1.2.1, 1.2.3, 1.2.4, 1.2.7, 5.5.1, 5.5.2, 5.12.1) symbolisch null; Gegenbeispiel „1.2.4 gilt nicht für n=0“ bestätigt | echte mathematische Prüfung |
| `dlmf_v54_semantic_core.py` | läuft; geometrische Reihe bei x=1 als Sonderfall (`nan`) korrekt markiert | Geltungsbereich wird beachtet |
| `dlmf_v55_regression.py` | „finite + symbolic regression examples passed“ | Regressionstest |
| `dlmf_v57_semantic_checks.py` | 2 Fälle wahr, 1 Fall (`DLMF00011`) mit Sonderfall x=1 als *nicht allgemein* erkannt | korrektes Negativergebnis |
| `dlmf_v58_typed_ast.py` | Selbsttests bestanden | Parser-Hilfsfunktion |
| `dlmf_v59_source_claims.py` | 3 exakte Identitäts- und 2 Randprüfungen bestanden; „source-domain proof remains open“ | Grenzen ehrlich benannt |
| `relationsatlas_v61_core.py` | „retrieval-only tests passed“ | Suchfunktion, kein Beweis |
| `dlmf_v56_preflight.py`, `parser_v53_core.py` | laufen ohne Ausgabe (Bibliotheksfunktionen) | — |
| `dlmf_lark_verifier.py` | **braucht eine CSV-Eingabe** (nicht im Repo) | nicht reproduzierbar ohne Rohdaten |
| `ki_tensor_v64_inventory_check.py` | **braucht `codebuch_v64.sqlite`** (nicht im Repo) | nicht reproduzierbar ohne Rohdaten |
| `consolidate.py` | nicht ausgeführt; braucht ZIP-Archive und zwei SQLite-Dateien | — |

**Unabhängige Gegenprüfung durch Claude:** Die 7 Identitäten aus `v66` wurden zusätzlich **numerisch** mit mpmath geprüft (30 Stellen, Zufallswerte, Seed 7). Alle stimmen, auch das Gegenbeispiel n=0. Damit hängt das Ergebnis nicht nur an sympys Vereinfachung.

### Bewertung

1. **Wissenschaftlich:** Geprüft sind bekannte Identitäten aus der DLMF, also Lehrbuchmathematik. Das zeigt, dass Werkzeuge und Geltungsbereiche funktionieren. Es ist **kein** Beleg für Trinitäten- oder Tensoraussagen; der Zweig sagt das selbst.
2. **Lücken:** Die Rohdaten (DLMF-Ernte, SQLite-Codebücher, CSV) fehlen. Die Ordner `daten/`, `codebuch/` und `tests/` sind leer. Die „lokal vorliegenden Buildskripte“ wurden laut `pipeline/README.md` nie übertragen. Diese Dateien gehören zu den angefragten privaten Archiven (F5).
3. **Datenqualität:** Die Kennzahlen sind mit dem Register auf `main` konsistent; die Zähllogik wurde bereits im Zweig selbst korrigiert („551 Formeln“ waren 550 verschiedene Texte).

## Empfehlung

- **Übernahme nach `main`:** technisch unbedenklich (nur neuer Ordner, keine sensiblen Inhalte, konfliktfrei). Ob der Ordner öffentlich auf `main` stehen soll, entscheidet Nils (neu im Entscheidungsblatt: DEC-KT-01). Claude empfiehlt die Übernahme, weil die Berichte genau die geforderte Ehrlichkeit über Zählstufen und Beweisgrenzen zeigen.
- **Testregister:** Die 7 bestätigten Identitäten werden als Testreferenzen `TST-KT-V66-*` in das Testregister (DATA-005) übernommen, mit Verweis auf Zweig-Commit `cf0bbe1`.
- **Nach Eingang der Archive (F5):** die 2 datenabhängigen Skripte und `consolidate.py` reproduzieren.

## E3 · Reproduktion

```
git archive origin/ki-tensor/no-loss-audit-2026-10-31 ki-tensor | tar -x -C <tmp>
python3 -m venv <tmp>/venv && <tmp>/venv/bin/pip install sympy==1.13.3 antlr4-python3-runtime==4.11.1 lark==1.2.2
cd <tmp>/ki-tensor/pipeline && <tmp>/venv/bin/python v66_verify_relations.py
```
