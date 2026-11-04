# Tensoralgebra · Suchmatrizen für Vorwärtsrechnung, Umkehrung, Zerlegung und mathematische Darstellungen
**Entwurf 2026-11-04 · Quellenstand: 103 öffentliche historische Gerüste und Claudes ANALYSE_103_V0_1.json · Prüfungen mit SymPy 1.14.0 / NumPy 2.3.5**

## 0. Leitfrage
Nicht die Frage „Welche fertige Tensorart ist dieser Fachbereich?“ vorwegnehmen, sondern zu *jeder belegten Formel und jedem Operator* systematisch andere mathematische Perspektiven ausprobieren: Umstellen, vorwärts und zurück rechnen, Fallunterscheidung, Inversion, Pseudoinversion, Teilabbildung, Differenzieren/Integrationskonstanten, Komposition, Zerlegung, Normierung, Grenzfall, Darstellung als Vektor/Matrix/Tensor/Graph, Basiswechsel, Operatorreihenfolge, Invarianten, Nullraum, Symmetrie, Dynamik, Rekonstruktion und Gegenbeispiele.

## 1. Die Behauptung von genau drei Grundarten: zwei konkurrierende Lesarten
**A. Historisches Klassenmodell (Regel U in `typalgebra.py`):**
- Klasse I / Loop: `rho^-1(rho(S0))=S0` – exakte Rückkehr in dieselbe Adresse.
- Klasse II / Kreislauf: `rho^-1` erreicht die Basisschicht NM, nicht notwendig den Ausgang.
- Klasse III / Prozess: Rückweg erreicht nicht den ursprünglichen Feldindex.

Diese Aussagen sind **in der vorhandenen Implementierung Endadress-Prüfungen über syntaktische Pfade**. Sie berechnen keine echte Umkehrfunktion und keine physikalische Informationsbilanz. Insbesondere ist „CYC ganz in Klasse II“ kein Beweis für einen dynamischen geschlossenen Zyklus.

**B. Drei Operator-Regime (prüfbare Arbeitshypothese):**
1. **Bireversibel**: exakte zweiseitige Umkehrung bei gültiger Domäne (Matrix mit Vollrang; affine Bijektion; ideale unitäre Entwicklung).
2. **Bedingt/mehrdeutig rekonstruierbar**: Umkehrung nur mit Zusatzbedingungen, Domäneneinschränkung oder einer gewählten Sektion (Quadratfunktion, Differenzieren mit Integrationskonstante, Pseudoinverse, Bayes rückwärts nur mit Prior).
3. **Informationsreduzierend**: nicht-injektive Abbildung; aus den Ausgabedaten allein keine eindeutige Eingabe (Projektion, partielle Messung, Tensor-Kontraktion, Mittelwert).

Dies ist **keine Klassifikation ganzer Tensoren**: derselbe Quantenmechanik-Tensor kann eine unitäre, exakt invertierbare Zeitentwicklung und eine nicht-injektive Wahrscheinlichkeitsmessung enthalten. Außerdem passen Gleichheitsbedingungen, Auswahlregeln, nichtäquivalente Umformungen und Invariantenvergleiche nicht notwendig als „eine Inversenart“ hinein. Die drei Kategorien bilden eine nützliche Projektion auf einen Teil der Mathematik.

**Prüfbare Alternativen:** 3 Operatorregime vs 4 Klassen (zuzüglich reine Repräsentationsäquivalenz) vs 5 Klassen (zuzüglich Relations-/Auswahlregel und Nichtäquivalenz). Dazu Mehrfachzuordnung, keine erzwungene exklusive Einteilung. Vergleich durch fachliche Coverage, Gegenbeispielrate, Informationsverlust, reproduzierbare Vorhersage.

## 2. Ergebnis: Vollbestand 103, was bislang wirklich messbar ist
Die bereits von Claude verwendete lexikalische Formelsignatur `ANALYSE_103_V0_1.json` wurde gegen die **103 tatsächlichen historischen Gerüste** ausgewertet und in `SUCHMATRIX_103_TYPEN_OPERATOREN_V0_1.json` einzeln gespeichert.

