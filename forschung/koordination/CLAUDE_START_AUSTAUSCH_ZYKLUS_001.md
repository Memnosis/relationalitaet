# Zwei-KI-Forschungsverbund · Startanweisung an Claude · Zyklus KI-2026-11-03-001

**Adressat:** Claude mit Schreib-/Leseberechtigung im Git-Repository `Memnosis/relationalitaet`.  
**Gegenstelle:** ChatGPT (Website, Redaktion/Integration, Prompt-Didaktik).  
**Auftraggeber / Autor:** Nils Sautter.  
**Status:** GPT hat die Übergabe angelegt. **Claudes Empfangsbestätigung steht aus.** Kein wechselseitiger Austausch oder abgeschlossener Zyklus wird hier behauptet.

## 0. Direkt in Claude kopieren

> Du bist die **Datenbestands- und Forschungs-KI Claude** im Projekt `Memnosis/relationalitaet`. Lies zuerst diese Datei: `forschung/koordination/CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md`. Lies dann `forschung/koordination/BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md` und `forschung/tensor/LOGIK_TENSOR_2_0_GOLDSTANDARD_ARBEITSSTAND_2026-11-03.md`. Du bearbeitest ausschließlich Forschungsbestände, Quellen, Glossar, Tensorachsen, Tests, Evidenz, Promptentwicklung/-analyse und Publikationsdossiers – **nicht** die Website-Dateien in `docs/`. Beginne Zyklus `KI-2026-11-03-001`: schreibe eine explizite Empfangsbestätigung in `forschung/koordination/zyklen/KI-2026-11-03-001/CLAUDE_ANTWORT.md` mit deiner tatsächlichen Modell-/Rollenangabe, gelesenen SHA/Dateiversionen und konkreter Arbeitsplanung. Bearbeite mindestens die Aufgaben `DATA-001` bis `DATA-004` unten und dokumentiere Tests, Grenzen, neue Dateien und Commit-IDs. Ändere keine historischen Originale und veröffentliche weder unfreigegebene Architekturanweisungen noch geheime Daten. Wenn deine Arbeit fertig ist, markiere `CLAUDE_ANTWORT.md` als `ready_for_gpt_review`. Anschließend prüft GPT die Lieferung, antwortet in `GPT_ANTWORT.md`, und erst nach beiderseitiger Bestätigung gilt der Zyklus als abgeschlossen. Leite niemals aus dem bloßen Vorhandensein einer Datei eine Bestätigung oder eine wissenschaftliche Freigabe ab. Starte mit deiner schriftlichen Empfangsbestätigung.

## 1. Zuständigkeiten und Konfliktregel

| Bereich | Owner | Was ist erlaubt? |
|---|---|---|
| Originalarchiv, No-Loss, SQLite/CSV/JSON, IDs, Quellen-/Claimregister, Glossar | **Claude** | Prüfen, konservativ zusammenführen, Vorher/Nachher/Hash und Migrationsberichte |
| Fachliche Tensorachsen A/B/C, 27 Logikfelder, Logik-Literatur, Beweis-/Gegenproben | **Claude** | Facharbeit + gesonderte Konflikte an Nils |
| Fachliche Prompts, Agenten- und Meta-Verträge, Probeläufe und Fehleranalyse | **Claude** | Entwickeln und tatsächlich testen; öffentlich erst nach Freigabe |
| Website, `docs/`, CSS, JavaScript, Navigation, visuelle Darstellung, veröffentlichte Aufgabenansichten | **ChatGPT** | Nur hier, mit Regressionstests und eigenem Git-Bericht |
| Architektur-/Buchfreigabe, Urheberentscheidung, finale Veröffentlichung | **Nils** | Nach verständlichem Variantenbericht und nachweisbarer Prüfung |

**Gleichzeitige Arbeit:** Claude committet nur in `forschung/register/`, `forschung/tensor/`, `forschung/koordination/`, `forschung/skills/` und nach Absprache `forschung/prompts/`. ChatGPT committet die Website und den Koordinationsbericht. Bei Dateikonflikt keine Force-Pushes/Überschreibungen; zunächst Konfliktakte schreiben.

**Wichtige Sicherheitsregel:** Das Git-Repository ist öffentlich. Interne unveröffentlichte Buchtexte, private Ursprungsdateien, personenbezogene Informationen oder vertrauliche Originalprompts **nicht** nach `main` hochladen. Für nicht veröffentlichungsfähige Inhalte einen wirklich privaten Speicher verwenden und in Git nur freigegebene Status-/Referenzdaten führen. Ein „internal“-Feld im öffentlichen Repository ist kein Zugriffsschutz.

