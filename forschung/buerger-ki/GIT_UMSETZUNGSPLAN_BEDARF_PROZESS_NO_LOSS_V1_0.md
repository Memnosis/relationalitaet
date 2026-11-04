# Bürger-KI · Git-Umsetzungsplan: Forschungslandkarte, Bedarf und tatsächliche Erfüllung
**Version:** 1.0 · **Stand:** 2026-11-04 · **Status:** Planung; keine vorgetäuschten Implementierungen
**Projektgrenze:** Nur `docs/buerger-ki*.html`, `docs/assets/buerger-ki-*.css` und `forschung/buerger-ki/**`. Die übrigen KI-Tensor-, SOULution-, Mitmach- und Navigationsdateien bleiben unangetastet. Arbeiten ausschließlich im bestehenden Branch `research/tensoratlas-auswertung-2026-11-04`; kein Merge nach `main` ohne Freigabe.

## A. Fachliche Entscheidung
Das Kernsystem ist keine Plattform für Kommunikation und keine automatisierte „Mehr-KI-Konferenz“. Es dient dazu, **konkrete Probleme** von Menschen rechts- und quellengebunden zu untersuchen:
`Bedarf feststellen → Rechtsposition bestimmen → tatsächliche Leistung prüfen → Differenz/Unterlassung analysieren → Gegenhypothese prüfen → Abhilfe entwickeln → Wirkung kontrollieren`.
Der Ablauf ist zyklisch: Wenn ein Ergebnis neue Fragen aufwirft, wächst der Quellen-, Glossar-, Thesen- und Skillbestand. Alle Fragen müssen auch ohne Vernetzung und ohne Einsatz einer kostenpflichtigen KI bearbeitbar bleiben.

**Sekundär:** Wo Menschen sich treffen und welche Kommunikationsmethoden es gibt. Kurz über vorhandene lokale Selbsthilfegruppen, Bibliotheken, Nachbarschaftszentren, bestehende Netzwerke und digitale Treffen informieren; keine neuen Stuhlkreise oder Moderationstheorien als Ersatz für konkrete Versorgungslösungen darstellen. Gruppentherapie als gesondertes medizinisches Angebot mit fachlicher Indikation, nicht mit Bürger-KI-Treffen gleichsetzen.

**Forschungsrechtliche Grenze:** „Schutzpflichten, Rechtsverletzungen und vermeidbare Schäden“ ist eine Forschungsdomäne, keine vorab bewiesene Verletzung. Politisch kritisiert ≠ empirisch schädlich ≠ rechtswidrig ≠ individuell zurechenbar ≠ strafbar. Jede Stufe braucht eigene Quellen, Definitionen und gegebenenfalls Gegenbeweise.

## B. Was schon vorhanden ist und erhalten bleibt
- `docs/buerger-ki.html`: umfangreiche Start-/Bestandsseite mit Anspruch, Versorgung, Vernetzung und Forschungslandkarte.
- `docs/buerger-ki-mein-recht.html`, `-gemeinsam.html`, `-grundlagen.html`, `-schutzpflichten.html`: vier vertiefende Seiten.
- `docs/assets/buerger-ki-design.css` und `forschung/buerger-ki/DESIGNGRAMMATIK_V1_0.md`: bestehende Farben, Karten, Icons und Status.
- `forschung/buerger-ki/FORSCHUNGSLANDKARTE_V0_1.json` / `.md`: 9 Forschungsräume, 39 Fragen, 11 Thesen, 11 Operationalisierungen, 20 Glossarbegriffe, 14 Quellen (Inventarstand beim Planbeginn; **keine bestätigten Ergebnisse**).
- `SKILL_KATALOG_V0_1.json`: 17 atomare Operationen, 15 fachliche Skill-Spezifikationen (nicht validiert).
- `SCHUTZPFLICHTEN_RECHTSVERLETZUNGEN_VERMEIDBARE_SCHAEDEN_V1_0.md`: vertiefte Rechts-/No-Loss-Akte.
- `SCHNITTSTELLE_TENSOR_UND_BEGEGNUNG_V1_0.md`: vorläufiger, noch nicht automatisierter Übergabevertrag.

**No-Loss-Verbot:** Keine Inhalte löschen, nur weil die Startseite entschlackt wird. Zuerst Bestands-Crosswalk mit Zielobjekt und Originalanker erzeugen; erst danach vorhandene Abschnitte verschieben, redigieren oder konsolidieren.

## C. Umsetzung als sechs lieferbare Git-Pakete

