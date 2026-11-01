# Tensor: Kernänderungen und Abnahmefundstellen – 2026-11-01

## Sofort prüfen
| Änderung | Öffentlich | Quellpfad | Prüfpunkt |
|---|---|---|---|
| Sechs Kernbereiche und Symbolik | https://memnosis.github.io/relationalitaet/ | docs/index.html | 01 Mini-KI (Gehirn), 02 Geo-KI (Globus), 03 Tensor (Ring-Matrix), 04 Komprimierung (Layer), 05 Visuelle Engine (Auge), 06 KI-Kollegen (Netzwerk) |
| Tensor mit Donut | https://memnosis.github.io/relationalitaet/tensor-einfuehrung.html | docs/tensor-einfuehrung.html | 27 anklickbare Positionen, Fachgrenzen und Erklärung |
| Task-PM-Karten | https://memnosis.github.io/relationalitaet/taskkarten.html | docs/taskkarten.html | Filter, Meta-Prompts, Kerngliederung, kopierbare ausgeschriebene Quellen-URLs, GitHub-Mitwirkung |
| Übergabequellen | https://memnosis.github.io/relationalitaet/quellen-und-uebergabe.html | docs/quellen-und-uebergabe.html | Paper, Register, Code und Aufgabenfamilien erreichbar |
| Task-Datenvertrag | https://github.com/Memnosis/relationalitaet/blob/main/forschung/minimal-ki/beobachter-v0_1/TASKKARTEN.json | JSON | 18 IDs, DoD, Abhängigkeiten, Meilensteine, Prioritäten, Quelladressen |
| Farb-/Komponentensystem | https://github.com/Memnosis/relationalitaet/blob/main/docs/assets/tensor-design.css | CSS | hell/dunkel, Akzentfarben und Fokus |
| SVG-Icons | https://github.com/Memnosis/relationalitaet/blob/main/docs/assets/tensor-icons.svg | SVG | sechs einheitliche Symbole |
| Designrichtlinie | https://github.com/Memnosis/relationalitaet/blob/main/forschung/website/DESIGNSYSTEM_V1.md | Markdown | fortlaufende Vorgaben |
| Eigenes Paper | https://github.com/Memnosis/relationalitaet/blob/main/forschung/minimal-ki/beobachter-v0_1/PAPER.md | Markdown | Quellen, eigener Forschungsstand |
| PM-Änderungsliste | diese Datei | Markdown | Was geändert und was noch offen ist |

## Test- und Abnahmebedingungen
- Code-/Git-Pfade über API abrufen; Dateiinhalte und 18 Task-IDs testen.
- Interaktives Browser-Rendering, Dark-Mode, Mobil, Tastatur, Kopierberechtigung sind zusätzlich im Browser zu testen; Git-Erfolg allein ist kein visueller oder funktionaler Browsertest.
- Alte Paper nicht gelöscht. Bestehende Projektseiten weitgehend erhalten; Startbereich auf sechs separat verlinkte Kernbereiche angepasst.
- Die Kopierfunktion kopiert den gesamten Meta-Prompt **mit voll ausgeschriebenen URLs**, nicht nur einen Quellennamen.
- GitHub-Mitwirkung: Issue-Erstellung erzeugt einen vorausgefüllten Entwurf; es wurde noch kein Issue automatisch eingereicht.

## Offene Aufgaben
1. Alle 106 historischen PM-Aufgaben mit den 18 aktuellen Tasks per Crosswalk abgleichen; anschließend einen Gesamt-Taskeinstieg anbieten. Aktuelle Website zeigt 18 ausformulierte Aufgaben, nicht alle 106.
2. Visuelle Engine, Komprimierung und KI-Kollegen als eigene vertiefte Fachseiten statt vorläufige Anker-/Querverweise.
3. Echte Diagramme 1–2 pro geeigneter Fachseite (erklärungsorientiert), Version und Quellen.
4. Responsiveness/Barrierefreiheit im Browser mit Screenshots und Tastatur prüfen.
5. Alte Designrichtlinie mit den sechs zuletzt festgelegten Namen/Icons abgleichen.
6. Durchgängige Git-Abnahme per CI für unerwünschte Begriffe, kaputte Links, fehlende Task-URLs.
