# Bürger-KI – Phase 7: Vom Forschungsbestand zur geprüften Verwaltungs-Skill-Engine

**ID:** BKI-PH7-001 · **Version:** 0.1 · **Datum:** 2026-11-04  
**Status:** Architektur und nächste Umsetzungsphase definiert; **keine Integration mit produktiven Verwaltungsdiensten nachgewiesen**.  
**Unabhängigkeit:** Bürger-KI nutzt erprobte Mitmach-Designprinzipien, ist aber organisatorisch und technisch **nicht** an die Tensor-Mitmachseite gekoppelt.

## 1. Ziel der Phase

Die existierende Bürger-KI-Forschungswerkstatt ist ein lokaler Demonstrator mit drei fiktiven Aufgaben und drei deterministischen Vergleichsstrategien. Phase 7 soll daraus ein überprüfbares Forschungswerkzeug für **echte, öffentlich dokumentierte Verwaltungsleistungen** machen, ohne Bürgerakten zu erfassen.

Die Forschungsfrage lautet: Können unabhängige Strategien dieselben Leistungs-, Zuständigkeits- und Quellenaufgaben reproduzierbar lösen? Welche Kombination erreicht den fachlich korrekten Zustand mit möglichst gutem Quellenbeleg, geringem Aufwand und transparenter Unsicherheit?

## 2. Verwaltungsbausteine als Harvest-Ziele, nicht als fertige KI-Skills

| Familie | Rolle | Anschlussfrage |
| --- | --- | --- |
| FIM: Leistungen / Prozesse / Datenfelder | fachlicher Objekt- und Prozesskatalog | Welche Leistungen und Bedingungen sind referenzierbar und versionierbar? |
| Leistungskatalog, XZuFi, Portalverbund | Suche nach Leistung, zuständiger Stelle, Online-Dienst | Welche offenen Schnittstellen und Datenfelder sind wirklich nutzbar? |
| Öffentliche Rechtsquellen | Originalnormen und Geltungsstand | Wie bilden wir konkreten Paragrafenbezug und Zeitstand ab? |
| KERN UX / Servicestandard | Interaktions- und Verständlichkeitsanforderungen | Welche Designkriterien lassen sich testen? |
| openCode und Fachbibliotheken | wiederverwendbare Software / Adapter | Welche Funktionen sind verfügbar, lizenziert, wartbar und überprüfbar? |

**Recherche-Ziele, keine hier bestätigten API-Anbindungen.** Offizielle Einstiegspunkte: https://docs.fitko.de/fim/ · https://docs.fitko.de/pvog/docs/ · https://www.design-system.gov.de/ · https://servicestandard.gov.de/ · https://opencode.de/de

## 3. Technische Kette und Verträge

`Aufgaben-ID → Quellen-Snapshot → Leistungsobjekt → Anfrageklassifikation → Skill-Auswahl → Strategie-Runner → Aussagen/Quellen → unabhängige Prüfungen → Ergebnisakte → Regression → freigegebene Version`.

Ein **Fachadapter** soll `service_id`, `jurisdiction`, `valid_at`, `source_id`, `conditions`, `exceptions`, `office_reference` zurückgeben. Ein **Strategie-Runner** muss bei gleicher Aufgabe und gleichem Quellenstand reproduzierbare Parameter dokumentieren. Ein **Reviewer** prüft Behauptungen gegen den fixierten Quellensnapshot.

Das Projekt soll keine persönliche Fallbearbeitung anbieten. Referenzaufgaben sind synthetisch, Fachinhalte stammen aus erlaubten öffentlichen Quellen. Freie Nutzereingaben gehören nicht in das öffentliche Forschungsregister.

## 4. Konkrete Arbeitspakete mit Abnahmekriterien

