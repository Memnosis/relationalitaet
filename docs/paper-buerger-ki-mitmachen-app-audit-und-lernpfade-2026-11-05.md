# Mitmach- und Bürger-KI-Anwendungen: Inventar, technische Prüfungen, Lernpfade
**Forschungspaper / Audit v0.1 · Stand 05.11.2026 · Nur nachgewiesene Tests als bestanden**

## 1. Inventarisierung
| Anwendung | Arbeitsfunktion | Eingang → Ausgang | Lernpfad |
|---|---|---|---|
| [Mitmachen](./mitmachen.html) | Forschungsaufgabe finden, vorbereiten | Themenkarte → Aufgaben-/Ergebnisweg | Frage → Methode → geeignete Aufgabe → Quelle → Test |
| [Mitmachen-Rückgabe](./mitmachen-rueckgabe.html) | Ergebnisakte vorbereiten | Formular → JSON / Issue-Link | Beobachtung → Quellenpinpoint → Test → Rückgabe |
| [Bürger-KI-Werkstatt](./buerger-ki-werkstatt.html) | Fragen, ausprobieren, vergleichen | Datenfrage → Strategienvergleich | Hypothese → drei Wege → Gegenprobe |
| [Feedback](./buerger-ki-feedback.html) | Quellenfehler/Ideen melden | Hinweis → GitHub-Issue / Redaktion | Fehler erkennen → Fundstelle → Korrektur |
| [Fail-Scanner](./buerger-ki-fail-scanner.html) | Verwaltungsdatensatz untersuchen | Eingabe → Befund/Export | Datensatz → Anomalie → alternative Erklärung |
| [Lernpfade](./buerger-ki-lernpfade.html) | Perspektiven- und Kontextnavigation | Anliegen → Wissenspfad | persönliches Anliegen → Fachfrage → Gegenblick |
| [Rechenschaft 100](./buerger-ki-rechenschaft-100.html) | Entscheidungsakte | Agenda → Originalakt/Ziel/Evaluation | Entscheidung → Baseline → Quelle → Messbarkeit |
| **Bürgerfragen-Vorschlagslabor (lokaler Stand)** | Zielgruppe, Ort, Fragetyp und Relation | Angaben → lokales JSON `draft_not_submitted` | Zielgruppe → Frage → Antwortformat → Biasprüfung → Einsendewunsch |

## 2. Technische Bestandsprüfung 05.11.2026
Die Dateien der sieben GitHub-Seiten und zugehörige Skripte wurden gelesen. Die Rückgabeseite hat ein Formular und eine lokale Downloadfunktion, aber keine in der gesichteten Seite ersichtliche `fetch()`-Übermittlung. Für Fail-Scanner wurden ereignisbasierte UI-Bausteine und Exportcode gefunden; kein belegter Server-Eingang. Die Werkstatt hat Client-Interaktionen und Abrufoperationen; damit ist noch keine vollständige Echtzeit-Funktionsprüfung erfolgt. Feedback führt auf ein GitHub-Issue-Formular und redaktionelle Kontakte. **Die statische Code-Prüfung ist kein Browser-End-to-End-Test**.
Das lokal erzeugte Vorschlagslabor `bki-question-proposal/0.1` wurde außerhalb der Webseite mit drei isolierten JS-Funktionstests geprüft: gültige regionale Einreichung enthält zwei Auswahloptionen und Status `draft_not_submitted`; fehlende Zielgruppe wird abgewiesen; zu wenige Optionen werden abgewiesen – **3/3 bestanden**. **Nicht getestet**: Browser-Rendering, Zugänglichkeit, tatsächliches Server-Speichern, Freigabe und öffentlicher Abruf.
Für die anderen Anwendungen: `static_inspected`, `e2e_not_run`. Keine erfundenen Testerfolge.

## 3. Technisches Design der neuen Fragen-App
Schema `bki-question-proposal/0.1`: `proposal_id`, `task_id?`, `target_group`, `population_frame`, `geography`, `locality`, `target_size_estimate`, `sample_design`, `question_text`, `response_type`, `response_options[]`, `skip_logic`, `related_question_ids[]`, `benchmark_ids[]`, `language`, `source_ids[]`, `bias_checks`, `version`, `review_status`, `submission_status`. V1-Prototyp erzeugt nur einige dieser Felder. Keine direkte Verarbeitung realer Bürgerfälle durch das Projekt als Voraussetzung.
Pfad: `Entwurf → Validierung → Vorschlagsreview → Test-Umfrage → Evidenzakte → redaktionelle Freigabe → öffentliches Lern-/Forschungsmodul`. Duplikat-, Antwortvoreinstellungs-, suggestive-Fragen- und Grundgesamtheitsprüfung vor Veröffentlichung.

## 4. Didaktische Sprachvarianten, No-Loss
| Rolle | Formulierung |
|---|---|
| Bürgerfrage | „Was möchte ich wissen – und wen betrifft es?“ |
| Forschungsfrage | „Welche Population, welches Outcome und welcher Zeitraum würden meine Vermutung prüfbar machen?“ |
| Gegenblick | „Welche andere Erklärung wäre mit denselben Daten vereinbar?“ |
| Ergebnissprache | „Wir haben beobachtet …; daraus folgt noch nicht …“ |
| Metasprache | „Welche Daten und welche Vergleichsregel müssten vorhanden sein, damit der Befund wiederverwendbar ist?“ |
Die Übergänge dürfen Fragestellung und Unsicherheit nicht verlieren: `Bürgeranliegen → Leitfrage → formale Untersuchungsfrage → messbares Outcome → Datensatz/Benchmark → Evidenz → Rückübersetzung`.

## 5. Übergreifende Crosswalk-Objekte
`app_id → skill_id → prompt_id → question_id → task_id → source_id → benchmark_id → result_id → review_id → publication_id`; jeweils Version, Provenienz, Änderungsdatum und Prüfergebnis. Fremdergebnis in Quarantäne, bevor es zur öffentlichen Evidenz wird. JSON-Schema `docs/data/mitmachen-ergebnis-schema-v1.json` bleibt Basis für die Rückgaben; keine stillschweigende Gleichsetzung von Download und Veröffentlichung.
Querverweise: [Originalsprache](./paper-buerger-ki-originalsprache-claims-didaktik-no-loss-v0-1.md), [Sprachräume](./paper-buerger-ki-sprachraeume-termini-operationalisierung-claims-v0-1.md), [Gesamtstand](./buerger-ki-gesamtstand.md), [Benchmark-Paper](./paper-benchmarks-evidenz-zeitkontext-crosswalk-2026-11-05.md).

## 6. Vor Veröffentlichung fehlende Tests
1. E2E-Browserprüfung für jede App mit positiven und negativen Eingaben.
2. Link-/Asset-Prüfung aller Navigationen, Tabs und Downloads.
3. Validierung von Daten- und Einheitenversionen; internationale Quellenlizenzen.
4. Erfolgreicher echter Eingang in freigegebenen GitHub-/Backendkanal; Empfangsbestätigung und deduplizierte ID.
5. Vergleich zweier KI-Rückübersetzungen mit dem ursprünglichen Anliegen.
6. Barrierefreiheit (Tastatur, Screenreader, Sprache) und Fehlerbehandlung.
**Status**: Bestandsaudit und technisches Konzept; keine vollständige UX-Freigabe.
