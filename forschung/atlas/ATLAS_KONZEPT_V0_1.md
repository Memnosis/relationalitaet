# Begriffsatlas · Konzept v0.1

## Wozu

Die Grundlagenwerke zu **Null (Rel0)**, **Einheit (Rel1)**, **Zyklus (Rel-Rel)** und **Trinität** enthalten zusammen über tausend Begriffe aus allen Wissenschaften. Jeder Begriff ist dort einer Klasse, einer Subklasse und einer Domäne zugeordnet. Der Atlas führt diese Listen in **einer** Datenbank zusammen und macht sie verfeinerbar:
- Querbezüge zwischen den Polen sichtbar machen (derselbe Begriff als Null und als Einheit),
- historische Quellen anhängen,
- Begriffe auf Tensoradressen abbilden,
- Größen mit dem Formelbestand und den Fixsternen verknüpfen.

## Bestand nach dem Import v0.1

| Werk | Pol | Einträge |
|---|---|---|
| Null-Matrix (18.02.2026) – Register mit Quellen und Jahr | Rel0 | 170 |
| Null-Matrix (25.02.2026, DE) | Rel0 | 314 |
| Null-Matrix (25.02.2026, EN) | Rel0 | 312 (an die DE-Einträge als Übersetzung angehängt) |
| EINheits-Matrix (12.03.2026) | Rel1 | 333 (davon 56 mit Primärquelle und DOI) |
| Matrix der Trinität (12.03.2026) | Trinität | 100 (50 Dualismen mit B / I / E, 15 Strukturerweiterungen, 35 Themen mit Status) |
| Zyklus-Matrix (20.03.2026) | Rel-Rel | 100 (mit Tensorkoordinate) |
| **Summe** | | **1.329 Einträge, 944 verschiedene deutsche Begriffe** |

## Datensatz je Begriff (`daten/begriffe_v0_1.jsonl`)

`uid, werk, werk_titel, doi, id, zeile, pol, sprache, begriff, begriff_en, domaene, subklasse, abschnitt (Klasse), beschreibung, beschreibung_en, quelle, jahr, primaerquelle, referenz, koordinate (Zyklus), pol_baseline / pol_identitaet / pol_emergenz (Trinität), status, korrigiert`

## Ausbaustufen

| Stufe | Inhalt | Stand |
|---|---|---|
| A0 | Import der Listen, Herkunft je Eintrag | **erledigt** (v0.1) |
| A1 | Begriffsnormalisierung: Synonyme, DE/EN, Schreibvarianten; ein Begriff, mehrere Fundstellen | offen |
| A2 | Polübergreifende Verknüpfung: derselbe Gegenstand als Null, Einheit, Zyklus (bisher 4 exakte Treffer, z. B. Fixpunkt, Shannon-Entropie, Strange Loop, terminales Objekt) | begonnen |
| A3 | Geschichte: Erstbeleg (Person, Jahr, Werk, DOI/ISBN) je Begriff | 170 + 56 Einträge haben bereits Quellen |
| A4 | Tensoradresse (M, K, S) je Begriff; Abgleich mit der Zyklus-Koordinate | Zyklus-Matrix hat Koordinaten |
| A5 | Verknüpfung mit Wikidata-Größen (Formelbestand) und Fixsternen | offen |
| A6 | Website-Atlas (GPT): Suche, Filter nach Pol, Klasse, Domäne; Begriffskarte | offen |

## Regeln

- **Mindeststandard:** Kein Eintrag der Originallisten wird gelöscht. Korrekturen werden als neue Felder ergänzt; der Originalwert bleibt erhalten.
- **Zählungen** kommen immer aus der Datenbank, nie aus dem Fließtext.
- **Erzeugung:** `python3 forschung/atlas/import_begriffe.py <md_korpus> forschung/atlas/daten` (Korpus lokal; ohne Korpus: SKIP).
