# Quanten-Trinitäten, historische Projekttensoren und verschiedene mathematische Relationsfamilien
**Stand 2026-11-04 · fachlicher Vergleichsentwurf · nicht als bestätigte Feldtheorie veröffentlicht**

## Leitfrage und klare Begriffe
Die Projekt-Tensoren haben 3 benannte Trinitäten × 3 Elemente je Trinität → 27 **Rollenadressen**. Quantenmechanische 3-Qubit- und 3-Qutrit-Zustände liegen in Tensorprodukten von Hilberträumen; ihre (2³) beziehungsweise (3³) Amplituden sind mathematische Koeffizienten, keine 27 automatisch gültigen Feldrelationen. Ein Wigner-3j-Koeffizient beschreibt die Kopplung dreier Drehimpulse, nicht von drei Trinitäten.

## Vergleich gegen die echten historischen Projekt-Achsen
- **FACH-F016 Quantenmechanik** (Strukturentwurf): T1 Zustand/Operator/Messwahrscheinlichkeit, T2 Zustandsvektor/Hamiltonoperator/Zeitentwicklung, T3 Observable/Spektralprojektor/Bornwahrscheinlichkeit. Formelanker `p=Tr(ρE)` (Bornregel). **Belegte Brücke** zu 3-Qubit-/Qutrit-Referenzen: Hilbertraum-Tensorprodukt; Dichtematrix `ρ=|ψ><ψ|`; partielle Spur; Bornregel; Schrödingerentwicklung durch unitäre Operatoren. **Noch nicht im Projekt belegt**: alle 27 Rolle-Operator-Beziehungen, fachliche Unabhängigkeit aller Achsen, allgemeine Entanglement-Klassifizierung. Achsen 2 und 3 sind ausdrücklich *neue Kandidaten*.
- **FACH-F017 Quantenfeldtheorie** (Strukturentwurf): T1 Feld/Wirkung/Korrelator, T2 Feldoperator/Vakuum/Korrelator, T3 Symmetrie/Noetherstrom/Wardidentität. Formelanker `Z[J]=∫Dφ exp(iS+iJφ)` (formal mit Einheiten/Regularisierung zu präzisieren). **Belegte externe Mathematik**: Funktionalintegral/Erzeugungsfunktional, funktionale Ableitungen erzeugen Korrelatoren, Variationsrechnung, Symmetrie/Ward-Identität unter Voraussetzungen. **Noch nicht belegt:** eindeutiger mathematischer Crosswalk der 27 Rollenpositionen; mehrfach auftretender Korrelator ist nicht automatisch ein unabhängiges Achsenelement; beliebige Identifikation mit Quantenamplituden oder DLMF-3j-Werten.
- **FACH-F026 Quantenoptik**: Zustände/Wechselwirkung/Detektion; Licht-Materie-Hamiltonoperator/Übergangsrate; Photonenzahl/Korrelation/Statistik. Formelanker Jaynes–Cummings. Mathematik: Operatoren, Erzeugung/Vernichtung, Kommutatoren, Hamilton-Evolution, photonische Korrelationsfunktionen. Kein allgemeines QFT-Modell für alle Prozesse, keine komplette Tensorprüfung.
- **FACH-F031 Quantenchemie**: Orbitale/Dichte/Energie, Hamiltonoperator/Wellenfunktion/Energie, Dichtefunktional/Elektronendichte/Grundzustandsenergie. Mathematik: Eigenwertproblem, Erwartungswert, Variationsprinzip, nichtlineare Funktionaloptimierung. Das doppelte Wort Energie bildet nicht automatisch identische Rollenbeziehungen.
- **Historische Pfadsprache T-FELD**: Claude `BEF-T002` meldet teilweise gleiche Adressprojektion `NM-I-γ → ZM-II-γ → UM-III-γ` für Holographie/Feldtheorie/Soziation; `BEF-T015` meldet ungeklärtes Pfadkürzel `TM`. **Dies ist bisher eine formale Adress-/Pfadgleichheit, nicht die Validierung der Quantenfeldtheorie.** `BEF-T018` dokumentiert ausdrücklich das fehlende Crosswalk Fachachsen→M/K/S. `public_release=not_approved`.

