# Zwischen Worten und Wirklichkeit
## Sprachräume, Termini, Operationalisierungen, Perspektivwechsel und Claims in Bürger-KI, SOULution und KI-Tensor

**Paper-ID:** BKI-LANGUAGE-001 · **Version:** 0.2 · **Stand:** 05.11.2026  
**Status:** Erweiterter Forschungsentwurf mit geprüftem Projektbestand, belegten methodischen Referenzen, eigenen Hypothesen und vorgeschlagenen Tests. Keine abgeschlossene empirische Sprachraumanalyse.  
**Claim-Register:** [Sprachräume und Perspektivwechsel v0.1](./data/bki-sprachraeume-claims-v0-1.json)  
**Anknüpfung:** [Originalsprache und Redaktion](./paper-buerger-ki-originalsprache-claims-didaktik-no-loss-v0-1.md) · [Bürger-KI](./buerger-ki.html) · [Forschungsbibliothek](./buerger-ki-forschungsbibliothek.html)

> **Leitgedanke:** Dieselbe Situation kann als Anliegen, Anspruch, Verwaltungsfall, Kennzahl, politisches Versprechen, wissenschaftliche These oder KI-Aufgabe beschrieben werden. Jede Beschreibung erschließt etwas – und kann etwas anderes verdecken. Die Perspektiven müssen ineinander übersetzbar sein, ohne ihre Unterschiede aufzulösen.

## Abstract

Dieses Paper analysiert nicht nur den Stil der Bürger-KI, sondern die Bedeutungsebenen und gesellschaftlichen Funktionen von Sprache. Im Mittelpunkt stehen (1) Sprachräume und Sprecherpositionen, (2) Begriffs- und Definitionsgeschichte, (3) Aussagenarten und Geltungsbedingungen, (4) Operationalisierung und Messbarkeit, (5) Perspektivwechsel und deren Invarianten, (6) differenzierte Thesenprüfung, (7) didaktische Wege sowie (8) eine eigene Claim-Architektur. Die zuvor verifizierten 21 redaktionellen Anker bleiben historisch erhalten. Neue Formulierungen sind als **Vorschläge**, wissenschaftliche Aussagen als **Hypothesen** oder **methodische Regeln** markiert.

Das zentrale Forschungspotenzial liegt in einer prüfbaren Frage: **Wie oft verändert ein Wechsel des Sprachraums den Gegenstand, das Erfolgskriterium, die zugeschriebene Verantwortung oder den Geltungsanspruch?** Dafür werden Vergleichs- und Gegenproben spezifiziert, nicht erfundene Messergebnisse.

## 1. Stand und Abgrenzung

Der bestehende Projektvergleich [Originalsprache und Claims](./paper-buerger-ki-originalsprache-claims-didaktik-no-loss-v0-1.md) dokumentiert 64 historische Überschriften, die erhalten geblieben sind, sowie 21 redaktionelle Anker. Eine frühere dramaturgische Verdrängung des menschlichen Einstiegs wurde durch Umordnung korrigiert. Danach wurden die kuratierte Forschungsbibliothek und der Verweis auf diesen Redaktionsaudit verbunden (Git-Stand 1f034353, 05.11.2026). Offen bleiben insbesondere echte Browser-, Nutzungs- und Verständnistests. Diese Arbeit setzt darauf auf, ersetzt sie aber nicht.

**Projektrahmen:** Die Bürger-KI entwickelt allgemeine, prüfbare Skills, damit Menschen Ziele besser verstehen und Handlungswege erkunden können. Sie ist kein System zur Sammlung oder Bearbeitung individueller Bürgerfälle. SOULution verbindet Forschungs- und Lösungsbereiche. Der KI-Tensor untersucht eigenständige mathematische und relationale Strukturen; sprachliche Analogien sind noch keine mathematischen Isomorphismen.

**Nicht behauptet:** repräsentative Aussagen über Behördenkommunikation, erwiesene KI-Wirksamkeit, vollständige Fachterminologie, verbindliche Rechtsauslegung oder die Schuld einzelner Institutionen.

## 2. Welche Sprachen? Welche Sprachräume?

Wir trennen drei Achsen. **Natürliche Sprachen** (z. B. Deutsch/Englisch und regionale Varianten), **fachlich-institutionelle Sprachräume** (wer mit welchem Zweck spricht) und **formale Repräsentationen** (Normen, Formeln, Ontologien, Datenfelder, Prompts). Ein Sprachraum ist hier ein *analytisches Modell*, kein homogenes soziales Milieu: Sprecher können mehrere Räume gleichzeitig nutzen.

| Sprachraum | Leitfrage | Typische Einheit | Risiko des Übergangs |
| --- | --- | --- | --- |
| Alltag und Lebenswelt | Was fehlt? Was will ich erreichen? | Erlebnis, Wunsch, Situation | als bloß subjektiv abgewertet |
| Recht | Welche Norm, Tatbestandsmerkmale und Rechtsfolge gelten? | Anspruch, Pflicht, Ermessen, Beweislast | aus allgemeinem Ziel wird scheinbar einklagbarer Anspruch |
| Verwaltung | Welcher Vorgang ist zuständig und wie wird entschieden? | Antrag, Bescheid, Frist, Zuständigkeit | Erledigung des Vorgangs wird mit Zielerreichung verwechselt |
| Medizin, Pflege, Soziales | Welcher Bedarf und welche geeignete Unterstützung bestehen? | Indikation, Angebot, Eignung, Zugang | Kontakt oder Ersttermin wird mit Versorgung gleichgesetzt |
| Wissenschaft | Was ist behauptet, gemessen, widerlegt oder offen? | Hypothese, Population, Indikator, Unsicherheit | Kennzahl wird ohne Definitionsgeschichte verallgemeinert |
| Politik und öffentliche Rechenschaft | Was wird versprochen, finanziert, gesteuert, evaluiert? | Programm, Ziel, Budget, Wirkung | Maßnahme wird mit Wirkung gleichgesetzt |
| Medien und Öffentlichkeit | Was wird sichtbar, betont und weitergegeben? | Schlagzeile, Narrativ, Korrektur | Zuspitzung oder Reichweite ersetzt Evidenz |
| Bildung und Didaktik | Was muss verstanden und selbst angewandt werden können? | Frage, Beispiel, Lernschritt, Gegenbeispiel | Vereinfachung tilgt entscheidende Bedingungen |
| KI, Daten und Software | Wie wird eine Frage spezifiziert und geprüft? | Prompt, Skill, Relation, Test, Provenienz | plausibler Text wird als validierte Fähigkeit behandelt |
| SOULution / KI-Tensor | Welche Beziehungen sind übertragbar, welche nicht? | Quellenknoten, Relation, Trinität, Tensor, Beweisakte | gemeinsames Vokabular wird als gemeinsame Algebra missverstanden |

