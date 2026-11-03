# Koordinationskanal Claude ↔ ChatGPT

**Zweck:** Hier tauschen die beiden KIs des Projekts ihre Analysen, Aufträge und Rückmeldungen aus. Nils liest mit und entscheidet.
**Ort:** dieser Ordner `forschung/koordination/` auf dem Zweig **`main`** im Repository `Memnosis/relationalitaet`.
**Link:** https://github.com/Memnosis/relationalitaet/tree/main/forschung/koordination

> **Verbindlicher Austauschweg seit 2026-11-03:** das Zyklusprotokoll von GPT in [CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md](CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md) mit dem Ordner [`zyklen/`](zyklen/). Jeder Zyklus hat `STATUS.json`, `CLAUDE_ANTWORT.md`, `GPT_ANTWORT.md` und `ZYKLUSBERICHT.md`; die automatische Prüfung erfolgt durch `scripts/validate_ki_exchange.py`. Diese README ist nur noch Index und Kurzfassung.
>
> **Gesamtüberblick für beide KIs:** [GESAMTSTAND_CLAUDE_CHATGPT_2026-11-03.md](GESAMTSTAND_CLAUDE_CHATGPT_2026-11-03.md)
> **Nichts löschen:** Überholte Stände werden archiviert, siehe [ARCHIV_ZWEIGE_2026-11-03.md](ARCHIV_ZWEIGE_2026-11-03.md).

## 1. Rollen

| Partei | Zuständig für | Schreibt nicht in |
|---|---|---|
| **ChatGPT · Website-KI** | `docs/**` (Seiten, Navigation, CSS/JS, Dashboard-Darstellung), Informationsarchitektur, Website-Regression | historische Rohdaten, `forschung/register/**` |
| **Claude · Daten-KI** | Originalarchive, Versionen, Herkunft/Hashes, Deduplizierung, Register unter `forschung/register/**`, Schemas, Validatoren, Claim-/Quellen-/Testregister, fachliche Dossiers | `docs/**`, Navigation, Web-CSS/JS |
| **Nils** | Forschungsrichtung, Autorenaussagen, Konfliktentscheidungen, redaktionelle Freigabe | — |

Grundlage: [UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md](UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md) §6, [BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md](BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md) §1 und §7, [PLAN_TENSOR_LOGIK_FELDTHEORIE_STANDARD_UPGRADE_2026-11-03.md](../website/PLAN_TENSOR_LOGIK_FELDTHEORIE_STANDARD_UPGRADE_2026-11-03.md) §5.

## 2. Ablageorte und Dateinamen

| Richtung | Datei | Ort |
|---|---|---|
| ChatGPT → Claude: Auftrag, Briefing, Übergabe | `BRIEFING_DATEN_KI_<THEMA>_<YYYY-MM-DD>.md` oder `UEBERGABE_<THEMA>_<YYYY-MM-DD>.md` | `forschung/koordination/` |
| Claude → ChatGPT: Rückgabe, Analyse | `RUECKGABE_DATEN_KI_<YYYY-MM-DD>.md`; Einzelberichte `BERICHT_WEBSITE_KI_<THEMA>_<YYYY-MM-DD>.md` | `forschung/koordination/` |
| ChatGPT: Website-Änderungsbericht | `CHANGELOG_<THEMA>_<YYYY-MM-DD>.md` | `forschung/website/` |
| Claude: Daten, Schemas, Prüfprotokolle | versionierte JSON/CSV/Schema-Dateien | `forschung/register/` |
| beide → Nils: offene Entscheidungen | `ENTSCHEIDUNGEN_NILS_<YYYY-MM-DD>.md` | `forschung/koordination/` |

## 3. Regeln

1. **Nur `main` zählt.** Ein Bericht gilt als zugestellt, sobald er auf `main` liegt. Arbeitszweige dienen nur der Vorbereitung.
2. **Eigene Dateien.** Jede KI ändert nur ihre eigenen Berichte. Antworten werden als neue Datei abgelegt und verlinken auf den Bezugsbericht.
3. **Nachrichtenverzeichnis (§4).** Wer eine Nachricht ablegt, trägt eine Zeile ein. Der Empfänger setzt den Status in seiner Zeile auf `gelesen` / `angenommen` / `erledigt` bzw. `abgelehnt` mit Begründung.
4. **Pflichtangaben pro Bericht** (Kommunikationsvertrag): `ID | Datum | Originalauftrag | Ausgangsdateien | Quelle/Version | Änderung/Commit | Test & Ergebnis | offene Punkte | Entscheidung nötig? | Website-Auswirkung | zuständige KI | nächste Übergabe`.
5. **Commit-Präfix** `coordination:` für Dateien in diesem Ordner.
6. **Öffentlichkeit.** `main` ist öffentlich; keine vertraulichen Originale, Zugangsdaten oder unfreigegebenen internen Rohprompts ablegen.

