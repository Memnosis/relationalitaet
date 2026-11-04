# Gesetzeübergreifende Rekonstruktion behördlicher Handlungslogiken

## Vom Weisungsatlas zur eigenständigen, quellenprüfbaren Regel- und Skillarchitektur der Bürger-KI

**Forschungspaper:** BKI-WA-PAPER-002  
**Fassung:** 0.1 · 5. November 2026  
**Status:** wissenschaftliche Arbeitsfassung mit geprüften Originalfundstellen und eigenen Rekonstruktionen; keine rechtliche Einzelentscheidung, keine abgeschlossene Vollerfassung der Behördenpraxis.  
**Verbindliche projektinterne Arbeitsregel:** **Keine originalgetreuen Behörden- oder Gesetzestexte in die von uns entwickelten Handlungsanweisungen übernehmen.** Gespeichert werden eigene Rekonstruktionen, Norm- und Fundstellen-IDs, eigene typisierte Regelmodelle, Versionen, Negativbefunde und Tests. Originale verbleiben an ihren externen Fundstellen.

### Abstract

Die Sammlung interner Behördenanweisungen ist nur ein vorbereitender Schritt. Wissenschaftlich produktiver ist es, aus verschiedenen Gesetzen, Verwaltungsverfahren und behördlichen Instruktionen die **wiederkehrenden Funktionen des Verwaltungshandelns** zu rekonstruieren: Zuständigkeit, Sachverhaltsermittlung, Beratung, Anhörung, Ermessen, Begründung, Zugang zu Informationen, Entscheidung, tatsächliche Erfüllung und Nachprüfung. Diese Funktionen können in unterschiedlichen Rechtsgebieten verwandt sein, obwohl ihr Normtext, ihre Bindungswirkung, ihre Bedingungen und ihre Ausnahmen abweichen. Das Paper entwickelt deshalb eine **gesetzeübergreifende Such- und Relationsmatrix** sowie eine Pipeline, die nur **eigene fachliche Rekonstruktionen** zu atomaren Kandidaten macht. Die Originalquelle bleibt durch stabile Referenzen und Versionsnachweise erreichbar; die eigene Rekonstruktion bleibt mit Gegenbeispielen, Alternativdeutungen, Geltungsbedingungen und Testakten überprüfbar. So kann aus einem heterogenen Weisungsarchiv eine erweiterbare Forschungsbibliothek von Bürger-KI-Skills entstehen, ohne dass ein Textarchiv als vermeintlich vollständige und aktuelle Rechtsauskunft ausgegeben wird.

---

## 1. Warum eine bloße Sammlung von Weisungen unzureichend ist

Verwaltungsanweisungen sind in unterschiedliche Normsysteme, Behördenorganisationen und zeitliche Geltungsräume eingebettet. Ein Amt kann nach Bundesgesetz handeln, zugleich aber an Landesverfahrensrecht oder eine besondere Verwaltungsvorschrift gebunden sein. Dieselbe Beschriftung „Dienstanweisung“ sagt noch nichts über Geltung, Rang, Bindung, Ausnahmen und Verfügbarkeit.

Der bisherige [Weisungsatlas](./buerger-ki-weisungsatlas-ergebnis-001.md) erfasst zunächst 13 Einstiegspunkte und die 16 Länder als Suchräume. Das ist ein **Quelleninventar**, keine vollständige Bestandsaufnahme. Seine nächste wissenschaftliche Aufgabe lautet deshalb nicht „alle PDF-Dateien kopieren“, sondern: Welche Gesetzesfunktion wird durch welche behördliche Anweisung **für welchen Aufgabenträger** praktisch ausgestaltet?

**Gegenprobe:** Eine Weisung einer Bundesbehörde lässt sich nicht allein wegen identischer Bundesrechtsgrundlage auf jeden kommunalen Fachbereich übertragen. Unterschiedliche Organisation, Fachaufsicht, Bundesauftragsverwaltung oder Ausführung als eigene Landesangelegenheit verändern den Bindungszusammenhang.

## 2. Rechtsebenen und Bindung – die unverzichtbare erste Matrix

