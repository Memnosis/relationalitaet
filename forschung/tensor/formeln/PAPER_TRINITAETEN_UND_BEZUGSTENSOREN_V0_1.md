# Trinitäten und Bezugstensoren im Formelbestand von Wikidata

**Reduktion definierender Formeln auf Ministrukturen, Suche nach geschlossenen Dreigrößen-Strukturen und Vorhersage fehlender Relationen**

Projekt Relationalität · Arbeitspapier v0.1 · 4. November 2026
Code und Daten: `forschung/tensor/formeln/` im Repositorium <https://github.com/Memnosis/relationalitaet>

---

## Zusammenfassung

Physikalische, chemische und technische Formeln werden meist einzeln betrachtet. Ihre gemeinsame Struktur bleibt dabei unsichtbar. Wir untersuchen 2.676 definierende Formeln aus Wikidata (CC0), deren Symbole dort auf benannte Größen abgebildet sind, und beantworten drei Fragen:

1. Wie häufig verbindet eine Formel genau drei Größen (*Trinität*), und welche Formen haben diese Trinitäten?
2. Gibt es höhere Strukturen, in denen mehrere Trinitäten ein geschlossenes Gerüst bilden?
3. Lassen sich aus solchen Gerüsten Formeln vorhersagen, die im Bestand fehlen?

**Trinitäten.** Ein Drittel aller Formeln ist trinitär (880 von 2.676; 32,9 %). Bei einer Vergleichsliste der 100 bekanntesten Schul- und Grundstudiumsformeln ist der Anteil gleich (34 %). Von den vollständig lesbaren Trinitäten sind 218 Potenzgesetze Xᵃ·Yᵇ·Zᶜ = konst. Davon haben 206 die einfachste Signatur 1:1:1, also Produkt oder Quotient. Additive Bilanzen (23) und Differentialbeziehungen (26) sind deutlich seltener.

**Bezugstensoren.** Aus den Potenzgesetzen leiten wir einen Graphen von *Bezugskanten* ab (422 Kanten): Eine Größe Y entsteht aus X durch Multiplikation mit einer Operatorgröße K. Wir definieren einen *Bezugstensor* als drei Operatoren, deren Verhältnis selbst eine Formel des Bestands ist (z. B. molare Masse M = m/n). Dazu gehören mehrere Zeilen von Größen, die über diese Operatoren ineinander übergehen. Der Bestand enthält 10 solche Tensoren, davon 8 mit mindestens drei Zeilen (3×3-Gerüste). In einem Nullmodell mit zufällig vertauschten Größen entstehen im Mittel 0,79 solcher Gerüste (p = 0,006; 1.000 Permutationen).

**Vorhersagen.** Die Tensoren sagen 35 Relationen voraus, die als eigene Formel im Bestand fehlen, aber aus zwei vorhandenen Formeln und der Operator-Schließung folgen. Ein Beispiel ist „molare Enthalpie = molare Masse · spezifische Enthalpie“. Alle 33 Vorhersagen mit verfügbaren Dimensionsangaben sind dimensional konsistent. Eine fachliche Einzelprüfung ergibt ein klares Bild: Im Bezugsraum der Stoffgrößen (Masse, Stoffmenge, Volumen) sind 13 von 20 Vorhersagen allgemein gültige Beziehungen, 6 gelten unter Bedingungen und nur 1 ist bedeutungslos. In der mechanischen Leiter (Dauer, Masse, Geschwindigkeit) ist nur 1 von 15 allgemein gültig, 7 sind bedeutungslos.

**Kontrolle.** Mit Gröbner-Elimination über geschlossene Dreiecke von Trinitäten leitet das Verfahren bekannte Gesetze ohne Vorwissen her, etwa P = F·v und ρ = c·M für reine Stoffe. Es erzeugt aber auch formal korrekte, fachlich sinnlose Relationen, wenn gleichnamige Größen verschiedene Rollen haben (Pendel–Kepler–BMI). Die Prüfung, ob Rollen übereinstimmen, ist daher der entscheidende, nicht automatisierbare Schritt.

Der aufbereitete Formelbestand wird als maschinenlesbarer Datensatz veröffentlicht. Er enthält TeX, SymPy-Ausdruck, Größenzuordnung, Exponentenvektor, Ministruktur und ISQ-Dimension.

---

## 1 Einleitung

Viele Gesetze der Physik und Chemie haben eine auffallend einfache Gestalt: Drei Größen sind durch ein Produkt oder einen Quotienten verbunden (F = m·a, U = R·I, ρ = m/V). Diese Beobachtung ist alt. Die Dimensionsanalyse nutzt sie seit Buckingham [1]. Nach dem Größenkalkül der ISO/IEC 80000 [2] ist jede abgeleitete Größe ein Potenzprodukt von Basisgrößen.

