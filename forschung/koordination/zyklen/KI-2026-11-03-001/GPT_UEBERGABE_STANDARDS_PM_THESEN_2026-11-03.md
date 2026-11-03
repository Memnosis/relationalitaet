---
cycle_id: KI-2026-11-03-001
agent: gpt
document: standards_project_management_theses_handoff
status: awaiting_claude_peer_review
updated_at: 2026-11-03
---
# GPT → Claude · Standards, Taskpriorisierung, Seitenvollaudit, Thesen und Geo-KI (P0)

**Auftraggeber Nils:** Anerkannte fachliche Standards/Methoden/Skills für beide KIs operationalisieren, gegenseitig prüfen, ergänzbar und später verlustfrei verdichtbar halten. Pro Austausch-Runde Aufgaben nach getrennten GPT- und Claude-Prioritäten neu bewerten. Eigenen Projektmanagementbereich mit nachweisbaren Etappen/Feldwirkungen umsetzen. Gesamte Website auf Vorwissen/Didaktik/Thesen/Geo-KI-Werkzeugwelt prüfen.

## 1. Neue für Claude lesbare Artefakte
- [Standards-/Methoden-/Skills-Register v1](../../STANDARDS_SKILLS_METHODENREGISTER_V1_2026-11-03.md) – FAIR, PROV-O, SHACL, JSON Schema, ISO/IEC 25010:2023, WCAG 2.2, Diátaxis, NIST AI RMF, GeoJSON/OGC; eigene Skills ausdrücklich erst als **vorgeschlagene Kompetenzprofile**, nicht automatisch getestet.
- [Seitenvollaudit](../../../website/SEITENAUDIT_GESAMT_LERNWEGE_THESEN_GEOKI_2026-11-03.md) – 25 bekannte Seiten mit konkreten didaktischen Nacharbeiten, vier Lernwegen und Lage der Thesen.
- [Projektmanagementseite](../../../../docs/projektmanagement.html), [öffentliche Datenlesesicht](../../../../docs/data/projektmanagement-v1.json), [Skript](../../../../docs/assets/projektmanagement.js) – 13 Taskfamilien, 6 nachweisbare Stufen, getrennte GPT-/Claude-Rankings, direkte Abhängigkeiten und betroffene Forschungsfelder. **Nur kuratierter Projektausschnitt**, keine 100+ Originalbefehle und keine vollendeten Testleistungen behaupten.
- [KI-Geschichte](../../../../docs/ki-geschichte.html) – historische Quellen und Vergleich mit relationalem Mini-KI-Programm.
- [Geo-KI-Systeme](../../../../docs/geoki-systeme.html) – Bibliotheken/GIS/Datenbanken/Standards mit Vor- und Grenzen.
- [Thesen-Einstieg](../../../../docs/thesen.html) – thematische Forschungsrichtungen, keine neu erfundenen originalen kanonischen These-IDs.

Die verantwortliche Website-KI hat diese Arbeiten in `docs/` angelegt. Claude bleibt für Quellen, fachliche Datensätze, Thesen-Originalregister, Skill-Tests und freigegebene Datenprojektion zuständig; bitte **nicht** die Website-Dateien überschreiben.

## 2. Konkrete Claude-P0-Aufträge
**C-P0-01 · Normenprofil prüfen:** Prüfe anhand der offiziellen Primärreferenzen, ob die ausgewählten Standards fachlich korrekt und angemessen beschrieben sind. Ergänze nur mit genauem Geltungsbereich, Status (Standard/Framework/Best Practice), Originalquelle, Lizenz und einem möglichen Testszenario. Mindestens FAIR/PROV-O/SHACL/JSON Schema plus Diátaxis/WCAG-Grenzen prüfen; aus einem ISO-Titel keine Zertifizierung ableiten.

**C-P0-02 · Register und Reviewer-Skills:** Entwerfe/prüfe Quellen-/Claim-/These-/Operatoren-Schema mit Referenz-IDs, Geltung, Evidenz, Version, status, Test, Autor/Prüfer, `impact_domains`, `depends_on`, `enables`, `public_release`. Teste an fünf realen anonymisierten Records, einschließlich mindestens zwei Invalid-Fällen. Entwickelte Prompts/Agenten-/Metaaufgaben separat versionieren, tatsächlich ausführen und beurteilen.

**C-P0-03 · Theseninventar:** Finde die **Originalthesen** in vorhandenen Beständen, bewahre Originalwortlaut/Versionen und gleiche sie mit den sechs thematischen Einstiegen auf `docs/thesen.html` ab; markiere Über-/Unterdeckung, alternative Interpretationen und Nichtzuordnungen. Keine willkürlichen IDs in den historischen Bestand schreiben. Liefere geprüften öffentlichen Thesenexport nur nach Nils-Freigabe.

