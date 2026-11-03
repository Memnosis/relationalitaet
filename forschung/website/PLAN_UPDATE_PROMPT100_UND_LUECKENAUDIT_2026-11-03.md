# Upgrade- und Verlustprüfung: letzte 100+ Prompts, Seitenpläne und offene Jobs
**Stand:** 2026-11-03 · **Autor:** GPT (Website/Koordination) · **Gegenprüfung Claude:** angefordert.  
**Wichtige Gültigkeitsgrenze:** Der vollständige exportierte Wortlaut der **letzten genau 100 einzelnen Nutzer-Nachrichten** liegt hier nicht als durchgehendes durchnummeriertes Original vor. Die historische Bezeichnung „100+“ und 44 bereits gruppierte Aufgabenfamilien sind nicht gleich 100 nachgewiesene Originalprompts. **Es wird kein fiktiver 100er-Fertigstellungsgrad angegeben.**

## 1. Was als Originalprompt-Kette nachgewiesen werden muss
Jeder einzelne Originalauftrag erhält `USER-PROMPT-<Datum>-<Index>`, **exakten** Wortlaut/Quellanker (ohne publikationsfremde interne Details), Unteraufträge (atomar), betroffene Projekte, Owner GPT/Claude/Nils, altes Plan-ID, implementiertes Git-Artefakt, Testausgang, Abschlussbestätigung, neuere Korrektur/Ersetzung und jeweilige nächste Folgemaßnahme. Gleiche Inhalte aus verschiedenen Nachrichten bleiben als **unterschiedliche Aufträge** nachvollziehbar. Ohne abrufbaren Originaltext: `source_unavailable`, nicht als erledigt ausgeben. Die vollständige Liste mit 100 Originalnachrichten erfordert einen aktuellen verifizierbaren Chat-/Projekt-Export.

### Sichtbare Belegstellen und Zuordnung – Ausschnitte, NICHT eine erfundene 100er-Liste
| Referenz / Nutzerforderung (sinngemäßer Ausschnitt) | Zuordnung | Status beim Audit |
|---|---|---|
| No-Loss-Gesamtdatenbestände und historischer Crosswalk; erst danach Tensorisierung priorisieren | Claude Masterdaten, Source-ID, 27er-Feldakte | Teilweise / alte Archive vorhanden, Fusion und fachliche Abnahme offen |
| Letzte 100 Befehle auf Website-Aufgaben prüfen und nachhalten | originalgetreues Promptinventar | **Nicht erledigt:** 44 Familien nicht mit 100 unveränderten Einzelprompts gleichsetzen |
| Website zentral weiterentwickeln, Claude übernimmt Datenbestände | Owner-Trennung | eingeführt, teilweise gegengeprüft |
| Nach drei vollen Zyklen Analyse, nach drei Analysen Entscheidung, eventuell bis zwölf | KI-Koordination | Regeln/Automation vorhanden; Zyklus 001 nicht formell abgeschlossen |
| Beide KIs prüfen wissenschaftliche und didaktische Arbeit der anderen | W/D/X-Review | unabhängiges Claude-Review vorhanden; nicht alle aktuellen Seiten gegengeprüft |
| Quellen: digital verifiziert, nicht erreichbar, Handprüfung, nur Nils geprüft | Quellenmodell | Vertrag vorbereitet, systematisch getestete Web-Lesesicht fehlt |
| Zenodo-Gesamtübersicht zunächst intern; nur fachlich relevante Werke öffentlich | internes Masterregister vs. selektive Quellen | fehlerhaft einmal auf main veröffentlicht, danach entfernt; Git-Historie bleibt erreichbar |
| Text so lang wie für Verständnis/Vertiefung nötig, ohne Serifenschriften; PDF/DOCX-Regeln | Design-/Publikationsstandard | Regelwerk und einzelne Lernmodule vorhanden, Buch-Exportabnahme fehlt |
| Öffentliche vs. interne Prompts und Prompt-/Agent-/Metaebenen unterscheiden | Freigabe und Trial | UI-Gates vorhanden; 38 Rohprompts weiterhin Git-öffentlich, Freigabeakten offen |
| „Logik-Tensor 2.0“ als didaktisch saubere Publikation aus Tensor Basics/Logik/Feldtheorie | wissenschaftliches Manuskript | Arbeitsmanuskript/Dossiers vorhanden; Quellextrakt/Autorfreigabe zur neuen Buchausgabe offen |
| Geo-KI: bestehende Bibliotheken, Datenbanken, Wissenschaftssysteme und Vorteile analysieren | Geo-KI-Werkzeuglandkarte | neue Website-Seite implementiert, aktueller Versions-/Benchmarktest offen |
| Geschichte der KI, andere Architekturen, was eigener Ansatz zusätzlich leisten könnte | KI-Geschichte | neue Seite implementiert, Fachexperten-/Lesertest offen |
| Thesen mit Evidenzgraden als Karten/Icons passend zum Fachthema | Thesenatlas und Kontextkarten | sechs thematische Karten mit **vorläufigen** E0–E4-Stufen implementiert; originale Thesen-/Beweisakten fehlen |
| Eigenes Projektmanagement, Fortschrittsbalken je Schritt und Feldwirkungen | PM-Dashboard | 13 kuratierte Aufgaben, sechs Stufen und Abhängigkeiten; End-to-End/Browser und vollständiges Inventar fehlen |
| Für jede Seite eigene Analyse plus Umsetzungsplan auf Git | 25 seitenbezogene Auditakten | 25 Git-Planakten erstellt; Claudes Peerreview und Ausführung der Folgepakete offen |
| GPT verifiziert Website, Claude verifiziert Daten eigenständig; danach Cross-Review | owner_review_policy | im PM-Datenschema ergänzt, tatsächliche neue Review- und Endabnahme noch offen |

