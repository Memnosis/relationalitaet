# Vorhersehbare Unterversorgung: Therapie, Pflege, Notfallbetten und institutionelle Verantwortung

## Historische Kapazitäts- und Wirkungskarte der Bürger-KI

**Paper-ID:** BKI-CAP-PAPER-001 · **Fassung:** 0.1, 5. November 2026  
**Status:** quellengebundene Bestands- und Methodenforschung. Kein kausaler Nachweis für konkrete Todesfälle, keine abgeschlossene strafrechtliche oder zivilrechtliche Bewertung.  
**Primärregister:** [Versorgungs- und Unterversorgungsatlas](./data/bki-versorgungskapazitaet-unterversorgung-v0-1.json).  
**Forschungspriorität:** (1) Therapieplätze, (2) Pflegeplätze, (3) nachgeordnet Notfall-/Akut-/Intensivbetten.  
**Arbeitsregel:** eigene Rekonstruktionen und Fundstellen, keine Originaltexte in den Handlungsanweisungen.

## Abstract

Der Bürger-KI-Handlungsatlas soll nicht nur verfügbare Hilfeangebote auflisten, sondern erkennen, wann Leistungen **tatsächlich zugänglich** sind, welche strukturellen oder saisonalen Engpässe über Jahre bestehen, was verantwortliche Institutionen vorab wussten und ob Gegenmaßnahmen erfolgten. Die Analyse unterscheidet streng formale Leistungsberechtigung, ausgewiesene Kapazität, personell betreibbare Kapazität, freie Kapazität zur benötigten Zeit, Behandlungsbeginn und gesundheitliches Ergebnis. Sie erweitert die Quellenkarte um Wartedauern, Ablehnungen, ausgelastete Einrichtungen, saisonale Spitzen, zeitlich datierte Warnungen, Planung, Finanzierung, Personal und Nachprüfung. Besondere Aufmerksamkeit gilt schwerwiegenden Schäden und vermeidbaren Todesfällen. Entscheidend sind jedoch voneinander getrennte Nachweisschritte: Unterversorgung → Pflicht → vorhersehbares Risiko → mögliche Abhilfe → konkrete Unterlassung → individuell/epidemiologisch gestützte Kausalität → gegebenenfalls Verschuldens- oder Vorsatzprüfung. Aus Frühwarnung und späterem Todesfall folgt für sich genommen **weder eine konkrete Todesursache noch strafrechtlicher Vorsatz**.

## 1. Drei getrennte Versorgungsräume

### T: Therapieplätze – Zugang zur Behandlung

Zu unterscheiden sind Beratung, Erstkontakt, psychotherapeutische Sprechstunde, Diagnostik, probatorische Sitzungen, Krisen-/Akutbehandlung, regulärer Beginn und kontinuierliche Behandlung. Eine zeitnahe Sprechstunde kann gut erreichbar sein, ohne dass anschließend ein regulärer Therapieplatz verfügbar ist.

**Messachsen:** Zeit seit erstem Hilfesuchen; Zeit bis zum ersten Kontakt; Zeit bis Sprechstunde; Zeit zwischen Indikation und Therapiebeginn; Anzahl erfolgloser Kontaktversuche; Fachgebiet; Altersgruppe; Erkrankungsschwere; Region; zugelassene Therapeutensitze vs. tatsächlich verfügbare Stunden; Kassenart; Behandlungsausfall.

