# Geo-KI – Open-Source-Skillteam: Architekturupgrade v0.1

## Stand und Ziel
Vorhandener Ausführungskern: `forschung/geoki/v0_4/src/geometry.py` enthält reine Python-Funktionen für Rotation, Spiegelung, Translation, Skalierung, Affinität, Polygonflächen, quadratische Bézierkurven, Segment-Schnittpunkte, Euler-Charakteristik sowie Euler-Schritt und Exponentiallösung. Die parametrisierte Formengalerie auf `docs/geoki.html#formen` ist ein Browserbeispiel, **kein** ausführbarer Ersatz für die Python-Tests.

## Standard-Skills
| Layer | Bibliothek | Funktion | Integrationsbedingung |
| --- | --- | --- | --- |
| Symbolik | SymPy Geometry | Symbolische Punkte, Kurven, Schnitte, Beweise und Gegenproben | Fehler-/Definitionsbereiche bewahren |
| Flächen und boolesche Geometrie | Shapely/GEOS | Polygonvereinigung, Differenz, Schnitt, Affinität | Toleranzen und Topologie testen |
| SVG-Pfadbearbeitung | Paper.js | Kurven, Path-Boolean, Vektorzeichnung | Browseradapter und reproduzierbarer Export |
| 3D | Three.js | Szenengraph, Kamera, Instancing, viele Primitive | Renderbudget, Datenmodell, Interaktionsprüfung |
| 2D generativ | vorhandene Browser-SVGs | Polygon, Stern, Rosette und Netz variieren | Prüfen, dass Parameterkombinationen nicht als verschiedene Formen gezählt werden |

## Beispielkomposition
**Aufgabe:** aus einer kleinen Parameterbeschreibung ein symmetrisches Ornament ableiten.
1. SymPy bestimmt oder prüft eine symbolische Vorbedingung.
2. Python-Kern erzeugt Grundpunkte und Transformationsfolge.
3. Shapely validiert Schnitte und Topologie.
4. Paper.js baut einen bearbeitbaren SVG-Pfad.
5. Observer prüft Anzahl der Objekte, Invariante, Bildauflösung, Laufzeit und Herkunft.
6. Ergebnis und inverser Test werden versioniert gespeichert.

## Messaufgaben
GEO-SKL-01 Adapter für typisierte Transformationen; GEO-SKL-02 Komposition mit Inversen; GEO-SKL-03 Tessellation/Fraktal; GEO-SKL-04 SVG/JSON-Export; GEO-SKL-05 planare Topologie-/Toleranztests; GEO-SKL-06 optionales Three.js-Rendering; GEO-SKL-07 Observer mit Laufzeit, Fehlerrate, Rücktest.

## Externe Primärdokumentation
- https://docs.sympy.org/dev/modules/geometry/index.html
- https://shapely.readthedocs.io/en/stable/manual.html
- https://paperjs.org/reference/path/
- https://threejs.org/docs/pages/InstancedMesh.html

**Status:** geprüfte Kompatibilitätskandidaten und geplante Integrationsmodule; keine dieser vier Bibliotheken ist dadurch bereits im laufenden Geo-KI-Kern installiert oder integriert.
