# Steuerungsmatrix: Aufgaben, Verantwortung und Prompt-Reife

Stand 2026-11-03 · Teilinventar: 40 konkrete Aufgabenfamilien aus bereits vorhandenen GitHub-Objekten und dem neuen Upload. **Kein vollständiger Abgleich der letzten 100 einzelnen Nutzerprompts.**

## Grundregeln

- **Nils entscheidet** bei Forschungsrichtung, Achsen-/Begriffswahl, Publikationsfreigabe, interner/öffentlicher Trennung und Änderungen an Originalwerken.
- **Automatisierbar mit Freigabe** bedeutet: Daten zusammenführen, Formate/IDs testen, Nachweise vorbereiten. Kein Projektmodell, keine wissenschaftliche These und kein veröffentlichter Prompt wird automatisch als fachlich freigegeben bezeichnet.
- **Externe Mitarbeit** betrifft abgrenzbare, geprüfte Teilaufgaben; auch hier erst Testlauf, Quellen-/Glossarbezug und Redaktionsfreigabe.
- **Architekturwirkung/Hebelwirkung** werden mit 0–3 geschätzt; dies sind analytische Prioritätsscores, keine gemessenen Leistungen.
- **Prompt-Status** ist getrennt von wissenschaftlichem Teststatus: Es können mathematische Tests vorliegen, obwohl niemand den dazugehörigen Mitmach-Prompt ausführte.
- **Stand:** In diesem Aufgabenregister sind 7 Meta-Prompt-Entwürfe im Git-Quellbestand, 6 fachliche Prompttexte in SOULution und 27 Objekte ohne eigenen Promptentwurf erfasst. Für **keines** der 40 Objekte liegt hier eine verlinkte, vollständige Prompt-Ausführungsakte samt redaktioneller Freigabe vor; das bedeutet nicht, dass historisch niemals Prompts oder Code getestet wurden.

## Primäre Entscheidungen von Nils (redaktionell/architektonisch)

| ID | Frage zur Entscheidung | Status |
|---|---|---|
| KI-AXIS-X | Wie sollen die alten neutralen NM/ZM/UM-Achsen zu den neueren T1/T2/T3-Modellen stehen: unabhängige Modelle, Crosswalk, Bevorzugung? | **P0**, Vorschlag: getrennt erhalten, Crosswalk statt Gleichsetzen |
| KI-FELD-01 | Welche der 27 Feldakten haben Priorität für Originalquellen- und Gegenprüfung? | **P0**, Quellenprüfung vor wissenschaftlicher Freigabe |
| KI-WELT-100 | Welches Fachmodell und welche acht anfänglichen Referenzwissenschaften bekommen vollständige Primärprüfung? | **P0**, methodische Auswahl vorbereiten |
| WEB-PUBLISH-GATE | Welche Fassungen des Machtbuchs/der Bücher und Cover werden öffentlich präsentiert? | **P1**, Originale und Entwürfe getrennt |
| WEB-PAPER-01 | Welche wissenschaftliche Einführung ist redaktionell publikationsreif? | **P1**, Veröffentlichung nur nach Belegprüfung |
| KI-BIO-EVIDENCE | Welche weitreichenden numerischen Aussagen bleiben ausschließlich historischer Hypothesenbestand? | **P1**, unabhängige Nachweise fehlen |

## P0: Sofortige Schutz- und Schlüsselarbeiten

