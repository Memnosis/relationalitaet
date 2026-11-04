---
id: PAPER-FPP-STRUCTURE-01
title: Strukturwissenschaft der Forschungsprozesse – Erkenntnis, Evidenz, Publikation
version: 0.1.0
status: research_draft_for_claude_peer_review
date: 2026-11-04
responsible_domain: Wissenschaftsmethodik / Tensoralgebra / Harvesting
not_a_release: true
underlying_protocol: forschung/koordination/FPP_01_FORSCHUNGS_PUBLIKATIONSPROTOKOLL_V0_1.md
reference_registry: forschung/koordination/FPP_01_STANDARDS_QUELLEN_GLOSSAR_V0_1.json
---
# Vom Forschungsbefund zum wissenschaftlichen Werk
## Strukturpaper über wissenschaftliche Erkenntnisproduktion, KI-Koordination und mögliche Trinitäten

### Zusammenfassung
Bei der automatischen Untersuchung von wissenschaftlichen Formelsammlungen entstehen nicht nur Formeln und Kandidaten für neue Relationen. Es entstehen zugleich Aussagen über die verwendeten Verfahren, Fehlerklassen, Belege, Interpretationen und Publikationsprozesse. Werden diese Resultate jeweils in einzelnen Papers, Chats und KI-Logs verteilt, sind sie schwer wiederzufinden und können widersprüchlich fortgeschrieben werden. Dieses Paper behandelt die Forschungsorganisation deshalb selbst als untersuchbares formales System: Objekte haben stabile IDs; Aktivitäten erzeugen Versionen, Ereignisse dokumentieren deren Herkunft; ein typisierter Abhängigkeitsgraph verbindet Algebra, Tensorakten, Fähigkeiten, Quell- und Glossarregister und redaktionell freigegebene Publikationen.

**Status:** struktureller Entwurf mit verifizierten externen Metadatenstandards, aber ohne vollständige Implementierung, formalen Beweis einer universellen 3×3×3-Struktur oder von Claude bestätigte Freigabe.

### 1. Fragestellung
Wie können Menschen und verschiedene KI-Systeme aus gemeinsam erforschten Quellen Erkenntnisse gewinnen, prüfen, korrigieren und ohne semantischen Verlust in die jeweils zuständigen wissenschaftlichen Texte überführen? Insbesondere ist zu trennen:
- **Erkenntnisgewinn:** Was ergibt sich mathematisch aus den Originalen und unter welchen Bedingungen?
- **Erkenntnisverwaltung:** Welche Akte ist kanonisch, was ist eine Ableitung, welche Version gilt?
- **Erkenntnisdarstellung:** Welches Manuskript, welche Datenansicht oder Website erklärt das Resultat?
Die Frage nach einer möglichen trinitären Struktur entsteht erst *nach* dieser funktionalen Trennung, nicht durch bloße Dreizählung.

### 2. Forschungsstand: offizielle Standards und ihre Aufgaben
Das zugehörige register `FPP_01_STANDARDS_QUELLEN_GLOSSAR_V0_1.json` enthält acht Originalstandards beziehungsweise Prinzipien mit ihren offiziellen Einstiegsadressen. Sie erfüllen unterschiedliche Aufgaben:
- **FAIR:** Forschungsdaten auffindbar, zugänglich, interoperabel und wiederverwendbar organisieren. https://www.go-fair.org/fair-principles/
- **W3C PROV-O:** Provenienzgraph `Entity ← generatedBy Activity → associatedWith Agent`; Entität/Aktivität/Akteur sind Typen von Herkunftsmetadaten, keine mathematisch bewiesene „Trinität“. https://www.w3.org/TR/prov-o/
- **RO-Crate 1.3:** Versionierte Forschungseinheiten über JSON-LD mit Daten, Software und beschreibenden Metadaten bündeln. https://w3id.org/ro/crate/1.3
- **JSON Schema 2020-12:** Formale Prüfung der technischen Datenstruktur. https://json-schema.org/draft/2020-12/
- **DataCite Metadata Schema 4.7:** Fach- und Publikationsmetadaten für zitierfähige Releases. https://schema.datacite.org/
- **CWL 1.2:** wiederholbare Kommandozeilen-Workflows, optional für wissenschaftliche End-to-End-Läufe. https://www.commonwl.org/specification/
- **SKOS:** Begriffslisten, Synonyme, Ober-/Unterbegriffe und verwandte Konzepte semantisch vernetzen. https://www.w3.org/TR/skos-reference/
- **DCAT 3:** interoperabler Katalog öffentlich zugänglicher Datensätze. https://www.w3.org/TR/vocab-dcat-3/
Diese Standards garantieren keine wissenschaftliche Wahrheit. Ein vollständiges Herkunftsdiagramm kann trotzdem eine ungültige Gleichung dokumentieren.

