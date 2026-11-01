# Tensor Website – Skill-Team- und Selbstbeobachtungs-Audit v1.0
**Prüfdatum:** 2026-11-01 · **Prüfobjekt:** `Memnosis/relationalitaet`, Branch `main`, Veröffentlichung `/docs`.

## Ergebnis für das Projektmanagement
**Nicht alle Website-Tasks sind umgesetzt.** Der Design- und Taskkarten-Pilot ist vorhanden, 18 Minimal-KI-Aufgaben sind mit Meta-Prompts ausformuliert. Der Abgleich der historischen 106 PM-Aufgaben, die vollständige visuelle Migration, die Bild-/Diagrammredaktion und die Browserabnahme bleiben offen.

## Auditteams: spezialisierte Prüffunktionen
Die folgenden zehn **logischen Prüfrollen** wurden in diesem Durchgang als strukturierte Auditperspektiven angewandt; es handelt sich nicht um eigenständig eingeloggte KI-Agenten und nicht um 99 live laufende Beobachter.

| Rolle | Prüfmethode | Ergebnis | Bewertung |
|---|---|---|---|
| S01 Repo-Inventar | Git-Tree rekursiv gelesen | 50+ historische und Website-Dateien, alle Kernseiten vorhanden | Geprüft |
| S02 Navigation | relative `href`/`src` in elf HTML-Seiten auf vorhandene Pfade geprüft | keine fehlenden internen Zielpfade in geprüften statischen Links | Teilprüfung |
| S03 Redaktion | elf Seiten gegen verbotenen Begriff und doppelte Formulierung geprüft | 4 Dopplungen gefunden und durch vier Einzelcommits beseitigt; danach 0 in geprüften Seiten | Korrigiert |
| S04 PM-Schema | 18 Taskkarten per JSON auf IDs, Definition of Done und Quellenlinks untersucht | 18/18 mit Kriterien und URLs | Bestanden, Inhalt nicht fachabgenommen |
| S05 Prompt-Übergabe | Quelltext der Taskseite auf Promptkopie und GitHub-Issue-Link untersucht | Kopier- und Mitwirkungsfunktion implementiert | Browserfunktion nicht ausgeführt |
| S06 Design Tokens | Suche nach gemeinsamem Stylesheet | 4/11 Seiten nach Pilotnachzug angebunden | 7 noch offen |
| S07 Diagramme & Bilder | `svg`, `img`, `mermaid` auf elf Seiten gesucht | 3/11 Seiten mit erkannter Visualisierung | Ausbau offen |
| S08 Wissenschaftliche Quellen | Paper, Geo-KI, Harvestingregister und Übergabeseite geprüft | Basisdokumente auf Git vorhanden; nicht alle Archivoriginale veröffentlicht | Teilweise |
| S09 Barrierefreiheit | Semantisches `main` und je ein `h1` in elf Seiten gezählt | 11/11 formale Grundbedingungen | WCAG-, Tastatur- und Screenreaderprüfung offen |
| S10 Deployment | Git-Dateien per Connector gelesen, zwei Pages-URLs über externen Abruf versucht | Git erreichbar; Pages-Abruf in diesem Prüfsystem fehlgeschlagen | Veröffentlichung im Browser nicht bestätigt |

## Konkrete Umsetzungen dieses Audits
- Vier Footer-/Redaktionsdopplungen in `docs/minimal-ki.html`, `docs/tensoralgebra.html`, `docs/projektstand.html` und `docs/bibliothek.html` behoben.
- `docs/quellen-und-uebergabe.html` verwendet nun ebenfalls `docs/assets/tensor-design.css`.
- Dieses prüfbare Auditprotokoll in `forschung/website` gesichert.
- Keine historischen Papers gelöscht oder ersetzt.