| Ebene | Gegenstand der Rekonstruktion | Prüfpflicht der Bürger-KI |
| --- | --- | --- |
| Verfassungsrecht | Gesetzesbindung, Kompetenzordnung, Rechtsschutz | Welches Organ darf handeln, welcher staatliche Vollzugstyp liegt vor? |
| EU-Recht | unmittelbar geltendes Recht, Umsetzungs- und Anwendungsvorrang je Konstellation | Welche EU-Norm gilt und wie wirkt sie im Fachgebiet? |
| Bundes- und Landesgesetz | Tatbestand, Rechtsfolge, Verfahrensrecht, Sonderregeln | Welche konkrete Norm ist für welche Aufgabe anwendbar? |
| Rechtsverordnung / Satzung | durch Rechtsgrundlage legitimierte Regelung | Ermächtigung, Gebiet, Adressat, Geltung, Rang prüfen |
| Allgemeine Verwaltungsvorschrift | verwaltungsinterne Generalregel und Vollzugskonkretisierung | Weisungsgeber, Normermächtigung/Kompetenz und Bindungsadressaten prüfen |
| Fachliche Weisung / Erlass / Dienstanweisung | konkrete Umsetzung, Arbeitsschritte, Entscheidungshilfen | interne Geltung nicht mit unmittelbar außenwirksamem Anspruch verwechseln |
| Arbeitshilfe / FAQ / Handbuch | Erklärung, fachliche Unterstützung, Anwendungspraxis | Autorität und Aktualität nicht aus Dokumenttyp oder Titel ableiten |
| Einzelfallentscheidung / Verwaltungspraxis | tatsächlich getroffene behördliche Entscheidung | Sachverhalt und Generalisierbarkeit separat prüfen |

