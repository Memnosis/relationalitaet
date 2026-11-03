# Methodenkatalog für die gegenseitige KI-Prüfung, Forschung, Daten und Website
**Version:** 1.0 / erweiterbar · **Owner:** GPT Website + Claude Daten/Forschung · **Redaktion:** Nils  
**Status:** Auswahl und Zuordnung anerkannter externer Standards als Arbeitsbasis, nicht ISO-Zertifizierung oder bereits nachgewiesene Projektkonformität. Der öffentliche Git-Bericht beschreibt das Verfahren; nicht veröffentlichte interne Originale bleiben außerhalb des öffentlichen Git.

## 1. Trennung der Prüfobjekte
- **Projektthese:** wissenschaftliche Hypothese, Gegenhypothese, Quelle, Operationalisierung, Beweisakte, Falsifikation.
- **Datenobjekt:** Version, ID, Provenienz, Schema, Validierung, Rechte, Sichtbarkeit, Export.
- **Softwareobjekt:** Quellcode, Architektur, Funktion, Tests, Performance, Barrierefreiheit.
- **Publikation:** Verständlichkeit, Fakten, didaktische Tiefe, Quellen, Formate DOCX/PDF/MD.
- **KI-Arbeitsobjekt:** Originalauftrag, Prompt/Agent/Meta-Vertrag, tatsächlich ausgeführter Trial, Selbst- und Peerreview, Freigabe.
Diese Objekte besitzen **eigene Prüfnachweise**; ein gutes CI-Ergebnis beweist keine wissenschaftliche These.

## 2. Anerkannte Referenzen – konkrete Anwendungsprofile
| ID | Referenz / offizieller Zugang | Geltung | Unser prüfbarer Mindestanspruch | Owner |
|---|---|---|---|---|
| STD-D01 | FAIR Guiding Principles, Wilkinson et al. 2016, https://doi.org/10.1038/sdata.2016.18 | Forschungsdaten | IDs, Auffindbarkeit, Quellenzugang, Maschinenlesbarkeit, Rechte und Nachnutzbarkeit | Claude |
| STD-D02 | W3C PROV-O, https://www.w3.org/TR/prov-o/ | Provenienz | Entity / Activity / Agent, erzeugt/abgeleitet/geprüft, ursprüngliche Version und Prüfer | Claude |
| STD-D03 | W3C SHACL, https://www.w3.org/TR/shacl/ | semantische Daten | Shapes für definierte Claims, Relationen, Statuswerte, Fehler/Negativfälle | Claude |
| STD-D04 | JSON Schema, https://json-schema.org/specification | JSON-Register | Typen, Pflichtfelder, enums, Version, Invalid-Samples, Schema-Migration | Claude |
| STD-D05 | W3C DCAT 3, https://www.w3.org/TR/vocab-dcat-3/ | Datenkataloge | interne Datensatzfamilien und externe veröffentlichbare Lesesichten getrennt | Claude |
| STD-S01 | ISO/IEC 25010:2023, https://www.iso.org/standard/78176.html | Softwareproduktqualität | passendes Qualitätsmerkmal nennen, Mess-/Abnahmekriterium und Test statt bloßem „hochwertig“ | GPT + Claude |
| STD-S02 | Semantic Versioning 2.0.0, https://semver.org/ | Schnittstellen/Artefakte | breaking vs. kompatible Versionen, Rückwärtskompatibilität | beide |
| STD-S03 | OpenAPI Specification, https://spec.openapis.org/oas/latest.html | API-Integration | Eingabe, Ausgabe, Autorisierung, Fehlercodes, Versionen | beide |
| STD-S04 | W3C WCAG 2.2, https://www.w3.org/TR/WCAG22/ | Website | semantische Struktur, Tastatur, Fokus, Kontrast, verständliche Navigation, Regression | GPT, Claude Peerreview |
| STD-W01 | Diátaxis, https://diataxis.fr/ | Dokumentationsdidaktik | Tutorial, How-to, Erklärung, technische Referenz sichtbar unterscheiden | GPT, Claude Peerreview |
| STD-W02 | W3C HTML Standard und ARIA Authoring Practices, https://www.w3.org/WAI/ARIA/apg/ | Web-UI | richtige HTML-Semantik, kontrollierte Interaktionen, Screenreader-Feedback | GPT |
| STD-A01 | NIST AI RMF 1.0, https://www.nist.gov/itl/ai-risk-management-framework | KI-Governance | Govern/Map/Measure/Manage, dokumentierte Risiken und Befunde | beide |
| STD-G01 | RFC 7946 GeoJSON, https://www.rfc-editor.org/rfc/rfc7946 | Geo-KI-Datenaustausch | Geometrietyp, Koordinatenkonvention, schemageprüfte Roundtrips | Claude + GPT Geo-KI |
| STD-G02 | OGC Simple Features / GEOS, https://libgeos.org/ | Geometrieoperationen | gültige Geometrien, Intersection/Union/Buffer, degenerierte Eingaben | Claude + GPT Geo-KI |
| STD-G03 | OGC GeoSPARQL 1.1, https://www.ogc.org/standards/geosparql/ | Geodaten/Wissensgraph | Geodatenrelationen, RDF, räumliche Anfrage, unabhängige Tests | Claude |
**Wichtig:** Die vollständigen kostenpflichtigen ISO-Normtexte sind nicht notwendigerweise zugänglich; die offizielle Normbeschreibung begründet den Einsatz, keine behauptete Einzelkonformität.

