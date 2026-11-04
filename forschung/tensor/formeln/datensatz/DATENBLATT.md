# Datenblatt · Formelbestand v0.1

## Zweck
Ein maschinenlesbarer Bestand definierender Formeln aus Wikidata. Jede Formel ist auf Größen abgebildet und für strukturelle Analysen aufbereitet: Stelligkeit, Trinitäten, Exponentenvektoren, Ministrukturen (Skelette), Bezugskanten und Bezugstensoren. Der Bestand ist für weitere Analysen und Berechnungen gedacht, z. B. Elimination, Dimensionsprüfung, Graphanalysen und Lernverfahren.

## Herkunft und Lizenz
- **Quelle:** Wikidata, <https://www.wikidata.org>. Datenlizenz **CC0 1.0** (gemeinfrei).
- **Auswahl:** alle Items mit definierender Formel (P2534) und mindestens einem Symbol (P7235), das über den Qualifikator P9758 („Symbol steht für“) auf eine Größe verweist.
- **Abrufzeitpunkt:** steht in `groessen_v0_1.json` → `abgerufen_am`.
- **Erzeugung:** `abruf_wikidata.py <ordner>` (Rohabruf), danach `bauen.py <ordner>/wikidata_roh.json` (Datensatz) und `../dschungel.py` (Analysen). Rohabruf und Datensatz sind deterministisch, abgesehen vom Stand von Wikidata zum Abrufzeitpunkt.

## Dateien

| Datei | Format | Inhalt |
|---|---|---|
| `formelbestand_v0_1.jsonl` | JSON Lines, eine Formel je Zeile | siehe Felder unten |
| `groessen_v0_1.json` | JSON | Größe (QID) → Bezeichnung de/en, ISQ-Dimension (P4020), Konstante ja/nein, Vorkommen |
| `skelette_v0_1.json` | JSON | Ministruktur-Kennung → kanonisches Skelett, Anzahl, Formeln |
| `trinitaeten_v0_1.csv` | CSV | alle Formeln mit genau drei Größen: Typ (multiplikativ / additiv / dynamisch / andere / nicht gelesen), Signatur, Größen |
| `bezugstensoren_v0_1.json` | JSON | Bezugstensoren: Schließungs-Trinität der Operatoren, Zeilen, Belegung |
| `ergaenzungen_v0_1.csv` | CSV | aus Bezugstensoren vorhergesagte, im Bestand fehlende Formeln, mit Art (parallel/Kette) und Dimensionsprüfung |
| `rollenpruefung_v0_1.csv` | CSV | fachliches Urteil je Vorhersage (korrekt / bedingt / ohne Bedeutung), Familie, Begründung; ein Prüfer |
| `abruf_wikidata.py`, `bauen.py` | Python | Erzeugung |

### Felder in `formelbestand_v0_1.jsonl`

| Feld | Bedeutung |
|---|---|
| `id` | Wikidata-QID des Items |
| `name_de`, `name_en` | Bezeichnung |
| `formel_tex` | erste definierende Formel mit Gleichheitszeichen (TeX) |
| `formeln_tex` | alle definierenden Formeln (TeX) |
| `symbole` | Liste {symbol (TeX), groesse (QID)} |
| `groessen` | nicht konstante Größen (QIDs) |
| `konstanten` | Naturkonstanten und mathematische Konstanten (QIDs) |
| `stelligkeit` | Anzahl der Größen; `trinitaer` = (stelligkeit == 3) |
| `parse` | `ok` / `fehler` / `ohne_gleichung` |
| `ausdruck` | SymPy-Gleichung als Text; Größen heißen `G_<QID>`, Konstanten `K_<QID>`; nicht zugeordnete Symbole behalten ihren Namen |
| `ausdruck_srepr` | dieselbe Gleichung verlustfrei (`sympy.srepr`), wieder einlesbar |
| `exponenten` | bei Monomgleichungen (Potenzgesetzen): {`G_<QID>`: Exponent} der Form Σ aᵢ·log Xᵢ = konst; Ableitungen dY/dX zählen als Y·X⁻¹ |
| `skelett` | Kennung der Ministruktur (siehe `skelette_v0_1.json`) |
| `symbole_zugeordnet` | Anteil der freien Symbole, die einer Größe oder Konstante zugeordnet sind |

## Einlesen

```python
import json, sympy as sp
Z = [json.loads(l) for l in open("formelbestand_v0_1.jsonl", encoding="utf-8")]
f = next(z for z in Z if z["id"] == "Q29539")              # Dichte
gl = eval(f["ausdruck_srepr"], vars(sp))                    # SymPy-Gleichung
```

## Bekannte Grenzen
- **Parser:** Ein Teil der TeX-Formeln ist für `sympy.parsing.latex` nicht lesbar (Quote in der Zusammenfassung). Vektoren und Tensoren werden als Skalare gelesen, Satzauszeichnung (Fettdruck, Pfeil) wird entfernt.
- **Zuordnung:** Symbole ohne Eintrag in P7235 bleiben unzugeordnet, z. B. oft die Zeit `t` in Ableitungen.
- **Konstanten:** werden über eine feste Liste und über die Bezeichnung („Konstante“, „constant“) erkannt.
- **Auswahlverzerrung:** Wikidata bildet vor allem Größen nach ISO/IEC 80000 ab; Mathematik, Ökonomie und Sozialwissenschaften sind unterrepräsentiert.
- **Rollen:** Gleiche QID heißt nicht gleiche Rolle (z. B. Masse eines Körpers vs. Zentralmasse). Strukturelle Befunde sind deshalb Kandidaten, keine fachlichen Aussagen.
