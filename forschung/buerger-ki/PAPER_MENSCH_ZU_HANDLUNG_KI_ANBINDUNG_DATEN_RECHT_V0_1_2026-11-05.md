# Bürger-KI – Vom Anliegen zu Handlung, Begleitung und öffentlicher Erkenntnis
## Sprach- und Pfadübergänge, soziale Mikrokosmen, optionale KI, Datenflüsse, rechtliche Grenzen und Betreiberperspektive

**Paper:** BKI-LIFE-CYCLE-001 · **Stand:** 2026-11-05 · **Version:** 0.1 · **Status:** Forschungs- und Betriebsmodell; keine Freigabe für Personen-/Gesundheitsdatenerhebung oder medizinische/individuelle Beratungsfunktion.  
**Anschluss:** [Sprachprojekt](./SPRACHPROJEKT_PFADGRAMMATIK_UEBERSETZBARKEIT_WISSENSRAEUME_V1_2026-11-05.md), [Elementinventar](./SPRACHPFADE_ELEMENTINVENTAR_V0_1.json), [Gesamtarchitektur](./MASTERPLAN_ARCHITEKTUR_LERNPFADE_CROSSWALK_SKILLS_V1_2026-11-05.md), [bestehendes Impressum/Datenschutz](../../docs/impressum.html).

## Abstract – Die eigentliche Anschlussfrage

Die Website ist keine eigenständig beratende KI. Das Projekt entwickelt Fähigkeiten, Beziehungs- und Forschungsformen. Die zentrale Frage lautet nicht „Welche weiteren Seiten bauen wir?“, sondern: **Was kann ein Mensch nach der richtigen Erkenntnis tun, was macht er allein oder gemeinsam, wer hält den Faden später wieder auf, und welche öffentlichen Ergebnisse entstehen daraus?** Dabei dürfen Interesse, Kontaktaufnahme, Teilnahme, medizinische Unterlagen, persönlicher Fortgang und Forschungsbeitrag nicht zu einem unkontrollierten gemeinsamen Datenbestand verschmelzen. Dies ist eine Entwurfsentscheidung und keine Aussage über bestehende technische Dienste.

## 1. Fünf voneinander getrennte Betriebsräume

| ID | Raum | Tatsächliches Leistungsversprechen | Daten beim Projekt | Status |
| --- | --- | --- | --- | --- |
| BKI-SRV-01 | Öffentliches Wissen | Bedeutung, exakte Quellen, 2–3 passende Links, Perspektiven | keine vom Projekt angelegten Bürgerfallakten; technisch notwendige Hostingdaten beim Betreiber des Hostings | heute grundsätzlich möglich |
| BKI-SRV-02 | Selbsthilfe-Werkzeuge | Suchplan, Gesprächsvorbereitung, lokal exportierbares Protokoll und Kalenderhinweis | bei lokaler Benutzung keine Übermittlung des Inhalts an Projektserver; Hosting-/Browserdaten separat | zu entwickeln |
| BKI-SRV-03 | Gemeinsame Unterstützung | öffentlich angekündigte Treffen, Such-Kaffeekränzchen, freiwillige Kontaktaufnahme, moderierte Austauschformate | nur bei freiwilliger Teilnahme erforderliche Kontaktdaten; Veranstalter/Verantwortlichkeit festzulegen | eigenständiger optionaler Dienst |
| BKI-SRV-04 | Persönliche Begleitung | privater Terminplan, Erinnerung, Unterlagenübersicht, ggf. KI-Verarbeitung bei ausdrücklicher Auswahl | entweder lokal / bei separatem vertrauenswürdigen Anbieter oder neuer gesicherter Spezialdienst | hochsensibler, nicht implementierter Forschungszweig |
| BKI-SRV-05 | Öffentliche Forschung | allgemeine Erkenntnisse aus Primärquellen, dokumentierten Projekttests und freiwillig freigegebenen methodischen Hinweisen | grundsätzlich keine persönlichen Fälle; getrennt geregelte Forschung nur nach Einwilligung, Methodik und Prüfung | bereits Forschungsbestände; neue Beteiligung offen |