**Die wichtige zusätzliche Achse ist die Sprecherposition**: betroffene Person, beratende Stelle, Leistungsträger, Leistungserbringer, Prüfinstanz, Forschende, Journalist, KI-System. Dieselbe Terminologie kann je Sprecher andere Interessen und Kompetenzen haben. Diese Unterschiede sind zunächst zu rekonstruieren, nicht pauschal zu unterstellen.

## 3. Terminologie: Ein Wort, mehrere Bedeutungen

Die Terminologiearbeit unterscheidet Objekt, Begriff, Benennung und Definition; ISO 704:2022 gibt hierfür einen einschlägigen methodischen Rahmen [Q1]. W3C SKOS bietet u. a. bevorzugte und alternative Benennungen sowie hierarchische und assoziative Relationen zwischen Konzepten [Q2].

**Beispielreihe (Forschungsfragen, keine Gleichsetzungen):**

| Wort | Mögliche unterschiedliche Lesarten | Notwendige Trennung |
| --- | --- | --- |
| Bedarf | subjektiv geäußertes Bedürfnis / fachlich festgestellter Bedarf / statistischer Planungsbedarf | wer definiert, nach welcher Regel, für wen? |
| Anspruch | moralisches Anliegen / Leistungsanspruch aus einer Norm / politischer Anspruch | Rechtsquelle und Voraussetzungen |
| Zugang | erreichbare Information / formale Berechtigung / tatsächlicher geeigneter Leistungsbeginn | Zeitpunkt, Verfügbarkeit und Nutzbarkeit |
| Versorgung | Struktur, Kapazität, Kontakt, Termin, laufende geeignete Leistung | Prozess- und Ergebnisindikator |
| Erfolg | Antrag gestellt / Entscheidung ergangen / Leistung bewilligt / Ziel tatsächlich erreicht | ausdrücklich festgelegtes Zielkriterium |
| Evidenz | Beleg / empirische Studienlage / rechtlicher Beweis / öffentliche Sichtbarkeit | Beweisstandard und Kontext |
| Kontrolle | Überwachung / Qualitätsprüfung / Rechenschaft / Gegenprobe | prüfende Instanz, Befugnis, Maßstab |
| Verantwortung | Zuständigkeit / Pflicht / kausaler Beitrag / Vorwerfbarkeit | keine automatische Ableitung aus einem Befund |
| Vernetzung | Links / gemeinsame Terminologie / wiederverwendbare Skills / Koordination | kein Schluss auf zentrale Fall- oder Datensammlung |
| Tensor | mathematischer Tensorbegriff / projektspezifische 3×3×3-Struktur | explizite Definition, Abbildungs- und Invarianztest |

**Begriffsakte als Minimalvertrag:** `concept_id`, `surface_forms[]`, `language`, `domain`, `jurisdiction`, `valid_from/to`, `definition`, `source_ids[]`, `broader/narrower/related`, `operationalizations[]`, `counterexamples[]`, `owner`, `review_status`. Das Wort ist kein eindeutiger Schlüssel. Fachlich verschiedene Bedeutungen behalten eigene Sinn-IDs; bloße Synonyme erhalten keine neue Sachidentität.

## 4. Sprache ist nicht gleich Aussage: Anspruchstypen

Für die Analyse wird jede Aussage typisiert:

1. **Erlebnis-/Anliegenaussage:** Eine Person berichtet ein Problem oder Ziel.
2. **Deskriptive Aussage:** Eine Quelle berichtet einen Zustand, ein Ereignis oder eine Verteilung.
3. **Definitorische Aussage:** Ein Begriff gilt in einem ausdrücklich definierten Rahmen.
4. **Normative Aussage:** Ein Recht, eine Pflicht, ein Soll oder ein Versprechen wird behauptet.
5. **Kausalaussage:** Eine Ursache-Wirkungs-Verbindung wird postuliert.
6. **Prognose:** Eine bedingte Zukunftsaussage wird gemacht.
7. **Methodische Aussage:** Eine Prüfregel oder Messoperation wird vorgeschlagen.
8. **Evaluative Aussage:** Ein Ergebnis wird an einem Zielmaßstab beurteilt.
9. **Redaktioneller Claim:** Eine einprägsame Verdichtung motiviert zum Weiterdenken; sie ist kein selbsttragender Fachbeweis.

Der Wechsel von „Ich habe keinen Platz“ zu „Es besteht strukturelle Unterversorgung“ benötigt zusätzliche Population, Stichprobe, Zeitraum, Region, Bedarfskriterium und Gegenprüfungen. Der Wechsel von „Ein Antrag wurde bewilligt“ zu „Die Hilfe wurde erbracht“ benötigt Nachweise über die tatsächliche Leistung. Der Wechsel von „Mehr Geld wurde bereitgestellt“ zu „Das Problem wurde gelöst“ benötigt eine Wirkungsprüfung.

## 5. Operationalisierung: vom Wort zur prüfbaren Frage

**Operationalisierung** heißt hier: Ausdrücklich festlegen, welche Beobachtungen unter welchen Bedingungen als Beleg für eine begrenzte Aussage zählen. Operationale Ergebnisse bleiben kontextgebunden; sie sind nicht identisch mit einem ganzen Begriff.

