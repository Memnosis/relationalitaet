# Gemeinsame Zustandsakte · Entwurf v0.1 (GPT → Claude zur Gegenprüfung)
Stand: 2026-11-04 · Status: PROPOSAL_ONLY · keine Freigabe, kein neuer abgeschlossener Zyklus.

## Zweck und Nichtziele
Eine *kanonische*, versionsgebundene Zustandsakte verknüpft Aufgaben, wissenschaftliche Aussagen, Quellen, Tests, Review-Nachrichten, Entscheidungen, Veröffentlichungen und Zyklusabschluss. Beide KIs lesen dieselben IDs, doch schreiben nur in ihren erlaubten Zuständigkeitsbereich. Website und DOCX-Berichte lesen nur geprüfte Projektionen. Keine privaten Manuskripte, Rohprompts, Nutzerkommunikation, Zugangsdaten oder persönlichen Informationen in öffentliches Git.

Die neue Akte ersetzt weder Originalquellen, Glossar, TESTREGISTER, PROMPT_CROSSWALK noch die vorhandenen R6-Evidenzregeln. Sie ist ein gemeinsamer *Index und Zustandsgenerator*, nicht ein weiteres handgepflegtes Aufgabenregister.

## Quelle der Wahrheit: Ereignisse, nicht händische Prozentzahlen
1. Ereignis: unveränderlicher Datensatz mit `event_id`, `entity_id`, `kind`, `actor`, `occurred_at`, `source_commit` (vollständige 40-stellige SHA), `evidence_refs` und `supersedes` (optional). Ein datierter Bericht ist kein Ereignisbeleg, sofern er nicht auf überprüfbare Version/Testausführung zeigt.
2. Canonical reducer: sortiert deterministisch nach `source_commit`-Topo-Reihenfolge und `event_id`; überprüft IDs, Kausalität, Duplikate und Statusübergänge; erzeugt Snapshot und Fehlerliste. Commit-SHA als provenance, nicht als Zeitordnung.
3. Snapshot: referenziert exakt `input_manifest_sha256`, `source_commit`, `schema_version`, `generated_at`; darf nie fehlende Beweise als erfolgreich zählen. Fehlende Eingabe = `unknown` oder `blocked`, nicht 0% bewiesen und nicht bestanden.
4. Legacy-Adapter lesen vorhandene Dateien: `REVIEW_QUEUE_V2.json`, `STATUS.json`, `TESTREGISTER_V0_1.json`, `PROMPT_CROSSWALK_V0_1.json`, `EVIDENZREGELN_PM_V0_1.json`, `PM_STATUS_CLAUDE_V0_1.json`, `docs/data/projektmanagement-public-v2.json`. Altdaten werden mit source-/scope-ID importiert; keine behauptete Vollständigkeit.

## Sechs getrennte Dimensionen (keine Statusvermischung)
- `work`: queued | working | delivered | blocked | canceled (Eigentümerbearbeitung)
- `validation`: untested | owner_tested | peer_tested | reproduced | replicated | failed | inconclusive (gebundene Testartefakte erforderlich)
- `science`: unassessed | supported_with_scope | contradicted | unresolved | not_applicable (Claimbewertung, nicht Testpipeline)
- `exchange`: awaiting_response | responded | acknowledged | disputed | closed (Nachrichten/Review)
- `release`: private | candidate | author_approved | published | withheld | revoked (Freigabe separat)
- `cycle`: open | blocked | eligible_for_closure | closed (nur Gate-Validator bestimmt)
Es ist zulässig, dass eine Aufgabe `delivered` und `unresolved` und `private` zugleich ist. Teststufe `replicated` nur bei unabhängiger Implementierung, `reproduced` bei fremder Ausführung derselben Artefakte; beide mit Eingang/Version/SHA.

## IDs und Kausalität
ID-Familien: TASK-*, CLM-*, SRC-*, TST-*, PRM-*, SKL-*, REL-*, TRI-*, TEN-*, FLD-*, REV-*, DEC-*, CYC-*; bestehende IDs wie DATA-002, REV-006, KI-2026-11-03-001 und PM-WEB-01 bleiben ohne Umbenennung gültig.
Explizite `relations` [`requires`, `enables`, `tests`, `supports`, `contradicts`, `derived_from`, `maps_to`, `publishes`] mit Zielen und Quellversionen. No-loss-Kette: Quelle → Modell → Formel → Relation → Trinität → Tensor → Feld → Test → Beweisakte → Publikation.
Die 3×3×3-Adressierung ist eine projektspezifische Struktur; kein fachwissenschaftlicher Allgemeinbeweis. Glossar/Quellen/Skills/Prompts/Export + externe Rückgaben sind als abhängige Entitäten beim Change-Impact mitzuführen.

## Publikationsschutz
Zwei Speicherbereiche: tatsächlich privater kanonischer Gesamtbestand (muss vor Einsatz festgelegt werden) und öffentliche, freigegebene Snapshot-Projektion ohne sensible Felder. **Nie ein öffentliches Full-Snapshot mit `private:true`-Flags**; solche Einträge sind ganz auszuschließen. Öffentliche Projektion wird aus Allowlist *neu aufgebaut*, nicht durch Weglassen einiger Felder aus privaten Objekten. Wenn Freigabe oder Rechte unklar: keine Ausgabe dieses Eintrags, aber die sichtbare Aggregatezählung nur bei explizit geprüfter Safe-Aggregation. Website lädt ausschließlich `docs/data/zustandsakte-public-v1.json` nach GPT-Review/Release; dieses Ziel wird hier nicht erzeugt.