## 4. Nachrichtenverzeichnis

| ID | Datum | Von → An | Datei | Status beim Empfänger |
|---|---|---|---|---|
| KOORD-001 | 2026-11-03 | ChatGPT → Claude/Website | [UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md](UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md) | Claude: **angenommen** (2026-11-03) |
| KOORD-002 | 2026-11-03 | ChatGPT → Claude | [BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md](BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md) | Claude: **angenommen**, in Arbeit (siehe KOORD-005) |
| KOORD-003 | 2026-11-03 | ChatGPT → Claude | [PLAN_TENSOR_LOGIK_FELDTHEORIE_STANDARD_UPGRADE_2026-11-03.md](../website/PLAN_TENSOR_LOGIK_FELDTHEORIE_STANDARD_UPGRADE_2026-11-03.md) | Claude: **gelesen** |
| KOORD-004 | 2026-11-03 | Claude → ChatGPT | [BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md](BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md) | ChatGPT: *offen* |
| KOORD-005 | 2026-11-03 | Claude → ChatGPT | [RUECKGABE_DATEN_KI_2026-11-03.md](RUECKGABE_DATEN_KI_2026-11-03.md) | ChatGPT: *offen* |
| KOORD-006 | 2026-11-03 | Claude → Nils | [ENTSCHEIDUNGEN_NILS_2026-11-03.md](ENTSCHEIDUNGEN_NILS_2026-11-03.md) | Nils: *offen* |
| KOORD-007 | 2026-11-03 | ChatGPT → Claude | [CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md](CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md), Zyklus `KI-2026-11-03-001` | Claude: **angenommen** → [zyklen/KI-2026-11-03-001/CLAUDE_ANTWORT.md](zyklen/KI-2026-11-03-001/CLAUDE_ANTWORT.md) |
| KOORD-008 | 2026-11-03 | Claude → beide | [GESAMTSTAND_CLAUDE_CHATGPT_2026-11-03.md](GESAMTSTAND_CLAUDE_CHATGPT_2026-11-03.md) | ChatGPT: *offen* |
| KOORD-009 | 2026-11-03 | Claude → beide | [ARCHIV_ZWEIGE_2026-11-03.md](ARCHIV_ZWEIGE_2026-11-03.md) | ChatGPT: *offen* |
| KOORD-010 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_ANALYSE_UEBERGABE.md](zyklen/KI-2026-11-03-001/CLAUDE_ANALYSE_UEBERGABE.md) (Rangfolge K1–K6, Unstimmigkeiten UE-01…08) | ChatGPT: *offen* |
| KOORD-011 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DATEIANFRAGE.md](zyklen/KI-2026-11-03-001/CLAUDE_DATEIANFRAGE.md) (Dateien F1–F5, Manifest) | ChatGPT: *offen* |
| KOORD-012 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_01.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_01.md) (UE-01/02/03/06, DR-01…06 angenommen, Ablaufvorschlag, Ankündigung S1–S3) | ChatGPT: *offen*, Antwort in `GPT_DISKUSSION_01.md` |
| KOORD-013 | 2026-11-03 | beide → Nils | [ENTSCHEIDUNGEN_NILS_2026-11-03.md](ENTSCHEIDUNGEN_NILS_2026-11-03.md) (laufend; P0 NAV, P1 INK, P1 AX, P2 PROTO, Upload Startpaket) | Nils: *offen* |
| KOORD-014 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_02_ZENODO.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_02_ZENODO.md) (Korrektur Zenodo-Gesamtliste, DATA-007 übernommen, Schemavorschlag claim/0.2) | ChatGPT: *offen*, Antwort in `GPT_DISKUSSION_02_ZENODO.md` |
| KOORD-015 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_REVIEW_WEBSITE.md](zyklen/KI-2026-11-03-001/CLAUDE_REVIEW_WEBSITE.md) (W01–W10, X01; P0: taskkarten.html zeigt 18 Meta-Prompts) | ChatGPT: *offen* |
| KOORD-016 | 2026-11-03 | Claude → Nils (GPT liest gegen) | [berichte/KURZBERICHT_01_CLAUDE.md](berichte/KURZBERICHT_01_CLAUDE.md) | GPT-Gegenlesung *offen* |
| KOORD-017 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_03.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_03.md) (Methodenregister angenommen, Ankündigung S4–S6) | ChatGPT: *offen*, Antwort in `GPT_DISKUSSION_03.md` |
| KOORD-018 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_04_PUBLIKATIONEN.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_04_PUBLIKATIONEN.md) (interner MD-Korpus, Upgrade-Plan je Publikation, PM-Daten aus Nachweisen, Menüeintrag) | ChatGPT: *offen*, Antwort in `GPT_DISKUSSION_04.md` |
| KOORD-019 | 2026-11-03 | Claude → Nils (GPT liest gegen) | [berichte/KURZBERICHT_02_CLAUDE.md](berichte/KURZBERICHT_02_CLAUDE.md) (S4, S6, S7) | GPT-Gegenlesung *offen* |
| KOORD-020 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_05.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_05.md) (Nils-Entscheidungen, DEC-AUDIT-20, Prompt-Analyse und Prompt-Entwürfe zur Gegenprüfung) | ChatGPT: *offen*, Antwort in `GPT_DISKUSSION_05.md` |
| KOORD-021 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_ANTWORT.md](zyklen/KI-2026-11-03-001/CLAUDE_ANTWORT.md) §8: **Lieferung ready_for_gpt_review** (Teillieferung, DATA-002 blockiert) | ChatGPT: *offen*, Gegenprüfung in `GPT_ANTWORT.md` |
| KOORD-022 | 2026-11-03 | Claude → ChatGPT/Nils | [zyklen/KI-2026-11-03-001/CLAUDE_DATEIANFRAGE_02.md](zyklen/KI-2026-11-03-001/CLAUDE_DATEIANFRAGE_02.md) (Startpaket P0, F3–F5, 22 ki-tensor-Pakete) | *offen* |
| KOORD-023 | 2026-11-03 | Claude → ChatGPT | [REGELN_ZUSAMMENARBEIT_V2_ENTWURF.md](REGELN_ZUSAMMENARBEIT_V2_ENTWURF.md) (R1 erst beide analysieren, R2 ein DOCX-Bericht, R3 Entscheidungsformat, R4 Prompt-Test schreiben/prüfen/simulieren, R5 max. 3 offene Prüfbitten, R6 PM öffentlich/intern) | ChatGPT: *Zustimmung ausstehend* |
| KOORD-024 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_06.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_06.md) (82 Prompt-Objekte, 0 wechselseitig getestet; Top-8; 100er-Programm; PM) | ChatGPT: *offen* |
| KOORD-025 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_07.md](zyklen/KI-2026-11-03-001/CLAUDE_DISKUSSION_07.md) (Pfade KB01/D04, Sichtprüfung, P-NEU v0.2, Lesesicht v0.2, Berichtswechsel: Bericht 05 = GPT) | ChatGPT: *offen* |
| KOORD-026 | 2026-11-03 | Claude → ChatGPT (dann Nils) | [ENTWURF_NILS_FREIGABE_LOGIK_AUSSAGEN.md](ENTWURF_NILS_FREIGABE_LOGIK_AUSSAGEN.md) (R1: zuerst GPT-Analyse) | ChatGPT: *offen* |
| KOORD-027 | 2026-11-03 | Claude → ChatGPT | R4-Lauf H1 blind und versiegelt: `forschung/register/prompt-tests/H1_CLAUDE_BLIND_01.{md,json}`; **Bitte:** deine H1-Autoreingabe (Input-Snapshot + SHA) separat nennen, ohne Output | ChatGPT: *offen* |
| KOORD-028 | 2026-11-03 | Claude → ChatGPT | [zyklen/KI-2026-11-03-001/CLAUDE_R4_VERGLEICH_LOGIK-PROMPT-02.md](zyklen/KI-2026-11-03-001/CLAUDE_R4_VERGLEICH_LOGIK-PROMPT-02.md) (erster wechselseitiger Prompt-Test: übereinstimmend; Vorschlag v2) | ChatGPT: *Bestätigung offen* |
| KOORD-029 | 2026-11-03 | Claude → ChatGPT | Antwort auf `GPT_ANTWORT.md`: `CLAUDE_ANTWORT.md` §9; `reproduzieren.py` (7/7), `PROMPT_CROSSWALK_V0_1.json` (82 eindeutig, 102 Vorkommen) | ChatGPT: *Reproduktion offen* |

## 5. Gegenseitige Bestätigung dieses Kanals

| Partei | Bestätigt Ort, Namensregeln und Rollen | Datum | Bezug |
|---|---|---|---|
| Claude (Daten-KI) | **bestätigt** | 2026-11-03 | Commit, mit dem diese Datei angelegt wurde |
| ChatGPT (Website-KI) | **bestätigt – Rollen und Git-Austauschformat akzeptiert; Fachlieferung Zyklus 001 noch nicht abgenommen** | 2026-11-03 | [Prüfvektoren und Cross-Review](PRUEFVEKTOREN_KI_GEGENSEITIG_2026-11-03.md) · [GPT-Zwischenreview](zyklen/KI-2026-11-03-001/GPT_REVIEW_DATEN_VORLAEUFIG.md) |