## 2. Aufgabenliste: erster Arbeitszyklus

### Claude / Daten-KI

| ID | Priorität | Arbeitsgegenstand | Erwarteter überprüfbarer Output | Geltung |
|---|---|---|---|---|
| DATA-001 | P0 | Historischen Logik-Tensor 1.0 und Tensor-Basics / Tensor 2.0 mit vorhandenen Git-/Archivbeständen abgleichen | Quellen-/Versionsmanifest und 27 Logikfeld-Crosswalk (Original/Neu/Hypothese), keine automatische Vereinigung | öffentlich nur nach redaktionellem Review |
| DATA-002 | P0 | A neutrale Achsen, B operative Triaden, C fachimmanente Trinitäten, G mathematischer 27er-Träger vergleichen | vier Modelltypen sauber getrennt; 2 konkrete Logikbeispiele, 1 Gegenbeispiel und Konformitätsbericht | Kernmethoden intern, freigegebener Fachauszug möglich |
| DATA-003 | P0 | Quellenstatus vierfach + `prüfung_ausstehend` als Workflow, unabhängig von wissenschaftlicher Evidenz | validierbares Schema, 5 Beispielclaims, Prüfer/Fundstelle/Datum/Lizenz/Rückgabe | geeignete offene Quellenaufgaben später öffentlich |
| DATA-004 | P0 | Logik-Tensor 2.0 als wissenschaftliche Publikation und weitere Promptaufgaben vorbereiten | Claim-/Beweislücken-Register, 6 detaillierte Fachprompts in Prompt-/Agent-/Meta-Ebenen, 1 dokumentierter Prompt-Probelauf | Entwürfe nicht automatisch veröffentlichen |
| DATA-005 | P1 | Vorhandene Mathematiktests und Versionen den Aufgaben-/Claim-IDs zuordnen | Testreferenzen mit realer Ausführungsakte; historischer Test ≠ Prompt-Test | publikationsfähig nur nach Prüfung |
| DATA-006 | P1 | Weitere unfertige Buch-/Paper-Bestände aus No-Loss inventarisieren | Titel, Originalpfad, Bestand, Rechte, Reifestufe, sinnvolle nächste Promptarbeit | noch keine neue Buchpublikation |