**Nicht vergleichbare Zeitreihen:** Die [BPtK-Auswertung vom 09.12.2022](https://www.bptk.de/pressemitteilungen/psychisch-kranke-warten-142-tage-auf-eine-psychotherapeutische-behandlung/) nennt rund 142 Tage zwischen Sprechstunde und Behandlungsbeginn auf Basis eines Patientenkollektivs aus 2019. Die [vdek-Analyse vom 17.06.2026](https://www.vdek.com/presse/pressemitteilungen/2026/wartezeiten-psychotherapie-akutbehandlung.html) wertet rund 1,5 Mio. Abrechnungsdaten aus 2022–2024 aus und berichtet für 80 % der Erwachsenen und 85 % der Kinder weniger als vier Wochen **nach dem Erstgespräch bis zur probatorischen Sitzung**. Eine Probatorik ist nicht gleich Beginn einer längerfristigen Richtlinientherapie; zudem kann die Suche vor dem Erstgespräch fehlen. Die Befunde zeigen daher **keinen einfachen Widerspruch über dieselbe Größe**.

**Wichtiger Negativfall:** `Sprechstundentermin_erreicht` ≠ `regelmäßiger_Therapieplatz_vorhanden`. Ein hoher rechnerischer Versorgungsgrad oder eine steigende Kopfzahl der Fachkräfte beweist nicht die Verfügbarkeit eines geeigneten Termins.

Die [KBV-Zahlen 2025](https://www.kbv.de/infothek/zahlen-und-fakten/gesundheitsdaten/bedarfsplanung-landesbeschluesse-ueber-unterversorgung) dokumentieren förmliche Feststellungen von Unterversorgung und drohender Unterversorgung in Planungsbereichen; diese betreffen **überwiegend Hausärzte**, also nicht speziell alle Psychotherapiezugänge. Das ist eine nützliche institutionelle Frühwarn-Datenfamilie, aber keine Psychotherapieplatz-Warteliste.

### P: Pflegeplätze – tatsächliche Aufnahmemöglichkeit

**Vier essenzielle Mengen:** genehmigte Plätze; personell betreibbare Plätze; bereits belegte Plätze; unmittelbar für den gesuchten Pflege-/Betreuungsbedarf aufnahmebereite Plätze. Dazu Kurzzeitpflege, vollstationäre Dauerpflege, Tagespflege, ambulante Pflege und spezielle Indikationen trennen.

[Destatis GENESIS 22412-0010](https://genesis.destatis.de/datenbank/online/statistic/22412/table/22412-0010/search/s/Detailsuchezg) dokumentiert für den 15.12.2023 **874.562 verfügbare Plätze in vollstationärer Dauerpflege** und **775.961 dort versorgte Pflegebedürftige**. Aus der statistischen Differenz lässt sich **kein Bestand kurzfristig frei vermittelbarer Pflegeplätze** ableiten: Einrichtungsprofil, Personal, Pflegegrad, Besonderheiten, Aufnahmesperren, Kosten und Ort können einen Platz praktisch unzugänglich machen. Eine weitere Folge: Vollstationär versorgte Pflegebedürftige sind nur ein Teil aller [rund 5,7 Mio. Pflegebedürftigen Ende 2023](https://www.destatis.de/DE/Presse/Pressemitteilungen/2024/12/PD24_478_224.html).

**Zeitreihe:** Die [Destatis-Einrichtungsstatistik](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Pflege/Tabellen/pflegeeinrichtungen-deutschland.html) führt 11.634 Pflegeheime 2009, 15.380 im Jahr 2019 und 16.505 im Jahr 2023, jedoch verändert sich der Mix der Pflegearten. Eine Zunahme der Einrichtungen beweist weder wachsende sofort verfügbare Plätze noch eine bedarfsgerechte Versorgung.

**Schadens- und Wirkungsklassen:** verzögerte Entlassung aus der Klinik, Überforderung pflegender Angehöriger, verschlechterte Versorgung, vermeidbare Wiederaufnahme, Pflegeverschlechterung und – wo fachlich belegbar – schwerwiegende Schäden oder Todesfälle. Eine solche Folge muss jeweils unabhängig nachgewiesen werden, nicht vom bloßen Platzmangel abgeleitet.

### A: Notfall-, Akut- und Intensivkapazität – nachgeordneter Forschungsraum

Die [Destatis-Krankenhauszeitreihe](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankenhauser/Tabellen/gd-krankenhaeuser-jahre.html) reicht von 1991 bis 2024: 665.565 aufgestellte Betten im Jahr 1991, 494.326 im Jahr 2019 und **472.851 im Jahr 2024**. Die nationale durchschnittliche Bettenauslastung betrug 2024 **72,0 %**. **Das ist keine Aussage über die freie Notfall-/Intensivkapazität während einer bestimmten Grippewoche und in einer bestimmten Region.**

[Destatis für 2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankenhauser/Tabellen/eckzahlen-krankenhaeuser.html) weist **25.956 Intensivbetten** und 7.748 Intermediate-Care-Betten aus. Das [DIVI-Intensivregister](https://zenodo.org/records/17899565) liefert eine andere Ebene: **tagesbezogene, aggregierte Daten** zur gemeldeten Intensivversorgung seit der Pandemie, mit regionalen Unterschieden. Der [Bundesregisterüberblick](https://www.verwaltungsdaten-informationsplattform.de/register/218) unterscheidet öffentliche und differenzierte nichtöffentliche Datenzugänge.

**Saisonale Warnung:** Das RKI überwacht respiratorische Wellen und berichtet für 2025/26 Hospitalisationen und erhöhte Krankheitslast in bestimmten Altersgruppen. Eine epidemiologische Welle und ein lokal fehlendes Bett sind aber nicht dasselbe Ereignis. Ebenso dürfen Influenza-/RSV-assoziierte Todesfälle aus dem [Saisonbericht 2025/26](https://edoc.rki.de/bitstream/handle/176904/13996/ARE-Saisonbericht_RKI_2025_26.pdf?isAllowed=y&sequence=1) **nicht** als „Todesfälle wegen Bettenmangel“ gezählt werden.

Das [BMG zur Notfallreform](https://www.bundesgesundheitsministerium.de/service/gesetze-und-verordnungen/guv-21-lp/notfallreform/faq-notfallreform) beschreibt Übergabe- und Koordinationsprobleme zwischen 112, 116117, Rettungsdienst, Notaufnahme und ambulantem Notdienst. Das kann eine **strukturbezogene Systemhypothese** stützen, aber nicht automatisch einzelne klinische Versorgungsfehler oder Todesursachen.

## 2. Historischer Untersuchungsraum: mindestens sechs Zeit- und Entscheidungsachsen

`Jahr → Quartal → Woche/Tag (bei saisonaler Spitze) → Region → Leistung/Einrichtung → Beleg`.

1. **Bedarf:** geschätzte Hilfesuchende, Diagnosen, Pflegegrad, stationäre Nachfrage, Altersstruktur, saisonale Krankheitslast.
2. **Kapazität:** Verträge, Planbetten, betriebene Betten, Personal/FTE, freie Plätze, Spezialfähigkeit, Bereitschaft, Terminfenster.
3. **Zugang:** Antrag/Erstsuche, Wartebeginn, Kontaktversuche, Erstberatung, reale Aufnahme, Ablehnung und alternative Vermittlung.
4. **Warnungen:** Datum der öffentlichen/interinstitutionellen Warnung, Sprecher, konkretes Risiko, erwarteter Zeitraum, Vorhersagegüte, Empfänger.
5. **Entscheidungen:** Verantwortungsbereich, Haushalts-/Personal-/Planungsbeschluss, Ressourcenzuweisung, Maßnahme, Kontrolle, Änderung.
6. **Folgen:** belegte Verzögerungen, zusätzliche Risiken, Morbidität, Mortalität, alternative Erklärung und kontrafaktische Begutachtung.

**Forschungsdesign:** Vor jedem bekannten Engpass die damals **bereits verfügbare** Datenlage rekonstruieren. Nachträglich eingetretene Todesfälle oder Kapazitätsengpässe dürfen nicht zur scheinbar sicheren Vorhersage rückprojiziert werden.

## 3. Frühwarn- und Versäumnis-Matrix

| Prüfstufe | Wissenschaftliche Frage | Benötigter Beleg |
| --- | --- | --- |
| W1 Warnsignal | War ein spezifisches Defizit vor der Hochsaison bekannt? | datierte Warnungen, Bedarfsplanung, Prognosen |
| W2 Vorhersagbarkeit | War die Risikospitze bei damaligem Wissen vernünftig vorhersehbar? | Zeitreihen, Bandbreite, Prognosefehler |
| W3 Zuständigkeit | Wer konnte rechtlich/tatsächlich welche Gegenmaßnahme veranlassen? | Kompetenz-, Vertrags-, Aufsichts- und Entscheidungsakte |
| W4 Handlung | Welche Maßnahmen wurden geplant, finanziert oder verworfen? | Protokolle, Budgets, Stellen-/Bedarfspläne, Beschlüsse |
| W5 Engpass | Trat tatsächlich eine für die konkrete Versorgung relevante Kapazitätslücke ein? | Wochen-/Tagesdaten, Betriebsfähigkeit, Verweisungen |
| W6 Schaden | Trat ein konkreter medizinischer Schaden oder Todesfall ein? | unabhängiger klinischer/gerichtlicher Befund |
| W7 Kausalität | Wäre der Schaden durch rechtzeitig mögliche Maßnahmen vermeidbar gewesen? | differenzierte fachliche Gegenhypothesen |
| W8 rechtliche Pflicht | Bestand eine einschlägige individuelle/institutionelle Handlungspflicht? | überprüftes Recht und Rollen der Akteure |
| W9 Verschulden | Welche Kenntnisse, Sorgfaltsmaßstäbe und Entscheidungsspielräume bestanden? | zeitgenössische Belege, ggf. gerichtliche Feststellung |
| W10 Vorsatz | Liegen Belege für den jeweils rechtlich erforderlichen subjektiven Tatbestand vor? | gesonderte Prüfung; bloße Warnungen genügen **nicht** |

Diese Reihenfolge verhindert sowohl eine pauschale Entlastung („Kapazität ist immer knapp“) als auch einen unbegründeten strafrechtlichen Vorwurf („Warnung + späteres Unglück = Vorsatz“).

## 4. Todesfälle und Pflichtverletzungen: Beweisordnung statt Verdachtsautomatik

### Epidemiologischer Zusammenhang
Statistische Zusammenhänge zwischen hoher Belastung, Wartezeiten, Personalmangel und ungünstigen Outcomes können **Hypothesen** generieren. Übersterblichkeits- oder krankheitsassoziierte Todesfallzahlen dürfen nicht automatisch einer organisatorischen Fehlplanung zugeschrieben werden. Dafür sind Risikoadjustierung, konkurrierende Erklärungen und möglichst überprüfbare Gegenfaktoren nötig.

### Medizinische und zivilrechtliche Ebene
[§ 630h BGB](https://www.gesetze-im-internet.de/bgb/__630h.html) enthält bestimmte Regeln zur Beweislast bei Behandlungs- und Aufklärungsfehlern, beispielsweise bei groben Behandlungsfehlern und Dokumentationsmängeln. **Nicht jeder Warte- oder Kapazitätsengpass erfüllt diese Merkmale.** Prüfung von Behandlungsverhältnis, konkreter Handlung, Befunderhebung, Organisationspflicht, Kausalität, Schaden und Dokumentation getrennt durchführen.

### Strafrecht und Unterlassen
[§ 13 StGB](https://www.gesetze-im-internet.de/stgb/__13.html) betrifft eine besondere rechtliche Einstandspflicht bei bestimmten Unterlassensdelikten. [§ 222 StGB](https://www.gesetze-im-internet.de/stgb/__222.html) erfasst fahrlässige Tötung, wenn die jeweiligen Voraussetzungen belegt sind. [§ 15 StGB](https://www.gesetze-im-internet.de/stgb/__15.html) unterscheidet den Grundsatz vorsätzlicher Strafbarkeit und ausdrücklich erfasste Fahrlässigkeit.

**Zentrale Begrenzung:** Eine Warnung vor zu wenigen Betten kann Kenntnis eines allgemeinen Risikos dokumentieren. Sie beweist weder eine konkrete Garantstellung noch die Vermeidbarkeit eines bestimmten Todesfalls, individuelle Schuld oder das Bewusstsein und Wollen bzw. Inkaufnehmen eines tatbestandlichen Erfolgs.

### Amtliche Verantwortung und Gerichtsentscheidungen
Getrennte Aktenkategorien: Planungs-/Aufsichtsfehler, unterlassene Kapazitätsausweitung, Organisationspflichtverletzung, ärztlicher Behandlungsfehler, Fehler in der Rettungslogistik, Budgetentscheidung, Verweisungsversagen, Gegenmaßnahmen, gerichtliche Beweisaufnahme und bindende Entscheidung. **Aus dem Urteil eines Einzelfalls dürfen nicht ungeprüft pauschale Aussagen über alle Einrichtungen gezogen werden.**

## 4a. Bereits belegte Todesfolgen medizinischer Fehler – ausdrücklich keine Kapazitätskausalität

Der [Medizinische Dienst Bund](https://md-bund.de/presse/pressemitteilungen/neueste-pressemitteilungen/vermeidbare-gesundheitsschaeden-verursachen-milliardenkosten-einsparpotenziale-durch-mehr-patientensicherheit-nutzen.html) berichtete am 20. August 2026 über die Begutachtung von **11.735 Behandlungsfehlervorwürfen im Jahr 2025**. Es wurden **2.700 Fälle mit ursächlichem Fehlerschaden** bestätigt; in **97 Fällen** führte der Fehler zum Tod oder trug wesentlich dazu bei. Die öffentlichen [Jahresberichte 2022–2025](https://md-bund.de/richtlinien-publikationen/behandlungsfehler.html) erlauben eine separate historisch-methodische Vergleichsarbeit.

**Entscheidende Nichtentsprechung:** Die 97 ärztlich begutachteten fehlerbezogenen Todesfälle sind **nicht** als 97 Todesfälle infolge von Therapieplatz-, Pflegeplatz- oder Intensivbettenmangel belegt. Um eine solche Teilmenge zu identifizieren, wären fallbezogene, rechtmäßig zugängliche, nachweisbare Kategorien zum Kapazitätsengpass, zur Kausalität, zum Behandlungspfad und zur Versorgungssituation nötig. Der Atlas darf weder Todesfälle aus allgemeinen Mortalitätszahlen noch Behandlungsfehler pauschal als Unterversorgungsschäden etikettieren.

**Erster konkreter Forschungsauftrag:** Die publizierte MD-Statistik nach Pflege, Notaufnahme, stationärer Versorgung und organisatorischen Ursachen auswerten. Für die Unterversorgungskarte wird eine getrennte Kategorie `error_causality_confirmed_capacity_causality_not_tested` geführt.

## 5. Wie prüfen wir „Hochsaison trotz Ansage“?

**Retrospektiver Prüfpfad `CAP-SEASON-01`:**
1. Zu einer Saison und Region den **vor der Saison** zugänglichen Warnbestand fixieren.
2. Den angekündigten Bedarf samt Prognoseunsicherheit, relevanter Erkrankung und erwarteter Woche dokumentieren.
3. Den damals entscheidungsbefugten Träger und realistische Beschaffungs-/Personalvorlaufzeiten bestimmen.
4. Planung und tatsächliche Maßnahmen mit Datum auswerten (Stellen, Vertretungen, Umverteilung, Transport, Reserve, Termin-/Bettensteuerung).
5. Betriebliche Kapazität gegen Tages-/Wochenbedarf prüfen – nicht Jahresdurchschnitt gegen Tageshöchstwert.
6. Überläufe, Ablehnungen, Übergabeverzögerungen und Umverteilungen nachweisen.
7. Gesundheitliche Folgen separat und risikoadjustiert untersuchen.
8. Gegenhypothesen: unvorhersehbare Wellenstärke, kurzfristige Personalausfälle, geänderte Behandlungspraxis, lokale Spezialbedarfe, Patient:innenwünsche.
9. Bei konkreten Schäden fachliches Kausalitätsgutachten; erst danach rechtliche Verantwortung prüfen.
10. Nachfolgende Reformen/Änderungen und ihre messbaren Auswirkungen als eigenen Test erfassen.

**Bewertungsstatus:** `warning_found`, `action_documented`, `action_missing_unverified`, `operational_shortage_confirmed`, `outcome_associated`, `causal_link_established`, `legal_breach_found`, `intent_established`. Diese Stufen dürfen nicht ineinander übergehen.

## 6. Gerichte, Sozialgerichte und institutionelle Rechtswege

Für den Forschungsgraphen sind mehrere getrennte Streittypen relevant:
- **Leistungsrecht:** Versorgung nach SGB V, Pflegeleistungen nach SGB XI; gerichtliche Klärung typischerweise im Sozialrecht.
- **Bedarfsplanung:** Vertragspsychotherapie, Ermächtigungen, Sitzverteilung; andere Verfahren und Klägerrechte als individuelle Leistungsstreitigkeiten.
- **Zivilrechtliche Haftung:** konkreter Behandlungs-/Organisationsfehler samt Schaden und Kausalität.
- **Strafrecht:** Verletzungs-/Tötungsdelikte, besondere Unterlassenspflichten und subjektiver Tatbestand, jeweils individuell.
- **Aufsicht und Struktur:** Krankenhaus- und Pflegeheimaufsicht, Bedarfspläne, Qualitätssicherung, Vertrags-/Förderentscheidungen.

**Juristische Quellensuche für Folgearbeit:** Sozialgerichtsbarkeit/Bundessozialgericht, Bundesgerichtshof, Oberlandesgerichte, Veröffentlichungen der Landeskrankenhausplanung, MD-/Qualitätsberichte, Schlichtungsstellen, Prüfberichte und parlamentarische Drucksachen. Fallberichte sind zuerst zu typisieren (Vorwurf / Ermittlungen / Gutachten / Urteil / rechtskräftig / offen); in dieser Fassung **kein konkretes Todesfallurteil als einschlägig validiert**.

## 7. Standards, Datenquellen und Definitionen

| Familie | Primärdaten | Typische Schwäche |
| --- | --- | --- |
| Therapie | KBV, BPtK, vdek, G-BA, KVen, 116117, Kassen | unterschiedliche Start- und Endpunkte von Wartezeit |
| Pflege | Destatis GENESIS 22412, BMG, Kassen, Landesheimplanung | kein bundesweites Echtzeitregister kurzfristig aufnahmefähiger Plätze |
| Akut-/Intensivbetten | Destatis 23111, DIVI, RKI, Landeskrankenhauspläne, Notfallrettung | Jahreskapazität ≠ tägliche betriebsbereite Sonderkapazität |
| Saison | RKI ARE/SARI/Influenza/RSV, DIVI, Rettungsdienst | Krankheitslast ≠ nachgewiesener Versorgungsfehler |
| Frühwarnung | Landesausschüsse, Klinikträger, Verbände, Prüfberichte, Parlamente | Prognosegüte und Maßnahmenräume rekonstruieren |
| Folgen | Morbidität, Mortalität, Beschwerden, Gutachten, Gerichtsurteile | Selektionsbias und nicht automatisch nachgewiesene Kausalität |

## 8. Umsetzungsobjekte im Bürger-KI-Handlungsatlas

`need_class → capacity_type → time_window → region → demand_indicator → operational_capacity → access_event → shortage_claim → warning → competent_actor → decision/mitigation → harm_indicator → causal_review → judicial_finding → skill_test`.

Minimalschema pro Befund:
```json
{
  "claim_id": "BKI-CAP-EXAMPLE-01",
  "service": "psychotherapy|residential_care|emergency_icu",
  "jurisdiction": "DE",
  "area": "not_established",
  "interval": "not_established",
  "unit": "persons|requests|days|licensed_places|staffed_places|free_places",
  "demand": null,
  "capacity": null,
  "access_delay": null,
  "warning_source_id": null,
  "warning_published_before_event": null,
  "mitigation_evidence_ids": [],
  "harm_evidence_ids": [],
  "causality": "not_established",
  "applicable_duty": "not_reviewed",
  "fault": "not_reviewed",
  "intent": "not_established",
  "provenance": [],
  "original_text_stored": false,
  "review": "research_candidate"
}
```

Das Schema enthält absichtlich keine individuellen Bürgerfälle. Der später nötige medizinische/gerichtliche Einzelfallbezug wird zunächst ausschließlich durch öffentlich dokumentierte, extern referenzierte Entscheidungen und geprüfte Fallklassen erfasst.

## 9. Sechs falsifizierbare Forschungsaufträge

**CAP-EXP-01 Therapie:** Zwei explizit verschieden definierte Wartedauer-Indikatoren über 2019–2024 vergleichen. Eine scheinbar schnelle Probatorik darf nicht zum Nachweis eines vollständig verfügbaren Therapieplatzes werden.

**CAP-EXP-02 Pflege:** Verfügbare statistische Plätze, tatsächlich versorgte Personen, regionalen Bedarf und belegbare Aufnahmesperren getrennt auf Länder-/Kreisebene untersuchen. Die rechnerische Differenz von Plätzen und Bewohnern ist keine belegte freie Vermittlungskapazität.

**CAP-EXP-03 Notfallbett:** Für zwei Grippe-/RSV-Saisons tagesbasierte Intensivressourcen mit RKI-Krankheitslast, lokalen Krankenhaus-/Rettungsdienstmeldungen und vorab datierten Kapazitätswarnungen vergleichen. Krankenhaus- und Intensivkapazität strikt trennen.

**CAP-EXP-04 Vorwarnungsatlas:** Für eine Region alle vor einer bekannten Hochsaison veröffentlichten relevanten Warnungen sammeln, mit dokumentierten Maßnahmen und zeitlichem Vorlauf vergleichen. Notwendige Zwischenstufen bei fehlenden Quellen auf `unknown` lassen.

**CAP-EXP-05 Gerichts-/Schadensakten:** Eine methodische Matrix von öffentlich belegten, geeigneten Urteilen und Sachverhalten erstellen. Keine unbestätigte Zuschreibung eines Todesfalls zu Bettenmangel. Nach zivil-/sozial-/strafrechtlichem Gegenstand trennen.

**CAP-EXP-06 Systemwirkung:** Vor-/Nachher-Vergleich geeigneter Kapazitäts-, Planungs- oder Steuerungsänderungen und negative Kontrollen, unter Kontrolle von demografischen, epidemiologischen und methodischen Veränderungen.

**Keine der sechs Studien ist durch den Quellenkatalog abgeschlossen.** Begutachtete Kausalitäts- oder Vorsatzbefunde liegen für diesen Piloten **nicht** vor.

## 10. Fazit und Priorität

Für die Bürger-KI ist Unterversorgung ein Paradebeispiel für das Ziel **„nicht nur einen Anspruch oder Kontakt finden, sondern tatsächliche Hilfe erreichen“**. Therapie und Pflege benötigen mehr als ein Organisationsverzeichnis: sie brauchen zeitliche Verfügbarkeit, Fachpassung, Aufnahmekapazität und nachvollziehbare Alternativen. Die Notfallversorgung benötigt zusätzlich detaillierte saisonale und tagesbezogene Kapazität und ein rückblickendes Warnungs-/Entscheidungsregister.

Die Frage, ob strukturelle Mängel zu vermeidbaren Todesfällen führen, ist **wissenschaftlich untersuchbar** – durch Zeitreihen, individuelle dokumentierte Schäden, klinische Gutachten, kontrafaktische Studien und juristische Prüfungen. Sie ist aber ohne diese Nachweise nicht zu entscheiden. Bei der Frage nach **Vorsatz** ist die Beweislast besonders hoch: Ein bekanntes abstraktes Risiko und eine möglicherweise unzureichende Politik sind keine automatische strafrechtliche Vorsatzzuschreibung.

**Reifegrad:** Quellen- und Forschungsdesign implementiert; 0 unabhängig überprüfte kausale Todesfallzuschreibungen, 0 fachlich abgenommene Haftungs-/Vorsatzfeststellungen. Gesamt-Bürger-KI-Programmzähler bleibt 3/10 Abnahme-Gates.

## Primärfundstellen

- [Destatis Krankenhäuser, Zeitreihe 1991–2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankenhauser/Tabellen/gd-krankenhaeuser-jahre.html)
- [Destatis Krankenhausdaten 2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankenhauser/Tabellen/eckzahlen-krankenhaeuser.html)
- [Destatis Pflegeplätze und Pflegebedürftige 1999–2023](https://genesis.destatis.de/datenbank/online/statistic/22412/table/22412-0010/search/s/Detailsuchezg)
- [Destatis Pflegebedürftigkeit 2023](https://www.destatis.de/DE/Presse/Pressemitteilungen/2024/12/PD24_478_224.html)
- [BPtK Wartezeitmethodik](https://www.bptk.de/pressemitteilungen/psychisch-kranke-warten-142-tage-auf-eine-psychotherapeutische-behandlung/)
- [vdek 2026 Psychotherapie-Kassenanalyse](https://www.vdek.com/presse/pressemitteilungen/2026/wartezeiten-psychotherapie-akutbehandlung.html)
- [KBV Unter-/Überversorgungsbeschlüsse](https://www.kbv.de/infothek/zahlen-und-fakten/gesundheitsdaten/bedarfsplanung-landesbeschluesse-ueber-unterversorgung)
- [DIVI/RKI historischer Kapazitätsdatensatz](https://zenodo.org/records/17899565)
- [RKI ARE/SARI Saisonbericht 2025/26](https://edoc.rki.de/bitstream/handle/176904/13996/ARE-Saisonbericht_RKI_2025_26.pdf?isAllowed=y&sequence=1)
- [BMG Notfallversorgungsreform](https://www.bundesgesundheitsministerium.de/service/gesetze-und-verordnungen/guv-21-lp/notfallreform/faq-notfallreform)
- [§ 630h BGB](https://www.gesetze-im-internet.de/bgb/__630h.html), [§ 13 StGB](https://www.gesetze-im-internet.de/stgb/__13.html), [§ 15 StGB](https://www.gesetze-im-internet.de/stgb/__15.html), [§ 222 StGB](https://www.gesetze-im-internet.de/stgb/__222.html)

*Dieses Paper dient der Entwicklung allgemeiner Bürger-KI-Fähigkeiten und verarbeitet keine persönlichen Versorgungsfälle.*