**Verfassungsanker:** Art. 20 Abs. 3 GG bindet die Exekutive an Gesetz und Recht. Art. 83 GG sieht grundsätzlich die Ausführung von Bundesgesetzen durch die Länder vor. Art. 84 und 85 GG unterscheiden Ausführung als eigene Angelegenheit und Bundesauftragsverwaltung, einschließlich unterschiedlicher Möglichkeiten allgemeiner Verwaltungsvorschriften und Weisungen. Quellen: [Art. 20 GG](https://www.gesetze-im-internet.de/gg/art_20.html), [Art. 83 GG](https://www.gesetze-im-internet.de/gg/art_83.html), [Art. 84 GG](https://www.gesetze-im-internet.de/gg/art_84.html), [Art. 85 GG](https://www.gesetze-im-internet.de/gg/art_85.html).

**Verfahrensrechtlicher Anker:** §§ 1–2 VwVfG begrenzen den Anwendungsbereich und nehmen unter anderem Steuer- und Sozialverwaltungsverfahren aus. Für diese sind vor allem die jeweiligen Fachverfahrensgesetze zu prüfen; Landesrecht kann zudem an die Stelle des Bundes-VwVfG treten. Quellen: [§ 1 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__1.html), [VwVfG Gesamtausgabe (§ 2)](https://www.gesetze-im-internet.de/vwvfg/BJNR012530976.html), [§ 1 SGB X](https://www.gesetze-im-internet.de/sgb_10/__1.html), [§ 1 AO](https://www.gesetze-im-internet.de/ao_1977/__1.html).

Damit lautet die erste Prüffrage jeder Weisungsrekonstruktion **nicht** „Was steht in dem Dokument?“, sondern **„Für welche Behörde, Aufgabe, Rechtslage und Situation kann dieses Dokument maßgeblich sein?“**

## 3. Gesetzeübergreifende Funktionsfamilien

Die gleichen **fachlichen Funktionen** lassen sich in verschiedenen Rechtsfamilien wiederfinden. Ihr gemeinsamer Name erlaubt zunächst einen Vergleich, aber **keine automatische Übertragung der juristischen Regel**.

| Funktionsfamilie | Allgemeines Verfahren | Sozialverwaltung | Steuerverwaltung | Kritischer Unterschied |
| --- | --- | --- | --- | --- |
| Sachverhalt von Amts wegen ermitteln | [§ 24 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__24.html) | [§ 20 SGB X](https://www.gesetze-im-internet.de/sgb_10/__20.html) | [§ 88 AO](https://www.gesetze-im-internet.de/ao_1977/__88.html) | AO mit besonderen Ermittlungs- und Risiko­managementregelungen |
| Beweismittel / Mitwirkung | [§ 26 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__26.html) | [§ 21 SGB X](https://www.gesetze-im-internet.de/sgb_10/__21.html) | [§ 90 AO](https://www.gesetze-im-internet.de/ao_1977/__90.html) und weitere Vorschriften | Mitwirkungslasten und Befugnisse fachrechtlich verschieden |
| Anhörung | [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html) | [§ 24 SGB X](https://www.gesetze-im-internet.de/sgb_10/__24.html) | [§ 91 AO](https://www.gesetze-im-internet.de/ao_1977/__91.html) | Ausnahme- und Soll-/Muss-Konstellationen unterscheiden |
| Begründung der Entscheidung | [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html) | [§ 35 SGB X](https://www.gesetze-im-internet.de/sgb_10/__35.html) | [§ 121 AO](https://www.gesetze-im-internet.de/ao_1977/__121.html) | Begründungsmaßstab und Ausnahmefälle differieren |
| Akteneinsicht | [§ 29 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__29.html) | [§ 25 SGB X](https://www.gesetze-im-internet.de/sgb_10/__25.html) | besonderen Regelungen unterstellt | kein identisches allgemeines Akteneinsichtsrecht unterstellen |
| Beratung / Verfahrenshilfe | [§ 25 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__25.html) | [§§ 14–16 SGB I](https://www.gesetze-im-internet.de/sgb_1/BJNR030150975.html) | spezifische Auskunfts-/Verfahrensregeln | Sozialrecht mit besonderen Beratungs- und Annahmeregeln |
| Ermessen / Entscheidungsspielraum | [§ 40 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__40.html) | besondere Ermessensnormen | besondere steuerliche Entscheidungsspielräume | nicht jede Verwaltungshandlung ist eine Ermessensentscheidung |
| Zugang zu amtlichen Informationen | [§ 1 IFG](https://www.gesetze-im-internet.de/ifg/__1.html) für Bundesbehörden | spezifische fachliche Akteneinsicht plus Informationszugangsrecht im jeweiligen Anwendungsbereich | Steuergeheimnis und spezialisierte Regeln | IFG ist keine freie Veröffentlichungserlaubnis und nicht überall identisch |

### Forschungsbefund 1: gleiche Operation – anderer Geltungsraum

In den ersten vier Familien treten vergleichbare Prozessideen auf: Tatsachen beschaffen, Vorbringen berücksichtigen, rechtlich relevante Gründe offenlegen. Für die technische Skillbibliothek kann man **gemeinsame Operatoren** wie `identify_facts`, `check_hearing`, `test_reasoning` definieren. **Welche Normvorgaben sie anwenden dürfen, muss jedes Mal die Fach- und Geltungsschicht bestimmen.**

### Forschungsbefund 2: ähnliche Bezeichnung – andere Rechtsfolge

Bei der Anhörung kann eine sprachlich ähnliche Ausgangslage durch abweichende Ausnahmen, besondere Steuerdatenregeln oder unterschiedliche Soll-/Muss-Formulierungen einen anderen Prüfgang verlangen. Eine Bürger-KI muss diese Unterscheidung erhalten, statt aus allen Paragraphen eine einzige „Anhörungsregel“ zu verschmelzen.

### Forschungsbefund 3: behördliche Weisung ist kein Gesetzesersatz

Weisungen können für den Verwaltungsvollzug wichtig sein, ersetzen aber nicht die gesetzlichen Voraussetzungen. Ein internes Prüfschema kann beispielsweise zusätzliche Bearbeitungsschritte vorsehen. Ob daraus ein Recht des Bürgers entsteht oder eine behördliche Entscheidung rechtswidrig ist, lässt sich daraus **nicht automatisch** folgern.

## 4. Die GGO als Beispiel der Verwaltung über Verwaltungsvorschriften

Die [Gemeinsame Geschäftsordnung der Bundesministerien](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_21072009_O11313012.htm) enthält in §§ 69–71 Vorgaben zur Bezeichnung, Vorbereitung, Begründung und formellen Behandlung von Verwaltungsvorschriften. Sie ist ihrem Anwendungsbereich nach primär eine Ordnung für die Bundesministerien und kein allgemeines Landes-Vollzugsrecht.

**Eigene Rekonstruktionen, keine Wiedergabe des Originals:**

- **GGO-R69-A:** Bei einer abstrakt-generellen verwaltungsinternen Regelung verlangt die Geschäftsordnung eine hinreichend erkennbare Bezeichnung als Verwaltungsvorschrift. Prüfbar: Dokumenttyp, erlassende Stelle, Betroffenheit der GGO.
- **GGO-R69-B:** Bei der Erarbeitung solcher Vorschriften ist das bezeichnete Vorbereitungs-Handbuch als methodische Grundlage einzubeziehen. Prüfbar: tatsächlicher Vorbereitungsvorgang und Dokumentationsnachweis.
- **GGO-R69-C:** Neue Vorschriften sollen durch eine begründete Notwendigkeit getragen werden; der vorhandene Regelbestand soll vereinfacht und reduziert werden. Prüfbar: dokumentierte Notwendigkeit, Bestandsabgleich, Kompetenz.

**Präzisierung gegenüber dem ersten Atlas:** Diese drei Sätze sind keine „Originaltexte“ und **keine unabhängig fachlich abgenommenen Regelakte**. Die erste Kurzrekonstruktion darf insbesondere nicht die Verbindlichkeit der Bezeichnungspflicht zu einer bloßen Empfehlung abschwächen. Fachliche Unsicherheit bleibt als solche ausgewiesen.

## 5. Beispiel einer wirklichen Gesetzeübergreifenden Rekonstruktion

### Testgegenstand: Eine Behörde trifft eine belastende Entscheidung aufgrund unvollständiger Tatsachen

**Fallmodell:** In einer fiktiven Verwaltungsakte wird eine entscheidungserhebliche Information übersehen. Das System soll die einschlägigen Prüfanforderungen identifizieren, ohne vorher das Rechtsgebiet oder das anwendbare Verfahren zu erraten.

**Ablauf der eigenen Rekonstruktion:**

1. **Tätigkeit einordnen:** allgemeines Verwaltungsverfahren, Sozialleistung, Steuerverfahren oder besonderes Fachverfahren?
2. **Rechtsregime bestimmen:** Geltung nach §§ 1–2 VwVfG, § 1 SGB X oder § 1 AO; ggf. Landesverfahrensrecht und spezialgesetzliche Sonderregelung.
3. **Amtsermittlung untersuchen:** Wurden auch für die betroffene Person günstige Umstände unter dem jeweils geltenden Regime berücksichtigt?
4. **Mitwirkung abgrenzen:** Welche Sachverhaltsaufklärung obliegt der Behörde, welche Mitwirkung kann die Person schulden?
5. **Anhörung prüfen:** Welche Rechte und konkreten Ausnahmen gelten vor der belastenden Entscheidung?
6. **Begründung prüfen:** Stellt die Entscheidung die wesentlichen Tatsachen und Rechtsgründe in dem erforderlichen Umfang dar? Liegt eine begründete Ausnahme vor?
7. **Weisungsbezug ergänzen:** Gibt es einen für die handelnde Behörde geltenden internen Ablauf, der diese Schritte konkretisiert?
8. **Gegenprobe:** Gleiche äußere Beschreibung in einem anderen Rechtsgebiet – ändern sich die entscheidenden Voraussetzungen oder Ausnahmen?
9. **Ergebnisform:** `belegt / möglicherweise betroffen / nach Quelle ungeklärt / nicht anwendbar / widerlegt` samt Normstellen, nicht automatisch „Behörde handelte rechtswidrig“.

**Wert dieses Beispiels:** Dieselbe problemorientierte Bürgerfrage führt zu einem **vergleichbaren Prüfgraphen**, dessen rechtliche Regeln je Anwendungsbereich verschieden sind. Das ist genau die Form der Wiederverwendung, die wir suchen.

## 6. Die Projektregel „keine Originaltexte“ im Detail

### 6.1 Verbindliche Anweisung

**BKI-WA-RED-001:**

> Für unsere eigene interne Handlungs- und Skillbibliothek werden fremde Originaltexte **nicht als Textbestand gespeichert oder erneut publiziert**. Stattdessen führen wir eigene fachlich verantwortete Beschreibungen, abstrahierte Anweisungskandidaten, Quellen-URLs, eindeutige Fundstellen, Fassungshinweise, Hashes, Geltungs-/Konfliktrelationen und Tests. Für die fachliche Überprüfung wird die Originalfundstelle gesondert aufgerufen; originale PDFs werden nicht Bestandteil der veröffentlichten oder rekonstruierten Markdown-Bibliothek.

**Wichtig:** Das ist eine **bewusst strengere Projektregel**, nicht die Aussage, dass jede amtliche Vorschrift urheberrechtlich geschützt wäre. [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html) unterscheidet amtliche Werke und privilegierte amtliche Texte; andere Unterlagen, eingebettete Drittinhalte und Nutzungsbedingungen benötigen gegebenenfalls eigene Beurteilung. Auch frei zugängliche Originale können ohne Kopie nach Fundstelle und abstraktem Inhalt erschlossen werden.

### 6.2 Erlaubte interne Ergebnisobjekte

- `source_ref`: stabile URL/DOI/Aktenzeichen/Seiten- oder Abschnittsanker; Herausgeber, Abruf- und Versionsdatum.
- `hash`: SHA-256 des für die Prüfung temporär gelesenen Originals; Hash ist kein Ersatz für eine korrekte Rechtsfassung.
- `own_summary`: in eigenständiger Sprache formulierte Inhalts- und Zweckbeschreibung, ausdrücklich als Rekonstruktion gekennzeichnet.
- `rule_model`: Akteur, Handlung, Bedingung, Ausnahme, Geltungsgebiet, Adressat, Modalität und Normreferenz.
- `relation`: `implements / explains / narrows / exceptions / supersedes / conflicts_with / merely_similar`.
- `test_record`: synthetischer Positiv-/Negativ-/Grenzfall, erwartete Ergebnisse und Prüfentscheidung.
- `gap_record`: Quellen nicht verfügbar, Fassung unbekannt, Rechtsstand nicht geklärt, konkurrierende Auslegung.

### 6.3 Nicht in die interne oder öffentliche Regelbibliothek übernehmen

- Kopierte Behörden-PDFs, HTML-Volltexte und unredigierte Volltranskripte.
- Originalabsätze als „Atom“ ohne eigenständige Neuformulierung.
- Automatisch aus Originaltext geschnittene Satzfragmente.
- Ungeprüfte aus Webseiten übernommene Formulierungen, die als eigene Regeln ausgegeben werden.
- Aus „nicht gefunden“ abgeleitete Behauptungen einer fehlenden Verwaltungsvorschrift.

### 6.4 Quellentreue trotz Paraphrasen

„Keine Originaltexte“ bedeutet **nicht** „keine Originalquellen prüfen“. Die Originalfundstelle bleibt Pflicht. Wo die exakte sprachliche Unterscheidung (etwa zwingende Pflicht gegenüber bloßer Regelformulierung) entscheidend ist, muss ein Fachprüfer den Wortlaut **an der Fundstelle** vergleichen. Die eigene Regelakte hält die geprüfte Modalität und das Prüfergebnis fest, nicht die ursprüngliche Formulierung.

## 7. Neuform der Verarbeitung: PDF/Web → Metadaten → eigene Markdown-Rekonstruktion

**Bisheriger Ansatz:** Dokument lesen → kopierten Text in Markdown legen → Sätze mit Modalwörtern abschneiden → scheinbare Regeln erzeugen.

**Korrigierter Ansatz:**

1. **Quellenexistenz feststellen:** amtliche Herausgeberseite, öffentlicher PDF-Link oder freigegebener Anhang einer Auskunftsanfrage.
2. **Provenienz fixieren:** Fundstelle, Dokument-/Fassungskennung, Herausgeber, Zeitbezug, Quelle, Hash.
3. **Struktur erkennen:** Seitenzahl, Gliederung und mögliche Arbeitspositionen; Originaltext nur zur temporären Sichtung.
4. **Wirkungs- und Normraum bestimmen:** Rechtsgebiet, Behörde, Zuständigkeit, externe/interne Bindung, Zeitpunkt.
5. **Eigene Beschreibung verfassen:** Welche Handlung wird von wem unter welchen Bedingungen verlangt, zugelassen oder empfohlen?
6. **Fachübergreifende Suchmatrix befragen:** Gibt es ähnliche Regel-Operationen in anderen Gesetzen oder Behörden?
7. **Konflikt-, Ausnahme- und Hierarchieprüfung:** Welche Ähnlichkeiten sind unzulässig, welche spezialgesetzliche Regel geht vor?
8. **Atomare Modellakte erzeugen:** mit überprüfbaren Quellenreferenzen, **ohne Zitattext**.
9. **Fachprüfung und Gegenprobe:** Original bei Bedarf extern einsehen; eigene Rekonstruktion gezielt widerlegen oder bestätigen.
10. **Skill-Abnahme:** Nur fachlich geprüfte Modelle stehen zur späteren Bürger-KI-Ausführung bereit.

### Technische Umsetzung

Der [Weisungsatlas-Konverter v0.2](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/weisungsatlas_atomizer.py) wurde entsprechend umgestellt: Aus lokal bereitgestellten PDF-/HTML-/TXT-Dateien entstehen jetzt **nur Metadaten, Strukturhinweise und eine leere Markdown-Arbeitsvorlage**. Originalabsätze werden nicht mehr in Markdown oder JSON geschrieben; maschinelle Regelkandidaten werden ausdrücklich nicht vorab als gültig ausgegeben. Die Entwicklung und die Tests der späteren semantischen Rekonstruktions-KI sind noch offen.

## 8. Atomare Regelakte: Datenmodell der eigenen Handlungsanweisungen

```json
{
  "rule_id": "BKI-FUNC-HEARING-SOC-001",
  "version": "0.1",
  "rule_family": "hearing_before_adverse_decision",
  "reconstruction_type": "own_paraphrase",
  "legal_regime": "social_administrative_procedure",
  "source_refs": [
    {"url": "https://www.gesetze-im-internet.de/sgb_10/__24.html",
     "locator": "§ 24 Abs. 1 und 2", "version": "verify_at_use"}
  ],
  "actor": "competent_social_authority",
  "trigger": "planned_adverse_administrative_act",
  "required_check": "hearing_required_and_exceptions",
  "exceptions": "must_check_individually",
  "recipient": "affected_participant",
  "jurisdiction": "according_to_applicable_law",
  "effective_at": "unverified",
  "analogous_rule_ids": ["BKI-FUNC-HEARING-GEN-001",
                         "BKI-FUNC-HEARING-TAX-001"],
  "equivalence_status": "not_equivalent_by_default",
  "test_refs": ["BKI-WA-TEST-HEARING-01"],
  "independent_review": "not_completed",
  "original_text_stored": false,
  "approval": "candidate_only"
}
```

Der Vertrag vermeidet eine zentrale Falle: **`analogous_rule_ids` ist kein juristischer Gleichheits- oder Ableitungsbeweis**. Einzelne Voraussetzungen und Ausnahmen dürfen verschieden sein.

## 9. Relationsatlas: Gesetze überlagern, ohne sie zu verschmelzen

Wir schlagen **zwei getrennte Graphen** vor.

**A – Norm-/Behördengraph (juristischer Geltungsraum):** `Norm → ermächtigte/gebundene Behörde → Vollzugsaufgabe → Verwaltungsvorschrift → Geltungsgebiet → Zeitraum → mögliche Fachentscheidung`. In diesem Graphen sind Bundes-, Länder- und Kommunalbehörden nicht bloß kartografische Knoten, sondern unterschiedliche Kompetenzträger.

**B – Funktions-/Skillgraph (vergleichende Rekonstruktion):** `Frage → benötigter Operator → vergleichbare Rechtsregime → fachrechtliche Sonderbedingungen → geprüfte Regelmodelle → Test → Ergebnis`. Das Ziel ist Wiederverwendung methodischer Prüfungen, **nicht** die Übertragung fremder Normbefugnisse.

### Relationsfamilien

- **Identische Quelle:** identischer Norm- oder Fassungsanker.
- **Funktionsanalogie:** beide Regeln betreffen beispielsweise eine Anhörung.
- **Gemeinsamer Operator:** beide benötigen Prüfung der Vollständigkeit.
- **Spezialregel:** ein Rechtsregime ergänzt oder ersetzt für seinen Anwendungsbereich einen allgemeinen Maßstab.
- **Kompetenzbeziehung:** eine Stelle darf eine bestimmte Aufgabe zuweisen oder kontrollieren.
- **Abweichung:** Voraussetzungen, Fristen oder Modalität unterscheiden sich.
- **Konfliktbehauptung:** zwei Ergebnisse erscheinen widersprüchlich; die Geltung ist erst zu prüfen.
- **Nichtentsprechung:** ähnliche Begriffe, aber nachweislich verschiedene Funktion oder Rechtsfolge.

**Beweislast:** Jede als bestätigte Äquivalenz veröffentlichte Relation benötigt geklärte Begriffe, denselben Anwendungsbereich, überprüfte Voraussetzungen und geeignete Positiv-/Gegenfälle. Für die KI-Tensoralgebra ist das erst ein **möglicher** mathematischer Anschluss, kein automatisch existierender 27-Feld-Tensor.

## 10. Metamatrix für die 16 Länder und Bundesbehörden

Ein Länderatlas reicht allein nicht aus. Die angemessene Struktur ist

`(Territorium × Behördenfamilie × Rechtsgebiet × Rechtsregime × Dokumenttyp × Fassung × Regeloperation × Quellenstatus)`.

**Beispielfelder der Klassifikation:**
- **Territorium:** DE; DE-BB; DE-NW; Bezirk; Landkreis; Kommune.
- **Behörde:** Ministerium; Landesamt; Bundesoberbehörde; Jobcenter; Finanzamt; Ordnungsamt usw.
- **Fachrecht:** SGB II, SGB X, AO, Gewerberecht, Melderecht, Schulrecht, Bau-/Ordnungsrecht.
- **Normbasis:** materiellrechtliche Anspruchsnorm, Verfahrensnorm, Organisationsnorm, interne Weisung.
- **Zeitstand:** Datum der Veröffentlichung, Inkrafttreten, Aufhebung, konkrete wirksame Fassung.
- **Erkenntnisstand:** `unknown / discovered / source_verified / reconstructed / fachlich_reviewed / independently_checked`.

Nicht untersuchte Bereiche sind sichtbar mit `unknown` zu kennzeichnen. Die Anzahl der Länder ist bekannt, die Zahl aller Weisungen jedoch unbekannt und kann wegen nicht veröffentlichter Bestände aus offenen Archiven allein nicht zuverlässig hochgerechnet werden.

## 11. Differenz zwischen Transparenz und Rekonstruktion

Das Informationsfreiheitsgesetz kann den Zugang zu amtlichen Informationen des Bundes eröffnen; § 1 IFG bezeichnet den grundsätzlichen Informationszugang, während §§ 3–6 IFG Ausnahmen und Schutzinteressen enthalten. Ein erfolgreiches Auskunftsverfahren ist **keine fachliche Validierung** aller erhaltenen Informationen. Ebenso folgt aus dem Zugang nicht zwangsläufig die Berechtigung, fremde Werke unverändert zu publizieren.

Eigene Projektregel: **FragDenStaat-Anträge bleiben Fund- und Provenienzpfade.** Die Bürger-KI importiert in ihren modellierten Regelbestand nur eigene fachlich geprüfte Schlussfolgerungen und verweist auf die freigegebenen Dokumentfundstellen. Das verhindert auch, dass die erste gefundene Weisungsfassung unbemerkt zum angeblich aktuellen Behördenstandard wird.

Quellen: [IFG § 1](https://www.gesetze-im-internet.de/ifg/__1.html), [§ 3](https://www.gesetze-im-internet.de/ifg/__3.html), [§ 6](https://www.gesetze-im-internet.de/ifg/__6.html), [§ 7](https://www.gesetze-im-internet.de/ifg/__7.html).

## 12. Sechs notwendige Versuche

### BKI-WA-T01 – Funktionsvergleich Amtsermittlung
**Frage:** Lässt sich ein einheitlicher Test zur Berücksichtigung günstiger Tatsachen entwickeln, der VwVfG, SGB X und AO korrekt unterscheidet?  
**Positiv:** richtige drei Rechtsregime, zutreffende Normanker.  
**Negativ:** AO-Sonderregel ungeprüft auf den Sozialleistungsbereich übertragen.  
**Abnahme:** unabhängiger fachlicher Vergleich und dokumentierte Unterschiede.

### BKI-WA-T02 – Anhörung mit Ausnahmen
**Frage:** Erkennt der Skill die unterschiedliche Struktur der Anhörungsanforderung und fachlichen Ausnahmen?  
**Grenzfall:** automatisch erlassene Entscheidung, Rechtsgebiet unbestimmt.  
**Abnahme:** keine pauschale Anhörungspflicht ohne Ausnahmen und anwendbares Verfahren.

### BKI-WA-T03 – Begründung und Ermessen
**Frage:** Kann die KI rechtliche Gründe, tatsächliche Gründe und die gesonderte Begründung von Entscheidungsspielräumen unterscheiden?  
**Negativ:** normale Begründungsanforderungen als vollständigen Ermessensnachweis ausgeben.

### BKI-WA-T04 – Bundes-/Landes-Weisungsgrenze
**Frage:** Kann die KI erkennen, dass eine Bundesweisung nicht automatisch einer beliebigen Kommune bindend vorgegeben ist?  
**Abnahme:** Prüfgraph mit Art. 83–85 GG und konkreten Ausführungszuständigkeiten.

### BKI-WA-T05 – Eigene Rekonstruktion statt Kopie
**Frage:** Exportiert die Pipeline aus einer Prüfeingabe ausschließlich Quellenmetadaten, Strukturdaten und eine eigene leere Rekonstruktionsvorlage?  
**Negativ:** Textkopien in Markdown, JSON, Debugprotokollen und vermeintlichen „Atomen“.  
**Abnahme:** automatisierter Nichtübernahme-Test mit künstlicher Schlüsselphrase, zusätzlich manuelle Sichtprüfung.

### BKI-WA-T06 – Versionen und Konflikte
**Frage:** Erkennt ein Skill den Unterschied zwischen einer alten Weisungsfassung und einer neuen Gesetzesnorm?  
**Abnahme:** Ergebnis als potenzieller Fassungs-/Rechtskonflikt mit genauer Zeit- und Fundstellenangabe; keine automatische Rechtswidrigkeitsbehauptung.

## 13. Forschungsleistung, die wir wirklich messen wollen

**Nicht:** Anzahl kopierter PDFs, Wortmenge der Markdown-Dateien oder Anzahl automatisch extrahierter Sätze.

**Sondern:**
1. Zahl eindeutig zugeordneter Behörden-/Norm-/Fassungsbeziehungen.
2. Zahl fachlich geprüfter **eigener** Regelmodelle.
3. Zahl bestätigter und widerlegter funktionsübergreifender Relationen.
4. Zahl korrekt erkannter Ausnahmen, Nichtentsprechungen und Geltungswechsel.
5. Trefferquote mit unabhängigen Goldstandards und negativen Testfällen.
6. Erhalt der Quellen- und Versionsprovenienz ohne Originaltextübernahme.
7. Messbarer Mehrwert gegenüber bloßer Direktantwort und einfachstem Regel-Skill.
8. Wiederverwendung eines allgemeinen Prüfschritts in mindestens zwei fachlich verschiedenen Rechtsregimen.

Ein **falsifizierbarer Forschungsanspruch** ist: Ein methodisch geteilter, aber rechtlich streng typisierter Skill kann verschiedene Verwaltungsverfahren zuverlässiger untersuchen als eine untypisierte, pauschal verallgemeinerte Weisungsregel. Der Nachweis steht aus.

## 14. No-Loss-Architektur und Projektabgleich

`Quelle/Fundstelle → Dokumentfassung → Gesetzes-/Behördenkompetenz → eigene Rekonstruktion → Funktionsfamilie → atomare Regel → Gegenbeispiel → Test → Skill → Ergebnisakte → Paper`.

Bei einer Änderung der Quelle sind mindestens neu zu prüfen: Fassungsstand, betroffene Regel-ID, Behördenbindung, Verfahrensrecht, Fachskill, Negativfälle, Publikationsaussagen. Das gemeinsame **Glossar**, die Quellenregister und die Skill-IDs müssen synchronisiert werden. Neue Kandidaten bleiben im Harvest-Pool, bis sie eine Prüfung bestehen.

**Bestandskorrektur (No-Loss):**
- Der frühere [Weisungsatlas v0.1](./buerger-ki-weisungsatlas-ergebnis-001.md) enthielt eine Idee zur PDF→Markdown-Volltranskription und ein Skript, das Quelltexte exportierte. Diese **Prozessannahme ist durch BKI-WA-RED-001 ersetzt**.
- Das ursprüngliche Dokument bleibt als historischer Forschungsstand referenzierbar, darf aber nicht länger als aktuelle Ausführungsanweisung gelten.
- Die nun überarbeitete Pipeline v0.2 exportiert keine Quellabsätze. Sie liefert eine Vorlage für eine menschlich oder später technisch unterstützte **eigene** Rekonstruktion.
- Bestand 13 Quellen-Einstiege und 16 Bundesländerknoten bleibt vorläufig. Kein fingierter Vollerfassungs- oder fachlicher Abnahmestatus.

## 15. Wissenschaftlicher Ausbauplan – noch keine neue Phase freigegeben

**Schritt A:** Sechs Funktionsfamilien vollständig quellenbasiert typisieren (Amtsermittlung, Anhörung, Begründung, Beratung, Informationszugang, Zuständigkeit).  
**Schritt B:** Jeweils VwVfG, SGB X, AO und ausgewählte landes-/fachrechtliche Abweichungen getrennt modellieren.  
**Schritt C:** Mit mindestens zwölf synthetischen Fällen und zwölf Gegenbeispielen die Unterschiede testen; Prüfurteile unabhängig abnehmen.  
**Schritt D:** Erst danach entsprechende eigene Handlungsanweisungen als freigegebene Skills aufbauen und mit dem Bürger-KI-Strategielabor vergleichen.

**Gesamtstatus:** Die Projektregel und die Meta-Architektur sind entworfen; mehrere Rechtsgrundlagen sind gegen ihre offiziellen aktuellen Einzelnorm-Fundstellen geprüft. Die tatsächliche fachliche Abnahme einzelner Regelmodelle und die vollständigen Vergleichstests fehlen. Der allgemeine Bürger-KI-Fortschrittszähler wird deshalb **nicht automatisch erhöht**.

---

## Primärquellenverzeichnis (nur Links und eigene Einordnung)

**Grundgesetz:** [Art. 20](https://www.gesetze-im-internet.de/gg/art_20.html), [83](https://www.gesetze-im-internet.de/gg/art_83.html), [84](https://www.gesetze-im-internet.de/gg/art_84.html), [85](https://www.gesetze-im-internet.de/gg/art_85.html). Kompetenz-, Gesetzesbindungs- und Weisungsfragen.

**Verwaltungsverfahren:** [§ 1 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__1.html), [§ 24](https://www.gesetze-im-internet.de/vwvfg/__24.html), [§ 25](https://www.gesetze-im-internet.de/vwvfg/__25.html), [§ 26](https://www.gesetze-im-internet.de/vwvfg/__26.html), [§ 28](https://www.gesetze-im-internet.de/vwvfg/__28.html), [§ 29](https://www.gesetze-im-internet.de/vwvfg/__29.html), [§ 39](https://www.gesetze-im-internet.de/vwvfg/__39.html), [§ 40](https://www.gesetze-im-internet.de/vwvfg/__40.html).

**Sozialrecht:** [§§ 14–17 SGB I](https://www.gesetze-im-internet.de/sgb_1/BJNR030150975.html), [§ 1 SGB X](https://www.gesetze-im-internet.de/sgb_10/__1.html), [§ 20](https://www.gesetze-im-internet.de/sgb_10/__20.html), [§ 21](https://www.gesetze-im-internet.de/sgb_10/__21.html), [§ 24](https://www.gesetze-im-internet.de/sgb_10/__24.html), [§ 25](https://www.gesetze-im-internet.de/sgb_10/__25.html), [§ 35](https://www.gesetze-im-internet.de/sgb_10/__35.html).

**Steuerrecht:** [§ 1 AO](https://www.gesetze-im-internet.de/ao_1977/__1.html), [§ 88](https://www.gesetze-im-internet.de/ao_1977/__88.html), [§ 90](https://www.gesetze-im-internet.de/ao_1977/__90.html), [§ 91](https://www.gesetze-im-internet.de/ao_1977/__91.html), [§ 121](https://www.gesetze-im-internet.de/ao_1977/__121.html).

**Weisungswesen und Informationszugang:** [GGO §§ 69–71](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_21072009_O11313012.htm), [IFG](https://www.gesetze-im-internet.de/ifg/), [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html), [Weisungsatlas](./buerger-ki-weisungsatlas.html).

*Ende der Forschungsversion 0.1. Die nächste Phase darf aus diesem Paper erst nach dem Abgleich von Registern, Konverterregel und Gegenproben entwickelt werden.*
