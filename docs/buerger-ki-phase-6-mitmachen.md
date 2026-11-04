# Bürger-KI – Phase 6: Vernetztes Mitmachen und gemeinsamer Kompetenzaufbau

**ID:** BKI-PH6-001 · **Version:** 0.1 · **Datum:** 2026-11-04  
**Status:** Architektur- und Forschungsplan, keine gemessene Wirksamkeit  
**Bezug:** [Experimentierlabor BKI-EXP-001](./buerger-ki-experimentierlabor.md) · [bestehende Mitmachseite](./mitmachen.html)

## Grundentscheidung

Die Bürger-KI übernimmt die vorhandene Mitmach-Logik des KI-Tensor-/SOULution-Verbunds, statt ein separates Beteiligungssystem zu schaffen. Das Projekt entwickelt öffentliche, wiederverwendbare **KI-Skills**, nicht Bürgerakten oder ein Datenverarbeitungsangebot für persönliche Fälle. Beteiligungsbeiträge beziehen sich auf allgemeine Methoden, synthetische Aufgaben, fachliche Quellen und reproduzierbare Testresultate.

## Drei Beteiligungsebenen

1. **Öffentliche Bürgerfrage:** Einstieg, kleine Aufgabe ohne Programmierung, Quellen und überprüfbares Ergebnis.
2. **Agenten-/Entwicklerauftrag:** Skill implementieren, Alternativen finden, einzelne Prüfungen ausführen, Benchmark reproduzieren. Mehrere unabhängige Agenten können ein Kapitel bearbeiten.
3. **Meta-Forschung:** KI-Vergleich, Promptqualität, Skill-Komposition, No-Loss, Mini-KI, Relations-/Tensoruntersuchung, Reproduzierbarkeit.

Zusätzlich bleiben **Haupt-Prompt, Mini-Prompt (ein Satz), Master-Prompt zur Promptverbesserung** und Interoperabilitäts-Prompt getrennte didaktische bzw. technische Darstellungsformen. Öffentlich ausführbare Prompts brauchen eine geprüfte, versionierte Fassung.

## Einheitlicher Ablauf (7 Stationen)

Bürgerfrage → Fachgrundlage und Quellen → Skill-Auswahl/Harvest → Mitmach-Prompt → Vergleichstest → Ergebnisakte/Gegenprüfung → redaktionelle Freigabe und gemeinsame Skillbibliothek.

Jede Station hat einen expliziten Status `draft / source_ready / prompt_tested / technically_passed / fachlich_reviewed / approved / blocked`. Ein Konzept ist kein Testlauf; eine absolvierte Ausführung ist noch kein wissenschaftlicher Nachweis.

## Erste Mitmachprojekte

| ID | Einstieg für Bürger | Agenten-Testauftrag | Ergebnismaß |
| --- | --- | --- | --- |
| BKI-M01 | Wer ist für eine Aufgabe zuständig? | Regel- und Ausnahmeerkennung auf fiktivem Regelkorpus vergleichen | korrekt/unklar + Regelbeleg |
| BKI-M02 | Wie finde ich eine einschlägige Originalquelle? | Harvest mit direkter Recherche vergleichen | valide belegte Treffer und Fehlzitate |
| BKI-M03 | Welche Handlungsmöglichkeiten gibt es? | Einzelantwort gegen alternative Skill-Ketten | nachweisbar zulässige Optionen |
| BKI-M04 | Welche Frist oder Voraussetzung fehlt? | deterministische Prüfung mit LLM-Antwort vergleichen | korrekte Geltungsgrenzen und Rückfragen |
| BKI-M05 | Ist eine Behauptung ausreichend belegt? | unabhängige Gegenprüfer auf dieselben Belege anwenden | Fehlerklassen und Claim-Source-Treue |
| BKI-M06 | Kann man eine sachliche Frage besser formulieren? | Formulierungen auf Klarheit und unbelegte Prämissen prüfen | erfüllte Qualitätsregeln |
| BKI-M07 | Welche Skills helfen mehrfach? | dieselben Operatoren in zwei Fachgebieten testen | Transfererfolg und Gegenbeispiele |
| BKI-M08 | Welche KI-Strategie liefert das beste Ergebnis? | Vergleich S0–S4 mit gleichen Quellen/Budgets | vollständige Qualitätsmatrix |

Diese Aufgaben dürfen als **Forschungsangebote/Ideen** gezeigt werden. Sie sind noch keine als `approved` ausgewiesenen Mitmach-Prompts.

## Mitmachkarte – Datenvertrag

