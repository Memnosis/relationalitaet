# Bürger-KI – Ergebnisakte: Zielzerlegung und alternative Prüfrouten

**ID:** BKI-ZHA-RESULT-001 · **Datum:** 2026-11-05 · **Version:** 0.1  
**Status:** Struktureller Referenzbestand und interaktive Darstellung implementiert; **keine echten KI-Läufe und keine unabhängige fachliche Validierung**.

## Ausgangsfrage

Wie entwickeln wir aus einer Frage **(a) ein überprüfbares Ziel, (b) die nötigen Teilziele, (c) unterschiedliche Handlungsmöglichkeiten, (d) fehlende Informationen und (e) Gegenprüfungen**?

Der Gegensatz zum bloßen „Antworten auf Fragen“: Der Zieleatlas fragt zuerst nach dem angestrebten Zustand und dessen Erfüllung. Er darf einen möglichen Weg weder mit einer schon bewiesenen Rechtsposition noch mit dem tatsächlichen Erfolg verwechseln.

## Implementierte Forschungsartefakte

1. [Sechs Referenzmodelle als JSON](./data/bki-zielzerlegung-pilot-v0-1.json): je ein Ziel, drei Teilziele, drei alternative Prüfrouten, ungeklärte Voraussetzungen und zwei verbotene Fehlschlüsse.
2. [Interaktives Zielpfadlabor](./buerger-ki-zielpfade.html): Auswahl der vorbereiteten Fälle und Anzeige aller fünf Analysebestandteile.
3. [Kernpaper](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/KERNPAPER_ZIEL_HANDLUNGSATLAS_LEXIKON_META_V0_1.md): theoretischer Rahmen.

**Strukturelle Zählung:** 6 Aufgaben, 18 Teilziele, 18 alternative Prüfperspektiven, 18 explizit unbekannte Angaben und 12 negative Schlussregeln. Die JSON-IDs wurden vor der Speicherung auf Eindeutigkeit geprüft; die eigentliche fachliche Richtigkeit wurde nicht unabhängig geprüft.

## Sechs Tests

| Test | Ziel | Wichtige Negativprobe |
| --- | --- | --- |
| BKI-ZHA-T01 | Bewilligte Leistung tatsächlich erhalten | Bewilligung ist nicht Erfüllung |
| BKI-ZHA-T02 | Zuständige Stelle für Meldebescheinigung finden | keine erfundene lokale Zuständigkeit |
| BKI-ZHA-T03 | Behördliche Weisung rechtlich einordnen | Weisung ist nicht automatisch Gesetz |
| BKI-ZHA-T04 | Unterstützungsmöglichkeiten für Familien erkennen | keine unbedingte Leistungszusage |
| BKI-ZHA-T05 | Jugendamt und KESB vergleichen | Institutionen trotz Funktionsähnlichkeit nicht gleichsetzen |
| BKI-ZHA-T06 | Amtsermittlung im passenden Verfahren prüfen | VwVfG nicht pauschal auf AO/SGB X übertragen |

Die drei Routen pro Fall sind **Prüfperspektiven**, nicht drei garantiert erfolgreiche reale Handlungswege. Für einen fachlich vollständigen Zielgraphen benötigen wir später Bedingungen, Übergänge, Abbruchpunkte und Wirkungskriterien auf jeder Kante.

## Prüfprogramm für die nächste Entwicklungsstufe

**S0:** Direkte Antwort ohne strukturierte Zielanalyse.  
**S1:** Lexikon und Begriffsklärung.  
**S2:** Lexikon plus explizite Ziel-/Teilzielzerlegung.  
**S3:** S2 plus Norm-, Geltungs- und Quellenprüfung.

Für jede der sechs Aufgaben wird derselbe Frage- und Quellenstand eingefroren. Unabhängig entworfene Goldstandards bewerten: Zielerkennung, richtige Teilziele, realistische Alternativen, notwendige Rückfragen, Rechtsraumtreue, Negativfallbehandlung, Quellenbelege, Aufwand und Reproduzierbarkeit. Mindestens drei Wiederholungen je Strategie sind sinnvoll; das wäre ein **geplanter** Umfang von 72 Ausführungen. Er wurde bisher nicht durchgeführt.

## Forschungsgrenzen

- Kein frei generierender KI-Zielzerleger installiert; die Oberfläche zeigt fest vorbereitete Referenzmodelle.
- Keine reale Zuständigkeitsauskunft aus kommunalen Daten.
- Keine individuellen Falldaten im Forschungsbestand.
- Keine Übernahme von Originaltexten aus Behördenweisungen in die eigenen Handlungsanweisungen.
- Ein strukturell plausibles Zielmodell kann fachlich falsch sein: unabhängige Gegenprüfung erforderlich.

## No-Loss und Fortschritt

`Alltagsfrage → Begriffssinn → Zielzustand → Teilziel → Prüfrouten → Bedingungen → Quellen → Skill → Ausführung → unabhängiger Vergleich → Ergebnis`.

Der übergeordnete Fortschritt bleibt **3 von 10 Abnahme-Gates (30 %)**, weil die neu implementierte Darstellung kein noch offenes empirisches oder juristisches Abnahme-Gate erfüllt.

**Nächste technische Priorität:** S0–S3 als tatsächlich getrennte ausführbare Strategien mit identischem Quellenbudget und nachvollziehbarem Evaluator anschließen; vor einer KI-Wirkungsbehauptung den Goldstandard unabhängig erstellen.