| ID | Aufgabe | Zuständigkeit | Architektur | Hebel |
|---|---|---|---:|---:|
| KI-ARCH-01 | No-Loss historische Archive und Versionscrosswalk | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-TRI-01 | Trinitäten und Tensorgrundgerüste vollständig typisieren | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-FELD-01 | 27 Feldakten und 12 Relationspositionen Originalquellenprüfung | Forschung + Nils-Abnahme | 3/3 | 3/3 |
| KI-REG-01 | Glossar mit Definitionen und Provenienz | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-REG-02 | Kanonisches Quellenregister mit Fundstellen | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-COMP-01 | Ereignis-Nachzieh-Compiler und Regressionstests integrieren | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-PROMPT-01 | 100+ Originalprompts zu Anforderungen und Freigaben abgleichen | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-WELT-100 | 100 Welten und 300 Achsen auf Primärquellen-/27er-Zulässigkeit prüfen | Forschung + Nils-Abnahme | 3/3 | 3/3 |
| KI-TEST-08 | Acht v4.4-Testserien konkret ausführen | Automatisierbar + Freigabe | 3/3 | 3/3 |
| KI-AXIS-X | Crosswalk ältere NM/ZM/UM und neuere T1/T2/T3 Achsen | Nils entscheidet | 3/3 | 3/3 |
| KI-GLOSS-1008 | 1008er Glossar mit 935 Platzhaltern und 73 Donordefinitionen sanieren | Externe Mitarbeit nach Freigabe | 3/3 | 3/3 |
| WEB-NAV-TEST | Hierarchische Navigation, Anker, responsive und Tastatur testen | Automatisierbar + Freigabe | 2/3 | 3/3 |

## P1 / P2: Anschließende Arbeitspakete
| ID | Prio | Aufgabe | Zuständigkeit | Prompt-Vorbereitung |
|---|---|---|---|---|
| GEO-M1 | P1 | Generieren – Komponieren – Prüfen – Exportieren | Automatisierbar + Freigabe | Meta-Entwurf liegt in Git |
| FMT-H01 | P1 | Offene Format- und Skillstandards harvesten | Externe Mitarbeit nach Freigabe | Meta-Entwurf liegt in Git |
| FMT-H02 | P1 | Konvertierungsgraph und Roundtrip-Proben | Externe Mitarbeit nach Freigabe | Meta-Entwurf liegt in Git |
| FMT-H03 | P2 | CAD/GIS/3D-Operatoren interoperabel testen | Externe Mitarbeit nach Freigabe | Meta-Entwurf liegt in Git |
| FMT-H04 | P2 | Wissenschaftliche Daten- und Arrayformate prüfen | Externe Mitarbeit nach Freigabe | Meta-Entwurf liegt in Git |
| FMT-H05 | P1 | API-, MCP- und Workflow-Skills harvesten | Externe Mitarbeit nach Freigabe | Meta-Entwurf liegt in Git |
| WEB-PAPER-01 | P1 | Tensor-Forschungspaper und wissenschaftliche Einführung verknüpfen | Nils entscheidet | Meta-Entwurf liegt in Git |
| FIN-OPS-01 | P1 | Bundeshaushalt / Quellenharmonisierung | Externe Mitarbeit nach Freigabe | Fach-Prompt im Quelldokument |
| FIN-OPS-02 | P2 | Wohnkosten-Sankey | Externe Mitarbeit nach Freigabe | Fach-Prompt im Quelldokument |
| DEM-OPS-01 | P2 | Demokratieportal-Vergleich | Externe Mitarbeit nach Freigabe | Fach-Prompt im Quelldokument |
| DEM-OPS-02 | P2 | öffentliche Gemeinsamkeiten / Minderheiten | Nils entscheidet | Fach-Prompt im Quelldokument |
| ROOM-OPS-01 | P2 | Situation Room | Automatisierbar + Freigabe | Fach-Prompt im Quelldokument |
| ROOM-OPS-02 | P2 | War Room | Automatisierbar + Freigabe | Fach-Prompt im Quelldokument |
| KI-REL-01 | P1 | Relationsaussagen mit Gegenproben und Evidenzstatus | Forschung + Nils-Abnahme | Prompt noch auszuarbeiten |
| KI-MATH-01 | P1 | Wissenschaftliches Formelarchiv und Parserstände | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| KI-REG-03 | P1 | Skill-/API-/Operatoren-Register zusammenführen | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| SOUL-ATLAS-01 | P1 | SOULution Lösungsatlas rekonstruieren | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| KI-MODEL-135 | P1 | Fünf Modelle mit 135 Kombinationsslots typisieren | Forschung + Nils-Abnahme | Prompt noch auszuarbeiten |
| KI-AXIS-23 | P1 | Achsenalgebra v2.3 und 20 berichtete Interaktionsläufe reproduzieren | Forschung + Nils-Abnahme | Prompt noch auszuarbeiten |
| KI-GF-12 | P1 | Zwölf Funktionsfamilien und 324 Positionshypothesen prüfen | Forschung + Nils-Abnahme | Prompt noch auszuarbeiten |
| KI-CONF-27 | P1 | Confinement-Simulation, 27 äußere Kanten und 27 Tripelaudits validieren | Forschung + Nils-Abnahme | Prompt noch auszuarbeiten |
| KI-OPS-25 | P1 | M17–M25 Operator-/Selbstbezug-/Workflowtests | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| KI-MEDIA-PROMPT | P1 | Kontextprompts am aktuellen Abschnitt mit Probelauf entwickeln | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| KI-AGENT-META | P1 | Prompt-, Agenten-, Meta-Ebene als getestete Forschungsobjekte ausbauen | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| WEB-PUBLISH-GATE | P1 | Publikationsfreigabe, Buchcover und Rechtebestand abgleichen | Nils entscheidet | Prompt noch auszuarbeiten |
| WEB-PROMPT-RETURN | P1 | Externes Prompt-Exportpaket mit Quellen-/Glossarversion und Ergebnisrückgabe | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |
| KI-BIO-EVIDENCE | P1 | Biologische Relationen und weitreichende numerische Thesen gesondert prüfen | Forschung + Nils-Abnahme | Prompt noch auszuarbeiten |
| SOUL-SYNC | P1 | SOULution-Atlas, Fähigkeiten und neun Lösungsbereiche durch stabile IDs verknüpfen | Automatisierbar + Freigabe | Prompt noch auszuarbeiten |