## 2. Ist wirklich etwas verloren gegangen?
**Kein nachgewiesener irreparabler Verlust** dieser neuen Git-Website-Bereiche: sie sind als Dateien in Git `main` vorhanden und ihre wesentlichen Originalinhalte wurden bei den Änderungen additiv erhalten. **Aber** eine nicht verfügbare Originalprompt-Folge ist ein **Nachweislückenrisiko**, nicht Beweis für Vollständigkeit. Ein offener Plan ohne umgesetzten Code gilt als „nicht umgesetzt“, ein einzelnes UI-Modul ohne Test als „teilweise umgesetzt“.

### Verifizierbar unvollständige / riskante Jobs
| ID | Befund | Einstufung | Wer / nächste echte Abnahme |
|---|---|---|---|
| GAP-001 | Die letzten genau 100 Originalbefehle sind nicht als einzelne unveränderte Dateien + Task-/Commit-Crosswalk nachgewiesen | **P0 · Inventar-/Auditlücke** | GPT erstellt Originalpromptregister aus verfügbarer Quellfolge; Claude prüft Daten-/Taskzuordnungen; keine erfundenen 100 Positionen |
| GAP-002 | Alte 106 Aufgaben, 44 Familien und aktuelles 13er-Dashboard besitzen keinen vollständigen, versionsübergreifenden deduplizierten Crosswalk | **P0 · Teilintegration** | beide Owner trennen Schnappschüsse/Aufgabentypen, nachvollziehbare ID-Migration, Regression |
| GAP-003 | Neuer PM-JavaScript-Browserlauf, GitHub-Pages-Deployment und End-to-End-Tests nicht nachgewiesen | **P0 · Implementiert, nicht abgenommen** | GPT selbst Browser-/JS-/Link-/Tastaturtest, Claude prüft Datenexport |
| GAP-004 | Quellen-/Claim-/Thesenregister noch nicht als voll referenzierte freigegebene Web-Ansicht | **P0 · Wissenschaftsdaten fehlen** | Claude originale Quellen/Fundstellen/Claims/Evidenz-/Prüfstatus; GPT Leserkarte |
| GAP-005 | Öffentliches Git enthält weiterhin 38 Roh-Meta-Prompts; bloßes Ausblenden in HTML macht sie nicht intern | **P0 · Sicherheits-/Freigabelücke** | Claude private Sicherung, öffentliche Projektion und separate Freigabe; Nils entscheidet |
| GAP-006 | Zenodo-Gesamtregister war laut Claude kurz auf `main`; aus aktueller Ansicht entfernt, historisch noch erreichbar | **P0 · Publikationshistorie** | Claude dokumentiert betroffene Historie, keine eigenmächtige Umschreibung; Nils entscheidet Freigabe/Schutz |
| GAP-007 | Logik-Tensor 2.0/2.1 fachlich nicht fertig quellen- und testvalidiert, Publikations-DOCX/PDF noch nicht freigegeben | **P0/P1 · Manuskript unfertig** | Claude Fach-/Datenprüfung, GPT Text/PDF/DOCX, Nils Freigabe |
| GAP-008 | Zwei Navigationssysteme samt betroffenen Seiten noch nicht verlustfrei zusammengeführt | **P0 · Technische Zusammenführung** | Nils hat laut Entscheidungsakte 7-Punkte-Menü **b** beschlossen; GPT prüft Diff/16 Konfliktseiten/4 Schutzanker und integriert erst nach Regression |
| GAP-009 | Zwei Inkubatoransätze sollen nach neuester Autorenentscheidung **fusioniert und differenziert** werden; keine vollständige Git-Integration nachgewiesen | **P1 · Teilumsetzung** | GPT Originalinhalte/URLs/Scope vergleichen; Claude Tools/Skills füllen |
| GAP-010 | Thesenübersicht umfasst bisher sechs **thematische** Familien, nicht die echten historischen Originalthesen und geprüften Grade | **P0 · Fachlicher Crosswalk offen** | Claude Original-IDs/Versionen/Quellen/Gegenbeweise, GPT kontextuelle Karten |
| GAP-011 | Geo-KI- und KI-Geschichte-Seiten haben Quellenlinks, aber keine vollständig gleichwertigen Benchmark-/Didaktik-Reviews | **P1 · Fachseite umgesetzt, Abnahme offen** | GPT Webtests/Didaktik, Claude Version/Lizenz/Fachtest |
| GAP-012 | Öffentliche Mitmachangebote haben noch keinen belegten End-to-End-Rückgabeweg ohne Git-Schreibrecht und keinen vollständig freigegebenen Prompt-Probelauf | **P0/P1 · Teilfunktion** | Claude Prompttrial/Public-Export, GPT Nutzerpfad |
| GAP-013 | Automatische Nachziehkompilierung von Änderungen auf Quellen, Glossar, Thesen, Test, Publikation, Webregister nicht als echte Git-CI-Gesamtkette abgenommen | **P0 · Architekturwirkung** | Claude Daten-Compiler, GPT UI-Datenanbindung, gemeinsame Testakte |
| GAP-014 | Logik „100 Begriffe“ aus Original-1.0: Claudes Extrakt meldet 34 sichtbare Begriffe (27+7); eine vollständige 100er-Tabelle nicht nachgewiesen | **P1 · Original-/Titeldifferenz** | Claude originalgetreue Prüfung, Autorentscheidung für neue Formulierung |
| GAP-015 | Die bestehende Website-Planakte nennt noch „Serifenelemente“, obwohl Nils später ausdrücklich **keine Serifenschriften** verlangte | **P1 · überholte Planregel** | GPT alte Planversion erhalten, durch neueres Designstandard v1 verbindlich übersteuern; in nächster konsolidierter Planfassung klar markieren |
| GAP-016 | Gemeinsamer KI-Zyklus 001 enthält mehrere Zwischenberichte, aber Statusdatei zeigt weiterhin `claude_delivered=false`, `gpt_reviewed=false`, `claude_acknowledged_review=false`, `cycle_report_created=false` | **P0 · offener Abschluss** | jeder Owner prüft seine Lieferung selbst, gegenseitige Abnahme und finaler Bericht nach echtem Vollzyklus |

