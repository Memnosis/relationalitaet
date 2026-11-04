# Bürger-KI · Phase 8: Gesetzeübergreifender Funktionstest

**ID:** BKI-PH8-001 · **Datum:** 5. November 2026  
**Voraussetzung:** [Paper „Gesetzeübergreifende Rekonstruktion“](./paper-buerger-ki-gesetzeuebergreifende-weisungsrekonstruktion-v0-1.md) mit verbindlicher Arbeitsregel BKI-WA-RED-001.  
**Status:** erster Testkatalog angelegt; **keine** durchgeführten Fach- oder unabhängigen KI-Vergleichstests; Gesamtfortschritt der Bürger-KI unverändert 3/10 Abnahme-Gates.

## Die nächste fachliche Phase

Die Ergebnisse der Quellen- und Weisungsrecherche werden nicht in kopierte Volltextdatenbanken verwandelt. Stattdessen entstehen **eigenständige, quellenreferenzierte Handlungsfunktionen**, die im jeweiligen Gesetzesregime geprüft werden müssen.

## Sechs Funktionsfamilien

1. **F01 Amtsermittlung:** VwVfG, SGB X und AO getrennt prüfen.
2. **F02 Anhörung:** Grundsatz und fachrechtliche Ausnahmen unterscheiden.
3. **F03 Begründung:** tatsächliche und rechtliche Gründe, Ermessen, Ausnahmen.
4. **F04 Beratung und Antrag:** allgemeine Verfahrenshilfe gegenüber SGB I unterscheiden.
5. **F05 Akteneinsicht/Informationszugang:** Beteiligtenrecht und IFG-Zugang nicht gleichsetzen.
6. **F06 Behördliche Kompetenz:** Art. 83–85 GG, Bundes-/Länder-/Kommunal-Zuweisungen.

Alle sechs Familien sind im maschinenlesbaren [Testkatalog](./data/bki-gesetzeuebergreifende-tests-v0-1.json) als `not_reviewed` registriert.

## Zwölf falsifizierbare Fälle

Der erste Katalog enthält **12 synthetische Fälle**, jeweils mit positiver erwarteter Prüffunktion und einer verbotenen Verallgemeinerung. Er eignet sich zur Vorbereitung unabhängiger Fach-Goldstandards, nicht zur sofortigen Behauptung von KI-Benchmarkwerten.

**Erster Validierungsdurchlauf:** Drei Strategien auf dieselben Fälle anwenden:
- S0: direkte Standardantwort, ohne fachrechtliche Regimeprüfung.
- S1: Einordnung nach Rechtsgebiet und Funktionsfamilie mit Quelle.
- S2: S1 plus unabhängige Ausnahme-/Kompetenz-/Belegprüfung.

### Abnahmekriterien

- 12 Aufgaben mit eingefrorenem Quellen- und Rechtsstand.
- Je Aufgabe unabhängige Begründung der Soll-Lösung einschließlich Negativfall.
- Keine Verwechslung von Funktionsanalogie und Normgleichheit.
- Keine Originaltexte in den eigenen Markdown-/Regelmodellen.
- Ergebnisse nach Aufgabe, Strategie, Normregime, Quelle und Fehlerklasse aufschlüsselbar.
- 36 erste dokumentierte Strategie-Fall-Durchläufe, anschließend unabhängige Reviews, bevor Leistungssteigerungen behauptet werden.

## Verbindliche Änderung gegenüber früheren Plänen

Der ursprüngliche Schritt „PDF zu Markdown-Volltext transkribieren“ entfällt aus der **internen Handlungsanweisungsbibliothek**. Die PDF-/HTML-Datei dient als externe Originalfundstelle und zur befristeten quellenbezogenen Prüfung. Veröffentlichte Markdown-Objekte enthalten ausschließlich eigene Rekonstruktionen, Referenzen, Datumsangaben, Hashes und Teststatus.

Der [Konverter v0.2](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/weisungsatlas_atomizer.py) und sein [Nichtkopier-Regressionstest](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/test_weisungsatlas_atomizer.py) wurden angelegt. Eine erfolgreiche automatisierte Ausführung der Tests ist bislang **nicht bestätigt**.

**Status von Phase 8:** Forschungs- und Testdesign bereit; Goldstandards, unabhängige Fachprüfung und Vergleichsläufe offen. Keine Wirkungsmessung abgeschlossen.
