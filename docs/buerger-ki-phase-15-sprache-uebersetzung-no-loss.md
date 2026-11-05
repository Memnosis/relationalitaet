# Phase 15 – Sprache gezielt einsetzen, Bedeutungen übersetzen, Erkenntnisse erhalten

**ID:** BKI-PH15-LANG-001 · **Stand:** 05.11.2026 · **Status:** Bestand stichprobenartig geprüft; Forschungs- und Umsetzungsplan dokumentiert, noch kein Website-Rollout und keine fertige Übersetzungsengine.  
**Hauptpaper:** [Zwischen Worten und Wirklichkeit v0.2](./paper-buerger-ki-sprachraeume-termini-operationalisierung-claims-v0-1.md)  
**Verbindliche Leitidee:** Öffentlichkeit beginnt beim Menschen; Forschung kann tief sein, muss aber den Rückweg zur menschlichen Frage freihalten.

## 1. Ergebnis: Was jetzt wirklich vorliegt

Das historische Originalsprachen-Paper bewahrt die frühen Headlines und berichtet den Vergleich 64/64 erhaltener H1–H3-Überschriften mit der früheren Fassung. Das zweite, neue Sprachräume-Paper analysiert Sprachräume, Termini, Aussagearten, Operationalisierungen und Perspektivwechsel. In v0.2 enthält es eine konkrete Platzierungsstrategie und sechs spezifizierte Übersetzungsleistungen. Zwei redaktionelle Claim-Register sind getrennt: **21 historische Anker**, **28 neue, nicht freigegebene Vorschläge**. Die Bürger-KI-Forschungsbibliothek indiziert beide Forschungsstränge.

Der *vorgeschlagene* Sprachoperator ist noch kein funktionierender Skill. Die neue v0.2 ist kein unabhängiges Gutachten aller Rechts-, Politik- und Versorgungsdaten des Gesamtprojekts.

## 2. Auditmatrix: vorhandene Objekte und sichere Aussagen

| Objekt | Konkreter Fundort | Tatsächlich feststellbar | Begrenzung / No-Loss-Aktion |
| --- | --- | --- | --- |
| Hauptseite | `docs/buerger-ki.html` | menschliche Hero- und Originalüberschriften vorhanden; Lernwege folgen auf den frühen Kernabschnitten | nicht durch Projektmanagement-/Forschungslisten ersetzen; Browserprüfung offen |
| historischer Sprachaudit | `docs/paper-buerger-ki-originalsprache-claims-didaktik-no-loss-v0-1.md` | 64 ursprüngliche H1–H3-Titel laut Voranalyse erhalten | historische Snapshot-Referenz behalten; bei Änderungen Neuvergleich |
| Claim-Bestand 1 | `docs/data/bki-redaktionelle-anker-claims-v0-1.json` | 21 originalbasierte redaktionelle Anker mit Placement | Schutz und fachlicher Korrekturvorbehalt |
| Claim-Bestand 2 | `docs/data/bki-sprachraeume-claims-v0-1.json` | 28 neue, noch nicht redaktionell freigegebene Vorschläge | nicht automatisch auf Website oder als faktische Evidenz publizieren |
| wissenschaftliches Claim-Schema | `forschung/register/schema/claim.schema.json` | kontrolliertes `CLM-...`- und `SRC-...`-Format mit Quellen-/Evidenz-/Freigabefeldern | separate Mapping-Schicht; redaktionelle Slogans nicht als Fachclaims umetikettieren |
| Glossar im Web | `docs/data/glossar-kern.json` | 12 kuratierte Definitionskarten | 1.072 Originalbegriffe lediglich als historischer Bestand referenziert; Vollimport offen |
| öffentliche Thesen | `docs/data/thesen-uebersicht-v1.json` | 6 thematische Linien | weder historischer Gesamtbestand noch 12 neue LANG-T-Hypothesen damit identisch |
| Orchestrierung | `docs/data/bki-lernpfade-orchestrierung-v0-1.json` | 5 Haupteinstiege, 5 Lernwege, 6 Fachfilter, 12 Objektarten | Entwurfs- und Routingmodell, keine vollautomatische No-Loss-Implementierung |
| Pilot | `docs/data/bki-therapieplatz-fuenf-blickwinkel-v0-1.json` | 5 Perspektiven + 5 Spiegelungen | Fachquellen-/Bedeutungsübersetzungen noch nicht komplett als maschinenprüfbare Transformation modelliert |
| Bibliothek | `docs/data/bki-forschungsbibliothek-v0-1.json` | 21 kuratierte Einträge | ausdrücklich kein Gesamtarchiv |
| Standards | `forschung/koordination/FPP_01_STANDARDS_QUELLEN_GLOSSAR_V0_1.json` | dokumentierte Standards-Referenzen; Glossar-Crosswalk angekündigt | Referenzen sind keine Validierung eigener Projekthypothesen |
| Zenodo-Quellen | `forschung/register/QUELLEN_REFERENZSET_V0_1.json` | ausgewählte eigene historische Werke, datiert/DOI-bezogen | Veröffentlichung und Dateiabruf belegen nicht ihre fachlichen Aussagen |

