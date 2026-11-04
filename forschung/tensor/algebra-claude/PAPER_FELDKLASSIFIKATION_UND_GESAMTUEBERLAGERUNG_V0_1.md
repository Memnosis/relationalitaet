---
id: PAPER-ALGEBRA-FIELD-OVERLAY-01
status: research_draft_not_domain_approved
date: 2026-11-04
owner: gpt_review_requested_claude
depends_on:
  - docs/data/tensor-inventar-v10_7.json
  - forschung/tensor/algebra-claude/ANALYSE_103_V0_1.json
  - forschung/tensor/algebra-claude/ALGEBRA_LAUF_V0_1.json
---
# Tensoralgebra-Upgrade: Feldklassifikation und gemeinsame Überlagerung

## Kurzfassung
Die Tensoralgebra benötigt neben der bisherigen typisierten Pfadstruktur eine **Feldalgebra**. Diese muss verschiedene mathematische und semantische Ebenen auseinanderhalten: Rollenadressierung, Quellenfeld, relationale Aussage, Operator, Domäne, Evidenz und Darstellungsform. Eine einfache Überlagerung der Adressen erzeugt 2.781 Positionen, aber nicht 2.781 mathematische Beweise. Ein universeller 27er-Würfel ist zugleich als **Vergleichsindex** nützlich; er wird nicht ohne geprüfte Abbildung zum mathematischen Tensorprodukt.

## 1. Die bereits vorhandenen Bestände und ihre Grenzen
1. Öffentliches historisches Inventar: **103 Gerüste, 309 Trinitäten, 2.781 Adressen**. Die 103 enthalten Text-Rollen und Formelanker, **keine Pfade und keine Feld-für-Feld-Fachprüfung**. `verified_completed_tensors=null`.
2. Algebrafachbestand: **9 aus Werken erschlossene Tensorakten**; sieben mit mindestens einem deklarierten Pfad und zwei ohne. Die neun haben unterschiedlich viele belegte Felder: 18,27,9,27,27,7,27,0,0. 36 Paarvergleiche, 5 Spezialfallbeziehungen, 3 Varianten, 13 pfadunabhängig, 15 unbestimmt. Die Paaranalyse meldet 10 Kompositionskandidaten, darunter vier gemäß eigenen P1/P2/P3-Kriterien neue Pfadfolgen. **Das ist nicht der wissenschaftliche Beweis einer neuen Gleichung**.
3. Im Bericht `ANALYSE_103_V0_1.json` werden 44/103 mit mindestens einem der groben Formelmuster klassifiziert, 59 derzeit nicht. Eine trennscharfe Einteilung in drei mathematische Gesamtarten ist noch nicht belegt.

## 2. Drei Sortiersysteme statt einer einzigen Schublade
**Feldtyp (was für ein Feld?)**: Rolle/Term, Messgröße, Zustand, Operator, Relation, Modell, Beweis-/Quellenfeld, negative Befundposition; ein Feld kann mehrere Rollen besitzen. Kennzeichen `address, role_id, type_id, carrier, units, dimension, version`.

**Relations-/Operatorfamilie (was mathematisch geschieht?)**:
- Gleichung, Umstellung, Definition, Invariante, dimensionsbewahrende Rekonstruktion.
- Dynamik/Differentialgleichung, Anfangs-/Randwert, Rückintegration, Stabilität, Attraktor.
- Abbildung, Matrix, Hilbertraumoperator, Kommutator, Tensorprodukt, Kontraktion, Projektion.
- Wahrscheinlichkeit, Bayes, Messabbildung, marginale/informationsverlierende Abbildung.
- Graph-/Logikregeln, Typurteil, Komposition und Gegenmodell.
Mehrere Familien können **im selben Tensor vorkommen**.

**Rückrechenbarkeit pro Operator (nicht pro gesamtem Tensor!)**:
- R1 *eindeutig reversibel* auf expliziter Domäne,
- R2 *nur bedingt / mehrdeutig / partiell reversibel* mit Zweig, Anfangsbedingung oder Pseudoinverse,
- R3 *informationsreduzierend* (keine eindeutige Urbildrekonstruktion).
Das ist eine zu testende Dreiteilung; sie ist **nicht** als historisches I/II/III-Äquivalent bewiesen. Eine mathematische Inverse kann außerdem instabil sein (schlecht konditioniert), und die Frage nach empirischer Reversibilität ist getrennt.

Zusätzlich sollten mindestens **Quellentreue**, **Evidenzstatus** und **Fachdomäne** unabhängige Filterdimensionen sein. Sie sind keine mathematischen Tensorachsen.