- **PH7-A – Fachinventar:** drei ausgewählte Verwaltungsleistungen mit Originalquellen, FIM-/Leistungskatalog-Bezügen, Geltungsbedingungen, Zuständigkeiten und Stichtag erheben. **Abnahme:** drei prüfbare Fachakten und Negativfälle.
- **PH7-B – Datenadapter:** mindestens ein öffentlich dokumentiertes Datenformat oder eine abrufbare Quelle versioniert einlesen; Test für fehlende/veraltete Angaben. **Abnahme:** wiederholbarer Import und Schema-Prüfung.
- **PH7-C – Strategie-Engine:** vier Verfahren am **gleichen** eingefrorenen Fall: direkter KI-Ansatz, Skill-Kette, unabhängige Gegenprüfung, Regelhybrid. **Abnahme:** identische Inputs, nachvollziehbare Outputs, ausgeglichene Budgets.
- **PH7-D – Goldstandard und Review:** referenzierte Sollantworten von der Strategieausführung trennen. **Abnahme:** 3 × 4 Strategien × 3 Wiederholungen = 36 dokumentierte Ausführungen; Bewertung unabhängig.
- **PH7-E – Interaktionslabor:** Frage, Strategieauswahl, Ergebnisvergleich und Vorschlag mit sichtbarer Provenienz; kein vermeintlicher Echtservice. **Abnahme:** Browser-End-to-End-Test, verständliche Fehlermeldungen, unabhängige Reproduktion.
- **PH7-F – Verbesserungsschleife:** Änderungsvorschlag → Test gegen alten Stand → positiver/negativer Befund → Versionierung. **Abnahme:** mindestens ein überprüfter Veränderungsversuch einschließlich Regressionstest und offenem Negativbefund.
- **PH7-G – Forschungsmethoden/Quellen:** Paper, Quellenregister und Glossar IDs/Versionen synchronisieren. **Abnahme:** Quellen-Crosswalk und Statusübersicht vollständig.

## 5. Ein fairer Benchmark

Fünf getrennte Bewertungsdimensionen (je 0–4): Fachkorrektheit, Belegtreue, Abdeckung, Unsicherheitsbehandlung und Handlungsorientierung. Dazu Ausführungszeit, Werkzeugaufrufe, Ressourceneinsatz und Fehlerklasse. Keine einzige aggregierte „KI-Qualität“, die schwere fachliche Fehler verdecken könnte.

Die Strategiebedingungen werden vor einem Versuch eingefroren. Ein **formaler Regelcheck** kann ein prüfbares Teilurteil liefern, ersetzt aber keine unabhängige Prüfung offener Rechtsfragen. Für jedes Ergebnis sind stützende Originalstellen, Gegenproben und Änderungsstand zu nennen.

## 6. Gesamtprozess: zehn Abnahme-Meilensteine

Die Website bildet den Fortschritt anhand dieser **zehn gleich gewichteten, binären Abnahme-Gates** ab. Bei Teilfertigstellung bleibt ein Gate offen; Details können „in Arbeit“ zeigen. Das verhindert Scheingenauigkeit.

| Gate | Kriterium | Stand 04.11.2026 |
| --- | --- | --- |
| G01 | Grundkonzept und fachübergreifender Lösungsweg dokumentiert | **Erfüllt:** veröffentlichte Grundlagen-/Wege-Seiten |
| G02 | Methodik, Mitmach-Meta-Paper, Forschungs- und Testplan dokumentiert | **Erfüllt:** versionierte MD-Artefakte |
| G03 | Eigenständige lokale Vergleichswerkstatt im Repository implementiert | **Erfüllt:** HTML/JS vorhanden; Browser-E2E nicht nachgewiesen |
| G04 | Fachbestände/FIM-/Zuständigkeitsdaten quellengeprüft als Testkorpus | Offen |
| G05 | Mindestens ein echter Fachadapter mit wiederholbaren Importtests | Offen |
| G06 | Echter KI-Strategie-Runner mit fairen Vergleichsbedingungen | Offen |
| G07 | Unabhängige Bewertung von 36 Pilotläufen dokumentiert | Offen |
| G08 | Rückgabe- und Verbesserungskette unabhängig end-to-end geprüft | Offen |
| G09 | Regressions- und Übertragbarkeitstests bestanden | Offen |
| G10 | Öffentliche wissenschaftliche Ergebnisfassung nach Review freigegeben | Offen |

**Gesamtstand: 3/10 Gates (30 %) dokumentiert bzw. implementiert, nicht 30 % nachgewiesene KI-Wirksamkeit.** Für alle empirischen Gates G04–G10 gilt: bislang **0 bestandene Abnahmen**. Die drei erfüllten Gates sind Grundlagen- bzw. Implementierungsmeilensteine.

## 7. Phasenlandkarte (qualitative Statusangaben)

