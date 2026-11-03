# R4-Lauf · Leser-Prompt H1 „Kann das stimmen?“ · Claude, unabhängig (blind)

**Prompt:** H1 aus `docs/data/promptbibliothek-v1.json` (Zweig `integration/soulution-shared-core-2026-11-03`, Blob `4e09282`), Prompt-SHA-256 `fa0bb55b…5eec`.
**Blind:** Gelesen wurden nur `prompt`, `inputs`, `title` und `purpose`. **Nicht** gelesen: GPTs Ausgabe, `tests`, `provenance`, Quellenfalltests.
**Eingabe:** eigene, versiegelte Eingabe `H1_CLAUDE_INPUT_SNAPSHOT_01.json` (SHA-256 `a985549f…e19e`), ein Positiv- und ein Negativfall. GPTs Eingabe ist angefragt, um zusätzlich mit identischer Eingabe zu vergleichen.
**Akte:** [`H1_CLAUDE_BLIND_01.json`](H1_CLAUDE_BLIND_01.json) · **Status:** `public_release: not_approved`.

---

## Fall H1-C-POS

> „Die Relationale Logik ist keine weitere Variante, sondern die Meta-Logik, die alle bisherigen Logiksysteme als spezielle Realisierungen derselben trinitären Architektur versteht.“

**Ursprung und Originalquelle:** Nils Sautter, *Relationale Logik – der Logik Tensor*, Version 1.0, DOI 10.5281/zenodo.19282895, **S. 19, Abschnitt 9.1**. Wörtlich so im Original; per Sichtprüfung der Seite bestätigt.

**Datierung:** 28.03.2026, sowohl laut Zenodo-Veröffentlichungsdatum als auch laut Fußzeile des PDF („Vers. 1.0 / 28.03.2026“).

**Belegt:**
- Wortlaut, Fundstelle, Autor, Datum, Version.
- Im selben Werk sind **7** Logiksysteme tabellarisch zugeordnet (S. 14–15): klassisch, intuitionistisch, modal, mehrwertig, parakonsistent, Relevanz, algebraisch.

**Interpretation (nicht belegt):**
- „**alle** bisherigen Logiksysteme“ ist ein Allgemeinheitsanspruch. Das Werk zeigt 7 Zuordnungen, keine Einbettung aller Systeme.
- „Meta-Logik“ wird nicht formal definiert. Die Semantik auf S. 20 („gültig, wenn in allen drei Matrizen … konsistent zugeordnet“) gibt kein Prüfverfahren an.
- Spannung im Werk selbst: S. 15 sagt, der Tensor sei „nicht selbst ein weiteres Logiksystem“; S. 19 lässt aus ihm eine „eigenständige Relationale Logik“ hervorgehen. Das ist kein Widerspruch, aber eine Unterscheidung, die präzisiert werden sollte (Tensor als Rahmen ↔ Relationale Logik als System).

**Gegenbefunde aus der Fachliteratur.** Aus Fachwissen benannt, **in diesem Lauf nicht digital nachgeprüft**:
- Es gibt etablierte, formal definierte Rahmen für den Vergleich vieler Logiken: Institutionentheorie (Goguen/Burstall, 1980er/1992), abstrakte Modelltheorie (Barwise u. a., 1970er), „Universal Logic“ (Béziau, ab 2005). Sie definieren, was eine Logik ist und wann eine Übersetzung Folgerungen erhält. Daran müsste sich der Meta-Logik-Anspruch messen.
- Das Werk führt „Institution Theory“ selbst als „offen“ im Außenraum (S. 16). Es nennt also einen solchen Rahmen, bindet ihn aber nicht an.

**Offene Fragen:**
- Welche Übersetzungen zwischen Logiken sind gemeint?
- Erhalten sie die Folgerungsbeziehung?
- Wie wird mit Logiken umgegangen, deren Semantik nicht dreiteilig ist?

**Nicht geprüft:**
- die genannten Literaturstellen (Fundstellen nicht eingesehen)
- spätere Fassungen (Logik-Tensor 2.0 liegt Claude nicht vor)
- ob es Vorfassungen mit derselben Formulierung gibt

**Ergebnis:** Ursprung und Datum sind **belegt**. Der Anspruch selbst ist **nicht belegt** und nach heutigem Stand **nicht prüfbar formuliert**.

---

## Fall H1-C-NEG

> „Der Logik-Tensor wurde am 21.03.2026 veröffentlicht und erstmals hat damit jemand Logiksysteme in einem gemeinsamen Rahmen verglichen.“

**Datierung: falsch.** Der Logik-Tensor 1.0 ist vom **28.03.2026** (Zenodo-Datensatz 19282895 und PDF-Fußzeile). Der 21.03.2026 ist das Datum zweier **anderer** Werke desselben Autors: *Tensor Basics* (10.5281/zenodo.19152183) und *Tensor Field Theory* (10.5281/zenodo.19153910). Wahrscheinlich ist das die Quelle der Verwechslung.

**„erstmals“: Ursprung gefunden, als Tatsache nicht haltbar.** Das Werk sagt selbst auf S. 14: „Der 3×3×3-Tensor ermöglicht es erstmals, alle diese Systeme … als kohärente Varianten … zu verstehen.“ Der Ursprung des Wortes ist also das Original. Gemeinsame Rahmen für Logikvergleiche gibt es aber schon länger (siehe Gegenbefunde bei H1-C-POS; nicht digital nachgeprüft). Haltbar wäre höchstens „erstmals in **dieser** dreiteiligen Darstellung“.

**Belegt:** richtiges Datum, Herkunft des Worts „erstmals“ (S. 14).
**Interpretation:** dass die Verwechslung vom Datum der Schwesterwerke stammt.
**Nicht geprüft:** Literaturstellen der älteren Rahmen.

**Ergebnis:** Die Behauptung ist **in zwei Teilen falsch bzw. nicht haltbar**. Der Negativfall wurde erkannt.

---

## Bewertung des Prompts H1 aus diesem Lauf

| Kriterium | Befund |
|---|---|
| Verständlich | ja, allgemeinverständlich |
| Ergebnisform | Die Trennung „belegt / Interpretation / offen / nicht geprüft“ funktioniert gut. |
| Schwäche | Kein festes Ausgabeformat und keine Statuswerte. Vergleiche zwischen Läufen werden dadurch schwer. **Vorschlag:** Ergebnisfelder `ursprung`, `datierung`, `originalquelle`, `fundstelle`, `gegenbefunde[]`, `belegt[]`, `interpretation[]`, `offen[]`, `nicht_geprueft[]`, `gesamturteil (belegt / teilweise / nicht_belegt / falsch)` |
| Risiko | Eine KI kann Gegenbefunde „aus Wissen“ nennen, ohne sie zu prüfen. Der Prompt sollte verlangen, solche Angaben als ungeprüft zu kennzeichnen (hier freiwillig getan). |