### 3. Forschungsobjekte und Invarianten des No-Loss-Graphen
Die primäre Menge der Objekte `O` umfasst mindestens `Quelle, Modell, Formel, Relation, Trinität, Tensor, Feld, Test, Beweisakte, Analyse, Skill, Glossarbegriff, Paper, Veröffentlichung`.
Ein gerichteter multitypisierter Graph `G=(O,E,τ)` verbindet Objekte mit typisierten Kanten wie `derivedFrom`, `supports`, `contradicts`, `usesOperator`, `mentionedIn`, `specialCaseOf`, `supersedes`.
Eine gültige Kante besitzt mindestens Herkunft, Geltungsbereich, Typ, Version, Status und – wenn als wissenschaftliche Behauptung verwendet – einen Prüfpfad.

Zentrale technische Invarianten:
1. Identität: `object_id` ist stabil, `object_version` verweist auf eine unveränderliche Fassung.
2. Keine implizite Beweistransformation: `symbolically_derived` wird nie automatisch zu `domain_accepted`.
3. Kein stilles Überschreiben: konkurrierende Ergebnisse behalten ihre Hashes, alternative Herleitungen erhalten getrennte Kanten und Evidenzbewertungen.
4. Alle notwendigen Abhängigkeiten eines veröffentlichten Manuskripts sind im Manifest mit referenzierter Objektversion auflösbar.
5. Synonymisierung bewahrt Bedeutung und Fachkontext; gleiche Zeichenfolge ist kein wissenschaftlicher Isomorphienachweis.
6. Ein nicht bewerteter oder gescheiterter Test bleibt `unknown` oder `failed`, niemals `PASS`.
7. Änderung einer relevanten Quelle zieht einen überprüfbaren Impact über Glossar, Algebra, Skills, Tensoren, Papers und Website nach, ohne die Originaltexte rückwirkend zu verändern.

### 4. Die beobachteten Dreierstrukturen – Hypothesen, nicht Beweise
**T1 (Erkenntnisherkunft):** Quelle – Methode – Resultat.
**T2 (Aussagenprüfung):** Behauptung – Prüfung – Gegenbefund.
**T3 (Darstellungsprozess):** Forschungsakte – fachliche Abnahme – publizierte Darstellung.

Diese neun Rollen sind keine neun notwendig verschiedenen Objekte: „Methode“ kann selbst eine geprüfte Forschungsakte sein; „Prüfung“ ist fachliche Abnahmetätigkeit; „Resultat“ kann eine neue Behauptung erzeugen. Eine valide Formalisierung muss die Begriffe typisieren, Rollendopplungen kennzeichnen und prüfen, ob die drei Achsen tatsächlich orthogonal und gemeinsam notwendig sind.

Ein mögliches Tensor-Adressschema `T1×T2×T3` besitzt 27 Kombinationen. Für **jede** Kombination ist zu fragen, ob eine fachlich sinnvolle Relation besteht. Eine vollständige Tensorakte ist erst denkbar, wenn mindestens die mathematische Beziehung zwischen Trinitäten formalisiert, alle Positionen fachlich untersucht und negative Fälle ausdrücklich dokumentiert sind.

