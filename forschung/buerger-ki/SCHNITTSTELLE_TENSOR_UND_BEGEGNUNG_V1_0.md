# Bürger-KI ↔ KI-Tensor · Schnittstellen-, Begegnungs- und Pilotvertrag v1.0

**Stand:** 2026-11-04 · **Status:** Architektur/Spezifikation, nicht implementierte Automatik. **Geltung:** Bürger-KI-Forschungsbestand; globale Tensor-Dateien bleiben unberührt. Änderungen am Tensor erfolgen später nur über gesonderte Prüfung und Freigabe.

## 1. Rollen und Grenzen
**Bürger-KI:** öffentlicher Lern-, Handlungs-, Vernetzungs- und Forschungsraum; zunächst Website, Quellen, Anleitungen, Vorlagen, lokale selbstverwaltete Falldaten, bestehende lokale und digitale Organisationen. Sie ist derzeit weder eine eigenständige KI noch eine Plattform zur sicheren Speicherung privater Patientenakten noch ein tatsächliches Gruppenmatching.
**Tensor:** übergreifendes Forschungs- und Prüfsystem für formalisierte Relationen, Operationen, Invarianten, Umformung, Rückrechnung, Typen und Gegenproben. Er ist weder Richter noch Behandler oder Rechtsberatungsstelle.
**Menschen/Institutionen:** entscheiden und handeln eigenständig; Fachfragen benötigen geeignete Fachkompetenz. Kein Ersatz für medizinische Indikation oder rechtliche Einzelfallberatung.

## 2. Gemeinsames Prüfobjekt und geschlossene Forschungsrückkopplung
`Problemanlass → fachliche Frage → atomarer Skill → Operator/Relation → Test/Gegenprobe → Ergebnis → Rückgabe des geprüften Skills → Anwendung → Wirkungsmessung → neues Problem`
Die Übersetzung erfolgt ausdrücklich **nicht** durch automatisches Übernehmen aller Bürger-KI-Aussagen in Tensorfelder. Jede Generalisierung benötigt Typprüfung, Quellen, reproduzierbaren Test, Gegenprobe, Geltungsbedingungen und eine Abnahme.
Es werden **keine individuellen Fallakten** in den Tensor übertragen.

### Erntevertrag Bürger-KI → Tensor (BK-EXPORT)
- `object_id`: stabile ID; `version`; `source_refs` und `provenance`
- `problem_id`, `task_id`, `skill_id`, `operator_candidates[]`
- `input_schema`, `output_schema`, `assumptions`, `preconditions`, `constraints`
- `relation_family`, `invariants[]`, `inverse_status`, `counterexamples[]`
- `test_cases[]` mit synthetischen oder ausdrücklich zur Weitergabe freigegebenen Daten
- `baseline_id`, `quality_metrics`, `result_status`, `limitations`
- Keine Namen, Adressen, Akten, Diagnosen, Identifizierungs- oder Termindaten von Beteiligten; keine implizite Einwilligung.

### Rückgabevertrag Tensor → Bürger-KI (BK-IMPORT)
- `operator_id` mit Version, Quell- und Testreferenzen
- formale `input/output`-Typen, Definitionen und Geltungsgrenzen
- reproduzierbarer positiver/negativer/Grenz-/Gegenbeispiel-Test
- Integrationsvorschlag `skill_id`, `changes`, `benefit_hypothesis`
- Regression gegen bestehende Verfahren und fachliche Prüfung
- Status: `kandidat → getestet → fachlich geprüft → freigegeben`; kein stillschweigender Import
- Falls keine bestätigte Verbesserung: `null_result` mit Begründung, keine erfundene Tensorwirkung.