| These / Streitwort | Beobachtung / Nenner | Gegenprobe | Status |
| --- | --- | --- | --- |
| „Das Angebot ist erreichbar“ | reale Weg-/Wartezeit, Zugangsvoraussetzungen, Eignung, konkreter Zeitraum | formal gelistetes, aber faktisch unzugängliches Angebot | vorgeschlagener Test |
| „Der Vorgang ist erledigt“ | Abschluss des Verfahrens *und getrennt* Erfüllung des Bürgerziels | Entscheidung ohne tatsächliche Leistung | vorgeschlagener Test |
| „Die Region ist unterversorgt“ | definierter Bedarf, Kapazität, geeignete Angebote, Population, Zeitreihe | veränderte Definition / Ausweichangebote / Selektionsbias | vorgeschlagener Test |
| „Eine Maßnahme wirkt“ | vorher festgelegter Outcome, Vergleich, Zeitraum, Konfundierung | Trend ohne Maßnahme, Alternativerklärung | vorgeschlagener Test |
| „Ein KI-Skill hilft“ | gleicher Aufgabenbestand, validierte Referenz, Fehlerarten, Aufwand und Nutzbarkeit | Baseline ohne Skill; adversariale Fälle | vorgeschlagener Test |
| „Ein Lernpfad ist verständlich“ | reale Nutzer erklären Zweck, Grenzen und passenden nächsten Schritt | Verständnisfrage mit irreführender Formulierung | vorgeschlagener Test |
| „Zwei Begriffe sind äquivalent“ | identische Geltung unter ausdrücklich definierten Kontextbedingungen | fachlicher Gegenfall | vorgeschlagener Test |

**Pflicht bei jeder Operationalisierung:** `thesis_id`, `population`, `time`, `region`, `source_role`, `inclusion_exclusion`, `measure`, `denominator`, `threshold_or_decision_rule`, `uncertainty`, `alternative_explanations`, `retest`. Wo eine Größe nicht sinnvoll messbar ist, wird die Begrenzung dokumentiert, statt eine Scheinpräzision zu erzeugen.

## 6. Perspektivwechsel als Forschungsoperator

Wir unterscheiden **Umformulierung** (gleiche Bedeutung, andere Sprache), **Neuadressierung** (andere Sprecherrolle), **Skalenwechsel** (Mensch/Einrichtung/Region/System), **Zeitwechsel** (Ankündigung/Entscheidung/Umsetzung/Wirkung), **Normwechsel** (Wunsch/Versprechen/Pflicht), **Evidenzwechsel** (Bericht/Primärquelle/Studie/Test) und **Formalwechsel** (Text/Logik/Daten/Relation).

`P(statement, source_context, target_perspective) -> {reexpression, gained, lost, invariant, new_assumptions, evidence_needed, conflicts}`

Der Operator ist ein *Entwurf*. Er besteht die Prüfung nur, wenn behauptete Invarianten beim Hin- und Rückwechsel erhalten bleiben; veränderte Geltungsbedingungen müssen sichtbar werden. Ein Perspektivwechsel darf zusätzliche Erkenntnisse erzeugen, aber keine Tatsachen erfinden.

### Durchgehendes Beispiel: Therapieplatz

**Mensch:** „Ich brauche geeignete Behandlung und finde keinen Platz.“  
**Fachlich:** Welche Art der Behandlung ist indiziert, erreichbar und geeignet?  
**Rechtlich:** Welche Leistungsgrundlage und welche Voraussetzungen gelten konkret?  
**Institutionell:** Welche Stelle hat welchen Auftrag, welche Vermittlung wurde angeboten?  
**Statistisch:** Wie werden Bedarf, Wartezeit, Erreichbarkeit und Kapazität erfasst?  
**Politisch:** Welche Versorgungsziele wurden formuliert, welche Maßnahmen finanziert, welche Ergebnisse evaluiert?  
**KI:** Kann ein Skill die Begriffe und Wege erklären, Quellen unterscheiden und Widersprüche erkennen?  
**Didaktisch:** Welcher kurze Satz eröffnet die nächste freiwillige Vertiefung?

**Konstant bleiben soll** das Ausgangsanliegen; **nicht konstant bleiben müssen** die Messgrößen, Rechtsfragen und Zuständigkeiten. Genau diese Trennlinie ist der Erkenntnisgewinn. Die WHO-ICF zeigt als etablierte Referenz, dass Funktionsfähigkeit, Aktivität, Teilhabe und Kontextfaktoren unterschieden werden können [Q6]; sie ist kein Beweis für die speziellen Projektthesen.

## 7. Projektthesen – getrennt von Ergebnissen

| ID | These | Prüfmethode | Reife |
| --- | --- | --- | --- |
| LANG-T01 | Begriffsverschiebungen erklären einen Teil scheinbarer Meinungs- und Quellenwidersprüche. | stratifizierter Textvergleich mit und ohne Sinntrennung | offen |
| LANG-T02 | Die Trennung von Verfahrenserfolg und tatsächlicher Zielerfüllung macht relevante Lücken sichtbar. | paarige Vorgang-/Outcome-Kodierung | offen; konzeptuelle Unterscheidung |
| LANG-T03 | Ein Themenpfad wird verständlicher, wenn er mit der menschlichen Frage beginnt. | randomisierter Verständnistest gegen fachsprachlichen Einstieg | offen |
| LANG-T04 | Fachliche Genauigkeit und leichte Zugänglichkeit können durch gestufte Darstellung zusammen bestehen. | Prüffragen zu Verständnis und juristisch/fachlicher Genauigkeit | offen |
| LANG-T05 | Multiperspektivische Analyse findet zusätzliche, bisher verdeckte Forschungsfragen. | verblindeter Vergleich zu einperspektivischem Vorgehen | offen |
| LANG-T06 | Gemeinsame Skillbausteine sind über Fachräume wiederverwendbar, ohne Fachrecht und Risiken gleichzusetzen. | Transfer- und Negativtests mehrerer Fachgebiete | offen |
| LANG-T07 | Ein Claims-Register reduziert unbegründete sprachliche Drift. | Git-/Redaktions-Diff mit Blindreview | offen |
| LANG-T08 | Formalisierte Begriffsrelationen erleichtern die Suche, können aber irreführende Gleichheiten erzeugen. | Retrieval-Qualität, Mehrdeutigkeits-/False-Friend-Tests | offen |
| LANG-T09 | No-Loss-Verknüpfung von Quelle, Sinn, These, Test und öffentlichem Satz verringert unbelegte Schlussfolgerungen. | Audit neuer und historischer Änderungen | offen |
| LANG-T10 | Historische Definitionswechsel können stärker auf Kennzahlen wirken als die reale Veränderung. | Zeitreihen mit harmonisierten und originalen Definitionen | offen, fallabhängig |
| LANG-T11 | Perspektivwechsel sind nur dann methodisch tragfähig, wenn Verlust, Gewinn und neue Annahmen dokumentiert sind. | bidirektionale Rekonstruktion und Gegenbeispiele | methodische Sollregel |
| LANG-T12 | Eine gemeinsame 3×3×3-Adressierung zeigt für sich genommen noch keine mathematische Strukturähnlichkeit. | Operator-/Invarianz-/Isomorphieprüfung | methodische Abgrenzung |

