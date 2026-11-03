# SOULution · Zweitversuch und selbstprüfende Folge-Prompts

Stand: 2026-11-03. Forschungs- und Testprotokoll, keine Publikationsfreigabe.

## Grundregel
Ein zweiter Fehlschlag beendet den Lauf nicht durch fingierte Resultate. Er erzeugt eine konkrete, minimal prüfbare Mitmachaufgabe: Ursache → vorhandene Ressourcen → kleinster realer Test → erwartetes Artefakt → Gegenprobe → Abbruchbedingung. Ergebnisse werden nicht als abgeschlossen ausgegeben. Nur tatsächlich geprüfte Quellen dürfen als Belege dienen.

## Evidenzstufen
`entdeckt → per Web lesbar → heruntergeladen → geparst → unabhängig reproduziert`. Keine automatische Hochstufung.

## VP-01 · Historischer Evaluierungs- und Fristenatlas

**Zweiter Versuch:** teilweise. NKR-Sammelangaben erneut zugänglich; keine zehn einzeln belegten Evaluationsfälle extrahiert

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-01 (Historischer Evaluierungs- und Fristenatlas). Ziel: Extrahiere aus drei datierten NKR-Berichten eine quellengenaue Stichprobe von mindestens 10 einzeln identifizierbaren Evaluierungspflichten. Erfasse Rechtsbasis, zuständige Stelle, Fristauslöser, Fälligkeit, tatsächliche Durchführung, Bericht/Übermittlung, Publikationsdatum, Verfügbarkeit und Änderungen. Trenne nicht auffindbar von verspätet belegt und von nicht fällig. Berechne nur bei nachgewiesenem Nenner eine Fristquote. Erwartete Abnahme: 10 Fallakten mit Quellen und Datumslogik; mindestens 2 vollständig rückverfolgt Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Musterfälle aus NKR-Berichten mit Primärgesetzen und tatsächlichen Berichtsdaten verknüpfen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-02 · Fristenregelmaschine und Negativtests

**Zweiter Versuch:** wiederholt_getestet. 6/6 synthetische Fristen-Unit-Tests erneut bestanden; echte Normfristen ungetestet

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-02 (Fristenregelmaschine und Negativtests). Ziel: Entwirf eine maschinenlesbare Fristenregel für die Fälle aus VP-01. Prüfe Inkrafttreten, Übergangsrecht, Friständerung, Durchführung, Übermittlung und Veröffentlichung getrennt. Teste 6 Gegenfälle einschließlich noch nicht fällig, nicht veröffentlicht aber durchgeführt, geändert, aufgehoben, verspätet und unbekannt. Erwartete Abnahme: 6 reproduzierbare Tests mit richtigem Status und Beleg Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Zwei reale Rechtsfälle und Änderungsfälle in Testregeln übernehmen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-03 · Laufende Entscheidungen und Änderungsmonitor

**Zweiter Versuch:** blockiert_laufzeit. DIP-API-Dokumentation geprüft; erneuter direkter HTTPS-Aufruf ConnectionError; API-Key Voraussetzung

**Ursachenklasse:** environment_or_auth

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-03 (Laufende Entscheidungen und Änderungsmonitor). Ziel: Prüfe die tatsächliche maschinenlesbare Abrufbarkeit aktueller Verfahrensdaten. Erfasse eine begrenzte Menge neuer/geänderter Vorgänge samt ID, Zeitstempel, amtlicher Quelle und Version. Simuliere mindestens zwei aufeinanderfolgende Abrufe und dokumentiere echte Differenzen ohne erfundene Ereignisse. Erwartete Abnahme: Datenabruf, Schema, Deltaprotokoll und Fehlerfall Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: DIP-Adapter mit gültiger Zugangskonfiguration und zwei zeitversetzten Abrufen testen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-04 · SVIK-Rechts- und Zuständigkeitskette

**Zweiter Versuch:** teilweise. SVIK-Pflichten beschrieben; vollständige Rechtsversions- und Institutionenmatrix fehlt

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-04 (SVIK-Rechts- und Zuständigkeitskette). Ziel: Ermittle für SVIK jede einschlägige Pflicht und Zuständigkeit mit genauer Normfassung, Fristauslöser, Adressat, Berichtsempfänger und Kontrollbefugnis. Trenne Rechtspflicht, verwaltungsinternen Standard und Forschungsforderung. Erwartete Abnahme: Quellengebundene Verantwortungs- und Pflichtmatrix Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Normen samt Fassungszeitraum und Berichtsempfänger einzeln extrahieren

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-05 · SVIK-Datenzugang und Dateiverarbeitbarkeit

**Zweiter Versuch:** blockiert_laufzeit. Bund- und Länderportale per Web lesbar; HTTPS-Rohdatenabruf erneut ConnectionError

