# Gesamtprüfung der Website: Grundlagen, Didaktik, Fachwissen, Thesen und Auswirkungen

**Stand:** 03.11.2026 · **Owner:** Website-GPT · **Daten-/Fachgegenprüfung:** Claude ausstehend.  
**Prüfumfang:** 25 einzeln abgerufene bekannte HTML-Fach-/Verwaltungsseiten aus `docs/`, darunter vier neue bzw. unmittelbar zuvor neu aufbereitete Einstiegspunkte. Das ist der **bekannte Website-Bestand dieses Audits**, kein Beweis, dass kein unreferenziertes HTML im Repository existiert. Aussagen zum Inhalt stammen aus den abgerufenen HTML-Dateien und Überschriften, nicht aus einer vollständigen grafischen Browser-/Screenreaderprüfung. Die neue Laufzeitfunktion des Projektmanagements bleibt praktisch abzunehmen.

## 1. Bewertungsmaßstäbe

Jede fachliche Seite wird entlang folgender unabhängiger Fragen beurteilt:
1. **E1 Allgemeinverständnis:** Grundbegriffe, Motivation, Kontext, anschauliches Beispiel.
2. **E2 Ausdifferenzierung:** Varianten, konkurrierende Ansätze, historische Entwicklung, Geltungsbedingungen.
3. **E3 Fachwissen:** Quellen, präzise Begriffe, Operatoren, Test und Gegenprobe.
4. **Diátaxis-Funktion:** Einführung/Tutorial, Handlungshilfe, Erklärung, Referenz – je nach Aufgabe. Nicht jede Seite braucht alle vier Inhalte in sich.
5. **Wissensvoraussetzungen und Anschluss:** Wo kann man fehlende Kenntnisse aufbauen? Welche Seite folgt danach?
6. **Quellen/Forschungsstatus:** Zugänglichkeit, fachlicher Nachweis, Promptprobelauf und redaktionelle Freigabe getrennt.
7. **Projektwirkung:** welche Felder, Tests, Thesen, Publikationen und Mitmachaufgaben gewinnen durch den nächsten Schritt?
8. **Gestaltung/Usability:** Serifenfreiheit, klare Karten, Icons, fachbezogene Farben, lesbare Tabellen und reale Bedienung.

### 2. Einzelseiten-Audit

