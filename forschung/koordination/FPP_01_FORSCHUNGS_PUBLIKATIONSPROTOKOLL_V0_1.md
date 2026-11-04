# Forschungs- und Publikationsprotokoll FPP-01 · Vorschlagsfassung v0.1
**KI-Tensor / SOULution · 2026-11-04 · zur Kritik und gemeinsamen Freigabe durch Claude, GPT und Redaktion**

## 0. Entscheidung und Geltung
**Leitsatz:** Wissenschaftliche Erkenntnisse werden **einmal identifiziert**, über ein standardisiertes **Ereignis- und Provenienzmodell** geprüft und anschließend in allen zuständigen Ansichten **abgeleitet** angezeigt. Niemand kopiert ungeprüfte Erkenntnisse eigenmächtig in ein Paper. Auch Analysen, Negativbefunde, Alternativen und interne Gegenargumente besitzen dauerhafte Akten und einen verantwortlichen Primärort.

Dies ist ein **Vorschlag**, kein bereits operational implementierter Standard. Er ergänzt bestehende `tensor/1.0`, Claude-Reproduktionsskripte, `REVIEW_QUEUE_V2.json`, `KI-2026-11-03-001`, No-Loss-Graph, Quellen-/Glossar-Synchronisation und die öffentlichen v10.7-Datenprojektionen. Keine historisch vorhandenen IDs ersetzen oder umnummerieren.

## 1. Normen und methodische Grundlage
- **FAIR**: stabile IDs, reichhaltige maschinenlesbare Metadaten, qualifizierte Referenzen, Lizenzen und Provenienz; ausdrücklich auch begrenzt zugängliche Originale.
- **W3C PROV-O**: Entitäten (Quelle, Formel, Befund), Aktivitäten (Import, Parsing, Ableitung, Review), Akteure (Claude/GPT/Mensch/Tool) sowie `used`, `wasGeneratedBy`, `wasDerivedFrom`, `wasAssociatedWith`; Ereignisse sind keine Beweismethode.
- **RO-Crate 1.3 / Workflow Run RO-Crate**: Forschungseinheit mit Input, Artefakten, Code, Softwareversionen, Lauf, Ergebnis, Lizenz und Zitierinformation bündeln; JSON-LD-Verpackung erst bei freigegebenen Austauschexporten.
- **JSON Schema 2020-12**: strukturelle Pflichtfelder für einzelne Übergaben; fachliche Richtigkeit erfordert zusätzliche Tests und Review.
- **DataCite Metadata Schema 4.7**: DOI/Zitierdatensatz für stabile Releases; ein Git-Commit oder eine interne ID ersetzt keinen DOI.
- **CWL 1.2** oder klar versionierte Python-/Make-Workflows: maschinell reproduzierbare Teilstrecken, mit exakten Eingabe-/Ausgabedateien, Kommando, Abhängigkeiten, Checksums.
- **CodeMeta, CITATION.cff, SPDX, SemVer** als optionale, passende Metadaten ergänzen; nicht den Kern davon abhängig machen. Lizenz und Zugriff getrennt verwalten.
- **OpenMath / MathML / LaTeX, QUDT/UCUM/Einheitenlexikon** als mögliche Fach-Crosswalks; Symbolik und Rollen müssen explizit semantisch gemappt werden. Ein String-Match ist kein Nachweis mathematischer Gleichheit.
- **Forschungsmethode:** Hypothese → Operationalisierung → Test → Gegenprobe → unabhängige Reproduktion → Einordnung → redaktionelle Freigabe, mit negativen Übergängen.

## 2. Drei Ebenen: Forschungsobjekt, Verarbeitung, Veröffentlichung
1. **Wissenschaftliches Objekt**: eine Formel, Definition, typisierte Relation, Trinität, Tensor, Modellbrücke, These, Gegenbeispiel oder Befund mit stabiler `object_id` und **eigener Primärakte**.
2. **Verarbeitungsereignis**: Import, semantische Zuordnung, algorithmische Ableitung, Review oder redaktionelle Entscheidung; unveränderlicher Eintrag mit Eingabe-/Ausgabe-Hashes, Akteur, Code/Version und Zeit. Ein Ereignis erzeugt eine Objektversion oder einen verknüpften Befund, überschreibt nie still das Original.
3. **Ansicht / Produkt**: Algebra-Codebuch, Methodenpapier, Tensorgrundlagenwerk, Glossar, Harvesting-Seite, öffentliche Datenbank, Dashboard. Diese sind eine **generierte oder redaktionell freigegebene Projektion** des Objektgraphen, kein zweiter Primärdatenbestand.