### Paket 0 – Bestands-Crosswalk und Datenvertrag (zuerst)
**Dateien (neu innerhalb BK):**
- `forschung/buerger-ki/inventar/NO_LOSS_CROSSWALK_V1.json`
- `forschung/buerger-ki/inventar/INHALTSINVENTAR_V1.md`
- `forschung/buerger-ki/schema/BK_FORSCHUNGSOBJEKT_SCHEMA_V1.json`
**Inhalt:** alle bestehenden Abschnitte und Aussagen, Fragen, Rechtsquellen, Thesen, Lernziele, Operatoren, offene Gegenbeispiele, Referenzen, Provenienz/Version/Status. Jede vorhandene Aussage erhält Ziel-ID oder bewusst begründetes Duplikat.
**Abnahme:** Keine unzugeordnete wesentliche Aussage; vorhandene Links/Anker dokumentiert; maschinenlesbares JSON validiert, alte Registerdaten ohne Verlust rekonstruierbar.

### Paket 1 – Bedarfsermittlung als erster sichtbarer Forschungszugang
**Neu:**
- `docs/buerger-ki-bedarf.html` – Einstieg „Wo können wir Bedarf heute schon feststellen?“
- `forschung/buerger-ki/bedarf/BEDARFSRAEUME_V1.json`
**Startbereiche (nicht vorab als Rechtsverletzungen klassifizieren):**
Gesundheit/Psychotherapie; existenznotwendiger Lebensunterhalt; Wohnen/Energie; Kinderbetreuung/Bildung; Pflege/Assistenz; Arbeit/Einkommen; Rente/Alter; Behördenverfahren/Rechtsschutz.
**Pro Bedarfsraum sechs Schlüsselfelder:** (1) fraglicher Bedarf, (2) anwendbare Rechtsposition, (3) vorhandene Daten und deren Aussagegrenzen, (4) tatsächliche Erfüllung, (5) institutionelle Verantwortung, (6) offene Forschungs-/Lösungsfrage.
**Wichtige Beispiele:** Warte-/Behandlungszugang und fachliche Eignung; geschuldete/ausgezahlte Sozialleistungen; Kita-Anspruch nach § 24 SGB VIII; Wohnkostenbelastung und geltender Unterkunftsbedarf. Verfügbare Statistiken sind nicht automatisch individualrechtliche Nachweise.
**Abnahme:** Mindestens vier vollständig quellengebundene Beispielkarten mit Norm, Originalquelle, Zeitstand und expliziter Aussagegrenze; alle weiteren Räume als offen gekennzeichnet.

### Paket 2 – Durchgehender Prozess als wiederverwendbare UI-Grammatik
**Änderungen nur an BK-Seiten und BK-CSS.** Sieben Schritte werden zur wiederkehrenden Navigation:
`Frage → Rechtsposition → Tatsachen → Nachweis → Gegenprüfung → Lösung → Wirkung`.
Nicht jede Seite zeigt alles in voller Länge; kurze Einstiege führen zu Deep-Dives. Systematisch unterschiedliche Boxen: Rechtsquelle, Datenbefund, Interpretation, Hypothese, Warnung, Gegenprobe, Lösungsvorschlag, Ergebnis. Diese Kennzeichnungen haben sichtbare Wörter, nicht nur Farben.
**Abnahme:** Mobile und Desktop sinnvoll lesbar; korrekt gegliederte Überschriften; Links existieren; Icons konsistent; Warn- und Statusfarben nicht als unbewiesene Qualitätsurteile; Tastaturbedienung, Kontrast/Dunkelmodus geprüft.

### Paket 3 – Quellenfundus, Thesen, Glossar und Operationalisierungen mit Nachzug
**Dateien (BK-lokal):** `forschung/buerger-ki/quellen/REGISTER.json`, `thesen/REGISTER.json`, `operationalisierungen/REGISTER.json`, `glossar/REGISTER.json` – Migration aus `FORSCHUNGSLANDKARTE_V0_1.json` erst mit dokumentierter Gleichheit/Crosswalk.
**Verknüpfung:** Jede Frage besitzt IDs zu Primärquelle(n), These(n), Gegenhypothesen, Messregeln, Skills und Ergebnisstatus. Datenquelle mit Abrufdatum, Geltungszeitraum, Qualität, zitierfähigem Originalanker; Unbekanntes nicht erfinden.
**Nachzug:** Änderung einer Quelle markiert betroffene Frage/These/Operationalisierung/Glossar/Skill/Website; vorerst überprüfbarer manueller Change-Report, keine fingierte Echtzeitautomatik.
**Abnahme:** Konsistenzprüfung aller IDs, Referenzen, doppelter/nicht mehr aktueller Aussagen; null verlorene Bestandsobjekte.

