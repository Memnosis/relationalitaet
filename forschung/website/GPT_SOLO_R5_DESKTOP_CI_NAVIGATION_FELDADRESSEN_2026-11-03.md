# GPT-Solo R5 · Desktop-CI, 33-Seiten-Regressionsschutz und Tensor-Feldadressen

**Stand:** 2026-11-03 · **Rolle:** GPT Website · **Claude:** während der angekündigten Pause nicht beteiligt · **Status:** neue Git-Artefakte und konkrete Fehlerkorrekturen committet. **Kein abgeschlossener gegenseitiger KI-Zyklus.**

## A. Neue tatsächlich umgesetzte Änderungen

| ID | Teilauftrag | Datei / Commit | Resultat und Grenze |
|---|---|---|---|
| W-R5-01 | Echter Desktop-Browsertest statt alleiniger Syntax-/Linkprüfung | `scripts/verify_website_browser.mjs` · `348af38` | Playwright-Chromium-Tests für Startseite, 7-Gruppen-Menü, PM-Filter, 82/102-Promptanzeige, sechs Thesenkarten und elf Fachseiten – **Ausführung in GitHub Actions noch nicht als bestanden nachgewiesen** |
| W-R5-02 | Automatische Ausführung im Browser | `.github/workflows/website-browser-smoke.yml` · `a12063a` | Github Action startet lokalen HTTP-Server aus `docs/`, installiert Chromium und prüft Browserinteraktionen. Browser-Lauf-/Statuslog offen |
| W-R5-03 | Missverständliche Prompt-Statistik korrigieren | `docs/assets/workflow-stand.js` · `4a80cd3` | Gruppenwerte als **eindeutige IDs** bezeichnet: acht Gruppen summieren 82, 102 ist die Zahl der Vorkommen einschließlich 20 Überlappungen |
| W-R5-04 | Aufgabenfortschritt von Freigabe trennen | `docs/assets/projektmanagement.js` · `4018c38`, `docs/projektmanagement.html` · `86c31c3` | Sechs dokumentierte Bearbeitungsstufen nicht mehr als unabhängige Test- oder Publikationsfreigabe beschriftet |
| W-R5-05 | Geo-KI-Feldadressen 1-basiert darstellen | `docs/geoki.html` · `ba72a10`, `04a3962` | Auswahlcode und Starttext von fälschlichem `T0.E0.R0` zu `T1.E1.R1`; Browser-Test auf genau 27 Felder und korrekte erste Adresse ergänzt (`a47757a`) |
| W-R5-06 | Öffentliche redaktionelle Metaanweisung korrigieren | `docs/geoki.html` · `04a3962` | Nichtleserbezogenen Hinweis auf Chat-Bilder entfernt; stattdessen fachliche Grenze zwischen Struktur und validierten Feldrelationen erläutert |
| W-R5-07 | Bestehende Strukturzeichnung bewahren | `docs/assets/media/tensor_27_structure_only.svg` · `e1a2a4a`, `docs/tensor-einfuehrung.html` · `3a2469c` | Aus Integrationszweig stammende **bereits existierende** Grafik mit 27 beschrifteten Positionen als aufklappbare Ergänzung eingebunden. Keine neuen mathematischen oder physikalischen Beziehungen behauptet |

## B. Tatsächliche Prüfungen dieser Runde
- GitHub `compare_commits(main, integration/soulution-shared-core-2026-11-03)` zeigt weiterhin **160 Commits voraus / 250 dahinter** (wechselnder Git-Stand); unveränderte/überholte Zweigseiten dürfen nicht blind über die entwickelten `main`-Seiten gelegt werden.
- GitHub Pages `projektmanagement.html` und `ki-systeme.html`: externer Webabruf fehlgeschlagen. Containerzugriff auf `raw.githubusercontent.com`: DNS-Auflösung fehlgeschlagen. **Kein Live-Deployment nachgewiesen.**
- Alle 33 auditierten Hauptseiten wurden in drei separaten Git-HTML-Batches auf Dokumentvorkommen, lokale Linkziele und Navigationsskript geprüft: **keine fehlende `tensor-hierarchy.js`-Einbindung, keine duplizierten statischen HTML-ID-Attribute gefunden**. Diese Prüfungen sind eine Git-Dateiprüfung, nicht das Rendern.
- Öffentliche JS- und JSON-Dateien `projektmanagement.js`, `workflow-stand.js`, `anforderungsabdeckung.js` und weitere wurden zuvor syntaktisch geprüft; in dieser Runde ist **kein vollständiger Browserlauf lokal ausgeführt**.
- Die zuvor überprüften 72/72 Git-Nachweisdateien sind weiter ein **Dateiexistenz-Befund**, keine 72 erledigten Originalnutzeraufträge.

## C. Rest-Diff: bewusst nicht alles aus dem alten Zweig übernommen
- Die acht sicheren HTML-Unterseiten, zwei Quellen-/Codebuchdatenregister und die übernommenen wissenschaftlichen Brücken sind in `main`; die gesamte Zweignavigation und die 47er-Bibliothek mit Roh-Metaprompts **nicht**.
- Zwei zusätzliche SVG-Bestände wurden geprüft: `tensor_27_structure_only.svg` kann mit korrektem Struktur-/Evidenzhinweis verwendet werden; `geoki_rotation_verified.svg` wird **nicht** ohne Original-Testakte als vermeintlich verifizierte Resultatgrafik übernommen.
- Offene Unterschiede in `docs/bibliothek.html`, `docs/mitmachen.html`, `docs/projektstand.html`, `docs/glossar.html` und anderen Seiten sind vielfach neuere `main`-Entwicklungen. **Kein Full-Branch-Merge ohne Diff-/Regressionsnachweise**.

## D. Weitere Priorität während Solo-Phase
1. **W-P0-01:** ersten echten Chromium-Run in GitHub Actions anhand Resultat/Joblog bestätigen oder erkannte Laufzeitfehler beheben. Der Workflowcode alleine ist nicht `test_passed`.
2. **W-P0-02:** Cross-Page-Anker und dynamisch erzeugte IDs nach Browserergebnis abgleichen, alle 33 Seiten technisch abnehmen.
3. **W-P0-03:** unveränderte Originalprompts der exakt letzten 100 chronologischen Nachrichten, falls als verifizierte Quelle verfügbar, mit den 72 Atomaufträgen many-to-many verknüpfen. **Nicht aus 72 eine fingierte 100er-Liste ableiten**.
4. **W-P0-04:** Mitmach-Bedienwege ohne Git-Schreibrecht inkl. Ergebnisrückgabe testen; Rohpromptfreigabe/privates Archiv bleibt getrennt.
5. **W-P1-01:** noch fehlende Leserverbindungen aus Integrationszweig in geprüfte Fachseiten nachziehen, Quellen-/Claim-Karten nach Claude-Freigabe.

## E. Spätere gegenseitige Abnahme
Claude soll nach eigener Verfügbarkeit **nicht** 33 Seiten blind als wissenschaftlich geprüft bestätigen; fachliche Stichproben/Fundstellen und Exportdaten sind separat zu prüfen. GPT übernimmt Browser-/Navigations- und redaktionellen Eigentest, Claude die Daten-/Claims-Eigenprüfung. Danach wird jede Seite beziehungsweise jedes Testmodul anhand des tatsächlichen Source-SHA wechselseitig abgenommen.

**Ergebnis R5:** Echte zwei zusätzliche Browser-Testartefakte und mehrere konkrete Website-Korrekturen existieren. **Browser-Teststatus, vollständige 100er-Originalprompt-Herkunft und Zyklusabschluss bleiben offen.**
