# KI-Tensor v6.0 – Semantischer Fastpass statt Parser-Bottleneck

Über die historische SQLite-Tabelle v52_formula_parser wurden **alle 7.622 DLMF-Formeltexte** mit sehr schnellen, transparenten syntaktischen Familienmarkern priorisiert, unabhängig von generischem LaTeX-Parsing.

| Primäre Familie | Formelakten |
|---|---:|
| Differential/Ableitungs-Marker | 2176 |
| Spezialfunktions-Marker | 1688 |
| Summen-/Ellipsen-Marker | 1339 |
| Algebra | 1323 |
| Sonstige | 735 |
| Asymptotik | 256 |
| Produkte | 105 |

**3.864** Formeln erhielten rein heuristische Priorität 1 (Ableitungs-, Integral- oder Spezialfunktionsmarker). Eine geordnete Familie ist kein wissenschaftlicher Nachweis. 5.162 Formeltexte enthalten genau ein Gleichheitszeichen, 1.924 mehrere, 536 keines.

**Neu wissenschaftlich bestätigte oder widerlegte Relationen: 0.** Es wurde keine Definitionsbereichsprüfung ausgeführt; nur die Existenz von Bedingungsmetadaten markiert. Keine der Kategorien wurde als neue gültige Trinität gezählt.

Gesamtpaket in der Unterhaltung: KI_Tensor_Semantic_Fastpass_v6_0.zip mit formel_semantik_7622.csv und reproduzierbarem Skript. Priorität der nächsten Entwicklung: semantische Rollen-/Relationshypothese mit Original-Formelankern erzeugen; passende Testverfahren familienspezifisch und nur unter belegten Domänen durchführen. Das ist unabhängig vom allgemeinen Parser und durch konkrete bewiesene/widerlegte Relationsaussagen zu messen.