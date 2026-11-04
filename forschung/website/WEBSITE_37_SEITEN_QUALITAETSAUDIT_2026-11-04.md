# Website-Qualitätsaudit und Finalisierung · 04.11.2026

**Prüfumfang:** 37 bekannte veröffentlichte HTML-Dateien unter `docs/` einschließlich Start, KI, Geschichte, Kernforschung, Tensor, Tensoralgebra, Geo-KI, Geo-Werkzeuge, Mini-KI, Komprimierung, Visuelle Engine, Harvesting, Forschungsdaten, Projekte/Portfolio/Management, Inkubator, Mitmachen/Rückgabe/Taskkarten, SOULution, Publikations- und Fachregister, Sonderthemen und Impressum. **Stand:** GitHub-Quelltext geprüft, kein visuelles Live-Screenshot- oder externer Linktest.

## A. Befunde und konkrete Korrekturen

| Vorherige Schwäche | Nachgewiesene Ursache | Eingriff | Stand |
|---|---|---|---|
| Wechselnde Navigation | Altes `tensor-hierarchy.js` baute dynamisch Untermenüs, neues `website-unified.js` ersetzte sie erneut; übrig gebliebene Hierarchieklassen beeinflussten Flex/Breiten | Hierarchieskript und zugehöriges CSS aus allen 37 HTML-Seiten entfernt; identischer statischer 8-Punkte-Header als JS-Fallback; gemeinsames v3-Skript ersetzt vorhandene Navigation durch einen einzigen aktiven Header | Code aktualisiert |
| KI-Geschichte-Link verzerrt | Alte unterschiedliche Flexregeln, lange Quelllinks und nicht auf drei Spalten begrenzte Einzelseiten | Einheitliche Breakpoints, echte 3/2/1-Karten, definierte Linkumbrüche, KI-Fachfarbe; historisches Dossier als zusammengehöriger Rahmen mit Einordnung versehen | Code aktualisiert |
| Alte Unterseiten anders navigierbar | Fehlende v2-Gemeinschaftsdateien auf mehreren Detailseiten | Alle 37 Seiten erhalten v3-CSS und -JS, Breadcrumbs und auto-generierten Abschnittswegweiser, sofern kein eigener Lernpfad besteht | Code aktualisiert |
| Icons und Farben uneinheitlich | SVG-Symbole, Unicode-Icons und CSS-Pseudoglyphen gemischt | Bestehende SVG-Sprite-Icons für Hauptnavigation, Fachblöcke und alte Metathemen wiederverwendet; echte SVG statt Schriftzeichen | Code aktualisiert |
| Vier Spalten trotz neuer Drei-Spalten-Regel | `projektmanagement.html` enthielt explizit 4-Spalten-Grid; mobile Navigation zunächst ebenfalls 4 | Maximal drei Spalten, auf kleinen Displays 2 beziehungsweise 1 in Karten; mobile Hauptnavigation drei | Code aktualisiert |
| Meta-Inhalte noch nicht sauber ausformuliert | Visuelle Engine und Komprimierung waren nur kurze, unstrukturierte Einstiegstexte | Beide Seiten ausführlich umgebaut: drei Fachblöcke, mathematisches SVG-Beispiel, Gegenprobe, Daten/Skills und Mitmachaufgabe | Code aktualisiert |
| Fehlende Anker in Querverweisen | Referenzen auf `#benchmark`, `#GEO-M1`, `#FMT-H01`, die nicht statisch oder in öffentlichem Aufgaben-JSON existierten | Auf vorhandenen KI-Forschungsanker beziehungsweise öffentlich existierende Mitmachziele umgebogen | Code aktualisiert |
| Geo-KI Komposition optisch schwer zu vergleichen | Zwei identische Prüfpfeile lagen vollständig übereinander | Direktpfad türkis, zusammengesetzter Pfad orange gestrichelt, erklärende Legende | Code aktualisiert |
| Suche nach Tensor/Skill schaltete unpassenden Filter nicht vollständig ab | Nur das Select war verborgen, das Label blieb sichtbar | Select und Beschriftung wechseln gemeinsam | Code aktualisiert |

## B. Fachlicher Zusammenhalt und Navigation
Feste Hauptnavigation aller Seiten: `Start · KI · Tensor · Projekte · Harvesting · Publikationen · Mitmachen · SOULution`. Detail-URLs bleiben erhalten und erhalten eine übergeordnete fachliche Zuordnung und einen Inhaltswegweiser. Kein gleichrangiger Hauptmenüpunkt für KI-Geschichte, KI-Kollegen, Tensoralgebra, Codebuch, Thesen oder Inkubator. Projektmanagement ist ein unauffälliger Footerzugang (kein Sicherheitsmechanismus).