**Trennregel:** Ein Mensch darf eine Quelle lesen, ein Treffen besuchen oder selbst ein Exportdokument erzeugen, ohne sich bei Bürger-KI registrieren oder Gesundheitsdaten abgeben zu müssen. Kontakt zu einer Initiative ist kein Einverständnis mit wissenschaftlicher Auswertung oder Veranstaltungswerbung. Eine E-Mail-Adresse ist keine pauschale Erlaubnis für spätere personenbezogene Umfragen.

## 2. Sprachraum- und Pfadübergänge: wirkliche Dreh- und Angelpunkte

Die vorhandenen `LP-01..05` und die fünf Therapieplatzlinsen `ziel/wissen/hilfe/gesellschaft/forschung` bleiben die Navigationsidentitäten. Zwischenstufen sind dagegen *Entscheidungstore*, an denen Sprache, Zweck und mögliche Datennutzung wechseln.

| Übergang | Ankunftsfrage | Nötige sprachliche Übersetzung | Neue Welt / Aktion | Grenze |
| --- | --- | --- | --- | --- |
| W01 `ziel→wissen` | „Was meine ich mit Therapieplatz?“ | gewünschte Veränderung → Indikation, Sprechstunde, Probatorik, Behandlung | Begriffs- und Quellenwelt | keine Diagnose aus einem Wunsch |
| W02 `wissen→hilfe` | „Wen kontaktiere ich?“ | Fachkategorie → konkrete Angebotsart, Suchweg und Voraussetzungen | ausgewählte Links, Suchcheckliste | Terminvermittlung ≠ garantierte Behandlung |
| W03 `hilfe→selbst-handeln` | „Beginne ich wirklich?“ | Angebotsinformation → eigener, kleiner Arbeitsschritt | lokale Suchliste, Termintelefonat, Export | keine Website-Automatik behaupten |
| W04 `allein→gemeinsam` | „Ich kann mich nicht aufraffen“ | Eigenmotivation → freiwilliger gegenseitiger Organisationsrahmen | Kaffeekränzchen/Suchtreff | kein therapeutisches Gruppensetting vortäuschen |
| W05 `kontakt→dokumentieren` | „Was habe ich versucht?“ | flüchtige Erfahrung → strukturierte eigene Aufzeichnung | lokale Checkliste, Kalendereintrag | private Akte nicht automatisch als Forschungsdatenbank |
| W06 `angebot→passung` | „Ist das für mich sinnvoll?“ | Termin/Angebot → Eignung, fachliche Einschätzung und eigene Präferenzen | Therapieformen verstehen, Erstgesprächsfragen | keine automatisierte Therapiezuweisung |
| W07 `keine-lösung→minderung` | „Was kann ich bis dahin tun?“ | Ergebnislücke → Alternativen, akute Bedarfe, Unterstützung | Schadensbegrenzung/geeignete Hilfswege | Grenzen und Notfälle fachlich getrennt behandeln |
| W08 `persönlich→gesellschaftlich` | „Wiederholt sich dieses Hindernis?“ | individuelle Erfahrung → Forschungsfrage mit Population/Zeitraum/Nenner | Meta- und Evidenzwelt | kein Schluss aus Gruppe auf Repräsentativität |
| W09 `austausch→mitwirkung` | „Wie machen wir etwas sichtbar?“ | Gespräch → freiwillige, verantwortbare Beteiligung | öffentliche Veranstaltung, Petition, Fachgespräch | Teilnehmende weder exponieren noch zu Gesundheitsangaben drängen |
| W10 `weiterentwicklung→rückweg` | „Hat sich etwas geändert?“ | neue Quelle/Skill → erneute Orientierung | Quellenänderung, optionaler Sachnewsletter | kein heimliches Gesundheitsprofil/„Nudging“ |

**Übersetzungsprotokoll:** pro Kante `from_element`, `to_element`, `input_claim`, `retained_meaning`, `added_assumptions`, `non_equivalence`, `source_refs`, `possible_action`, `data_flow_id`, `review_status`. Ohne geprüfte Quellen keine fachliche Schlussfolgerung; ohne konkrete nachfolgende Erklärung kein verführerischer Klapptext.

## 3. Welche Wissensräume sind aus dem Bestand heraus möglich?

