# Bürger-KI → Skillbibliothek → Tensor-Kandidaten · v0.1

**Status:** Inventar/Spezifikation; **keiner der 32 Skills ist hiermit implementiert oder wissenschaftlich validiert.** 
**Abgrenzung:** Nur `forschung/buerger-ki/` und Bürger-KI-Seiten; keine Veränderung fremder Tensorinventare, Codebücher oder globaler Skillregister.

## Architektur

`Problem → fachlicher Vorgang → Skillkomposition → atomarer Operator → Relation → Test/Gegenprobe → Evidenz → Tensor-Kandidat`

Die **17 allgemeinen Operatoren (BK-OP)** sind potenziell übertragbar. Die **15 fachlichen Skills (BK-F)** bleiben zunächst im Bürger-KI-Fachkontext. Die Übertragung erfolgt durch einen ausdrücklich geprüften Crosswalk, nie durch Gleichsetzung von 27 Skills mit 27 Tensorfeldern.

## Atomare Operationen

| ID | Operation | mathematischer / logischer Träger |
|---|---|---|
| BK-OP-01 | Quelleneinheit erfassen | Provenienz |
| BK-OP-02 | Behauptung extrahieren | Extraktion |
| BK-OP-03 | Begriffe typisieren | Typisierung |
| BK-OP-04 | Regelvoraussetzungen auswerten | Prädikatenlogik |
| BK-OP-05 | Zeitgeltung prüfen | temporale Relation |
| BK-OP-06 | Soll-Ist vergleichen | Differenzoperator |
| BK-OP-07 | Rückrechnung durchführen | Inverse/partielle Inverse |
| BK-OP-08 | Widerspruch erkennen | Konsistenzprüfung |
| BK-OP-09 | Gegenprobe ausführen | Falsifikation |
| BK-OP-10 | Ursache von Korrelation trennen | kausales Modell |
| BK-OP-11 | Datenbedarf minimieren | Informationsreduktion |
| BK-OP-12 | Ergebnis gegen Zielzustand prüfen | Zielprädikat |
| BK-OP-13 | Fälle vergleichbar machen | Normalisierung |
| BK-OP-14 | Ergebnisse aggregieren | Aggregation |
| BK-OP-15 | Alternativen vergleichen | Mehrkriterienvergleich |
| BK-OP-16 | Skillfähigkeit evaluieren | Evaluation |
| BK-OP-17 | Abhängigkeiten nachziehen | Graph-Propagation |

## Fachliche Skill-Kompositionen

| ID | Aufgabe | atomare Abhängigkeiten |
|---|---|---|
| BK-F-01 | Materiellen Anspruch rekonstruieren | BK-OP-04,BK-OP-05,BK-OP-01 |
| BK-F-02 | Sozialleistungszahlung prüfen | BK-OP-06,BK-OP-12 |
| BK-F-03 | Versorgungsbedarf definieren | BK-OP-03,BK-OP-04 |
| BK-F-04 | Therapieangebot abgleichen | BK-OP-03,BK-OP-15 |
| BK-F-05 | Suchchronologie führen | BK-OP-01,BK-OP-05 |
| BK-F-06 | Patientenakte inventarisieren | BK-OP-01,BK-OP-11 |
| BK-F-07 | Patientenrechtsfrage prüfen | BK-OP-04,BK-OP-08 |
| BK-F-08 | Institutionelle Pflicht prüfen | BK-OP-04,BK-OP-05,BK-OP-12 |
| BK-F-09 | Unterversorgung untersuchen | BK-OP-13,BK-OP-14,BK-OP-10 |
| BK-F-10 | Bürgergruppe koordinieren | BK-OP-11,BK-OP-17 |
| BK-F-11 | Nächsten Schritt bestimmen | BK-OP-04,BK-OP-15 |
| BK-F-12 | Rechtserfüllung verfolgen | BK-OP-06,BK-OP-12 |
| BK-F-13 | Rechtsänderung auf Wirkung prüfen | BK-OP-05,BK-OP-15,BK-OP-17 |
| BK-F-14 | Antragsqualität prüfen | BK-OP-02,BK-OP-08,BK-OP-09 |
| BK-F-15 | Gruppen-Benchmark durchführen | BK-OP-13,BK-OP-14,BK-OP-16 |

