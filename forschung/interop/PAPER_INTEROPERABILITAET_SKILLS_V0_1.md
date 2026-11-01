# Interoperabilität als Skill-Forschungsprogramm der Tensor-Plattform
**Forschungspaper / technische Architektur v0.1 · 1. November 2026**

## Zusammenfassung
Die Geo-KI kann durch öffentlich verfügbare Spezialbibliotheken in einen interoperablen Werkzeugverbund wachsen. Eine Einbindung braucht jedoch mehr als Konvertierungsfunktionen: Wissenschaftlich bedeutsam sind **Formate, Schemata, Semantik, Operatoren, Einheiten, Quellenherkunft, Lizenz, messbarer Informationsverlust und reproduzierbare Rücktransformation**. Der Tensor dient dabei als mögliche relationale Beschreibung, nicht als verpflichtendes Speicherformat für jeden Skill. Das Forschungsprogramm unterscheidet offene technische Normen von frei zugänglichen Bibliotheken und deren Lizenzen.

## 1. Der vorhandene Kern
`forschung/geoki/v0_4/src/geometry.py`: reine Python-Funktionen für Rotation, komplexe Rotation, Flächenberechnung, Euler-Charakteristik, Euler-Schritt, Translation, Spiegelung, Skalierung, Affinität, Bézierkurve und Segmentüberschneidung. Diese Funktionen definieren keine vollständige wissenschaftliche 3D-, CAD-, GIS- oder Kompressionsengine. Die Webgalerie zeigt parametrisierte SVG-Ausgaben.

## 2. Acht Interoperabilitätsfamilien
1. **2D/3D-Geometrie und CAD:** SVG, DXF, STEP, IGES, OBJ, STL, PLY, glTF/GLB, 3MF, IFC; SymPy, Shapely, Paper.js, trimesh, meshio, ezdxf, PyVista, OpenCascade, three.js. Einheiten, B-Rep gegen Mesh und Topologie bleiben erhalten oder der Verlust ist offenzulegen.
2. **Geografische Daten:** GeoJSON, GeoParquet, FlatGeobuf, COG, STAC, GeoZarr; GDAL, GeoPandas, pyproj, xarray. Zu prüfen: CRS, Höhen- und Zeitbezug, Metadaten und Transformationen.
3. **Multidimensionale Wissenschaftsdaten:** HDF5, netCDF-CF, Zarr, NPY, Arrow; h5py, xarray, zarr, numpy, pyarrow. Prüfe Dimensionsnamen, Einheiten, Chunking, verlustfreie und verlustbehaftete Kompression.
4. **Tabellen, Datenbanken und Wissensgraphen:** CSV, Parquet, Arrow IPC, SQLite, RDF/Turtle, OWL, JSON-LD; pandas, DuckDB, NetworkX, rdflib. Semantische Aussage und Datenintegrität sind vom Container zu unterscheiden.
5. **API- und Skillverträge:** OpenAPI, AsyncAPI, JSON Schema, MCP, gRPC, Protobuf, GraphQL. Wichtig: Berechtigung, Seiteneffekt, versionsfähige Signatur, Fehlervertrag und verlässliche Sandbox.
6. **Reproduzierbare Forschung:** RO-Crate, DataCite, FAIR-Konventionen, Frictionless Table Schema, CWL, WDL, Snakemake. Herkunft und Testartefakte in maschinenlesbarer Form.
7. **Sprachen und Ontologien:** Universal Dependencies/CoNLL-U, XLIFF, TMX, TBX, RDF; OPUS, UD, Wikidata. Keine Annahme der vollständigen Abdeckung aller Sprachen.
8. **Modelle und wissenschaftliche Visualisierungen:** ONNX, safetensors, SVG, glTF, Mermaid, Vega-Lite. Ausführbarkeit und visuelle Aussage sind getrennt zu testen.

## 3. Ein universeller Format-Skill-Vertrag
Jeder Adapter soll `id, source_format, target_format, format_versions, schema, units, coordinate_reference, semantic_contract, preconditions, output_type, loss_profile, license, provenance, tests, rollback, status` bereitstellen. Ein Format-Skill ist **nicht** schon fachlich validiert, wenn beide Dateitypen gelesen werden können.

## 4. Skill-Komposition
**Geo-Pfad:** Parametrischer Generator → Typ- und Dimensionsprüfung → Shapely/GEOS oder SymPy → Meshkonverter → glTF/GLB → Three.js → visueller und numerischer Rücktest.

**Wissenschaftspfad:** Quelle + Schema → Parser → Normalisierung → Operatorprüfung → relationales Mapping → Rückrechnung → Codebuch → Forschungsartefakt.

**Außenwahrnehmung:** Katalogabfrage → Versions- und Lizenzprüfung → Download/Adapter → testbarer Skill → Beobachterereignisse.

## 5. Harvesting statt bloßem Modullistenbau
- **FMT-H01:** Formatregister, Hersteller/Normgeber, Lizenz, Version und Parser.
- **FMT-H02:** automatisierter Import von Schemas und Datentypen, Gegenprobe gegen Spezifikation.
- **FMT-H03:** graphförmige Konvertierbarkeit von Quell- zu Zielformaten und Rückwege.
- **FMT-H04:** Qualität und semantischer Verlust unter Round-Trip-Tests.
- **FMT-H05:** fachliche Geo-/CAD-/3D-Operatoren und ausführbare Benchmarks.
- **FMT-H06:** Wissenschaftsdaten und Codebuch-/Glossarbeziehungen.
- **FMT-H07:** API/MCP/Workflow-Skillverträge und Rechte-/Sicherheitstests.
- **FMT-H08:** automatisierte Suche nach neuen Bibliotheken und Versionen mit Quellenprüfung.

Der Registrybestand wächst erst dann zu einer Funktion, wenn mindestens ein Adapter nachweisbar ausführbar ist und seine Fehlerbedingungen beobachtbar sind.

## 6. Messgrößen
Abdeckung nach Formaten/Versionen und Operationen; Roundtrip-Genauigkeit; Topologiefehler; numerische Invarianz; Ressourcenbedarf; Laufzeit; fehlende Metadaten; manuelle Nacharbeit; Wiederholbarkeit. Separat messen, welche Aufgabenfamilien durch Adapter-Komposition erstmals lösbar werden.

## 7. Anschluss der Relationalität
Die dreifache Trinität bleibt ein wissenschaftlicher Rollenraum für belegte Fachmodelle. Die Software-Skill-Graphen haben eigene Typen und Eigenschaften. Beziehungen zwischen Dateiformat, Semantik und Konvertierung können Tensor-Kandidaten ergeben, müssen dies aber nicht. Unpassende Modelle bleiben im Außenraum.

## 8. Verifizierbare Primärreferenzen
- OGC Standards Stack 2026: https://docs.ogc.org/techpaper/26-050/26-050.html
- Trimesh Formats: https://trimesh.org/formats.html
- Arrow IPC und Formatstabilität: https://arrow.apache.org/docs/format/
- Zarr OGC: https://www.ogc.org/standards/zarr-storage-specification/
- NetCDF OGC: https://www.ogc.org/standards/netcdf/
- ODPS 4.2: https://opendataproducts.org/v4.2/
- OpenAPI: https://spec.openapis.org/oas/latest.html
- MCP: https://modelcontextprotocol.io/specification/

**Evidenzstatus:** Der Registerinhalt ist recherchierter Kandidatenbestand. Noch keine ausgeführte systematische Harvest- oder Konvertierungsmatrix.
