# Myokarditis nach COVID-19-Impfungen: Warum veröffentlichte Risikozahlen nicht automatisch vergleichbar sind

**Bürger-KI · Corona-Forschung · Methodenpaper COR-MYO-METHOD-01 · Ausgabe 1.0 · 5. November 2026**  
**Redaktioneller Status:** Geschlossene methodische Fallstudie auf Grundlage des dokumentierten Quellenbestands. **Keine** vollständige Nutzen-Schaden-Bilanz, kein systematischer Review und keine endgültige Bewertung individueller Impfentscheidungen.

## Zusammenfassung
Eine historische Spontanmelderate des Paul-Ehrlich-Instituts (PEI) und die adjustierte Überschussinzidenz einer nordischen Bevölkerungsstudie zu Myokarditis können beide relevante Sicherheitssignale beschreiben. Sie schätzen aber unterschiedliche Sachverhalte. Ein bloßer Vergleich der Zahlenwerte würde Altersgruppen, Falldefinitionen, Erfassungssysteme und Beobachtungsfenster vermischen. Dieses Paper demonstriert an drei bereits im Projekt erfassten Zahlen, wie eine reproduzierbare Vergleichssperre begründet wird. Das Ergebnis ist eine überprüfbare **Methodenregel**, keine neue kausale Risikoschätzung.

## 1. Forschungsfrage und Abgrenzung
**Forschungsfrage:** Unter welchen Bedingungen darf eine Spontanmelderate direkt mit einer populationsbasierten, adjustierten zusätzlichen Diagnoserate verglichen werden?

Antwort im vorliegenden Fall: Ein direkter zahlenmäßiger Vergleich als gleiches Risiko ist **nicht zulässig**. Unterschiedliche Erfassungsmechanismen und Definitionen sind ausdrücklich als Vergleichshindernisse zu kennzeichnen.

Die Analyse bezieht sich auf vorliegende publizierte Angaben. Sie ersetzt weder eine unabhängige Volltext-/Datenreanalyse noch ein medizinisches Beratungsgespräch.

## 2. Drei Messgrößen – drei unterschiedliche Aussagen

| Kennung | Herkunft und Population | Was wird gezählt oder geschätzt? | Publizierte Größe |
| --- | --- | --- | --- |
| MYO-NUM-01 | PEI-Sicherheitsbericht; Jungen 12–17; zweite Comirnaty-Dosis; Berichtsstand 30.09.2021 | Verdachtsmeldungen Myo-/Perikarditis pro zweite Dosis | 1 je 13.812 Dosen, arithmetisch etwa 7,24 je 100.000 |
| MYO-NUM-02 | Nordische Kohorte; Männer 16–24; zweite BNT162b2-Dosis | Adjustierte **zusätzliche** Myokarditisdiagnosen im 28-Tage-Fenster | 5,55 je 100.000 (95%-KI 3,70–7,39) |
| MYO-NUM-03 | Dieselbe Kohorte; Männer 16–24; zweite mRNA-1273-Dosis | Adjustierte **zusätzliche** Myokarditisdiagnosen im 28-Tage-Fenster | 18,39 je 100.000 (95%-KI 9,05–27,72) |

Die Zahlen werden hier zur Dokumentation ihrer **verschiedenen Messdefinitionen** aufgeführt. Sie werden nicht zu einem gemeinsamen Risiko addiert oder gemittelt.

## 3. Vergleichssperre und mögliche Teilvergleiche
Eine Vergleichsprüfung muss mindestens sechs Bedingungen abfragen:

1. **Population:** Alter, Geschlecht, Einschluss- und Ausschlusskriterien;
2. **Exposition:** Impfstoff, Dosis, Zeitraum und Referenzgruppe;
3. **Endpunkt:** Verdachtsmeldung, ärztlich diagnostizierte Myokarditis oder kombinierter Myo-/Perikarditis-Endpunkt;
4. **Zeitfenster:** Zeitpunkt der Exposition, Nachbeobachtung und Berichtsstichtag;
5. **Schätzer:** Meldungen pro Dosis gegenüber adjustierten zusätzlichen Diagnosen;
6. **Unsicherheit:** Erfassungs-, Selektions-, Kodierungs- und Konfundierungsrisiken sowie berichtete Konfidenzintervalle.

**Negativtest:** Wird MYO-NUM-01 mit MYO-NUM-02 als dieselbe klinische Inzidenz dargestellt, muss die Prüfung mit der Begründung „ungleicher Endpunkt und Schätzer; unterschiedliche Population“ abbrechen.

**Eingeschränkter Teilvergleich:** MYO-NUM-02 und MYO-NUM-03 stammen aus derselben Kohorte und teilen wesentliche Methodenbestandteile. Unterschiede zwischen Impfstoffgruppen sind dennoch nicht automatisch kausal, da Zuordnung und übrige Unterschiede berücksichtigt werden müssen.

## 4. Historische Warnkommunikation: Wissen zum jeweiligen Zeitpunkt
Dokumentiert sind frühe Hinweise aus Israel im Frühjahr 2021, öffentlich kommunizierte US-Pharmakovigilanz im Juni 2021, ein PEI-Sicherheitsbericht mit Stichtag Ende September 2021 und eine STIKO-Mitteilung vom 10. November 2021 zur Bevorzugung von Comirnaty bei unter 30-Jährigen. Größere veröffentlichte Kohortenanalysen folgten 2022.

