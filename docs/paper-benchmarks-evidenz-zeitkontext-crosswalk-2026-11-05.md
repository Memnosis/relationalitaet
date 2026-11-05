<!-- BKI-MINIMAL-PAPER-V1 -->
![Bürger-KI Logo](./assets/media/buerger-ki-zeichen.svg)

**Forschungsedition · Stand 5. November 2026**  
**Kurzbeschreibung:** Benchmark- und Evidenzarchitektur · Bürger-KI / Corona / SOULution – methodischer Bestand und Prüfstatus.  
**Schlagwörter:** Bürger-KI · Quellen · Evidenz · Tests · Benchmark- und Evidenzarchitektur  
**Kontakt:** Kontakt@erlebNils.de

---

# Benchmark- und Evidenzarchitektur · Bürger-KI / Corona / SOULution
**Forschungsedition v0.1 · 2026-11-05 · Ergänzung, kein Ersatz bisheriger Papers**

## Grundsatz: No-Loss, Trennung der Forschungsobjekte
Jedes Paper behält seine eigenständige Frage, Quellen, Gegenproben und Negativbefunde. Der gemeinsame Crosswalk verbindet `Quelle → Aussage → Messobjekt → Methode → Zeitstand → Unsicherheit → Gegenhypothese → Evidenzprüfung → Benchmark → Ergebnis → didaktische Perspektive → Publikation`. Ursprünglicher und späterer Quellenstand werden nicht überschrieben. Nicht durchgeführte Tests sind als offen auszuweisen.

## Vergleichsakte (Benchmark-Contract)
Pflichtfelder: `benchmark_id`, `version`, `claim_id`, `source_id`, `published_at`, `observation_start`, `observation_end`, `knowledge_cutoff`, `population`, `geography`, `numerator`, `denominator`, `unit`, `endpoint`, `method`, `measurement_version`, `uncertainty`, `evidence_status`, `comparability_status`, `license`, `reviewer`. Optionale Zuordnungen zu SDMX, DCAT, PROV-O, SKOS, QUDT/UCUM, GRADE und ROBINS-I. Einheiten-, Zeitstands- und Populationstransformationen benötigen dokumentierte Regeln und Tests; sonst `non_comparable`.

### Cluster und Beispielreferenzen (nicht automatisch gleichartig)
1. **Finanzen**: Schulausgaben Deutschland 2024 ca. 97,4 Mrd. EUR/Jahr; Destatis; Budget, kein Schadenswert.
2. **Bildung**: Kompetenzunterschiede IQB 2021 versus 2016; alters- und testbezogene Kennzahl, kein maskenbedingter Anteil belegt.
3. **Krankenhausförderung**: Corona-Hilfen 2020–2022 ca. 21,5 Mrd. EUR; BMG; Mittel nicht mit Nutzen gleichsetzen.
4. **Berufsbonus**: Pflegebonus 2022 budgetiert eine Milliarde EUR; Auszahlung, Berufsfeld und Wirkung getrennt.
5. **Abfallmenge**: Destatis 2024 49,3 Mio. Tonnen Siedlungsabfälle; Teilmenge des gesamten Abfallaufkommens.
6. **Atomentsorgung**: KENFO 2017 24,1 Mrd. EUR Einzahlung; 2025 25,6 Mrd. EUR Vermögen und 5,3 Mrd. kumulierte Auszahlungen, getrennte Bestands-/Flussgrößen.
7. **Medien**: Erscheinungstag der Aussage und tatsächlich damalige Evidenzversion; keine rückwirkende Zuweisung späteren Wissens.
8. **Medizin**: GRADE nur für klar abgegrenztes Outcome und Evidenzkörper; Quellenvertrauen, Evidenzsicherheit, Nutzen-Schaden-Abwägung separat.

## GRADE-Modul und Grenzen
`high`: sehr hohe Zuversicht in Effektschätzung; `moderate`: mäßig; `low`: begrenzt; `very_low`: sehr gering. Bewertung entlang Risiko systematischer Fehler, Inkonsistenz, Indirektheit, Ungenauigkeit, Publikationsbias; Aufwertungen begründen. Nicht mit Qualität eines Behördenportals oder Gewissheit eines Einzelfalls gleichsetzen. Andere Felder verwenden geeignete Rahmen (ROBINS-I, RoB 2, GRADE-CERQual, QUADAS-2, amtliche Statistikstandards) statt unkritischer Übertragung.

## Corona-Trinität der Aussage
**(1) Aussage / Perspektive**: starkes Pro, starkes Contra, neutraler Vergleich, genaue Wortwahl.
**(2) Beobachtbarkeit / Quellenzeit**: welche Zahlen waren zum Zeitpunkt des Berichts verfügbar, was ist später revidiert?
**(3) Prüfentscheidung / Grenzen**: Effektschätzung, Unsicherheit, Gegenbeleg, offene Daten, nächster Test.
Diese drei Schritte sind Analyseachsen und nicht automatisch eine formell belegte KI-Tensor-Trinität.