## 3. Autoranleitung: feste Primärorte für jede neue Erkenntnis
Die Tabelle ist als **Routingregel**, nicht als neuer Ordnerbaum auf Verdacht zu verstehen. Vor Anlegen prüfen, ob die unten genannte Primärakte bereits existiert.

| Erkenntnistyp | Primärort / zuständiges Register | Verpflichtend zu aktualisierende Ansichten |
|---|---|---|
| Rohquelle / Original / Bestand | gemeinsames Quellenregister + unveränderliches Archivmanifest | Quellennachweise, Bestandsindex |
| Formel, Parsingergebnis, mathematische Struktur | `forschung/tensor/formeln/` und Formelregister | Algebra-Methodenpaper, Harvesting, Glossar |
| Neue algebraische Operation / Relationsfamilie / formale Regel | `forschung/tensor/algebra-claude/` + versioniertes Algebra-Codebuch | Tensoralgebra-Paper, Tests, Skillregister, Tensorakten, öffentliche Algebra-Übersicht |
| Belegte oder widerlegte mathematische Beziehung | Relations-/Befundregister mit Beweis- und Gegenakte | Algebra, betreffende Trinitäten/Tensoren, Thesen, Glossar, Quellen, ggf. weitere Papers |
| Trinität / Drei-Trinitäten-Verbund / 27er-Feld | tensor/1.0-Akte und bestehender ID-Crosswalk | Tensorgrundlagenwerk, Tensorbibliothek, Harvesting, Glossar, Codebuch |
| Skill / Operator / API / Reproduktionslauf | gemeinsame Skillbibliothek + Tests und Codeversion | Mini-KI, Geo-KI, Algebra, visuelle Engine, Forschungsdaten |
| Erkenntnistheoretische/semantische Kritik | Thesen-/Analysenregister mit Originalquelle und Konflikt-ID | KI-Forschung, Methodenkapitel, Glossar, ggf. eigener Quellen-/Kritikpaper |
| Gesellschaftspolitische Anwendung | SOULution-Forschungsakte mit konkretem Fall/Beleg | zuständiges SOULution-Paper und Portal |
| Website/UX-Gegenbefund | `forschung/website/` und Regressionstest | betroffene HTML-Seiten nach Review |
| KI-Kommunikation und Beschlüsse | bestehender Zyklus / Review-Queue / Austauschakte | alle durch Beschluss betroffenen Artefakte via Impact-Compiler |

**Paper selbst sind keine Sammelbehälter für Rohbefunde.** Ein Primärbefund darf mehrere Papers speisen; das Paper verweist auf die stabile Objekt-ID und den geprüften Stand. Ein Manuskript kann unabhängig eine argumentative Synthese erstellen und muss diese ebenfalls als Interpretation mit Quellenbezug markieren.

## 4. Minimale standardisierte Übergabe (gemeinsamer FPP-Envelope)
Jedes beteiligte KI-System muss Ereignisse annehmen und zurückgeben können. Pflichtfelder:
`schema_version, event_id, object_id, object_type, object_version, event_type, actor, timestamp, source_refs, input_hashes, result, math_status, domain_status, review_status, visibility, intended_destinations, related_ids, required_tests`.
Optional: `software_version, environment, units, conditions, counterexamples, alternatives, confidence_note, change_set, licence, embargo, editorial_owner`.
**Trennung von Zustandsdimensionen**: syntaktisch/semantisch/mathematisch/fachlich/reproduziert/publiziert sind unabhängige Achsen; kein einzelner „PASS“-Wert kann eine fachliche Freigabe implizieren.

