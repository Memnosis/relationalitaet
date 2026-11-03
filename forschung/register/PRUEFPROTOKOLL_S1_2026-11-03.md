# Prüfprotokoll S1 · Zenodo-Quellenregister und Quellenstatus-Schema

**Zyklus:** KI-2026-11-03-001 · **Schritt:** S1 (Claude) · **Bezug:** P0-X1, DATA-003, DR-03, DR-05, DR-06 · **Datum:** 2026-11-03
**Angekündigt in:** `CLAUDE_DISKUSSION_01.md` §5; GPT ohne Einwand (`GPT_DISKUSSION_01.md`)

## Erzeugte Dateien

| Datei | Inhalt |
|---|---|
| `QUELLEN_ZENODO_V0_1.json` | 65 Werke (Konzepte), 70 Versionen, 94 Dateien von Nils Sautter auf Zenodo; DOI, Concept-DOI, Version, Datum, Lizenz, MD5 (Zenodo), eigener SHA-256, bytegleiche Git-Dateien |
| `werkzeuge/zenodo_register.py` | erzeugt das Register reproduzierbar (Standardbibliothek + curl) |
| `schema/vokabular.json` | alle Status-IDs in ASCII mit Anzeigetext (Quellenstatus, Evidenz D/F/O/K/B/offen, Aussageart, Redaktion, Vertraulichkeit, Alias-Typ) |
| `schema/claim.schema.json` | JSON-Schema 2020-12 für Aussagen, mit Bedingungsregeln |
| `schema/web-lesesicht.schema.json` | **Entwurf** der reduzierten öffentlichen Lesesicht für `docs/data/` (DR-06); GPT ergänzt die UI-Anforderungen (G3) |
| `pruefen.py` | Validator (Standardbibliothek, optional `jsonschema`) mit Selbsttest |
| `beispiele/CLAIMS_BEISPIELE_V0_1.json` | 6 echte Aussagen aus Zenodo-Originalen mit Seite/Zeile |
| `beispiele/CLAIMS_NEGATIV_V0_1.json` | 6 absichtlich ungültige Fälle |

## Ausgeführte Tests (tatsächlich gelaufen)

| Test | Befehl | Ergebnis |
|---|---|---|
| Download und Integrität | `python3 forschung/register/werkzeuge/zenodo_register.py --pruefen <tmp> --aus …` | 94 von 94 Dateien: Größe und MD5 stimmen |
| Reproduzierbarkeit | zwei Läufe hintereinander, Vergleich der Record-IDs | identisch. Ohne feste Sortierung schwankte die Zenodo-Suche zwischen Läufen (68 statt 70 Records); behoben durch `sort=mostrecent` |
| Validator-Selbsttest | `python3 forschung/register/pruefen.py` | 6/6 Beispiele gültig; 6/6 Negativfälle abgelehnt; JSON-Schema lehnt die 5 schema-prüfbaren Negativfälle ebenfalls ab; **OK** |
| Schema-Wohlgeformtheit | `jsonschema.Draft202012Validator.check_schema` | beide Schemas gültig |

## Befunde

1. **Lizenz:** alle 70 Versionen CC-BY-4.0, Zeitraum 2026-02-16 bis 2026-09-04. Vier Werke haben mehrere Versionen.
2. **Bytegleich in Git (löst einen Teil von DQ-004):** `relational_fractals_002.pdf` (18816496), `relational_fractals_txt002.pdf` (18816408), `relationale-fraktale00.pdf` (18815450), `relationale-gravitation00.pdf` (18802386). „00“ bezeichnet also die veröffentlichte Fassung. `relationale-gravitation.pdf` ist eine andere Fassung (Zuordnung in S2).
3. **Logik-Pfad geprüft, kein Fehler:** `LM : PRJ : NM-I-γ → ZM-II-γ → UM-II-γ` in LOGIK_TENSOR_2_1 §5 entspricht dem Logik-Tensor 1.0 (S. 6, S. 13). Der abweichende `HM : PRJ …→ UM-III-γ` in der Feldtheorie gehört zur Holographie-Matrix.
4. **TM : RST** in der Feldtheorie ist laut Original (Zeile 170) eine bewusst neutrale Standardform und keine Inkonsistenz.

## Grenzen

- Status `digital_verifiziert` bei den Werken bezieht sich **nur** auf Abruf und Integrität der Dateien. Der Inhalt jedes Werks bleibt `pruefung_ausstehend` bzw. `nicht_geprueft` (DR-05).
- Die Vollständigkeit hängt vom Zenodo-Suchindex ab. Werke ohne den Autorennamen „Sautter, Nils“ werden nicht gefunden.
- Die Werkdateien liegen nicht in Git (nur Metadaten und Hashes); die 4 bytegleichen Dateien waren schon vorher im Repository.
- Die Web-Lesesicht ist ein Entwurf; es gibt noch keinen Generator.

## Gegenprüfung durch GPT (Vorschlag)

D01, D02, D04 und D10 an diesen Dateien. Reproduktion: Selbsttest ausführen, eine Zenodo-DOI stichprobenartig öffnen und MD5 vergleichen, einen Negativfall abwandeln.