## Masken / Schule / Atteste – offene Prüfakte
Arbeitsrechtlicher FFP-Atemschutz, Alltagsmasken, medizinische Masken und Kinderpflichten unterscheiden. Rechtsausnahme ist nicht automatisch praktisch nutzbar. Benötigt: Bundesland, Stufe, Tag, Maskenart, Unterrichtszeit, ärztliche Ausnahmeanträge, Ablehnungen, psychologische Teilhabe, repräsentative Handhabungsbeobachtungen, Hitze und Begleitvariablen. Private Beobachtung „über 90 % stecken die Maske in die Tasche“ ist anekdotisch, ohne repräsentative Aussage. Bei möglichen Schäden erfolgt Gegenrechnung mit vermiedenen Infektionen; die Schulausgaben dienen nur als Vergleichseinheit, nicht als kausale Schadensschätzung.

## Berufsförderung Corona
`COR-BER-01` verknüpft: Programmbudget → Anspruchsgruppen → Auszahlungen → Ausbildungseintritte → Personalverbleib → Versorgungsqualität. Förderplan ≠ Auszahlung ≠ nachgewiesene Wirkung. Vergleichsgruppen: Intensivpflege, Notaufnahme, Rettungsdienst, MFA, Pflegeheime, ärztliche Berufe, Auszubildende. Fehlende Evaluationsdaten werden einzeln nach Programm verzeichnet.

## Abfall – Ressource – Restschuld
`RES-ABF-01`: Stoffmenge → technisch rückgewinnbarer Anteil → Preisband zum Stichtag → Sortier-/Transport-/Reinigungs-/Entsorgungskosten → Nettowert. Der Satz „jeder Müll ist Ressource“ ist eine Hypothese für Kreislaufdesign, keine Lösung per Definition. Preisbandszenarien sind nicht mit beobachtetem Umsatz zu verwechseln.
`RES-ATOM-01`: historische Förderungen, Betrieb, Rückbau, Zwischen-/Endlagerung, Haftung, Zeitwert und offene Verpflichtungen. Fondsbestand ≠ Rückstellung ≠ Finanzhilfe ≠ rechtlich entschiedene Schuld. Virtueller Strompreis nur bei nachvollziehbarem Lebenszyklus- und Diskontierungsmodell.

## Mitmach-Crosswalk
Bestehende Startpunkte: `docs/mitmachen.html`, `docs/mitmachen-rueckgabe.html`, `docs/buerger-ki-werkstatt.html`, `docs/buerger-ki-feedback.html`, `docs/buerger-ki-fail-scanner.html`, `docs/buerger-ki-lernpfade.html`, `docs/buerger-ki-rechenschaft-100.html`. Jede Anwendung erhält Lernpfad (Einstieg → Demonstration → Datenfrage → Gegenprobe → Ergebnis → Weiterweg), überprüfte Ein-/Ausgabe, Fehlerfälle und Status für tatsächlichen Empfang. Frontend-Export allein ist keine Server-Einreichung.
Querverweise: `docs/buerger-ki-gesamtstand.md`, `forschung/buerger-ki/SPRACHPFADE_ELEMENTINVENTAR_V0_1.json`, `forschung/interop/PAPER_INTEROPERABILITAET_SKILLS_V0_1.md`, `docs/data/mitmachen-ergebnis-schema-v1.json`, `forschung/buerger-ki/EVIDENTE_EVIDENZ_HISTORISCHE_KOHORTE_CORONA_TIEFENTEST_2026-11-05.md`, `docs/data/bki-corona-messvergleich-medienpilot-v0-2.json`.

## Quellen-Startregister
- [Destatis Abfallstatistik 2024](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/06/PD26_185_321.html), veröffentlicht 2026-06; 49,3 Mio. t Siedlungsabfälle, 182,8 Mio. t Bauabfälle.
- [UBA Abfallaufkommen](https://www.umweltbundesamt.de/daten/umweltzustand-trends/ressourcen-abfall/abfallaufkommen).
- [KENFO Finanzdaten](https://www.kenfo.de/ueber-den-kenfo); 2017/2025 getrennt.
- [Bundesumweltministerium Entsorgungskostenbericht 2025](https://www.bundesumweltministerium.de/fileadmin/Daten_BMU/Download_PDF/Nukleare_Sicherheit/kostenbericht_nukleare_entsorgung_deutschland_2025_de.pdf).
- [Cochrane GRADE-Handbuch](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14).
- [W3C PROV-O](https://www.w3.org/TR/prov-o/), [DCAT 3](https://www.w3.org/TR/vocab-dcat/), [SDMX](https://sdmx.org/standards-2/).

## Veröffentlichungsstatus
Dies ist eine nachprüfbare Projekt- und Forschungsfassung mit offenen Prüfaufträgen, **kein abgeschlossener systematischer Review und keine kausal gesicherte Gesamtsynthese**. Originalquellen und Originalpaper bleiben als eigenständige referenzierte Artefakte bestehen.


---

*Bürger-KI · Rechte verstehen. Probleme lösen. Gesellschaft verbessern.* · [Bürger-KI](./buerger-ki.html) · [Publikationen](./publikationen.html) · Kontakt@erlebNils.de · 05.11.2026
