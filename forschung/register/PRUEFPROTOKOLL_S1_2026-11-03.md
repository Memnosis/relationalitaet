# Prüfprotokoll S1 · Zenodo-Quellenregister und Quellenstatus-Schema

**Zyklus:** KI-2026-11-03-001 · **Schritt:** S1 (Claude) · **Bezug:** P0-X1, DATA-003, DR-03, DR-05, DR-06 · **Datum:** 2026-11-03
**Angekündigt in:** `CLAUDE_DISKUSSION_01.md` §5; GPT ohne Einwand (`GPT_DISKUSSION_01.md`)

## Erzeugte Dateien

| Datei | Inhalt |
|---|---|
| `QUELLEN_REFERENZSET_V0_1.json` | **öffentliches Referenzset**: nur die 3 freigegebenen Originalwerke (Logik-Tensor 1.0, Tensor-Basics, Feldtheorie) mit DOI, Concept-DOI, Version, Lizenz, MD5 (Zenodo), eigenem SHA-256 |
| *Gesamtregister (intern)* | aller Zenodo-Werke mit Versionen; **nicht in `main`** (Anweisung Nils, siehe Korrektur unten), Nils erhält es privat |
| `werkzeuge/zenodo_register.py` | erzeugt Gesamtregister (nur außerhalb des Repos, sonst Abbruch) oder Referenzset (`--referenzset`) reproduzierbar |
| `schema/vokabular.json` | alle Status-IDs in ASCII mit Anzeigetext (Quellenstatus, Evidenz D/F/O/K/B/offen, Aussageart, Redaktion, Vertraulichkeit, Alias-Typ) |
| `schema/claim.schema.json` | JSON-Schema 2020-12 für Aussagen, mit Bedingungsregeln |
| `schema/web-lesesicht.schema.json` | **Entwurf** der reduzierten öffentlichen Lesesicht für `docs/data/` (DR-06); GPT ergänzt die UI-Anforderungen (G3) |
| `pruefen.py` | Validator (Standardbibliothek, optional `jsonschema`) mit Selbsttest |
| `beispiele/CLAIMS_BEISPIELE_V0_1.json` | 6 echte Aussagen aus Zenodo-Originalen mit Seite/Zeile |
| `beispiele/CLAIMS_NEGATIV_V0_1.json` | 6 absichtlich ungültige Fälle |

## Ausgeführte Tests (tatsächlich gelaufen)

| Test | Befehl | Ergebnis |
|---|---|---|
| Download und Integrität | `python3 forschung/register/werkzeuge/zenodo_register.py --pruefen <tmp> --aus <privat>` | alle abgerufenen Dateien: Größe und MD5 stimmen |
| Schutz gegen Veröffentlichung | `… --aus forschung/register/TEST.json` ohne `--referenzset` | Abbruch mit Meldung, keine Datei geschrieben |
| Reproduzierbarkeit | zwei Läufe hintereinander, Vergleich der Record-IDs | identisch. Ohne feste Sortierung schwankte die Zenodo-Suche zwischen Läufen; behoben durch `sort=mostrecent` |
| Validator-Selbsttest | `python3 forschung/register/pruefen.py` (optional `QUELLEN_REGISTER=<privat>`) | 6/6 Beispiele gültig; 6/6 Negativfälle abgelehnt; JSON-Schema lehnt die 5 schema-prüfbaren Negativfälle ebenfalls ab; **OK** |
| Schema-Wohlgeformtheit | `jsonschema.Draft202012Validator.check_schema` | beide Schemas gültig |

## Befunde

1. **Lizenz:** alle geprüften Versionen CC-BY-4.0. Mehrere Werke haben mehrere Versionen (Versionsgraph im internen Register).
2. **Bytegleich in Git (löst einen Teil von DQ-004):** 4 PDFs im Hauptordner sind bytegleich mit veröffentlichten Zenodo-Dateien, u. a. `relationale-fraktale00.pdf` und `relationale-gravitation00.pdf`. „00“ bezeichnet also die veröffentlichte Fassung. `relationale-gravitation.pdf` ist eine andere Fassung (Zuordnung in S2).
3. **Logik-Pfad geprüft, kein Fehler:** `LM : PRJ : NM-I-γ → ZM-II-γ → UM-II-γ` in LOGIK_TENSOR_2_1 §5 entspricht dem Logik-Tensor 1.0 (S. 6, S. 13). Der abweichende `HM : PRJ …→ UM-III-γ` in der Feldtheorie gehört zur Holographie-Matrix.
4. **TM : RST** in der Feldtheorie ist laut Original (Zeile 170) eine bewusst neutrale Standardform und keine Inkonsistenz.

## Grenzen

- Status `digital_verifiziert` bei den Werken bezieht sich **nur** auf Abruf und Integrität der Dateien. Der Inhalt jedes Werks bleibt `pruefung_ausstehend` bzw. `nicht_geprueft` (DR-05).
- Die Vollständigkeit hängt vom Zenodo-Suchindex ab. Werke ohne den Autorennamen „Sautter, Nils“ werden nicht gefunden.
- Die Werkdateien liegen nicht in Git; die 4 bytegleichen Dateien waren schon vorher im Repository.
- Die Web-Lesesicht ist ein Entwurf; es gibt noch keinen Generator.

## Gegenprüfung durch GPT (Vorschlag)

D01, D02, D04 und D10 an diesen Dateien. Reproduktion: Selbsttest ausführen, eine Zenodo-DOI stichprobenartig öffnen und MD5 vergleichen, einen Negativfall abwandeln.

## Korrektur 2026-11-03 (Nils-Entscheidung)

Commit `6b50abe` hatte das **vollständige** Zenodo-Register als `QUELLEN_ZENODO_V0_1.json` auf `main` gelegt. Das widersprach der Anweisung in `ZYKLUS_001_ZENODO_RELEVANZ_STATT_GESAMTLISTE_2026-11-03.md` (Commit `e01670e`, fünf Minuten vor dem Push, von Claude zu spät gelesen). Nils hat entschieden: von `main` nehmen, privat übergeben.
- Die Datei ist aus dem aktuellen Stand von `main` entfernt. Sie bleibt in der Git-Historie (`6b50abe`); die Historie wird nicht umgeschrieben (Regel: nichts löschen, kein Force-Push).
- Ersatz: `QUELLEN_REFERENZSET_V0_1.json` mit den 3 freigegebenen Werken.
- Das Werkzeug verweigert künftig das Schreiben eines Gesamtregisters ins Repository.
- Das Beispiel `CLM-PROTEIN-908` (nicht freigegebene Quelle) wurde durch `CLM-LOGIK10-SYNTAX-CHURCH` ersetzt.
