# Rückgabe Daten-KI (Claude) an ChatGPT/Website — 2026-11-03

| Feld | Inhalt |
|---|---|
| ID | KOORD-005 |
| Datum | 2026-11-03 |
| Bezug | KOORD-001 Übergabe Achsensysteme · KOORD-002 Briefing Daten-KI · KOORD-003 Website-Plan |
| Quelle/Version | `main` @ `f3d6754` |
| Änderung/Commit | nur Koordinationsdateien; keine Änderung an `docs/` oder an Originaldaten |
| Entscheidung nötig? | ja, siehe [ENTSCHEIDUNGEN_NILS_2026-11-03.md](ENTSCHEIDUNGEN_NILS_2026-11-03.md) |
| Zuständige KI | Claude (Daten), ChatGPT (Website) |
| Nächste Übergabe | ChatGPT bestätigt Kanal in [README.md](README.md) §5 und meldet Status zu KOORD-004 |

## 1. Empfangsbestätigung

- **KOORD-001 und KOORD-002 angenommen.** Claude bearbeitet keine Dateien unter `docs/`, keine Navigation und kein Web-CSS/JS. Lieferungen erfolgen nach Briefing §7: `forschung/koordination/RUECKGABE_DATEN_KI_*.md`, `forschung/register/…`, `forschung/tensor/…` und `forschung/koordination/ENTSCHEIDUNGEN_NILS_*.md`.
- **KOORD-003 gelesen.** Die Datenschnittstelle aus Plan §5 wird eingehalten: Ändert Claude Datenverträge, wird das vorher hier angekündigt.
- **Kanal festgelegt:** [README.md](README.md) in diesem Ordner. Bitte dort in §5 bestätigen.

## 2. Bereits gelieferte Analyse

**KOORD-004:** [BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md](BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md)

Es geht um das Zusammenführen des Zweigs `integration/soulution-shared-core-2026-11-03` (160 Commits) in `main`.
- Es gibt 16 Konfliktseiten, verursacht durch einzeilig minifiziertes HTML und zwei parallele Navigationsskripte (`tensor-hierarchy.js` aus `main`, `site-nav.js` aus dem Zweig).
- Vier Abschnitte, die nur in `main` stehen, müssen erhalten bleiben: `#forschungswege`, `#prompt-freigabe`, `#prompt-ebenen` und `#algebra-weiterentwickeln`.
- Betrifft Plan-Paket **W0**: Navigation einschließlich `tensor-paper.html`. Im Zweig ist `tensor-paper.html` bereits an `site-nav.js` angeschlossen.

## 3. Erste Datenqualitätsbefunde (`main` @ `f3d6754`)

| ID | Befund | Wirkung auf Website |
|---|---|---|
| DQ-001 | Die Zahl der Aufgaben widerspricht sich: `forschung/register/README.md` nennt 24 Aufgaben-IDs, die Steuerungsmatrix 40 Familien, die Freigaberegeln und `GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json` 44 (`record_count`). | `projektstand.html` und `mitmachen.html` sollten bis zur Bereinigung **keine** dieser Zahlen als festen Wert zeigen. |
| DQ-002 | Das Glossar existiert in drei Fassungen: 1.008 (historische Zwischenfassung), 1.072 (v15.4, laut B3/B4 maßgeblich) und 12 Begriffe in `docs/data/glossar-kern.json`. Die Beziehung zwischen den Fassungen ist nicht maschinenlesbar dokumentiert. | `glossar.html` bezieht sich auf die 12er-Kernauswahl; ihre Herkunft soll angegeben werden, sobald das Versionsregister vorliegt. |
| DQ-003 | `dashboard/data/inventar.json` und `docs/data/inventar.json` sind bytegleiche Kopien ohne festgelegte Hauptquelle. | Künftig nur eine Quelle; die andere wird erzeugt. |
| DQ-004 | Dateinamen im Hauptordner ohne Versionsangabe bzw. mit Upload-Suffix: `rel-bio-recherche3 (3).md`, `trinity algebra.md`, `relationale-gravitation00.pdf`, `relationale-fraktale00.pdf`, `trinity_matrix_database_final.csv`. `Information Relational.md` und `information-relational.md` sind zwei unterschiedliche Fassungen desselben Texts. | Keine Umbenennung ohne Weiterleitung und Crosswalk; zuerst Versionsregister. |
| DQ-005 | Alle 10 JSON-Dateien sind syntaktisch gültig. Es gibt keine echten doppelten IDs; Mehrfachvorkommen in `GESAMTPROJEKT_…json` sind `origin`-Verweise. Es fehlen Schemas und ein Validator. | — |

## 4. Nächste Schritte der Daten-KI (Reihenfolge nach Briefing §8)

1. Versions- und Herkunftsregister aller Repository-Dateien: Pfad, SHA-256, Fassung, Vorgänger, Sprache, Status. Ohne Umbenennung und ohne Fusion.
2. Schemas für die Register und ein Validator; DQ-001 bis DQ-003 werden als Prüfregeln umgesetzt.
3. Briefing §8, Punkte 1–5: Achsenversionen A/B/C gegen G, Logik-Tensor-Belege, Feldtheorie-Claim-Audit, P0-Dossiers und Standardschema TENSOR-FIELD 0.1.

Hinweis: Historische Archive (v15.4, v17.3, v4.2 sowie die SQLite-Datenbank `codebuch_vereint_v40.sqlite`) liegen **nicht** im Repository. Claude kann sie erst prüfen, wenn Nils sie bereitstellt. Bis dahin werden nur die Git-Bestände bearbeitet.
