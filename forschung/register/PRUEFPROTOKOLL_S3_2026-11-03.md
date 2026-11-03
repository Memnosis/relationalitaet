# Prüfprotokoll S3 · Formale Tests, Website-Review, Prompt-Inventar

**Zyklus:** KI-2026-11-03-001 · **Schritt:** S3 (Claude) · **Bezug:** P0-X4 (wissenschaftlicher Teil), Prüfvektoren W01–W10, X01 · **Datum:** 2026-11-03
**Angekündigt in:** `CLAUDE_DISKUSSION_01.md` §5; GPT ohne Einwand. Prompt-Inventar zusätzlich auf Bitte von GPT (`86fb9db`).

## Erzeugte Dateien

| Datei | Inhalt |
|---|---|
| `forschung/tensor/logik-claude/tests/test_formal_k4.py` | 8 Tests: Modus ponens mit Gegenmodell und Fehlschluss, Graph G (54/81 Kanten, Mittelschicht, Zentrum), ℤ₂₇ ≇ (ℤ₃)³ |
| `forschung/koordination/zyklen/KI-2026-11-03-001/CLAUDE_REVIEW_WEBSITE.md` | Review W01–W10 und X01 mit Blob-SHAs |
| `forschung/register/werkzeuge/prompt_export.py` | Inventar und verlustfreier bereinigter Export der Prompt-Felder (nur außerhalb des Repos) |
| `forschung/register/PROMPT_INVENTAR_V0_1.json` | Kennzahlen und Hashes der Prompt-Felder, **ohne Inhalte** |
| `forschung/register/schema/vokabular.json` | ergänzt um `prompt_freigabe` (approved/not_approved) und `prompt_ausfuehrung` (passed/failed/not_run), gleiche Werte wie in GPTs Website-Sperre |

## Tatsächlich ausgeführte Tests

| Test | Ergebnis |
|---|---|
| `python3 forschung/tensor/logik-claude/tests/test_formal_k4.py` | 8/8 bestanden |
| Mutationstest: 3 absichtlich eingebaute Fehler (falsche Implikation, falsche Nachbarschaft, falsche Gruppenordnung) | jeweils schlagen die passenden Tests fehl (2, 2 und 1 Fehlschläge); die Tests sind also nicht wirkungslos |
| Website-Review (eigenes statisches Skript, 21 Seiten) | siehe Review; 2 P0-Befunde |
| Prompt-Export: Schutz gegen Schreiben ins Repo | Abbruch, keine Datei geschrieben |
| Prompt-Export: Verlustfreiheit (MITMACH_TASKS.json) | gleiche Einträge und IDs; alle übrigen Felder identisch; jeder Hash-Verweis passt zum Originaltext |
| Originaldateien nach dem Export | unverändert (`git status` sauber) |
| Validator `pruefen.py` nach Vokabular-Ergänzung | OK |

## Grenzen

- Die Tests belegen nur die jeweils genannte mathematische Aussage. Sie belegen keine Tensor- oder Feldtheorie und nicht die „trinitäre Deduktion“ des Originals: Für diese gibt das Original keine formale Semantik an, mit der man sie prüfen könnte.
- Der Prompt-Test zu P0-X4 (derselbe Modus ponens als Prompt-Probelauf) folgt, sobald die Ausführungsakte für Prompts festgelegt ist.
- Die privaten Sicherungen und Exporte liegen im Arbeitsbereich von Claude und werden Nils übergeben.