**Ursachenklasse:** environment_or_auth

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-05 (SVIK-Datenzugang und Dateiverarbeitbarkeit). Ziel: Versuche die amtlichen Downloads tatsächlich herunterzuladen. Dokumentiere URL, Zugangsbedingungen, MIME-Format, Dateihash, Datenjahr, Spalten, Metadaten, Lizenz und maschinelle Lesbarkeit. Trenne öffentlich genannt, erreichbar, heruntergeladen und erfolgreich geparst. Erwartete Abnahme: Mindestens je 1 belastbarer Datensatz für Bund, Länder und KTF ODER dokumentierter Blocker Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Downloads per Browser/CI mit Prüfsumme, Schema- und Lizenzprotokoll testen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-06 · Finanzfluss Plan–Ist–Bindung–Empfänger

**Zweiter Versuch:** nicht_reproduziert. Kein tatsächlicher Dateiexport für Soll/Ist und Empfänger eingelesen

**Ursachenklasse:** missing_empirical_validation

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-06 (Finanzfluss Plan–Ist–Bindung–Empfänger). Ziel: Rekonstruiere die drei Finanzierungssäulen und einen ausgewählten Haushaltstitel mit Ermächtigung, Soll, Bindung, Ist, Erstattung, Empfänger und Leistungsstand. Rechne Summen und Doppelzählungen gegen. Lege für nicht verfügbare Endempfängerdaten explizite Lücken an. Erwartete Abnahme: Reproduzierbare Finanzflussakte und Nachrechnung Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Originaldownload zuerst, dann Summen und Doppelzählungen maschinell prüfen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-07 · Zusätzlichkeit: Methoden- und Gegenvergleich

**Zweiter Versuch:** nicht_reproduziert. BMF/IW-Definitionen als verschieden erkannt; Originalrechenweg nicht reproduziert

**Ursachenklasse:** missing_empirical_validation

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-07 (Zusätzlichkeit: Methoden- und Gegenvergleich). Ziel: Rekonstruiere beide öffentlich verwendeten Zusätzlichkeitsdefinitionen mit Jahren, Bezugsgrößen, Gegenmodellen und Quellen. Prüfe die Rechenwege soweit verfügbar. Stelle Prozentwerte erst bei identischem Nenner einander gegenüber; andernfalls erkläre den Unterschied. Erwartete Abnahme: Methoden-Crosswalk, Rechenversuch, Grenzen Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Jahresbezogene Formeln, Nenner und Vergleichsszenarien aus Originalmaterial abgleichen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-08 · Ziele–Meilensteine–Output–Wirkung

**Zweiter Versuch:** teilweise. Amtliches phasenbasiertes Input/Output/Outcome/Impact-Modell belegt; kein einzelner Titel vollständig durchgerechnet

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-08 (Ziele–Meilensteine–Output–Wirkung). Ziel: Wähle einen konkreten SVIK-Haushaltstitel. Verbinde Mittelabfluss, definierte Zielindikatoren, Meilensteine, nachgewiesenen Output, Outcome und Impact. Prüfe welche Indikatoren nur Planungsfortschritt abbilden und ob Vergleiche zwischen Fachbereichen zulässig sind. Erwartete Abnahme: Eine vollständige Musterakte oder transparent belegte Lücken Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Einen Haushaltstitel samt Daten- und Indikatordefinition vollständig aus Bericht ziehen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-09 · Prüf- und Kontrollqualität

**Zweiter Versuch:** offen. Keine fünf vollständigen dokumentierten Kontrollketten

**Ursachenklasse:** missing_empirical_validation

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-09 (Prüf- und Kontrollqualität). Ziel: Ordne für eine Stichprobe von mindestens fünf Maßnahmen Rechtskontrolle, Mittelverwendungsprüfung, Evaluation, unabhängige Prüfung und Nachsteuerung zu. Prüfe Veröffentlichung, Frist, methodische Qualität und dokumentierte Folgen getrennt. Erwartete Abnahme: 5 Kontrollketten mit Nachweisstatus Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Zunächst zwei belastbare Beispiele aus NKR und Bundesrechnungshof, danach auf fünf erweitern

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-10 · Lösungs- und Alternativenatlas

**Zweiter Versuch:** teilweise. Amtliches Monitoring und Länderdashboard existieren; alternative Lösungen nicht gleichförmig getestet

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-10 (Lösungs- und Alternativenatlas). Ziel: Identifiziere vorhandene Monitoring-, Evaluations- und Datenwerkzeuge, ihre Schnittstellen, Lizenzen und Grenzen. Vergleiche zwei Verbesserungsvorschläge anhand der festgestellten Lücken statt ein paralleles Dashboard vorauszusetzen. Erwartete Abnahme: 2 belegte Lösungen plus Integrationsempfehlung Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Vorhandene Lösungen anhand eines identischen Qualitätsrasters vergleichen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-11 · Prompt-Benchmark und zwei Durchläufe

**Zweiter Versuch:** offen. Zwei textliche Recherchedurchläufe existieren, jedoch kein eingefrorener identischer Benchmark-Korpus

