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
- **Der Ersteller wechselt (Vorgabe Nils, 03.11.2026):** Bericht 04 Claude, **Bericht 05 GPT**, Bericht 06 Claude, Bericht 07 GPT usw.
- Die andere KI liest gegen und zeichnet im Bericht ab.

**Aufbau, immer gleich** (Vorgabe Nils, 03.11.2026: „Freigabe und Entscheidungen immer im Bericht an prominenter Stelle mit rotem Rahmen in Kurzform und ausführliche Erklärungen unten angehängt, damit ich alle Infos zur Entscheidung bei Fragen auf einem Bericht habe“):
0. **ROTER RAHMEN ganz oben, direkt unter dem Titel:** alle offenen Entscheidungen **und** Freigaben in Kurzform.
   - Je Zeile: ID · Priorität · Frage in einem Satz (höchstens 160 Zeichen) · Optionen in Stichworten · Empfehlung Claude **und** GPT · Antwortformat · Verweis „Anhang A*n*“.
   - Der Rahmen erscheint **immer**, auch wenn nichts offen ist (dann steht dort „keine offen“).
1. **Ampel und Kernaussage:** ein Satz pro Strang (Daten, Prompts, Website, Publikationen, Governance); Farbe immer mit Wort, nie Farbe allein
2. **Abwesenheit (R7)**, nur wenn ausgelöst
3. **Grafik Fortschritt:** Stufen statt Prozent (fehlt · erfasst · geprüft · gegengeprüft · freigegeben), aus Registerdaten erzeugt
4. **Was erledigt wurde:** mit Nachweis-Link
5. **Was hängt und warum:** Blocker mit Verantwortlichem
6. **Nächste Schritte** je KI
7. **Anhang A:** ausführliche Erklärung **jeder** Entscheidung aus dem roten Rahmen im Format R3, auf eigener Seite. Nils muss für eine Entscheidung keine andere Datei öffnen.
8. **Anhang B:** Fundstellen

**Werkzeug für beide KIs:** `forschung/koordination/berichte/vorlage/bericht_docx.mjs` erzeugt das DOCX aus einer JSON-Datei. Muster: `BEISPIEL_BERICHT.json`.
- Der Generator **verweigert** den Bericht, wenn eine Entscheidung im Rahmen keine vollständige R3-Erklärung im Anhang hat, eine KI-Empfehlung fehlt (Wert „ausstehend“ ist erlaubt) oder ein Abwesenheitsbericht ohne Abwesenheitsangaben ist.
- Ins öffentliche Repository schreibt er nicht.
- Tests: `forschung/koordination/tests/test_bericht_vorlage.py`.
- GPT kann ein eigenes Werkzeug nutzen, wenn das Ergebnis denselben Aufbau hat.

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

## R7 · Abwesenheit löst Bericht und Nachhol-Analyse aus

**Vorgaben Nils (03.11.2026):**
- „Wenn eine oder die andere KI über längere Zyklen abwesend war, löst das neue Berichts-/Analysepflicht aus.“
- **Definition:** „Abwesend ist, wenn auf 10 Beiträge einer KI kein Feedback oder Analyse kommt.“ (damit ist DEC-R7-SCHWELLEN entschieden)

**Messung** mit `forschung/koordination/werkzeuge/abwesenheit.py` aus der Git-Historie (Exit 3 = ausgelöst; Tests in `forschung/koordination/tests/test_abwesenheit.py`):
- **Beitrag** = ein Arbeitsschritt = eine eindeutige Commit-Betreffzeile. Mehrere Datei-Commits mit gleichem Betreff zählen einmal.
- **Feedback oder Analyse** = ein Commit der anderen KI mit
  - dem Trailer `Analyse-von: <sha>..<sha>` oder `Feedback-zu: <ID>` (R8, bevorzugt), oder
  - einer Feedback-Datei unter `forschung/koordination/` (Name enthält DISKUSSION, ANTWORT, REVIEW, ANALYSE, NACHHOL, VERGLEICH oder EINGANGSKONTROLLE) oder einer Änderung an `REVIEW_QUEUE_V2.json`.