Weniger untersucht ist die Frage, wie sich die Formeln eines **großen Bestands** zueinander verhalten:
- Welche Gestalten kommen wie oft vor?
- Welche Größen tragen viele Beziehungen?
- Gibt es Gerüste aus mehreren Formeln, die sich gegenseitig bedingen?
- Lassen sich aus ihnen fehlende Formeln ableiten?

Solche Fragen sind erst beantwortbar, seit Formeln in Wissensgraphen maschinenlesbar und mit Bedeutungen verknüpft vorliegen. In Wikidata [3] trägt ein Item seine definierende Formel (Eigenschaft P2534). Jedes Symbol (P7235) verweist über einen Qualifikator (P9758) auf das Item der Größe, für die es steht.

**Beiträge dieser Arbeit:**
1. Einen **aufbereiteten Formelbestand** (2.676 Formeln, 3.264 Größen) mit maschinenlesbaren Ausdrücken, Exponentenvektoren, Ministrukturen und ISQ-Dimensionen als offenen Datensatz.
2. Eine **Reduktion** jeder Formel auf ihre Stelligkeit, ihren Trinitätstyp, ihre Signatur und ihr kanonisches Skelett (Abschnitt 3.2–3.4).
3. Die Definition und einen Suchalgorithmus für **Bezugstensoren**: geschlossene Gerüste aus Trinitäten mit einer Operator-Schließung, samt Nullmodell (Abschnitt 3.6–3.8).
4. **Vorhersagen** fehlender Relationen mit Dimensionsprüfung, Klassifikation und fachlicher Einzelbeurteilung (Abschnitt 4.6).
5. Eine **Kontrolle** durch Wiederentdeckung bekannter Gesetze und eine Analyse der Fehlermodi (Abschnitt 4.7).

## 2 Verwandte Arbeiten

**Dimensionsanalyse und Größenkalkül.** Das Π-Theorem [1] reduziert eine physikalische Beziehung auf dimensionslose Gruppen. Unsere Exponentenvektoren sind die logarithmische Form derselben Potenzprodukte. Wir fragen aber nicht nach der Dimension einer einzelnen Formel, sondern nach der **Struktur eines Bestands**.

**Formelsuche.** Systeme wie MathWebSearch [4] und Approach Zero [5] finden Formeln über strukturelle Ähnlichkeit (Unifikation, Teilbaumvergleich). Unsere Skelette sind eine verwandte, gröbere Kanonisierung, die über Umbenennung und Vorzeichen minimiert. Sie dient der Zählung von Familien, nicht der Suche.

**Symbolische Regression.** AI Feynman [6] rekonstruiert Gesetze aus Messdaten und nutzt dabei Dimensionsanalyse und Separierbarkeit. Wir rekonstruieren Relationen aus **anderen Formeln**, nicht aus Daten.

**Elimination.** Die Ableitung neuer Relationen aus mehreren Gleichungen ist Elimination im Polynomring. Gröbner-Basen [7, 8] liefern sie konstruktiv; wir nutzen SymPy [9].

**Mathematik in Wikidata.** Die Erschließung mathematischer Formeln in Wikidata und ihre Verwendung für mathematisches Frage-Antworten [10] bilden die Grundlage unseres Datensatzes.

Uns ist keine Arbeit bekannt, die (a) den Anteil trinitärer Formeln in einem großen Bestand misst, (b) geschlossene Mehrformelgerüste mit Operator-Schließung definiert und gegen ein Nullmodell prüft und (c) daraus fehlende Formeln vorhersagt.

## 3 Daten und Methode

### 3.1 Daten

| | |
|---|---|
| Quelle | Wikidata, Abruf 2026-11-04T03:49Z (Formeln, Symbole), ISQ-Dimensionen (P4020) und fehlende Bezeichnungen per SPARQL am selben Tag |
| Auswahl | Items mit P2534 und mindestens einem P7235 mit Qualifikator P9758 |
| Umfang | 2.676 Formeln, 3.264 Größen, 1.168 Größen mit ISQ-Dimension |
| Lizenz | CC0 1.0 |
| Vergleichsbestand | 100 bekannte Formeln aus Schule und Grundstudium (Physik, Chemie, Mathematik, Biologie, Ökonomie), von Hand in SymPy kodiert |

### 3.2 Normalisierung

- **Satzauszeichnung entfernen:** Fettdruck, Vektorpfeil, Textschrift und Abstände werden aus dem TeX entfernt, z. B. `\boldsymbol{F}` → `F`.
- **Einlesen:** Die erste definierende Formel mit Gleichheitszeichen wird mit `sympy.parsing.latex` eingelesen.
- **Symbole zuordnen:**
  - Jedes Symbol, das in P7235 auf eine Größe verweist, wird durch `G_<QID>` ersetzt; Konstanten werden durch `K_<QID>` ersetzt.
  - Das gilt auch für gebundene Variablen, z. B. das V in dm/dV.
  - Konstanten sind Naturkonstanten und mathematische Konstanten. Erkannt werden sie über eine feste Liste und über die Bezeichnung.

