---
cycle_id: KI-2026-11-03-001
agent: gpt
document: thesis_evidence_page_audit_and_lost_tasks_handoff
status: awaits_claude_independent_data_review
updated_at: 2026-11-03
---
# GPT → Claude: Thesen, Evidenzgrade, 25 Seitenpläne, 100+-Promptlücke und Eigennachweise (P0)

**Neue Anweisung von Nils:** eine Seite und thematisch verteilte Karten/Rahmen/Icons für Thesen mit Evidenzgraden; zunächst Thesenabdeckung analysieren. Im Projektmanagement verifiziert **jede KI zunächst die eigenen Aufgaben**, danach gegenseitiger Review. Für jede Website-Seite eine eigene Git-Analyse mit Plan, historischer 100+-Originalprompt-Abdeckung, Planänderungen und Suche nach verlorenen/halbfertigen Jobs.

## GPT tatsächlich erledigt (Git-Dateien, nicht gleich Endabnahme)

1. [Daten `docs/data/thesen-uebersicht-v1.json`](../../../../docs/data/thesen-uebersicht-v1.json): sechs **thematische**, nicht kanonisch historisch identifizierte Forschungsfamilien; Stufen E0–E4 als **projektspezifische** Evidenz-/Nachweisklassen. Fachbehauptungen zunächst konservativ auf E1, selbst wenn einzelne Standardbeispiele formal gültig sind. `original_thesis_id=null`, `claude.review.status=pending`.
2. `docs/assets/thesen-evidenz.js` und `.css` sowie `docs/thesen.html` und die sechs fachlichen Abschnitte auf `tensor-einfuehrung.html`, `tensor-paper.html`, `tensoralgebra.html`, `minimal-ki.html`, `vernetzung-ki.html`, `geoki.html`. SVG-Icons aus vorhandenem Forschungs-Sprite, Fachtiefe per `details`, kein anderes Navigationstool. Alte Seiteninhalte wurden beim Einfügen rücksubstituiert und erhalten.
3. [25 individuelle Seitenaudits](../../../website/seiten/README.md) – pro Seite E1/E2/E3, Wissenslücke, konkreter Plan, getrennte eigene Abnahme und unabhängiger Review; zuvor nur Gesamtaudit vorhanden.
4. [Plan-/Verlustprüfung](../../../website/PLAN_UPDATE_PROMPT100_UND_LUECKENAUDIT_2026-11-03.md) – 16 identifizierte offene/teilfertige Jobs GAP-001…GAP-016. **Keine** Behauptung, genau die letzten 100 Originalnachrichten gelesen zu haben; 44 Aufgabenfamilien/106 ältere Aufgaben/13 kuratierte neue Taskfamilien sind ausdrücklich unterschiedliche Inventare und Stände.
5. `docs/data/projektmanagement-v1.json` jetzt mit `owner_verification` pro Task: GPT und Claude eigenständig, Cross-Review und End-to-End-Abnahme **nicht automatisch aus Artefakten abgeleitet**. Anzeige unter `docs/assets/projektmanagement.js` aktualisiert; [PM-Seite](../../../../docs/projektmanagement.html) verlinkt 25 Seitenaudits und 16 GAPs.
6. Statisch mit V8 geprüft: JavaScript-Syntax von beiden neuen Dashboards gültig; JSON-Struktur/Parsing der sechs Thesen und 13 Tasks gültig. **Browser-Lauf, fachliche Validierung und Deployment noch nicht belegt.**

## Claude P0: eigene Aufgaben und originales Thesen-/Claimregister prüfen

**DAT-A1 · OriginaIthesen finden:** Bisheriges historisches Register nach originärem Wortlaut, These-ID, Archiv-/Publikationsversion, Fachdomäne, Originalquelle (exakte Fundstelle), Gegenhypothese, Test/Negativtest und Evidenzstatus erschließen. Sechs Themen auf `docs/thesen.html` sind **keine** sechs bewiesenen historischen Thesen und keine Vollzählung; exakte Über-/Unterdeckung mit Original-IDs vorlegen. Kennzeichne, welche historische Aussage nicht zu den sechs Themen passt, statt sie zwangsweise einzupassen. Kein automatisches `E3` oder `E4`.

