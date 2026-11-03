# GPT-Solo-Fortsetzung R4 – Website-Regressionsbefund, Nachzug und 72 Anforderungen

**Datum:** 2026-11-03 · **Owner:** GPT Website. **Claude:** während dieser Teilrunde nicht beteiligt. **Status:** Git-Dateien und statische Prüfungen vorgenommen; *kein* vollständiger gegenseitiger KI-Zyklus und keine Autor-/Publikationsfreigabe.

## 1. Tatsächlicher Prüfbestand und Grenzen

| Gegenstand | Tatsächlich durchgeführt | Ergebnis | Einschränkung |
|---|---|---|---|
| Live-GitHub-Pages | HTTPS-Abruf von `index.html`, `ki-systeme.html`, `codebuch.html`, `projektmanagement.html`, Quellenatlas | Nicht abrufbar über verfügbares Web-/Container-Netz (keine erfolgreiche Auslieferung bestätigt) | Keine Aussage über echten Besucherbetrieb oder Browserdarstellung |
| 33 Seiten-Hauptnavigation | HTML der 33 einzeln auditierten Seiten aus Git gelesen; nach `tensor-hierarchy.js` gesucht | **Drei fehlende Einbindungen** identifiziert und korrigiert | JavaScript-Lauf, Keyboard/Touch/Screenreader nicht getestet |
| 33 Seiteninterne Sprungmarken | Literale `href="#…"` gegen vorhandene IDs auf 33 Git-HTML-Dateien geprüft | **Keine unaufgelösten statischen Selbstanker** gefunden | Dynamisch durch JavaScript erzeugte Zielanker nicht gleich einem Browser-Sprungtest |
| Acht integrierte Fachseiten | `docs/*.html` mit Hauptzweig geprüft, neues Nav-System vs. branch-eigenes geprüft | Alle 8 sind in `main`; unerwünschte `site-nav.js` dort nicht aktiv | Nicht alle älteren Zweigänderungen übernommen; kontrollierter Restdiff erforderlich |
| Lokale Bilder/Assets/Skripte | 45 zuvor erfasste Links/Assets aus Seiten anhand aktueller Git-Datei-Stati geprüft | 44 vorhanden; einziger alter Fehlverweis `promptbibliothek.html` bewusst nicht veröffentlichter Inhalt und auf integrierten Seiten durch Safe-Link ersetzt | Vollständige dynamische URLs und Laufzeit-API-Aufrufe später prüfen |
| Workflow-JS und Daten | Syntax von `tensor-hierarchy.js`, `projektmanagement.js`, `workflow-stand.js`, `thesen-evidenz.js` und dem neuen Abdeckungs-Skript geprüft; JSON-Parsing für die relevanten 5 Register | Syntaktisch gültig, ohne Laufzeitabnahme | Kein E2E-Test und kein GitHub-Actions-Erfolgsprotokoll |
| 72 atomisierte Anforderungen | Jeder der 72 `requirements[].evidence`-Pfade mit `fetch_file` gegen `main` abgerufen | **72/72 Quelldateien existieren** | Dateiexistenz ist weder die Erfüllung der Aufgabe noch Beweis ihres Originalprompt-Wortlauts |
| Letzte exakt 100 Nutzernachrichten | vorhandene 72 Fachaufträge und Projekt-/Gesprächssummaries gegengeprüft | **Nicht vollständig rekonstruierbar** | Kein datierter Volltext-/Message-ID-Export der exakt letzten 100 Originalnachrichten vorhanden; keine erfundene 100er-Erledigtquote |

## 2. Jetzt tatsächlich durchgeführter Nachzug

### P0-WEB-R4-01 – drei fehlende Navigationseinbindungen
- `docs/interoperabilitaet.html`, Commit `271b8c4`
- `docs/quellen-und-uebergabe.html`, Commit `1f1281e`
- `docs/impressum.html`, Commit `0b2082f`

Die Seiten behalten den bisherigen statischen HTML-Link-Fallback; ergänzt wurden lediglich das gemeinsame Skript `tensor-hierarchy.js` und die Navigation-CSS.

### P0-WEB-R4-02 – bestehende wissenschaftliche Fachbezüge aus Integrationszweig bewahren
Zusätzlich zu den bereits importierten acht Seiten wurden sechs nicht redundante Fachhinweise in bestehende Hauptzweigseiten übernommen, **ohne ungetestete Prompt- oder private Datenbestände zu importieren**:
- `docs/glossar.html` – zwölf redaktionelle Webdefinitionen gegen 1.008/1.072 historische Archivstände sauber abgrenzen (`158f31d`).
- `docs/harvesting.html` – Datenmengen versus tatsächlich geprüfte wissenschaftliche Relationen (`e694364`).
- `docs/interoperabilitaet.html` – Formatkompatibilität ist kein Modell- oder Physikbeweis (`c9dd3a2`).
- `docs/geoki.html` – Geo-KI als eigene Forschungsrichtung, keine automatisch bestätigte Tensor-KI (`7809d36`).
- `docs/medien.html` – SOULution-Werke und Fachmodule angemessen verknüpfen (`056e952`).
- `docs/projektstand.html` – Inventarzahlen und wissenschaftlich gesicherte Fortschritte unterscheiden (`1a762c5`).

