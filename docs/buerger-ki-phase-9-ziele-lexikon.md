# Phase 9 – Zieleatlas, Lexikon und Metaebene

**ID:** BKI-PH9-001 · **Version:** 0.1 · **Stand:** 05.11.2026  
**Referenz:** [Kernpaper](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/KERNPAPER_ZIEL_HANDLUNGSATLAS_LEXIKON_META_V0_1.md)  
**Status:** Eigenständiger maschinenlesbarer Startbestand und einfache lokale Such-/Lexikonansicht implementiert. Kein durchgeführter unabhängiger Fach- oder Nutzertest.

## 1. Ziel

Der Handlungsatlas erhält (a) einen mehrdeutigkeitsbewussten, multilingual erweiterbaren Begriffs- und Facherklärungsraum und (b) einen von menschlichen Zielen ausgehenden Handlungsgraphen. Wikipedia/Wikidata dürfen Identifikationskandidaten liefern, aber niemals fachrechtliche Gleichheit und behördliche Bindung allein beweisen.

## 2. Neue Artefakte

- [12 erste Begriffskarten, 8 Ziele, 7 Relationskandidaten, 6 synthetische Aufgaben](./data/bki-ziele-lexikon-kernel-v0-1.json).
- [Suchbare Lexikon-/Ziele-/Testansicht](./buerger-ki-ziele-lexikon.html).
- [Kernpaper mit Abdeckungslücken, Identitätstest und Atlasfamilien](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/KERNPAPER_ZIEL_HANDLUNGSATLAS_LEXIKON_META_V0_1.md).

### Standgrenze

Die zwölf Definitionen sind eigene didaktische **Entwürfe**, keine fachlich unabhängig geprüften Lexikoneinträge. Bei Wikidata ist `wikidata_qid=null` absichtlich gesetzt: Eine plausible Q-ID ohne tatsächliche Identitätsprüfung wäre ein Qualitätsmangel. Wikipedia-Links sind Rechercheverweise und keine Bestätigung der Rechtsgeltung. Die sechs Testkarten sind **nicht ausgeführt**.

## 3. Ausführbare Abnahmebedingungen

**PH9-A Lexikonstatus und Quellenklassen:** Jeder Begriff muss `concept_id`, eigene Definition, Fachraum, Geltungsraum, Alias, unabhängigen Status und Quellenrollen besitzen. 12/12 Strukturkandidaten erfasst, fachliche Prüfung 0/12.

**PH9-B Begriffsidentität:** Wikidata-Q-ID und Wikipedia-Artikel dürfen nur zugeordnet werden, wenn die Zielentität, die gewählte Bedeutung und der konkrete Rechtsraum unabhängig geprüft wurden. Status: 0 geprüfte Q-IDs.

**PH9-C Zielgraph:** Ziel, Erfolgskriterium, Teilziel, Handlungsoption, Hindernis und Gegenfall maschinenlesbar trennen. 8 Entwürfe, 0 unabhängig abgenommen.

**PH9-D Verbindung zum Weisungsatlas:** Ein Ziel → Begriff → Normregime → Behörde → Option → Skill → Evidenz mit überprüfter negativer Relation. Status: Architektur definiert, kein fachlich freigegebener End-to-End-Fall.

**PH9-E KI-Vergleich:** S0 Direkt, S1 Lexikon, S2 Lexikon+Ziel, S3 plus Quellenprüfung auf dieselben sechs Aufgaben; mehrfach wiederholen, unabhängige Prüfer und festes Quellenfenster. Status: 0 KI-Ausführungen.

**PH9-F Ausweitung:** 100 fachlich eingeordnete Begriffe, 30 belegte disambiguierende Beziehungen, 20 Zielmodelle und mindestens 30 synthetische Aufgaben als Forschungsziele. Noch nicht erreicht.

## 4. Zentrale negative Befunde

1. Gleicher Ausdruck bedeutet nicht denselben Fachbegriff.
2. Wikidata-Entität bedeutet nicht identische gesetzliche Begriffsdefinition.
3. Ein Wikipedia-Link liefert keine aktuelle Behördenanweisung.
4. „Bewilligung“ und „Erfüllung“ dürfen nicht verschmolzen werden.
5. Jugendamt und KESB besitzen ähnliche Schutzfunktionen, aber unterschiedliche Organisations- und Rechtsrahmen.
6. Das Ziel einer Person darf nicht aus dem Namen eines Behördenformulars abgeleitet werden.
7. Ein hohes Linkvolumen beweist keine gute Abdeckung.

## 5. Messkonzept

Getrennte Entwicklungskennzahlen statt irreführender Gesamtquote: Begriffskarten angelegt/geprüft, semantische Kanten vorgeschlagen/geprüft, Ziele dokumentiert/abgenommen, Tests definiert/ausgeführt, tatsächliche KI-Strategieverbesserung und Fehlerhäufigkeit. Der allgemeine Bürger-KI-Gesamtfortschritt bleibt **3 von 10 bisherigen Abnahme-Gates = 30 %**, da keines der alten empirischen Gates durch die neue Architektur automatisch bestanden ist.

## 6. Nächster substanzieller Test

Einen kontrollierten lexikalischen **Fehlzuordnungs-Benchmark** zuerst mit „Bewilligung/Erfüllung“, „Leistungsobjekt/Verrichtung“ und „Jugendamt/KESB“ durchführen. Erwartetes Resultat ist **nicht** maximale Gleichsetzung, sondern richtige Trennung. Erst nach unabhängigem Review wird der automatische Wikipedia-/Wikidata-Abgleich zugeschaltet.

## 7. No-Loss-Synchronisation

Kette: `Quelle → Begriff/Sinn → Lexikon-Relation → Ziel/Erfolgskriterium → Norm/Behördenzuständigkeit → Handlungsoption → Skill/Test → Gegenprobe → freigegebene Publikation`.

Das bisherige Glossar und Quellenregister werden durch Crosswalk-IDs angebunden; keine unbelegte Behauptung, alle historischen Registerdateien seien bereits technisch zusammengeführt. Die originale Arbeitsregel „keine Originaltexte in eigenen Handlungsanweisungen“ bleibt unverändert gültig.
