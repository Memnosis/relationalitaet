# Fachsemantik und vorhandene Formalisierungen – einfacher Quellen-Crosswalk

**Forschungsedition / Arbeitsregister 0.1 · 6. November 2026**  
**Status:** quellengeprüfte Beispiele und Fachzuordnung; keine abschließende Feldvalidierung.  
**Basis:** [12 Fachbündel und 103 Inventarobjekte](FACHKERN_BUNDLE_103_CROSSWALK_V0_1.json), [Formelbestand Wikidata](formeln/PAPER_TRINITAETEN_UND_BEZUGSTENSOREN_V0_1.md), [Logik-Goldstandard 2.0](LOGIK_TENSOR_2_0_GOLDSTANDARD_ARBEITSSTAND_2026-11-03.md).

## Leseregel

Jede Fachkarte unterscheidet: (1) **Begriff:** Was bedeutet er im Ursprungsfach? (2) **Verfahren:** Was kann damit wirklich gerechnet, entschieden oder beschrieben werden? (3) **Ordnung:** Begriff/Sinn, flächige Anordnung, räumliche Struktur, Bewegung, Operatorrelation oder Metatransfer. (4) **Grenze:** Was darf die Tensor-Grafik nicht behaupten? (5) **Quelle:** Autor, Jahr, prüfbare Referenz. Eine einfache Umschreibung ist als **eigene Paraphrase**, nicht als Autorenwortlaut zu behandeln. Mathematische Namen und Buchstaben sind optional; LaTeX wird in den populären Texten nicht vorausgesetzt.

## Fachkern-Crosswalk