## Promptreife (separate vier Spuren)
Für jede Aufgabe unabhängig pflegen:
1. **Fachprompt**: frei formulierte Ausgangsfrage → strukturierter Entwurf → fachlich analysiert → Probeausführung → validiert → redaktionell freigegeben.
2. **Agentenebene**: definierte Rollen/Skills → I/O- und API-Verträge → isolierte Skilltests → Agent-Kompositionstest → Übergabeakte.
3. **Metaebene**: Ziele/Abhängigkeiten → Architektur-/Geltungsgrenzen → Prüfplan → konkurrierende Modelle → Systemabnahme.
4. **Fachliche Evidenz**: Quellnachweis / formaler Beweis / Simulationslauf / unabhängige experimentelle Prüfung jeweils separat; ein funktionierender Prompt ist kein wissenschaftlicher Beweis.

## Drei Hebelketten
- **Archiv → Quelle → Glossar → Relation → Tensor → Test:** KI-ARCH-01, KI-REG-02, KI-REG-01, KI-TRI-01, KI-FELD-01, KI-COMP-01; dadurch werden viele Folgeaufgaben überhaupt prüfbar.
- **Fachseite → Kontextfrage → Prompt/Agent/Meta → Probeausführung → Mitmachfreigabe → Rückgabe:** WEB-NAV-TEST, KI-MEDIA-PROMPT, KI-AGENT-META, WEB-PROMPT-RETURN, KI-PROMPT-01.
- **Wissenschaft → offener Operator → Skill → wiederholbarer Test → Inkubator:** KI-MATH-01, KI-TEST-08, KI-AXIS-23, KI-GF-12, GEO-M1, FMT-H01–H05.

## Test-/Publikations-Stop-Regel
Ohne verlinktes Protokoll mit Input, verwendeter Promptversion/Modell, beobachtetem Output, Fehlern, Quelle, Testdatum und fachlicher Freigabe **nicht** „getesteter öffentlicher Prompt“ schreiben. Ein Meta-Prompt zum *Entwickeln* eines weiteren Prompts ist nicht dessen Probeausführung. Ein dokumentierter wissenschaftlicher Test ist wiederum kein Prompt-End-to-End-Test.

Maschinenlesbarer Datensatz: [GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json](GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json).

## Erweiterungsbedarf
Dies ist ein belastbarer Arbeitsindex, aber noch kein 100+-Vollaudit aller Originalnutzerprompts, aller historischen Git-Branches und aller ursprünglichen Archivdateien. Weiterer Import erzeugt neue Einträge mit `origin` und ggf. `prompt_trial_id`, nicht stillschweigend geänderte frühere IDs.