## Selbstbeobachtungsprotokoll des ausführenden Assistenten
| Ereignis | Erwartung | Beobachtung | Konsequenz |
|---|---|---|---|
| OBS-A1 Git-Inventar lesen | Alle Kernartefakte in `main` finden | Taskregister, Paper, 99 Rollen, eigene Donutseite und CSS gefunden | Bestandsnachweis vor Urteil |
| OBS-A2 Seiten prüfen | Redaktionelle Vorgaben durchgehend erfüllt | Vier Footer-Dopplungen entdeckt | Vier gezielte Git-Fixes |
| OBS-A3 Links analysieren | Seiten verweisen auf vorhandene lokale Ziele | Keine fehlenden statischen relativen Ziele in den untersuchten Seiten | Kein pauschaler Linkfehler-Claim; externe/JS-Links ungetestet |
| OBS-A4 Design-Reichweite | Gemeinsame Tokens überall aktiv | nur drei, nach Patch vier von elf | Migration nicht als abgeschlossen ausgeben |
| OBS-A5 Visualisierungen | Jede geeignete Fachseite mit begründeter Grafik | drei von elf Seiten mit SVG/Bild/Mermaid-Signatur | Fachgrafiken als eigener Task belassen |
| OBS-A6 Live-Abnahme | Git-Änderungen über Pages nachsehen | zwei öffentliche Aufrufe über Werkzeug nicht erreichbar | Keine Browser-Abnahme behaupten |
| OBS-A7 PM-Status | Alle Website- und Forschungs-Tasks vollständig eingebunden | nur 18 Minimal-KI-Aufgaben; historische 106 nicht öffentlich zusammengeführt | Crosswalk/Taskvollausbau mit Vorrang |

**Nicht gemessen:** tatsächliche Browser-JavaScript-Ausführung, Laufzeiten, Klickquote, Nutzer-Reaktionen, WCAG-Wert, wissenschaftliche Validität oder Aufgabenleistung einer autonomen KI. Diese Werte werden ausdrücklich nicht erfunden.

## Priorisierte Nacharbeit und Abnahme
| ID | Aufgabe | DoD |
|---|---|---|
| WEB-QA-01 | Automatischen Redaktions-/Linktest in CI ergänzen | Build schlägt bei gesperrtem Begriff, fehlendem Pfad, fehlendem Task-Quellenlink fehl |
| WEB-PM-02 | Historische 106 Tasks mit 18 Karten über ID/Scope abgleichen | nachvollziehbare gemeinsame Übersicht, Konflikte und Dubletten markiert |
| WEB-UX-03 | Icons und Fachfarben auf restliche sieben Seiten migrieren | 11/11 mit gemeinsamen Token-Styles, visuelle Regressionsprüfung |
| WEB-MEDIA-04 | Quellbezogene Diagramme und Bildmaterial einsetzen | pro geeigneter Seite 1–2 sinnvolle, altbeschriebene Grafiken mit Herkunft |
| WEB-CONTENT-05 | Eigenständige Vertiefungen Komprimierung, visuelle Engine, KI-Kollegen | jede Fachseite mit Modell, Beispiel, Evidenz, Quellen, Tasks |
| WEB-A11Y-06 | Mobile, Tastatur, Dark Mode und 200-%-Zoom abnehmen | dokumentierte Browsertests ohne kritische Blocker |
| WEB-DEPLOY-07 | GitHub Pages öffentlich prüfen | Statuscode, Assets und interaktive Bedienelemente extern nachgewiesen |
| WEB-PAPER-08 | Vollständige Paper-Fassung mit Historie/Original verknüpfen | No-Loss-Provenienz und Version eindeutig und öffentlich |
| WEB-SKILL-09 | Observer der Website automatisiert im Versionsworkflow ausführen | reproduzierbare Metriken und Fehlerprotokoll pro Commit |

## Fundstellen
- Startseite: https://memnosis.github.io/relationalitaet/
- Taskkarten: https://memnosis.github.io/relationalitaet/taskkarten.html
- Quellenportal: https://memnosis.github.io/relationalitaet/quellen-und-uebergabe.html
- Tensor-Darstellung: https://memnosis.github.io/relationalitaet/tensor-einfuehrung.html
- Paper: https://github.com/Memnosis/relationalitaet/blob/main/forschung/minimal-ki/beobachter-v0_1/PAPER.md
- JSON-Tasks: https://github.com/Memnosis/relationalitaet/blob/main/forschung/minimal-ki/beobachter-v0_1/TASKKARTEN.json
- Designrichtlinie: https://github.com/Memnosis/relationalitaet/blob/main/forschung/website/DESIGNSYSTEM_V1.md

**Gesamturteil:** Umsetzung teilweise. Lokale, automatisierbare Repo-Prüfungen wurden ausgeführt; keine autonome Multiagentenkoordination oder Live-Interaktionsmessung simuliert. Eine wissenschaftliche und visuelle Endabnahme erfordert weitere Schritte.