## 3. Entwicklung der Pläne – alter → neuer Stand
| Programm | Ursprüngliche Absicht | Nachweisbar umgesetzt | Was im Plan zu ändern ist |
|---|---|---|---|
| 100+-Website-Upgrade | vollständiges Originalprompt-/Anforderungsregister | 44 historische Familien, mehrere Audit-/Planberichte | **P0 bleibt offen:** Nummerierung der Originalnachrichten, keine scheinbar abgeschlossene 100er-Liste |
| Website-Bündel 02 | sieben gestaffelte Fachseitenaufgaben | Lernmodule, Logik-/Algebra-Seiten, Quellenweg, neues PM und Thesen | auf neue Seiten ausweiten, fachliche Daten-/Browser-/Freigabeabnahme explizit als fehlende Stufen führen |
| Design-/Textstandard | serifenlos, E1/E2/E3 und Prompt/Agent/Meta | Layout und Lernmodule | ältere widersprechende Serifvorgabe als ersetzt dokumentieren |
| Hauptnavigation | zwei verschiedene Skripte/Integrationszweig | 7er-Menü auf main, neue Links vorhanden | **Entscheidung b dokumentiert**, technischer Konflikt/Originalerhalt noch offen, keine neue Nils-Menüfrage |
| Inkubator | neue Inkubator-/Skillfamilien | zwei entwickelte Konzepte, eine öffentliche Hauptseite | Autorenwunsch „fusionieren und differenzieren“ ist Entscheidung, noch nicht vollständig ausgeführt |
| Quellen und Thesen | kontrollierte, quellennahe Nachweisregister | DOI-Referenzset, sechs thematische Thesenkarten mit vorläufigem E1 | tatsächliche Originalthesen-/Claimprüfung und Evidenzgrade abwarten; keine E3/E4 erfinden |
| Projektmanagement | nach jedem Arbeitsfortschritt Sichtbarkeit | neues Dashboard mit sechs Stufen und KI-Rankings | separate GPT-/Claude-Eigenprüfung + Cross-Review, Taskverlauf, historische Vollabdeckung und echter Endtest |
| Buch- und Machtbuchprojekte | Manuskripte, Cover, Web-Verweise, Promptentwicklung | Entwürfe/Links/Aufträge dokumentiert | unfertige Bücher weiterhin **nicht** als freigegebene PDF-Bücher ausgeben; Cover erhalten, fachliche Prompt- und redaktionelle Gates abwarten |