| Bündel / Tensorbeispiele | Bedeutung in einfachen Worten | Bereits vorhandene Fachformalisierung | Ordnungen | Autor / Quelle / offene Grenze |
|---|---|---|---|---|
| B01 F001–F010 | Wann folgt eine Aussage aus anderen? Welche Strukturen sind gleich? | Axiome, Beweisregeln, Wahrheit in Modellen, Mengen, Wahrscheinlichkeitsregeln, Vektor- und Tensoroperationen | O1 O2 O5 O6 | Frege, *Begriffsschrift* (1879); Alfred Tarski, Wahrheit/Modelltheorie (1933), https://plato.stanford.edu/entries/tarski/ ; Kolmogorov (1933), https://plato.stanford.edu/entries/probability-interpret/ ; Kolda/Bader (2009), https://doi.org/10.1137/07070111X . **Grenze:** 27 beschriftete Adressen allein kein koordinatenunabhängiger Tensor |
| B02 F011–F030 | Wie ändern sich Bewegung, Energie, Felder, Wellen und Raumzeit? | Bilanz-/Differentialgleichungen, Hamilton-Dynamik, Tensoren der Raumzeit, statistische Zustandsmodelle | O3 O4 O5 | Noether, *Invariante Variationsprobleme* (1918), https://arxiv.org/abs/physics/0503066 ; BIPM SI-Broschüre (2019, aktualisiert 2026), https://doi.org/10.59161/AUEZ1291 . **Grenze:** Formgleiche Gleichungen sind keine gleichartigen physikalischen Gegenstände |
| B03 F031–F040 | Welche Stoffe reagieren, binden, fließen und sättigen sich? | Reaktionsraten, Massenbilanz, Adsorptions- und Bindungskurven, Nernst/Beer–Lambert | O1 O4 O5 | Michaelis/Menten (1913), Kontext/Originalübersetzung https://pubmed.ncbi.nlm.nih.gov/21888353/ ; Langmuir (1918), Originaldaten separat prüfen. **Grenze:** Bedingungen, Stoffkomponenten, Massen- und Volumenbezug nicht vertauschen |
| B04 F041–F055 | Wie entstehen, regulieren und verändern sich biologische Systeme? | Populations-/Reaktionsgleichungen, Monod-Sättigung, Lotka-Volterra, Hodgkin-Huxley, SIR | O1 O4 O5 | Monod, „The Growth of Bacterial Cultures“ (1949); Korpusanker F046–F055. **Grenze:** verschiedene Mechanismen trotz ähnlicher Kurven |
| B05 F056–F060 | Was kann ein medizinischer Befund, eine Diagnose oder Versorgungskarte aussagen? | Hämodynamik, Bayesdiagnostik, Ereignisraten, IRT und Längsschnittanalyse | O1 O4 O5 | Hernán/Robins, *Causal Inference: What If* (2020), https://miguelhernan.org/whatifbook . **Grenze:** Gruppenrisiko ist keine individuelle Diagnose, Kausalität nicht mit Korrelation verwechseln |
| B06 F061–F070 | Wie funktionieren Berechnung, Datensysteme, Lernen und Informationsübertragung? | Formale Algorithmen, relationale Datenbankoperationen, Typurteile, Bellman, Entropie und gegenseitige Information | O1 O2 O4 O5 O6 | Turing (1936), https://www.verostko.com/turing/1936-paper.html ; Shannon (1948), https://doi.org/10.1002/j.1538-7305.1948.tb01338.x . **Grenze:** übertragene Nachricht nicht gleich verstandene Bedeutung |
| B07 F071–F077 | Wie werden Laute, Wörter, Sätze, Bedeutungen und Absichten voneinander unterschieden? | Lautfrequenzen, Merkmalsmatrizen, endliche Automaten, Grammatik, kompositionale Semantik und pragmatische Modelle | O1 O2 O4 O5 O6 | Peirce-Zeichenrelation, https://plato.stanford.edu/entries/peirce-semiotics/ ; Tarski für formale Semantik, https://plato.stanford.edu/entries/tarski/ . **Grenze:** phonologischer Code ist keine vollständige Bedeutungsbeschreibung |
| B08 F078–F080 | Woran erkennen wir Wahrnehmung, Lernen und Wirkung? | Signalentdeckung, psychometrische Itemmodelle, experimentelle Effektmessung | O1 O4 O5 | David Marr, *Vision* (1982), https://philosophy.hku.hk/courses/cogsci/davidmarr.php ; Hernán/Robins (2020), https://miguelhernan.org/whatifbook . **Grenze:** Lern-/Wirkungsmodelle benötigen Messannahmen und reale Datengrundlage |
| B09 F081 F082 F083 F087 | Wie entstehen wirtschaftliche Entscheidungen, Bilanzen, Risiken und kausale Schlüsse? | Budgetrestriktionen, Buchungsidentitäten, Portfoliovarianz, Instrumentvariablen | O1 O4 O5 | Hernán/Robins (2020), Identifikationsfrage; Ursprungspublikationen der jeweiligen Teilmodelle noch pinpointen. **Grenze:** Identität/Bilanz ist kein Verhalten oder Kausalgesetz |
| B10 F084 F085 F086 F088 F089 F090 | Wie werden soziale Beziehungen, politische Entscheidungen, Recht und Geschichte begründet? | Netzwerkmaße, Wahlrelationen, juristische Subsumtion, qualitative Kodierung, Quellenkritik | O1 O2 O5 O6 | Luhmann, Kommunikation als Selektion, https://www.degruyterbrill.com/document/doi/10.1515/9783839456743-010/html ; Peirce, https://plato.stanford.edu/entries/peirce-semiotics/ . **Grenze:** Normen/Verstehen nicht als Naturgesetze ausgeben |
| B11 F091–F098 | Wie werden technische Prozesse geregelt, stabilisiert und repariert? | PID-Regelung, Zustandsräume, Elastizität, Stoffbilanzen, Advektion/Diffusion | O3 O4 O5 | BIPM SI (2026), https://doi.org/10.59161/AUEZ1291 ; ursprüngliche Regelungs-/Verfahrenstechnikquellen noch pinpointen. **Grenze:** Randbedingungen, Parameter und Materialtyp sind Teil der Aussage |
| B12 F099 F100 | Wie werden Formen gestaltet, wahrgenommen und Klangrelationen gemessen? | Mehrkriterienbewertung, Fourier-/akustische Spektralanalyse, CAD-Transformationen | O1 O2 O3 O4 O6 | Marr (1982) für verschiedene Erklärungsniveaus, https://philosophy.hku.hk/courses/cogsci/davidmarr.php ; konkrete Gestaltungstheorien und Psychoakustik-Primärquellen noch ergänzen. **Grenze:** das Bild ersetzt keine Wahrnehmungsstudie oder Bedeutungstheorie |

## Besonders wichtige Semantik-Grenzen und Übertragungsschlüssel