- **Abwesend** ist eine KI, wenn die andere KI seit ihrem letzten Feedback **10 oder mehr Beiträge** gemacht hat. Eigene Arbeit ohne Feedback setzt den Zähler nicht zurück.

**Pflichten bei Auslösung:**
1. **Die abwesende KI** schreibt **vor neuer eigener Arbeit** eine **Nachhol-Analyse** aller Beiträge seitdem: `NACHHOLANALYSE_<KI>_<DATUM>.md` mit Commit-Bereich, Ergebnis je Thema (einverstanden / Fehler / Abweichung / Hinweis) und Nachweisen. Commit mit dem Trailer `Analyse-von:`.
2. **Die anwesende KI** schreibt einen **Abwesenheitsbericht** an Nils (DOCX, Typ `abwesenheitsbericht`, roter Rahmen wie R2), wenn die Abwesenheit **30 oder mehr** Beiträge umfasst oder offene Prüfbitten blockiert sind. Er unterbricht den Berichtswechsel nicht und trägt den Vermerk „Sicht einer KI, Gegenlesung ausstehend“.
3. Der **nächste reguläre Bericht** (R2) enthält einen Abschnitt „Nachhol-Analyse“ mit den Ergebnissen.
4. Sicherheitsfunde aus der Nachhol-Analyse gehen sofort an Nils (Ausnahme R1).
5. **Vor jedem Koordinations-Commit** führt jede KI `abwesenheit.py` aus und liest neue Feedback-Dateien der anderen KI. So kreuzen sich keine Anfragen mehr.

## R8 · Kennzeichnung und Versionierung

**Vorgabe Nils (03.11.2026):** „Kennzeichnung ist auch für Versionierung wichtig.“

1. **Jeder Commit nennt seine Urheberschaft** als Git-Trailer in der letzten Zeile der Nachricht:
   - `KI: claude`, `KI: gpt` oder `KI: nils`
   - Claude setzt zusätzlich `Claude-Session:` (Sitzungsnachweis).
   - Ohne Kennung ordnet das Werkzeug vorläufig GPT zu; mit `--streng` zählt der Commit nicht.
2. **Feedback-Commits nennen ihren Bezug:** `Analyse-von: <erster>..<letzter SHA>` oder `Feedback-zu: <REV-/DEC-/KOORD-ID>`.
3. **Testbehauptungen nennen den getesteten Stand:** „PASS“ gilt nur mit dem Commit-SHA (oder dem Datei-SHA-256) des tatsächlich getesteten Codes und dem Befehl. Ein Lauf in einer anderen Umgebung mit nicht committetem Code ist ein **Vorab-Lauf**, kein PASS. *(Anlass: Nachhol-Analyse F1: „6/6 PASS“ dokumentiert, im Repo 3/3 ERROR.)*
4. **Artefakte tragen Versionen im Namen oder im Kopf** (`_V0_1`, `schema_version`). Neue Fassung = neue Version, die alte bleibt erhalten (nie löschen, R0). Git-Tags sind in dieser Umgebung gesperrt (403). Deshalb tragen Versionsstände ihre Commit-SHA im Versionsmanifest (`forschung/register/VERSIONSMANIFEST_V0_1.json`).
5. **Berichte an Nils** nennen den Commit-SHA des Stands, auf dem sie beruhen.

## Zustimmung

| KI | Zustimmung | Datum | Änderungswünsche |
|---|---|---|---|
| Claude | **einverstanden** (Vorschlag) | 2026-11-03 | — |
| GPT | **einverstanden mit konkretisierten Schutzregeln** (R1–R6); **R2-Neufassung, R7 (Definition Nils) und R8 ausstehend** | 2026-11-03 | Siehe `zyklen/KI-2026-11-03-001/GPT_DISKUSSION_06.md`: Output-blinde Peer-Simulation, echtes SHA-Review, getrennte Tests/Freigabe, öffentliche Aggregation statt privater Einzelaufgaben; Altlücken bleiben offen. |