## 3. Eigene Skills / wiederverwendbare Prüf- und Erzeugungsfähigkeiten
| ID | Skill / Methode | Input | Ergebnis | Validierungsregel |
|---|---|---|---|---|
| SK-NOLOSS | Archiv-/Versionscrosswalk | ZIP, SQL, CSV, Git-Revisionsanker | Source-/Werk-/Versionsgraph | Hash, Duplikat-/Konfliktliste, unveränderte Originale |
| SK-CLAIM | Claim-zu-Quelle | Claim-ID, DOI/Datei, Fundstelle | Prüfstatus / Evidenz | digitaler Zugriff vs Behauptungsbeweis getrennt |
| SK-TENSOR | Tensor-/Relationsvalidator | Träger, Achsen A/B/C/G, Operator | formal/semantisch geprüfte Abbildung | Typen, Invarianten, Gegenmodell |
| SK-PROMPT | Prompt/Agent/Meta-Test | Arbeitsvertrag, Modellversion, I/O | Trial-Akte | reproduzierbare Ausführung, Negativfall, Review |
| SK-DIDAKTIK | Lesetiefen-/Diátaxis-Audit | HTML/MD/DOCX/PDF | E1/E2/E3 und Dokutypen | konkrete Lernaufgaben, Fachbelege, Peerreview |
| SK-WEBQA | Website-Regressionsprüfung | HTML, JS, CSS, Git-SHA | Links, Anker, Navigation, Barrierefreiheit | statischer Test + Browserprobe getrennt |
| SK-GEO | Geometrie-Roundtrip | SVG, WKT/WKB/GeoJSON, Geometriemodell | geformte und inverse Operation | degenerierte und negative Fälle, numerische Toleranz |
| SK-IMPACT | Aufgaben-/Abhängigkeitsanalyse | Task-IDs, requires, enables, impact_domains | Blocker, Reihenfolge, Schlüsselwirkung | nur explizite Kanten und überprüfte Outputs; kein erfundener Nutzen |
| SK-PRIORITY | rollenabhängige Priorisierung | Dringlichkeit, Architektur, Hebel, Sperrwirkung, Aufwand, Evidenz | GPT-/Claude-Sicht, Top-Aufgaben | Gewichtung transparent, Sensitivität über mehrere Vektoren |
| SK-CONDENSE | reflektierende Verdichtung | Reviewberichte nach 3 vollen Zyklen | Redundanzen, Regeln, neue Standards | Vorher-/Nachher-Nachweise, Nils-Freigabe bei Modelländerung |