| Wissensraum | Darstellungsform | Vorhandener Anker | Was noch fehlt |
| --- | --- | --- | --- |
| Begriffe der Psychotherapie | kleine `details`-Karte, Definitionsvergleich | Therapieplatz-Manifest, Lexikon | Primärdefinitionen mit Zeit-/Rechtsraum und fachlicher Abnahme |
| So finde ich einen passenden Suchweg | Handlungsbox mit 2–3 Quellen | 116117, Therapie-Linse Hilfe | Aktualitätscheck, notwendige Sonderbedingungen, Alternativen |
| Kontaktprotokoll | lokal druck-/exportierbares Formular ohne Upload | Ziel- und Wegemodelle | nutzerfreundlicher Entwurf, Offline-Verhalten, Browser-/TDDDG-Prüfung |
| Such-Kaffeekränzchen | kurze eigene Themenseite mit Ablauf, Grenzen, Moderation | `buerger-ki-gemeinsam.html` enthält „Gemeinsam an einem Tisch“ | organisatorische Zuständigkeit, Sicherheit, keine Gruppentherapie, Veranstalterdaten |
| Meine Unterlagen | Ausklappbare Übersicht + Hinweis auf ePA | aktuelles Gesundheits-/Versorgungsthema | keine Bürger-KI-ePA-Integration behaupten; Eignung lokaler Exportformate prüfen |
| Therapieformen/Passung | eigenständige Fachthemenseite, fachliche Vergleiche | Gesundheitsquellen, Therapieplatz-Daten | Leitlinien, fachliche Evidenz, keine automatische medizinische Auswahl |
| Wenn es kein Angebot gibt | kleiner Kerntext + tiefe Quellenwelt | Versorgungs-/Blindstellen-Paper | nach Region/Bedarf differenzierte, aktuelle Fachquellen und klare Grenzen |
| Gemeinsame Rechenschaftsfrage | Metaknoten + Paper/Quellenpfad | Gesellschaft/Institutionelles Lernen/Beweisakten | Ursachen- und Wirkungskriterien, unterschiedliche Rechtsräume |
| Zukunft der Therapie | eigenes Forschungs-Deep-Dive, keine Versorgungszusage | Forschungsbibliothek, Skills | Therapieforschung, Stand, Unsicherheit, Abgrenzung von spekulativen Ansätzen |
| Freiwillige öffentliche Beteiligung | getrennte Veranstaltungs-/Newsletterseite | Werkstatt, Mitmachansätze | rechtlicher Zweck, Kontaktliste/Einwilligung/Abmeldemechanismus |

**Gestaltungsregel:** Ein Klappelement braucht eine reale neue Antwort, ein nachvollziehbares Beispiel, Bedingungen, eine Quelle, einen Rückweg und eine wirkliche Tiefe. Ganze Fachwelten gehören auf Themenseiten mit eigenem fachlichen Eigentümer; die Klappe öffnet einen verständlichen Ausschnitt und die 2–3 exakt passenden Links, nicht eine versteckte Linkhalde.

## 4. Der vollständige Therapieplatz-Fall: mögliche Abzweigungen

1. **Nur verstehen:** Was heißt „Therapieplatz“? → Quellen, Unterschiede, keine Registrierung.
2. **Sofort etwas tun:** Suchwege, Sprechstunde/116117 und individuelle Kontaktaufnahme → lokale Checkliste.
3. **Nicht allein aktiv werden:** freiwillig organisiertes Suchtreffen. Gemeinsam motivieren und öffentliches Praxiswissen austauschen; jeder entscheidet selbst über persönliche Gespräche und Dokumentation. Keine unbefugten Anrufe für Dritte, keine automatische Gruppenoffenlegung.
4. **Eigene Übersicht führen:** Kontakte und Termine in eigener Datei oder Kalender. Die offizielle ePA besteht unabhängig von Bürger-KI.
5. **Geeignete Behandlung auswählen:** fachliche Beratung und persönliche Präferenzen, Informationen über Behandlungsformen; kein automatisches KI-Therapierezept.
6. **Keine Versorgung gefunden:** sorgfältig belegte Alternativen, Zwischenunterstützung und ggf. dringliche Versorgungsmöglichkeiten; keine unbelegte Garantie.
7. **Gemeinsam über Versorgung sprechen:** Forschung über öffentliche Kapazitätsdaten/Definitionen, moderiertes Gespräch, danach ggf. gezielte Fragen an verantwortliche Institutionen.
8. **Öffentliche Beteiligung:** freiwilliges Treffen, Fachdialog oder Aktion, bei der Teilnahme nicht als Patientenstatus veröffentlicht werden muss.
9. **Langfristig wiederkommen:** öffentliches Forschungsupdate oder freiwillig bestellte Information; persönliche Erinnerungen sind ein anderer Dienst.
10. **Wirkung überprüfen:** Was änderte sich wirklich? Nicht Nutzeraktionen/Emails/Anmeldungen zählen statt Ergebnis und fachlichem Nutzen.