Gleiche Größe heißt damit gleiches Symbol über alle Formeln hinweg.

### 3.3 Stelligkeit, Trinität, Trinitätstyp

- Die **Stelligkeit** n einer Formel ist die Zahl ihrer nicht konstanten Größen. Eine **Trinität** ist eine Formel mit n = 3.
- Für vollständig lesbare Trinitäten unterscheiden wir:
  - **multiplikativ (Potenzgesetz):** Die Gleichung ist ein Monom gleich einem Monom, also Σ aᵢ·log Xᵢ = konst. Ableitungen dY/dX gehen nach dem Größenkalkül als Y·X⁻¹ ein. Der **Exponentenvektor** (a₁, a₂, a₃) beschreibt die Formel bis auf Konstanten vollständig. Ihre **Signatur** ist |a₁|:|a₂|:|a₃|, normiert auf das kleinste Glied (1:1:1 für F = m·a, 1:1:2 für E = ½·m·v²).
  - **additiv:** X = ±Y ± Z (Bilanz).
  - **dynamisch:** eine Differentialbeziehung, die kein Monom ist.
  - **andere** sowie **nicht gelesen**.

### 3.4 Ministrukturen (Skelette)

Das **Skelett** einer Formel ersetzt Größen durch Platzhalter x₀, x₁, … sowie Zahlen und Konstanten durch k. Es wird über alle Umbenennungen der Platzhalter und beide Vorzeichen minimiert. Damit haben F = m·a, U = R·I und p = m·v dasselbe Skelett. Formeln mit gleichem Skelett bilden eine **Familie**.

### 3.5 Keime und Dreiecke (Elimination)

- Drei Trinitäten, die paarweise mindestens eine Größe teilen, bilden einen **Keim**. Teilen alle drei dieselbe Größe, ist es ein **Stern**. Teilt jedes Paar genau eine *andere* Größe, ist es ein **Dreieck**.
- In einem Dreieck lassen sich zwei der drei Verbindungsgrößen eliminieren: Gröbner-Basis in lexikographischer Ordnung, Faktoren aus Einzelgrößen werden entfernt. Übrig bleibt eine Relation zwischen den übrigen Größen.
- Jede abgeleitete Relation wird dreifach geprüft:
  - **P1 Rollen:** Bedeuten gleichnamige Größen dasselbe?
  - **P2 Neuheit:** Steht die Relation schon als eigene Formel im Bestand?
  - **P3 Stabilität:** Liefern alle Eliminationsreihenfolgen dieselbe Relation?

### 3.6 Bezugskanten und Bezugsoperatoren

Aus einem multiplikativen Exponentenvektor über (X, Y, K) mit a_X = −a_Y folgt

  log Y = log X + (a_K / a_X) · log K,  also  Y = konst · K^s · X.

Wir nennen dies eine **Bezugskante** X → Y über den **Operator** K mit Exponent s. Beispiel: Aus c = C/m folgt C → c über Masse mit s = −1. Ein **Bezugsoperator** ist eine Größe, die viele Bezugskanten trägt.

### 3.7 Bezugstensoren

Sei W eine multiplikative Trinität des Bestands über drei Operatoren (K₁, K₂, K₃), die **Schließung**. Eine **Zeile** zu W ist ein Tripel von Größen (Y, X, Z) mit den Kanten

  X → Y über K₁ (Exponent s₁),  X → Z über K₃ (s₃),  Y → Z über K₂ (s₂),

wobei die drei Exponenten mit W verträglich sind: s₃·log K₃ − s₁·log K₁ = s₂·log K₂ ist (bis auf einen Faktor) genau W. Eine Zeile heißt **vollständig**, wenn alle drei Kanten im Bestand stehen. Sie heißt **ergänzbar**, wenn genau zwei Kanten stehen; die dritte folgt dann algebraisch aus den beiden anderen und W.

Ein **Bezugstensor** ist eine Schließung W mit mindestens zwei Zeilen; mit drei oder mehr Zeilen ist er ein 3×n-Gerüst. Ein Tensor ist damit nicht bloß eine Menge verwandter Formeln:
- Seine Spalten sind die **Bezüge**, z. B. „je Masse“, „je Stoffmenge“, „insgesamt“.
- Seine Zeilen sind die **Sachgrößen**, z. B. Wärmekapazität oder Enthalpie.
- Die Schließung garantiert, dass der Umlauf über die drei Operatoren exakt zum Ausgangspunkt zurückkehrt: K₁^(s₁) · K₂^(s₂) · K₃^(−s₃) = konst.

