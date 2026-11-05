# Sprachphase 2 – Wissensräume, Quellenkuratur und die Entscheidung über Darstellung

**ID:** BKI-SW-PH2-REPORT-001 · **Stand:** 05.11.2026 · **Status:** Pilot-Quellenprüfung für acht Wissensräume, noch keine vollständige Fach-/Browserfreigabe.  
**Maschinenlesbare Matrix:** [Acht Wissensräume](./PHASE_2_WISSENSRAEUME_QUELLENMATRIX_V0_1.json)  
**Vorgänger:** [Phase-1-Analyse](./PHASE_1_BERICHT_BEDEUTUNGSUEBERGAENGE_L0_L1_L2_V0_1_2026-11-05.md), [schlanke Übersetzung](./BERICHT_DOPPELUNG_SPRACHE_SCHLANKE_UEBERSETZUNG_V0_1_2026-11-05.md), [36+ Forschungs-Nuclei](./WISSENS_NUCLEI_DEEP_DIVE_REGISTER_V0_1_2026-11-05.json).

## 1. Ergebnis: nicht jeder Wissenskern bekommt eine neue Seite

Die erste Quellenkuratur arbeitet an **acht Entscheidungsfragen** und ordnet die passende Form zu. Ein einfacher Unterschied wird sofort erklärt; dahinter können bei hinreichendem Inhalt eine Klappe, ein Vergleich oder ein vollständiges Paper folgen. Der Leser soll beim Anliegen bleiben oder nach eigener Wahl in die tiefere Welt gehen.

| ID | Kernfrage | Darstellung | Nachgewiesener Stand / wesentlich offene Arbeit |
| --- | --- | --- | --- |
| WR-01 | Therapieplatz: Wo beginnen, was vermittelt 116117? | bestehende Themenseite + konkrete Handlungswelt | 116117 als Primärinformation; regionale Zugänge und Alternativen offen |
| WR-02 | Sprechstunde oder tatsächlicher Behandlungserfolg? | kurze Gegenüberstellung + Evidenzklappe | Servicebegriffe vorhanden; Wirkung, Wartezeit und Eignung vertiefen |
| WR-03 | Praxisakte, ePA und eigener Ordner? | knapper Vergleich, später Akten-Themenseite | ePA-Funktion geprüft; Praxisaktendetails noch unabhängig prüfen |
| WR-04 | Was kann ich bei der ePA einstellen/ablehnen? | kompakter Rechtevergleich | gematik-Widerspruchsseite und FAQ; Rechtsprüfung und Verbrauchersicht ausbauen |
| WR-05 | Eigene Dokumente bei KI verwenden? | **einmaliges kontextgebundenes Sternchen** mit kompaktem Vergleich | providerbezogene Datenflüsse und lokale Alternativen noch zu recherchieren |
| WR-06 | Wie bleiben Gesundheitsdaten maschinenlesbar und sinnvoll? | kurzer FHIR-/MIO-Einstieg + technischer Deep Dive | HL7- und MIO-Einstiege gefunden, konkrete deutsche Profile/Interoperabilität offen |
| WR-07 | Jemand hilft jemandem – was lässt sich weitergeben? | kleine Methodenklappe + vorhandene Initiativen | Kaffeekränzchen-Methode und konkrete Organisationen noch fachlich abgleichen |
| WR-08 | Wann ist Unterversorgung nachgewiesen? | präzise Meta-Frage + Paper/Quellen | noch keine populations- oder pflichtenbezogene Schlussfolgerung freigegeben |

## 2. Gezielte Primärquellen und ihre genaue Rolle

