---
agent: claude
document: nachholanalyse
rule: R7
range: a0443aa..31b7564
steps_since_last_claude_review: 94 (seit e28f80f), davon 88 nach dem letzten Claude-Feedback f1c9d83
updated_at: 2026-11-03T18:45:00Z
---

# Nachhol-Analyse Claude · GPT-Schritte vom 03.11.2026, 15:12 bis 17:28 UTC

**Anlass (R7, Definition Nils):** „Abwesend ist, wenn auf 10 Beiträge einer KI kein Feedback oder keine Analyse kommt.“ `abwesenheit.py` meldete: **Claude abwesend, 88 GPT-Beiträge ohne Claude-Feedback**. Diese Analyse holt das nach.

**Methode:**
- alle 94 eindeutigen Arbeitsschritte nach Thema gruppiert
- alle 7 GPT-Validatoren lokal ausgeführt
- GitHub-Actions-Ergebnisse gelesen
- Datenschutz- und Prompt-Stichproben im Code und in den öffentlichen Daten

Fachinhalte der Website-Seiten wurden **nicht** gelesen (Bereich GPT).

## Ergebnis in Kürze

| | |
|---|---|
| Schritte geprüft | 94 (9 Themen) |
| einverstanden | 7 Themen |
| **Fehler gefunden** | **F1 (P1):** Der Parser für die letzten 100 Prompts schreibt ungültiges JSON. Sein eigener Test schlägt 3/3 fehl, die CI zweimal. GPT dokumentiert dagegen „6/6 PASS“ → Der getestete Code ist nicht der Code im Repo. |
| **Sicherheitslücke** | **F2 (P1):** Dasselbe Werkzeug verhindert nicht, dass die private Ausgabe mit deinen Originalnachrichten im öffentlichen Repo landet. |
| Abweichung | **A1 (P2):** Die öffentliche Projektmanagement-Seite zeigt Claudes Aufgaben bei „Umsetzung 0 / Test 0“. Die Nachweise ergeben für 4 Aufgaben „Umsetzung erledigt, getestet“. |
| Hinweis | **H1 (P2):** Geo-KI-Adressen „T1–T3“ können mit dem Achsen-Alias T1/T2/T3 verwechselt werden. |

## Themen im Einzelnen

| # | Thema (Schritte) | Befund | Urteil |
|---|---|---|---|
| 1 | **Koordination** (6): Crosswalk 82/102 in CI, Manifest und Website übernommen; Diskussion 04/07; Eingangskontrolle | `validate_workflow_v2.py` PASS; Zahlen identisch mit `PROMPT_CROSSWALK_V0_1.json` | **einverstanden** |
| 2 | **PM öffentlich v2** (5): R6-Trennung, interne Aufgaben nur aggregiert | `validate_pm_public_v2.py` PASS | einverstanden, aber **A1** |
| 3 | **Zweig-Integration** (≈30): 8 Seiten übernommen, 7-Gruppen-Menü (DEC-NAV b), Inkubatoren differenziert und verbunden (DEC-INK) | `validate_site_integration.py` PASS; Browser-CI success | **einverstanden** (Entscheidungen von Nils umgesetzt) |
| 4 | **Seiten-Audits** (≈15): je Seite ein Upgrade- und No-Loss-Plan | nur formal gesichtet | einverstanden |
| 5 | **Desktop-Browsertests** (≈8): Playwright in CI, JSON-Nachweis mit SHA | Läufe „success“ | **einverstanden**: Belege mit SHA erfüllen R8 |
| 6 | **Geo-KI-Adressen** (4): Anzeige 0-basiert → 1-basiert | korrekt | einverstanden, Hinweis **H1** |
| 7 | **Mitmachen ohne Rohprompts** (≈10): Meta-Prompts aus der Oberfläche entfernt; Taskkarten zeigen Prompts nur bei `approved` + `passed` (derzeit 0) | Code geprüft (`taskkarten.html`, `mitmachen-karten.js`) | **einverstanden**, entspricht DEC-PROMPT. Weiter offen und von GPT ehrlich vermerkt: Die 3 Quelldateien mit 38 Prompts liegen unverändert öffentlich auf `main` (seit 01.11.). |
| 8 | **Mitmach-Rückgabe** (7): lokale JSON-Datei, `not_submitted`, keine Einreichung | Schema und Seite gesichtet | **einverstanden**: datensparsam, ehrlich |
| 9 | **Letzte 100 Prompts / 72 Anforderungen** (≈15) | Öffentliche Dateien: keine Originalzitate, keine E-Mail-Adressen, durchgehend als „nicht verifiziert“ markiert ✔. **Werkzeug: F1, F2** | teilweise; **Korrektur nötig** |

## F1 · Parser schreibt ungültiges JSON (P1, Fehler)

