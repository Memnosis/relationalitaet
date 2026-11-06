# g30 – Entwurf der ausführenden Geo-, Feld- und Tensorengine

**Status:** Architekturvertrag v0.1 · 2026-11-06 · *nicht implementiert*, außer ausdrücklich erwähnten Bestandsteilen. **Name:** g30 (vorläufig; "0" = Ziffer Null am Ende).

## 0. Ziel und Prüfgegenstand

g30 führt **typisierte Objekte** (Zahl, Größe mit Einheit, algebraischer Ausdruck, Vektor, geometrischer Träger, Graph, formale Rolle, Aussage mit Quellbeleg) auf **versionierten Pfaden** durch Feldadressen innerhalb von Tensoren und über deklarierte **Tensorbrücken**. Die Engine protokolliert jeden Schritt mit Rolle, Versionsstand, Voraussetzungen, Operatortyp, Herkunft, Beweis-/Evidenzstatus, Invertierbarkeit und Verlust. Sie erzeugt bei Bedarf CAD/SVG/A4-Darstellungen, ohne grafische Metaphern als Fachbeweis auszugeben.

**Unterscheiden:** die Indexbewegung der 27 Adressen; die tatsächliche mathematische Funktion; die semantische Umdeutung; die geometrische Einbettung; die Zeit-/Prozessänderung; den Wechsel von Gesamtordnungen (O1–O6). Das sind verschiedene Operationen mit verschiedenen Verträgen.

## 1. Bestandsanker (zu importieren, nicht ersetzen)

- `forschung/geoki/v0_4/src/geometry.py`: 13 Python-Funktionen, darunter Rotation, Translate, Reflect, Scale, Affine, Bézier, Flächen- und Eulerberechnung. 2D-Kern, keine allgemeine CAD-/Topologieengine.
- `forschung/tensor/algebra-claude/typalgebra.py`: 27er-Adressierung, Pfadsignaturen, typisierte PRJ/RST/CYC/REC, Vergleich und Überlagerung. Pfadtypen sind **nicht** bereits Semantik-Interpreter. Besondere Vorsicht: CYC = Klasse-II-Adresspfad; nicht automatisch geschlossener Umlauf.
- `forschung/tensor/formeln/DREIECKE_V0_1.json`: zwei erfolgreiche/bedingte Ableitungen, eine fachlich ungültige Kombination wegen Rollenverwechslung.
- `forschung/tensor/kandidaten/KAND-LUHMANN-01_v0_1.json`: 27 Arbeitsfragen, **keine 27 freigegebenen Operatoren**.
- `forschung/tensor/kandidaten/KAND-LUHMANN-01_WELTEN_DONOR_CROSSWALK_v0_1.json`: drei neue 27er-Kandidatenwelten und indexbezogene Tests, Semantiktransfers offen.
- `docs/data/geo-tensor-icon-stamps-v0-1.json`: Formen-, Operator- und Evidenzstempel.
- `forschung/register/BESTANDSWEGWEISER.md`: Altarchive und Importgrenzen.

## 2. Modularchitektur

| Modul/Package | Aufgabe | Kernfunktion (geplant) |
|---|---|---|
| `g30.core` | Typisierung und Werte | `Value`, `Quantity`, `Expression`, `Claim`, `Shape`, `TypedRelation` |
| `g30.registry` | versionierter Korpus | `load_tensor`, `load_source`, `validate_manifest` |
| `g30.address` | 3×3×3-Feldcodierung | `encode/decode`, `trinity_groups`, `axis_permute` |
| `g30.operators` | ausführbare Funktionen | `precondition`, `apply`, `inverse`, `loss`, `postcondition` |
| `g30.formula` | symbolische Algebra/Einheiten | `solve`, `substitute`, `eliminate`, `dimension_check` |
| `g30.geometry` | 2D/3D/Graphen | `rotate`, `affine`, `project`, `measure`, `topology_check` |
| `g30.graph` | adressierte Relations-/Hypergraphen | `neighbors`, `hyperedge`, `find_typed_paths` |
| `g30.scheduler` | Zustandsmaschine/Workflow | `plan`, `step`, `branch`, `join`, `stop`, `budget` |
| `g30.transfer` | Wechsel zwischen Tensoren | `bridge_typecheck`, `transport`, `compare`, `roundtrip` |
| `g30.evidence` | Prüf- und Quellakte | `record_input/output`, `counterexample`, `hash_trace` |
| `g30.render` | CI/CAD-Ausgaben | `svg`, `dxf`, `a4`, `icon`, `animation_frames` |
| `g30.api` | JSON-API/CLI | `run`, `validate`, `explain`, `export` |

**Ausführungsvertrag:** `step(value, operator, context) -> {outcomes[], status, trace, guard_results, evidence_refs, reversibility, information_loss}`. Mehrdeutige Inversion liefert mehrere Kandidaten oder Fehler, niemals heimliche Auswahl. Eine interaktive Zeichnung ist eine Projektion des Zustands, nicht die Quelle des fachlichen Wahrheitsstatus.