## 5. Datenflüsse und Betreiberverantwortung: vier getrennte Varianten

**A. Keine projektseitige Erhebung:** Statische Seiten und Links. Hosting protokolliert technische Verbindungsdaten; vorhandene `docs/impressum.html` beschreibt GitHub-Pages/weitere Zugriffe. Keine durch das Bürger-KI-Projekt angelegte Fallakte.

**B. Lokaler Export:** Ein HTML-Tool erzeugt z. B. Kontakt-/Suchplan oder Kalenderdatei im Browser. Kein automatisches Senden an den Projektbetreiber; nur ausdrücklich ausgelöster Export. Lokale Speicherung/Endgerätezugriff und zugrunde liegende technische Risiken sind separat zu prüfen (TDDDG §25). Auch lokal bedeutet nicht automatisch „sicher“.

**C. Freiwillige Kontaktliste:** Nur E-Mail-Adresse, eng umrissene Zwecke, Nachweis der Einwilligung und Abmeldemöglichkeit; bei regelmäßigem Newsletter/Veranstaltungseinladungen getrennte Zweckwahl und Double-Opt-in als dokumentierbarer Nachweis. Keine Pflichtangabe einer Diagnose und kein automatisches Mitführen des behandelten Webthemas. Die Betreiberorganisation ist Verantwortliche für diesen Kontaktzweck; Anbieter/Empfänger/Speicherfristen vorher spezifizieren.

**D. Persönlicher Gesundheits-/KI-Dienst:** getrennte hochsichere Anwendung oder bestehender vertrauenswürdiger Dienst mit nachvollziehbarer Verantwortlichkeit, Authentifizierung, Verschlüsselung, Berechtigung, Löschung, Export, Betriebs-/Missbrauchskonzept, Rechtsgrundlage und regelmäßig erforderlicher Prüfung einer Datenschutz-Folgenabschätzung. Gesundheitsdaten sind besondere Kategorien gemäß Art. 9 DSGVO. Hierfür reichen vorhandenes statisches Hosting und dessen Datenschutzhinweise nicht.

### Daten- und Output-Matrix

| Tätigkeit | Minimale Eingabe | Speicherort | Output | Freigabeschwelle |
| --- | --- | --- | --- | --- |
| Wissensseite lesen | URL-Anfrage | Hosting-Protokolle | Quellen/Lernweg | vorhanden |
| Checkliste verwenden | lokal eingegebene Kontaktzeit / gewünschte Aufgabe | nur lokal, wenn technisch so umgesetzt | ausdruckbare Liste, freiwilliger ICS-Export | Browser- und Datenschutztest |
| Kaffeekränzchen besuchen | ggf. freiwillige RSVP-Adresse | eigener Veranstalter-/Anmeldedienst | Ort/Zeit, Ablauf, Regeln | separates Veranstalter-/Datenkonzept |
| E-Mail-Updates erhalten | E-Mail + Zweckwahl | separater Verteiler | thematisches Update oder Einladung | Datenschutztext + Einwilligungsnachweis |
| Persönliche Unterlagen verwalten | Dokumente/Befunde | **nicht** im jetzigen Bürger-KI-Repo | Übersicht, Terminplanung | eigener Dienst und Sicherheits-/Rechtsreview |
| Persönliche KI nutzen | aktiv ausgewählte Frage/Dokumente | ausdrücklich gewählter KI-Dienst | Entwurf/Erklärung, keine Diagnosegarantie | Anbieter-/Datenfluss-Review |
| Forschungsbeitrag einreichen | methodischer Hinweis + benannte Einwilligung, ggf. vorab anonymisierte Angaben | getrennte redaktionelle Eingangsstelle | geprüfter Quellen-/Testkandidat | Moderation, Schutz vor Reidentifikation |
| Öffentliche Studie | überprüfte öffentliche Quellen und definierte Forschungsdaten | Forschungsregister | Ergebnis, Gegenbeispiel, Paper | methodische und rechtliche Abnahme |