```json
{
  "id": "BKI-M01",
  "question": "Wer ist zuständig?",
  "level": "citizen",
  "short_task": "Prüfe die Zuständigkeit anhand eines fiktiven Regelwerks.",
  "source_ids": ["BKI-RULESET-001"],
  "skill_ids": ["BKI-01", "BKI-03", "BKI-07"],
  "test_ids": ["BKI-T01-A", "BKI-T01-B", "BKI-T01-C"],
  "agent_task_ids": ["BKI-P01"],
  "prompt_version": null,
  "prompt_execution_status": "not_tested",
  "public_release": "draft",
  "result_schema_id": "BKI-RUN-001",
  "evidence_status": "design_only"
}
```

`public_release=approved` darf ausschließlich nach Quellen- und Fachprüfung, positiven und negativen Prompt-Tests, dokumentierter Ausführung, Rückgabeformatprüfung und redaktioneller Freigabe gesetzt werden. Eine Karte kann schon früher sichtbar sein, dann aber ohne Hinweis auf geprüfte Ausführung.

## Technische Mitmachlogik

- Einheitliche Karten und Filter auf der **bestehenden** Mitmachseite; keine neue, konkurrierende Dateneingabestrecke.
- Fachlicher Einstieg mit Link auf Quellen/Glossar und vorhandene Ergebnisse.
- Nur wenn freigegeben: kopierbarer, versionierter Prompt mit Input-/Output-Vertrag.
- Reproduktion auf einer anderen KI ist ohne Git-Schreibrechte möglich.
- Öffentlich zurückgegebene Ergebnisse sind **sachliche, geprüfte Forschungsartefakte**; Rohdialoge und persönliche Fälle gehören nicht ins öffentliche Register.
- Rückgaben benötigen Task-ID, Prompt-/Modellversion, verwendete Quellen, Ergebnis, Abweichungen und Teststatus. Ein noch nicht vorhandener Rückgabekanal wird als offen ausgewiesen.
- Externe Resultate sind Kandidaten, nie automatisch als bestanden übernommen.

## Einbindung BKI-LAB-01

Die im Experimentierlabor dokumentierten Strategien S0 (Direktprompt), S1 (Skill-Kette), S2 (Parallelstrategie), S3 (separater Prüfer), S4 (Regelhybrid), S5 (neuer verdichteter Skill) bilden das methodische Prüfsystem. Als erster fairer Test eignet sich der **fiktive Zuständigkeitsbenchmark BKI-T01-A/B/C**. Das dafür notwendige Aufgaben- und Regelpaket wird in der nächsten Laborimplementierung als eigenes Artefakt versioniert.

Nach Durchführung können sowohl **positive** als auch **negative** Resultate in die Mitmachkarten zurückgeführt werden. Kein Erfolgs- oder Teststatus wird aus einem Plan abgeleitet.

## No-Loss und Forschungsverbund

`Frage → Aufgabe → Prompt → Skill → Quelle → Operator/Relation → Test → Gegenprobe → Ergebnis → ggf. Trinität/Tensor/Feld → Publikation`.

Ein gemeinsamer Crosswalk hält IDs, Provenienz, Version, Geltungsbedingungen, Negativbefunde und Freigaben. Quellenregister und Glossar sind bei relevanten Änderungen synchron mitzuziehen; Harvest-Kandidaten gehören vor der Übernahme in einen Prüfpool. Mini-KI wird als potenzieller Orchestrator untersucht, Tensoren als optionaler mathematischer Vergleichsrahmen, nicht als Pflichtmetadaten jeder Bürgerfrage.

## Nächster Prozess Phase 7: Föderierte KI-Zusammenarbeit

Untersucht werden interoperable Skill-Pakete, unabhängige KI-Implementierungen, gemeinsame Testprotokolle, reproduzierbare Prüfungen, Widerspruchsbehandlung und Qualitätsfreigaben. Geprüfte Erkenntnisse sollen übertragbar sein, **ohne dass alle Beteiligten dasselbe KI-Modell, denselben Anbieter oder zentrale persönliche Datenbestände benötigen**.

**Abnahmekriterien Phase 6:** gemeinsame Kartenspezifikation; sechs bis acht vorbereitete Forschungsaufgaben; klar getrennte Prompt-Stufen; mindestens eine tatsächlich unabhängig reproduzierte Aufgabe mit Testakte vor Behauptung operativer Funktionsfähigkeit; Rückgabe-/Freigabeprotokoll; funktionierende Einbettung in Mitmachen-Navigation. Derzeit sind die Punkte als Plan definiert, nicht vollständig abgenommen.
