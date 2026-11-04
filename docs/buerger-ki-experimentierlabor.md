# Bürger-KI · Erstes Forschungsresultat: Test- und Projektkatalog, Experimentierlabor

**ID:** BKI-EXP-001  
**Version:** 0.1 · 2026-11-04  
**Status:** Forschungsentwurf / Testdesign; **keine empirischen Pilotresultate und keine validierten Leistungsgewinne**  
**Zugehörigkeit:** Bürger-KI Phasen 4–6; SOULution; Mini-KI; Deep Dive & Harvest; No-Loss; Tensorvergleich  
**Ziel:** Unterschiedliche KI-Strategien an identischen, synthetischen und quellenprüfbaren Aufgaben objektiv vergleichen, verlässliche Skills identifizieren und Verbesserungen reproduzierbar nachweisen.

## 1. Grundsatz, Forschungsfrage, Hypothesen

Dieses Projekt entwickelt **Fähigkeiten für Bürger**. Es verarbeitet selbst keine persönlichen Bürgerfälle und legt keine Bürgerakten an. Das Labor nutzt konstruierte Referenzaufgaben sowie öffentlich zugängliche Fachquellen und Testartefakte.

**Forschungsfrage:** Welche Kombination aus direkter KI-Antwort, modularen Skills, paralleler Recherche, unabhängiger Gegenprüfung und regelbasierter Kontrolle erzeugt bei gleichem Auftrag die korrekteren, vollständigeren, besser begründeten und praktischeren Ergebnisse?

- **H1:** Modulare Skill-Ketten verbessern die Abdeckung gegenüber dem Direktprompt.
- **H2:** Unabhängige Gegenprüfung reduziert unbelegte Aussagen gegenüber einer bloßen Selbstprüfung.
- **H3:** Ein Harvest-/Deep-Dive-Schritt findet mehr **valide** Handlungsoptionen als die isolierte Grundantwort.
- **H4:** Wiederverwendbare, fachübergreifende Skill-Komponenten reduzieren Aufwand, ohne Qualität zu verlieren.
- **H5:** Eine kontrolliert verdichtete Skill-Version übertrifft die ursprüngliche Kette auf ungesehenen Referenzaufgaben.
- **H6:** Tensor-/Relationsklassifikation erkennt relevante wiederkehrende Strukturen; **offen**, ob sie die Aufgabenlösung verbessert.

Die Hypothesen sind **zu prüfen**, nicht vorweggenommene Befunde.

## 2. Projektvorschläge – erste Forschungsstaffel

| Projekt-ID | Vorhaben | Kernexperiment | Ergebnisartefakt | Priorität |
| --- | --- | --- | --- | --- |
| BKI-P01 | **Strategie-Arena** | Direktantwort vs. feste Skill-Kette vs. parallele Skill-Komposition vs. Skill-Netzwerk mit Gegenprüfung | Vergleichsmatrix und Fehlertaxonomie | 1 |
| BKI-P02 | **Harvest-Labor** | Freie Recherche vs. Quellenkatalog vs. Quellen-/Werkzeug-Harvest mit Provenienz | geprüfte Quellen- und Werkzeugtreffer, Negativbefunde | 1 |
| BKI-P03 | **Anspruchs-/Verfahrens-Navigator** | Fachprüfpfad mit Vorbedingungen, Zuständigkeit, Alternativen, Fristen | überprüfbarer Verfahrensgraph | 1 |
| BKI-P04 | **Unabhängiger Prüfer** | Selbstkritik vs. getrennte Prüfinstanz vs. deterministische Teilprüfungen | Widerspruchs- und Nachweisbericht | 1 |
| BKI-P05 | **Skill-Schmiede** | Mehrere Skills komponieren; Kandidaten verdichten; auf Holdout-Aufgaben regressionsprüfen | versionierter Kandidat mit Testakte | 2 |
| BKI-P06 | **Mini-KI-Orchestrator** | Auswahl/Abfolge der Skills als regelbasiertes System gegenüber LLM-Planung | Ausführungsprotokoll, Fehlerraten, Aufwand | 2 |
| BKI-P07 | **Relations-/Tensorvergleich** | Voraussetzung–Operator–Folge-Strukturen von Aufgaben und Skills vergleichen | Relationsmatrix, Invarianten, Gegenbeispiele | 2 |
| BKI-P08 | **Mitmach-Reproduktionslabor** | Testanleitung auf externer KI wiederholen, ohne Git-Zugriff | reproduzierbare öffentliche Rückmeldung | 3 |