## 6. Medizin- und Produktgrenzen

Die ePA wird nach gesetzlichen Vorgaben über die Telematikinfrastruktur und die Apps der Krankenkassen zugänglich gemacht. Bürger-KI kann verlässlich erklären, wie Menschen ihre eigene ePA nutzen, aber nicht behaupten, sie direkt aus dem statischen Webangebot anzulegen oder darauf zuzugreifen.

Eine bloße Such- oder Dokumentationshilfe ist nicht schon deshalb ein Medizinprodukt, weil Gesundheit Thema ist. Sobald Software nach ihrer Zweckbestimmung beispielsweise diagnostisch/therapeutisch entscheidet, überwacht oder dosiert, können Medizinprodukterecht und ggf. weitere Anforderungen greifen. Beim BfArM ist die konkrete Zweckbestimmung entscheidend. **Keine Behandlungsempfehlungsengine als Nebenprodukt des Übersetzungs-Skills einführen.**

Gesundheitliche Termine als bloße vom Nutzer selbst eingetragene Erinnerungen sind anders einzuordnen als eine KI, die aus Befunden individuell notwendige Untersuchungsintervalle ableitet. Letzteres ist medizinische Entscheidungsunterstützung und fachlich/produktrechtlich neu zu prüfen.

## 7. Rechtsprüfung vor jeder Erweiterung

**Für das aktuelle Angebot:** `docs/impressum.html` besitzt Impressum/Datenschutzabschnitte einschließlich Hosting, externer Ressourcen, Kontakt, Cookies/Rechte. Das ist der aktuelle Textbestand; keine juristische Wirksamkeitsbescheinigung.

**Vor separatem E-Mail-Verteiler:** konkrete Verantwortliche, Zweck, Rechtsgrundlage, Empfänger/Auftragsverarbeiter, Speicherfristen, Löschung/Widerruf, Nachweis des Opt-in, Abmeldelink, sensible Themenwahl, ggf. UWG §7 (Werbe-Emails). Eine öffentliche Veranstaltung muss nicht auf Gesundheitsstatus schließen lassen; Einladungen nach sensiblem Website-Thema dürfen den Empfängern nichts offenbaren.

**Vor Konten/Akten/KI:** Art. 5/6/9/13/25/28/32/35 DSGVO sowie Drittländer/Transfers, Rollenverteilung, ggf. Auftragsverarbeitung, Lösch- und Auskunftspflichten, Sicherheits- und Bedrohungsmodell; spezialgesetzliche Anforderungen und ggf. Medizinprodukterecht. Die Datenschutzerklärung muss zum tatsächlich betriebenen Dienst passen. Bestehende öffentliche GitHub-Issues sind **kein** Eingang für persönliche Gesundheits- oder Fallinformationen.

**Vor lokalen Tools:** TDDDG §25 und Ausnahmen prüfen; keine Behauptung, Browser-LocalStorage sei automatisch datenschutzfrei. Bei privatem Gerät oder geteiltem Computer lokale Aufzeichnungen schützen bzw. warnen.

**Vor öffentlicher Zusammenkunft:** Rollen, Moderation, Freiwilligkeit, Grenzen der gegenseitigen Hilfe, Schutz vor Stigmatisierung, vertrauliche Kommunikation, Veranstaltungsorganisation und gegebenenfalls allgemeine Sicherheitsanforderungen klären. Austausch über Unterversorgung ist keine Gruppentherapie.