**Fachliche Startquelle:** `forschung/tensor/PAPER_DREIFACHE_TRINITAET_FELDTHEORIE_WEB_V0_1.md` (Website-Auszug, nicht historisches Original), ursprüngliche Logik-Tensor-1.0-PDF (Nils' Upload), `Tensor-Basics-Grundlagen(1).md`, `Tensor_2_0(1).md`, `Tensor-Feld-Theorie-Field-Theory.md` und die Archive; nur dann „vorhanden“ markieren, wenn im eigenen Arbeitsraum tatsächlich zugänglich. Die hochgeladenen Originale sind nicht automatisch aus dem öffentlichen Git-Repository abrufbar.

### ChatGPT / Website-KI

| ID | Priorität | Arbeit | Abnahme |
|---|---|---|---|
| WEB-001 | P0 | Seitensicherung und navigationsfähige Fachseiten Tensor/Logik/Feldtheorie/Algebra inventarisieren | Original-URLs und Abschnitte bleiben, Link-/Navigationsaudit |
| WEB-002 | P0 | Vorhandene Tensor-Einführung mit A/B/C/G in zwei Lesetiefen aufwerten | bestehende Inhalte nicht kürzen; Fachclaims statusklar |
| WEB-003 | P0 | Logik-Tensor/Feldtheorie aus vorhandenem Text didaktisch vertiefen | 3 historische Matrizen, 27 Felder und Originalverweise bleiben |
| WEB-004 | P1 | Prompt-/Agent-/Meta-Karten und kontextspezifische Fragen bereitstellen | öffentlich geprüfte Ausführbarkeit nicht vorab behaupten |
| WEB-005 | P1 | Gemeinsame Übergabe/Review/Abschlussberichte pro Zyklus und sichtbare Freigabestufen | keine Website-Anzeige unveröffentlichter Rohdaten |
| WEB-006 | P2 | Nach Website-Abnahme unfertige Bücher als Prompt-/Publikationsaufgaben mit Claude aufteilen | Abhängigkeiten und Buchversionen erhalten |

## 3. Verbindlicher Ablauf für jeden Austauschzyklus

1. **Auftrag**: GPT schreibt hier eindeutige Aufgaben-IDs, erwarteten Output, Quellen und Prüfkriterien.
2. **Empfang**: Claude liest wirklich, bestätigt in `CLAUDE_ANTWORT.md` mit `status: accepted`, nennt SHA/Dateien und beginnt erst dann.
3. **Ausführung**: Claude legt Ergebnisse/Diff/Tests in den eigenen Fachverzeichnissen ab; Antwortstatus `ready_for_gpt_review`.
4. **Gegenprüfung**: GPT liest Claudes Git-Dateien, prüft Test- und Nachweiskette, legt `GPT_ANTWORT.md` an; bei Problemen `changes_requested`, sonst `gpt_accepted`.
5. **Rückbestätigung**: Claude liest GPT-Antwort und bestätigt die korrekte Interpretation in seiner Antwort (`acknowledged_gpt_review`).
6. **Abschluss**: GPT schreibt `ZYKLUSBERICHT.md` mit Ergebnissen, offener Arbeit, Nils-Entscheidungen, Dateipfaden/Commits, Status und nächstem Zyklus. Erst dann `completed`.
7. **Nils-Bericht**: pro vollständigem Austauschzyklus ein verständlicher Projektbericht mit Links; wenn Nils nicht im Chat ist, ist dieser im Git abrufbar. Eine automatische ChatGPT-Nachricht ohne ausdrücklich eingerichtete Automatisierung wird **nicht** behauptet.

**Echte Automatisierung vs. KI-Autonomie:** Ein GitHub-Workflow kann Schema, Pflichtdateien, Statusfolge und Links automatisch prüfen. Er kann **nicht ohne zusätzliche autorisierte Claude-/ChatGPT-API und Berechtigung** die zwei KI-Assistenten selbstständig starten oder freigeben. Claude führt den eigenen Prompt aus; GPT liest die Antwort beim nächsten aktiven Durchgang. Für vollständig autonome Zustellung wären gesonderte GitHub-Runner- und API-Connectoren mit Geheimnisverwaltung und Nutzereinwilligung erforderlich.

## 4. Antwortformat Claude (erste Datei)

Erstelle `forschung/koordination/zyklen/KI-2026-11-03-001/CLAUDE_ANTWORT.md`:

```yaml
---
cycle_id: KI-2026-11-03-001
agent: claude
status: accepted
acknowledges: CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md
read_commit: <tatsächlich gelesener Commit>
updated_at: <UTC ISO-8601>
tasks: [DATA-001, DATA-002, DATA-003, DATA-004]
---
```

Darunter: tatsächlich gelesene Quellen, fehlende Originale, vorhandene Vorarbeiten, konkrete Planung. Nach Bearbeitung aktualisiere den Status zu `ready_for_gpt_review`, protokolliere `deliverables`, `tests`, `limitations`, `next_actions` und verlinke jeden Commit. **Keine fingierten Tests oder Bestätigungen.**

## 5. Berichtformat GPT und Nils

`GPT_ANTWORT.md`: `cycle_id`, `agent: gpt`, `status: gpt_accepted` oder `changes_requested`; geprüfte Claude-Dateien/Commits, Testbefund, Website-Folgen und Konflikte.

`ZYKLUSBERICHT.md`: nach Claude-Rückbestätigung:
- was fertig ist (mit Nachweis),
- was nur entworfen oder nicht getestet ist,
- Nils-Entscheidungen als verständliche Alternativen,
- Änderungen Website-GPT vs. Daten-Claude,
- nächste Runde und Fristen/Abhängigkeiten,
- Prompt- und Öffentlichkeitsfreigaben,
- Git-Revisionsanker.

## 6. Testlauf „Mitmachen mit zweiter KI“
Dieser Pilot modelliert einen späteren öffentlichen Mitmachprozess. Die KI Claude hat Git-Schreibzugang, fremde Leser gewöhnlich nicht. Öffentlich kann später ein Exportpaket mit Quellen, klarer Aufgabe und Rückgabeformat angeboten werden. Externe Beiträge werden vor Integration in den Datenkern geprüft. Git-Zugang ist für externe Leser **keine Voraussetzung** und darf nicht als solche dargestellt werden.

**Bestätigungsstand bei Erstellung:** GPT-Handoff: angelegt. Claude-Empfang: offen. Claude-Lieferung: offen. GPT-Gegenprüfung: offen. Claude-Rückbestätigung: offen. Abschlussbericht: offen.
