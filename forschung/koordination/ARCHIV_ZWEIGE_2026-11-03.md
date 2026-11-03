# Archiv · Zweige und Sicherungskopien — Stand 2026-11-03

**Regel von Nils:** Es wird nichts gelöscht, weder Dateien noch Zweige noch Tags. Jeder Zweig wird zusätzlich durch einen **Archivzweig** `archiv/<zweig>-2026-11-03` gesichert, der auf denselben Commit zeigt. Archivzweige werden nie weiterbewegt, gelöscht oder überschrieben. Unveränderliche Git-Tags konnten aus der Claude-Sitzung nicht angelegt werden (HTTP 403 beim Tag-Push). Nils oder GPT können sie mit denselben Namen nachtragen.

Angelegt von: Claude (Daten-KI). Wiederherstellen eines Standes: `git checkout archiv/<name>-2026-11-03`. Übersicht auf GitHub: https://github.com/Memnosis/relationalitaet/branches/all?query=archiv

| Zweig | Commit | Letzter Stand | Inhalt | Status | Archivzweig |
|---|---|---|---|---|---|
| `main` | `f3ca054` | 2026-11-03 | Hauptstand, Website über GitHub Pages | aktiv | `archiv/main-2026-11-03` |
| `integration/soulution-shared-core-2026-11-03` | `62ee8e5` | 2026-11-03 | 160 Commits: Inkubator, Register, Piloten, Skills, 12 Seiten, CI | aktiv, nicht in `main`; siehe KOORD-004 | `archiv/integration-soulution-shared-core-2026-11-03` |
| `ki-tensor/no-loss-audit-2026-10-31` | `cf0bbe1` | 2026-10-31 | 48 Commits: Audits v3.9–v6.9, DLMF-Pipeline | aktiv, nicht in `main`, konfliktfrei übernehmbar | `archiv/ki-tensor-no-loss-audit-2026-11-03` |
| `koordination/daten-qualitaet` | `4dddbd3` | 2026-11-03 | erste Fassung des Merge-Berichts; Inhalt identisch auf `main` als `BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md` | überholt, archiviert | `archiv/koordination-daten-qualitaet-2026-11-03` |
| `Trinity_Database` | `2109d35` | 2026-03-11 | Upload-Stand März | historisch | `archiv/Trinity_Database-2026-11-03` |
| `eeg` | `3ec712c` | 2026-03-12 | Upload-Stand März (identisch mit Tag `csv`) | historisch | `archiv/eeg-2026-11-03` |
| `trinity-database-phi` | `e47335e` | 2026-03-14 | 1 eigener Upload | historisch, nicht in `main` | `archiv/trinity-database-phi-2026-11-03` |
| `relational-metrology` | `7afaa21` | 2026-03-16 | 1 eigener Upload | historisch, nicht in `main` | `archiv/relational-metrology-2026-11-03` |
| `power-spect` | `b73e884` | 2026-03-18 | 1 eigener Upload | historisch, nicht in `main` | `archiv/power-spect-2026-11-03` |

Bereits vorhandenes Tag: `csv` → `3ec712c` (unverändert).

**Nicht im Repository** (nur bei Nils bzw. in der ChatGPT-Konversation): No-Loss-Archive v15.4, v17.3, v4.2, `codebuch_vereint_v40.sqlite`, Logik-Tensor 1.0 (PDF), Tensor-Basics, Tensor 2.0, Feldtheorie-Original, Logik-Tensor-2.0-Manuskript (MD/DOCX/PDF). Für diese Dateien wird ein privater Archivort empfohlen. `main` ist öffentlich.