**Evidenzstatus:** Keine dieser projektbezogenen Thesen wird hier als empirisch bestätigt ausgegeben. Bestehende Normen und Standardmodelle liefern Werkzeuge, nicht automatisch Beweise der projektspezifischen Wirksamkeit.

## 8. Claims: eigenständige Ebenen, keine Werbeliste

### 8.1 Die gesicherten Originale

Die 21 bereits verifizierten Original-Claims bleiben im [ursprünglichen Register](./data/bki-redaktionelle-anker-claims-v0-1.json). Besonders wichtig sind:

- **„Rechte verstehen. Tatsächliche Erfüllung prüfen.“** — Bürger-KI-Kernversprechen
- **„Ein Bescheid ist noch keine Leistung.“** — bewusstes Spannungsverhältnis
- **„Vom Anliegen zur Lösung.“** — menschlicher Weg
- **„Vernetzte Fähigkeiten. Mehr Handlungsmöglichkeiten.“** — Skillprinzip
- **„Wissen verbinden. Lösungen möglich machen.“** — eigenständige SOULution-Stimme

Diese Sätze werden nicht als neu erfunden ausgegeben und nicht durch die untenstehenden Vorschläge überschrieben.

### 8.2 Neue Claim-Familien (Entwürfe)

**Mensch / Ziel**
- „Nicht der Vorgang zählt. Sondern was ankommt.“
- „Vom eigenen Anliegen zur verständlichen Möglichkeit.“
- „Welche Antwort hilft – und welche Frage fehlt noch?“

**Begriffe / Sprachräume**
- „Dasselbe Wort. Nicht immer dieselbe Wirklichkeit.“
- „Wer den Begriff wechselt, verändert manchmal die Frage.“
- „Zwischen Alltagssatz und Fachbegriff liegt ein Lernweg.“
- „Begriffe verbinden. Bedeutungen unterscheiden.“

**Recht / Verwaltung**
- „Entschieden ist nicht erfüllt.“
- „Zuständig sein ist nicht dasselbe wie wirksam helfen.“
- „Vom Rechtswort zur tatsächlichen Wirkung.“

**Evidenz / Wissenschaft**
- „Erst die Definition. Dann die Zahl.“
- „Was wurde gezählt – und was bleibt unsichtbar?“
- „Eine Quelle ist ein Anfang, kein fertiger Schluss.“
- „Auch eine Erkenntnislücke ist ein Forschungsergebnis.“

**Politik / Gesellschaft**
- „Ein beschlossenes Ziel ist noch kein erreichtes Ziel.“
- „Geld misst Aufwand. Wirkung braucht eigene Maßstäbe.“
- „Rechenschaft beginnt bei der Frage, was tatsächlich geschah.“

**KI / Skills**
- „Nicht mehr Antworten. Besser prüfbare Fähigkeiten.“
- „Ein guter Skill kennt auch seine Grenzen.“
- „Wissen verknüpfen, ohne Unterschiede zu verwischen.“

**Didaktik / Perspektivwechsel**
- „Ein Thema. Mehrere Wege zum Verstehen.“
- „Die nächste Frage öffnet den nächsten Raum.“
- „Wer die Perspektive wechselt, entdeckt andere Lücken.“
- „Du entscheidest, wie tief du gehst.“

**SOULution / Tensor / Forschung**
- „Gemeinsame Struktur ist noch keine gleiche Bedeutung.“
- „Relationen prüfen statt Ähnlichkeiten behaupten.“
- „Erkenntnisse verbinden. Unterschiede beweisen.“
- „Kein Ergebnis geht verloren – auch kein Gegenbeispiel.“

Diese Claims sind bewusst *nicht* automatisch Homepageslogans. Jeder erhält im separaten Register Perspektive, Funktion, Fachrisiko, erlaubten Einsatzort und Redaktionsstatus.

### 8.3 Claimbildung aus einer These

**Beispiel LANG-T02**  
These: Der Verwaltungsabschluss bildet das Bürgerziel nicht notwendig ab.  
Fachsatz: „Formaler Verfahrensabschluss und tatsächlicher Outcome sind getrennte Variablen.“  
Öffentliche Headline: „Ein Bescheid ist noch keine Leistung.“ (historisch gesicherter Original-Claim.)  
Lernfrage: „Was ist tatsächlich angekommen?“  
Prüffrage: „Welche konkreten Ereignisse belegen die Zielerfüllung?“  
Gegenprobe: „Kann trotz noch ausstehendem formalen Abschluss bereits eine relevante tatsächliche Hilfe erbracht sein?“  
**Regel:** Ein Claim verdichtet die These, ersetzt aber weder Quellen noch Gegenprüfung.

## 9. Mehrsprachigkeit, regionale und institutionelle Geltung

Ein Begriffsknoten benötigt **natürliche Sprache**, **Rechtsordnung**, **historischen Stand** und **Fachkontext**. „Anspruch“, „Entitlement“, „eligibility“ und „right“ dürfen nicht ohne Kontext zu identischen Rechtsfolgen erklärt werden. Ebenso ist ein in Deutschland gebräuchlicher verwaltungsrechtlicher Begriff nicht automatisch mit schweizerischen, österreichischen oder EU-spezifischen Kategorien deckungsgleich.

**Pflichtfälle für Tests:** echte Synonyme; Teilüberlappung; Übersetzung ohne exakte Entsprechung; „false friends“; mehrdeutige Kurzbegriffe; zeitlich umdefinierte Kennzahlen; Laien-/Fachbedeutung; scheinbare Gegensätze; metaphorische Übertragung; veraltete institutionelle Benennungen.

Die Europäische Kommission fordert für verständliche öffentliche Texte u. a. präzise Formulierungen, Erklärung von Fachjargon und Aufmerksamkeit für falsche Freunde zwischen Sprachen [Q5]. Das ist ein Gestaltungsbezug, keine durchgeführte Evaluation der Bürger-KI.

## 10. Testprogramm: „Was ändert sich beim Wechsel?“