### P0-PM-R4-03 – Originalprompt-Abdeckung im Projektmanagement
- Neues public-safe `docs/data/anforderungsabdeckung-v1.json` (`800d5a2`): neun **redaktionell gruppierte** Aufgabenfelder und 72 Atom-Aufträge; keinerlei Originalchat-/Metaprompt-Volltexte.
- Neues `docs/assets/anforderungsabdeckung.js` (`a9e7ccc`): zugängliche Tabellenstruktur aus JSON ohne unbereinigte HTML-Injektion.
- `docs/projektmanagement.html` (`eca690b`): neuer Abschnitt `#anforderungen-und-originalprompts` erklärt, was 72 Anforderungen belegen und was noch nicht.
- `scripts/validate_site_integration.py` (`f853a15`, `57c84ba`) erweitert: **33** auditierte Seiten statt nur acht, relative Links/Assets, sichere Navigation, die neun Bereichssummen, 72 Git-Herkunftsdateien und ausdrücklicher Negativtest gegen fingierten 100er-Quellnachweis.

## 3. Was an Aufgaben verloren bzw. halb fertig ist

Keine der 72 geprüften **verlinkten Git-Dateien** fehlt im aktuellen Hauptzweig. Aber dieser Befund lässt **keine Aussage** darüber zu, ob die zugehörige Originalanforderung vollständig erfüllt wurde. Offen bzw. teilweise:
1. P0 vollständiger Original-Nachrichtencrosswalk (genau 100, chronologisch, Message-ID, Text/Hash, atomare Aufträge, Nachfolgeentscheidungen).
2. P0 echte GitHub-Pages-/Desktop-/Keyboard-/Screenreader-Abnahme, PDF-/Grafik- und Bibliotheksansichten.
3. P0 komplette, konfliktfreie Restintegration des 160-Commit-Zweigs; wichtige Zweigabschnitte gezielt übernommen, aber kein beliebiges pauschales Merging.
4. P0 tatsächliche wissenschaftliche und unabhängige Prüfung von Originalthesen, 27 Feldakten, Tensor-/Feldtheorie und kanonischem Claudes Datenexport.
5. P0 sichere Ausführung und Ergebnisrückgabe der Mitmachangebote ohne Git-Schreibrecht, Freigabe/Privatsicherung historisch öffentlicher Metaprompts.
6. P0 kanonisches, aus Testakten generiertes Projektmanagement; derzeit redigierter Snapshot, nicht automatisch an alle Original-Testbestände gebunden.
7. P1 fortlaufender Website-Ausbau auf E1 Grundlagen, E2 Alternativen/Entwicklung und E3 Quellen/Rechnungen/Negativfälle; darunter juristische/gesellschaftliche dynamische Themen.
8. P1 fehlende echte Testmetriken zur Wirkung von KI-/Skill-/Tensor-Komposition gegenüber einfachen Baselines.

## 4. Konkrete nächste GPT-Schritte, bis die unabhängige Gegenprüfung möglich ist

1. **Technische Akzeptanz:** CI-Ergebnis und tatsächliche GitHub Pages prüfen, `validate_site_integration.py` lokal/CI ausführen; Fehler mit SHA/Output dokumentieren. `fetch_commit_workflow_runs` zeigt nur PR-Läufe und keine Ergebnisse für den untersuchten Push; daraus ist kein erfolgreicher CI-Lauf ableitbar.
2. **Restdiff:** Zweig `integration/soulution-shared-core-2026-11-03` nur nach Abschnitts- und Ankerdiff mit aktuellem `main` abgleichen; keine sensiblen Promptbibliotheken; jetzt fehlende fachliche Zusammenhänge bei Glossar, Geo-KI, Harvesting, Quellen/Medien teils nachgezogen.
3. **Provenienz und Aufgaben:** Originalnachrichten-ID-Export als fehlendes Testmaterial dokumentieren, 72er-Anforderungsregister dann mit tatsächlichen 100 Nutzernachrichten verbinden; Stände offen/teilweise/getestet/abgenommen trennen.
4. **Website-Lernwege und Wirksamkeit:** 33 Einzelaudits mit tatsächlich ausgeführten Abnahmen aktualisieren, Quellen-/Thesenkarten erst nach geprüfter Claude-Projektion befüllen.

**Wichtig für spätere Claude-Übergabe:** Claude soll diesen konkreten GPT-Artefaktstand unabhängig beurteilen, aber während der aktuell angesagten Pause nicht durch weitere offene Prüfbitten unterbrochen werden. Gemeinsamer KI-Zyklus 001 wird dadurch nicht abgeschlossen.