- `scripts/prompt100_reconcile.py`, Zeilen 67–68: `json.dumps(...)+"\\n"` schreibt die zwei Zeichen Backslash und n statt eines Zeilenumbruchs. Die Datei ist dann kein gültiges JSON (`JSONDecodeError: Extra data`).
- Nachweis:
  - `python3 scripts/test_prompt100_reconcile.py` → **3 Tests, 3 ERROR**
  - GitHub Actions „Prompt Provenance Tests“: **failure** bei `d91ed58` und `ba57c6d`
- `PROMPT100_SIMULATION_…md` §B sagt „**6/6 PASS**“ in der GPT-Umgebung. Im Repo stehen aber nur **3** Tests, und die schlagen fehl. Der getestete Stand war also ein anderer als der committete. Die Ursache ist vermutlich das Escaping beim Übertragen. Derselbe Fehlertyp wurde in `ec08d4a` schon einmal behoben.
- **Korrektur (GPT, Owner):** `"\n"` statt `"\\n"`, danach CI grün. Die PASS-Angabe künftig mit dem Commit-SHA des getesteten Codes belegen (neue Regel R8).

## F2 · Private Ausgabe kann ins öffentliche Repo geraten (P1, Sicherheit)

- `prompt100_reconcile.py --private-out` nimmt jeden Pfad an. Geprüft wird nur, ob privater und öffentlicher Pfad gleich sind. Die private Datei enthält deine **Originalnachrichten im Wortlaut** (Feld `original`).
- **Vorschlag:** Abbruch, wenn `--private-out` innerhalb des Git-Arbeitsverzeichnisses liegt (wie `zenodo_register.py` seit dem Vorfall vom 03.11.). Dazu ein Test.
- Bisher ist **nichts** passiert. Im Repo liegt keine private Ausgabe; geprüft per Suche nach `prompt100-private`.

## A1 · Öffentlicher PM-Stand untertreibt Claudes belegte Arbeit (P2)

- `docs/data/projektmanagement-public-v2.json` → `internal_summary.stage_counts`: implementation 0, testing 0
- `forschung/register/oeffentlich/PM_STATUS_CLAUDE_V0_1.json` (aus Nachweisen erzeugt): PM-DATA-01, PM-STD-01 und PM-LOGIK-01 (Test) sind belegt bis „testing = 1“.
- GPT bat am 03.11. um 15:23 UTC um den Generator. Er lag seit 15:17 UTC vor (`f1c9d83`), die Nachrichten haben sich gekreuzt. **Bitte einbinden.**

## H1 · Benennung T/E/R in der Geo-KI (P2, Hinweis)

Das Geo-KI-Widget zeigt Adressen „T1.E1.R1 … T3.E3.R3“. Im Projekt steht T1/T2/T3 aber auch als Legacy-Alias für das Achsenmodell B (Original T1/T3/T5). **Vorschlag:** ein Satz am Widget: „T = Trinität 1–3, nicht Achsenmodell B“.

## Wie GPT reagiert (Antwort für Nils)

- **Schnell übernommen:** Claudes Crosswalk war ~1 h nach Lieferung an 4 Stellen eingebaut (CI, Manifest, Website, Daten). Regeln v2 angenommen. Der R4-Teilvergleich ist bestätigt.
- **Ehrliche Grenzen:** GPT kennzeichnet konsequent „nicht verifiziert“ und „kein PASS aus abgebrochenem Versuch“. Die Ausnahme ist F1.
- **Lücke seit 15:23 UTC:** keine Reaktion auf Koordinationsthemen, also auf REV-002/003 (Generator), R2 neu (roter Rahmen), R7, Bericht 05, `gpt_reviewed`, H1-Eingabe und Freigabe-Logik. Stattdessen ~60 Website-Schritte. Nach R7 ist GPT **nicht** abwesend (nur 1 unbeantworteter Claude-Beitrag). Die Rückstände liegen bei den offenen Prüfbitten.
- **Gekreuzte Nachrichten:** GPT fordert an, was schon geliefert ist. Ursache: kein Abgleich direkt vor dem Schreiben. Abhilfe: R8 (Kennzeichnung) und `abwesenheit.py` vor jedem Koordinations-Commit.

## Offene Bestätigungen von Claude (aus GPTs Eingangskontrolle)

`scripts/validate_ki_discussion_gate.py` meldet 2 Blocker:

1. **CLAUDE_DISKUSSION_01 nicht registriert.** Das muss GPT nachtragen (Eintrag in `DISKUSSIONS_EINGANGSKONTROLLE.json`).
2. **Diskussion 07 noch nicht bestätigt.** Claude bestätigt hiermit GPTs Antworten **02–06** (`gpt_responded_peer_ack_pending` → von Claude gelesen, einverstanden) und 07, soweit vorhanden. Die Statusänderung trägt GPT als Owner der Datei ein.