**Pilotkorpus (noch zu bilden):** Für die Themen Therapieplatz, Sozialleistungszahlung, Schulversorgung, behördlicher Bescheid und öffentliches Maßnahmenprogramm jeweils 5–10 öffentlich zugängliche und korrekt datierte Texte aus mehreren Sprachräumen. Persönliche Bürgerakten sind weder erforderlich noch Forschungsgegenstand.

**Kodierung:** Quellentyp, Sprecherposition, Begriffssinn, Aussageart, implizite Annahmen, Ziel/Outcome, Zeit, Raum, Rechtskontext, operationalisierte Einheit, behauptete Kausalität, alternative Erklärung und erkennbarer Claim.

**Vergleiche:** (A) Originalsprache vs. redaktionelle Vereinfachung; (B) Menschensicht vs. Institutionensicht; (C) Norm vs. Umsetzung; (D) Messgröße vs. beobachtbarer Outcome; (E) Erklärung durch Mensch vs. KI-Skill; (F) Vorwärts- vs. Rückübersetzung; (G) DE/EN- und Rechtsraumwechsel; (H) gleiche Operatoren bei verschiedenen Fachthemen.

**Kennzahlen nach vorab definierter Rubrik:** Bedeutungsverlust; falsche Äquivalenzen; unzulässige Schlussfolgerungen; unmarkierte Geltungswechsel; neue produktive Fragen; Quellenrückführbarkeit; korrekte Wahl eines Lernwegs; Aufwand; Verständlichkeit; Anzahl bestätigter/widerlegter Relationen. **Keine Werte vor Versuchsdurchführung.**

**Negative Befunde bleiben erhalten:** Wenn eine Formulierung die Verständlichkeit verbessert, aber die juristische Genauigkeit senkt, ist dies kein Erfolg. Wenn ein Blickwinkel keine neue Frage liefert, wird er nicht künstlich als zusätzliche Erkenntnis gezählt.

## 11. Informationsarchitektur und No-Loss-Vertrag

**Kanonische Kette:** `Quellfassung → Begriffssinn → Aussageart → These → Operationalisierung → Test/Gegenbefund → Ergebnis → Claim-/Lernweg-Projektion`.

**Querverbindungen:** `Ziel / Norm / Zuständigkeit / Skill / Trinität / Tensor` werden referenziert, nicht ungeprüft gleichgesetzt.

Bei neuen Erkenntnissen:
1. Quelle und Zeitraum verifizieren;
2. Begriffssinn oder Definition ergänzen, nicht still überschreiben;
3. betroffene Thesen, Messregeln, Skills, Tests, Erklärseiten und Claims ermitteln;
4. Gegenproben auslösen und Status festhalten;
5. alte Versionen und negative Befunde erhalten;
6. menschliche Einführungen nur bei sachlichem oder didaktischem Gewinn ändern;
7. öffentliche Claims vor Freigabe auf implizite Fachbehauptungen prüfen.

Die Umsetzung kann sich an SKOS (Begriffsnetze), PROV-O (Herkunft) [Q3] und FAIR (Auffindbarkeit, Zugänglichkeit, Interoperabilität, Nachnutzung) [Q4] orientieren. Diese Standards ersetzen nicht die inhaltliche Fachprüfung.

### Skizze eines Claim-Objekts

```json
{
  "claim_id": "BKI-LC-001",
  "text": "Dasselbe Wort. Nicht immer dieselbe Wirklichkeit.",
  "origin": "new_proposal",
  "role": "terminology_intro",
  "perspective": "language_space",
  "linked_theses": ["LANG-T01"],
  "concept_ids": [],
  "source_ids": ["Q1", "Q2"],
  "evidence_status": "editorial_proposal_not_empirical_result",
  "public_placement": "terminology_deep_dive",
  "risk_note": "may overgeneralize: not every word has multiple meanings",
  "review": "pending"
}
```

## 12. Didaktische Navigation: ein Thema, unterschiedliche Wege

Für jedes Kernthema bleiben fünf freiwillige Einstiege möglich: **Anliegen und Ziele**, **Wissen verstehen**, **Wege und Unterstützung**, **Gesellschaft untersuchen**, **Forschung und Werkzeuge**. Die Fachquelle hat einen Eigentümer; dieselbe Erkenntnis kann aus mehreren Blickwinkeln erklärt werden. Nicht jede Seite braucht eine Wiederholung der vollständigen Fachakte.

Jeder Pfad beginnt mit einer menschlich formulierbaren Frage, führt zu einer wichtigen Quelle, zeigt das zur Antwort notwendige Begriffs- oder Messmodell und ermöglicht mindestens einen **alternativen Blick**, eine **Gegenprüfung** und einen **Rückweg zur Übersicht**. Der Technikpfad zeigt bei Interesse die Skill-, Test- und Provenienzakte.

### Probe für die Navigation

„Ich finde keinen Therapieplatz“ → „Welche Art von Platz?“ → „Was gilt als Versorgung?“ → „Welche Unterstützungswege sind bekannt?“ → „Wie wird eine Versorgungslücke gemessen?“ → „Was kann eine KI hierzu nachweislich leisten?“ → zurück zum Ausgangsanliegen. **Weder alle Stationen noch die Reihenfolge sind Pflicht.**

## 13. Quellenregister und Quellenrollen

