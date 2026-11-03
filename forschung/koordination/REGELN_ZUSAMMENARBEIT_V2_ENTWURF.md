# Regeln der Zusammenarbeit Claude ↔ GPT · v2 · ENTWURF zur Einigung

**Stand:** 2026-11-03 · **Vorgeschlagen von:** Claude · **Auftrag Nils (03.11.2026):** „macht das unter euch aus bzw. analysiert erst beide, bevor Auftrag oder Bericht an mich“, „Berichte vereinheitlichen und grafisch aufpeppen“, „Fragen an mich und offene Entscheidungen immer mit genug Infos“.
**Gilt ab:** Zustimmung beider KIs (GPT trägt unten ein). Ergänzt und ersetzt nichts Bestehendes stillschweigend; betroffen sind README §3, `RHYTHMUS_3_3_9_12…`, `PRUEFVEKTOREN…` und `PROGRAMM_100_ZYKLEN…`.

## R1 · Erst beide analysieren, dann Nils

1. **Kein Auftrag, Bericht oder Entscheidungswunsch an Nils**, bevor **beide** KIs den Inhalt analysiert haben.
2. Ablauf:
   - Die erste KI legt einen Entwurf ab: `ENTWURF_NILS_<THEMA>.md`.
   - Die zweite KI analysiert ihn innerhalb ihrer nächsten Runde und vermerkt `einverstanden` / `abweichend: …`.
   - Bei Uneinigkeit klären die KIs **untereinander**, höchstens 2 Runden.
3. **An Nils geht nur:**
   - was nur ein Autor entscheiden kann (Inhalt, Veröffentlichung, Richtung)
   - oder was die KIs nach 2 Runden nicht einig werden
4. **Ausnahmen ohne gemeinsame Vorprüfung:**
   - Sicherheitsvorfälle, z. B. versehentlich Veröffentlichtes
   - reine Bitten um Dateien
   - direkte Antworten auf eine Frage von Nils; diese tragen den Vermerk „Sicht einer KI, Gegenlesung ausstehend“

## R2 · Ein Bericht, ein Format (DOCX)

**Gemeinsamer Bericht** nach je 3 Schritten bzw. nach jedem vollen Zyklus: **einer** statt zwei getrennter Berichte.
- Der Ersteller wechselt.
- Die andere KI liest gegen und zeichnet im Bericht ab.

**Aufbau, immer gleich:**
1. **Ampel und Kernaussage:** ein Satz pro Strang (Daten, Prompts, Website, Publikationen, Governance)
2. **Grafik Fortschritt:** Stufen statt Prozent (fehlt · erfasst · geprüft · gegengeprüft · freigegeben), aus Registerdaten erzeugt
3. **Was erledigt wurde:** mit Nachweis-Link
4. **Was hängt und warum:** Blocker mit Verantwortlichem
5. **Entscheidungen für Nils** im Format R3
6. **Nächste Schritte** je KI
7. **Anhang:** Fundstellen

**Gestaltung:** serifenlose Schrift (Textstandard v1), Farben nach validierter Palette, jede Grafik mit Textalternative (Tabelle).

## R3 · Entscheidungsvorlagen für Nils: genug Information

Jede Frage an Nils enthält:

| Feld | Inhalt |
|---|---|
| Worum geht es? | zwei bis drei Sätze ohne Fachjargon |
| Warum jetzt? | was blockiert ist oder was droht |
| Optionen | 2 bis 4, je mit **Folgen** (was passiert danach, was kostet es, was ist nicht mehr möglich) |
| Empfehlung | **von beiden KIs**, getrennt, wenn sie verschieden sind |
| Wenn nicht entschieden | was dann passiert |
| Antwortformat | z. B. „KT: a“ |
| Hintergrund | Link zur Analyse |

## R4 · Prompts: einer schreibt, der andere prüft und simuliert

Für jeden Prompt, der freigegeben werden soll:

| Schritt | Wer | Ergebnis |
|---|---|---|
| 1 Schreiben | Autor-KI | Prompt mit ID, Version, Ein- und Ausgabevertrag, Positiv- und Negativfall |
| 2 Eigenlauf | Autor-KI | Ausführungsakte (Input-Hash, Output-Hash, Tests, Grenzen) |
| 3 Analyse | Gegen-KI | Bewertung nach D08 und W07/W08, **ohne** den Eigenlauf zu kennen |
| 4 Simulation | Gegen-KI | **unabhängige** Ausführung mit demselben Input-Snapshot und eigene Akte |
| 5 Vergleich | beide | Übereinstimmung, Abweichungen, Ursachen; danach eine neue Prompt-Version, falls nötig |
| 6 Vorlage | beide | gemeinsamer Freigabevorschlag an Nils (R3) |

**Status-Werte:** `not_run` → `owner_run` → `peer_reviewed` → `peer_simulated` → `compared` → `approved` (nur Nils). Damit gilt ein Prompt erst dann als **wechselseitig getestet**, wenn Schritt 4 vorliegt.

## R5 · Obergrenze für offene Aufträge

- Jede KI hat **höchstens 3 offene Prüfbitten** an die andere.
- Neue Aufträge an die andere KI erst, wenn deren offene Prüfbitten beantwortet sind. Ausnahme: Sicherheitsvorfälle.
- **Prüfbitten gehen vor neuen eigenen Aufträgen.** Eine ausstehende Gegenprüfung blockiert den Zyklus; ein neuer Auftrag tut das nicht.

## R6 · Projektmanagement: öffentlich und intern getrennt

| Ebene | Inhalt | Ort |
|---|---|---|
| Öffentlich (`docs/data/projektmanagement-*.json`) | öffentliche Aufgaben mit Stufen; interne Aufgaben **nur als Summe** (z. B. „12 interne Aufgaben, 5 geprüft“); Prompts nur mit `public_release = approved` mit Text, sonst nur ID, Titel und Teststatus | Website (GPT) |
| Intern für Nils | alle Aufgaben, Prompts, Archive, Blocker, Entscheidungen, Grafiken | gemeinsamer DOCX-Bericht (R2), privat übergeben; kein öffentliches Git |
| Erzeugung | Stufen werden **aus Nachweisen erzeugt** (Prüfprotokolle, Testregister, `STATUS.json`), nicht von Hand gepflegt | Generator Claude, Darstellung GPT |

## Zustimmung

| KI | Zustimmung | Datum | Änderungswünsche |
|---|---|---|---|
| Claude | **einverstanden** (Vorschlag) | 2026-11-03 | — |
| GPT | *ausstehend* | | |
