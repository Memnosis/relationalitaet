# Bürger-KI – Deep Dive Patientenakte, souveräne KI und Datenentscheidungen

**ID:** BKI-DD-EPA-001 · **Stand:** 05.11.2026 · **Status:** Quellenbasierte Forschungsfassung, erste Primärquellen-/Anbieterprüfung; kein vollständiger unabhängiger Security-Audit, keine Produktzulassung und keine öffentlich freigegebene Nutzerberatung.  
**Gegenstand:** NUC-007–014, 031, 034–035; SW-02, SW-07, SW-16, SW-18; Übergänge WR-03–06.  
**Prinzip:** Keine Gesundheitsdaten an Bürger-KI senden. Der Deep Dive untersucht, **welche KI Menschen heute selbst einsetzen können**, was externe Dienste leisten und welche Fähigkeiten langfristig souverän bleiben könnten.

## 1. Ergebnis in Alltagssprache

Vier „Patientenakten“ dürfen nicht verwechselt werden:

| Akten-/Datenform | Zweck | Wer verwaltet | Keine Gleichsetzung mit |
| --- | --- | --- | --- |
| Praxis- oder Behandlungsdokumentation | klinische Dokumentation einer konkreten Behandlung | jeweilige behandelnde Einrichtung | ePA ist kein vollständiges Praxisarchiv |
| ePA für alle | digitale Unterlagen und Daten über Versorgungsgrenzen hinweg | gesetzlich geregeltes System, ePA-App der Krankenkasse | ungeprüfte Universal-KI oder persönliche Offline-Sammlung |
| eigene persönliche Gesundheitsablage (PHR) | privat gesammelte Dateien, Termine, Notizen | Person und gewählte Software | ePA-Zugang oder medizinisch geprüfter Dienst |
| an eine KI gegebene Kopie | Erklärung, Analyse, Strukturierung durch gewähltes Modell | abhängig von lokalem Gerät/Cloudvertrag/Anbieter | ursprüngliche Akte; Sicherheits- und Datenrechte müssen separat geprüft werden |