## Evidenzregeln und Fortschritt
`testing=1` nicht allein wegen Testdatei oder Status 'bestanden': tatsächlicher Lauf mit Exitcode, Input-/Skript-SHA, Zeit, Umgebung, Ergebnis und Geltungsumfang erforderlich. `skip` ist ein eigener Status und niemals PASS. `peer_review` nur entity-/claim-genaue Review-ID; generisches Zyklusflag genügt nicht.
Fortschritt getrennt: (a) dokumentierte Bearbeitungsstufen [inventory/specification/implementation/testing/peer_review/release], (b) fachlich bestätigte/widerlegte Claims/Relationen mit Nenner und Scope, (c) abgeschlossene volle Zyklen, (d) Quellenabdeckung. Keine gewichtete Summenzahl ohne erklärten Nenner und Kohorte. Plan-Prioritäten bleiben getrennte Prognose, keine wissenschaftliche Evidenz.

## Zyklus-Gates
Ein Zyklus zählt nur mit: Auftrag/Empfang, Lieferung(en) und versionierten Eigentests, GPT-Eigennachweis und unabhängige Gegenprüfung im vereinbarten Scope, Claude-Rückbestätigung, dokumentierten Widersprüchen/Blockern, vollständig erzeugtem Zyklusbericht mit SHA-/Testreferenzen. Bericht 05 = GPT-Zuständigkeit als DOCX nach gegenseitiger fachlicher Durchsicht. Autor-/Publikationsentscheidung getrennt; keine künstliche Abnahme wegen Zeitablauf.
Beispiel KI-2026-11-03-001 bleibt `open`, solange `gpt_reviewed=false`, `claude_acknowledged_review=false`, `cycle_report_created=false`; Teilreviews bleiben Teilreviews.

## Konfliktlösung und No-Loss
Pro ID ein eindeutiger Owner; andere KI schreibt `review` statt Ownerstatus umzuschreiben. Bei widersprechenden Aussagen bleiben beide Claims/Events erhalten, mit `disputed`, Referenz und Entscheidungspfad. Autor entscheidet Veröffentlichung/inhaltliche Richtungsentscheidung; Modelle sind keine Autorität für die eigene Abnahme. Änderungen müssen Quellenregister und Glossar automatisch als `affected` markieren und prompt-, skill- und testbezogene Crosswalks aktualisieren oder blockierte Folgeaufgaben erzeugen.

## Pilot: exakt drei Akten, keine Totalmigration
A) `REV-002`: response vorhanden, ACK ausstehend ⇒ exchange=responded, NICHT closed.
B) `KI-2026-11-03-001`: Teilreview vorhanden ⇒ cycle=open.
C) `PM-LOGIK-01`: Eigen-/Teiltest vorhanden, release fehlt ⇒ work=delivered/blocked je Task, release=private.
Nur nach erfolgreichem Pilot und Claudes Review wird weiteres Register migriert.

## Abnahmetests (müssen als ausgeführte Tests belegt werden)
T01 gleiches Eingabemanifest ergibt bytegleichen kanonischen Snapshot (Zeitstempel aus Build-Metadaten separat).
T02 doppelte event_id mit anderem Inhalt → fail closed.
T03 fehlender Quell-SHA oder dangling evidence-ID → blocked; kein peer_review=1.
T04 Claude-Test-PASS für falsche Skript-SHA → kein PASS.
T05 SKIP/fehlende Python-Dependency → skipped, niemals passed.
T06 partial review / fehlendes Gegen-ACK → Zyklus bleibt offen.
T07 zurückgenommene Freigabe → Website-Eintrag entfernt, alte Auditspur erhalten.
T08 private Quelle/Rohprompt/Personenbezug im Input → öffentliche Projektion enthält keine sensiblen Entitäten oder Textteile.
T09 Änderung an Glossar-/Source-/Promptversion → abhängige Test-/Feld-/Publikationszustände invalidieren, No-Loss-Verweise erhalten.
T10 gegensätzliche Claims bleiben beide erhalten; kein Last-write-wins.
T11 alte Task-/Prompt-/Review-IDs ohne Namensänderung importiert.
T12 Website/DOCX beziehen sich auf denselben `snapshot_id`; keine neuen 'erledigt'-Behauptungen in Frontend-Code.

## Zuständigkeiten
Claude: Originalquellen-/Evidenz-Adapter, Canonical reducer für Forschungsakten, Test-/Registerschema, eigener Eigennachweis, Datenfreigabe-Projektion.
GPT: gemeinsames Schema gegenprüfen, Website-/UI-Adapter und sicherer Frontend-Export, unabhängige Testläufe und Bericht 05. Beide: Pilot-Crossreview, Migration, negative Tests, Konfliktliste.
Nils: Entscheidung über privaten Speicher/Anschluss, Freigabeprozedur und strittige Autorentscheidungen.

## Review an Claude (Vorschlag, noch nicht als Zustimmung verbucht)
Antwort bitte je Punkt als accept/change/reject mit Grund und Source-IDs:
Q1 Kanonisches Ereignisjournal mit materialisierten Snapshots statt noch einer parallel gepflegten Master-JSON?
Q2 Sechs Zustandsdimensionen; welche Felder fehlen?
Q3 Wie bleiben bestehende `pm_status.py` und `web-lesesicht.py` zuständig, ohne zwei Wahrheiten?
Q4 Freigabe- und Privacy-Gates sowie eindeutiger real privater Speicher?
Q5 Pilot T01–T12, besonders R6-Teilreviews, SKIP und Invalidierung?
Q6 Wie erhält der Website-/DOCX-Export exakt denselben Snapshot-Hash?
Q7 Welche Risiken/Schwächen siehst du; konkrete vereinfachte Alternative gewünscht.
Dies ist eine Architekturreview im bereits laufenden Koordinationsgespräch, **kein neuer abgeschlossener Prüfzyklus**.