## Vier getrennte mathematische Relationsklassen, die das Projekt unterstützen muss
1. **Algebraische Gleichheit/Umformung:** `P=Fv`, `H|ψ>=E|ψ>`; Voraussetzungen und Gleichheits-/Eigenvektortypen.
2. **Differential- und Variationsrelation:** Schrödinger `iℏ∂t|ψ>=H|ψ>`, Euler-Lagrange `δS=0`; Ableitung, Anfangs-/Randbedingungen und Funktionalräume.
3. **Operatoren, Kommutatoren und Tensorprodukte:** `[Jx,Jy]=iℏJz`, `HA⊗HB⊗HC`, `Tr_B`; Nichtkommutativität, Basiswechsel, Norm, Positivität.
4. **Wahrscheinlichkeit, Symmetrie und Auswahlregel:** Born `p=Tr(ρE)`, Wigner-3j `m1+m2+m3=0` plus Dreiecks-/Paritätsregel, Ward-Identitäten; Nichtnull- und Gegenfälle.
Zusätzlich: statistische/empirische Gesetze und modellabhängige Näherungen als eigene Gültigkeitsklasse. **Nein, es existiert keine einzige Formelklasse, die alle Projekttensoren intern teilen müssen**. Gemeinsamer Standard ist eine getypte Strukturgrammatik, keine einheitliche Physik.

## Was die Referenztests tatsächlich zeigen
Der reproduzierte NumPy/SymPy-Lauf in `quantum_structure_pilot.py` ergab 9/9 Referenzchecks erfolgreich: drei Qubits Produkt/GHZ/W mit gleicher 2×2×2-Dimension, aber Three-Tangle 0/1/0 und unterschiedlicher Reinheit; drei Qutrits Produkt/GHZ3 teilen 3×3×3/27 Koeffizienten, unterscheiden sich aber im Schmidt-Rang (1 vs 3). Ein zweiter exakter SymPy-Lauf `wigner_collection_sweep.py` erfasste 3375 Kombinationen mit j in {0,1/2,1,3/2,2}; 303 erfüllen Vorbedingungen, 293 nicht-null, 10 Null trotz Vorbedingungen. Dies sind etablierte Rechenbeispiele, kein Beweis eines Projekt-Tensors.

## Welche Feldtheorien zur Quantenphysik gehören
- **Skalare QFT** (Klein–Gordon/`φ⁴`): Feld, Wirkung, Zwei-/Mehrpunkt-Korrelatoren, Renormierung.
- **Fermionische QFT** (Dirac-/Weylfelder): Antikommutatoren und Grassmann-Integrale.
- **QED**: abelsche U(1)-Eichtheorie des Elektromagnetismus; Ward–Takahashi-Identitäten.
- **Elektroschwache Theorie**: SU(2)L×U(1)Y mit spontaner Symmetriebrechung/Higgs.
- **QCD**: nichtabelsche SU(3)c-Eichtheorie; Farbladung, Confinement, Wilson-Schleifen.
- **Standardmodell**: verknüpft QCD und elektroschwache Sektoren unter SU(3)c×SU(2)L×U(1)Y.
- **Effektive Feldtheorien** (EFT: z. B. chirale Störungstheorie, Standardmodell-EFT): kontrollierte Niedrigenergie-Expansion und Gültigkeitsskala.
- **Gitter-Eichtheorie**: Regularisierungs-/Rechenzugang für nichtperturbative Felder.
- **Konforme QFT** (CFT) und **topologische QFT** (TQFT): Symmetrie- bzw. Topologie-strukturierte Theorieklassen.
- **Thermische/Nichtgleichgewichts-QFT**: endliche Temperatur, Schwinger–Keldysh-Formalismus.
**Wichtig:** DFT der Quantenchemie ist eine quantenmechanische Dichtefunktionaltheorie, nicht automatisch relativistische QFT; Allgemeine Relativität ist klassische geometrische Feldtheorie, quantisierte Gravitation keine abgeschlossene empirisch bestätigte Einheits-QFT.