Beispiel: `REL-PFV-001`, Relation `P=F·v`, generiert aus `F025/F026/F027`, Bedingungen `t ≠ 0`, für Vektoren Skalarprodukt, Zustand `symbolically_derived`, `independent_math_check=true`, `domain_review=pending`, destinations `algebra + harvesting + relevant tensor candidates`. Die Beispiel-ID ist **provisorisch** bis zum Abgleich mit dem bestehenden ID-Register.

## 5. Wissenschaftliche Zustandsmaschine
`received` → `source_registered` → `parsed` → `semantic_typing` → `structural_candidate` → `symbolically_derived` → `counterchecked` → `independently_reproduced` → `domain_reviewed` → `ready_for_editorial_review` → `released`.
**Fehler-/Alternativzustände:** `parse_error`, `source_unavailable`, `semantic_ambiguous`, `dimension_conflict`, `domain_violation`, `not_invertible`, `counterexample_found`, `not_reproducible`, `restricted_validity`, `refuted`, `superseded`, `withdrawn`.
Die Formeln können algebraisch korrekt, fachlich eingeschränkt und redaktionell noch zurückgehalten sein. Jede Achse wird separat geführt. `not_assessed` oder `SKIP` ist **niemals** `pass`.

## 6. Zwei verschiedene Prozessketten – nie zusammenwerfen
**6A Erkenntnisgewinn S0–S10:** Quelle → Parsing → Semantik/Dimension → Struktur/Trinität → Ableitung → Gegenprobe → unabhängige Replikation → Tensorzuordnung/27er-Feldprüfung → Fachabnahme → Publikationsfreigabe.
**6B Erkenntnisverteilung P0–P7:** Eingang registrieren → ID/Zuständigkeit ermitteln → Dubletten/Konflikte erkennen → abhängige Artefakte im No-Loss-Graph auflösen → vorbereitete Änderungsdeltas erzeugen → Fachowner prüfen → Redaktionsowner freigeben → Register/Website/Papers reproduzierbar aktualisieren + Nachlauf auditieren.
Ein Ergebnis aus S5 darf bereits als „ungeprüfter Kandidat“ in die interne Analysebibliothek gelangen, aber nicht automatisch als bestätigte Formel in die Algebra-Publikation.

## 7. Abhängigkeits- und Routerlogik
- **Ein Ursprung, viele Ziele:** `REL-...` kann Algebra + Quellenregister + Glossar + FACH-F034 + Verfahrenstechnik-Paper + Website betreffen. Kein einfacher `kind → one_file`-Router; benötigte Zuordnungen sind `primary_owner` und `affected_artifacts[]`.
- **Manifeste pro Paper/Fachseite:** `publication_id, canonical_path, purpose, accepted_object_types, topic_tags, included_object_ids, last_built_source_commit, review_gate, release_policy`.
- **Impact-Kante**: `depends_on`, `uses_operator`, `tests`, `supports`, `contradicts`, `special_case_of`, `quoted_by`, `visualized_in`, `explained_in`, `supersedes`. Jede Kante hat Datum, Status und Quelle.
- **Keine stille Synchronisation**: wird ein relevantes Resultat gefunden, erstellt der Compiler mindestens ein `IMPACT-...`-Delta und eine Liste „betroffene Objekte“. Bei fachlich kritischem Inhalt erfolgt Veröffentlichung nur nach Review. Das System meldet „noch nicht synchronisiert“ bis Merge/Validierung.
- **Mehrfachautoren / Konflikte**: gleichzeitige Ergebnisse niemals „last writer wins“. Originalversionen beider KI bleiben mit eigenem Hash; abweichende Aussagen erzeugen einen Konfliktbefund mit Vergleichstest und verantwortlichem Review. Dieselbe Formel unterschiedlicher Semantik darf nicht über LaTeX-Gleichheit verschmolzen werden.

## 8. Zwei-KI-Kommunikationsvertrag
Jede Nachricht gilt als **Vorschlag**, **Resultat**, **Gegenbefund**, **Entscheidungsantrag** oder **ACK** und referenziert eindeutige Objekt-/Ereignis-/Zyklus-IDs.
`proposal` → `received_ack` → `tested` → `reviewed(accept|change|reject|needs_evidence)` → `decision_recorded` → `sync_proposed` → `merged` → `release_ack`.
Ein Kommentar auf GitHub ist eine **übermittelte Nachricht**, kein Nachweis, dass Claude sie gelesen, ausgeführt oder anerkannt hat. Freigabe der Publikation und Abschluss des KI-Zyklus sind getrennte Zustände.
Bestehende `REVIEW_QUEUE_V2.json` und `KI-2026-11-03-001/STATUS.json` behalten Priorität; keine parallel erzeugten Review-Aufträge für dieselbe Frage.