## 3. Was erntet der Tensor konkret?
| Bürger-KI-Fall | Operatorfamilie | Tensor-Frage | messbares Rückgabeprodukt |
|---|---|---|---|
| Recht vs. Erfüllung | dreistufige Bedingungslogik | Welche Voraussetzungen, Ausnahmen und unbekannten Werte? | nachvollziehbarer Anspruchsprüfer |
| nicht gezahlte Leistungen | Soll-Ist/temporale Relationen | Welche Beträge/Zeiträume sind vergleichbar, was ist invertierbar? | Differenz- und Rückrechnungs-Skill |
| Psychotherapieplatzsuche | Constraint- und Abdeckungssuche | Wann erfüllt ein Angebot die fachlichen Anforderungen? | prüfbarer Eignungs-/Status-Skill |
| Versorgungslücke | Mengen, Kapazität, Zeit, Warteschlange | Sichtbare Nachfrage ≠ Bedarf ≠ Leistung | sauber begrenzter Kapazitäts-Benchmark |
| Fehler-/Konfliktkultur | Ereignis-, Widerspruchs- und Kausalgraph | Welche Pflicht, Handlung und Wirkung lässt sich getrennt rekonstruieren? | Konflikt-/Unterlassungsprüfmatrix |
| Gruppenkooperation | Graph und Deduplikation | Was erhöht den Nettoeffekt ohne Verdrängung? | Gruppenvergleich mit Gegenhypothese |

## 4. Reale Begegnung: Sechs Zugangspunkte
- **Allein:** Küchentisch, Smartphone, Papierakten, persönliches Problem; niemand muss Mitglied einer Gruppe werden.
- **Bei bestehender Hilfe:** Selbsthilfekontaktstelle, Patientenberatung, 116117, Anlaufstellen, Beratungsinitiativen.
- **Nachbarschaft:** Bibliothek, Stadtteilzentrum, Mehrgenerationenhaus, bestehendes offenes Café oder Bürgerveranstaltung.
- **Digital:** vorhandene thematische Communitys, Veranstaltungslisten, digitale Selbsthilfegruppen, moderierte Videotreffen.
- **Organisiert:** bereits existierende Gruppen, Fach- und Patientenvertretungen, regionale Initiativen.
- **Institutionell:** Anhörungen, kommunale Verfahren, Rückmeldungen, dokumentierte Gespräche mit zuständigen Stellen.
Die Website verweist auf vorhandene Angebote. Ohne geprüfte reale Partner, Termin und Einverständnis darf sie **kein aktives Bürger-KI-Café und keine existierende lokale BK-Gruppe suggerieren**.

## 5. „Wo trifft man sich auf einen Kaffee?“ – minimale reale Begegnung
**Pilotmoment BK-MEET-01:** Ein vorhandener öffentlicher Ort (Bibliothek, Selbsthilfekontaktstelle etc.) bietet *freiwillig* ein 60–90-minütiges offenes Informations- und Methoden-Treffen an. Die Bürger-KI liefert einen einseitigen Ablauf: Begrüßung/Vertraulichkeit, gemeinsames Problem ohne Krankendetails, Skilldemo mit synthetischem Fall, offene Quellenfrage, nächster freiwilliger Schritt, anonymisierte Methodenrückmeldung.
**Nicht erforderlich:** Mitgliedschaft, Diagnose, Vollname auf Teilnehmerliste, persönliche Falloffenlegung oder Nutzung einer bestimmten KI.
**Prüfen:** Ort tatsächlich bestätigt? Träger/Ansprechpartner beteiligt? Zugänglichkeit? Moderation? Notfall-/Verweisstruktur? Datenschutz und Regeln für Minderjährige? Wie gelangt eine geprüfte Methodenverbesserung zurück?
**Nullfall:** Niemand erscheint oder niemand möchte sich vernetzen. Das ist ein zulässiges Forschungsergebnis; individuelle Werkzeuge bleiben nutzbar.

## 6. Online zu lokalen Treffen – keine erfundene soziale Plattform
Pfad: `Thema wählen → Region selbst bestimmen → bestehende lokale Anlaufstellen/öffentliche Treffen prüfen → Teilnehmer entscheidet → geschützter persönlicher Kontakt nach Regeln des Trägers → freiwilliger Mitmachbeitrag`.
Vor Veröffentlichung eines konkreten Orts-/Termineintrags: Originalquelle, Zeit, Adresse, Ansprechpartner, Öffentlichkeitsstatus und überprüfbares Aktualisierungsdatum. Kein improvisiertes, öffentliches Personenmatching oder Gesundheitsdaten in GitHub-Issues.
Nicht existierende Gruppen werden nicht als Angebote dargestellt. Bei fehlenden Treffpunkten wird auf eine vorhandene Kontaktstelle verwiesen oder eine klar als *Vorschlag* markierte Selbstorganisationsanleitung angeboten.

