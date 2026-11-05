# KI-Tensor · CI/CAD Feld- und Semantik-Drucksprache v0.1

**Status:** Druckfähiger Forschungsprototyp (A4 hochkant, exakt zwei Seiten). **Referenz:** T-SOZ / Soziation, 27 erfasste Quellbegriffe. **Kein** Beleg dafür, dass jedes Feld bereits eine mathematische Operation oder geometrische Form besitzt.

## Layoutvertrag

- **Seite 1 – Feldatlas:** 27 Positionen als **flaches rechteckiges 3×9-Koordinatenfeld** (drei Schichtzeilen NM, ZM, UM; je neun Felder in Reihenfolge I-α, I-β, I-γ, II-α … III-γ). Darunter eine Karte zu Ganzheit, Quellen und Evidenz; darunter Feldindex mit allen 27 Quellbezeichnungen.
- **Seite 2 – Tensor-Semantik:** drei **nebeneinanderstehende 3×3-Matrizen**, je eine für NM, ZM, UM. Zeilen I/Kern, II/Kreislauf, III/Öffnung; Spalten α/Struktur, β/Funktion, γ/Relation. Direkt darunter drei Semantikkarten, dann Beispiel der Feld-/Operator-Code-Sprache und die Statuslegende.
- **A4-typografischer Vertrag:** dunkles Schieferblau als Titel; Teal für Potenzial/Referenz; gedämpftes Blau für Prozess; Bernstein für Stabilisierungs-/Öffnungslesart. Serifentitel, gut kontrastierende serifenlose Datenfelder, drei Achsen immer ausdrücklich beschriften.
- **Eine Feldnummer ist kein Wahrheitsstempel.** Das Raster ist eine verlustfrei adressierbare Datenform, kein physikalischer Würfel. 3D-Darstellungen werden nur mit expliziter geometrischer Einbettung verwendet.

## Programmierbare Feldsprache

```text
T-SOZ@0.1#NM-I-α {
  bedeutung: "Latente strukturelle Assoziationspotenzialität …"
  quelle: "doi:10.5281/zenodo.19406996"
  relation: OFFEN
  operator: OFFEN
  geometrie: OFFEN
  test: OFFEN
}
```

**Schema je Feld:**
`tensor_id, version, feldadresse, originaltext, quelle, provenienz, bedeutung, relation_id, operator_id, form_id, geometrische_abbildung, voraussetzungen, vorwaerts_test, rueckweg_test, invarianten, gegenbeispiel, evidenzstatus`.

**Stempel:**
`Q` = Quelltext erfasst; `M` = mathematische Relation nachgewiesen; `O` = Operator mit Test; `R` = Rückweg bestanden; `?` = offen. Positive Stempel nur an *die einzelne nachgewiesene Behauptung* binden, nicht pauschal an den Tensor.

## Schnittstellen zu Geo-KI und Trinity Algebra

1. `read_tensor(tensor_id, version)` liefert Originalachsen, Quellen, Feldtexte und verifizierte Pfade, nicht erfundene Formeln.
2. `type_field(address)` trennt Quellbegriff, Rollenlesart und belegte Operation.
3. `map_to_geometry(relation, form)` benötigt explizite, typverträgliche Abbildung, sonst `OFFEN`.
4. `test_transform(f, map)` prüft Struktur- und gegebenenfalls Semantikerhalt.
5. `render_a4(index, semantics, evidence)` liefert die zwei Seiten und verwendet eine Feld-ID nur einmal.

Die vorhandenen Geo-KI-Operationen (Rotation, Translation, Spiegelung, Skalierung, Affintransformation etc.) bleiben im Quellkern separat implementiert. Ein Rubik-/Ordnungswechsel ist **kein** semantischer Umbau historischer Rollen ohne Nachweis.

## Geplante Übertragungen

- Mit demselben Druckvertrag lassen sich T-LOGIK, T-HOLO, T-SOZ19 und Luhmann-Kandidaten aus ihren Feldakten rendern.
- Für Soziation 1.9 muss vor einer vollständigen Semantikpublikation die teilweise fragmentierte PDF-Extraktion überprüft werden.
- Mathematische Formeln und Operatoren stehen erst auf der Karte, wenn sie in der jeweiligen Beweisakte verankert und geprüft wurden.
- Der Feldatlas unterstützt eine Feldtheorie als **Code + Sprache + Geometrie + Evidenz**, ersetzt diese aber nicht.

## Bestandsquellen

- `forschung/tensor/algebra-claude/TENSOREN_PUBLIKATIONEN_V0_1.json`
- `forschung/tensor/algebra-claude/typalgebra.py`
- `forschung/geoki/v0_4/src/geometry.py`
- `docs/data/geo-tensor-icon-stamps-v0-1.json`
- Originalbeleg T-SOZ DOI https://doi.org/10.5281/zenodo.19406996

**Publikationsregel:** Vor Freigabe das zweiseitige Layout fachlich und typografisch gegen die Originalfelder gegenlesen. Keine automatische Hochstufung offener Felder.