**Vor Forschungsbeiträgen von Betroffenen:** Forschungszweck, Minimierung, Einwilligung/Rechtsgrundlage, Pseudonymisierungs- und Reidentifikationsrisiko, wissenschaftlicher Prüfweg, etwaige Ethikprüfung und besondere Schutzbedürftigkeit beurteilen. Aus einer Mailadresse oder Kaffeekränzchenteilnahme erwächst keine allgemeine Forschungsfreigabe.

## 8. E-Mail- und Gemeinschaftsangebote: konkrete Wahlfreiheit

Getrennte, unabhängige opt-ins statt „Ja, ich möchte mitmachen“:
- **Über neue öffentliche Quellen/Forschung informiert werden.**
- **Einladungen zu öffentlichen Treffen erhalten.**
- **Bei einem konkreten Kaffeekränzchen anmelden.**
- **Eigene, ausdrücklich ausgewählte methodische Beobachtung zur Prüfung einreichen.**

Keine vorausgefüllten Kästchen, keine versteckte Kopplung. Ein Mensch, der etwas über einen Therapieplatz gelesen hat, soll nicht automatisch zu einer Liste „psychisch erkrankter Menschen“ werden. Die Liste darf nicht aus Besuchskontexten oder Suchbegriffen abgeleitet werden.

Die Idee eines offenen Aktionstags am Berliner Alexanderplatz zum Welttag der psychischen Gesundheit **10. Oktober** kann als späteres Ereignismodul dienen. Der 10. Oktober 2026 liegt am Projektstand 05.11.2026 bereits zurück; nächster regulärer Termin ist der 10. Oktober 2027. Offene, nicht krankheitsbezogene Opt-in-Kontaktmöglichkeit und fachliche Kooperation vor Einladungsversand klären.

## 9. Betreiberperspektive: reale, erlaubte Schnittmengen

| Betreiberinteresse | Nutzermehrwert | Zulässiger Projektoutput ohne Gesundheitsakte |
| --- | --- | --- |
| Menschen finden die passenden Quellen | schnelle, zielnahe Orientierung | anonymisierte, aggregierte Nutzbarkeitstests *nur mit geeigneter Erhebungsgrundlage* |
| Welche Frage ist ungeklärt? | transparente Forschungsgrenze | redaktionell geprüfter Fragen-/Quellenbedarf |
| Welche Fähigkeitsbausteine fehlen? | künftig präzisere Erklärungen/Tools | Skill-Backlog, Testfehler, Regressionsprotokoll |
| Gemeinsame Handlung ermöglichen | weniger Einstiegshürden, mehr Unterstützung | öffentlich dokumentiertes Veranstaltungsformat |
| Gesellschaftlich nützliche Evidenz | Rechenschaft über Quellen/Methoden | Papers, Gegenbefunde, qualifizierte Quellenbeiträge |
| Menschen freiwillig wieder erreichen | ausdrücklich gewünschte Updates/Einladung | zweckgebundene separate Kontaktliste – keine Personen-Fall-Datenbank |

**Kernschluss:** Eine Kontaktadresse ist kein wissenschaftlicher Fall. Eine Gruppenveranstaltung ist keine Therapie. Ein erfolgreich erzeugter Brief ist keine erbrachte Leistung. Eine große Menge eingereichter Beobachtungen beweist nicht automatisch Repräsentativität. Die Schnittmenge liegt zunächst bei **gemeinsam nützlichem Wissen, freiwilliger Zusammenarbeit und nachweisbar besseren Werkzeugen**.

## 10. Entwicklungspakete und Verantwortlichkeit

**P0: Sprach-/Zweck-Review**: Übergänge W01–W10 dem bestehenden Pfadinventar zuordnen; unterscheiden, wo Kontext-/Begriffssprung oder neues rechtlich relevantes Produkt beginnt. Historische Claims nicht ändern.

**P1: Null-Daten-Pilot**: lokale Suchliste + ICS-Export auf statischer Seite (erst nach Security-/Browser-Review), zwei bis drei geprüfte Quellen pro Abschnitt, Quellenstatus und Rückweg. Kein Account.

**P2: Gemeinschaftspilot**: Konzept „Gemeinsam anfangen“ als fachlich moderiertes, freiwilliges Präsenzformat mit klarer Abgrenzung von Therapie, sicherem Ablauf und möglichem Veranstalter. Zunächst keine allgemeine Mitgliederdatenbank.