**Thematische Seitengruppen:**
- Start: vier Kernprojekte, gemeinsame Infrastruktur, öffentlich verfügbare Daten und Mitmachen.
- KI: Entwicklungslinien, selbstorganisiertes Skilllernen, unabhängige KI-Gegenprüfung, Quellen/Publikationen. Geschichte ist ein Fach-Dossier.
- Tensor: mathematische Definition, 3×3×3-Rollen, echte Datensätze, Algebra, Harvesting-Anschlüsse, 27er-Feldprüfungen.
- Geo-KI: veränderbare Rotation → Norminvariante → Komposition/Gegenprobe → Formengenerator → öffentliche Skills → eigenes Prüfexperiment.
- Visuelle Engine: Struktur-, Prozess- und Prüfgrafiken; konkretes Rotationsbeispiel; Datenvertrag und medienübergreifende Icongrammatik.
- Komprimierung: parametrische Rekonstruktion; genaue/angenäherte/strukturelle Qualitätsmaße; Verbindung zu Geo-KI, Tensor und Mini-KI.
- Projekte: vier wirkliche Entwicklungsprojekte plus Portfolio und nachvollziehbare Meilensteine.
- Harvesting/Forschungsdaten: mathematische Trinitätensuche, 103 historische Tensorgerüste und 13 implementierte Geofunktionen neben acht klar als Kandidaten geführten Interoperabilitätsfamilien.
- Publikationen: Papers, Codebuch, Index, Thesen, Glossar, Medien, Inkubator und Quellen.
- SOULution: 3×3-Lösungsbereiche mit Originalgestaltung und Quellenbezug.
- Mitmachen: Aufgaben aus öffentlich freigegebenen Datensätzen, Rückgabe, Gegenbefunde und Reviews.

## C. Prüfstand am GitHub-Quelltext
- **37/37** bekannte HTML-Seiten: exakt ein sichtbarer statischer `nav[aria-label=Hauptnavigation]` mit identischen acht Textpunkten; keine Referenz auf die entfernte Hierarchie-Logik.
- **37/37**: gemeinsame Fach-CSS-/JS-Dateien eingebunden.
- **37/37**: im statischen Quelltext keine doppelten IDs und keine fehlenden unmittelbar lokalen `#`-Anker ermittelt.
- **37/37**: die Summe der öffnenden und schließenden `section`- beziehungsweise `svg`-Elemente ist ausgeglichen.
- **13 eingebettete Inline-JavaScript-Blöcke** über die 37 Seiten auf Syntax geprüft, **0 Syntaxfehler**.
- Die 15 bekannten direkt genutzten Hauptgrafik-/SVG-/CSS-/JS-Quellen und weitere bedarfsgeladene Assets wurden stichprobenhaft über den GitHub-Connector auf Existenz geprüft; auffällige fehlende Hauptgrafiken wurden nicht festgestellt.
- Ein Inventar von 13 öffentlichen Mitmachaufgaben wurde zur Prüfung der dynamischen Task-Anker herangezogen; zwei im Inventar fehlende IDs wurden umgeleitet.
- Die öffentlich verfügbaren Tensor- und Skillregister bleiben quellgebunden und klar als Inventare, Softwarefunktionen oder Kandidaten gekennzeichnet; keine erfundenen wissenschaftlichen Prüfresultate.
- Neues unabhängiges QA-Werkzeug: `scripts/audit_website.py`, zur Prüfung der gesamten `docs/`-Seiten auf Dateiziele, IDs/Fragmente, SVG-Symbole, identische Navigation, alte JS-Module und Tensorzahlen.

## D. Nicht als abgeschlossen behaupten
1. **Visueller Browser-Test** auf 320, 375, 768, 1024 und 1440 Pixel einschließlich Darkmode ist mit dem hier verfügbaren GitHub-Zugriff nicht möglich und muss separat erfolgen.
2. Die tatsächlichen klickbaren Umschaltungen müssen zusätzlich im realen Browser mit Maus, Tastatur und Screenreader getestet werden. Statische Syntaxprüfung simuliert keine DOM- oder Browserzustände.
3. Externe Quellen-URLs und Veröffentlichungsstatus von GitHub Pages wurden hier nicht vollständig live geöffnet. Die GitHub-Dateien sind aktualisiert, externe HTTP-Status können sich ändern.
4. Ältere vertiefte Fachtexte sind nicht inhaltlich verkürzt worden. Ihre Übernahme in separate Papers benötigt Quellen-, No-Loss- und redaktionelle Abnahme.
5. Die vollständige alte SQLite-Masterdatenbank und die neueren mathematischen Feldprüfakten sind noch nicht im öffentlichen JSON-Inventar integriert. Das wurde bereits separat an Claude adressiert.

## E. Weiterer verbindlicher Ausbau
- Jede fachliche Änderung bekommt einen Abschnitt über Begriff, Eingabe, Operator/Relation, Ergebnis, Gegenprobe, Belegstatus und Quellen; bei ausreichender Länge ein freigegebenes Paper.
- Jede neue Navigation und Hauptseite muss vom Skript `scripts/audit_website.py` und einem visuellen Browser-/Responsivtest erfasst werden.
- Keine erneute parallele Nav-Logik: der Standard ist `docs/assets/website-unified.js` und `docs/assets/website-unified.css`. `tensor-hierarchy.js` ist nicht in HTML aktiv zu verwenden.
- Original-Grafikbestände, Inhalte, Daten und Querverweise nicht löschen; Änderungen werden per Git-Version und Quellenregister nachvollziehbar.
