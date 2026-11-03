# Seitenanalyse: Geo-KI

**Website-Datei:** [`docs/geoki.html`](../../../docs/geoki.html) · **Priorität:** P0 · **Analyse:** GPT, Stand 03.11.2026 · **Unabhängiger Fachreview:** Claude ausstehend bzw. nur ältere Revisionen geprüft.

## Tatsächlich vorhandener Stand
Generator, Formfamilien, Werkzeugvergleich und neue Evidenzkarte. Dieser Befund beruht auf dem in Git abgerufenen Seitentext und vorhandenen Änderungsberichten; kein kompletter Browser-/Lesertest ist damit bestätigt.

## Zentraler offener Befund
Operatoren aus GEOS/SymPy/CGAL/CAD sind noch nicht tatsächlich gegen identische Eingaben gegentesten worden.

## Didaktik/Evidenz
- **E1 Grundlagen:** Zu Beginn notwendigen Begriff und Nutzen ohne Vorwissen erklären.
- **E2 Ausdifferenzierung:** Varianten, historische Entwicklung, andere Methoden, Geltungsbereich und Alternativen sichtbar machen.
- **E3 Fachwissen:** Originalquelle, exakte Fundstelle, Tests, Gegentests, Status und Grenzen getrennt zeigen.
- Die neue Thesenkarte ist eine **thematische Zuordnung**, keine rekonstruierten Original-These-ID und kein Beweis der Projekthypothese.
- Fachliche Korrektheit und Quellen: Claude; Text, Navigation, Icons, Seitenintegration: GPT; echte Freigabe: Nils.

## Umsetzungsfolge und Abnahme
1. **P0 Bestandsabgleich:** aktuelle Git-Datei/Anker/Originalgrafiken/Links mit SHA sichern, keine Bestandsteile verlieren.
2. **Fachliche und redaktionelle Ergänzung:** Zwei Operatorfamilien auswählen; Format-Roundtrip mit Fehlergrenzen messen; Ergebnisse mit GIS-/Quellenbelegen in Karten zeigen.
3. **Eigennachweis GPT:** Textdiff, Link-/Assetprüfung, Desktop-/JS-Test und tatsächlichen Commit an Aufgabe binden.
4. **Peerreview Claude:** fachliche Quellen, Gegenbeispiele, Didaktik und Evidenz prüfen; nur nach tatsächlicher Rückantwort weiterfreigeben.

**Verknüpfte Aufgabenfamilien:** PM-GEO-01. **Offene Belege:** vollständiger Einzelprompt-Crosswalk für letzte 100+ Originalnachrichten; siehe [Gesamt-Upgrade-/Abdeckungsprüfung](../PLAN_UPDATE_PROMPT100_UND_LUECKENAUDIT_2026-11-03.md). Eine allgemeine Themenfamilie ist kein belegter einzelner Originalprompt.

**Änderungslog:** [Gesamtseiten-Audit](../SEITENAUDIT_GESAMT_LERNWEGE_THESEN_GEOKI_2026-11-03.md) · [Website-Changelog](../CHANGELOG_PM_KI_HISTORY_GEO_THESES_2026-11-03.md). **Reife:** umgesetzt/teilweise erklärt, Endabnahme ausstehend.

## R5 · Funktionaler Nullindex-Fehler und reproduzierbarer Test (03.11.2026)

**Tatsächlich korrigiert:** Das dynamische 27er-SVG nutzte für die Auswahl zunächst die Rohschleifen-Indizes `T0.E0.R0`; Anzeige und Standardposition verwenden nach `ba72a10`/`04a3962` nun die gültige **einsbasierte** Konvention `T1.E1.R1` bis `T3.E3.R3`. Ein für Website-Leser nutzloser interner Redaktionshinweis wurde durch die sachliche Grenze von Struktur zu Beweis ersetzt.

**Abnahmespezifikation:** `scripts/verify_website_browser.mjs` klickt unter Chromium `#matrix rect:first`, prüft 27 auswählbare Positionen und `T1.E1.R1`. **Erwarteter Test vorhanden, tatsächlich bestandener Browser-/CI-Lauf noch offen.** Die fachliche Interpretation aller Positionen bleibt separat bei Claude.