### 5. Testansatz und konkurrierende Modelle
- **H0:** Zwei Rollenbeziehungen und ein generischer Herkunftsgraph reichen; die dritte Achse bietet keinen zusätzlichen Erkenntnisgewinn.
- **H1:** Drei fachlich unterschiedliche Trinitäten liefern messbare Erklärungs- oder Rekonstruktionsleistung gegenüber H0.
- **Kontrollmodell:** W3C PROV-O mit `Entity, Activity, Agent` und typisierten Provenienzkanten; das Modell selbst ist nicht 3×3×3.
- **Test 1:** Gleiche 30 heterogene Forschungsereignisse in Paargraph, PROV-O-Graph und Projekt-Tensorentwurf abbilden; verlorene Bedeutung, zusätzliche Regeln und unklassifizierbare Zustände messen.
- **Test 2:** Eine Achse entfernen und prüfen, welche Fehlerdetektion, Quellaufklärung oder Weiterleitung dadurch verloren geht (Ablation).
- **Test 3:** Gegenfälle mit widersprüchlichen Mathematikergebnissen, mehreren Rezensenten und wechselnden Publikationsfreigaben.
- **Test 4:** Die 27 Positionen einzeln mit `belegt|widerlegt|offen|nicht_anwendbar` versehen; keine leere Position als mathematische Aussage ausgeben.
Diese Experimente sind **geplant**, nicht durchgeführt. Ergebnis kann auch sein: keine robuste Trinität / kein gültiger Tensor.

### 6. Das doppelte Prozessmodell
**Forschung S0–S10:** ursprüngliche Quelle → Formel-/Analyseextraktion → fachliche Semantik → normalisierte Signatur → Muster-/Relationskandidat → formale Herleitung → Gegenprobe → unabhängige Reproduktion → Tensor-/Feldzuordnung → Fachabnahme → Release.
**Verteilung P0–P7:** Ereignis aufnehmen → Primärakte und ID erkennen → Dublette/Abweichung prüfen → Abhängigkeitsgraph auswerten → Paper-/Glossar-/Quelle-/Skill-Deltas erzeugen → fachliche Prüfung → redaktionelle Freigabe → versionierte Projektionen aktualisieren und Audit schreiben.
Ein neues Strukturpaper ist selbst ein `publication`-Objekt und bekommt einen Manifestzustand; seine Analyse ist im Analysen-/Befundregister zu erfassen, nicht ausschließlich in diesem Text.

### 7. Beispiel: Formel und Methodenanalyse
Aus `W=F s`, `P=W/t` und `v=s/t` wird unter geeigneten Definitionen `P=Fv` abgeleitet. Daraus folgen **verschiedene Forschungsobjekte**:
- `REL-...`: die algebraische Beziehung samt Domain und Gegenbeispiel.
- `METHOD-...`: der eliminierende Ableitungsalgorithmus und seine Grenzen (auch Sternformen und Nullresultate).
- `ANALYSIS-...`: beobachtete Fehler- und Ertragsstatistiken, Gegenmodelle, offene Verbesserungen.
- `IMPACT-...`: die fachlich begründeten Auswirkungen auf Algebra, Harvesting, Tensorakten, Glossar, Quellenverzeichnis und Paper.
Das Algebra-Paper erhält die fachliche Herleitung, dieses Strukturpaper nur die Meta-Erkenntnis, und eine didaktische Website darf jeweils auf beide Originale verweisen. **Keine gegenseitige Kopie ohne Kennung.**

