# SOULution · Vorpublikations-Prüfprogramm v0.1
Stand: 2026-11-03 · Pilot SVIK und laufender Entscheidungsmonitor

## Verbindliche Reihenfolge
1. Quellen und Datenzugänge tatsächlich prüfen, historisches Fristenregister als Ground Truth bilden.
2. Einzelaufgaben ausführbar testen, Nachweise und Gegenproben dokumentieren.
3. Zwei Prompt-Durchläufe auf identischer Testmenge vergleichen.
4. Erst dann didaktisch ausreichende Publikation mit Originalcovern und belegten Auszügen neu ausarbeiten. Umfang nach Bedarf, keine feste Seitenobergrenze.

## Fachliche Regeln
- Status: offen | in_arbeit | blockiert | getestet | reproduziert | validiert.
- Quellenstatus gesondert: entdeckt | erreichbar | abgerufen | gelesen | maschinell verarbeitet | unabhängig reproduziert.
- Rechtsstatus: nicht_faellig | faellig | fristgerecht_belegt | verspaetet_belegt | nicht_gefunden | angefragt | abweichung_belegt | geaendert.
- Ursprungsfassung, Stichtag und Aussageebene stets festhalten. Ein fehlender öffentlicher Nachweis ist kein Beweis eines Rechtsverstoßes.
- SOULution, KI-Tensor und Mini-KI nutzen gemeinsame Register, aber getrennte fachliche Tests.
- Keine Veröffentlichung als abgeschlossene Studie vor dokumentierter Abnahme.

## Aufgaben und direkt verwendbare Arbeits-Prompts