1. **Grundidee & Vernetzung:** dokumentierte Konzeption
2. **Anwendungsfelder:** dokumentierte Konzeption
3. **Vom Anliegen zur Lösung:** dokumentierter Pfad
4. **Skillarchitektur:** spezifiziert / empirisch offen
5. **Lernen und Selbstverbesserung:** Hypothesen / Tests offen
6. **Mitmach-Logik als eigenständiges Design:** Meta-Paper und lokaler Prototyp; Nutzerstudien offen
7. **Verwaltungs-Skill-Engine:** **aktuelle Phase**, Umsetzungsplan; Fachadapter noch offen
8. **Unabhängige Validierung, Replikation und Veröffentlichung:** Zukunftsphase, keine validierten Wirksamkeitsdaten

**Wichtige Unterscheidung:** Der Phasenstand ist ein Planungs-/Forschungsstand, keine Prozentzahl wissenschaftlichen Erfolgs.

## 8. Publikationen, Quellen und No-Loss

Die Bürger-KI-Seite soll die **Forschungsbibliothek prominent** direkt nach dem Einstieg zeigen: No-Loss-Gesamtstand, Skill-Deep-Dive/Harvest, Experimentierlabor, Meta-Paper zur Mitmachlogik, Phase-6-Design und Phase-7-Forschungsplan. Für Verwaltung und Rechtsgrundlagen sollen die Originalquellen separat und konkret zugänglich bleiben; ein Paper ersetzt keine Originalquelle.

Gemeinsamer Registervertrag:
`Quelle → Verwaltungsobjekt → Begriff → Skill → Strategie → Test → Gegenprobe → Ergebnis → Paper → Freigabe`.

**Keine dokumentierten Ergebnisse erfinden.** Die GitHub-Papers sind vorerst Forschungs-/Arbeitsfassungen und nicht automatisch wissenschaftlich begutachtet. Die gesonderte Tensor-Mitmachseite wird nicht verbunden.

## 9. Nächste Umsetzung

Zuerst drei reale Leistungen anhand amtlicher Originalbestände aussuchen und versionieren, dann drei synthetische Aufgaben daraus erstellen. Anschließend den regelbasierten Runner ergänzen und das Interface mit den Quellenakten verbinden. Erst danach echte KI-Strategien hinter einem serverseitigen Adapter anschließen (keine API-Schlüssel auf GitHub Pages). Im Anschluss Referenzbewertungen unabhängig durchführen und dokumentieren.

**Fertigkeitskriterium für Phase 7:** Mindestens eine reale Quellenfamilie, ein wiederholbarer Import, eine funktionierende fachliche Skill-Ausführung und ein unabhängiger Vergleich mit konkreten negativen Tests. Das ist gegenwärtig noch **nicht erreicht**.

## Zwischenstand Phase 7.2: Rechtsquellen-Adapter (4. November 2026)

**Umgesetzt im Repository:**
- [XML-Adapter für lokal gespeicherte Gesetzesdateien](../forschung/buerger-ki/bki_gii_adapter.py) (Gesetzeskürzel BMG/GewO; Extraktion von Paragraphen; SHA-256-Herkunfts- und Texthashes; expliziter Ausschluss einer automatischen Prüfung der Rechtsgültigkeit und örtlichen Zuständigkeit).
- [Synthetische Regressionstests](../forschung/buerger-ki/test_bki_gii_adapter.py) für gültigen Input, Normduplikate, falsche Quelle, unerwünschte Entity-Deklarationen, fehlende Normen und falsches Gesetz.
- [CI-Workflow](../.github/workflows/bki-gii-adapter-tests.yml) zur isolierten automatischen Testausführung.

**Noch nicht nachgewiesen:** erfolgreicher GitHub-Actions-Lauf, echter XML-Download/Import vom amtlichen Anbieter, vollständige GII-Formatabdeckung, unabhängige Rechtsprüfung. Es wurde kein produktiver öffentlicher PVOG-Adapter implementiert.