### Paket 4 – Sichtbare Fortschritte und Status-Flags
**Neu:** BK-seitiger Status-/Nachweisindex, ggf. `docs/buerger-ki-forschung.html`.
**Verbindliche Flags:**
- `OFFEN`: Frage noch nicht geklärt
- `QUELLE_ERFASST`: Original vorhanden, Auslegung noch offen
- `RECHTSSTAND_GEPRUEFT`: Norm und Fassung geprüft, keine Fallentscheidung
- `DATENBEFUND`: Messung/Population/Zeit/Nenner nachgewiesen
- `HYPOTHESE`: zu testende Aussage
- `GEGENBELEG`: widerlegende/limitierende Evidenz
- `PFLICHTABWEICHUNG_VERDACHT`: konkrete Rechtsfrage und Tatsachen, keine Feststellung
- `RECHTSVERLETZUNG_FESTGESTELLT`: nur mit belastbarem Rechtsprüf-/Entscheidungsanker und exakter Reichweite
- `WIRKUNG_GEPRUEFT`: Ergebnis mit Baseline/Gegenprobe
- `BLOCKIERT`: benötigte Quelle, Erlaubnis oder Daten fehlen.
**Metrik:** beantwortete vs. offene Fragen, bestätigte/widerlegte Thesen, abgeschlossene vs. nicht bestandene Tests, echte Erfüllungsnachweise. Keine Fortschrittsbalken allein aus Textmenge.
**Abnahme:** jedes Flag hat Definition, Nachweis-ID, Aktualisierungsstand und gegebenenfalls Sichtbarkeit der Unsicherheit.

### Paket 5 – Skills und Tensor-Rückkopplung erst aus echten Forschungsergebnissen
- Bürger-KI exportiert abstrahierte Problem-, Operator-, Relations- und synthetische Testfälle, keine Gesundheitsakten.
- Tensor prüft Typen, Invarianten, alternative Darstellungen, Rückrechnung und Gegenbeispiele. Eine übereinstimmende 3×3×3-Adresse ist kein mathematischer Beweis.
- Rückgabe nur als Version mit Testprotokoll, Einschränkungen und nachgewiesenem Zusatznutzen gegenüber bestehenden Hilfen.
- Kein automatischer Mehr-KI-Dialog als Voraussetzung; kein vorgespiegeltes Nutzer- oder Gruppenmatching.
**Abnahme:** mindestens ein tatsächlich bestandener Vorher/Nachher-Test und eine reproduzierbare Rückgabe – oder ehrlicher Null-/Negativbefund. Globale Tensoränderung erfordert gesonderte Freigabe.

## D. Konkrete Redaktionsregeln / Was jetzt nicht passieren darf
1. Die Bedarfsermittlung ist Startfrage, nicht automatisch politische Anklage. Keine erfundenen Zahlen, repräsentativen Quoten oder Kausalnachweise.
2. Rechtsanspruch, institutionelle Sicherstellungspflicht, gesellschaftliches Ziel und politischer Gestaltungsspielraum konsequent trennen.
3. „Verbrechen gegen die Menschlichkeit“ nicht als Ersatzetikett für nachgewiesene/angenommene politische Fehlentscheidung verwenden.
4. Stuhlgespräch, Fishbowl, Moderation und Gesprächskompetenzen nur als **optionale Begegnungshilfe** an tatsächlichen Orten; nicht als Hauptlösung, nicht als eigenständiger therapeutischer Pfad.
5. Prävention/Fehlerkultur als Ursachen- und Lösungshypothese mit Fachquellen und Gegentests untersuchen; kein Ersatz für notwendige Behandlung.
6. Gruppenbildung und struktureller Nachweis nicht voraussetzen. Bereits vorhandene Angebote/Initiativen zuerst inventarisieren.
7. Statische HTML-Seite ist kein aktiver KI-Dienst; keine Behauptung, personenbezogene Unterlagen würden hochgeladen, verarbeitet, geschützt gespeichert oder mit anderen geteilt.
8. Die im Gespräch genannten drei fachlichen Meilensteine (Therapie-Rechtsakte, Benchmark, Tensor-Rückgabe) bleiben **optional wachsendes Backlog** und werden nicht zum Flaschenhals für neue Forschungsräume.

## E. Git- und Veröffentlichungsregeln
- Pro Paket kleine thematische Commits mit Liste geänderter Dateien, Stand der Tests und offenen Punkten.
- Die BK-Inventardatei ist zunächst autoritative Referenz; spätere normalisierte Register nur nach bestandener No-Loss-Migrationsprüfung.
- Seiten/Quellen nicht zusammenführen, bevor ihre IDs und Geltungsstände geklärt sind.
- Erneute fachliche Prüfung zeitabhängiger Gesetze, Richtlinien und Statistiken vor Veröffentlichung.
- Keine Änderungen an `docs/index.html`, globaler Navigation, Tensor-Register, SOULution-Seiten, anderen Fachprojekten und `main`.
- Öffentliches Pages-Deployment folgt erst gesonderter Freigabe und Abnahme.

## F. Unmittelbar nächster Git-Durchgang
1. **Paket 0:** Vorhandene Seitenabschnitte und Wissensobjekte inventarisieren.
2. **Paket 1:** Quellengestütztes Bedarfsraum-Schema mit einer verständlichen Website-Ansicht erstellen.
3. **Paket 2:** Die Sieben-Schritt-Prozessgrammatik auf der Bedarfsansicht erproben, dann übertragen.
**Danach** erst Registermigration, Flags, Kompetenztiefe und Tensortransfer. Keine vorgeschaltete Pflicht, erst einen Therapieplatz-Benchmark „abzuschließen“.
