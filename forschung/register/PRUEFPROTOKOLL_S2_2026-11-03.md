# Prüfprotokoll S2 · Versionsmanifest und Logik-Tensor-1.0-Auszug

**Zyklus:** KI-2026-11-03-001 · **Schritt:** S2 (Claude) · **Bezug:** P0-X3, DATA-001, DQ-003, DQ-004 · **Datum:** 2026-11-03
**Angekündigt in:** `CLAUDE_DISKUSSION_01.md` §5 und `CLAUDE_DISKUSSION_02_ZENODO.md` §5; GPT ohne Einwand.

## Erzeugte Dateien

| Datei | Inhalt |
|---|---|
| `forschung/register/VERSIONSMANIFEST_V0_1.json` | alle Dateien auf `main`: Bereich, Owner, Typ, Größe, SHA-256, Git-Blob, erster/letzter Commit, Commit-Zahl, Sprachschätzung; Dubletten; Namensfamilien-Kandidaten; bytegleich mit veröffentlichter Fassung (ja/nein; DOI nur für das Referenzset) |
| `forschung/register/werkzeuge/versionsmanifest.py` | erzeugt das Manifest reproduzierbar |
| `forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.{md,json}` | 27 Felder mit Adresse und Seite, 3 LM-Pfade, 5 Axiome, 7 Logiksysteme, Begriffstabelle Kapitel 8, Abgleich mit 2.1 §4 |
| `forschung/tensor/logik-claude/werkzeuge/logik10_extrakt.py` | erzeugt den Auszug, prüft vorher die SHA-256 der Quelle |

## Tatsächlich ausgeführte Tests

| Test | Ergebnis |
|---|---|
| Manifest über alle Dateien auf `main` (vollständige Historie, 323 Commits) | Dateien und Historie erfasst; Kennzahlen im Manifest unter `zaehlung` |
| Dubletten (bytegleich) | 1 Gruppe: `dashboard/data/inventar.json` = `docs/data/inventar.json` (bestätigt DQ-003) |
| Namensfamilien | 7 Kandidaten: Information Relational (2 Dateien), Chemie DE/EN, Sonnensystem DE/EN, Zeit DE/EN, Fraktale (3 PDFs), Gravitation (2 PDFs), Soziale Operatoren DE/EN |
| Bytegleich mit veröffentlichter Fassung | 4 PDFs im Hauptordner |
| Quellenprüfung Logik-PDF | SHA-256 stimmt mit Referenzset |
| 27 Felder gegen Seitentext | 27/27 gefunden |
| Gegenproben (6 Fälle: erfundene Begriffe, echte Begriffe auf falscher Seite) | 6/6 korrekt nicht gefunden |
| Abgleich mit 2.1 §4 | 27/27 identisch |
| Bericht gegen Daten | Feld- und Systemtabelle im Bericht maschinell gegen JSON geprüft: identisch |

## Befunde für die andere KI und für Nils

1. **„100 Logik-Begriffe“:** Die Tabelle in Kapitel 8 des Originals hat 34 Zeilen (7 Außenraum + 27 Feldbegriffe). Die Zahl 100 steht in GPTs Arbeitsfassungen 2.0/2.1 und im Briefing. Frage an Nils: Gibt es eine Fassung mit 100 Begriffen?
2. **Tabelle 2.1 §4:** inhaltlich identisch, aber ohne Adressen. Vorschlag an GPT: Adressspalte ergänzen.
3. **DQ-004 teilweise geklärt:**
   - `…00.pdf` bzw. `…_002.pdf` sind veröffentlichte Fassungen.
   - `relationale-gravitation.pdf` ist eine abweichende Fassung.
   - DE/EN-Paare sind als Kandidaten erkannt; ob es Übersetzung, neuere Fassung oder Auszug ist, wird je Paar noch geprüft.
4. **DQ-003 bestätigt:** Das Inventar existiert doppelt. Eine Hauptquelle festzulegen, entscheiden GPT (Website/Dashboard) und Claude gemeinsam; bis dahin keine Änderung.

## Grenzen

- Das Manifest gilt nur für `main`; Zweige und externe Archive sind nicht enthalten.
- Die Sprachschätzung beruht auf Häufigkeiten von Funktionswörtern; bei kurzen Dateien steht „unbestimmt“.
- Die Namensfamilien sind Vermutungen aus Dateinamen.
- Mehrzeilige Begriffsnamen in Kapitel 8 werden nur mit der ersten Zeile erfasst.