## 3. Minimale maschinenlesbare Objekt-Signatur

```json
{
  "run_id": "g30-run-demo-001",
  "tensor": {"id": "FACH-F011", "version": "frozen-import"},
  "address": "NM-I-α",
  "payload": {
    "kind": "quantity",
    "value": 12,
    "unit": "m",
    "quantity_kind": "distance",
    "role_id": "distance-of-the-same-motion",
    "context_id": "motion-001"
  },
  "operation": {
    "id": "divide-by-duration",
    "version": "0.1",
    "requires": [
      {"role_id": "duration-of-the-same-motion", "value": 3, "unit": "s"}
    ],
    "output_quantity_kind": "average_speed",
    "output_unit": "m/s",
    "guard": ["same_motion", "nonzero_duration", "dimension_consistency"],
    "status": "engine_example_not_field_licensed"
  },
  "candidate_target": {"tensor_id": "FACH-F011", "address": "NM-I-β"},
  "evidence": {"source_ids": [], "field_rule_verified": false}
}
```

**WICHTIG:** Die Adresse in diesem Beispiel ist ein willkürliches Formatbeispiel; keine tatsächliche Operation ist durch FACH-F011/NM-I-α bereits genehmigt. Im realen Lauf ist daher `field_rule_verified=false` ein **hartes STOP/UNVERIFIED**, außer in einem explizit gekennzeichneten Sandbox-Modus.

### Typen für eine Aussage über ein Feld

`SOURCE_TEXT` → `FIELD_ROLE_CANDIDATE` → `OPERATOR_SPECIFIED` → `TESTED_MATH` → `SEMANTICALLY_VALIDATED` → `RELEASED` (separate Achsen, keine automatische lineare Hochstufung). Ein mathematisch wahrer Ausdruck genügt nicht zur fachlichen Freigabe.

## 4. Definition einer Tensorbrücke

Eine Brücke verbindet `(Quell-Tensor@Version, Feld/Rolle, Datentyp)` mit `(Ziel-Tensor@Version, Feld/Rolle, Datentyp)` und benennt:
- explizite Typkonversion und fachliche Rollenzuordnung;
- Quelle/Autoren und Voraussetzungen;
- ob es Identität, Isomorphie, Teilabbildung, Analogie oder lediglich Visualisierung ist;
- was erhalten bleiben soll (Einheit, Relation, Invariante, Semantik) und was verloren gehen darf;
- definierte Rückabbildung oder deren Unmöglichkeit;
- qualifizierte Prüfakte plus Gegenbeispiel.

**Keine automatische Übertragung** zwischen Luhmann-Verstehen, Peirce-Interpretant und mathematischen Größen. Keine Kantenkomposition über unbekannte Einheiten/Rollen.

## 5. Datenhaltung und Quellen

**Start:** Git als versioniertes No-Loss-Quellarchiv + SQLite als lokaler, reproduzierbarer Arbeitsindex mit JSON-Funktionen und FTS5. TSV/CSV/JSON/JSONL als Import/Export, JSON Schema Draft 2020-12 als Validierung. **Optional später:** Parquet/DuckDB für Korpusstatistik; Graphdatenbanken erst bei gemessenen Engpässen.

Tabellen/Collections (stabile Schlüssel + Version): `source`, `author`, `citation`, `glossary_term`, `tensor`, `trinity`, `field`, `expression`, `quantity_type`, `unit`, `operator`, `operator_binding`, `relation`, `hyperedge`, `bridge`, `test_case`, `test_result`, `run`, `run_step`, `proof_record`, `asset`, `version_link`.
- Historische IDs nicht überschreiben, sondern über `version_link` / Herkunft nachziehen.
- `operator_binding` verknüpft die **eine geprüfte ausführbare Regel** mit **einem** Feld/Kontext. `field` allein ist nie ausführbar.
- Wissenschaftliche Quellbelege mit DOI/URL, Herausgeber/Autor, Jahr, Abschnitt/Seite, Quellentyp, Lizenz, Abruf-/Archivdatum. Zitataussagen vs Paraphrase unterscheiden.
- Provenienz als `entity`, `activity`, `agent` im Sinne W3C PROV-O (2013).
- Gesonderter `status` je Aussage, mathematischem Satz, Übertragung, Bildobjekt und Test.

## 6. Testserie – Vorschlag mit überprüfbaren Freigabekriterien