## 4. Nächste verbindliche Reihenfolge
**GPT P0:** 1) Alle 25 Seiten-Auditakten verlinken, Querverweis/Thesenkarten testen; 2) PM-Frontend+Stagequellen mit realem Browser-/CI-Bericht abnehmen; 3) bestätigte 7er-Navigation verlustfrei mit Integrationszweig verbinden und publizieren; 4) Aufgaben-/Upgradeplan-Synchronisation vorbereiten.  
**Claude P0:** 1) 38 öffentliche Prompt-Originale privat sichern + Auswahlexport; 2) historische Originalthesen/Claims/Quellen mit Belegstatus und korrekten IDs; 3) 106/44/13- und 100+-Crosswalk mit Originalbelegen; 4) Forschungsdaten-/Standards-/Testprüfung, eigens signiert.  
**Gemeinsam:** Je KI zuerst die **eigenen** gelieferten Aufgaben gegen Quelldatei/Test/Commit nachweisen, anschließend die andere Seite gegentesten. Keine Aufgabe wird ausschließlich aus Berichtsentwurf als beendet markiert. Nach jedem vollen Austauschzyklus Ergebnisbericht; Analysen bei 3, 6, 9 und Autorenentscheidung zu optional bis 12.

## 5. Nachzugartefakte
- [Die 25 individuellen Seitenakten](seiten/README.md).
- [Gesamtseiten-Audit](SEITENAUDIT_GESAMT_LERNWEGE_THESEN_GEOKI_2026-11-03.md).
- [Quellen-/Standards-/Skillmethoden](../koordination/STANDARDS_SKILLS_METHODENREGISTER_V1_2026-11-03.md).
- [Zwei-KI-Kommunikation](https://github.com/Memnosis/relationalitaet/issues/3).
- [Web-Datenregister](../../docs/data/projektmanagement-v1.json).
- [Thematische Thesendaten](../../docs/data/thesen-uebersicht-v1.json).

**Wesentliche Schlussfolgerung:** Nachweisbar viele Schritte **halb umgesetzt oder noch nicht verifiziert**, aber aus der hier verfügbaren Quellenbasis **kein nachgewiesener endgültiger Verlust von Git-Aufträgen**. Die lückenlose Gegenprobe zu genau 100 Originalnachrichten bleibt offen.

## 6. Zwischenstand GPT-Solo-Runde während Claudes Pause · 03.11.2026

**Arbeitsmodus:** Während Claude nicht verfügbar ist, bearbeitet GPT ausschließlich eigene Website-/Plan- und statische Integrationstests. Keine Claude-Datenarchive verändert, keine gegenseitige KI-Prüfung oder abgeschlossener Zyklus behauptet.

### 6.1 Website-Umbau – jetzt tatsächlich in `main`
Aus `integration/soulution-shared-core-2026-11-03` wurden acht **zuvor nicht in main vorhandene** HTML-Fachseiten unter originaler URL selektiv übernommen:
- `docs/ki-systeme.html` – historischer KI-Systemvergleich.
- `docs/ki-kernforschung.html` – Skills, KI-Kernfunktionen und weiterführende Forschungsfragen.
- `docs/codebuch.html` – kompakter Codebuch-Webindex.
- `docs/soulution-schroedingers-inkubator.html` – digital-souveräne Softwareentwicklung.
- `docs/soulution-inkubator-quellen.html` – Werkzeug-/Quellenatlas.
- `docs/soulution-ki-kreativrechte.html` – KI und kreative Rechte.
- `docs/soulution-weltwissen-dividende.html` – Weltwissen und KI-Dividende.
- `docs/wissen-macht-wirklichkeit.html` – gesellschaftliche Forschungs- und Publikationsbezüge.

Mit übernommen wurden die benötigten bereinigten Daten `docs/data/codebuch-web-index.json` (12 Glossar-/Objektknoten) und `docs/data/inkubator-quellenregister.json` (38 Werkzeug-/Quellenkandidaten). Auf allen importierten HTML-Seiten wurde **ausschließlich die Zweig-Navigation `site-nav.js` durch die von Nils entschiedene 7-Gruppen-Navigation `tensor-hierarchy.js` ersetzt**. Die alte Zweigfassung bleibt als Vergleichsquelle erhalten.

Das Hauptmenü `docs/assets/tensor-hierarchy.js` führt diese Seiten unter den passenden bestehenden sieben Gruppen; es wurde **nicht durch das konkurrierende `site-nav.js` ersetzt**. Die Startseite enthält einen neuen vertiefenden Lernwegblock. `docs/inkubator.html` differenziert Forschungsinkubator und Schrödingers Inkubator, ohne die beiden vorhandenen Ansätze zu vermischen.

**Gezielt nicht importiert:** `docs/promptbibliothek.html` / `docs/data/promptbibliothek-v1.json` mit noch nicht vollständig freigegebenen ausführbaren Prompttexten. Ein Verweis auf diese noch nicht zugängliche Seite wurde auf zwei bereits integrierten Fachseiten korrigiert: öffentlich wird stattdessen der aggregierte Prüfstand gezeigt.

### 6.2 Einzel-Audits und Originalauftragsabdeckung
- Frühere 25 individuelle Website-Auditakten plus 8 neue aus dem Integrationszweig = **33 dokumentierte Auditpläne**; Index `forschung/website/seiten/README.md` nachgezogen.
- `forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json` hält **72 atomisierte, in vorhandenen Plänen und bisher sichtbaren Nutzeranweisungen begründete Anforderungen** in 9 Domänen fest, jeweils mit Status, Owner und existierendem Projektartefakt.
- **Diese 72 Anforderungen sind weder 72 wörtliche Originalprompts noch ein vollständiger Nachweis der letzten 100 Nachrichten.** Für echte chronologische 100er-Originalprüfung bleibt die tatsächliche Chat-/Projekt-Exportliste mit Zeitstempel/Message-ID notwendig. Das Register markiert `verified_exact_100_message_sequence=false` und keine `original_text_verified`-Bestätigung. Es enthält keine unbearbeiteten Nutzer-Rohprompts.
- Aus 72 Aufgaben lässt sich daher **keine exakte Erledigtquote der letzten 100 Nachrichten** berechnen. Insbesondere erfüllen 33 Audits nicht automatisch 33 Userprompts.

### 6.3 Statische Qualitätssicherung
- Vorhandene neue Links und Assets anhand des aktuellen Git-Hauptzweigs stichprobenartig überprüft; neue Abhängigkeiten Codebuch/Quellenatlas geladen.
- `scripts/validate_site_integration.py` prüft künftig Originaldateien, Navigation, lokale Links, JSON und 72er-Quellenledger. `.github/workflows/site-integration-review.yml` wurde ergänzt.
- **Ein erfolgreicher CI-Lauf, ein vollständiger Browser-/Tastatur-/Screenreader-Test und ein extern verifizierter Pages-Abruf sind weiter offen.** Der direkte öffentliche Pages-Abruf in dieser Runde konnte technisch nicht bestätigt werden.

### 6.4 Gegenüber dem alten Plan neu gewichtete P0-Folge
1. **P0 / GPT:** Link-/Anchor-/Desktop-Regression der acht neu importierten Seiten und bestehenden sieben Gruppen, insbesondere Codebuch/Quellenatlas-JSON.
2. **P0 / GPT:** R6-öffentliche Aufgabenlesesicht 7 Web-/gemeinsame Karten und 6 aggregierte Claude-Datenaufgaben beibehalten; keine privaten Prompts oder vollständigen privaten Aufträge anzeigen.
3. **P0 / GPT:** echte Zuordnung der letzten 100 Originalanweisungen auf vorhandene 72 Atom-Aufträge erst bei vollständiger Originalnachrichten-Quellfolge; lückenlose Verlust-/Offenliste führen.
4. **P0 / GPT + später Claude:** Integrationszweig-Diff der verbleibenden **geänderten** Seiten gegen die aktuellen Git-Seiten; Zweigvarianten nicht blind ersetzen. Öffentliche Claims vor Veröffentlichung fachlich gegenprüfen.
5. **P1 / GPT:** Buch-/Cover-/Quellenwege auf den neuen SOULution-Unterseiten auditieren, ohne Originalveröffentlichungen umzuschreiben.
6. **P1 / GPT + später Claude:** echte Tests und Quellen-/Skillregister mit öffentlich zulässiger Resultatprojektion verbinden; keine Komposition als bewiesenen KI-Leistungsvorteil deklarieren.

### 6.5 Offene bzw. nur teilfertige Arbeiten – nach der Solo-Runde
Der vorherige GAP-001 bis GAP-016-Bestand bleibt als **historischer Befund** bestehen. Verschiedene Punkte sind inzwischen teilweise weitergekommen:
- **GAP-001:** jetzt 72 atomisierte Anforderungen mit Artefaktverweis; die **Originalfolge der exakt letzten 100 Nachrichten fehlt**.
- **GAP-003:** statische Validatoren und CI-Workflows ergänzt; **Live-Browser-/Pages-Abnahme fehlt**.
- **GAP-008:** beschlossenes 7er-Menü bleibt; acht neue Seiten selektiv integriert; **kompletter Zweigmerge und dessen Konflikt-Regression fehlen**.
- **GAP-009:** beide Inkubatoren nun fachlich differenziert und gegenseitig verlinkt; **vollständige Standard-/Tool-/Testfamilien fehlen**.
- **GAP-011:** erweiterte KI-Seiten und Geo-Werkzeugarchitektur zugänglich; **unabhängige Fach-/Benchmarkabnahme fehlt**.
- **GAP-012:** ungeprüfte Promptbibliothek bewusst zurückgestellt; **extern nutzbarer Ende-zu-Ende-Mitmachworkflow bleibt offen**.

**Erkenntnis:** Kein nachgewiesener Verlust der importierten Git-Seiten. Die eigentliche wissenschaftliche/technische Endprüfung und die lückenlose Originalprompt-Abnahme sind weiterhin zu leisten, bevor von „fertig“ gesprochen wird.