**C-P0-04 · Geo-KI Review:** Für SymPy, GEOS/Shapely, CGAL, Open CASCADE, QGIS/PostGIS, OSM, Natural Earth, GeoJSON/GeoSPARQL jeweils Nutzung, Lizenz (inkl. Daten-/Tile-Lizenz), I/O, Operatorfamilie und Regressionsempfehlung. Vergleiche **nicht** Kartendatenbank, GIS-Frontend und symbolischen Rechner als identischen Algorithmustyp. Schlage 2–3 ausführbare Skills mit Fairness-/Negativfällen vor.

**C-P0-05 · Dynamische Taskpriorisierung:** Für deine DATA-Aufgaben priorisiere *Provenienz-/Sicherheitsrisiko*, *wissenschaftliche Geltung*, *Schema/Versionierung*, *Abhängigkeiten*, *Machbarkeit*, *Quellenzugang*, *Nutzen*. Vergleiche mit GPT-Websitegewichtung, markiere Abweichungen und welche Aufgabe systemweit neue Funktionen freischaltet. Keine ungemessene Wirksamkeitsbehauptung als Beweis deklarieren. Übergib verlässlich versionierte **öffentliche Projektionen** statt private Ursprungsdatensätze.

**C-P0-06 · Peer-Review der Website:** Prüfe `docs/projektmanagement.html`, `docs/thesen.html`, `docs/geoki-systeme.html`, `docs/ki-geschichte.html`, Start-/Projekt-Navigation und die neue Taskkarten-Freigaberegel gegen W01–W10 und X01, mit **konkreten Git-SHAs**, Positiv-/Negativbefund, Didaktikfragen und Schnittstellenkriterien. Browser-Tests als `not_assessed` markieren, wenn nicht durchgeführt.

## 3. Pflicht zur erneuten Taskanalyse pro Runde
Erstelle `forschung/koordination/zyklen/KI-2026-11-03-001/CLAUDE_TASK_PRIORITAETEN_01.md` mit:
- vorheriger/nächster Aufgabenrang je Claude und begründeter Änderung,
- erledigt/teilweise/offen anhand Datei/Test/Commit und fehlenden Geltungs-/Abnahmebedingungen,
- mindestens drei **nachgewiesenen** Abhängigkeiten zu GPT-Aufgaben,
- Blocker, Inputbedarf, Teamgrenzen, alternative Reihenfolge und maximal mögliche Hebelwirkung,
- neue Standards/Skills als `candidate` bis zur Testakte und Gegenprüfung.
Bei jedem späteren Zyklus denselben Bericht als neue Version, alte Version nicht überschreiben. Nach 3 vollen Zyklen verdichten: Dubletten, nützliche Prüfmethoden, wirkungslose Prozesse und neue Normprofile mit Crosswalk, nicht Originale verlieren.

## 4. Bereits von Claude entdeckte Sicherheitsfragen
`CLAUDE_REVIEW_WEBSITE.md` fand **18 weitere nicht freigegebene Meta-Prompt-Karten** auf `docs/taskkarten.html`. GPT hat den UI-Gate mit Commit `dbd6f71c07c877807e40a4268b7a4b41520b9491` ergänzt; die vollständigen Rohprompt-Datensätze stehen in öffentlichen JSON-Archiven und bleiben deswegen **nicht** privat. Diese Lücke darf nicht allein als UI-Erfolg geschlossen werden. Bitte 38 Rohpromptobjekte (13 + 7 + 18) verlustfrei privat sichern, Originale versionieren, öffentliches Minimalexportformat und Veröffentlichungsentscheidung vorlegen.

Die von Claude bereits gemeldete vorübergehende Zenodo-Gesamtliste wurde laut seiner Diskussionsantwort aus `main` entfernt, bleibt aber in Git-Historie zugänglich. Der ursprüngliche Nutzerwunsch lautet **interne Gesamtübersicht**. Claude soll die Release-/Historienrisiken Nils transparent als Entscheidungsakte vorlegen, ohne eigenmächtigen Force-Push oder unautorisierte Historienneuschreibung.

## 5. Abnahme und Austausch
Claude dokumentiert seine Gegenprüfung in `CLAUDE_REVIEW_STANDARDS_PM_THESEN_01.md` und die Rangliste in `CLAUDE_TASK_PRIORITAETEN_01.md`, committet sie im Zyklusordner, und bestätigt im gemeinsamen GitHub-Issue #3. GPT liest die tatsächlichen Dateien, antwortet mit geprüften Änderungen und nur nach reziproker Bestätigung folgt `ZYKLUSBERICHT.md`. Ein schon vorhandenes eigenständiges Website-Review wird berücksichtigt und nicht künstlich erneut als volle Runde gezählt.

**Zyklus-Status bei dieser Übergabe:** Claude hat Datenarbeitsstand und unabhängigen Website-Review geliefert, aber das zentrale `STATUS.json` führt weiterhin keinen vollständig gegenseitig bestätigten Abschluss. Bericht nach jedem vollständigen Zyklus; Analysen nach 3/6/9, ggf. 12.

**An Nils:** Konflikte nur als verständliche Entscheidung mit Alternativen, Folgewirkungen und bevorzugter Option; redaktionelle und Quellfreigaben bleiben bei ihm.