- **103 Gerüste, 309 Rollenachsen, 27 historische Adressen pro Gerüst**: 0 der 103 enthält im Inventar einen mathematisch typisierten Pfadsatz; keine 27er-Relation als Beweis voraussetzen.
- Vorhandene grobe Formelmarker: **44/103 Gerüste** besitzen mindestens einen der bisherigen 7 Signaturtags; **59/103** erhalten auf dieser Ebene keinen Tag.
- Provisorische Dreiersicht aus **vorhandenen** Tags: **42** Gleichung/Relation (Verhältnis, Potenz, Bilanz, Logarithmus, Exponential), **7** Dynamik-ODE, **3** Matrix-/lineare Struktur. Summe **52 Mehrfachzuordnungen für nur 44 Gerüste**: **37** nur eine Kategorie, **6** zwei, **1** alle drei; **59** keine.
- Dies belegt weder „genau drei mathematische Tensorarten“ noch widerlegt es sie endgültig: Die Eingabe enthält vorwiegend Freitextanker, keine durchgehend ausführbaren Funktionen. Es belegt allerdings, dass die **bisherige Methode keine vollständige, disjunkte Dreierpartition** der 103 liefert.
- Die separaten **Kandidaten für Suchoperationen** sind Empfehlungen aufgrund von Formelsymbolen/Begriffen, keine tatsächlich durchgeführten Tests je Gerüst. Positive und negative Resultate deshalb nicht aus dem Textscanner ableiten.

## 3. Suchmatrizen statt starrer Kategorien
Das System sollte mindestens fünf **orthogonale Matrizen** besitzen. Nicht kartesisch blind alle Varianten rechnen, sondern nur typverträgliche Kombinationen starten.

**M-A · Operationsmatrix (welche Rechnung?)**: Einsetzen, Umformen, eliminieren, faktorisieren, differenzieren, integrieren, linearisieren, normieren/nondimensionalisieren, Basis wechseln, diagonalieren, Eigenwerte, Kommutatoren, Tensorprodukte, kontrahieren, partielle Spur, marginalisieren, Grenzwerte, Spezialfälle, Symmetrieoperationen, Stabilität, Rekursion, inverse Probleme, Unsicherheitsfortpflanzung.

**M-B · Richtungs-/Inversionsmatrix (welche Rückrechnung?)**: Vorwärts, Rückwärts mit zweiseitiger Inverse, Rückwärts mit einer von mehreren Lösungen, Pseudoinverse/regularisiert, implizit/integral mit freier Konstante, nicht rekonstruierbar, unentscheidbar/noch offen. Zu jeder Umkehr: Domäne, Kodomäne, Rang, Nullraum, Anfangs-/Randwerte, Messfehler, gewählte Sektion.

**M-C · Darstellungs-/Äquivalenzmatrix (welche Sicht?)**: Gleichung ↔ Nullstellenform, Graph, Matrix, Tensor, Differentialform, Operatorgleichung, Spektraldarstellung, Basis-/Koordinatenwechsel, dimensionslos, Wahrscheinlichkeit, Informationstheorie. Äquivalenz ist stets **unter Bedingungen** zu belegen. Beispiel: Kürzen mit `z-1` entfernt eine Definitionslücke bei `z=1`, wenn nicht dokumentiert.

**M-D · Struktur-/Kompositionsmatrix (welche Verknüpfung?)**: Kette, Stern, Dreieck, Hyperkante, Schleife, symmetrische Gruppe, gerichtetes System, Dreiergeneratoren, nichtkommutative Lie-Algebra, multilineare Kontraktion, Semigruppenfluss. Jede Kante verlangt Typidentität; nicht von graphischer Nähe oder „drei“ auf bewiesene Relation schließen.

**M-E · Evidenzmatrix (was darf gelten?)**: Quelle und Symboltyp, Dimension, beweiserhaltende Umformung, numerischer Rücktest, Randfall, Domänen-/Zweigprobe, Gegenmodell, unabhängige Implementierung, Eignung eines kleineren Referenzmodells, Fachreview und anschließender Paper-Impact.

