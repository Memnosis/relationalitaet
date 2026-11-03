# Einzelaudit: Mitmach-Ergebnisrückgabe

**Seite:** `docs/mitmachen-rueckgabe.html` · **Owner:** GPT · **Reife:** lokale Ergebnisvorbereitung implementiert, echter Rückkanal offen.

## Zweck und didaktische Einordnung
Eine Person ohne Schreibrechte im Git-Repository soll aus einer öffentlichen Task-ID, einer überprüfbaren Frage, Testeingaben, Ergebnissen, Quellen und negativen Befunden einen nachvollziehbaren Forschungsbeitrag erzeugen können. Das ist der erste technische Schritt der Rückgabekette, nicht deren Abschluss. Die Website erklärt Grundlagen und grenzt Datenübertragung, fachliche Abnahme und Veröffentlichung voneinander ab.

## Tatsächlich umgesetzt
- HTML-Formular auf eigenständiger, serifenloser Fachseite; 7er-Navigation, Quellen-/Mitmachlinks.
- `docs/assets/mitmachen-rueckgabe.js` erzeugt lokal ein JSON-Dokument und bietet Kopieren oder Download; keine automatische Netzwerkübertragung oder Speicherung.
- `docs/data/mitmachen-ergebnis-schema-v1.json` dokumentiert Pflichtfelder und Schutzstatus `not_submitted`, `independent_review=pending`, `publication_approved=false`.
- Öffentliche `docs/mitmachen.html` und das globale Mitmachen-Menü verlinken die Seite.
- `scripts/verify_website_browser.mjs` enthält einen synthetischen Test für Eingaben, Download und fehlende automatische Freigabe. Ein bestandener GitHub-Action-Browserlauf ist **noch nicht dokumentiert**.

## Abnahme und Gefahren
1. **P0** Tatsächliche lokale Browserausführung (Kopieren, JSON-Download, Pflichtfelder, falsche Task-ID, Datenschutztexte) mit prüfbarem Output/Commit und Regressionstest.
2. **P0** Externen Weg ohne Repo-Schreibrechte testen: `issues/new` setzt GitHub-Konto und aktivierte Issues voraus und ist eine **öffentliche** Einreichung, kein anonymer sicherer Empfänger. Kein automatischer Upload im aktuellen System.
3. **P0** Alle vorhandenen öffentlichen Aufgabenklassifikationen auf erlaubte Rohtexte/Quellen prüfen; private oder nicht genehmigte Meta-Prompts nicht in Formularvorgaben übernehmen.
4. **P1** Separates, abgesichertes Empfangsverfahren nur nach Architektur-, Moderations- und Datenschutzentscheidung; Empfangs-ID und späteres Review erst nach bestätigtem echten Eingang.
5. **P1** Negative oder erfolglose Tests als gleichwertige Forschungsbeiträge berücksichtigen; nichts nur bei Erfolg veröffentlichen.

**Endstatus:** teilweise implementiert, nicht E2E-fertig. **Crosswalk:** `M02`, `S08`, `M04` und `M07` des 72er-Arbeitsregisters. [Methodik und Simulation](../PROMPT100_SIMULATION_CROSSWALK_UND_MITMACH_RUECKGABE_2026-11-03.md).
