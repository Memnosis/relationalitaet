# Website-Runde: Projektmanagement, KI-Geschichte, Geo-KI-Werkzeuge und Thesen
**Datum:** 2026-11-03 · **Owner:** GPT Website · **Peerreview:** Claude offen · **Zyklus:** KI-2026-11-03-001  
**Projektentscheid:** neue Website-Bereiche auf bestehender GitHub Pages-Struktur aufbauen, keine alte Seite löschen, keine fremden Daten fusionieren.

## 1. Verbindliche Änderungen
| P0/P1 | Datei / Gegenstand | Commit | Effekt |
|---|---|---|---|
| P0 | `forschung/koordination/STANDARDS_SKILLS_METHODENREGISTER_V1_2026-11-03.md` | `854976f` | erweiterbare Normen-/Methoden-/Skillprofile und rollenspezifische Taskpriorisierung |
| P0 | `docs/data/projektmanagement-v1.json` | `62c7a9d` | **13 kuratierte** Taskfamilien (9 P0, 4 P1; 6 GPT, 6 Claude, 1 gemeinsam), 6 Nachweisstufen und explizite direkte Wirkungs- und Abhängigkeitskanten |
| P0 | `docs/projektmanagement.html` | `2f2bf80`, gemeinsame CSS-Korrektur `4c051fa` | neue interaktive Projektsteuerung, sechs Fortschrittsstufen, getrennte Owner-/Rangfolgen, Schlüsselwirkungs- und Forschungsfeldansicht |
| P0 | `docs/assets/projektmanagement.js` | `f1000e4` | Lesen einer datierten öffentlichen JSON-Projektion, sichere DOM-Ausgabe, Filter, gewichtete Sortierung, Impact-Überblick |
| P0 | `docs/assets/tensor-hierarchy.js` | `e9ae4c5`, `d3bba00` | vorhandene Navigationsimplementierung **nicht ersetzt**, nur neue Links unter Forschung/Projekte ergänzt |
| P0 | `docs/index.html`, `docs/projektstand.html` | `7f6c67c`, `610f0f7`, `0322a44` | Dashboard, KI-Geschichte und Thesen auffindbar; historische Projektübersicht bleibt |
| P1 | `docs/ki-geschichte.html` | `29941a2`, `08e1276` | Turing/Dartmouth, symbolische KI, Backpropagation, Transformer, Agenten vs. KI-Tensor-Forschungsansatz |
| P1 | `docs/geoki-systeme.html` | `b47f391`, `df2c4e6` | Vergleich existierender Geometriebibliotheken, GIS-Plattformen, Datenbanken und Standards |
| P0 | `docs/thesen.html` | `1a13fa4`, `3f9e333` | sechs *thematische*, nicht automatisch fachlich bewiesene Forschungsansätze mit Gegenhypothesen und zentralem Theseneinstieg |
| P0 | `docs/minimal-ki.html`, `docs/geoki.html`, `docs/tensor-paper.html` | `da1347f`, `6158d62`, `e230932` | fachliche Anknüpfungen zu KI-Geschichte/Geo-KI-Systemen/Thesen hinzugefügt, bestehender Inhalt erhalten |
| P0 | `docs/taskkarten.html` | `dbd6f71` | Claudes W07-Fund übernommen: 18 ungeprüfte Meta-Prompts nicht länger ohne Test-/Freigabebedingung als ausführbare Kopiertexte anzeigen |
| P0 | `scripts/validate_projectmanagement.py`, `.github/workflows/projektmanagement-check.yml` | `d80c0e4`, `296cd88` | JSON-Schema-/Referenz-/Stage-Prüfer, JavaScript-Syntaxprüfung via Node und statischer Website-Vorprüfungslauf definiert |
| P0 | `forschung/website/SEITENAUDIT_GESAMT_LERNWEGE_THESEN_GEOKI_2026-11-03.md` | `8cfb453` | konkrete Einzelfallbewertung **25 bekannter Seiten**, didaktische Lerntiefen, Fach-/Quellenlücken und Thesenplatzierung |
| P0 | Claude-Übergabe `GPT_UEBERGABE_STANDARDS_PM_THESEN_2026-11-03.md` | `f108de4` | Normenreview, Thesen-Originalliste, Geo-KI-Prüfung, eigene Claude-Rangliste, gegenseitige Website-Gegenprüfung |