**P3: Freiwilliger Kontaktkanal**: eigenständige Newsletter- und Veranstaltungszwecke mit Einwilligungs-/Lösch-/Betreiberkonzept. Kein offenes Freitext-Gesundheitsformular.

**P4: Persönliche KI/Akte nur separat prüfen**: zunächst externe, selbst gewählte Apps und patienteneigene ePA verlinken; wenn das Projekt selbst einen Dienst anbieten soll: gesondertes Architektur-/DSGVO-/Medizinprodukterecht-Projekt mit Sicherheitsprüfung und Budget.

**P5: Forschungsperspektive**: öffentliche Versorgungsdaten, institutionelle Zuständigkeiten, definierte Metriken und unterscheidbare Meta-Fragen erforschen. Beteiligungserfahrungen nur über gesonderte, rechtlich/ethisch bewertete Wege.

**Abnahme (bevor live):** Datenfluss-Diagramm, gesetzliche Anforderungen pro Dienst und Zweck, klare Betreiberrollen, aktuelle Impressum/Datenschutzhinweise, technische Tests, Moderations-/Löschprozess, mindestens ein realistisch vollständig durchgespielter menschlicher End-to-End-Pfad ohne versprochene Phantomfunktion.

## 11. Quellen und offene Prüfungen

**Offizielle Fach- und Rechtsquellen:**
- [116117 – Psychotherapie](https://www.116117.de/de/psychotherapie.php) – Vermittlungsarten, Voraussetzungen, Grenzen.
- [KBV – Psychotherapie](https://www.kbv.de/psychotherapie) – fachlicher Kontext.
- [BMG – ePA für alle](https://www.bundesgesundheitsministerium.de/themen/digitalisierung/elektronische-patientenakte/epa-fuer-alle) – Zugriffsmodell.
- [EU DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) – Art. 5, 6, 9, 13, 25, 28, 32, 35.
- [DDG §5](https://www.gesetze-im-internet.de/ddg/__5.html) – Anbieterinformationen.
- [UWG §7](https://www.gesetze-im-internet.de/uwg_2004/__7.html) – elektronische Werbung.
- [TDDDG §25](https://www.gesetze-im-internet.de/ttdsg/__25.html) – lokale Endeinrichtung.
- [BfArM Status/Klassifizierung](https://www.bfarm.de/DE/Medizinprodukte/Aufgaben/Feststellung-rechtlicher-Status-und-Klassifizierung/_node.html) – Zweckbestimmung medizinischer Software.
- [WHO World Mental Health Day](https://www.who.int/campaigns/world-mental-health-day) – 10. Oktober.

**Grenzen:** Keine abschließende anwaltliche oder behördliche Prüfung; keine Einzelfallbehandlung; keine Datenschutz-Folgenabschätzung; kein produktrechtlicher Bescheid; keine klinische Wirksamkeitsstudie. Der Betrieb der neuen Angebote ist gerade *nicht* begonnen. Über spezifische Hosting- oder KI-Dienstleister kann erst nach konkreter Auswahl eine verbindliche Datenflussprüfung erfolgen.

## 12. No-Loss-Vertrag

Originalarchitektur `LP-01..05`, fünf Therapie-Linsen, Originalclaims, Quellen-IDs, Fachpaper und negative Befunde bleiben bestehen. Neu eingeführt werden getrennte `BKI-SRV`-Betriebsräume und `W01..W10`-Übergänge. Das ist ein **Crosswalk über den Bestand**, keine Ablösung. Veränderungen an einer fachlichen Aussage ziehen Begriffe, Quelle, Perspektivwechsel, geplante Funktionen, externe Links und redaktionelle Aussage mit. Ein neues Datenprodukt wird niemals still als „nur eine neue Klappe“ behandelt.

**Entscheidungsfrage für jede Feature-Idee:** Kann dieselbe menschliche Wirkung ohne personenbezogene Datenerhebung erreicht werden? Falls ja, diese Variante zuerst testen. Falls nein, eigenen Zweck und verantwortlichen Dienst ausarbeiten, bevor ein Formular live geschaltet wird.