**DAT-A2 · Evidenzgrade begutachten:** Unterscheide (a) Zugänglichkeit/Quellenprüfung, (b) fachlicher Evidenzstatus, (c) mathematische vs. empirische Beweise, (d) tatsächlich ausgeführter Software-/Prompt-Test und (e) redaktionelle Publikationsfreigabe. Prüfe die vorgeschlagenen E0–E4 gegen unsere wissenschaftlichen Evidenzakten (z.B. historische E0–E5) und liefere einen dokumentierten Crosswalk oder alternative Levels mit den entsprechenden **Geltungsbereichen**, keine stillschweigende Gleichsetzung.

**DAT-A3 · Eigentest, dann Cross-Review:** Deine Daten-/Forschungstasks unabhängig nach realem Input, tatsächlicher Ausführung, Validator/Gegenprobe und Ergebnis/Commit beurteilen. `owner_verification` darf nicht als GPT-Abnahme deiner Arbeit gelesen werden. GPT macht seinerseits Browser-/Web-Eigentests. Nach beiden Eigentests prüft jeweils die andere KI den konkreten Daten- oder Website-SHA. Abweichungen und fehlende Abnahme dokumentieren, keine erledigte Aufgabe nur aus einem Markdownplan.

**DAT-A4 · 100+ und 16 Jobs:** Prüfe die 16 GAPs gegen alte Daten-/Websitepläne und deine verfügbaren historischen Quellarchive; kennzeichne `belegt_abgeschlossen`, `halb_implementiert`, `nur_geplant`, `source_not_accessible`, `veraltet_durch_neueren_Auftrag`, `wirklich_verloren_nachgewiesen`. Das letzte Label nur vergeben, wenn konkret ursprüngliches Material nachweislich nicht rekonstruierbar ist. Die **Originalsequenz der letzten 100 Nutzerprompts** ist im aktuellen Git nicht vollständig belegt; keine aus 44 Familien erfundene 100er-Liste. Ein tatsächlicher Chat-Export wird benötigt, falls Claude diesen nicht über die erlaubten Quellen abrufen kann.

**DAT-A5 · Neueres Autorenrecht im Plan:** Die gemeinsame Entscheidungsdatei `forschung/koordination/ENTSCHEIDUNGEN_NILS_2026-11-03.md` führt bereits **7-Punkte-Menü Variante b**, Inkubator **fusionieren und differenzieren** sowie Berichte an Nils als **DOCX**. Diese neueren Vorgaben ersetzen alte unentschiedene Planstellen. Der ältere Website-Plan enthält auch „Serifenelemente“; die spätere Anweisung lautet **keine Serifenschrift**, bitte in Crosswalks sichtbar korrigieren.

## Claude-Lieferformat / Dialog
- `CLAUDE_THESEN_ORIGINAL_CROSSWALK_01.md` (+ kleine geprüfte JSON-Projektion nach Freigabe): Originalthese→Themenkarte→Quelle→Test→Evidenzstatus, inklusive nicht zuordenbarer Originale.
- `CLAUDE_EVIDENZGRADE_REVIEW_01.md`: E0–E4 und historische E0–E5 sowie Beleg-/Zugangsstatus sauber typisiert.
- `CLAUDE_TASK_EIGENABNAHME_UND_100_PROMPT_GAPS_01.md`: eigene Aufgaben mit tatsächlichen Testakten, 16 Lücken-Gegenprüfung und Aktualisierung deiner Prioritäten.
- Eine Gegenprüfung an der **neuesten** GPT-Websitefassung (nicht an den alten 21 Seiten-SHAs), mit korrigierbaren P0-Befunden. Bitte erst deine Eigenprüfung abgeben und dann GPT-Ergebnisse gegentesten.

Bitte deine Antwort im [gemeinsamen Issue #3](https://github.com/Memnosis/relationalitaet/issues/3) mit Datei-/Commitlinks bestätigen. GPT prüft daraufhin deine tatsächlichen Quell-/Testakten und dokumentiert Änderungen am eigenen Plan. Ein Zyklusabschluss wird **erst nach reziproker Endbestätigung** und Bericht behauptet.

## Sicherheitsgrenzen und langfristige Lernregeln
Das interne Vollregister aller Zenodo-Werke, unveröffentlichte Originalbücher und 38 noch unfreigegebene Meta-Prompts dürfen nicht erneut über die öffentliche Git-Lesesicht verbreitet werden. Frühere versehentliche Publikation bleibt in der Git-Historie zu prüfen. Erst nach privater Sicherung und Autorfreigabe reduzierte Webdaten an GPT liefern. Die drei KI-Berichtanalysen folgen nach Zyklen 3,6,9, eventuelle Erweiterung auf 12 nach Nils-Entscheidung; pro vollem Zyklus ein Bericht.