| Gate | Gegenstand | Kandidaten / Freigabekriterium |
|---|---|---|
| T00 | No-Loss-Import und Revisionskette | alle bestandsmäßig verfügbaren Akten importiert; SHA-/Versionscheck; keine stillen Überschreibungen |
| T01 | 3×3×3-Adressen | 27 einzigartige Adressen, bidirektionale Zuordnung, keine unerlaubte Rollentauschung |
| T02 | Formeln und Größen | Dimensions- und Einheitenprüfungen, Nullnenner, Definitionsbereiche, Rollenkollisionen |
| T03 | Geo-Kern | Referenztests + numerische Toleranzen + Sonderfälle: Kollinearität, degenerierte Segmente, Singularität |
| T04 | Operatoren | Typkontrakt, Vor-/Nachbedingungen, gleiches Ergebnis bei Wiederholung gleicher Eingabe |
| T05 | Vorwärts- und Rückweg | invertierbare Funktionen: roundtrip; nichtinvertierbare: ausdrücklich `LOSS` |
| T06 | Pfadalgebra | Ende=Anfang, Pfadkomposition, erlaubte Schleife, Terminierung, Erreichbarkeit |
| T07 | Tensorbrücken / Ordnungswechsel | keine automatische Übertragung; sechs O1–O6-Ordnungstypen und Grenzmarkierung |
| T08 | Dreiecksalgebra | P=F·v gültig unter Annahmen, Dichte-Spezialfall, Pendel–Kepler–BMI zwingend `REJECT` |
| T09 | Luhmann / Semantik | 27 Quellfragen übernommen; Verstehen ≠ Zustimmung, Interpretation ≠ physikalischer Operator |
| T10 | Renderer | 27 Inhalte auf A4, saubere Druckränder, keine 3×3×3→4×4-Grafik, SVG/DXF-Adressgleichheit |
| T11 | Performance | Benchmark P50/P95 für Feldschritt, 27-Schritt, 100-Tensor-Brückenindex, 10.000-Schritt-Pfad, Peak-RAM |
| T12 | Missbrauch/Robustheit | untrusted JSON, Code-Injection, zyklische Workflows, begrenzte Rechenzeit und Speicher, sichere Formel-Parser |
| T13 | No-Loss-Publikation | durchgehende Kette Quelle→Feld→Operator→Test→Trace→Grafik→Publikation |

**Zielumfang für erste Entwicklungsrunde:** mindestens 150 reproduzierbare Prüfbeispiele, aufgeteilt auf alle Gates; nicht als bereits bestanden ausgeben. Für Eigenschaftstests Hypothesis (inverse, Metamorphie, Typinvarianten); pytest für Regression; zusätzliche unabhängige Vergleichswerte bei Rechenalgorithmen.

**Performance:** keine versprochenen absoluten Millisekunden ohne Messung; zuerst Benchmark-Hardware, kalte/warme Läufe und Eingabedichte dokumentieren. Aussage "alle finalisierten Tensoren" nur nach Prüf-Freigabe je fachlicher Bindung.

## 7. Entwicklungsreihenfolge

**M0 – No-loss & Loader:** Inventar samt Originalversionen importieren, prüfen, Statusfelder.  
**M1 – Single-field MVP:** eine definierte Formel als typisierten Schritt einschließlich Begründung/Trace ausführen.  
**M2 – 27-address runtime:** Pfadsuche und freigegebene Operatorverkettung, Stop-/Branch-/Merge-Regeln.  
**M3 – Geo-CAD:** bestehende 2D-Operationen plus stabiles Rendering und Messungen.  
**M4 – Dreiecks- und Rubikprüfung:** Rückwege, Kommutatoren, verlorene Rollen, negativ validierte Formeldreiecke.  
**M5 – Cross-tensor transfer:** erstmals eine **fachlich geprüfte** Brücke zweier ausgereifter Tensoren; keine reine Indexvertauschung als Erfolg melden.  
**M6 – Lern- und A4-Drucksystem:** 27 Feldkarten und neun Trinitätskarten aus denselben überprüften Daten.  
**M7 – Leistung und Korpusharvest:** Regression auf alle geeigneten, validierten Bestände, Benchmarks und Erweiterbarkeit.

## 8. Externe Standards / Bibliotheken (begründete Auswahl)

- JSON Schema 2020-12: https://json-schema.org/draft/2020-12/
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- SQLite JSON und FTS5: https://www.sqlite.org/json1.html und https://www.sqlite.org/fts5.html
- SymPy (Gleichungslöser): https://docs.sympy.org/latest/modules/solvers/solvers.html
- Hypothesis: https://hypothesis.readthedocs.io/en/latest/
- CGAL Robustheitsprinzip / exakte Prädikate: https://www.cgal.org/exact.html

## 9. Kritische Grenzen

1. 27 Feldpositionen sind keine zwingend 27 voneinander unabhängigen Grundformeln.
2. Viele Geometrieformen können aus wenigen Operationen generiert werden; ihre **semantische Interpretation** benötigt fachliche Modelle und Transferbelege.
3. Beliebige Formeln nie mit `eval` aus Nutzereingaben ausführen; nur geprüfte Operator-AST/Registry mit Ressourcenlimits.
4. Ein Graph der paarweisen Kanten erhält keine irreduzible Dreierrelation ohne Hyperkanten- und Rollenmetadaten.
5. Projektion 3D→2D oder 27→9 verliert häufig Information; Inversion wird zur mehrdeutigen Rekonstruktion und darf nicht automatisch als eindeutig markiert werden.
6. „Bedeutung verändert sich bei der Feldbewegung“ ist eine *modellgebundene Regel*, keine intrinsische Eigenschaft von Koordinaten.