1. **116117 Psychotherapie** – [116117](https://www.116117.de/de/psychotherapie.php): Sprechstunde, Vermittlungscode, Akutbehandlung und probatorische Sitzung. Die Seite beschreibt unterschiedliche Wege und Bedingungen; daraus folgt keine universelle Behandlungsgarantie.
2. **gematik ePA Widerspruch** – [Widerspruchsübersicht](https://www.gematik.de/anwendungen/epa-fuer-alle/widerspruch): Unterschied zwischen Widerspruch gegen Anlage, Zugriff, Befüllung und Datenweitergabe für Sekundärnutzung. Diese Optionen müssen auch redaktionell **getrennt** bleiben.
3. **gematik ePA FAQ** – [FAQ](https://www.gematik.de/anwendungen/epa-fuer-alle/faq): praktische Fragen zu Rechten, ePA-Zugriff und Dokumentverwaltung. Zeitstand und Konstellation im jeweiligen Abschnitt angeben.
4. **gematik ePA Überblick** – [ePA für alle](https://www.gematik.de/anwendungen/epa-fuer-alle): Patientenfunktionen und Unterschiede zwischen ePA und anderen Systemen.
5. **HL7 FHIR** – [FHIR-Spezifikation](https://hl7.org/fhir/): medizinische Datenformate/Resources, Versionen und Konformität. Eine korrekte FHIR-Repräsentation beweist keine angemessene klinische Entscheidung.
6. **KBV MIO** – [mio.kbv.de](https://mio.kbv.de/): nationale medizinische Informationsobjekte und ihre Entwicklung/öffentlichen Kommentierungswege. Verbindung von Standard und tatsächlicher Datenbedeutung fachlich prüfen.
7. **NAKOS** – [Selbsthilfegruppen](https://www.nakos.de/informationen/basiswissen/selbsthilfegruppen/): konkretes Gruppen-/Methodenmaterial im nächsten Rechercheblock gegenprüfen.
8. **DI.DAY** – [Initiative](https://diday.org/de/): vorhandene digitale Selbstbestimmungsprojekte; noch kein eigener Veranstaltungsbetrieb.

**Quellenstatus:** Nr. 1–6 in diesem Turn durch öffentliche Suchergebnisse stichprobenartig verifiziert; Nr. 7–8 sind als bekannte Quellenkandidaten geführt, noch nicht im selben Umfang neu überprüft. Primärquellen sind mit den Aussagen verbunden, für die sie tatsächlich zuständig sind. Kein bloßer Linkstatus oder „offizielle Domain“ gilt als fachlicher Beweis sämtlicher Aussagen.

## 3. Wie wir das Wissen darstellen

**Direkt auf der Seite:** Jeder verständliche Kern bekommt zuerst 1–3 sinnvolle Sätze. Beispielsweise „Eine psychotherapeutische Sprechstunde klärt den weiteren Behandlungsbedarf; ein Termin dafür ist nicht schon der Beginn einer längerfristigen Behandlung.“

**Kurzer Kontextkasten:** Zwei bis drei herausragende Links, wenn sie **unterschiedliche Funktionen** erfüllen (Weg, Fachverständnis, Gegenprüfung); wenn nur eine passende Quelle geprüft ist, erscheint nur eine, nicht künstlich eine dritte.

**Substanzielle Klappe:** Geöffneter Zustand liefert fachliche Unterschiede, Beispiel, konkrete Quelle, eine Grenze/Gegenfrage und den Rückweg. Eine einzelne Überschrift mit weiteren Links reicht nicht.

**Eigene Themenseite:** Wenn mehrere eigenständige Entscheidungspunkte existieren, insbesondere Patientenakte (Akte, Zugriff, KI-Kopie, ePA-Forschung, Rechte) oder Therapieplatz (Bedarf, Suchwege, Behandlung, gesellschaftliche Versorgung).

**Forschungs-Deep-Dive:** Bei Standards, medizinischer Eignung, Rechtsnormen, Messmethodik, ethischer/algorithmischer Analyse, Tensor-Relationsvergleich. Keine Überfrachtung des Alltagswegs.

## 4. Der Datenentscheid als einzelner Handlungshinweis

Wenn der Mensch ausdrücklich **eigene Unterlagen mit einer KI bearbeiten möchte**, darf dort ein kleines `*` oder „Was passiert mit meinen Daten?“ erscheinen. Nur an der relevanten Handlung, nicht auf jeder Seite. Dahinter: lokal vs. externe Cloud, Datenübermittlung, Speicherung/Weiterverwendung, Rechte und seriöse Alternativen, jeweils zum tatsächlich gewählten Anbieter. Keine Datenübertragung durch den Stern selbst. Sollte Bürger-KI irgendwann einen Übermittlungsdienst betreiben, reicht dieser Hinweis nicht als alleinige rechtliche Maßnahme.

## 5. Schlüsselfrage: Was fehlt wirklich noch?

- **Patientenakte:** Praxisakte/ePA-Eigentümer und Rechte noch quellenrechtlich vervollständigen; Open-Source-Gesundheitsanwendungen, konkrete Anbieter, Standardprofile, KI-Sicherheitsbedingungen und klinische Grenzen nachziehen.
- **Therapieplatz:** Geeignete Behandlungsformen und konkrete Suchbedingungen nach Fachquellen; Wartezeit-/Bedarfsdaten nicht mit Erstterminen vermischen.
- **Kaffeekränzchen:** Echte Organisationen und Unterstützungsfunktionen, Methodenbelege und freiwillige Rückgabe anonymisierter *allgemeiner* Hilfsbausteine.
- **Gesellschaftliche Frage:** Unterversorgung und Institutionenpflichten durch geeignete Maßstäbe und Quellen untersuchen. Keine vorschnelle Verrechtlichung.
- **Übersetzung:** Ursprüngliche 14 Fälle mit genau diesen Quellen/Begriffssinnen abgleichen, ohne die Sprachtheorie erneut zu schreiben.

## 6. No-Loss und nächste Abnahme

Die acht Fragen sind **Präsentations-/Quellenprojektionen** über bestehende `BKI-PH1-H*`, `BKI-NUC-*`, `BKI-TOPIC-THERAPY` und `LP-01..05`. Die Quellenregister bleiben Originaleigentümer; eine zusätzliche Quelle erhält zunächst Rolle, Fundstelle, Datum und Prüfstatus, nicht still eine konkurrierende kanonische ID.

**Aktuelles Gate:** erster quellenorientierter Entwurf vorhanden; allgemeine klinische/rechtliche Freigabe, vollständige Deep Dives und Browsertests ausstehend. Phase 2 kann weitergeführt werden, ist aber noch nicht abgeschlossen. Als nächster konzentrierter Arbeitsblock eignen sich Aktenformen / ePA-Rechte / KI-Kopie / Open-Source-Angebote / Standards, gefolgt von der Therapie-Suchwelt.