| Seite | Dringlichkeit | Bereits geleistet / didaktischer Typ | Wesentliche nächste Erweiterung |
|---|---|---|---|
| [`index.html`](../../docs/index.html) | P0 | Einstieg und sechs Kernbereiche; neuer gestufter Lernpfad | Übergreifende Projektarchitektur als erklärtes Diagramm und Verlinkung der jeweiligen Thesen/Nachweise |
| [`minimal-ki.html`](../../docs/minimal-ki.html) | P0 | Vier Kernfunktionen, Operatoren, Anschluss Geo-KI; KI-Geschichte nun verlinkt | Gegenüberstellung mit Regel-, Lern- und Agentensystemen plus faire Bewertungsmetriken und eigene Experimente |
| [`geoki.html`](../../docs/geoki.html) | P0 | Formengenerator, Rotation, 27er-Darstellung, Forschungskette; neue Werkzeugseite verlinkt | Rundreise-Tests SVG/GeoJSON/CAD, Geometriegültigkeit und 3D-/Topologiegrenzen |
| [`tensor-einfuehrung.html`](../../docs/tensor-einfuehrung.html) | P0 | Ringmatrix, 27 Felder, neutral/operativ/fachimmanent/formal unterschieden | Mehr durchgerechnete Beispiele, Testartefakte und klare Originalverweise |
| [`tensor-paper.html`](../../docs/tensor-paper.html) | P0 | Drei historische Logikmatrizen, 27 Fachpositionen, E1-/E3-Gegenmodell, heutige Feldgrenzen | Claudes 27 Einzelclaims, kalkülgenaue Beweise und Gegenmodelle; Originaltext und Neuansatz getrennt |
| [`tensoralgebra.html`](../../docs/tensoralgebra.html) | P0 | Sechs Fachreferenzen und konkreter Nichtisomorphie-Gegenbeweis; drei Lesetiefen | Reproduzierbare Operator-/Relationsfamilien, Quelle, Test-ID und Negativbeispiele je Fall |
| [`bibliothek.html`](../../docs/bibliothek.html) | P0 | Projektquellen/Glossar und verständlicher Quellenprüfweg | Öffentlich freigegebene claimbezogene Lesesicht von Claude statt gesamter interner Zenodo-Übersicht |
| [`projektstand.html`](../../docs/projektstand.html) | P0 | Historische Bestände, Meilensteine, Aufgabenübersicht | Alte Projektzahlen sauber gegen zeitgestempelte neue Aufgaben-/Testergebnisse abgrenzen |
| [`projektmanagement.html`](../../docs/projektmanagement.html) | P0 | **Neu:** GPT-/Claude-Aufgaben, sechs Stufen, Filter, priorisierte Folgeabhängigkeiten und Feldwirkungen | Browser-/JS-Funktionsabnahme, kanonisches Datenregister, echtes Verlaufsarchiv pro Task |
| [`mitmachen.html`](../../docs/mitmachen.html) | P0 | Taskkarten, Quellen, Prompt/Agent/Meta, Lesetiefen, UI-Freigabefilter | Roh-Meta-Prompts stehen weiterhin öffentlich in zwei JSON-Registern: privat sichern, freigegebene Lesesicht, Rückgabe ohne Git |
| [`ki-geschichte.html`](../../docs/ki-geschichte.html) | P1 | **Neu:** Turing/Dartmouth, symbolische und neuronale Ansätze, Transformer/Agenten, eigenes Forschungsziel | Claude-Fachreview, weitere Ansätze und belastbare Leistungs-/Fairnesskriterien |
| [`geoki-systeme.html`](../../docs/geoki-systeme.html) | P1 | **Neu:** SymPy, GEOS/Shapely, CGAL, CAD, QGIS/PostGIS, Geo-Daten und offene Standards | Tatsächliche Versions-/Lizenzprüfung, gleichwertige Testeingaben, Operator-/Formatvergleich |
| [`thesen.html`](../../docs/thesen.html) | P0 | **Neu:** sechs thematische Forschungsrichtungen samt Gegenhypothese und Prüfung | Original-These-IDs/Claimbelege und Evidenz/Reviewstatus aus Claudes Quellen-/Thesenregister |
| [`soulution.html`](../../docs/soulution.html) | P1 | Neun Lösungsbereiche, gemeinsame Werkzeuge, Forschungsbestände/Publikationen | Externe Belege, Messbarkeit, Evaluation je Lösungsmodul und Publikationsversionen |
| [`medien.html`](../../docs/medien.html) | P1 | Bildbibliothek, Originalgrafiken, Fachfarben und Rechte | Medien-IDs, Quellen/Lizenzen, Alt-Texte, Exportqualität und Anschluss an Didaktikblöcke |
| [`quellen-und-uebergabe.html`](../../docs/quellen-und-uebergabe.html) | P0 | Pflichtunterlagen, Aufgabenquellen, KI-Übergaben und Grafikmaterial | Privates Originalmaterial vs. öffentliche Lesesichten und Rückgaben sauber trennen |
| [`harvesting.html`](../../docs/harvesting.html) | P1 | Formelernte, historische 7.622 Formeln, Parser/Tests und Nachzug | tatsächlich getestete Formelrelationen, Typen, exakte Quellen, Fehlerklassen und reproduzierbare Läufe |
| [`interoperabilitaet.html`](../../docs/interoperabilitaet.html) | P1 | Acht Geo-Skill-Familien und API-/Format-Arbeitsideen | echte Tests, Datenaustauschformate, klare 3D-Operatorengrenzen; **globale Nav-Erweiterung aktuell nicht belegt** |
| [`glossar.html`](../../docs/glossar.html) | P0 | Codebuch/Glossar und offene Definitionsaufgaben | 1008/1072-Versionen und 935 frühere Platzhalter korrekt vergleichen; Original- und Fachbelege nachziehen |
| [`inkubator.html`](../../docs/inkubator.html) | P1 | Kompetenzfamilien Geometrie, Audio, Video, Semantik, Skills, APIs | konkrete Werkzeugregister mit I/O, Versionen, Lizenzen, Skilltests, Nutzen und Alternativen |
| [`komprimierung.html`](../../docs/komprimierung.html) | P2 | kompaktes Forschungsziel zur Regelverdichtung | Codecs, Kompressions- und Verlustmetriken, Rekonstruktion, fairer Benchmark |
| [`visuelle-engine.html`](../../docs/visuelle-engine.html) | P2 | visuelle Verknüpfung von wissenschaftlichen Daten und Regeln | echte Graph-/2D-/3D-Verfahren, Beispielkorpus, Render- und Usabilitytests |
| [`vernetzung-ki.html`](../../docs/vernetzung-ki.html) | P1 | überprüfbare Vernetzungshypothese, Versuchsgedanke und Bedingungen | Vernetzungsgrad, Baseline, Kostenkontrolle, Gegenmodell, statistische Auswertung |
| [`taskkarten.html`](../../docs/taskkarten.html) | P1 | 18 historische Taskkarten für Beobachter-/Skill-Aufgaben | Task-IDs zu Prompttrial, Testakten, Owner, Stand und Review verbinden |
| [`impressum.html`](../../docs/impressum.html) | P1 | Impressum/Datenschutz/Lizenzen/Projektinventar (Rechts-/Referenzfunktion) | rechtliche Einzelangaben, Zugangs-/Freigabepraktiken, Findbarkeit prüfen; **globale Nav-Erweiterung nicht belegt** |