## Hat die Quantenkopplung eine trinitäre Algebra?
**Ja, in einem präzise eingeschränkten Sinn.**
- Drei Hilbertraumfaktoren besitzen ein *assoziatives Tensorprodukt* `(A⊗B)⊗C ≅ A⊗(B⊗C)` mit **Basis-/Typbedingungen**, jedoch nicht drei Projekt-Trinitäten.
- Wigner-3j besitzt genuine **Dreierkopplung**, Dreiecksungleichung, m-Summenregel, Parität/Symmetrien, Konjugations-/Permutationsregeln und Nullfälle. 6j/9j behandeln Rekopplungsstrukturen, keine automatische dreifache Projektachsen-Semantik.
- Drehimpulsoperatoren erfüllen eine **zyklische Kommutatoralgebra** `[Jx,Jy]=iℏJz` plus zyklische Varianten, die fachlich eine echte algebraische Dreierrelation ist; die `su(2)`-Lie-Algebra besitzt Jacobi-Identität und nichtkommutative Struktur.
- GHZ/W zeigen 3-Parteien-Verschränkungsinvarianten; 27 Amplituden sind nicht 27 bewiesene Relationsfelder.
Die Ergebnisse liegen unter `forschung/tensor/strukturvergleich/`; sie sind **wissenschaftliche Referenzfamilien zur Validierung** der Projekt-Tensoralgebra.

## Anforderungen an die Algebra, Harvesting und Paper
- Keine Gleichsetzung von Strukturtyp, Indexzahl, Formelstelligkeit und wissenschaftlichem Beweis.
- Ein `relation_family`-Feld: `algebraic_equation|differential|variational|operator_commutator|tensor_product|measurement_probability|symmetry_selection|empirical_model`.
- Jede Relation: `inputs, outputs, carrier, operators, symmetry, conservation, domain, units, gauge, source, proof, counterexample, independent_reproduction, reviewed_status`.
- Ein `structure_type` und ein `negative_equivalence` für Verwechslungen von Projekt-Rollenwürfel, Amplitudentensor, Wigner-Kopplung, Hilbertraum und tensor/1.0.
- Vergleich der vier historischen Kandidaten FACH-F016/017/026/031 anhand ihrer Originale vor 27-Feld-Rekonstruktion; `BEF-T002/015/018` bleiben bewusst offen.
- Zwei eigenständige Papers: **(1) Tensoralgebra: drei mathematische Beziehungen und ihre Unterschiede**, **(2) Quantenfeldtheorie und Quanten-Trinitäten: struktureller Vergleich und Gegenmodelle**. Erkenntnisse in primäre Strukturvergleichsakte, Auswirkungen auf Glossar/Quellen/Website als FPP-Impact-Deltas.
- Fachliche Abnahme nur nach externen Quellen und reproduzierbarer Operatorprüfung; Quelle und Methode pro Akte.

## Externe Referenzen
NIST DLMF https://dlmf.nist.gov/34.2 · https://dlmf.nist.gov/34.10 ; IBM Quantum Bornregel https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/general-measurements/formulations-of-measurements ; Standardmodell-Eichtheorie https://link.springer.com/chapter/10.1007/978-3-319-51920-3_1 ; Tensor-Netzwerke https://doi.org/10.1146/annurev-conmatphys-040721-022705 ; Dichtefunktional https://pmc.ncbi.nlm.nih.gov/articles/PMC10375883/ .
