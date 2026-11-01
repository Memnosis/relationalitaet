# Tensor – Designsystem und Website-Vorgaben v1.0
**Stand:** 2026-11-01 · **Status:** freigegebene Entwicklungsgrundlage, noch kein vollständiges Frontend-Rollout.

## Bestandsschutz
- Website und Repository bleiben an ihrem bisherigen Ort; Pages unter `/docs`.
- Sechs Kernbereiche: Minimal-KI, Geo-KI, Tensoralgebra, Komprimierung, Visuelle Engine, KI-Modellvergleich. Forschungsbibliothek, Aufgaben und Projektsteuerung sind zusätzliche Bereiche.
- Keine kosmetische Löschung historischer Veröffentlichungen, 18 Task-IDs, 99 Beobachterrollen, Paper oder Quellendaten.
- Pro wissenschaftlichem Tensor exakt 3 Trinitäten × 3 Elemente × 3 Rollen = 27 Positionen. Die Anzahl der Skills ist davon unabhängig.
- Kein öffentliches Vorkommen des internen Begriffs `Courseware`; automatische Prüfung vor Deployment. Bekannte Textdopplung `Forschungs-Forschungsplattform` bei späterer redaktioneller Migration korrigieren.

## Farblogik
| Rolle | Hell | Dunkel |
|---|---|---|
| Hintergrund | #F8FAFB | #10171C |
| Flächen | #FFFFFF | #19232B |
| Text | #17272E | #E6F1F4 |
| Hilfstext | #435961 | #ABC0C6 |
| Linien | #C9D8DC | #435760 |
| Tensor gesamt | #086C78 | #67CCD4 |
| Minimal-KI | #5D4F9A | #B2A5ED |
| Geo-KI | #086F86 | #65C9E5 |
| Tensoralgebra | #3D6A3E | #A5DAA0 |
| Komprimierung | #93611E | #E4BF75 |
| Visuelle Engine | #9B4877 | #E3A3CF |
| KI-Modellvergleich | #5B6474 | #BAC5DA |
| Quellen | #326B63 | #8CDBCF |
| Mitwirkung | #A25835 | #F1AA83 |

Neutrale Flächen dominieren; Fachfarben ausschließlich als feine Cardkante, SVG-Detail, Label oder Diagrammakzent. Status nie nur über Farben. Kontrast und Fokus nach WCAG 2.2 AA testen.

## Iconvertrag
Einheitliche Version der Lucide-SVG-Icons: Minimal-KI `brain-circuit`, Geo-KI `shapes`, Algebra `grid-3x3`, Komprimierung `layers-3`, visuelle Engine `scan-eye`, Modellvergleich `git-compare-arrows`. Ergänzend Beobachter `eye`, Skills `workflow`, Forschung `library-big`, Quellen `book-open-check`, PM `list-todo`, Mitwirkung `handshake`. Icons plus aussagekräftige Textlabels; keine vermischten Emoji- oder Fontbibliotheken. Eigene Tensor-Wortmarke als Ring-Matrix mit 27 Elementen, vereinfacht für kleine Größen.

## Informationshierarchie
1. Start: sechs Bereichskarten und ihre Relationen; leise Forschungs- und Aufgabenleiste.
2. Fachbereich: Erklärung → Modell → interaktives Beispiel → Teststand → Grenzen → Paper → Quellen → Tasks.
3. Paper: Abstract, Fachmodelle, eigene Rekonstruktion, Evidenz, Tests, Ergebnisse, offene Fragen, Version.
4. Task: ID, Bereich, Meilenstein, Status, Meta-Prompt, kurze Anleitung, Ergebnis und Abnahme, spezifische Quellen.
5. Quellenportal: Paper, Code, Daten, Lizenzen, Versionen, Übergabe an externe KIs.
6. PM: echte Zahlen, Abnahmen, Blocker, Herkunft und Aufgabenverweise.

## Taskkarten und Mitwirkung
**Alle Tasks** erhalten schrittweise Meta-Prompts der Form **„Entwickle einen Prompt für …“**. Nur vorhandene Aufträge übernehmen; keine erfundenen Leistungen oder Aufgabenstände.

Pflichtdaten: `id, project_id, milestone_id, title, goal, meta_prompt, instructions, deliverables, acceptance, dependencies, references[], status, priority, version, provenance`. Bearbeitungszustände: inventarisiert → prompt_vorbereitet → beauftragt → in_arbeit → eingereicht → geprüft → abgenommen; optional blockiert. Die vorhandenen **18** Minimal-KI-Karten sind der Pilot. Historische Projektbaseline mit **106** Aufgaben erst per ID-Crosswalk und Dublettenprüfung erschließen, anschließend alle zugehörigen Prompts nachziehen. Eine Taskkarte kopiert ihren Prompt, führt zu spezifischen Dokumenten, erklärt das erwartete Artefakt und bietet einen überprüfbaren Mitwirkungsweg.

## Wissenschaftliche Bilder, Diagramme und Mermaid
Meist **1–2**, bei konkretem Bedarf **3** sinnvoll platzierte Grafiken pro Seite; kein künstlicher Diagrammzwang. Für jede Grafik: Erkenntnisfrage, Quelle, Bildunterschrift, Textalternative und Daten-/Versionsstand. Mermaid in versioniertem Quelltext, publiziert als geprüftes SVG (inklusive Altbeschreibung), nicht über eine fremde Laufzeitabhängigkeit. 3×3×3-Tensorvisualisierung aus eigenem Schema, nicht als bloßes Mermaid-Raster. Bilder aus eigenen Daten, sauber lizenzierten Originalen oder erkennbaren Illustrationen; mit Media-Manifest inkl. Quelle/Lizenz/Alttext/Einbauort.

## Ausführung ohne erneuten Komplettumbau
- D0: Richtlinien auf Git ablegen; keine öffentliche Seite umgestalten.
- D1: gemeinsame CSS-Tokens, Icons und eine isolierte Vorschau aufbauen.
- D2: Taskkarten und Übergabeportal als Pilot migrieren, bestehende Kopierfunktion erhalten.
- D3: Paper/Forschungsbibliothek mit sinnvoll platzierten Diagrammen.
- D4: Fachbereiche stufenweise aktualisieren; Startseite **zuletzt**.
- D5: PM-Crosswalk historische 106 Aufgaben ↔ vorhandene 18 Taskkarten mit No-Loss-Abgleich.

## Abnahme
Desktop und Mobil, Dark Mode, 200 % Zoom, Tastatur, Kontrast, Bildalternativen, stabile Linkziele, Promptzuordnung pro Task-ID, Unverändertheit historischer Originale, Git-Diff und nachvollziehbare Rückrollmöglichkeit. Kein Deployment ohne prüfbaren Inhaltserhalt. 
