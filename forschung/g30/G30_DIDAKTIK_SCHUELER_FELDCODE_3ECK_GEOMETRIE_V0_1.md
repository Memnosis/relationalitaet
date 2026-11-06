# g30 – Schülermodul: Vom Dreieck zur Feldalgebra

Status: didaktischer Methodenentwurf v0.1, 2026-11-06. Kein Nachweis einer universellen Tensoralgebra.

## Lernpfad in sechs Schichten
1. Sehen und Experimentieren: Dreieckspunkte A,B,C zeichnen; Rotation, Translation, Skalierung, Spiegelung.
2. Messen und Entdecken: Seitenlängen, Winkel, Umfang, Fläche, Vorher/Nachher.
3. Mathematik und Code: deklarative Kartendaten getrennt von `OperatorSpec`; Typsicherheit, Domäne, Invariante, inverse Funktion.
4. 6er-Struktur: A,B,C und die drei Beziehungen AB,BC,CA; geometrisch messbare Strecken, **nicht** automatisch beliebige semantische Relationen.
5. 9er-/27er-Projektfelder: Feldadressen als Kombination von drei Achsen; Operatorbindung ausdrücklich zuweisen.
6. Forschungsablauf: Eingabe, Berechnung, Ergebnis, Rückweg, Gegenbeispiel, Protokoll, Quellen.

## Didaktische Formregel
Ein Feld ist zunächst eine `FieldCard` mit `address, title, meaning, source, status, icon`. Eine ausführbare Regel ist ein gesondertes `OperatorSpec` mit `input_type, output_type, preconditions, f, inverse, invariants, counterexamples, tests, version`. Nur `field_operator_binding` verbindet Karte und Programm. `source_status` ≠ `math_test_status` ≠ `domain_evidence_status`.

## Exaktes Minimalbeispiel: Dreieck drehen
Punkte: A=(0,0), B=(4,0), C=(0,3).
Fläche vor Drehung: |det(B-A,C-A)|/2=6.
Rotation um Ursprung um 90 Grad: R(x,y)=(-y,x).
Nach Drehung: A'=(0,0), B'=(0,4), C'=(-3,0).
Fläche danach: |det(B'-A',C'-A')|/2=6.
Inversion: R^-1(x,y)=(y,-x); führt exakt zurück.
Invariante: alle drei Seitenlängen, Flächeninhalt und Winkel.
Kontrast: Skalierung um Faktor 2 vervierfacht den Flächeninhalt (6→24): ein klarer Gegenfall zur Hypothese „jede Transformation ist flächentreu“.
Kontrast: Projektion P(x,y)=(x,0) reduziert Fläche auf 0 und ist nicht eindeutig invertierbar.

## Verbindliche Testliste
D-01 Eingabepunkte und Orientierung; D-02 Fläche 6; D-03 Rotation 90° mit Erwartungswerten; D-04 Kantenlängen erhalten; D-05 Fläche bleibt 6; D-06 inverse Rotation rekonstruiert exakt; D-07 Komposition zweier Rotationen; D-08 Skalierung 2: Fläche 24; D-09 Projektion: Fläche 0 und Rückweg blockiert; D-10 unbekannte Feldoperatorbindung: BLOCKED, kein Absturz.

## 9er-Unterrichtseinheiten (didaktische Projektglossierung)
1 Punkt und Lage; 2 Verbindung und Strecke; 3 Winkel und Dreieck; 4 Drehen; 5 Verschieben; 6 Spiegeln; 7 Skalieren; 8 Messen; 9 Rekonstruieren und Prüfen.
Dies sind **didaktische Stationen**, nicht neun historische oder empirisch validierte Trinitäten.

## Gemeinsame UI
Große Bühne → links Mini-Bibliothek; rechts nur aktuelle Feldkarte; unten ein gemeinsamer Player. Als zweite Ebene Formeln/Code aufklappbar, als dritte Ebene Testreport; keine separaten Player pro Experiment.
Vorlesemodus Grundschule: Wirkung und Symbol; Sekundarstufe I: Messung, Vorher/Nachher; Sekundarstufe II: Matrixoperator, Determinante, Inverse und Definitionsbereich; Forschung: Typisierter Tensortransfer und Nachweisakte.

## Höhere Ordnung: aktuelle Prüfstandsgrenze
`G30_HOEHERE_ORDNUNGEN_108_FELDAKTEN_PRUEFUNG_V0_1.json`: 108 Kandidatenfelder aus 4 Welten, 36 Dreiergruppen, 4 6er-Kandidaten. 76 strukturelle/Index-/Schutzprüfungen bestanden, aber 0 fachlich validierte Tensoroperatoren und 0 validierte theorieübergreifende Transfers. Dies ist eine Grenze, kein Softwareabsturz.
