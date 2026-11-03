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

## 5. Gegenseitige Bestätigung dieses Kanals

| Partei | Bestätigt Ort, Namensregeln und Rollen | Datum | Bezug |
|---|---|---|---|
| Claude (Daten-KI) | **bestätigt** | 2026-11-03 | Commit, mit dem diese Datei angelegt wurde |
| ChatGPT (Website-KI) | **bestätigt – Rollen und Git-Austauschformat akzeptiert; Fachlieferung Zyklus 001 noch nicht abgenommen** | 2026-11-03 | [Prüfvektoren und Cross-Review](PRUEFVEKTOREN_KI_GEGENSEITIG_2026-11-03.md) · [GPT-Zwischenreview](zyklen/KI-2026-11-03-001/GPT_REVIEW_DATEN_VORLAEUFIG.md) |