### 8. Prozessstand und technische Grenze (04.11.2026)
Vorhanden: Formelanalyse und Elimination, Tensoralgebra-Prototyp, `tensor/1.0`-Schema, Befundregister, Reproduktionsskript, Review-Queue, öffentlicher Teilbestand historischer Tensoren und Geo-Skills sowie FPP-01-Routingvorschlag.
Nicht als fertig nachgewiesen: automatische semantische Glossar-Übernahme, deduplizierender Quellen-Nachzug, Autoren-/Rechteprüfung, komplette Impact-Verteilung an alle Manuskripte, zweite unabhängige Implementierung über gesamte Rohkorpora und mathematische Beweisführung für die vorgeschlagene 27er-Struktur.
Der vollständige Altbestand des Glossars (1.072 historische Einträge) liegt nicht als überprüftes Live-Glossar in der Website. Neue Begriffe daher **als Kandidaten mit Quell-ID aufnehmen** und erst nach Crosswalk/Review mit bestehenden Definitionen vereinigen.

### 9. Harvesting-Standardpipeline (maschinenlesbarer Plan)
1. Neue zitierte Standards oder Normen aus Forschungsakten erkennen.
2. Offizielle kanonische URL, Ausgabe/Version, Herausgeber, Status und Lizenz erfassen.
3. Quellen-Deduplizierung gegen DOI/URI/URN und historische Kennungen.
4. Begriffe aus Titel und Fachinhalt extrahieren, als SKOS-Kandidaten mit Synonymen und Bezug speichern.
5. Analyse- und Algebra-Beziehungen berechnen; mögliche Trinitäten gesondert mit Negativkontrollen testen.
6. Auswirkungen auf Primärakten, Methodenpaper, Glossar, Quellen, Codebuch, Skills und Websites ermitteln.
7. Nur freigegebene Datenauszüge ausgeben; neue Papers und fachliche Schlussfolgerungen benötigen Freigabe.
8. Rücklauf: Ereignis/Manifest aktualisieren, Validierung durchführen, offene Änderungsbedarfe zählen.

### 10. Anforderungen an nächste Entwicklungsstufe
- Stabile Forschungs-ID für dieses Paper und alle darin genannten Relationen/Tests.
- Kanonische Quelle/Glossarbegriffe statt pro-Paper-Parallelquellenlisten.
- Gemeinsames elektronisches Paper-Manifest mit enthaltenen Objekt-IDs und `last_source_commit`.
- Gezielter Impact-Compiler mit fehlertoleranter, idempotenter Entwurfs-/Prüffunktion; kein automatisches Publish.
- Mindestens ein durchgängiger Pilot: Normquelle PROV-O → Quellenkandidat → Glossarbegriff „Provenienz“ → Strukturpaper → Algebra-Hypothese → Gegenprüfung → Website-Quellenlink.
- Claude: Review „accept / change / reject / needs_evidence“ auf die Trinitäten, die Domain-Grenzen und die Integration in vorhandene Register.
- Formaler Prüfstatus: `proposed`, keine ungetestete Aussage über „selbstorganisierte“ Tensorentstehung.

### 11. Zugehörige Akten
- `forschung/koordination/FPP_01_FORSCHUNGS_PUBLIKATIONSPROTOKOLL_V0_1.md` – technische Vorgabe.
- `forschung/koordination/FPP_01_EVENT_SCHEMA_V0_1.json` – struktureller Übergabevertrag.
- `forschung/koordination/FPP_01_ROUTING_PROPOSAL_V0_1.json` – Primärorte und Paper-Manifeste, Entwurf.
- `forschung/koordination/FPP_01_STANDARDS_QUELLEN_GLOSSAR_V0_1.json` – acht offizielle Standardquellen mit Glossarkandidaten.
- `forschung/tensor/algebra-claude/typalgebra.py`, `forschung/tensor/formeln/formel_struktur.py` – ausführbare mathematische Prototypen.
- `docs/tensoralgebra.html`, `docs/harvesting.html`, `docs/glossar.html` – aktuelle öffentliche Einstiege.

**Redaktioneller Freigabevorbehalt:** Dieses Papier ist ein internes wissenschaftliches Strukturpaper im Entwurfsstand. Seine Verlinkung als „Forschungsentwurf“ ist zulässig; es ist noch kein freigegebenes Grundlagenwerk.