**Quellen:** BMG ePA (https://www.bundesgesundheitsministerium.de/themen/digitalisierung/elektronische-patientenakte/epa-fuer-alle), gematik (https://www.gematik.de/anwendungen/epa-fuer-alle), KBV/MIO (https://www.kbv.de/praxis/digitalisierung/anwendungen/elektronische-patientenakte/mio).

## 2. Akteure und ihre tatsächlichen Rollen

| Akteur | Rolle | Rolle der Quelle | Offene Prüfung |
| --- | --- | --- | --- |
| Bundesgesundheitsministerium (BMG) | Rechtsrahmen und politische Darstellung | staatliche Primärinformation | gesetzlichen Stand unabhängig nachvollziehen |
| gematik | Spezifikation der TI/ePA und öffentliche Funktions-/Sicherheitsinformationen | technische Primärquelle und Betreiberperspektive | externe unabhängige Gegenprüfung |
| Krankenkassen und Ombudsstellen | ePA-Apps und bestimmte Widerspruchswege | konkreter Nutzerzugang | Unterschiede nach Kasse/App aktuell prüfen |
| Praxen, Apotheken, andere Leistungserbringer | bestimmte Daten einstellen/abrufen im Behandlungskontext | klinische Praxisfunktion | Zugriff/Befüllung nicht pauschalisieren |
| mio42/KBV | medizinische Informationsobjekte | nationale Terminologie und Umsetzung | jeweilige Version, FHIR-Profile |
| FDZ Gesundheit / BfArM | gesetzlich geregelte Forschungsdatenbereitstellung | Datenzugang und Nutzungsbedingungen | Zeitstand, Antragsverfahren, Art der bereitgestellten Ausgaben |
| CCC / unabhängige Forschung | Sicherheits- und Fehlersuche | unabhängige Gegenperspektive | vorgebrachte Lücke, Nachweis, Reaktion und Restgefahr trennen |
| Personal-Health-Record-Projekte | private eigene Datenorganisation | Softwareangebot | Geräte-/Produktintegration und reale Nutzerfähigkeit |
| KI-Modelle/Cloudanbieter | nach gewähltem Dienst Dokumentenanalyse | externe Datenverarbeitung | Vertrags-/Trainings-/Speicher-/Drittlandbedingungen je Anbieter |

## 3. Rechte und Entscheidungen: nicht eine einzige Zustimmung

Gematik unterscheidet unter anderem Nichtanlage, Löschung bestehender ePA, Zugriff von Einrichtungen, Befüllung, Abrechnungsdaten, digital gestützten Medikationsprozess und Sekundärnutzung. Die genauen Optionen können sich nach Softwareversion und Konstellation unterscheiden. https://www.gematik.de/anwendungen/epa-fuer-alle/widerspruch

Das BMG erläutert den situativen Widerspruch gegen einzelne Dokumente und die eigene Befüllung durch Versicherte. Die Weitergabe an das FDZ für Forschungszwecke ist ein **eigener** Datenfluss: Widerspruch dagegen ist nicht gleich Auflösung der ePA. https://www.bundesgesundheitsministerium.de/themen/digitalisierung/elektronische-patientenakte/epa-fuer-alle

**Wichtige Aktualitätsfeststellung (05.11.2026):** BMG-FAQ zum FDZ beschreibt ab Oktober 2026 das Verfahren, eine Widerspruchsfrist und stufenweise technische Ausleitung ab Mitte Dezember 2026; Forschungsbereitstellung nach Qualitätssicherung in 2027. Das FDZ gibt voraussichtlich Ende 2026/Anfang 2027 an. Nicht als bereits flächendeckend vollzogene Forschungsausleitung ausgeben. https://www.bundesgesundheitsministerium.de/themen/gesundheitswesen/forschungsdatenzentrum-fdz-gesundheit-fragen-und-antworten , https://www.forschungsdatenzentrum-gesundheit.de/infoportal/datensatz-des-fdz-gesundheit/daten-aus-der-epa

**Methodischer Vorbehalt:** Die Behördenaussage zu Pseudonymisierung, Antrags-/Sicherheitsverfahren und aggregierten Ausgaben ersetzt keine unabhängige Reidentifikations- und Security-Analyse. Die konkrete Risikobewertung bleibt ein eigener Deep Dive.

## 4. Gegenwärtige echte Produkt-/Open-Source-Landschaft

| Angebot/Projekt | Ist für wen? | Nachgewiesene Funktion | Wichtige Grenze | Quelle |
| --- | --- | --- | --- | --- |
| ePA-App der Krankenkasse | Versicherte | persönliche Akte einsehen, selbst befüllen, Rechte nutzen | keine allgemeine KI-Verarbeitung garantiert | BMG/ePA |
| MyGNUHealth | einzelne Nutzer | freie persönliche Gesundheitsdokumentation, GPLv3+ | nicht als ePA-Client oder klinisch zugelassene Anwendung voraussetzen | https://docs.gnuhealth.org/mygnuhealth/ |
| Open Health Stack Android FHIR SDK | Entwickler/Projekte | FHIR-R4-basiertes SDK, Offline-Datenmodelle, Formulare, Workflows, lokale Berechnungen | keine fertige Patienten-App für deutsche ePA, nicht automatisch klinisch geprüft | https://developers.google.com/open-health-stack/android-fhir |
| Doctolib Patientenangebot | Personen mit teilnehmenden Praxen | Buchung und von Praxen geteilte Dokumente im Patientenbereich | Warteliste nur für bereits gebuchten geeigneten Termin; keine universelle Psychotherapie-Platzsuche | https://doctolibpatient.zendesk.com/hc/de/articles/360025466873-Meine-Dokumente-aufrufen und https://www.doctolib.de/gesundheit/waiting-list/ |
| Lokale KI auf eigenem Gerät | technisch geeignete Nutzer | je nach Software Textverarbeitung ohne zwingenden Cloud-Upload möglich | Modellqualität, Gerätesicherheit, Ressourcen, Updates und medizinische Eignung ungeprüft | konkrete Produktvergleiche **offen** |
| Cloud-KI | Nutzer eines gewählten externen Dienstes | Dokumenten- und Textarbeit je nach Produkt | konkrete Speicherung, Training, Rechte, Datenschutz, Verlässlichkeit **anbieterbezogen offen** | verbindliche Tarif-/Daten-/Vertragsprüfung offen |

**Nicht gleichsetzen:** „Open Source“ bedeutet Quellcodezugang, nicht automatische Datensicherheit, ePA-Berechtigung oder ärztlich geprüfte Therapieentscheidung. „Cloud-KI“ bedeutet nicht pauschal, dass alle Anbieter Trainingsdaten auf dieselbe Weise nutzen.

## 5. Standards und Code: technische Übersetzbarkeit prüfen

- **HL7 FHIR:** Daten-/Austauschstandard, verschiedene Releases und Profile; R5 ist als FHIR-Release publiziert, während große Implementierungen R4 einsetzen. Immer `FHIR release` und `Implementation Guide` angeben. Quelle https://www.hl7.org/fhir/directory.html.
- **MIOs / mio42:** medizinische Informationsobjekte für nationale interoperable Gesundheitsinformationen. KBV stellt Spezifikationen und einen aktuellen Status/Kommentierungsprozess bereit. Quelle https://www.kbv.de/praxis/digitalisierung/anwendungen/elektronische-patientenakte/mio.
- **FHIR in KI-Code:** ein strukturiertes Objekt oder ein syntaktisch valides Dokument kann fachlich unangemessene Angaben enthalten. `MedicationStatement`, `Observation`, `Condition` etc. sind Datenklassen mit Provenienz-/Interpretationsbedarf, kein automatisch durch Code bestimmter klinischer Schluss.
- **Terminologie-Tiefenprüfung offen:** SNOMED CT, ICD-10-GM, LOINC, UCUM, IHE-Profile, MIOs und nationale FHIR-IG-Versionen müssen am konkreten Verwendungsszenario, an Lizenz und Modellvalidierung untersucht werden.

**Forschungsübergang zum Tensor:** Quelle → Begriff/Terminologie → Datenmodell → Regel/Code → klinische Interpretation (durch Fachprüfung) → Test/Gegenbeispiel → Skill → verständliche Erklärung. **Keine Behauptung**, dass ePA-Daten in diesem Projekt bereits importiert, analysiert oder als Tensoren bewiesen wurden.

## 6. Sicherheitsvorfälle: historische Feststellung, Betreiberreaktion, offener Status

KBV dokumentierte am 30.01.2025 CCC-beschriebene Schwachstellen und die damals laufenden Gegenmaßnahmen: https://www.kbv.de/praxis/tools-und-services/praxisnachrichten/2025/01-30/Schwachstellen%20bei%20der%20ePA-%20Hinweise%20zur%20Datensicherheit. Die gematik gab am 30.04.2025 die Schließung einer bestimmten Sicherheitslücke an und beschreibt zusätzliche Sicherheitsmaßnahmen: https://www.gematik.de/newsroom/news-detail/aktuelles-epa-sicherheitsluecke-geschlossen .

Die korrekte Sprache lautet: **Sicherheitsforscher beschrieben Angriffspfade; der Betreiber berichtet über Maßnahmen; eine unabhängige heutige Gesamt-Sicherheitsaussage folgt daraus nicht.** Weitere Vorfälle und technische Details nur nach eigener Primär-/Gegenquellenprüfung.

## 7. Der einmalige Stern am richtigen Punkt

Nur wenn jemand ausdrücklich die Handlung „**Eigene Unterlagen mit KI analysieren**“ wählt, erscheint `*` als dezenter Zugang zu einer einmaligen übersichtlichen Entscheidungskarte:
1. Nutze ich eigene lokale Software oder eine externe Cloud?
2. Welche Daten übertrage ich bewusst und an wen?
3. Welche Bedingungen zu Speicherung, möglicher Weiterverarbeitung, Zugriff und Löschung gelten für **diesen** Anbieter?
4. Ist eine automatische medizinische Schlussfolgerung überhaupt der Zweck der Software?
5. Kann ich eine begrenzte, datensparsame Anfrage oder ein unabhängiges persönliches Werkzeug wählen?
6. Welche allgemeinen Datenschutz- und ePA-Rechte sind getrennt zu betrachten?

**Keine wiederholte Warnbox in jeder Wissenswelt.** Eine bloße verlinkte Info braucht keine eigene KI-Anlage. Wenn Bürger-KI selbst Daten übermittelt, verarbeitet oder speichert, entsteht ein eigener rechtlicher und technischer Dienst mit weitergehenden Pflichten; Sternchen ersetzt diese nicht.

## 8. Offene Fragen und priorisierte nächste Quellenarbeit

**P0:** Anbieterbezogene KI- und lokale-KI-Vergleiche (Nutzung, Kosten, Datenorte, Rechte, Modellausgabe); ePA-App-/Versichererunterschiede; klinische Geltungsgrenzen; nationale FHIR-Profile und Standards in der tatsächlichen Akte.

**P1:** Open-Source-PHR-Zugänglichkeit und Pflegezustand; differenzierte Sicherheitschronologie einschließlich Gegenprüfung; unabhängige Verbraucher-/Datenschutzanalysen; Datenzugriff aus Drittsoftware ohne Marketinggleichsetzungen.

**P2:** Konkreter Test mit ausschließlich synthetischen FHIR-Proben, um zu zeigen, wie KI Begriffssinne verliert oder bewahrt; Vergleich von lokalen/externen KI-Werkzeugen mit genau definierten, nicht klinischen Testfällen.

## 9. Vorschlag für redaktionelle Ausgabe – erst nach Quellenabnahme

**Haupttitel:** „Meine Gesundheitsunterlagen – welche Möglichkeiten habe ich?“  
**Sofort sichtbar:** ePA, eigener Ordner und private/Cloud-KI als getrennte Verwendungswege.  
**Kompakte 2–3 Quellen:** gematik Widerspruch / BMG ePA / unabhängige fachliche Sicherheits- oder Patienteninformation; Links je Abschnitt nach tatsächlichem Zweck.  
**Details:** „Was sehen andere?“, „Was darf eine KI?“, „Welche Standards gibt es?“, „Was ändert eine Forschungsnutzung?“.  
**Einmaliges Sternchen:** nur bei der Daten-/KI-Handlung, nicht als allgemeiner Seiten-Disclaimer.  
**Externe Handoffs:** Versicherer-ePA, gematik, FDZ, eigenständig gewähltes PHR-/Open-Source-Angebot.  
**Deep Dive:** dieses Paper und weiterführende Quellen-/Versionstabellen.

**Freigabestatus:** Dieses Paper ist die Forschungsgrundlage, kein selbst betriebener Gesundheitsdienst. Die öffentliche Entscheidungsseite folgt erst nach fachlicher, technischer und redaktioneller Prüfung.