### VP-01 · Historischer Evaluierungs- und Fristenatlas
**Priorität:** P0  
**Quellen:** NKR-Berichte, Gesetze und Evaluationsberichte  
**Prompt:** Extrahiere aus drei datierten NKR-Berichten eine quellengenaue Stichprobe von mindestens 10 einzeln identifizierbaren Evaluierungspflichten. Erfasse Rechtsbasis, zuständige Stelle, Fristauslöser, Fälligkeit, tatsächliche Durchführung, Bericht/Übermittlung, Publikationsdatum, Verfügbarkeit und Änderungen. Trenne nicht auffindbar von verspätet belegt und von nicht fällig. Berechne nur bei nachgewiesenem Nenner eine Fristquote.  
**Abnahme:** 10 Fallakten mit Quellen und Datumslogik; mindestens 2 vollständig rückverfolgt  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-02 · Fristenregelmaschine und Negativtests
**Priorität:** P0  
**Quellen:** Rechtsquellen, Datumsereignisse, VP-01  
**Prompt:** Entwirf eine maschinenlesbare Fristenregel für die Fälle aus VP-01. Prüfe Inkrafttreten, Übergangsrecht, Friständerung, Durchführung, Übermittlung und Veröffentlichung getrennt. Teste 6 Gegenfälle einschließlich noch nicht fällig, nicht veröffentlicht aber durchgeführt, geändert, aufgehoben, verspätet und unbekannt.  
**Abnahme:** 6 reproduzierbare Tests mit richtigem Status und Beleg  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-03 · Laufende Entscheidungen und Änderungsmonitor
**Priorität:** P0  
**Quellen:** DIP, Bundestagsdrucksachen, ausgewählte Regierungsseiten  
**Prompt:** Prüfe die tatsächliche maschinenlesbare Abrufbarkeit aktueller Verfahrensdaten. Erfasse eine begrenzte Menge neuer/geänderter Vorgänge samt ID, Zeitstempel, amtlicher Quelle und Version. Simuliere mindestens zwei aufeinanderfolgende Abrufe und dokumentiere echte Differenzen ohne erfundene Ereignisse.  
**Abnahme:** Datenabruf, Schema, Deltaprotokoll und Fehlerfall  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-04 · SVIK-Rechts- und Zuständigkeitskette
**Priorität:** P0  
**Quellen:** GG, SVIKG, LuKIFG, BMF, Bundestag  
**Prompt:** Ermittle für SVIK jede einschlägige Pflicht und Zuständigkeit mit genauer Normfassung, Fristauslöser, Adressat, Berichtsempfänger und Kontrollbefugnis. Trenne Rechtspflicht, verwaltungsinternen Standard und Forschungsforderung.  
**Abnahme:** Quellengebundene Verantwortungs- und Pflichtmatrix  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-05 · SVIK-Datenzugang und Dateiverarbeitbarkeit
**Priorität:** P0  
**Quellen:** Bundeshaushalt-Bundesdashboard, Länderdashboard, KTF  
**Prompt:** Versuche die amtlichen Downloads tatsächlich herunterzuladen. Dokumentiere URL, Zugangsbedingungen, MIME-Format, Dateihash, Datenjahr, Spalten, Metadaten, Lizenz und maschinelle Lesbarkeit. Trenne öffentlich genannt, erreichbar, heruntergeladen und erfolgreich geparst.  
**Abnahme:** Mindestens je 1 belastbarer Datensatz für Bund, Länder und KTF ODER dokumentierter Blocker  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-06 · Finanzfluss Plan–Ist–Bindung–Empfänger
**Priorität:** P0  
**Quellen:** SVIK-Datensätze und Haushaltspläne  
**Prompt:** Rekonstruiere die drei Finanzierungssäulen und einen ausgewählten Haushaltstitel mit Ermächtigung, Soll, Bindung, Ist, Erstattung, Empfänger und Leistungsstand. Rechne Summen und Doppelzählungen gegen. Lege für nicht verfügbare Endempfängerdaten explizite Lücken an.  
**Abnahme:** Reproduzierbare Finanzflussakte und Nachrechnung  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-07 · Zusätzlichkeit: Methoden- und Gegenvergleich
**Priorität:** P0  
**Quellen:** BMF-Analyse, IW-Analyse, Haushaltsdaten  
**Prompt:** Rekonstruiere beide öffentlich verwendeten Zusätzlichkeitsdefinitionen mit Jahren, Bezugsgrößen, Gegenmodellen und Quellen. Prüfe die Rechenwege soweit verfügbar. Stelle Prozentwerte erst bei identischem Nenner einander gegenüber; andernfalls erkläre den Unterschied.  
**Abnahme:** Methoden-Crosswalk, Rechenversuch, Grenzen  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-08 · Ziele–Meilensteine–Output–Wirkung
**Priorität:** P0  
**Quellen:** BMF-Monitoring, Fachressorts, Evaluationen  
**Prompt:** Wähle einen konkreten SVIK-Haushaltstitel. Verbinde Mittelabfluss, definierte Zielindikatoren, Meilensteine, nachgewiesenen Output, Outcome und Impact. Prüfe welche Indikatoren nur Planungsfortschritt abbilden und ob Vergleiche zwischen Fachbereichen zulässig sind.  
**Abnahme:** Eine vollständige Musterakte oder transparent belegte Lücken  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-09 · Prüf- und Kontrollqualität
**Priorität:** P1  
**Quellen:** NKR, Bundesrechnungshof, Bundestag, Fachministerien  
**Prompt:** Ordne für eine Stichprobe von mindestens fünf Maßnahmen Rechtskontrolle, Mittelverwendungsprüfung, Evaluation, unabhängige Prüfung und Nachsteuerung zu. Prüfe Veröffentlichung, Frist, methodische Qualität und dokumentierte Folgen getrennt.  
**Abnahme:** 5 Kontrollketten mit Nachweisstatus  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-10 · Lösungs- und Alternativenatlas
**Priorität:** P1  
**Quellen:** Vorhandene amtliche und wissenschaftliche Werkzeuge  
**Prompt:** Identifiziere vorhandene Monitoring-, Evaluations- und Datenwerkzeuge, ihre Schnittstellen, Lizenzen und Grenzen. Vergleiche zwei Verbesserungsvorschläge anhand der festgestellten Lücken statt ein paralleles Dashboard vorauszusetzen.  
**Abnahme:** 2 belegte Lösungen plus Integrationsempfehlung  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-11 · Prompt-Benchmark und zwei Durchläufe
**Priorität:** P0  
**Quellen:** VP-01 bis VP-10 Ergebnisse  
**Prompt:** Führe H1–H5 sowie die professionellen P01–P08 auf demselben eingefrorenen Quellenstand aus. Vergleiche Vollständigkeit, Datenverfügbarkeit, Fehler, prüfbare Aussagen, Aufwand und wiederverwendbare Datenobjekte. Wiederhole den Test nach Prompt-Optimierung mit gleicher Testmenge.  
**Abnahme:** Vorher/Nachher-Testmatrix samt Quellen, Fehlerklassen und Nachprüfungen  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-12 · Gemeinsame Skill- und Datenbank-Wiederverwendung
**Priorität:** P0  
**Quellen:** Existierende Git-Register, Inventar, historische Bestände  
**Prompt:** Ordne jedem benötigten Skill und Datentyp eine existierende Quelle oder einen belegten Fehlbestand zu. Unterscheide on_git, local_only, Kandidat, ausführbar, getestet und validiert. Vermeide neue Kopien gemeinsamer Quellenobjekte.  
**Abnahme:** Crosswalk und 3 kleine ausführbare Skilltests oder begründete Blocker  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-13 · Relations- und Tensorübergabe
**Priorität:** P1  
**Quellen:** Geprüfte Befunde VP-01 bis VP-12  
**Prompt:** Extrahiere nur quellengebundene, typisierte Relationskandidaten mit Träger, Definition, Geltung, Test und Gegenbeispiel. Prüfe vorhandene Tensorregister auf Duplikate. Gib Kandidaten an KI-Tensor weiter; bestätige keinen 3×3×3-Tensor ohne drei geprüfte Trinitäten und 27 geprüfte Feldpositionen.  
**Abnahme:** Relationsakten, kein erfundener Tensorabschluss  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-14 · Buchbelege, Originalcover und Didaktik-Abnahme
**Priorität:** P0  
**Quellen:** Originalbücher, validierte Testakten  
**Prompt:** Sichere Originalcover und exakte Buchauszüge mit Seitenangaben. Leite nur geprüfte Zahlen und Beispiele in den Haupttext ab. Erkläre notwendige Relationen verständlich; Seitenzahl nach didaktischem Bedarf. Kennzeichne Leserprompt, Metakasten, Profi-Anhang und Forschungsstand; teste fachfremde Lesbarkeit.  
**Abnahme:** Quellenfeste Doppelseitenplanung und redaktionelle Freigabeliste  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

### VP-15 · Digitale Anhänge und Website-Crosswalk
**Priorität:** P1  
**Quellen:** Vorhandene SOULution-Seite, Mitmachen, Git-Register  
**Prompt:** Verknüpfe die fünf Hauptprompts und Profi-Aufgaben mit stabilen IDs, Quellenakten und Ergebnissen. Prüfe Links, Originaldateien, Lizenzen und Publikationsstatus auf eigenem Branch. Verwende vorhandene Register und Diagramm-/Designregeln.  
**Abnahme:** Validierter Navigationstest und aktualisierter Quellen-/Promptatlas  
**Status:** offen; bisherige Recherche ersetzt keinen Test.

## Go/No-Go der Buchproduktion
Pflicht: VP-01 bis VP-08, VP-11, VP-12 und VP-14 müssen zumindest mit realen Quellen/Daten testweise durchlaufen sein; Fehlschläge sind erlaubt, aber als solche belegbar. VP-09, VP-10, VP-13 und VP-15 dürfen offene Anschlussaufgaben enthalten, wenn Grenzen im Buch nicht als Befunde ausgegeben werden. Jede Zahl und jedes Originalzitat benötigt genaue Fundstelle und Stichtag.
