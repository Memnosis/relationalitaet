# Partizipation und klare Projektgrenzen · Entwurf 2026-11-04

**Status:** Architekturvorschlag im Forschungsbranch, keine öffentliche Ausschreibung und keine neue automatisierte Schreibberechtigung.

## Vier voneinander getrennte Ansichten

1. **Historische Grundlagen** (eigene, stabile Website-Lesestrecke): Originalarbeiten, frühere KI-Papers, Forschungsgeschichte, ursprüngliche Formeln, Datensätze und unveränderte Versionsstände. Provenienz und ausdrücklich markierte, nicht bestätigte historische Aussagen.
2. **Aktuelle Forschung**: Neue Hypothesen, Experimente, Paper-Kartografie, Beweis- und Negativakten. Keine automatische Freigabe durch einen Git-Commit.
3. **Mitmachen**: Redigierte, kleine, tatsächlich erprobte Aufgaben für Leser und IT-Leute, jeweils Kontext/Kompetenzanforderung, benötigte Quellen, Zeitaufwand als optionale Angabe, Exportvertrag, Testbeispiel, Qualitätskriterien, keine Kontopflicht für reine Lesetätigkeit.
4. **Publikationen**: Nur freigegebene Ausgaben mit Version, Quellen, Urheberrecht und nachvollziehbarer Grundlage. Vorab veröffentlichte Entwürfe müssen als Entwürfe gekennzeichnet sein.

## Teilnahmepfade

**Leser/Fachinteressierte (kein Programmieren):**
- Forschungsfrage, verständliche Originalquellen und ein validierter direkter Prompt;
- Beispiel eines guten und eines fehlgeschlagenen Ergebnisses;
- Ergebnisse als strukturiertes Formular/Datei oder manuell einreichbaren Datensatz; kein öffentlicher Rohchat-Upload;
- Rückmeldung über Status (eingegangen, gesichtet, überprüft, übernommen, abgelehnt), ohne automatische Evidenzbehauptung.

**IT-Entwickler:**
- Fork/PR mit Issue-Template und maschinenlesbarem Eingabe-/Ausgabevertrag;
- Tests, Reproduktionskommando, Abhängigkeiten/Lizenzen/Threat-Model, keine Geheimnisse;
- Codeschema, Security Review, Review-Antwort und Mergefreigabe;
- Skill-Veröffentlichung nur nach Regression und Konflikttests.

**Externe KIs/Agenten:**
- Exportpaket mit freigegebener Aufgabenfassung und referenzierter Prompt-/Skillversion;
- Modell-/Harness-/Laufmetadaten, Test- und Negativresultate, datensparsame Rückgabe;
- Ergebnis wird als Kandidat aufgenommen; Review des Menschen/der unabhängigen KI getrennt.
- Rate Limits, Schutz gegen Prompt Injection und untrusted attachments.

**Zwei interne Forschungs-KIs:**
- Im bestehenden 100-Zyklen-Programm nur vollständig belegte Austauschzyklen zählen;
- Rohkommunikation in tatsächlich privatem Repository; öffentliche Freigabeprojektion ohne private Konfiguration;
- getrennte Owner für Website/Redaktion vs. Forschung/Originaldaten; gegenseitige Reviewpflicht.

## Statusautomat
draft → scoped → test_run → reviewed → approved → published
mit Seitenpfad für rejected/blocked/needs_revision. Statusänderungen speichern Quelle, Datum, Entscheider und Testanker. Leserbeiträge bleiben eigenständige Provenienzobjekte, werden nie direkt zu Beweisen hochgestuft.

## Datenverträge
Task: id, prompt_version, source_refs, skill_refs, expected_outputs, test_contract, rights, privacy_class, approved_status.
Submission: submission_id, task_id/version, submitter_pseudonym_optional, consent, timestamp, files, hashes, response, evidence_status.
Result: result_id, tested_method, baseline, checks, negative_findings, reviewer, provenance_refs, release_status.
Paper: ro-crate metadata, complete prose, dataset, script, author roles, related papers, release decision.

## Website-Upgrade
- `ki-geschichte.html` als historische Perspektive, klarer Quellen-/Gegenwartsfilter.
- `ki-systeme.html` als heutige Systemlandkarte mit verlinkten Architekturalternativen.
- `minimal-ki.html` als Implementierungs- und Vergleichslabor.
- Neue Forschungsseite für Skillverdichtung und Prompt-Analyse erst nach redaktioneller Prüfung.
- `mitmachen.html` als einzige öffentliche Aufgabendrehscheibe; getrennte Einstiegspfade Leser/IT/KI, ein gemeinsames Prüfprotokoll.
- Dashboard zeigt getrennte Zahlen für Entwürfe, ausgeführte Tests, Fachreview und freigegebene Ergebnisse.

## Migration / Rollout
P0: Rohdaten-Sichtbarkeit prüfen, niemals private Konversationen in public Git vervielfältigen.
P0: Originaldateien und Pages-Anker inventarisieren, Backups/Hash.
P1: 100-Prompt-Korpus freigegeben/anon. wählen, Annotation pilots.
P1: Kontrakte und negative Tests für drei Mitmachaufgaben liefern.
P1: prototypische Modell-/Skill-Baselines ausführen.
P2: Browser-/CI-Checks und Ergebnisannahme mit Datenschutzprüfung.
P2: fachliche Gegenprüfung, redaktionelle Freigabe, dann Navigation/Publikation.

## Evidenzgrenzen
Derzeit ist dies ein Plan. Keine öffentlichen Formulare/Einreichungs-APIs wurden implementiert und keine 100 Prompt-Benchmarks durchgeführt.