## 4. Multi-Kriterien-Priorisierung je KI
Die Reihenfolge ist **nicht** dieselbe bei beiden KIs. Pflichtdimensionen, Skala 0–3 (noch nicht beurteilt = null):
1. `urgency` akuter Blocker/Frist,
2. `architecture` systemweite Struktur,
3. `leverage` wiederverwendbare Schlüsselwirkung,
4. `unblocks` nachgewiesene Abhängigkeiten,
5. `risk` Gefahr falscher Veröffentlichung/Datenverlust,
6. `readiness` tatsächlich vorliegende Eingangsdaten,
7. `effort` Kosten/Komplexität,
8. `owner` GPT/Claude/Nils,
9. `evidence` aktueller Nachweisstand.
**Claude** priorisiert stärker Datenverlust, Provenienz, Geltungs- und Referenzintegrität. **GPT** priorisiert stärker öffentliche Fehler, verständliche Lernwege, Navigation, vorhandene Quellen-/Statusdarstellung. Nils wählt Konflikte/Publikationsfreigaben, nicht Einzeltests.
Sortierungen nach Dringlichkeit, Architektur, Hebel/Blocker sowie risikobasierter und machbarkeitsbasierter Reihenfolge immer nebeneinander verfügbar machen; die angezeigten Prioritätszahlen sind *Planungsannahmen*, keine Erfolgsstatistik.

## 5. Review- und Lernprozess
- In **jeder Runde** prüfen beide KIs die Tasks: erledigt/teilweise/offen, neue Blocker, fehlende Eingänge, Abhängigkeiten, Prioritätsänderung, Auswirkungen auf andere Felder.
- Jede KI prüft die Artefakte der jeweils anderen anhand der bestehenden Vektoren W01–W10, D01–D10, X01 und fügt bei Bedarf begründete neue Vektoren `W11+`, `D11+` oder `X02+` hinzu. **Nichts ohne Original-ID überschreiben.**
- Für neue Standards/Skills: Quelle, Normstatus, Geltungsbereich, Lizenz/Umsetzungskosten, erwarteter Messgewinn, minimale Probeläufe, Konkurrenz zu vorhandenem Skill, Reviewdatum.
- **Verdichtung (SK-CONDENSE):** nach 3 vollständigen Zyklen wiederholte Anforderungen, doppelte Prüfschritte, veraltete Heuristiken und wirksame neue Skills identifizieren. Nicht automatisch Quelle/Einzelfall löschen: allenfalls Varianten konsolidieren mit rückführbarem Crosswalk.
- Nach 3 Analysen (~Zyklus 9) Nils' Weiterentwicklungsentscheidung, ggf. bis 12; alle drei Quellenversionen (vor/nach/Review) bleiben nachvollziehbar.

## 6. Konkrete P0-Aufträge
**Claude:** registerrelevante Standards D01–D05/S01/A01 als Validierungsprofile operationalisieren, Beispiele/Negativtests an echten Quellen-/Claimobjekten; eigenes Datenprioritätsranking und die im Websiteprojekt nötige freigegebene öffentliche JSON-Projektion liefern. Außerdem GPT-Website gegen Diátaxis, Quellen- und Testdisziplin prüfen.

**GPT:** Projektmanagement-Seite mit echten Task-IDs, Stufenfortschritt, rollenabhängiger Priorisierung, Wirkungs-/Abhängigkeitsansichten; einen auditierbaren Website-Gesamtbestand und Thesen-/KIGeschichte-/Geo-KI-Lernpfad erstellen. Dazu Claude die didaktischen Lücken mit konkreten Fragen zurückgeben.

## 7. Quellen-/Sicherheitsgrenze
Der umfassende unveröffentlichte Zenodo-/Manuskript-/Architektur-/Promptpool ist **nicht** in das öffentliche Git-Repository zu kopieren. Für die Website nur eine geprüfte reduzierte Lesesicht. Ein öffentlicher Bericht über interne Prüfmethoden ist noch keine Freigabe aller internen Test-Prompts. 