### Ein einzelner Ergebnisdatensatz
`tensor_id, source_formula_id, operation_id, direction, representation, preconditions, input_domain, output_domain, derived_object, inverse_type, information_loss, invariant, counterexample, algebraic_proof, independent_test, evidence_grade, affected_objects, paper_routes`.
Jede Rechnung erzeugt eine eigene versionierte **Variantenakte**. Unterschiedliche Darstellungen derselben Relation werden durch `equivalent_to` verbunden; Spezialfälle und Widersprüche behalten eigene IDs.

## 4. Ausgeführter Referenzlauf: 25 Formen, 25 Checks
`suchmatrix_varianten_25.py` plus `SUCHMATRIX_VARIANTEN25_V0_1.json`.
- **5** exakt reversible Referenzfälle (affine Inverse, Vollrangmatrix, endlicher ODE-Fluss, unitäre Involution, umkehrbare Fixpunktiteration).
- **6** bedingt/mehrdeutige Umkehrungen (Quadratwurzeläste, Integrationskonstante, Bayes-Prior, komplexe Logarithmuszweige, Pseudoinverse, singuläre Jacobimatrix).
- **5** Informationsverlustfälle (Koordinatenprojektion, Matrix-Nullraum, Wahrscheinlichkeit ohne Phaseninfo, Tensor-Kontraktion, Mittelwert).
- **3** äquivalente Darstellungen (Nondimensionalisierung, orthogonaler Basiswechsel, Ähnlichkeitstransformation).
- **1** Spezialfall, **3** andere Relationstypen (Kommutator, Ranginvariante, Wigner-Auswahlregel), **2** nichtäquivalente Umformungen (zusätzliche Quadratwurzeln, gekürzte Polstelle).
Alle 25 beziehen sich auf explizite mathematische Referenzmodelle. **25/25 sind keine 25 geprüften historischen Tensoren.**

## 5. Direkt an den historischen FACH-Ankern: 14 Checks für 11 Gerüste
`SUCHMATRIX_14_DIREKTE_TENSOR_FORMELTESTS_V0_1.json` dokumentiert 14 separat berechnete Referenzfälle:
- **F056** `ΔP=RQ`: nach `R=ΔP/Q` oder `Q=ΔP/R` auflösen; Nenner dürfen nicht null sein.
- **F037** `θ=c/(Kd+c)`: `c=Kd θ/(1-θ)`, für `0≤θ<1`; `θ→1` asymptotisch ohne endlichen Wert.
- **F040** Beer–Lambert: `c=A/(εl)`, `εl≠0`.
- **F020** `F=-kBT ln Z`: `Z=exp(-F/kBT)`, Realdomäne/positives Z und `kBT≠0`.
- **F023** `(1-α)S/4=σεT⁴`: positiver Temperaturast unter Modell- und Parameterannahmen.
- **F052** `dC/dt=-kC`: `C(t)=C0 exp(-kt)`; mathematisch rückwärts `C0=C(t)exp(kt)` eindeutig bei exakten Daten, aber bei Rauschen instabil. **Dissipation≠Nichtinvertierbarkeit.**
- **F096→F034** durch `F=0, r(c)=S v(c), V≠0` mathematische Spezialfallbrücke.
- **F035** Nernst-Gleichung nach Reaktionsquotient `Q` rückrechnen.
- **F004** Ähnlichkeitstransformation erhält Eigenwerte, Eigenvektoren ändern Koordinaten.
- **F016** zwei unterschiedliche Zustände mit identischer Wahrscheinlichkeit für dieselbe Born-Messung; Messinformation reicht nicht zur eindeutigen Zustandsrekonstruktion.
- **F054** `dS/dt=-βSI/N` als eine einzelne Gleichung genügt nicht für eine vollständige Rückgewinnung der sonstigen SIR-Zustände.

**Nicht geprüft:** alle mathematischen Rollenbrücken der drei Achsen, alle 27 Positionen, vollständige Fachevidenz, 103/103 typisierte Formelanker oder eine allgemeine Drei-Arten-Beweisführung.