## Zwei Vertikaltests

### BK-PROBLEM-THER-001 – psychotherapeutische Versorgung
1. Bedarf **fachlich** feststellen; KI ersetzt keine Diagnose.
2. Vorhandene Versorgung auf Eignung, Erreichbarkeit und Zeit prüfen.
3. Kontakte, Ergebnisse und offene Schritte mit Quellenbezug erfassen.
4. Geeignete Rechtswege und institutionelle Pflichten unterscheiden.
5. Individuelles Ziel ist **tatsächliche Erreichbarkeit erforderlicher Behandlung**, nicht bloß ein Suchergebnis.
6. Davon unabhängig Patientenakten- und Rechtsfragen weiterhin begleiten.
7. Gruppenbefunde nur mit definiertem Nenner und Auswahlkorrektur; keine Gleichsetzung von Gruppenbefund und Rechtsverletzung.

### BK-PROBLEM-SOZ-001 – zustehende Sozialleistung
1. **Materiellen Anspruch** unabhängig von einem Bescheid prüfen.
2. Antrag / Bewilligung / vorläufige Entscheidung / Vorschuss / Fälligkeit sauber trennen.
3. Anspruch und tatsächlichen Zahlungseingang abgleichen.
4. Richtige Klärung, Beratung oder Eilrechtsschutz nur sachverhaltsabhängig prüfen.
5. Abschluss erst bei **tatsächlicher Leistungserfüllung** oder nachvollziehbar geklärter Nichtberechtigung; Folgeschäden getrennt prüfen.

## Tensor-Transfer und Suchmatrix

| Relationsfamilie | Operatoren | mögliche formale Prüfung | Risiko |
|---|---|---|---|
| Bedingung → Erfüllung | OP-04, OP-12 | dreiwertige Logik, Wahrheitstabellen | offen nicht als falsch klassifizieren |
| Soll/Ist und Inversion | OP-06, OP-07 | Differenz, Rückrechnung, Dimensionsprüfung | Nichtinvertierbarkeit |
| Provenienz und Versionierung | OP-01, OP-05, OP-17 | gerichteter typisierter Graph, No-Loss-Test | Quellenverwechslung |
| Netzwerk und Abdeckung | OP-13, OP-14 | Mengen, Graphen, statistische Abdeckung | Selektionsbias |
| Vergleich und Evaluation | OP-15, OP-16 | Alternativenvergleich, Baselines, Fehlermaße | Scheinkausalität |

**Feldsortierung für spätere Überlagerung bestehender Tensoren:** Gegenstandstyp, Operatorfamilie, Ein-/Ausgabe-Typ, Zeitabhängigkeit, Invertierbarkeit, Invariante, Quellenstatus, Beweismethode und Fehlerfamilie. Eine `3×3×3`-Adresse ist zunächst Metadatum, kein Beleg für gemeinsame Mathematik.

## Testvertrag für jeden Skill

`skill-id + version + input-schema + preconditions + operator + output-schema + provenance + positive-test + negative-test + boundary-test + inverse/countertest + baseline + evidence-status`

Erst bei reproduzierbar bestandenen Tests darf von einer bestätigten Fähigkeit gesprochen werden. Ein erfolgreicher Skill beweist weder automatische Rechtsverletzung noch generelle Unterversorgung.

## Rückfluss und Synchronisation

Eine spätere Freigabe muss über stabile IDs die Kette `Quelle → Aussage → Relation → Operator → Skill → Test → Ergebnis → Tensor-Kandidat` rekonstruieren können. Bei Änderungen sind **Glossar, Quellenregister, Prompt-Exporte, Benchmarks und abhängige Prüfakten** gemeinsam nachzuziehen. Diese Datei ist ein Übergabekandidat, noch **kein** Update globaler Register.