### 3.8 Nullmodell

Wir vertauschen die Größen-Etiketten aller multiplikativen Trinitäten zufällig. Erhalten bleiben dabei die Häufigkeit jeder Größe und das Exponentenmuster jeder Formel; Formeln mit doppelt vergebener Größe werden verworfen. Danach zählen wir die vollständigen Zeilen und die Bezugstensoren mit mindestens drei Zeilen, in 1.000 Permutationen mit festem Startwert. Der empirische p-Wert ist (1 + #{Null ≥ beobachtet}) / (1 + 1.000).

### 3.9 Dimensionsprüfung

Für Größen mit ISQ-Dimension (P4020) prüfen wir, ob Σ aᵢ·dim(Xᵢ) = 0 gilt, und zwar für jede vollständig gelesene Monomformel ohne Konstanten und für jede Vorhersage.

### 3.10 Klassifikation der Vorhersagen

Eine Vorhersage Y ↔ Z heißt **parallel**, wenn die beiden vorhandenen Kanten die *definierenden* Formeln von Y und von Z sind. Dann sind beide Größen über ihre eigene Definition auf dieselbe Basis X bezogen, z. B. spezifische und molare Wärmekapazität auf die Wärmekapazität C. In allen anderen Fällen heißt sie **Kette**; dort kann die Basisgröße in den beiden Formeln verschiedene Rollen spielen.

## 4 Ergebnisse

### 4.1 Lesbarkeit des Bestands

| | Anzahl | Anteil |
|---|---|---|
| Formeln | 2.676 | 100 % |
| ohne Gleichung (Ungleichungen, logische Aussagen, Mengen) | 533 | 19,9 % |
| eingelesen | 1.773 | 66,3 % |
| nicht einlesbar | 370 | 13,8 % |
| Monomformeln (Exponentenvektor) | 398 | 14,9 % |

**Dimensionsprüfung:** Von den vollständig gelesenen Monomformeln ohne Konstanten sind **225 dimensional konsistent**. 48 sind nicht prüfbar, weil Dimensionsangaben fehlen. Eine Formel ist inkonsistent: der degenerierte Eintrag „ruhend“ (v = 0). Der Bestand ist damit, soweit lesbar, dimensional sauber. Zugleich ist die Prüfung ein Test der Zuordnung von Symbolen zu Größen.

### 4.2 Trinitäten

| | Wikidata | Top-100 |
|---|---|---|
| Stelligkeit 3 | **880 (32,9 %)** | 37 (34 mit drei verschiedenen benannten Größen) |
| häufigste Stelligkeiten | 3 > 2 > 4 | 3 > 4 > 2 |

Trinitätstypen in Wikidata:

| Typ | Anzahl | Beispiele |
|---|---|---|
| multiplikativ, Signatur 1:1:1 | 206 | ohmsches Gesetz, Dichte, Impuls, molare Masse, Stromstärke = dQ/dt |
| multiplikativ, Signatur 1:1:2 | 9 | Bremsweg, Raumwinkel Ω = A/r², Rotationsenergie, Staudruck |
| multiplikativ, Signatur 1:2:2 | 3 | Gravitationsgesetz, Coulomb-Gesetz |
| additiv | 23 | mechanische Energie, Überdruck, elektrische Flussdichte D = ε₀E + P, Baryonenzahl |
| dynamisch (nicht monomial) | 26 | |
| andere (Funktionen, Summen, nicht zugeordnete Symbole) | 384 | |
| nicht eingelesen | 229 | |

In der Vergleichsliste sind 26 der 34 Trinitäten Potenzgesetze, 3 additiv und 3 nichtlinear.

**Befund 1:** Ein Drittel aller Formeln verbindet genau drei Größen. Unter den vollständig lesbaren Trinitäten dominiert die Form *Produkt oder Quotient*: 206 von 218 multiplikativen haben Signatur 1:1:1. Die Trinität ist damit die häufigste Grundeinheit des Formelbestands, und ihre häufigste Gestalt ist die einfachste.

### 4.3 Ministrukturen

734 verschiedene Skelette. Die größten Familien:

| Skelett | Formeln | Beispiele |
|---|---|---|
| x₂ = k·x₀/x₁ | 120 | elektrischer Strom, Phasengeschwindigkeit, Feldstärke, Widerstand, ohmsches Gesetz |
| x₂ = k·x₀·x₁ | 69 | Ladung, Kraft, Gewichtskraft, Partialdruck, Permeabilität |
| x₀ = k/x₁ | 24 | Frequenz, Wellenzahl, Krümmung, Leitwert |
| x₀ = dx₁/dx₂ | 17 | Beschleunigung, Geschwindigkeit, Leistung, Stromstärke, Winkelbeschleunigung |
| x₀ = x₁ + x₂ | 17 | mechanische Energie, Überdruck, Lebensalter, Laplace-Matrix |

**Befund 2:** Zwei Skelette, Quotient und Produkt, tragen 189 Formeln aus Elektrodynamik, Mechanik, Optik und Chemie. Dieselbe Ministruktur wiederholt sich quer durch die Fachgebiete.

### 4.4 Bezugsoperatoren

422 Bezugskanten. Die Operatoren mit den meisten Kanten sind **Dauer (21), Masse (19), Volumen (13), Dichte (11) und Stoffmenge (9)**, gefolgt von Stromstärke, Geschwindigkeit, Feldstärke, Länge und Radius (je 5–6).

**Befund 3:** Die wichtigsten Operatoren sind die Größen, auf die man andere Größen **bezieht**:
- auf die Zeit: Raten,
- auf die Masse: spezifische Größen,
- auf die Stoffmenge: molare Größen,
- auf Volumen, Fläche und Länge: Dichten.

### 4.5 Bezugstensoren

Der Bestand enthält **10 Bezugstensoren** mit zusammen 39 Zeilen, davon **8 mit mindestens drei Zeilen**. Sie zerfallen in zwei Familien.

**(A) Bezugsraum der Stoffgrößen.** Die Operatoren sind Masse, Stoffmenge, Volumen, Länge und Fläche; die Schließungen sind die Normierungsgrößen.

| Schließung W | Zeilen | Beispiele (Y · X · Z) |
|---|---|---|
| molare Masse M = m/n | 6 | spezifische · absolute · molare Wärmekapazität; ebenso freie Energie, Enthalpie, Entropie, innere Energie, Gibbs-Energie |
| Dichte ρ = dm/dV | 6 | spezifische Wärmekapazität · Wärmekapazität · Wärmespeicherzahl; spezifische Aktivität · Aktivität · Aktivitätskonzentration; Massenanteil · Komponentenmasse · Massenkonzentration |
| molares Volumen Vm = V/n | 3 | Wärmespeicherzahl · Wärmekapazität · molare Wärmekapazität; Stoffmengenanteil · Komponentenstoffmenge · Stoffmengenkonzentration |
| längenbezogene Masse m/l | 3 | Exposition · Ladung · Linienladungsdichte |
| Massenbelegung m/A | 2 | Exposition · Ladung · Flächenladungsdichte |

Die Tensoren dieser Familie greifen ineinander: Die Wärmekapazität erscheint als Zeile in den Tensoren zu M, ρ und Vm. Zusammen ergeben sie für jede extensive Größe C das Gerüst

  C  →  C/m (spezifisch)  →  C/n (molar)  →  C/V (volumenbezogen),

mit den Übergängen M, ρ, Vm und der Verträglichkeit **M = ρ·Vm**. Diese Verträglichkeit ist im Bestand selbst eine Formel und wurde in Abschnitt 4.7 unabhängig über Elimination gefunden.

**(B) Mechanische Leiter.** Die Operatoren sind Dauer, Masse und Geschwindigkeit; die Schließungen sind kinematische und dynamische Grundgesetze.

| Schließung W | Zeilen | Beispiele |
|---|---|---|
| Massenänderungsrate ṁ = m/t | 7 | Geschwindigkeit · Beschleunigung · Kraft; Ortsvektor · Geschwindigkeit · Impuls; Leistung · Energie · spezifische Energie |
| Geschwindigkeit v = dr/dt | 4 | Drehmoment · Kraft · Leistung |
| Impuls p = F·t | 3 | Beschleunigung · Geschwindigkeit · Leistung |
| Beschleunigung a = dv/dt | 3 | Impuls · Masse · Kraft (**vollständig**) |
| Newtons zweites Gesetz F = m·a | 2 | Geschwindigkeit · Dauer · Impuls (**vollständig**) |

Familie (B) bildet die bekannte Leiter Ort → Geschwindigkeit → Beschleunigung, multipliziert mit der Masse zu Impuls → Kraft, als Tensor ab. Nur hier stehen Zeilen vollständig im Bestand (2 von 39). Familie (A) ist im Bestand ausschließlich über Definitionen vertreten: Jede Größe ist gegenüber ihrer Basis definiert, die Querbeziehungen fehlen.

**Nullmodell:**

| Kennzahl | beobachtet | Nullmodell Mittel (sd) | Maximum | p |
|---|---|---|---|---|
| vollständige Zeilen | 2 | 0,00 (0,00) | 0 | 0,001 |
| Bezugstensoren mit ≥ 3 Zeilen | 8 | 0,79 (1,29) | 10 | 0,006 |

**Befund 4:** Der Formelbestand enthält geschlossene 3×n-Gerüste weit häufiger, als es die Häufigkeit der beteiligten Größen erwarten ließe. Die Struktur liegt in den Formeln, nicht in den Größen-Häufigkeiten.

### 4.6 Vorhersagen fehlender Relationen

Die ergänzbaren Zeilen liefern **35 Relationen**, die im Bestand nicht als eigene Formel stehen. 33 davon sind dimensional konsistent, 2 sind mangels Dimensionsangabe nicht prüfbar; keine ist inkonsistent.

Jede Vorhersage wurde einzeln fachlich beurteilt (`datensatz/rollenpruefung_v0_1.csv`; ein Prüfer, Begründung je Fall):
- **korrekt**: allgemein gültig;
- **bedingt**: gilt nur unter einer Zusatzannahme;
- **ohne Bedeutung**: dimensional korrekt, physikalisch ohne allgemeinen Sinn.

| | korrekt | bedingt | ohne Bedeutung | Summe |
|---|---|---|---|---|
| Familie A (Stoffgrößen) | **13** | 6 | 1 | 20 |
| Familie B (Mechanik) | 1 | 7 | **7** | 15 |
| parallel | 14 | 8 | 4 | 26 |
| Kette | 0 | 5 | 4 | 9 |

Auswahl:

| Vorhersage | Familie / Art | Urteil |
|---|---|---|
| molare Wärmekapazität, Enthalpie, Entropie, innere Energie, freie Energie, Gibbs-Energie = M · spezifische Größe | A / parallel | korrekt (6 Fälle) |
| Wärmespeicherzahl = ρ · spezifische Wärmekapazität | A / parallel | korrekt |
| Massenkonzentration = ρ · Massenanteil; Aktivitätskonzentration = ρ · spezifische Aktivität | A / parallel | korrekt |
| Impuls / Volumen = Massenstromdichte | A / parallel | korrekt |
| molare Masse = ρ · Vm; Stoffmengenkonzentration = Stoffmengenanteil / Vm | A / parallel | korrekt |
| Ladungsdichte = ρ · Exposition | A / parallel | bedingt: Ladung der in Luft erzeugten Ionen |
| Drehmoment = d(Drehimpuls)/dt | B / parallel | korrekt |
| Kraft = ṁ · Geschwindigkeit | B / Kette | bedingt: Schub bei Massenstrom, nicht F = m·a |
| Leistung = Impuls · Beschleunigung | B / parallel | bedingt: konstante Masse, parallele Bewegung |
| Leistung = Drehmoment / Dauer | B / parallel | ohne Bedeutung (richtig wäre P = τ·ω) |
| Impuls = ṁ · Ortsvektor | B / Kette | ohne Bedeutung |

**Befund 5:**
- **Familie A:** Die Vorhersagen sind überwiegend gültige, aus Lehrbüchern bekannte Beziehungen, die im Bestand nur implizit enthalten sind. Ihre Operatoren sind reine **Bezugsgrößen**: Man teilt dieselbe Sachgröße durch Masse, Stoffmenge oder Volumen *desselben* Systems. Die Rollen bleiben dabei stabil.
- **Familie B:** Die Operatoren (Dauer, Geschwindigkeit, Massenrate) bezeichnen **Vorgänge**, deren Rolle von Formel zu Formel wechselt: Ableitung, Mittelwert, Strom. Dimensional geht alles auf, inhaltlich selten.
- **Klassifikation parallel/Kette:** Sie reichert gültige Vorhersagen an (14 von 26 gegenüber 0 von 9), trennt aber nicht vollständig.
- **Dimensionsprüfung:** Sie trennt gar nicht.

Der stärkste automatische Vorfilter ist die Art des Operators: Bezugsgröße oder Vorgangsgröße.

### 4.7 Kontrolle durch Elimination

**Top-100.** Unter 99 Keimen sind 3 Dreiecke:

| Dreieck | eliminiert | abgeleitet | Prüfung |
|---|---|---|---|
| Arbeit · Leistung · Geschwindigkeit | Arbeit, Weg, Zeit | **P = F·v** | gültig; nicht unter den 100 enthalten |
| Dichte · Stoffmenge · Konzentration | Masse, Stoffmenge, Volumen | **ρ = c·M** | gilt nur für reine Stoffe |
| Pendel · Kepler 3 · BMI | Länge, Masse, Periode | g·a³ = BMI·L³·G | Scheinbeziehung: Länge = Pendellänge vs. Körpergröße, Masse = Zentral- vs. Körpermasse |

**Wikidata.** In einem Lauf mit derselben Momentaufnahme ergaben sich 239 Dreiecke.¹
- 49 lieferten eine saubere Relation, darunter molare Größe = M · spezifische Größe (7 Fälle), volumenbezogene Größe = ρ · spezifische Größe (6), Lichtstärke = Beleuchtungsstärke · r² und Belichtung = Beleuchtungsstärke · Dauer.
- 35 enthielten nicht zugeordnete Symbole; 100 brachen ab (Wurzeln, Zeitlimit); 54 waren nicht einlesbar.

**Befund 6:** Elimination über Dreiecke findet bekannte Gesetze ohne Vorwissen wieder. Damit ist das Verfahren auf bekannter Physik geeicht. Zugleich zeigt das dritte Top-100-Dreieck den typischen Fehlermodus, nämlich gleiche Bezeichnung bei verschiedener Rolle. Er ist formal nicht erkennbar.

¹ Dieser Lauf (`wikidata_lauf.py`) verwendet eine engere Konstantenliste; deshalb weicht die Zahl der Trinitäten geringfügig ab (884 statt 880).

## 5 Diskussion

### 5.1 Was die Ergebnisse bedeuten

1. **Die Trinität ist die Grundeinheit des Formelbestands.** Ein Drittel aller Formeln verbindet genau drei Größen, unabhängig davon, ob man einen kuratierten Kanon oder einen offenen Wissensgraphen betrachtet. Die häufigste Form ist die einfachste: ein Produkt oder Quotient.
2. **Trinitäten verbinden sich zu Gerüsten, die mehr sind als ihre Teile.** Ein Bezugstensor koppelt mehrere Trinitäten über eine gemeinsame Operator-Schließung. Er besitzt einen **geschlossenen Umlauf**: Wer eine Größe nacheinander auf Masse, Stoffmenge und wieder zurück bezieht, kommt exakt zum Ausgangspunkt zurück. Diese Eigenschaft ist überprüfbar und im Nullmodell selten.
3. **Gerüste machen implizites Wissen explizit.** Der Bestand definiert jede spezifische, molare oder volumenbezogene Größe einzeln gegenüber ihrer Basis. Die Querbeziehungen stehen nicht da, folgen aber zwingend. Der Tensor ist die Struktur, aus der sie folgen.

### 5.2 Nutzen

| Anwendung | Was das Verfahren liefert |
|---|---|
| **Pflege von Wissensgraphen** | 13 allgemein gültige, bisher nur implizite Relationen (vor allem molare, spezifische und volumenbezogene Größen), die als Formel in Wikidata ergänzt werden können; ein Dimensions-Check, der Fehler der Symbolzuordnung aufdeckt |
| **Lehre** | Familien gleicher Ministruktur („120 Gesetze, ein Quotient“) und Bezugstensoren als Ordnungsschema für spezifische, molare und volumenbezogene Größen |
| **Formelsuche und Wissensorganisation** | Skelett-Kennungen, Exponentenvektoren und Bezugskanten als Indizes, die über Fachgrenzen hinweg verbinden |
| **Prüfwerkzeug für Ableitungen** | Elimination mit drei Prüfungen; Operatorart (Bezugs- vs. Vorgangsgröße) und Klassifikation parallel/Kette als Vorfilter für die Rollenprüfung |
| **Weitere Forschung** | der Datensatz selbst: maschinenlesbar, mit Größen und Dimensionen, für Graph-, Elimination- und Lernverfahren |

### 5.3 Grenzen

- **Abdeckung:**
  - 13,8 % der Formeln sind nicht einlesbar.
  - Nur 14,9 % sind Monomformeln mit vollständigem Exponentenvektor; die Tensorsuche stützt sich auf diese Teilmenge.
  - Nicht zugeordnete Symbole schließen Formeln aus, etwa die Zeit t in vielen Ableitungen.
- **Vektoren und Tensoren** werden als Skalare gelesen; Richtungen und Indizes gehen verloren.
- **Rollen:** Gleiche QID bedeutet nicht gleiche Rolle. Die fachliche Beurteilung der 35 Vorhersagen stammt von einem einzigen Prüfer; eine unabhängige Doppelbeurteilung mit Übereinstimmungsmaß steht aus.
- **Auswahlverzerrung:** Wikidata bildet vor allem Größen nach ISO/IEC 80000 ab. Mathematik, Biologie, Ökonomie und Sozialwissenschaften sind kaum vertreten.
- **Nullmodell:** Die Permutation erhält Häufigkeiten und Exponentenmuster, nicht aber Fachgebiete. Ein Nullmodell innerhalb der Fachgebiete wäre strenger.
- **Neuheit:** Alle Vorhersagen und Ableitungen sind fachlich bekannt. Der Beitrag liegt in ihrer **automatischen Gewinnung aus einem Bestand** und in der Struktur, die sie erklärt, nicht in neuer Physik.

### 5.4 Ausblick

1. Abdeckung erhöhen: robusterer TeX-Leser, Zuordnung gebundener Zeitvariablen, Vektorformeln.
2. Weitere Bestände einbeziehen: DLMF, NIST-Konstanten, kuratierte Formelsammlungen anderer Fächer.
3. Rollenprüfung mit mehreren unabhängigen Fachurteilen als Goldstandard; daraus einen offenen Benchmark „Dreiecke und Bezugstensoren“ bilden.
4. Höhere Gerüste untersuchen: Verknüpfung mehrerer Bezugstensoren zu einem Bezugsraum, etwa {m, n, V, A, l, t} mit allen Schließungen.
5. Die 13 als korrekt beurteilten Vorhersagen der Wikidata-Gemeinschaft zur Prüfung vorlegen.
6. Die Operatorart (Bezugs- vs. Vorgangsgröße) als Typ in die Tensorsuche aufnehmen und ihre Trennschärfe an einem größeren, doppelt beurteilten Satz messen.

## 6 Verfügbarkeit und Reproduktion

| Datei | Inhalt |
|---|---|
| `datensatz/formelbestand_v0_1.jsonl` | 2.676 Formeln mit TeX, Symbolen, Größen, SymPy-Ausdruck (Text und verlustfrei), Exponentenvektor, Skelett |
| `datensatz/groessen_v0_1.json` | 3.264 Größen mit Bezeichnung, ISQ-Dimension, Konstantenkennung, Vorkommen |
| `datensatz/skelette_v0_1.json` | 734 Ministrukturen mit Formeln |
| `datensatz/trinitaeten_v0_1.csv` | 880 Trinitäten mit Typ und Signatur |
| `datensatz/bezugstensoren_v0_1.json` | 10 Bezugstensoren mit Zeilen und Belegung |
| `datensatz/ergaenzungen_v0_1.csv` | 35 Vorhersagen mit Art und Dimensionsprüfung |
| `datensatz/rollenpruefung_v0_1.csv` | fachliches Urteil (korrekt / bedingt / ohne Bedeutung) je Vorhersage mit Begründung |
| `datensatz/DATENBLATT.md` | Felder, Herkunft, Grenzen |
| `datensatz/abruf_wikidata.py`, `datensatz/bauen.py` | Abruf und Aufbereitung |
| `dschungel.py` | Trinitäten, Bezugskanten, Bezugstensoren, Vorhersagen, Nullmodell, Dimensionsprüfung (nur Standardbibliothek) |
| `formel_struktur.py`, `dreiecke.py`, `wikidata_lauf.py`, `top100_lauf.py` | Reduktion, Elimination, Vergleichsbestand |
| `tests/` | 21 Tests, darunter ein synthetischer Bestand mit bekannter Bezugsstruktur |

Alle Zahlen dieser Arbeit entstehen mit `python3 forschung/register/reproduzieren.py`. Das Nullmodell ist mit festem Startwert deterministisch. Daten: CC0 (Wikidata). Code und Analysen wurden mit KI-Unterstützung erstellt und durch Tests sowie unabhängige Gegenrechnung abgesichert.

## Literatur

[1] E. Buckingham: On physically similar systems; illustrations of the use of dimensional equations. *Physical Review* 4 (1914) 345–376.
[2] ISO 80000-1:2022 *Quantities and units – Part 1: General.* International Organization for Standardization.
[3] D. Vrandečić, M. Krötzsch: Wikidata: a free collaborative knowledgebase. *Communications of the ACM* 57(10) (2014) 78–85.
[4] M. Kohlhase, I. Sucan: A search engine for mathematical formulae. In: *Artificial Intelligence and Symbolic Computation (AISC 2006)*, LNCS 4120, Springer, 241–253.
[5] W. Zhong, R. Zanibbi: Structural similarity search for formulas using leaf-root paths in operator subtrees. In: *Advances in Information Retrieval (ECIR 2019)*, LNCS 11437, Springer, 116–129.
[6] S.-M. Udrescu, M. Tegmark: AI Feynman: a physics-inspired method for symbolic regression. *Science Advances* 6(16) (2020) eaay2631.
[7] B. Buchberger: *Ein Algorithmus zum Auffinden der Basiselemente des Restklassenringes nach einem nulldimensionalen Polynomideal.* Dissertation, Universität Innsbruck, 1965.
[8] D. Cox, J. Little, D. O'Shea: *Ideals, Varieties, and Algorithms.* 4. Aufl., Springer, 2015.
[9] A. Meurer et al.: SymPy: symbolic computing in Python. *PeerJ Computer Science* 3 (2017) e103.
[10] M. Schubotz, P. Scharpf, K. Dudhat, Y. Nagar, F. Hamborg, B. Gipp: Introducing MathQA – a math-aware question answering system. *Information Discovery and Delivery* 46(4) (2018) 214–224.