**Quellengrenzen:**
- [GII-Hinweise](https://www.gesetze-im-internet.de/hinweise.html): XML für maschinelle Verarbeitung; konsolidierte Texte sind von der amtlichen Verkündungsfassung im Bundesgesetzblatt zu unterscheiden.
- [FITKO PVOG Suchdienst](https://docs.fitko.de/efa-parametrisierung/docs/parametrisierungsleitfaden/): öffentlich nutzbare Such-API, Abfragen und nachgelagerte Filter oft erforderlich.
- [PVOG Bereitstelldienst](https://pvog.fitko.de/docs/bereitstelldienst/ueberblick/): vollständiger Datenzugriff nur autorisiert, kein automatisch offener Gesamtdatenexport.
- [PVOG Versionierung](https://docs.fitko.de/pvog/docs/anbindung_bed/schnittstelle/anbindung_bed_versionierung/): dokumentierte neue Version v3/XZuFi 2.3.1; beim späteren Adapter zwingend Versionsvertrag beachten.

**Nächster überprüfbarer Schritt:** echten GII-XML-Snapshot (BMG und GewO) herunterladen, dessen Original-URL und SHA dokumentieren, Parser mit den echten Dateien und dem Regressionskorpus erfolgreich ausführen, die extrahierten Paragraphen gegen die sichtbaren Originalstellen vergleichen und offene Fehler in einer Import-/No-Loss-Akte festhalten. Erst danach ist eine technische Adapterabnahme sinnvoll.

**Fortschrittszähler unverändert 3/10 Gates (30 %).** Code- und Testanlage zählen nicht als G05, solange kein wiederholbarer, erfolgreich belegter Echtimport vorliegt.

## Phase 7.3 – Realer Quelltransport statt bloßem XML-Mock (5. November 2026)

**Neue, tatsächlich gespeicherte technische Artefakte:**
- [XML-/ZIP-Importer v0.2](../forschung/buerger-ki/bki_gii_adapter.py) liest GII-`xml.zip` mit genau einer XML-Datei; prüft Archivstruktur, Größe, externe Quelle und verwahrt SHA-256 für ZIP und enthaltenes XML getrennt.
- [9 synthetische Regressionstests](../forschung/buerger-ki/test_bki_gii_adapter.py) prüfen unter anderem Archivannahme, Doppeldokumente und unsichere Mitgliedspfade.
- [Live-Echtquellenprüfung](../forschung/buerger-ki/bki_gii_live_smoke.py): BMG (`https://www.gesetze-im-internet.de/bmg/xml.zip`, Ziel § 18) und GewO (`https://www.gesetze-im-internet.de/gewo/xml.zip`, Ziel § 14); Quellen- und Paragraphen-Hashes werden in `bki_gii_live_result.json` festgehalten.
- [GitHub-Actions-Test](../.github/workflows/bki-gii-adapter-tests.yml) führt synthetische Tests bei Codeänderung durch. Die **Live-Prüfung läuft nur bei manuellem `workflow_dispatch`**; ihre JSON-Akte wird bei Ausführung als Artifact abgelegt.

**Evidenzgrenze:** Die Website von Gesetze-im-Internet dokumentiert bei beiden Gesetzen XML als herunterladbares **ZIP-Paket**, nicht als direkte Einzel-XML. Dieser Transportfehler wurde im Adapter korrigiert. Ein erfolgreicher Live-Abruf konnte aus dieser Arbeitsumgebung **nicht** durchgeführt oder als GitHub-Workflow-Bericht geprüft werden. Bis zu einem erfolgreichen und nachvollziehbaren Lauf **keine Freigabe** des Echtquellen-Adapters. Der Parser behandelt konsolidierte Rechtstexte, nicht amtlich verkündete Fassungen, und entscheidet weder örtliche Behördenzuständigkeit noch individuelle Ansprüche.

**No-Loss-Negativbefunde:**
- Vorversion nahm fälschlich eine direkt bereitgestellte XML-Datei als einzigen realen Eingabetyp an.
- Vorhandene Quellen-ID-Prüfung ist keine inhaltliche Rechtsprüfung.
- Ein erfolgreiches CI-Unittest-Paket wäre noch kein Nachweis von Live-Datenkompatibilität.
- G04/Fachkorpus und G05/Datenadapter bleiben bis zur unabhängigen Abnahme offen; Gesamtstand bleibt bei **3/10 Gates**.

**Nächste Abnahme:** GitHub Actions manuell ausführen; Ergebnis-`bki_gii_live_result.json` mit `passed` und beiden Zielparagraphen bestätigen; 2 Originalstellen stichprobenhaft gegen extrahierte Texte vergleichen; Quelle, Stichtag und eventuelle Parserfehler versionieren. Erst danach echten Skill-Runner und örtliche PVOG-Leistungsauflösung aufsetzen.