**Code / Bedeutung / Verstehen:** Claude Shannon (1948) formalisiert Nachrichten, Auswahl und Kanaleffekte. Alfred Tarski (1933) formalisiert Wahrheit und Erfüllung **für definierte formale Sprachen**. Charles S. Peirce entwickelt Zeichen–Objekt–Interpretant als genuin semiotisches Dreierverhältnis. Niklas Luhmann unterscheidet Information, Mitteilung und Verstehen als Selektionen der Kommunikation. David Marr (1982) trennt Aufgabe, Repräsentation/Algorithmus und Implementierung. **Diese Modelle sind nicht identisch.** Ein möglicher gemeinsamer Medien-Tensor ist nur über explizite getypte Übersetzungskarten prüfbar.

**Wissensrepräsentation als technische Brücke:** W3C-SKOS (Miles/Bechhofer, 2009) gibt standardisierte Labels, Ober-/Unterbegriffe und fachliche Begriffsabbildungen, https://www.w3.org/TR/skos-reference/ . RDF verwendet Relationstripel Subjekt–Prädikat–Objekt, https://www.w3.org/TR/rdf10-concepts/ . **Ein RDF-Triple ist keine von sich aus irreduzible Luhmann- oder Peirce-Trinität**. Es eignet sich als Speicher-/Austauschformat, nicht als Gleichheitsbeweis.

**Maßordnung:** Eine gemessene physikalische Größe braucht Einheit und Referenz; die BIPM-SI-Broschüre und ISQ-Dimensionen helfen beim Nachweis, ob eine Umformung überhaupt möglich ist. **Soziale, semantische und mathematische „Dimension“ heißen nicht automatisch dasselbe.**

**Geometrischer Transfer:** Ein grafischer Würfel, Graph oder Torus darf semantische Rollen visualisieren. Erst ein Typ-/Operatornachweis belegt, dass eine Transformation inhaltlich erlaubt ist. Eine reale 3D-Raumposition ist verschieden von drei Indizes eines begrifflichen Feldes.

## Pflichtsatz für jedes spätere Tensor-Paper

> **Was bedeutet der Begriff?** (Fachdefinition mit Autor, Werk, Jahr und Quelle)  
> **Wie wird er operationalisiert?** (Messung, Verfahren, Regel oder Modell)  
> **Wie wird er formalisiert?** (in einfachen Sätzen, optional erst danach symbolisch)  
> **Welche Ordnungen berührt er?** (O1–O6 getrennt kennzeichnen)  
> **Was lässt sich übertragen?** (überprüfte Operation, Nachweis, Rückweg)  
> **Was lässt sich nicht übertragen?** (Bedeutungsverlust, Gegenbeispiel, nicht erfüllte Annahme)  
> **Welcher Fortschritt gegenüber dem alten Paper?** (konkretes neues Resultat / neue belegte Quellenentscheidung, nicht nur neue Gestaltung).

## Kurzbeispiel für eine einfache Fachkarte

**B06/B07/B10 – Morse, Code und Verstehen.** Das Morsealphabet ordnet einzelnen Zeichen kurze und lange Signale zu. Dieselbe Folge kann als Licht, Ton oder als aufgeschriebener Punkt-/Strichcode übertragen werden. Damit bleibt bei korrektem Trägerwechsel und vollständiger Trennung **die codierte Zeichenfolge** erhalten. Das ist ein technischer Rekonstruktionsbefund. Ob das Wort richtig verstanden, als Mitteilung eingeordnet oder akzeptiert wird, ist eine **andere fachliche Prüfung** (Shannon ↔ Peirce ↔ Luhmann). Für den Medien-Tensor: O1 Begriff/Sinn, O2 Feld-/Codefolge, O4 Signalfolge/Bewegung, O5 Encoder/Decoder, O6 geprüfte Übersetzungsakte. O3 physischer Raum nur dann, wenn der Signalträger oder die geometrische Realisierung tatsächlich Teil des Modells ist.

**No-Loss-Regel:** Historische Originaldefinitionen nicht durch diese kurzen Arbeitsdefinitionen ersetzen. Jede abweichende Altversion erhält Quell-ID und Differenzakte. Die populäre Sprache erklärt; der technische Anhang präzisiert. Quellenarten: historische Originalarbeit, wissenschaftliche Sekundärdarstellung, Norm/Standard, Projektthese und eigenständige Rekonstruktion bleiben getrennt.

**Offener Zustand:** Kein automatischer wissenschaftlicher Beweis für alle 103 Tensoren. Der Crosswalk erstellt eine gemeinsame Fachsemantik-Schicht und dokumentiert, wo Urheber, Erstjahr, Formelgeschichte, Geltungsbedingungen oder Primärquellen noch tatsächlich geprüft werden müssen.