Weitere statisch bemerkte Seite ohne globales Hierarchieskript: `quellen-und-uebergabe.html`. Der bestehende Header ist ein Fallback, kein bewiesener Navigationsfehler. Der bekannte Konflikt zwischen `main`-Navigation und dem Integrationszweig bleibt offen; dieses Audit führt **keinen Merge** durch.

## 3. Wo stehen die Thesen – und wo gehören sie hin?

**Bisher:** verstreut auf `vernetzung-ki.html` (Hypothese kritische Vernetzung), `minimal-ki.html` (Forschungsziele), `tensor-paper.html` (Meta-Logik und Feldbehauptungen), `geoki.html` und anderen Fachbereichen. Ein durchgehend mit Primärquellen und Tests verknüpftes öffentliches *Original-Thesenregister* war nicht nachgewiesen.

**Jetzt vorgesehen:**
- **Zentraler Einstieg** `docs/thesen.html`, innerhalb der Forschungsnavigation.
- **Kontextkarten** an jeder betroffenen Fachseite: These → Gegenhypothese → fachlich passende Quellen → Operator/Test → aktueller Evidenzstatus → offene Mitmachprüfung.
- **Internes originales Quellen-/Thesenregister** bei Claude: exakte historische Originaltexte/IDs, Datenbankversionen, Provenienz, Claim-/Beweisakte, alternative Interpretationen, negative Befunde. **Keine automatisch erfundenen kanonischen IDs** aus sechs thematischen Leserkarten.
- **Projektmanagement:** Nicht die These selbst, sondern ihre überprüfbaren Entwicklungs- und Validierungsaufgaben, samt Wirkungs- und Abhängigkeitsrelationen.

## 4. Gesamtlernwege

**KI-Interessierte:** Start → KI-Geschichte → Minimal-KI → vergleichbare Baselines → Mitmachen.  
**Mathematisch Interessierte:** Start → Tensor verstehen → Logik-Tensor → Tensoralgebra → Quellen- und Beweisprüfung.  
**Geometrie-Entwickler:** Start → Geo-KI-Formengenerator → etablierte Bibliotheken und Geo-Daten → Interoperabilität → reproduzierbare Operatorentests.  
**Kritische Mitforschende:** Thesen → Gegenhypothesen → Quellenstatus → Gegenprüfung → Mitarbeit.  
**Projektkoordination:** Projektstand (historisch) → Projektmanagement (aktuelle kuratierte Aufgaben) → Git-Zyklen/Standards → Ergebnisse und Entscheidungen.

## 5. Welche Felder profitieren von welchen P0-Arbeiten?

Ein **validiertes Quellen-/Claim-/Thesenregister** ermöglicht Logik- und Feldprüfungen, gute Publikationsquellen, korrekte Mitmachaufgaben und die Statusanzeige im Dashboard. Ein **verlässliches öffentliches Exportformat** ermöglicht Quellenanzeigen, Taskkarten, Prompt-Tests und sicheren externen Beitrag. Ein **getestetes Navigations- und didaktisches Seitensystem** erschließt sämtliche Forschungsseiten und reduziert doppelte Erklärungsarbeit. Dies sind *erwartete Architekturwirkungen*, deren tatsächliche Verbesserungen im Aufgabenregister und den gegenseitigen KI-Reviews erst nachgewiesen werden müssen.

## 6. Anerkannte Methoden und späterer Verdichtungsprozess

Der [gemeinsame Standards-/Skills-Katalog](../koordination/STANDARDS_SKILLS_METHODENREGISTER_V1_2026-11-03.md) ergänzt die bestehenden W01–W10/D01–D10/X01 um FAIR, PROV-O, SHACL, JSON Schema, ISO/IEC 25010, WCAG 2.2, Diátaxis, NIST AI RMF und OGC/GeoJSON. **Pro Task-Runde** Owner-Prioritäten neu berechnen: Dringlichkeit, Architektur, Schlüsselwirkung, abhängige Tasks, Risiken, Eingangsdaten und Aufwand. Jede KI prüft Artefakte der anderen. Nach drei vollen Zyklen Standards/Skills auf Dopplungen, bewährte Verfahren und Fehlerrisiken untersuchen und nur mit Crosswalks verdichten; keine Originaldaten/Thesen löschen.

**Offen:** tatsächlicher Desktop-Browser- und Deployment-Test aller neu angelegten Seiten, Claude-Fach-/Didaktikreview, Erstellung der kanonischen Thesen-/Quellenprojektion und des originalgetreuen Aufgaben-/Verlaufsregisters.