**Umfang der Prüfung:** Zuordnung anhand aktuell im Repository vorliegender Strukturen und repräsentativer Texte, kein Full-Content-Review aller 582 Baumobjekte und kein Import des historischen ZIP-Archivs.

## 3. Wie wir Sprache tatsächlich einsetzen

**Stark:** Hero, Projektidentität und sachlich interessante Umkehrungen. **Mittel:** Einführung eines Kernthemas und Überschriften zu überraschenden Erkenntnissen. **Dezent:** Navigation, Zwischenüberschriften, Erklärabsätze und Lernhilfen. **Neutral und präzise:** Quellen, Rechtsgrundlagen, Indikatoren, wissenschaftliche Daten, Skill-Spezifikationen und Tests.

Ein guter Perspektivwechsel erhält einen knappen merkwürdigen oder prägnanten Satz, danach aber eine normale Erklärung mit fachlichen Voraussetzungen. Für Menschen mit Alltagsfragen nie erst das Quelleninventar ausrollen.

Die bestehende Anfangssprache bleibt unangetastet; nur tatsächlich neue Erkenntnisrichtungen dürfen neue Claims benötigen. „Wissen verbinden. Lösungen möglich machen.“ gehört zur Stimme von SOULution; die Bürger-KI und der KI-Tensor behalten ihre Identitäten.

## 4. Übersetzen als prüfbare Funktion

| Übersetzung | Pilotoutput | Fehlerprüfung |
| --- | --- | --- |
| TR-01 Alltag → Fachfrage | Ziel, offene Bedingungen, passende Begriffe | Diagnose-/Rechtsbehauptung ohne Quelle? |
| TR-02 Fachsprache → Klartext | Erklärung + Originaldefinition + Ausnahmen | Definition/Unsicherheit verloren? |
| TR-03 Institution → Wirkung | Vorgang und Ziel-/Leistungserfüllung getrennt | „erledigt“ unzulässig mit „gelöst“ gleichgesetzt? |
| TR-04 Quelle → These/Test | typisierte Aussage + Messregel + Gegenprobe | Norm/Empirie und Korrelation/Kausalität verwechselt? |
| TR-05 Formalmodell → Lernweg | erklärter Zusammenhang + Link zur Relations-/Testakte | metaphorische Analogie als Beweis dargestellt? |
| TR-06 Sprachen/Rechtsräume | Ausgangs- und Zielbenennung + Sach-/Rechtskontext | behauptete Äquivalenz statt Unterschied? |

**Bewertung:** exact-in-context / partial-overlap / broader / narrower / analogy-only / contradiction / not-equivalent / unassessed. Für die meisten migrations- und rechtsbezogenen Übersetzungen zunächst `unassessed` statt Sicherheit zu simulieren.

## 5. Technischer Crosswalk ohne Identitätsverlust

Die drei Einheiten **redaktioneller Claim**, **fachlicher Claim** und **Fachkonzept** sind nicht austauschbar:

- `BKI-CLAIM-...` = historischer redaktioneller Anker.
- `BKI-LC-...` = neuer redaktioneller Vorschlag.
- `CLM-...` = fachliche Einzelbehauptung unter dem bestehenden wissenschaftlichen Schema.
- `LANG-T...` = vorerst Paper-interne Forschungshypothese.

Ein Crosswalk erhält `from_id`, `to_id`, `relation_type` (`explains`, `expresses`, `tested_by`, `supported_by`, `contradicted_by`, `unassessed`), `scope`, `source`, `review_status` und `version`. Er **vergibt keine neuen CLM-IDs** ohne vollständige Evidenzdaten. Das Redaktionsregister erhält zukünftig optional `related_claim_ids[]`, `concept_sense_ids[]`, `allowed_placements[]`, `risk_note`, `review_status`; historische vorhandene Datensätze bleiben unverändert, bis ein Migrationsvertrag existiert.

### Synchrongrenzen

Bei jeder Übersetzungsänderung nachziehen: Quellenrolle / Quellenfassung; Glossar und Begriffssinn; fachliche These/Claim; Operationalisierung; Test und Gegenfall; Skill; Lernpfad/Website-Text; redaktionelle Claims; Änderungsakte. Ein fehlender Abgleich wird als offener Impact protokolliert, nicht still übernommen.