**Erste Staffel:** P01–P04. P05–P08 nutzen die Ergebnisse und bleiben bis zu einer belastbaren Baseline Explorationsprojekte.

## 3. Referenzaufgaben: zehn Testfamilien, drei Fälle je Familie = 30 Aufgaben

Jede Familie erhält einen **positiven**, **Grenz-/Mehrdeutigkeits-** und **Negativ-/Fehlinformationsfall**. Alle Aufgaben werden als synthetische, nicht personenbezogene Beispiele verfasst. Maßgebliche Fachquellen, Stichtage und erwartete Aussagen müssen vor Testbeginn in einer Referenzakte festgehalten werden.

| Familie | Positivfall | Grenzfall | Negativ-/Fehlerfall | Hauptprüfziel |
| --- | --- | --- | --- | --- |
| T01 Zuständigkeit | Behörde für klaren Antrag finden | zwei plausible Stellen | erfundene Zuständigkeit | Zuständigkeitsgrundlagen |
| T02 Fristen | Frist aus festem Muster berechnen | Feiertag/Fristbeginn ungeklärt | falsche Pauschalfrist | Rechenweg und Vorbehalte |
| T03 Ansprüche | Anspruchsvoraussetzungen strukturieren | unvollständige Tatbestandsmerkmale | nicht existente Anspruchsnorm | belegte Voraussetzungen |
| T04 Offene Quellen | Norm oder amtliche Hilfe lokalisieren | konkurrierende Fassungen | veraltete Fassung | Quellenstand und Priorität |
| T05 Verbraucherproblem | Reklamationswege nennen | verschiedene Vertragstypen | frei erfundene Pflicht | Alternativen und Geltung |
| T06 Bildung | öffentliches Verfahren darstellen | Zuständigkeitswechsel | falsche Verallgemeinerung | regionale Abhängigkeit |
| T07 Wohnen | Verfahrensoptionen vergleichen | unklare Tatsachenbasis | überzogene Erfolgsaussage | Unsicherheitskennzeichnung |
| T08 Verwaltung | sachliche Nachfrage formulieren | fehlende Belege | manipulative Unterstellung | Trennung Frage/Behauptung |
| T09 Evidenz | Studien-/Behauptungslage prüfen | widersprüchliche Quellen | halluziniertes Zitat | Belegtreue |
| T10 Skill-Transfer | dieselbe Prüfmethode in zwei Gebieten | andere Geltungsbedingungen | unzulässiger Transfer | Wiederverwendung ohne Fehlschluss |

Die 30 Fall-IDs lauten **BKI-T01-A/B/C bis BKI-T10-A/B/C**. **Aufgabetexte, Goldstandards und Quellenlinks sind noch zu erstellen**; die Tabelle ist ein Katalog, kein abgeschlossener Benchmark.

## 4. Teststrategien (identische Aufgabe, identischer Ressourcenrahmen)

- **S0 Direktprompt:** eine Antwort ohne explizite Skill-Kette.
- **S1 Sequenz:** Anliegenanalyse → Harvest → Fachprüfung → Optionen → Handlung.
- **S2 Parallel:** unabhängige Recherche- und Fachprüfzweige; Ergebnisse zusammenführen.
- **S3 Prüfer:** S1 + separater Gegenprüfer, der Quellen und Schlussfolgerungen überprüft.
- **S4 Regelhybrid:** S1 + deterministische Prüffunktionen für strukturierte Teile (z. B. Format, definierte Fristenlogik, Quell-ID-Vollständigkeit).
- **S5 Kandidat:** neu komponierter/verdichteter Skill; nur auf Holdout-Teil mit S1/S3 vergleichen.

**Fairnessregel:** Gleicher Aufgabenwortlaut, gleiche Quellengrundlage, gleicher Stichtag, derselbe erlaubte Werkzeugzugang pro Vergleichsgruppe, dokumentiertes Modell, Modellversion, Promptversion, Token-/Zeitbudget. Unterschiede in Zugriff und Budget separat ausweisen; niemals ungleiche Durchläufe als direkten Strategievergleich ausgeben. Reihenfolge der Strategien randomisieren; mehrere Wiederholungen und unabhängige Blindprüfung einplanen.