## 7. Zwei nicht zu unterstellende Hypothesen
**BK-H-NET-01:** Menschen mit vergleichbaren Anliegen nutzen bestehende Kontakte oder knüpfen freiwillig neue Verbindungen. **Nicht vorausgesetzt.** Test: Sichtbarkeit und tatsächliche Inanspruchnahme geeigneter Angebote, Freiwilligkeit, Gründe gegen Vernetzung, langfristige Beteiligung, Konflikte, Zugänglichkeit und Nebenwirkungen.
**BK-H-EVID-01:** Vernetzung und bessere Werkzeuge erhöhen die Qualität individueller bzw. struktureller Unterversorgungsnachweise. **Nicht automatisch wahr.** Test: fachliche Belegprüfung, Unterscheidung Bedarf/registrierter Nachfrage/erfüllte Versorgung, belastbarer Nenner, regionale/zeitliche Eingrenzung, Auswahlverzerrung, institutionelle Gegenposition, Norm und Rechtsschutz.
**BK-H-AI-01:** Mehrere autonom miteinander kommunizierende KIs verbessern die Ergebnisse gegenüber guten Regeln, einem einzelnen Werkzeug und menschlicher Gegenprüfung. **Nicht belegt und für Stufe 1 nicht erforderlich.** Erst als separaten Benchmark prüfen (Qualität, Kosten, Fehlerrate, Reproduzierbarkeit); ohne Vorteil nicht implementieren.

## 8. Was, wenn alle gleichzeitig Ansprüche geltend machen?
Rechtlich mögliche Einzelansprüche bleiben individuell. **Viele Anträge sind weder ein Nachweis der Unterversorgung noch ein Grund, Rechte herunterzurechnen.** Zu testen sind: Zahl fachlich berechtigter Fälle, registrierte Nachfrage, tatsächlich erreichbare Leistungen, Bearbeitungsfähigkeit, Wartezeit, Verdrängung, institutionelle Reaktionen und Alternativangebote. Kein Masseneinreichungsautomat. Bei strukturellem Problem: institutionelle Pflichten und Gegenbefunde getrennt prüfen.

## 9. Umsetzungsphasen (mit Abnahmekriterium)
**Stufe 0 – jetzt:** statische Website, drei Erkenntnispfade, 32 spezifizierte Skills, zwei Vertikaltests, strukturierte Austauschverträge; keine aktive KI, automatische Gruppensuche oder Datenübertragung.
**Stufe 1 – erster Pilot:** lokales eigenes Such-/Aktenprotokoll, erprobte Anleitungen, geprüfter Skilltest mit synthetischen Fällen; Erfolg: reproduzierbar korrekte Ausgaben gegenüber vorhandenem Angebot.
**Stufe 2 – reale Kooperation:** Einladung über vorhandene lokale Organisation; ein bestätigtes Treffen oder Nullbefund; nur einwilligungsbasierte, aufbereitet freigegebene Methodenrückmeldung.
**Stufe 3 – wissenschaftliche Ernte:** getestete Operatoren-Crosswalk, fachliche Freigabe, Tensor-seitige Vergleichsakte; Null-/Negativergebnisse dokumentieren.
**Stufe 4 – Rückgabe:** reproduzierbare, versionierte Verbesserungen als BK-Skills mit Vorher/Nachher-Tests. Eine echte KI-zu-KI-Orchestrierung nur bei nachgewiesenem Nutzen und separater Entscheidung.

## 10. Synchrone Registerpflicht
Bei späterer Übernahme: gemeinsam zu ändern sind Quellen, Glossar, Skillvertrag, Tests, Evidenz- und Versionsstatus, Promptvorlage und betroffene Seiten. Die globale Tensor-Infrastruktur wird **nicht** in diesem Bürger-KI-Commit angepasst; Übergabestatus bleibt `proposed`.