## 6. Phase 15: Arbeitsreihenfolge und Abnahmekriterien

| Priorität | Paket | Liefergegenstand | Abnahme |
| --- | --- | --- | --- |
| A – architekturkritisch | BKI-15.1 Baseline | unveränderter Überschriften-/Claim-Snapshot und Fundstellen | 21/21 Claims und historisch verifizierte Titel referenzierbar; keine neuen Löschungen |
| A – architekturkritisch | BKI-15.2 Mapping | Meta-Crosswalk von BKI-CLAIM, BKI-LC, LANG-T zu wissenschaftlichen CLM-/SRC-Kandidaten | keine Scheingleichheit; unbekannte Referenzen bleiben offen |
| B – Schlüsselwirkung | BKI-15.3 Quellen/Glossar | 12 Webbegriffe und Originalglossar v15.4 mit Status und Proben abgleichen | 1.072 nie mit 12 gleichsetzen; Duplikate/Mehrdeutigkeiten sichtbar |
| B – Schlüsselwirkung | BKI-15.4 Übersetzungspilot | fünf öffentlich belegte Perspektivkonversionen; Therapieplatz zuerst | Input, Output, Geltung, Verlust, Gegenprobe, Quelle vorhanden |
| B – Schlüsselwirkung | BKI-15.5 Redaktionspilot | 2–3 Stellen zur echten Erkenntnisöffnung wählen, ohne Hero-Umbau | Original-Headlines bleiben; Links funktionieren; Aussage fachlich plausibel |
| C – empfohlen | BKI-15.6 Prüfprotokoll | Fachreview, Verständnistest, fehlerhafte Übersetzungen als Negativbeispiele | keine erfundenen Erfolgsscores, Negativresultate erhalten |
| C – empfohlen | BKI-15.7 Automatisierung | Änderungs-/Impact-Diff im No-Loss-Compiler | Quell-/Begriffswandel markiert abhängige Claims und Lernwege |

**Erste fünf Fälle:** Therapieplatz; bewilligte, aber nicht ausgezahlte Sozialleistung; schulisches Unterstützungsangebot oder Pflege; ein politischer Programmbeschluss im Vergleich zur Wirkung; ein relationales KI-Tensor-Beispiel. Das ist eine Testauswahl, keine Aussage über fertige Lösungsfähigkeiten.

## 7. Quell- und Statuskontrolle

Externe methodische Referenzen:
- [EU-Kommission: Plain language](https://translation.ec.europa.eu/languages-and-translation-european-commission/plain-language-making-european-commission-texts-clear_en) – Klarheit und notwendige Fachpräzision.
- [EU-Kommission: English Style Guide](https://commission.europa.eu/system/files/2023-11/styleguide_english_dgt_en.pdf) – Zielgruppenunterschied und technische Fachbegriffe.
- [W3C SKOS](https://www.w3.org/TR/skos-reference/) – Begriffe, unterschiedliche Benennungen und Relationen.
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) – Herkunft und Versionierungsbezüge.

**Offen:** Links der konkreten Fach- und Rechtsquellen in allen fünf Pilotfällen bis auf Fundstellenebene verifizieren. Für die Diskussion des Gesamtsystems projektinterne Zenodo-Eigenquellen, internationale Standards und externe Studien sauber unterscheiden. Referenzen in diesem Plan sind eine Arbeitsgrundlage, keine pauschale Validierung der Hypothesen.

## 8. Was die Phase nicht tun darf

Keine Übernahme fremder Rechtsordnungen als gleichwertig; keine automatischen medizinischen Bewertungen; keine Verarbeitung persönlicher Bürgerdaten als Projektziel; keine zentrale Ablage von Bürgerfällen; keine unbelegte Schuldzuweisung; keine unprüfbaren Wirkungsversprechen; keine Umdeutung des Projekttensors zum mathematischen Tensor ohne Definition und Beweis; keine erzwungene 3×3×3-Spracheinordnung. Die fünf Lernperspektiven bleiben **freiwillige Navigationsmöglichkeiten**, nicht ein Pflichtverfahren.

## 9. Resultat und nächster Einstieg

**Dokumentiert:** Sprachstrategie im Hauptpaper, erste Inventar-/Schema-Gapanalyse, konkret testbarer Phase-15-Plan.

**Noch auszuführen:** Formaler Crosswalk, Glossar-Originalabgleich, Übersetzungskorpus, Implementierung der Tests, Live-/Browserprüfung und redaktionelle Freigabe.

**Empfohlener erster Arbeitsschritt:** BKI-15.2 Crosswalk, parallel mit einem kleinen, überprüfbaren Therapieplatz-Übersetzungsbeispiel; erst danach öffentliche Sprachakzente verändern.