## 3. Tatsächlich ausgeführte Feldüberlagerung: alle 103 Gerüste
Aus den Originalachsen wurden **2.781 geordnete Rollen-Tripel** erzeugt (27 pro Gerüst). Die normalisierten Textbestände umfassen **757 verschiedene Rollenlabels**. In den 103 Gerüsten haben **45** mindestens eine doppelt verwendete Rollenbezeichnung; nur **FACH-F054** hat zwei vollständig identische Achsen. Über alle **5.253 Tensorpaare** besitzen **149** mindestens einen gemeinsamen exakt normalisierten Rollenbegriff.

**Wichtige Negativbefunde:**
- Ohne Achsenausrichtung: **0 identische vollständige Dreier-Rollenkombinationen an derselben Position in verschiedenen Gerüsten**.
- Auch nach allen sechs Achsenpermutationen: **0 Paare mit einem exakten gemeinsamen Rollen-Tripel über drei Achsen**.
- Nach optimaler erlaubter **rein lexikalischer** Achsenpermutation: **144 Paare mit Übereinstimmung auf genau einer Achse, 5 Paare auf zwei Achsen, 0 Paare auf drei Achsen**.
Diese Nullbefunde sind ***nur* lexikalisch**; bei synonymen oder mathematisch äquivalenten Begriffen können wichtige Äquivalenzen noch unerkannt bleiben. Jede semantische Achsenpermutation muss explizit typisiert und fachlich begründet sein.

Kandidatenpaare mit Zwei-Achsen-Schnittmenge:
1. FACH-F007 Geometrie ↔ FACH-F015 Allgemeine Relativität (Metrik, Krümmung, Geodäte).
2. FACH-F006 Differentialgleichungen ↔ FACH-F043 Systembiologie (Zustand, Stabilität).
3. FACH-F010 Statistik ↔ FACH-F064 Maschinelles Lernen (Parameter, Stichprobe, Modell; nach Permutation zwei Achsen belegt).
4. FACH-F020 Thermische Physik ↔ FACH-F045 Biophysik (Energie, freie Energie).
5. FACH-F052 Pharmakokinetik ↔ FACH-F098 Pharmakoökonomie (Dosis, Exposition).

**Zu prüfende Schlussfolgerung:** Drei Achsen sind textuell überwiegend fachlich verschieden; die gemeinsame Mathematik kann dennoch in Operatoren, Gleichungsfamilien, Transformationen, speziellen Grenzfällen und Isomorphismen liegen. Gerade diese Ebene fehlt bislang als geprüfter Crosswalk.

## 4. Bereits überlagerte neun pfadbasierte Tensorakten
Originalquelle `ALGEBRA_LAUF_V0_1.json` wurde neu indexiert: 9 Objekte, 36 Vergleiche; 5 Spezialfälle, 3 Varianten, 13 unabhängige Pfadbestände, 15 unbestimmte. Sieben haben Pfade, zwei nicht. Insgesamt zehn formale Kreuzkompositionen, darunter vier interne Neuerfüllungen. Für alle müssen die Positionen **beide** Quellen, Typbedingungen, formale Gleichheit, mathematische Geltung und mindestens eine unabhängige Wiederholung erhalten. `P3_eigen` ist keine unabhängige Engine.

## 5. Feld-Eigenschaftsmatrix für die neue Algebra
Jede Feldakte `(tensor_id, tensor_version, field_address)` erhält getrennte maschinenprüfbare Eigenschaften:

| Gruppe | Felder | Prüfstatus |
|---|---|---|
| Identität | `field_id, original_label, role_ontology, source_ref` | Kanonreferenz und ID-Test |
| Mathematischer Träger | `carrier_type, scalar_field, dimension, units, coordinate_system` | Typprüfung |
| Inhalt | `relation_type, defining_equations, assumptions, constraints` | Originalquellenprüfung |
| Operation | `forward, inverse, partial_inverse, branching, composition, contraction, basis_change` | Rechen- und Domänenprüfung |
| Geometrie/Topologie | `invariants, symmetries, rank, topology, singularities` | Eigenständige mathematische Gegenprüfung |
| Zeit/Statistik | `state, dynamics, stochastic_model, information_loss, stability` | Vorwärts-/Rückwärts-/Identifizierbarkeitsprüfung |
| Nachweis | `provenance, proof, counterexample, repro_sha, review_status` | Unabhängigkeit, Fachabnahme, Freigabe |

Alle ungetesteten Eigenschaften bekommen `unknown`; leere Felder werden nicht automatisch `false`.