| ID | Quelle | Rolle und Grenze |
| --- | --- | --- |
| Q1 | [ISO 704:2022 – Terminology work: Principles and methods](https://www.iso.org/standard/79077.html) | Terminologische Methode; keine Aussage über Projektwirksamkeit |
| Q2 | [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/) (2009) | Konzeptnetze, Benennungen, Relationen |
| Q3 | [W3C PROV-O](https://www.w3.org/TR/prov-o/) (2013) | Modell zur Herkunft von Aussagen und Artefakten |
| Q4 | [Wilkinson et al., FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) (2016) | Forschungsdaten- und Artefaktorganisation |
| Q5 | [European Commission: Plain language](https://translation.ec.europa.eu/languages-and-translation-european-commission/plain-language-making-european-commission-texts-clear_en) | Klartext- und Übersetzungsregeln, nicht empirische Projektbewertung |
| Q6 | [WHO ICF](https://www.who.int/standards/classifications/icf) | Beispiel für systematische Trennung von Funktionsfähigkeit, Teilhabe und Kontext |
| P1 | [Originalsprach-Audit](./paper-buerger-ki-originalsprache-claims-didaktik-no-loss-v0-1.md) | historische Projektbeobachtung und Original-Claims |
| P2 | [Kernpaper Lernpfade](../forschung/buerger-ki/KERNPAPER_LERNPFADE_NOLOSS_WISSENSORCHESTRIERUNG_V0_1.md) | projektspezifische Informationsarchitektur |
| P3 | [Therapieplatz-Blickwinkel](./buerger-ki-blickwinkel-therapieplatz.html) | didaktischer Pilot, keine repräsentative Versorgungsstudie |
| P4 | [Bürger-KI-Gesamtstand](./buerger-ki-gesamtstand.md) | Arbeitsstand und methodische Fachverknüpfungen |

**Quellenqualität:** Q1–Q6 begründen Methoden und externe Begriffsmodelle; P1–P4 belegen nur den projektinternen Stand. Eine externe Primärquellen-Recherche zu jeder projektspezifischen Rechts-/Versorgungsaussage ist damit nicht erledigt.


## 15. Sprachstrategie für das Gesamtprojekt: Zurückhaltung, Akzente, Übersetzung

**Redaktionelle Leitentscheidung (Vorschlag, noch keine empirisch validierte Wirkung):** Die Sprache folgt dem Zweck der jeweiligen Ebene; *nicht* jeder wissenschaftliche Fund erhält einen Slogan und *nicht* jeder Slogan gehört auf die Hauptseite. Die anfänglich starke, menschliche Stimme von Bürger-KI bleibt die öffentliche Leitstimme. Tiefer liegende Forschungsobjekte besitzen andere Sprachregister, aber ihre Wege zurück zum Ausgangsanliegen bleiben sichtbar.

### 15.1 Fünf kommunikative Tiefen und ihre jeweilige Sprache

| Ebene / Ort | Tonalität und Dichte | Akzentregel | Prüfpflicht |
| --- | --- | --- | --- |
| 0 – Hero, Projektidentität | direkt, menschlich, kurze Sätze, maximal ein zentrales Spannungsverhältnis | **sehr stark, sehr selten**; verifizierte Original-Claims priorisieren | keine implizite Erfolgsgarantie |
| 1 – Hauptbereich, Einleitung | Frage → Beispiel → kurze Erklärung → optionaler Weg | **ein klarer Akzent pro inhaltlicher Einheit**, nicht pro Karte | Quelle/Handlungsgrenze im nächsten Schritt |
| 2 – Kernthema und Lernweg | neugierige Fragen, Wahlfreiheit, verständliche Varianten | **Akzent am Erkenntnissprung oder Perspektivwechsel**, nicht an jedem Übergang | tatsächlicher neuer Blickwinkel statt Paraphrase |
| 3 – fachlicher Deep Dive und Paper | genaue Begriffe, Definitionen, Daten, Gegenargumente | **sparsam**: eine präzise Leitthese, sonst Sachprosa | Geltung, Messbarkeit, Quellenrollen |
| 4 – Quellen-/Daten-/Test-/Skillakte | nüchterne eindeutige Terminologie und Maschinenlesbarkeit | **kein redaktioneller Claim im Beweisfeld** | exakte IDs, Versionen, Negativbefunde, Teststatus |

Die Menge ist eine **Gestaltungshypothese**, keine mechanische Quote: Starke Formulierungen nur dort, wo sie die Erkenntnis verbessern. Keine künstliche Rotation der 21 gesicherten Claims und 28 neuen Vorschläge auf jeder Seite. Kein „Werbedruck“ in Rechts- und Gesundheitsdetails.

### 15.2 Claims haben Rollen, keine bloß stilistischen Varianten

- **Identität**: langfristiger Projektanker (kanonische ursprüngliche Formulierung).
- **Widerspruch**: ein tatsächliches Spannungsverhältnis, das sachlich im Folgetext aufgelöst wird.
- **Erkenntnissprung**: markiert, warum eine neue Perspektive etwas anders erkennen lässt.
- **Leitfrage**: öffnet eine freiwillige Lernoption.
- **Merksatz**: verdichtet eine überprüfte fachliche Unterscheidung.
- **Forschungsthese**: ist falsifizierbar, mit Test/Kontext, kein öffentlicher Werbeslogan.
- **Methodenregel**: benennt, wie wir vorgehen; beweist noch keine Wirkung.

**Auswahl vor Neudichtung:** (1) existierenden historischen Claim prüfen, (2) seine Rolle/Kontextpassung beurteilen, (3) neue Formulierung nur bei zusätzlicher Erkenntnis entwickeln, (4) Risiken/Gegenbeispiele dokumentieren, (5) redaktionelle Freigabe. Ein wissenschaftlich falscher Original-Claim darf trotz historischer Erhaltung nicht unkommentiert weiter als Sachbehauptung erscheinen.

### 15.3 Sechs Übersetzungsleistungen, nicht nur DE/EN

| Typ | Ausgang → Ziel | Nutzen | Verlust- und Fehlerrisiko |
| --- | --- | --- | --- |
| TR-01 | Lebenswelt → Fachfrage | Menschen können ihr Ziel und entscheidende Fachfragen verstehen | subjektive Situation fälschlich zur fachlichen Diagnose machen |
| TR-02 | Fachsprache → verständlicher Text | Quelle wird ohne unnötigen Jargon erschließbar | Ausnahmen, Unsicherheit, Geltungsbereich verschwinden |
| TR-03 | Institutionenbeschreibung → tatsächliche Wirkung | Vorgang, Leistung und Zielerfüllung auseinanderhalten | eigene Bewertungsmaßstäbe unterschieben |
| TR-04 | Quelle/Messgröße → These/Operation | Belegkette und Gegenproben offenlegen | Korrelation/Kausalität, Norm/Beobachtung verwechseln |
| TR-05 | Relations-/Skillmodell → Lernweg/Handlungsoption | Forschung didaktisch vermitteln | Architekturmetapher als bewiesene Praxiswirkung darstellen |
| TR-06 | natürliche Sprache / DE-AT-CH-EU-Rechtsraum → anderer Sprach-/Rechtsraum | Inhalte sprachlich auffindbar und rechtlich kontextualisierbar machen | Scheinsynonyme, falsche Rechte/Institutionen übertragen |

**Übersetzungsregel:** Ein gelungenes sprachliches Äquivalent ist nicht notwendig ein semantisches, rechtliches, institutionelles oder mathematisches Äquivalent. Für jede Gattung ist ihr eigenes Äquivalenzkriterium nötig. Rückübersetzungen können Fehler aufzeigen, reichen aber nicht als alleiniger Qualitätsnachweis; vor allem im Recht sind unabhängige fachliche Vergleiche entscheidend.

### 15.4 Übersetzungsakte und technische Zustände

`translation_id, source_object_id, source_text_ref, source_language, target_language, source_space, target_space, source_sense_ids, target_sense_ids, claim_type, context/jurisdiction/time, equivalence_type, invariant, added_assumptions, omitted_information, counterexamples, source_ids, reviewer, review_status, affected_learning_routes, change_event_id`.

**Kategorien der Beziehung:** `exact_in_defined_context`, `partial_overlap`, `broader`, `narrower`, `analogy_only`, `contradiction`, `not_equivalent`, `unassessed`. Keine Standardsyntax behauptet: Dies ist das vorgeschlagene projektspezifische Modell. Konzeptsinn und Benennungen lassen sich an W3C SKOS anlehnen; Herkunft und Bearbeitung an W3C PROV-O.

### 15.5 Beispiel: Ein Satz, mehrere Räume

**Originalanliegen:** „Ich finde keinen Therapieplatz.“

- Alltag → „Welche erreichbare und geeignete Unterstützung suche ich?“
- Medizin → „Welche fachliche Indikation, Behandlungsform und Dringlichkeit sind überhaupt festzustellen?“
- Recht → „Welche konkrete Leistungsgrundlage und welche Voraussetzungen gelten?“
- Verwaltung/Versorgung → „Was wurde vermittelt; kam eine geeignete Leistung tatsächlich zustande?“
- Wissenschaft → „Was wurde wann und bei welcher Population als Bedarf, Kapazität, Zugang und Beginn gemessen?“
- Politik → „Welche Zielwerte und Maßnahmen existieren und welche Wirkungen sind belegt?“
- KI-Skill → „Kann die Übersetzung Quellen und Handlungsalternativen unterscheiden, ohne die Person zu diagnostizieren oder Ansprüche zu behaupten?“
- Didaktik → „Was bedeutet hier eigentlich: einen Platz haben?“

**Sprachlicher Akzent am Wechsel:** „Ein vermittelter Termin ist noch keine gesicherte Behandlung.“ **Status:** Beispiel-Claim, nicht medizinische oder rechtliche Vollständigkeitsbehauptung. Es gibt Fälle, in denen ein Termin sehr wohl eine passende und ausreichende Intervention darstellt; deshalb Einzelfallkontext beachten.

### 15.6 Unterschiedliche Projektstimmen

**Bürger-KI** spricht vom Anliegen und den erreichbaren Möglichkeiten; sie verspricht keine automatische Leistungsdurchsetzung. **SOULution** verbindet Wissen und Lösungsräume; sein vorhandener Claim „Wissen verbinden. Lösungen möglich machen.“ bleibt eigenständig. **KI-Tensor** verwendet genaue Relations- und mathematische Begriffe; anschauliche Metaphern dürfen keinen Strukturbeweis ersetzen. **Mini-KI / Skillforschung** sagt erst dann „kann“, wenn Tests es für den konkreten Geltungsbereich belegen; sonst „soll“, „wird untersucht“ oder „ist spezifiziert“. **Gesellschafts-/Politikforschung** unterscheidet Aussage, Quelle, politische Bewertung, Indikator und mögliche Kausalität.

**Keine einheitliche Stimme für alle Artefakte:** Es gibt ein gemeinsames Wörter- und Quellenregister, aber bewusst unterschiedliche Darstellungsformen.

### 15.7 Gestaltungsregeln und redaktionelle Abnahme

1. Auf Hero und Haupteinstieg keine Massen von Forschungs-IDs, Phasenständen oder Quellenbannern; Kontext und Vertiefung unmittelbar erreichbar.
2. Claim sichtbar **nur** mit eigenem Erkenntnisbeitrag. Ein Akzent ist oft genug; weitere Karten sollten klare Fragen statt immer neue Punchlines erhalten.
3. Besonders starke Akzente für **echte Widersprüche**, **Perspektivwechsel**, **erreichte Nachweise**, **Grenzfälle** und **negative Befunde** reservieren.
4. Fachtexte erklären einen Schlüsselbegriff zunächst am konkreten Beispiel und präzisieren erst dann Definition und Ausnahmen.
5. Quellen, Tests, Gesetze und Daten bleiben zitiergenau und ohne stilistische Überschreibung.
6. Jede neue Übersetzung bewahrt mindestens den Ausgangskontext, die Zielaussage, die Unsicherheit und die Rückführung zur Quelle; sonst als `lossy` markieren.
7. Keine KI-generierte Übersetzung als fachlich geprüft deklarieren, bevor ein geeigneter Review vorliegt.
8. Für öffentliche Lerntexte Verständlichkeit mit *echten Aufgaben* prüfen: Kann man Bedeutung, Grenze und nächsten Weg unterscheiden? Nicht bloß Lesbarkeitszahlen optimieren.

**Quellenbezug:** [Europäische Kommission, Plain Language](https://translation.ec.europa.eu/languages-and-translation-european-commission/plain-language-making-european-commission-texts-clear_en); [Europäische Kommission, English Style Guide](https://commission.europa.eu/system/files/2023-11/styleguide_english_dgt_en.pdf); [W3C SKOS](https://www.w3.org/TR/skos-reference/); [W3C PROV-O](https://www.w3.org/TR/prov-o/). Dies sind externe Methodenbezüge; die projektspezifische Platzierungsstrategie ist ein eigener Entwurf.

## 16. Bestandsaudit, No-Loss-Risiken und Phase 15

**Audit vom 05.11.2026:** Repository-Stichprobe der aktuellen Bürger-KI-Hauptseite, Lernwege, Therapieplatz-Pilot, zwei Claim-Register, des Kern-Glossars, Thesenüberblicks, Lernwege-Datenmodells, der Forschungsbibliothek sowie Standards-/Quellenregister. Vollständige inhaltliche Prüfung aller Repository-Dateien und des historischen ZIP-Glossars erfolgte nicht. Details und Prioritäten: [Phase-15-Audit und Umsetzungsplan](./buerger-ki-phase-15-sprache-uebersetzung-no-loss.md).

### 16.1 Tatsächlich vorhandener Bestand

- Gesicherte redaktionelle Anker: **21**, getrennt von **28** neuen, nicht freigegebenen Vorschlägen.
- Historische Hauptseite: Vergleich mit **64** ursprünglichen H1–H3-Überschriften, im vorherigen Originalsprach-Audit als erhalten dokumentiert.
- Lernpfad-Modell: **5** Haupteinstiege, **5** Lernwege, **6** Themenfilter, **12** modellierte Objektarten.
- Therapieplatz-Pilot: **5** Perspektiven und **5** Spiegelungen.
- Forschungsbibliothek: **21** kuratierte Einträge, **kein** vollständiger Repository-Katalog.
- Öffentliche Glossar-Vorschau: **12** Kurzdefinitionen; historischer Bestand mit **1.072** Termini wird nur referenziert, nicht vollständig im Webregister geführt.
- Öffentliche Thesenübersicht: **6** thematische Linien, keine vollständige historische Thesenliste.
- Bestehendes fachliches Claim-Schema: verlangt u. a. `CLM-...`-IDs und strukturierten Quellen-/Evidenz-/Freigabestatus; redaktionelle `BKI-LC-...`-Datensätze sind **nicht** automatisch Instanzen dieses Schemas.

### 16.2 Zentrale No-Loss-Befunde

**Stärke:** Die ursprünglichen Claims sind historisch getrennt gesichert; menschlicher Einstieg, kuratierte Fachbibliothek und fünf Perspektiven sind angelegt. Ein neues Paper kann ohne Verdrängung der Startseite erscheinen.

**Risiko A:** Zwei Claim-Regime: Redaktionsanker und Vorschläge einerseits, striktes Evidenz-Claimschema andererseits. **Lösung:** explizite Crosswalk-/Mapping-Akte, ohne redaktionelle Slogans als wissenschaftliche Claims auszugeben.

**Risiko B:** Im Glossar stehen 12 Webkurzdefinitionen; 1.072 historische Definitionen sind nicht in dieser Datei. **Lösung:** erst historisches Originalinventar und Deduplikation, dann Verlinkung von Sinn-IDs und Sprachvarianten. Keinesfalls Web-Kurzfassung als vollständiges Glossar bezeichnen.

**Risiko C:** 6 publizierte thematische Thesen sind nicht alle bisherigen Projektthesen; die zwölf `LANG-T`-Thesen sind Paper-interne Hypothesen. **Lösung:** Querverweise bei Erhalt der IDs, nicht stillschweigender Merge.

**Risiko D:** Forschungsbibliothek = kuratierte Auswahl, nicht Gesamtarchiv. **Lösung:** getrennte Inventarisierung und Relevanznavigation; keine willkürlichen Vollständigkeitsquoten.

**Risiko E:** Quellenliste mischt Standards, Forschungsquellen und interne Papers; ein gültiger Standard ist kein Beweis einer Projektaussage. **Lösung:** Quellenrollen und konkrete Belegstellen je Aussage erfassen.

**Risiko F:** Perspektivwechsel und Übersetzungsoperator sind derzeit **Spezifikation**, keine implementierte und empirisch getestete Sprach-KI. **Lösung:** kleinen, überprüfbaren Goldstandard-Korpus und Negativtests bilden.

### 16.3 Nächste Phase: Prioritäten

**Phase 15A – sichern:** unveränderten historischen Claim-Bestand, Originalseiten-Headlines und bestehende Lernwege als Baseline fixieren; alle neuen sprachlichen Eingriffe versionieren.

**Phase 15B – Crosswalk:** redaktionelle Claims, wissenschaftliche Claims, Terminologie, Thesen, Quellrollen und Perspektiven durch Mapping verbinden, ohne ihre Identitäten zu verschmelzen.

**Phase 15C – fünf konkrete Übersetzungsproben:** Therapieplatz als Vertikaltest, zusätzlich Sozialleistungszahlung, Schule/Pflege, eine politische Wirkungsaussage und ein KI-Tensor-Relationsbeispiel. Jeweils menschliche, fachliche, institutionelle, wissenschaftliche und technische Darstellung samt Gegenprobe.

**Phase 15D – redaktioneller Prototyp:** nur zwei oder drei tatsächliche Perspektivwechsel auf bestehenden Seiten mit explizitem alternativen Pfad erproben; die Hero-Sätze und bestehenden Hauptüberschriften unangetastet lassen.

**Phase 15E – prüfen:** Verständlichkeit, Äquivalenzfehler, Rückführbarkeit, erfasste Ausnahmen, Perspektivmehrwert, Quellenintegrität und No-Loss-Regressionsprüfung. Erst dann Claims für mehr Sichtbarkeit freigeben.

**Definition fertig:** Kein historischer Text und keine Quellen-/Begriffs-/Thesen-ID verloren; neue Vorschläge bleiben erkennbar; mindestens ein Perspektivwechsel besitzt Original, fachliche Übersetzung, Quellen-/Geltungsnotizen, Gegenbeispiel und nachvollziehbaren Rückweg; Änderungen am öffentlichen Text sind tatsächlich geprüft.

## 14. Abnahme und nächste Forschungsstufe

**In v0.1 tatsächlich geleistet:** historischer Anschluss an das Originalsprach-Paper; getrennte Typologie der Sprachräume, Aussagearten und Begriffe; explizite Hypothesen und falsifizierbare Tests; Vorschläge für neue Claims nach Funktion; Zuordnung zu Quellen und No-Loss-Register.

**Offen und ausdrücklich nicht als erledigt markieren:** vollständiger historischer Textkorpus aller Seiten/Publikationen; fachliches Review der Terminologie; mehrsprachiger Referenzkorpus; empirische Perspektivwechsel- und Verständnistests; automatische Regressionsprüfung; Integrationsprüfung jeder einzelnen These gegen das gesamte Projektinventar; Browser- und Nutzerabnahme.

**Publikationsregel:** Dieses Paper kann als Forschungsentwurf zugänglich sein; Claims mit `origin=new_proposal` sind nicht redaktionell freigegeben und erhalten keine automatische Platzierung im Hero. Der Bestand wird erweitert, nicht umgeschrieben.

---
*Bürger-KI · Wissen wird verständlich, wenn der Weg zwischen den Bedeutungen sichtbar wird. Forschungsfassung v0.1.*
