# Bürger-KI · Skill-Deep-Dive und Harvest v1.0
**Stand:** 4. November 2026 · **Geltungsbereich:** ausschließlich Bürger-KI · **Status:** Bestandsanalyse, Entwicklungs- und Testprogramm, keine validierten Fähigkeiten

> **Die Menschen haben Ziele. Bürger-KI entwickelt Fähigkeiten, damit sie diese Ziele wirksamer erreichen können.** Vernetzt werden Wissen, Skills, Anwendungsmöglichkeiten, Quellen, Fehlerkorrekturen und bestehende Hilfsangebote – keine persönlichen Fallbestände.

## 1. Was ist bei Bürger-KI ein Skill?

Ein Skill ist eine **wiederverwendbare, nachvollziehbare Fähigkeit** zur Unterstützung einer konkreten Aufgabe. Er besitzt einen klaren Zweck, Eingaben, Ausgaben, Voraussetzungen, Grenzen, Quellen-/Versionstand und mindestens positive, negative und Grenztests. Ein Prompt allein ist noch kein geprüfter Skill. Auch ein rechtlich plausibler Antworttext ist noch kein nachgewiesener Nutzen.

**Vier Ebenen:**
1. **Atomare Operation:** Quelle erfassen, zeitliche Geltung prüfen, Regeln typisieren, Soll-Ist vergleichen, Gegenprobe ausführen.
2. **Zusammengesetzter Fachskill:** mehrere Operationen führen zu einer arbeitsfähigen Antwort, z. B. Zahlung oder Therapieangebot strukturiert prüfen.
3. **Aufgabenweg:** vom Ziel einer Person über Klärungsfragen bis zu nachvollziehbaren Handlungsoptionen. Keine eigenständige Fallübernahme durch Bürger-KI.
4. **Harvest-/Lernschleife:** nur überprüfte allgemein nutzbare Verbesserung wird an Katalog, Tests, Glossar, Quellen- und ggf. Tensor-Crosswalk zurückgegeben.

## 2. Inventar und harte Statusgrenze