## 6. Überlagerungsoperatoren
Nicht nur `overlay(T1,T2)`, sondern eine typisierte Familie:
- `O_pos`: gleiche Adresse und exakte gleiche Rollen-IDs (lexikalischer Screeningtest allein reicht nicht).
- `O_align`: Achsenausrichtung mit expliziter, belegter Abbildung zwischen Rollen und Dimensionen; alle sechs Permutationen nur als *Kandidaten*.
- `O_sem`: gleiche wissenschaftliche Größe/Rolle nach Quellen-, Einheiten- und Kontextabgleich, mit `equal|special_case|partially_shared|incompatible|unresolved`.
- `O_math`: gleiche Trägermathematik/Operatorfamilie oder expliziter Isomorphismus/Homomorphismus; Identität, Umformung, Differential-/Operatorbeziehung und Geltungsbereiche prüfen.
- `O_path`: typkorrekte Pfadfolge, Komposition, Hysterese, Rückrechnung und Gegenprobe; soweit vorhanden Claudes Typalgebra wiederverwenden.
- `O_evidence`: kumulative Quellen-/Test- und Widerlegungsbetrachtung; widersprechende Befunde bleiben getrennt.
- `O_union`: **verlustfreie Vereinigung von Akten** nach ID und Typ; keine irrtümliche physikalische Addition.
- `O_intersect`: Schnittmenge nur für tatsächlich semantisch äquivalente Felder; rein lexikalische Schnittmenge separat markieren.
- `O_difference`: welche Eigenschaften/Operatoren fehlen oder unterscheiden sich?
- `O_composition`: nur für kompatible Träger und mathematisch definierte Verknüpfung, mit Gegenprobe.

## 7. Zentrale Hypothese prüfen: drei Klassen oder fünf gemischte Familien?
**H3:** Alle projektmathematischen Operationen lassen sich sinnvoll als R1 exakt reversibel, R2 eingeschränkt/mehrdeutig reversibel oder R3 nicht eindeutig reversibel klassifizieren.
**H0:** Die drei Rechenklassen sind nur eine **Projektion** auf die Invertierbarkeit, während mindestens Operationstyp, Informationsverlust, zeitliche Stabilität, Geltungsbereich und Referenzabbildungen unabhängige Dimensionen bilden. Gleiche Tensoren können R1- und R3-Operationen enthalten, z.B. unitäre Entwicklung und nichtinvertierbare Messstatistik der Quantenmechanik.
**Vergleich:** R1–R3 vs mathematische fünf- bis achtgliedrige Operator-Typfamilie, Kontrolle für Mischfälle, Stabilität und notwendige Bedingungen. Zuerst an 9 pfadbasierten Tensorakten und 10 ausgewählten Fachgerüsten; später an allen 103. Bis dazu Fachakten, die alle Operatoren und Feldbeziehungen auflösen, bleibt die drei-Tensoren-Klassen-Hypothese **offen**.

## 8. Welche Ergebnisse wie weiterverwenden?
- **Algebra**: operator- und feldorientierter Typkatalog, Überlagerungsfunktionen, Inversions-Gegenbeispiele, 36 paarweise Pfadvergleiche, 5 Kandidatenpaare.
- **Tensorakten**: neue Feldattribute und vorläufige Crosswalks unter Original-IDs; **keine Überschreibung des historischen Inventars**.
- **Harvesting/Skills**: explizite Operationen `align_axes`, `field_profile`, `domain_guard`, `compose`, `try_inverse`, `compare_invariant`, `explain_difference`, `generate_counterexample`.
- **Quellen/Glossar**: Kandidaten zu Träger, Operatorfamilie, Rückrechenbarkeit, Invariante, Feldrolle; FPP-01-Ereignis-/Impactentwürfe bis zum kanonischen Abgleich.
- **Papers**: dieses Strukturpaper, Tensoralgebra-Fachpaper, Fachanwendungen. Die 103er-Rohmatrix bleibt Datensatz, kein per Hand kopierter Papertext.
- **Website**: Interaktive Feldvergleichsmatrix und 3×3-Fachkarten mit Links auf Originaldatensätze; Quelle, Reifegrad und semantischen Vorbehalt sichtbar.

## 9. Quellen und Vorbehalte
Kanonische Daten: `docs/data/tensor-inventar-v10_7.json`, `forschung/tensor/algebra-claude/ANALYSE_103_V0_1.json`, `ALGEBRA_LAUF_V0_1.json`, `BEFUNDREGISTER_TENSOR_V0_1.json`. Spezifische Teilresultate `FELDUEBERLAGERUNG_103_V0_1.json`, `ACHSENALIGNIERUNG_103_FELDUEBERLAGERUNG_V0_1.json`, `ACHSEN_ALIGNMENT_POTENZIALE_103_V0_1.json`, `UEBERLAGERUNG_9_PFAD_TENSOREN_V0_1.json`.

Die aktuelle Untersuchung ist **kein Beweis, dass alle Tensoren voneinander unabhängig sind**. Ebenso begründet gleiche Fachsprache keinen wissenschaftlichen Isomorphismus. Ein numerischer gemeinsamer Feldindex ist erst nützlich, wenn wir seine semantische und mathematische Bedeutung sauber rekonstruieren.
