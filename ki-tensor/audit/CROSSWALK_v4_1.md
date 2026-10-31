# KI-Tensor · Crosswalk-Prüfung v4.1 (2026-10-31)

Die verbundenen SQLite-Tabellen `v115__v107_trinitaeten`, `v115__v109_trinitaeten_review` und Glossartabellen wurden nach ihren **tatsächlichen Primärschlüsseln** verglichen.

## Trinitäten
- v10.7: **309** Achsen in **103** Tensorgerüsten.
- v10.9 Review: **297** Achsen in **99** Tensorgerüsten.
- Alle 297 Review-Achsen sind als `(tensor_id, achse)` auch im 309er-Inventar enthalten; alle drei Elementtexte stimmen **297/297** exakt überein.
- Die fehlenden zwölf Review-Achsen entsprechen vier kompletten Tensorgerüsten: **CORE-T1, CORE-T2, CORE-T3 und FACH-F001**. Sie sind **nicht gelöscht** und im v10.7-Bestand weiterhin vorhanden.
- v11.2 enthält zwölf zusätzliche Achsenpositionen mit Identifikatoren P1–P4. Ihre Identität/Neuheit gegenüber den 309 ist noch nicht fachlich geprüft; deshalb nicht automatisch addieren.

## Glossar
- v15.4: **1.072** Glossarzeilen.
- v11.5: **1.008** Glossarzeilen.
- Die 1.008 alten IDs sind in v15.4 vorhanden; es gibt somit **64 zusätzliche Zeilen** gegenüber dem älteren Kernstand (noch keine fachliche Validierungsbehauptung).

## Aussagegrenzen
- Ein gemeinsamer Schlüssel und gleiche Elementtexte belegen Versionskontinuität, **nicht** die wissenschaftliche Richtigkeit der Relation.
- `v3.8`-DLMF-675-Rohtripel sind nicht mit den 309 historischen Originalachsen identisch gezählt.
- 103 Tensorgerüste bedeuten 103 strukturierte 3×3×3-Entwürfe, **keine** 103 vollständig geprüften Tensoren.
- Offen bleiben Quellenprüfung, Relationsbeweise, Gegenproben und die Klassifikation sämtlicher nicht passender Achsen.

## Arbeitspriorität
1. Die vier im v10.9-Review fehlenden Tensoren (drei CORE und FACH-F001) quellenbewahrend rückführen.
2. Für die 64 zusätzlichen Glossareinträge und 1.008 gemeinsamen IDs die Definitionshistorie und Quellendifferenzen dokumentieren.
3. Historische Achsen und DLMF-675 über Erklärungsfunktion, Bedingungen und mathematischen Relationsbeleg abgleichen.
4. Bestandsversionen und binäre No-Loss-Artefakte auf GitHub via Git/Git-LFS sichern, ohne den historischen Branch zu überschreiben.