**Ursachenklasse:** missing_empirical_validation

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-11 (Prompt-Benchmark und zwei Durchläufe). Ziel: Führe H1–H5 sowie die professionellen P01–P08 auf demselben eingefrorenen Quellenstand aus. Vergleiche Vollständigkeit, Datenverfügbarkeit, Fehler, prüfbare Aussagen, Aufwand und wiederverwendbare Datenobjekte. Wiederhole den Test nach Prompt-Optimierung mit gleicher Testmenge. Erwartete Abnahme: Vorher/Nachher-Testmatrix samt Quellen, Fehlerklassen und Nachprüfungen Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Quellen-Snapshot fixieren, identische Fälle H1-H5/P01-P08 ausführen und Fehler messen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-12 · Gemeinsame Skill- und Datenbank-Wiederverwendung

**Zweiter Versuch:** technisch_teilgeprüft. GitHub-Register und Skillreferenzen existieren; keine drei ausgeführten realen Skills

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-12 (Gemeinsame Skill- und Datenbank-Wiederverwendung). Ziel: Ordne jedem benötigten Skill und Datentyp eine existierende Quelle oder einen belegten Fehlbestand zu. Unterscheide on_git, local_only, Kandidat, ausführbar, getestet und validiert. Vermeide neue Kopien gemeinsamer Quellenobjekte. Erwartete Abnahme: Crosswalk und 3 kleine ausführbare Skilltests oder begründete Blocker Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Skilladapter anhand vorhandener Implementierung mit Eingabe/Ausgabe/Tests ausführen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-13 · Relations- und Tensorübergabe

**Zweiter Versuch:** offen. Relationsfamilien sind Kandidaten; keine fachlich validierte Tensorüberführung

**Ursachenklasse:** missing_empirical_validation

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-13 (Relations- und Tensorübergabe). Ziel: Extrahiere nur quellengebundene, typisierte Relationskandidaten mit Träger, Definition, Geltung, Test und Gegenbeispiel. Prüfe vorhandene Tensorregister auf Duplikate. Gib Kandidaten an KI-Tensor weiter; bestätige keinen 3×3×3-Tensor ohne drei geprüfte Trinitäten und 27 geprüfte Feldpositionen. Erwartete Abnahme: Relationsakten, kein erfundener Tensorabschluss Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Relations-ID gegen historische Register prüfen; Gegenprobe und 27 Feldakten nur bei begründetem Kandidat

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-14 · Buchbelege, Originalcover und Didaktik-Abnahme

**Zweiter Versuch:** blockiert_material. Originalcover und vollständige Buch-PDFs in diesem Lauf nicht als gesicherte Satzmaterialien abgeglichen

**Ursachenklasse:** missing_originals

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-14 (Buchbelege, Originalcover und Didaktik-Abnahme). Ziel: Sichere Originalcover und exakte Buchauszüge mit Seitenangaben. Leite nur geprüfte Zahlen und Beispiele in den Haupttext ab. Erkläre notwendige Relationen verständlich; Seitenzahl nach didaktischem Bedarf. Kennzeichne Leserprompt, Metakasten, Profi-Anhang und Forschungsstand; teste fachfremde Lesbarkeit. Erwartete Abnahme: Quellenfeste Doppelseitenplanung und redaktionelle Freigabeliste Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Originale aus Werkarchiv beschaffen; Originalcover unverändert, Zitate mit Seite und Freigabe prüfen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund

## VP-15 · Digitale Anhänge und Website-Crosswalk

**Zweiter Versuch:** teilweise. Draft-PR und Seiten-Dateien vorhanden, kein bestätigter Browser-/Mobile-Abnahmetest

**Ursachenklasse:** partial

**Selbstprüfender Folge-Prompt:**

> Arbeite an VP-15 (Digitale Anhänge und Website-Crosswalk). Ziel: Verknüpfe die fünf Hauptprompts und Profi-Aufgaben mit stabilen IDs, Quellenakten und Ergebnissen. Prüfe Links, Originaldateien, Lizenzen und Publikationsstatus auf eigenem Branch. Verwende vorhandene Register und Diagramm-/Designregeln. Erwartete Abnahme: Validierter Navigationstest und aktualisierter Quellen-/Promptatlas Führe zuerst einen reproduzierbaren Machbarkeitstest mit realen Eingaben und Originalquellen durch. Prüfe vor jeder Neuentwicklung bestehende Datenbanken, Skills und Register. Erkenne fehlenden Zugang, fehlende Daten, unklare Begriffe und Methodenfehler getrennt. Falls ein Schritt scheitert: nenne den genauen Schritt, Fehlertyp, Quelle, benötigte Rechte und minimale ersetzende Teststrategie. Stelle keine weiteren theoretischen Vorschläge ohne Testversuch als Ergebnis dar. Formuliere danach den kleinstmöglichen Folgeauftrag mit benötigtem Input, präziser Ausgabe, Gegenprobe und Definition of Done. Gib Status 'ausgeführt', 'teilweise', 'blockiert' oder 'nicht prüfbar' aus, dazu Originalquellen, Versionen und Befunde. Erfinde keine Prüfungen, Daten oder Fristverstöße. Spezifischer nächster Schritt: Statische Link-/ID-Tests plus Desktop/Mobiltest; erst nach Review mergen

**Vorgesehene Buchdarstellung:** Offene Mitmachaufgabe, nicht als bewiesener Sachbefund
