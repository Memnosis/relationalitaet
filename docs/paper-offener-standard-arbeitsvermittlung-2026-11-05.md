<!-- BKI-MINIMAL-PAPER-V1 -->
![Bürger-KI – Forschung und Verbindung](./assets/media/buerger-ki-zeichen.svg)

**Forschungsedition · Offene Standards für Arbeitsvermittlung und Potenzialagenturen**

**Kurzbeschreibung:** Quellengebundene Forschungs- und Entwicklungspublikation mit eigenständigem Prüfstatus und offenen Fragen.  
**Schlagwörter:** Bürger-KI · Quellen · Evidenz · Crosswalk · Offene Standards für Arbeitsvermittlung und Potenzialagenturen  
**Stand:** 5. November 2026  
**Kontakt:** Kontakt@erlebNils.de

---

# Offene Standards für Arbeitsvermittlung und Potenzialagenturen
**Forschungspaper v0.1 · 05.11.2026 · eigenständig, nicht Teil der Corona-Forschung**

## Leitfrage
Was würde ein offener, überprüfbarer Daten- und Verfahrensstandard für Stellen, Aufgaben, Kompetenzen, Qualifizierung, freiwillige Berufsinteressen und Vermittlungsergebnisse ermöglichen? Der Standard ersetzt weder Jobcenter noch Beratung; er definiert Schnittstellen für verlässlich ausgetauschte Informationen.

## Was existiert bereits?
- [ESCO](https://esco.ec.europa.eu/en/use-esco): mehrsprachige europäische Berufe und Skills, Linked Open Data sowie Web- und lokale API.
- [ISCO-08](https://isco.ilo.org/en/isco-08/): internationale statistische Berufsklassifikation; [KldB 2010](https://statistik.arbeitsagentur.de/DE/Navigation/Grundlagen/Klassifikationen/Klassifikation-der-Berufe/KldB2010/KldB2010-Nav.html): deutsche Berufsklassen.
- [O*NET](https://www.onetcenter.org/): Tätigkeits-, Interessen-, Kompetenz- und Arbeitskontextdaten aus den USA; keine automatische Übertragung auf Deutschland.
- [HR Open Standards](https://www.hropenstandards.org/): Austauschmodelle für HR-Prozesse; Normversion und Implementationsumfang pro Anwendung prüfen.
- [schema.org/JobPosting](https://schema.org/JobPosting): semantische Kennzeichnung öffentlich ausgeschriebener Stellen.
- [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/), [PROV-O](https://www.w3.org/TR/prov-o/), [SKOS](https://www.w3.org/TR/skos-reference/), [SDMX](https://sdmx.org/): Metadaten, Herkunft, Begriffe, statistische Daten.

## Das technische Transparenzproblem der Jobbörse
[BundesAPI / jobsuche-api](https://github.com/bundesAPI/jobsuche-api) dokumentiert technisch beobachtete Jobsuche-Endpunkte und ein OpenAPI-Modell. Es handelt sich nach Eigenangabe um **keine offiziell bereitgestellte, garantierte öffentliche BA-API**. Nutzungsrechte, Stabilität, Datenschutz, Rate Limits und Zertifikats-/Authentifizierungsanforderungen vor jeder Integration prüfen. Das Projekt soll keine nicht autorisierten Zugriffspfade oder Bewerberdatensammlung aufbauen.

## Module eines möglichen offenen Standards
1. **Stelle/Auftrag:** eindeutige Kennung, Tätigkeitsbestandteile, Ort, Lohn/Entgelt, Zeit, Gültigkeit, Quelle, Arbeitgeberidentität und Aktualisierung.
2. **Skillprofil als freiwilliges Datenprodukt:** ESCO/KldB-Referenzen, nachweisbare Fähigkeiten, selbstgewähltes Ziel, Datensparsamkeit, Berichtigungs- und Löschrechte.
3. **Matching-Empfehlung:** maschinenlesbare Begründung, Alternativvorschläge, Unsicherheit, Widerspruchs- und Korrekturmöglichkeit, kein automatisiertes Personenwerturteil.
4. **Qualifizierung:** Kurs-/Zertifikatsanbieter, Voraussetzungen, Kosten, Zeit, Finanzierung, Kompetenzergebnis und Prüfmethode.
5. **Auftragsbündelung:** regionale Nachfrage, gemeinsame Vertriebskapazität, Qualitäts- und Preisvereinbarungen, menschengeprüfte Vertragswege.
6. **Wirkung:** Vermittlung, stabiler Verbleib, Einkommensentwicklung, Zufriedenheit, zusätzliche statt nur verlagerte Aufträge.
7. **Audit:** Version, Herkunft, begründete Transformationen, Fehlerfälle, Datenschutzfreigaben, Verantwortlichkeiten.

## Offene Standardisierung heißt nicht:
- Gesetzliche Leistungsgewährung zu automatisieren.
- Persönliche Bewerbungsprofile ohne rechtliche Grundlage öffentlich zu machen.
- Hilfebedürftigkeit oder Empathie durch algorithmisches Scoring zu ersetzen.
- Nur beim Arbeitsamt gemeldete Stellen zum vollständigen Arbeitsmarkt zu erklären.
- Ohne API-Nutzungsvertrag auf technisch auffindbare Endpunkte zu vertrauen.

## Forschungsfragen und Piloten
**OFF-JOB-01:** Wie viele veröffentlichte Stellen lassen sich zwischen ESCO, KldB, ISCO semantisch verlustarm umrechnen?
**OFF-JOB-02:** Wie viel der realen regionalen Auftragsnachfrage ist in öffentlichen Stellenanzeigen nicht sichtbar?
**OFF-JOB-03:** Können mehrsprachige Skills zu besserer beruflicher Orientierung führen, ohne standardisierte Abwertungen?
**OFF-JOB-04:** Lässt sich eine regionale Handwerks-/Gründer-Auftragsbörse mit freiwilligem, datensparsamem Matching testen?
**OFF-JOB-05:** Welche Rolle übernehmen menschliche Beratende; wann sind Entscheidungen ohne sie unzulässig oder ungeeignet?

## Messbare Tests
Roundtrip zwischen ESCO ↔ KldB mit Bedeutungsverlust; Dublettenerkennung; Versionen und Löschungen; kontrollierte Validierung nichtstandardisierter Tätigkeiten; menschlich bewertete Passungsqualität; Schutz vor indirekter Diskriminierung; Outcome- und Kostenvergleich mit bisheriger Vermittlung.

## Projekt-Crosswalk
[Bürger-KI Skills](./buerger-ki-skillzentrum.html) → [Potenziale](./paper-potenziale-arbeitslosigkeit-unbezahlte-arbeit-innovation-2026-11-05.md) → [Kaffeekränzchen-Fragen](./buerger-ki-kaffeekraenzchen-fragen.html) → [Evidenz/Benchmark](./paper-benchmarks-evidenz-zeitkontext-crosswalk-2026-11-05.md).
**Status:** Standardsinventar und Modellvorschlag; keine staatliche Zertifizierung, keine vollständige API-Implementierung und keine echten Bewerbungsdaten.


---

*Bürger-KI · Rechte verstehen. Probleme lösen. Gesellschaft verbessern.*  
[Zur Bürger-KI](./buerger-ki.html) · [Forschungsbibliothek](./bibliothek.html) · Kontakt@erlebNils.de · 05.11.2026