Diese zeitliche Folge zeigt, dass die Behauptung, das Sicherheitssignal sei erst 2022 oder 2023 bekannt geworden, sachlich nicht trägt. **Sie beweist allein noch keine konkrete behördliche Verzögerung.** Dazu müssten Erhebungs-, Kenntnis-, Beratungs-, Entscheidungs- und Veröffentlichungszeitpunkte getrennt rekonstruiert werden.

## 5. Unsicherheiten und Gegenproben
- Spontanmeldungen sind keine bestätigte Krankheitsinzidenz; Unter- und Übermeldung sind zu prüfen.
- Kohortendiagnosen beruhen auf Falldefinitionen, Kodierung, Auswahl und statistischer Adjustierung; Residualkonfundierung bleibt möglich.
- Ein Vergleich unterschiedlicher Altersgruppen oder unterschiedlicher Endpunkte darf nicht durch die identische Einheit „pro 100.000“ legitimiert werden.
- Ein beobachtetes Impfrisiko ist **keine** vollständige Bilanz aus Impf- und Infektionsrisiken, Erkrankungsschwere, Zeitstand und individuellen Voraussetzungen.
- Eine formale GRADE-Bewertung eines definierten Evidenzkörpers liegt in diesem Pilot nicht vor; ein Gesamt-Evidenzgrad wird nicht erfunden.

## 6. Reproduzierbarer Mini-Test
Eingabe sind drei Datensätze mit den Feldern `source_id`, `population`, `vaccine`, `dose`, `endpoint`, `estimator`, `risk_window`, `unit`, `uncertainty` und `knowledge_cutoff`. Der Prüfschritt stellt zuerst Messdefinitionen gegenüber und entscheidet dann `directly_comparable`, `conditionally_comparable` oder `not_directly_comparable`, jeweils mit einer konkreten Begründung.

Die arithmetische Umrechnung `100000 / 13812 ≈ 7.24` ändert **nicht** den Charakter der PEI-Verdachtsmeldungen. Der vorhandene [synthetisch strukturierte Vergleichsdatensatz](./data/bki-corona-myokarditis-zahlenvergleich-pilot-v0-1.json) dokumentiert diese Unterschiede. Ein vollständiger externer Reproduktionstest wurde hier nicht durchgeführt.

## 7. Ergebnisse, Grenzen und verbleibender Deep Dive
**Als methodischer Befund geschlossen:** Gleiche Einheiten garantieren nicht gleiche Messobjekte. Der direkte Vergleich der PEI-Meldungen mit der adjustierten Nordic-Zusatzinzidenz ist in dieser Konstellation gesperrt. Der Zeitbezug von Sicherheitshinweisen gehört zur Auswertung.

**Weiterhin offen:** fachliche Validierung jedes Originalwerts und seiner Quellenversion, Alters-/Dosis-/Produkt-spezifische Impf-gegen-Infektions-Risiken, absolute Hintergrundraten, Krankheitsverläufe, klinische Langzeitfolgen und ein vollständiges historisches Behörden-/Medien- und Entscheidungs-Audit. Dafür sind separate Deep Dives notwendig.

Das Paper kann deshalb **als abgegrenzte Methodenstudie** veröffentlicht werden, aber ausdrücklich nicht als abschließender Überblick über Myokarditis und COVID-19-Impfungen.

## Quellen und zugehörige Akten
1. [Paul-Ehrlich-Institut: Sicherheitsbericht bis 30. September 2021](https://www.pei.de/SharedDocs/Downloads/EN/newsroom-en/dossiers/safety-reports/safety-report-27-december-2020-30-september-2021.pdf?__blob=publicationFile&v=9).
2. [Nordische Bevölkerungs-Kohortenstudie, JAMA Cardiology 2022](https://jamanetwork.com/journals/jamacardiology/fullarticle/2791253).
3. [STIKO: Pressemitteilung 10. November 2021](https://www.rki.de/DE/Themen/Infektionskrankheiten/Impfen/Staendige-Impfkommission/Empfehlungen-der-STIKO/PM/PM_2021-11-10.html).
4. [RKI Epidemiologisches Bulletin 46/2021](https://www.rki.de/DE/Aktuelles/Publikationen/Epidemiologisches-Bulletin/2021/46_21.pdf?__blob=publicationFile&v=1).
5. [Erste projektinterne Zahlenakte](./paper-corona-myokarditis-zahlen-fruehwarn-pilot-2026-11-05.md).
6. [Myokarditis-Medienanalysen 11–20](./paper-corona-myokarditis-medien-011-020-erste-analyse-2026-11-05.md).

**Provenienz:** Die konkrete Zahlen- und Quellenbasis wurde aus der vorhandenen Projektakte COR-MYO-01 übernommen. Diese Ausgabe präzisiert Vergleichslogik, Grenzen, methodisches Ergebnis und noch offene Aufträge. Keine neuen Primärdaten erhoben.