**Primärinventar:** [SKILL_KATALOG_V0_1.json](https://github.com/Memnosis/relationalitaet/blob/research/tensoratlas-auswertung-2026-11-04/forschung/buerger-ki/SKILL_KATALOG_V0_1.json): **17 atomare Operatoren BK-OP-01 bis BK-OP-17 und 15 fachliche Kompositionen BK-F-01 bis BK-F-15**, sämtlich `specified`, ohne gespeicherte bestandene Tests und ohne Validierung.

**Fachlicher Crosswalk:** [SKILLS_ZUM_TENSOR_CROSSWALK_V0_1.md](https://github.com/Memnosis/relationalitaet/blob/research/tensoratlas-auswertung-2026-11-04/forschung/buerger-ki/SKILLS_ZUM_TENSOR_CROSSWALK_V0_1.md): Relationen, Invarianten, Kompositionsideen, zwei Vertikaltests und Transferregeln; noch keine tatsächliche Tensor-Integration.

**Früherer Benchmarkbestand:** [BENCHMARK_UND_RUECKFLUSS_V0_1.json](https://github.com/Memnosis/relationalitaet/blob/research/tensoratlas-auswertung-2026-11-04/forschung/buerger-ki/BENCHMARK_UND_RUECKFLUSS_V0_1.json): **abweichendes Schema** mit früher definierten Funktionen `BK-F-01` bis `BK-F-10`, Hypothesen und Metriken. Wichtig: Seine **BK-F-Kennungen kollidieren semantisch** mit dem späteren Skill-Katalog (z. B. `BK-F-03` = „Wohnungs- und Mietschutz“ im Benchmark, aber „Versorgungsbedarf definieren“ im Skill-Katalog). **Nie ohne Herkunftsnamespace gleichsetzen!** Das alte `BK-F` ist ein **historischer Funktionsalias** und kein eindeutiger Schlüssel für neue Joins. Vor irgendeinem automatisierten Nachzug wird ein vollständiger, explizit geprüfter Alias-/Konflikt-Crosswalk mit eigener neuer Kennung benötigt.

**Harvestergebnis heute:** Katalog und Relationstypen erfasst; `0` implementierte, `0` bestätigte und `0` validierte Skills aus diesem dokumentierten Bestand. Der Zählstand sagt nichts über Fähigkeiten anderer Dienste oder zukünftige Tests.

## 3. Welche Skillfamilien eignen sich für fachübergreifenden Einsatz?

| Skillfamilie | Basiskandidaten aus dem Katalog | Fachübergreifender Nutzen | Negative Probe |
|---|---|---|---|
| Primärquelle und Provenienz | OP-01, OP-02, OP-17 | Herkunft, Original, Änderung, Aussage nachvollziehbar | Sekundärbericht wird als Primärnorm ausgegeben |
| Rechts-/Regelstand und Voraussetzungen | OP-03, OP-04, OP-05 | In mehreren Rechtsgebieten unterschiedliche Regeln korrekt prüfen | unbekannte Voraussetzung wird zu „nicht erfüllt“ |
| Soll-Ist und Rückrechnung | OP-06, OP-07, OP-12 | Leistungen, Fristen, Mengen und Resultate vergleichen | Zeiträume oder Einheiten unvereinbar |
| Kritik, Gegenprobe, Kausalität | OP-08, OP-09, OP-10 | Widerspruchs- und Ursachenhypothesen prüfen | bloße Korrelation wird als Ursache gewertet |
| Optionen, nächster Schritt | OP-15, F-11, F-14 | Handlungsoptionen und Informationslücken erklären | eine Möglichkeit wird als garantierter Erfolg ausgegeben |
| Lernen aus Ergebnissen | OP-16, OP-17 | Baseline, Regression, Änderungsauswirkungen | Textmenge ersetzt echten Qualitätsnachweis |

Die Fachskills bleiben im jeweiligen Fachgebiet zu prüfen. Eine identische Operatorbezeichnung bedeutet nicht dieselben Normen, eine identische Zielerreichung oder gleiche Fehlerrisiken.

## 4. Harvest: Was sammeln, vergleichen und zurückführen?

**Harvest ist keine Ernte persönlicher Fälle.** Harvest bedeutet: bestehende Kompetenzen, Skill-Spezifikationen, mathematische Operatoren, Quellenverfahren, überprüfbare Muster und fehlende Gegenproben inventarisieren, **bewerten und wiederverwendbar machen**.

**A. Bestands-Harvest:** Bürger-KI-Skills; bisherige SOULution- und Tensor-Methoden nur lesen/als Kandidaten referenzieren, nicht ohne Freigabe verändern; bewährte externe Open-Source-Bibliotheken oder Standards als Recherchekandidaten. Fremde Werkzeuge bleiben fremde Implementierungen mit Lizenz-, Versions- und Eignungsprüfung.

**B. Funktions-Harvest:** Welche Aufgabe erfüllt ein Kandidat tatsächlich? Welche Eingaben braucht er? Welche Ausgaben erzeugt er? Wo versagt er? Worin unterscheidet er sich von einer einfachen Checkliste oder einer bisherigen KI-Antwort?

**C. Relations-Harvest:** Typen, Bedingungen, Differenzen, partielle Inverse, Invarianten, Zeitgeltung, Abhängigkeitsgraphen, Gegenbelege, Alternativen, Ergebnisprüfung.

**D. Kompositions-Harvest:** Welche Kombination liefert einen neuen Nutzen gegenüber Einzelschritten? In welcher Reihenfolge müssen Bedingungen und Quellen geprüft werden? Welche Teile können modular ausgetauscht werden?

**E. Negativ-Harvest:** Fehler, Abbruchgründe, unpassende Rechtslage, unklare Begriffe, Nichtinvertierbarkeit, unzureichende Quellen, fehlender messbarer Vorteil; ausdrücklich als Ergebnisse behalten.

**F. Tensor-Übergabe:** Nur typisierte, abstrahierte, geprüfte Operator- und Relationenkandidaten mit Test und Geltungsbedingungen. Die 3×3×3-Adressen sind ein möglicher Ordnungsrahmen, **kein** mathematischer Gleichheitsbeweis. Import erst nach separater Freigabe und bestandenen Tests.

## 5. Harvestergebnis als überprüfbares Objekt

```json
{
  "harvest_id": "BK-HARV-001",
  "source_namespace": "bk-skill-catalog-v0.1",
  "source_skill_ids": ["BK-OP-01", "BK-OP-05", "BK-OP-04"],
  "goal": "Anwendbare Regeln samt Herkunft und Voraussetzungen prüfen",
  "domains_to_test": ["SOZIAL", "VERWALTUNG", "FAMILIE"],
  "status": "candidate",
  "input_types": ["Normquelle", "Geltungsdatum", "abstrakter Testfall"],
  "output_types": ["Quellenverweis", "Regelstand", "Voraussetzungsstatus", "offene Fragen"],
  "invariants": ["Quelle nachvollziehbar", "offen ist nicht falsch", "Datum stimmt"],
  "negative_tests": ["falsche Normfassung", "fehlende Voraussetzung", "Ausnahme/Übergangsrecht"],
  "baseline": "Checkliste ohne Skillkomposition",
  "benefit_verified": false,
  "tensor_transfer_status": "not_requested"
}
```

Die JSON-Skizze zeigt **nur das Format eines Kandidaten**, kein behauptetes Testergebnis.

## 6. Erster fachlicher Harvest-Kandidat

**BK-HARV-001 – Regeln, Quellen und Voraussetzungen prüfen.**

Komposition: `BK-OP-01 → BK-OP-05 → BK-OP-04 → BK-OP-09 → BK-OP-12`.

**Fachübergreifende Testfelder:**
- Sozialleistungsfrage: Welche Regel galt wann, welche Voraussetzungen sind bekannt und was fehlt noch?
- Verwaltungsfrage: Welche Stelle ist zuständig, welche Fristenregel gilt und welche Ausnahmen existieren?
- Betreuungsfrage: Welche Rechtsposition und Voraussetzungen gelten in der relevanten Konstellation?

**Abnahme:** Mit synthetischen, quellenreferenzierten Testfällen muss die Komposition korrekte Voraussetzungen, die passende Rechtsfassung und echte Unsicherheiten ausweisen. Vergleich mit einer fachlich korrekten Checkliste. Ohne diesen Nachweis bleibt die Komposition `candidate`.

## 7. Zweiter fachlicher Harvest-Kandidat

**BK-HARV-002 – Geschuldet, zugesagt, tatsächlich erreicht.**

Komposition: `BK-OP-01 → BK-OP-04 → BK-OP-06 → BK-OP-12 → BK-OP-09`.

**Einsatzräume:** Sozialleistungszahlung (fällige Zahlung vs. Geldeingang), medizinische Versorgung (fachlich geeigneter Versorgungseinstieg statt bloßer Vermittlung), Verwaltungsverfahren (vorgesehene Handlung vs. tatsächlicher Verfahrensstand).

**Unterschiede bleiben erhalten:** Beträge, Termine und fachliche Behandlungseignung haben unterschiedliche Typen und Qualitätsanforderungen. „Soll-Ist“ allein entscheidet keinen Anspruch und keine medizinische Angemessenheit.

## 8. Tests und Qualität

**Minimum pro Skill:** stabile eindeutige ID mit Namespace; Version; überprüfbarer Zweck; Inputs/Outputs; Abhängigkeiten; Fachgrenzen; Quellenstand; positiver Test; negativer Test; Grenztest; Vergleich mit Baseline; Fehlerrisiken; Ergebnis; Reviewer/Prüfdatum.

**Metriken:** korrekte Antworten und Quellenabdeckung, korrekt erkannte Unsicherheit, Verfahrensfehler, Bearbeitungszeit und tatsächlicher hilfreicher nächster Schritt. Nicht gemessen wird eine angeblich einheitliche „Zufriedenheit“ ohne definierten Bezugsrahmen. Tests können zuerst mit vollständig synthetischen Situationen erfolgen.

**Status:** `inventoried → candidate → specified → implemented → tested → validated`, ferner `rejected` oder `blocked`. Übergänge benötigen dokumentierte Tests. Beim vorliegenden 32er-Inventar bleibt der ursprüngliche Status `specified`; die Ernteansätze hier sind `candidate`.

## 9. Rückkopplungs- und No-Loss-Vertrag

`Anwendungsfeld → Bürgerfrage → Quelle/Definition → Operator → Skillkomposition → Test → Negativbefund/Ergebnis → Verbesserung → fachübergreifende Prüfung → (ggf.) Tensor-Kandidat`

Jedes Objekt referenziert stabile IDs und die genaue Quellversion. Eine Änderung muss **Quellenregister, Glossar, Forschungsfragen, Thesen, Operationalisierungen, Skillkatalog, Testfälle, öffentliche Deep-Dives und Export-Kandidaten** konsistent nachziehen. Derzeit ist dies eine Arbeitsregel, **kein bereits implementierter automatischer Nachzieh-Compiler** für Bürger-KI.

**Abgrenzung:** Kein öffentliches Fall-/Patientenregister, keine Vorgabe zur Verarbeitung fremder persönlicher Angelegenheiten, keine imaginäre Community-Infrastruktur. Die Erforschung und Bereitstellung von Skills ist das Projekt.

## 10. Anschluss an Phase 3

Phase 3 überführt diese technische Tiefe in einen **einfachen, auch ohne KI verständlichen Problemlösungsweg**. Jeder Schritt kann durch einen oder mehrere Skills unterstützt werden, aber die Reihenfolge und die fachliche Beurteilung werden nicht von einer Skillliste diktiert. Die Website zeigt stets zuerst die Bürgerfrage, danach welche allgemeine Fähigkeit hilfreich sein könnte.

**Weblinks:** [Bürger-KI](./buerger-ki.html) · [Anwendungsfelder](./buerger-ki-anwendungsfelder.html) · [Phase 3: Prüf- und Lösungsweg](./buerger-ki-weg.html) · [No-Loss-Gesamtstand](./buerger-ki-gesamtstand.md).