## 2. Prüfbefunde
**Erfolgreiche statische Prüfung am tatsächlichen Git-Inhalt:**
- 13 PM-Aufgaben eindeutige IDs, 6 Stagefelder je Task, zulässige P0/P1-Priorität und bekannte direkte Abhängigkeiten; keine unbekannten ID-Referenzen.
- Vorhandene `projektmanagement.js`- und JSON-Datei im HTML verlinkt; neues Dashboard im bestehenden Projektemenü und in Start/Projektstand verlinkt.
- Alle vier neuen Fach-/Steuerungsseiten verwenden serifenlose Systemschrift und bestehende Stylesheets/Iconkonventionen.
- `ki-geschichte.html`, `geoki-systeme.html` und `thesen.html` von den betreffenden ursprünglichen Seiten aus verlinkt.
- Claude entdeckte ungeschützte Taskkarten-Prompts; die erneute Git-Prüfung zeigt die neue Bedingung `public_release==='approved' && prompt_execution_status==='passed'`.
- Geprüfte Git-Blob-SHAs nach den letzten Änderungen: `projektmanagement.html` `7f74dc4ebe44`, `projektmanagement.js` `cd3cb107cd68`, `projektmanagement-v1.json` `dfd16e30c097`, `thesen.html` `9ee03c15aaea`, `ki-geschichte.html` `74a5ef354859`, `geoki-systeme.html` `be5894806112`, `tensor-hierarchy.js` `23b3661ef99f`, `taskkarten.html` `0f1c3bcb4ff5`.

**Noch nicht geprüft:** tatsächliche GitHub-Pages-Bereitstellung (Webabruf dieses Prüfdurchgangs nicht erfolgreich), Browser-/JavaScript-Verhalten, responsives Layout, Barrierefreiheit, unabhängige E2/E3-Fachprüfung aller Seiten, CI-Workflow-Lauf und aktuelle Claude-Gegenbestätigung für diese Runde. **Ein Workflow im Git ist kein bestandener Workflow.**

## 3. Inhaltliche Trennungen
- Aufgabenbalken: pro Task **Anzahl der sechs belegten Arbeitsstufen**, nicht Anzahl bewiesener Forschungsresultate.
- Rankings: getrennte GPT-/Claude-Gewichtungen für Dringlichkeit, Architektur, Hebel, Blocker, Risiko, Bereitschaft, Aufwand; initiale Planungswerte 0–3 ausdrücklich hypothetisch. Claude soll nach echter Quellen-/Aufgabenprüfung Reihung hinterfragen.
- Thesen: `thesen.html` hat nur einen didaktischen Forschungsfragen-Einstieg; originaler Thesentext, IDs und Claim-Tests liegen bei Claude, nicht fiktiv in der Website.
- Geo-KI: Software, Algorithmen, GIS, Geodatenbank und Datensatz sind nicht gleichbedeutend und nicht automatisch „KI“.
- KI-Geschichte: Standardmethoden werden mit dem eigenen, noch zu prüfenden Forschungsprogramm verglichen; keine unbelegte allgemeine Intelligenzbehauptung.
- Zenodo: vollständige Autorenübersicht intern; eigene zitierte Werke ausschließlich relevant zur historischen Projektaussage.

## 4. Echte offene P0-Sicherheitsfrage
Claude fand insgesamt **38 Meta-Prompt-Felder** in drei öffentlich lesbaren Registern (13 + 7 + 18). GPT hat zwei UI-Freigabefilter umgesetzt, doch die Roh-JSON-Daten verbleiben öffentlich. Sie benötigen eine wirklich private No-Loss-Sicherung, Freigabeverzeichnis und einen sicheren Export. Zusätzlich war ein umfassendes Zenodo-Gesamtregister kurzzeitig in `main`, laut Claude inzwischen entfernt, **aber weiter aus der Git-Historie erreichbar**. Ein öffentliches `internal`-Flag schützt solche Inhalte nicht. Keine unautorisierte Historienneuschreibung; Nils erhält eine Entscheidungsvorlage zu Schutz/Versionierung.

## 5. Nächste Reihenfolge
1. **Claude P0:** öffentliche Daten-/Promptfreigabe und Originalthesen-/Quellenprojektion, Standards an realen Fällen, aktuelle eigene Taskprioritäten, Peerreview der neuen GPT-Seiten.
2. **GPT P0:** Browser-/Dashboard-Funktions- und Desktop-Abnahme; Nav-Mergekonflikt mit Integrationszweig ohne Inhaltsverlust lösen; Kanonisierung der Website-Lesesichten erst nach Claude-Datenfreigabe.
3. **Beide:** pro KI-Runde Tasks neu sortieren und Abhängigkeiten gegen tatsächliche Ergebnisse prüfen; gegeneinander W01–W10/D01–D10/X01 auditieren; Berichte nach jedem vollständigen Zyklus, Dreieranalysen nach 3/6/9.

**Zyklusstatus:** 001 noch nicht als vollständig gegenseitig bestätigt dokumentiert. Dieser Changelog ist keine Abschlussakte.