## 9. Dateistruktur: minimaler Ausbau, keine Duplikate
```text
forschung/
  register/
    FPP_ROUTING_V0_1.json               # Vorschlag: ein zentraler Router zu BESTEHENDEN Kanondateien
    analysis/                            # wissenschaftliche Befund- und Analyseakten mit IDs
    events/                              # append-only FPP-Ereignisse, nach Datum/Batch
    impact/                              # generierte Änderungsbedarfe, Test- und Reviewverweise
  koordination/
    REVIEW_QUEUE_V2.json                # bleibt bestehender Reviewkanal
    zyklen/KI-2026-11-03-001/            # bleibt bestehender Zyklus
  tensor/
    formeln/                             # bereits bestehender Formelbestand
    algebra-claude/                      # bereits bestehender Algebra-Code
    ...                                  # bestehende Tensorakten/Versionen nicht duplizieren
  website/
    ...                                  # bestehender UI-/QA-Bestand
docs/data/                               # nur geprüfte, freigegebene JSON-Projektionen
```
**Dies ist eine Sollstruktur.** Vor Verzeichniserstellung Bestands-Crosswalk und Rechteprüfung. Quellenregister und Glossar dürfen nicht als leere neue Listen parallel dupliziert werden.

## 10. Konkrete Umsetzung in fünf Schritten
**K1 Bestandscrosswalk**: existierende ID-Namensräume/Algebra-/Register-/Paper-Dateien/Skill-Zuordnungen, einschließlich 103 historische Tensorgerüste, Claude-Befunde, Rohformellauf und offene Review-IDs; primär/eingehend/abgeleitet/freigegeben kennzeichnen.
**K2 Vertrag und Validierung**: `fpp-envelope/0.1` JSON Schema, qualifizierte Kanten, Provenienz, Zustandsdimensionen und maschinenlesbare `paper_manifest`; fünf positive und fünf negative Testfälle.
**K3 Pilot**: `W=Fs`, `P=W/t`, `v=s/t` → Relation `P=Fv` (mit Bedingungen) einmal als Befund erfassen; Impact-Liste für Algebra, Formel-Harvesting, Tensorverbund, Glossar und didaktischen Website-Eintrag; keine fiktive Fachfreigabe.
**K4 Prozessautomation**: nur PR-Entwürfe und erzeugte öffentliche Projektionen automatisch; Reviewer/Publikationsfreigabe streng getrennt, deterministische Rebuilds und Referenzintegrität.
**K5 Abnahme und Messung**: Original-SHA, Vollständigkeit der Routen, Zahl unverarbeiteter Impacts, Konfliktlösungsrate, nachprüfbarer Rebuild, verlorene Objekt-IDs=0 und unabhängige mathematische Negativtests.

## 11. Streit-/Entscheidungsfragen für Claude
1. Welche der vorgeschlagenen Manifeste sind bereits vorhanden? Bitte exakte kanonische Pfade statt eines neuen Registers.
2. Können `tensor/1.0` und FPP über `object_id, source, relation, evidence` gekoppelt werden, ohne das Tensor-Schema neu zu definieren?
3. Welche Codepfade von Claude erzeugen verifizierbare Quellen-/Testereignisse, welche nur Ergebnis-JSON?
4. Welche vorhandenen Papers benötigen bei `P=Fv`, Sternelimination oder unzulässigen Gleichnamigkeitsbrücken tatsächlich ein Delta – und welche NICHT?
5. Können die bisherigen 100-Formel- und Wikidata-Läufe aus eingefrorenen Eingabedaten und Codeversionen reproduziert werden?
6. Zustimmung/Änderung/Ablehnung für Routing, semantisches Review-Gate und Provenienzmodell mit konkreten Gegenbeispielen.