## 5. Messsystem und Fehlerklassen

**Primäre Endpunkte (je 0–4, anhand eines vorab festgelegten Bewertungsrasters):**
1. **Faktische Korrektheit** – nachprüfbare und zutreffende Aussagen.
2. **Quellen- und Belegtreue** – Beleg stützt genau die zugeordnete Aussage.
3. **Abdeckung** – relevante Optionen, Voraussetzungen, Zuständigkeiten.
4. **Handlungsnutzwert** – umsetzbare, bedingte Schritte statt Scheinsicherheit.
5. **Unsicherheitskompetenz** – kennt fehlende Information, Geltungsgrenzen und Widersprüche.
6. **Reproduzierbarkeit** – gleiche Eingaben/Quellen führen zu vergleichbar geprüften Ausgaben.

**Sekundär:** Bearbeitungszeit, Token-/Werkzeugverbrauch, Anzahl Quellen, Duplikate, Treffer mit belastbarer Provenienz, Zahl zurückgewiesener Behauptungen, korrekt erkannte Negativbefunde.

**Fehlercodes:** F01 Quelle nicht existent; F02 Quelle belegt Aussage nicht; F03 veraltete/ungeeignete Rechtslage; F04 fehlende wesentliche Alternative; F05 unzulässige Generalisierung; F06 Frist-/Rechenfehler; F07 ungerechtfertigte Gewissheit; F08 Zirkelschluss der Selbstprüfung; F09 Ressourcenüberschreitung; F10 Skill-Schnittstellen-/Übertragungsfehler.

**Gesamtwertung:** Primär werden die sechs Endpunkte **einzeln** ausgewiesen; ein zusammengefasster Durchschnitt ist nur eine Zusatzkennzahl. Schwere Fakt-/Quellenfehler können eine Freigabe unabhängig vom Durchschnitt sperren. Statistische Unterschiede erst nach tatsächlichen Wiederholungen berichten.

## 6. Experimentierprozess: zwölf Schritte

1. **Aufgabe einfrieren:** ID, Wortlaut, Fachgebiet, Stichtag, erwarteter Lösungskorridor.
2. **Quellenpaket fixieren:** amtliche Primärquellen, Version, Abrufdatum, Hash/URL.
3. **Goldstandard erstellen:** überprüfbare Muss-Aussagen, zulässige Alternativen, verbotene Fehlschlüsse.
4. **Strategien einfrieren:** Skill-IDs, Promptversionen, Modelle, Zugänge, Budgets.
5. **Test aufsetzen:** gleiche Aufgaben mit S0–S4; S5 nur in Verbesserungsstudie.
6. **Ausführen:** Outputs, Laufzeit und Werkzeugaufrufe mit unveränderlichen Artefakt-IDs protokollieren.
7. **Blind prüfen:** getrennte Prüfer ohne sichtbaren Strategienamen; Meinungsverschiedenheiten auflösen.
8. **Gegenproben:** Negativfälle, widersprechende Quelle, fehlendes Tatbestandsmerkmal, Quellenentzug.
9. **Auswerten:** je Aufgabe/Strategie Fehler, Belege, Kosten und Qualitätsdimensionen vergleichen.
10. **Verbesserungshypothese:** Änderung nur mit konkretem, falsifizierbarem Erfolgsmaß vorschlagen.
11. **Holdout/Regression:** Kandidat auf bislang ungesehenen Aufgaben testen; keine Trainings-Leakage.
12. **No-Loss-Nachzug:** Ergebnisse, Gegenbeispiele, Quellen, Glossar, Skillversionen, Relationen und Tensorbezüge synchronisieren.

## 7. Minimaler Maschinenvertrag

Eine Ausführung soll als JSON/JSONL gespeichert werden, mit mindestens:

```json
{
  "run_id": "BKI-RUN-0001",
  "task_id": "BKI-T01-A",
  "strategy_id": "S0",
  "model_id": "UNSET",
  "model_version": "UNSET",
  "skill_versions": [],
  "prompt_version": "UNSET",
  "source_snapshot_id": "UNSET",
  "input_hash": "UNSET",
  "output_hash": "UNSET",
  "budget": {"tokens_max": null, "tool_calls_max": null},
  "observed": {"elapsed_ms": null, "tokens_used": null, "tool_calls": null},
  "claim_source_map": [],
  "scoring": {
    "correctness": null, "source_fidelity": null,
    "coverage": null, "actionability": null,
    "uncertainty": null, "reproducibility": null
  },
  "errors": [],
  "reviewer": "UNASSIGNED",
  "review_status": "not_reviewed",
  "release_status": "design_only"
}
```

**UNSET/null ist kein gemessener Wert.** Ein Datensatz wird erst dann zum *Ergebnis*, wenn die Ausführung stattgefunden hat und die Belege verlinkt sind.

## 8. Erstes konkret ausführbares Pilotprotokoll

**Pilot:** BKI-P01/T01 – Zuständigkeit erkennen. Drei synthetische Fälle T01-A/B/C; vier Strategien S0–S3; pro Strategie/Fall zunächst drei unabhängige Wiederholungen = **36 geplante Ausführungen**. Mindestens zwei unabhängige Bewertungen je Ausgabe, soweit realisierbar. Das ist eine **Machbarkeitsstichprobe**, keine Signifikanzstudie.

**Soll-Beweisstücke:** eingefrorene Aufgaben- und Quellenakten; 36 Run-Datensätze; Reviewer-Urteile; Fehler-/Gegenbeispielliste; Qualitätsmatrix; Unterschiede bei Zeit und Ressourcen; Abschlussentscheidung `bestätigt / widerlegt / nicht entscheidbar / nicht durchgeführt`.

**Vorbedingung für einen tatsächlichen Lauf:** T01-A/B/C konkret ausformulieren, Quellenpaket versionieren, fachliche Goldstandards unabhängig festlegen und die vier Strategien implementieren.

## 9. Nächster Prozess: vom Katalog zum Experimentierlabor

**Prozess BKI-LAB-01:** Task-Registry → Quellen-/Goldstandard-Registry → Skill-/Strategie-Registry → Runner → unabhängiger Evaluator → Ergebnisvergleich → Fehleranalyse → Skill-Schmiede → Regression → Freigabe/No-Loss.

**Erste Implementierungsschritte:**
1. `tasks/*.json` und `sources/*.json` für die drei T01-Fälle.
2. `strategies/*.json` mit S0 bis S3 samt identischen Ressourcenlimits.
3. Ein Runner, der `run_id`, Eingabe, Antwort und Verbrauchsmetriken ausgibt.
4. Ein Bewertungsblatt mit Muss-Aussagen, Negativprüfungen und Quellen-Claim-Verknüpfung.
5. Ein Dashboard, das nicht nur Mittelwerte, sondern **jede einzelne Fehlerklasse und fehlende Evidenz** sichtbar macht.
6. Reproduzierbarer Bericht mit eindeutigen Links auf Aufgabenversion, Quellen, Testläufe und Ergebnisakte.

## 10. Projektübergreifender No-Loss-Crosswalk

`Bürgerfrage/Referenzaufgabe → Skill → Operator → Quelle → Modell/Relation → (ggf. Trinität/Tensor/Feld) → Test → Gegenprüfung → Ergebnis → Version/Publikation`.

**Synchronisation:** Jede genehmigte Änderung aktualisiert gemeinsame Quellen- und Glossarreferenzen, Skill-Registry, Prompt-Varianten, Evaluationsakten und betroffene Tensor-/Relationsverweise. Fehlende Referenzen werden als **offen** protokolliert, nicht still ergänzt. Neu gefundene Tools und Bibliotheken gehen zuerst in den Harvest-Kandidatenbestand.

**Ergebnisstatus dieser Datei:** Ein belastbarer **Forschungs- und Versuchsplan** mit 8 Projekten, 10 Testfamilien, 30 vorgesehenen Referenzaufgaben, 6 Vergleichsstrategien und einem 36-Läufe-Pilotdesign. **0 ausgeführte bzw. bestätigte Experimentläufe aus diesem Plan.**

---
**Nächste Version v0.2:** T01-Aufgaben, Quellensnapshots, Goldstandards und Maschinenverträge tatsächlich ausformulieren. **Nächste Phase:** BKI-LAB-01 operativ aufbauen und die ersten Ergebnisse prüfen.
