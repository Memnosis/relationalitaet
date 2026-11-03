# Prüfprotokoll S4 · Validierungsprofile nach Standards und Prioritätenliste

**Zyklus:** KI-2026-11-03-001 · **Schritt:** S4 (Claude) · **Bezug:** Methodenregister §6 Claude-P0, STD-D01/D02/D04/D05/S02, SK-PRIORITY · **Datum:** 2026-11-03
**Angekündigt in:** `CLAUDE_DISKUSSION_03.md`; GPT hat nicht widersprochen.

## Erzeugte und geänderte Dateien

| Datei | Inhalt |
|---|---|
| `profile/profile_pruefen.py` | 9 maschinell prüfbare Mindestkriterien: FAIR F1, F2, I1, R1.1, R1.2; PROV wasAttributedTo und wasGeneratedBy; SemVer; DCAT-Trennung intern/öffentlich. Dazu eine Negativprobe. |
| `PRIORITAETEN_CLAUDE_V0_1.json` | 12 Aufgaben, 8 Dimensionen auf Skala 0–3, Claude-Gewichtung, 4 Sortierungen (gewichtet, Dringlichkeit, Hebel/Blocker, sofort machbar) |
| `QUELLEN_REFERENZSET_V0_1.json`, `PROMPT_INVENTAR_V0_1.json`, `logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json`, `beispiele/CLAIMS_BEISPIELE_V0_1.json` | um Werkzeug- und Zeitangaben ergänzt (Lücken aus der Erstprüfung); Erzeuger angepasst, damit die Angaben künftig automatisch entstehen |
| `VERSIONSMANIFEST_V0_1.json` | neu erzeugt am aktuellen Stand (181 Dateien) |

## Tests

| Test | Ergebnis |
|---|---|
| Erstlauf über 6 Register | 4 mit Lücken. 1 davon war ein Fehler im Prüfskript (Aussagen wurden über die Quellen-ID gezählt), behoben. 3 echte Lücken: fehlende Werkzeugangabe (3×) und fehlender Zeitstempel (1×), in den Erzeugern behoben. |
| Zweitlauf über 7 Register (inkl. Prioritätenliste) | 7/7 erfüllen alle 9 Kriterien |
| Negativprobe (Register ohne IDs, doppelte IDs, unbekannter Status, interner Datensatz, falsches Versionsformat) | 9/9 Kriterien korrekt **nicht** erfüllt |
| `pruefen.py` (Claims) nach den Änderungen | OK |

## Nicht geprüft (`not_assessed`)

- SHACL: keine RDF-Daten
- FAIR-A1: Abrufbarkeit externer Links, keine Netzprüfung
- ISO/IEC 25010 und NIST AI RMF: nicht maschinell prüfbar

**Ein bestandenes Kriterium heißt „Mindestanforderung erfüllt“, nicht „normkonform“.**

## Prioritäten aus Claude-Sicht (gewichtet)

1. DEC-NAV-01 · 2. DEC-PROMPT-01 · 3. Tensor 2.0 an Claude · 4. Projektstände aus Nachweisen erzeugen · 5. No-Loss-Archive an Claude · 6. Achsen-Crosswalk DATA-002

Sofort machbar ohne weitere Zuarbeit: DEC-PROMPT-01, DEC-KT-01, FRAGE-LOGIK-100 (je eine Antwort von Nils).