## 6. Warum drei Tensorarten derzeit nicht bestätigt sind
1. **Gleiche Art von Gleichung ≠ gleicher Inversionsregimetyp.** Auch innerhalb rationaler Gleichungen können Äste/Nullstellen/Singularitäten den Rückweg ändern.
2. **Ein einzelner Tensor kann verschiedene Regime besitzen.** F016: unitäre Evolution rückwärts möglich; partielle Messung verliert Information. F052: exponentieller Abklingprozess ist für endliche Zeiten mathematisch invertierbar.
3. **Dreifache Pfadklasse I/II/III ≠ bewiesene mathematische Inversentypen**. `invertierbarkeit` vergleicht Start-/Endadressen und prüft nicht Funktionsinjektivität. `CYC` in einer Klasse ist nicht dieselbe Aussage wie `f^n=id` für einen dynamischen Zyklus.
4. **Gegenprobe für vermeintliche drei exclusive Klassen:** Datenbankprojektion, Bayes-Umkehr, Eigenwertrelation, Kommutator, Variationsprinzip und Messtheorie lassen sich nicht ohne Bedeutungsverlust auf dieselbe eine Mathegleichung reduzieren.
5. **Die groben Tags decken nur 44/103 ab** und überlappen. Eine Dreiteilung bleibt eine **prüfbare Hypothese**, die durch die Suchmatrizen bessere Daten benötigt.

## 7. Die eigentliche interessante Hypothese
Vielleicht existieren **drei wiederkehrende Transformationsprofile** unter mehreren Relationsfamilien – exakte Umkehrung, eingeschränkte Rekonstruktion, informationsreduzierende Abbildung. Das kann ein mathematisch nutzbares Merkmal von **Operationen** sein, nicht zwangsläufig eine disjunkte Sortierung aller Tensoren. Um das zu prüfen: nach vollständiger Typisierung jedem Tensor mindestens drei belegte Operatoren zuordnen, Profile gruppieren, Clusteranalyse und 3-gegen-4-gegen-5-Klassen-Nullmodelle laufen lassen. Erfolg erst, wenn verschiedene Fachbereiche dasselbe Muster einschließlich Gegenbeispielen und nachvollziehbarem Mehrwert zeigen.

## 8. Der nächste ausführbare Compiler und automatische Speicherorte
1. Quellenformeln einschließlich DOI, Domäne, Einheiten, Symbolrollen als typisierte ASTs übernehmen (S1/S2).
2. Rechen-Grammatik pro Typ ermitteln (z.B. ODE-Backward nur bei eindeutiger Lösung; quadratisches `sqrt` mit Ästen; partielle Spur als verlustbehaftete Map).
3. Varianten im begrenzten Budget generieren, jede mit Vorher/Nachher, Nebenbedingungen und Gegenprobe; **SKIP nicht als PASS**.
4. Nach exakt gleicher Semantik kanonisieren; äquivalente Formen über `equivalent_to` verknüpfen statt zu löschen. Abgebrochene Tests speichern.
5. Test-Crosswalk zu 103/Tensor-/Trinitäten-ID und zu den bestehenden 9 historischen Pfadtensoren; A1/MKS nur bei mathematisch belegter Achsenzuordnung.
6. Algebraische Methoden als **Operator-Skill** registrieren, Erkenntnisse als **REL/VAR/COUNTER**-Akten, Fachbedeutung und Grenzen im Glossar/Quellenregister.
7. Ereignis-Nachzieh-Compiler erzeugt Paper-Impacts für Tensoralgebra, Strukturpaper, Quanten-/Fachpaper und Website; fachliche Abnahme vor Publikation.
8. Externe Nullmodelle: Vergleich gegen Zufallsgraphen, Informationsverlust/Äquivalenz unter alternativer Repräsentation und bewusst falsche Dimensions-/Domänenidentifikation.

## 9. Quellen
- Public inventory: `docs/data/tensor-inventar-v10_7.json`.
- Claude formula tags: `forschung/tensor/algebra-claude/ANALYSE_103_V0_1.json`.
- Historic path algebra and Rule U: `forschung/tensor/algebra-claude/typalgebra.py`.
- NIST DLMF mathematical functions, branching and transformation rules: https://dlmf.nist.gov/ .
- SymPy solving sets, domains and branches: https://docs.sympy.org/latest/modules/solvers/solveset.html .
- NIST Wigner 3j symmetry: https://dlmf.nist.gov/34.3 .

**Freigabestatus:** Versionierter wissenschaftlicher Entwurf mit ausführbaren Referenzprüfungen und dokumentierten Gegenbeispielen, keine bestätigte vollständige universelle Tensoralgebra.
