---
id: PAPER-KT-2026-010
title: Was ist Logik? Was ist „Was ist“? Definitionen, Messregime und Benchmarkkritik
date: 2026-11-04
version: 0.1.0
status: research_draft_not_peer_reviewed
links: [PAPER-KT-2026-008, PAPER-KT-2026-009]
privacy: redacted_research_public_branch
---
# Was ist Logik? Was ist „Was ist“? Der Benchmark des Benchmarks

## Leitfrage
Wenn wir prüfen, ob ein System „intelligent“, „logisch“, „erfolgreich“ oder „wahrheitsgemäß“ sei, sind bereits mehrere Entscheidungen vorausgesetzt: Begriff, theoretischer Gegenstand, zulässige Schlussregeln, Operationalisierung, Itemkorpus, Messskala, Aggregationsregel, Entscheidungsgrenze, Folgen.

## 1. Logik ist nicht gleich empirische Wahrheit
Klassische Modelltheorie: Γ ⊨ φ bedeutet, dass in jeder Interpretation, in der Γ wahr ist, auch φ wahr ist. Ein gültiger Schluss kann von faktisch falschen Prämissen ausgehen. Separat: Γ ⊢ φ (Ableitbarkeit in festgelegtem Beweissystem). Soundness/Completeness verbinden beide *relativ zu spezifizierten formalen Systemen*. Nicht jede Logik akzeptiert dieselben Schlussregeln. In klassischer Logik gilt Explosion (A, ¬A ⊢ B); relevante und parakonsistente Systeme lehnen sie typischerweise ab. Beall/Restall diskutieren logischen Pluralismus; daraus folgt weder Beliebigkeit noch „alles ist wahr“.

## 2. Was ist ein „Was ist“?
- Deskriptive Definition: tatsächlichen Gebrauch erfassen.
- Stipulative Definition: Begriff für einen Zweck festlegen.
- Explikation (Carnap): unpräzisen Begriff für ein bestimmtes Forschungsziel verbessern.
- Theoretische Definition: Rolle innerhalb eines Modells/Theoriegefüges.
- Operationale Definition (Bridgman): Mess-/Beobachtungsoperationen festlegen; Gegenposition: ein Konstrukt wird nicht durch eine einzelne Operation erschöpft.
- Wittgenstein: Begriffe können Familienähnlichkeiten statt eines einzigen gemeinsamen Wesenskerns besitzen.
Begriffe, Realität und Messung sind miteinander verbunden, aber nicht identisch.

## 3. Prüf- und Messverfahren
**Formal:** Wahrheitstafeln, SAT/SMT, Modellprüfung, Theoremprover, Gegenmodelle, Soundness-/Completeness-Beweise, Konsistenz/Entscheidbarkeit/Komplexität.
**Empirisch:** Interventions- und Kontrollstudien, Wiederholung, Generalisierung, Validierung an externen Aufgaben, Reliabilität, Unsicherheitsintervalle, Referenzstandards.
**Messwissenschaft:** Repräsentations- und Skalentheorie; ordinal/intervall/Verhältnis unterscheiden, Kalibrierung und Unsicherheit; für abstrakte Fähigkeiten psychometrische Konstruktvalidität und Validierung am beabsichtigten Einsatz.
**Sociotechnisch:** Wer legt Gewichte, Schwellen und Population fest? Wie verändern Rankings und Messung das Verhalten?

## 4. Kritiktraditionen
- Sokratische Frage nach einer Definition, später philosophische Definitionstheorie.
- P. W. Bridgman (1927): operationalistische Definitionen; selbst umstritten als universelle Begriffstheorie.
- Cronbach & Meehl (1955): Konstruktvalidität psychologischer Tests.
- Goodhart/Strathern und Campbell: bei Verwendung von Indikatoren als Ziel entstehen Anpassungs- und Korruptionsanreize; keine deterministische Universalregel.
- Theodore Porter (1995): die Macht von Quantifizierung und Zahlen als scheinbar objektive Entscheidungsgrundlage.
- Wendy Espeland & Michael Sauder (2007): Rankings verändern Institutionen, die sie bewerten.
- Sally Engle Merry (2016): politische und kulturelle Annahmen hinter Indikatoren.
- Cathy O'Neil (2016): gesellschaftliche Risiken opaker, folgenreicher algorithmischer Scorings.
- Eriksson et al. (2025): Review von ca. 110 KI-Benchmarkstudien zu Kontamination, Konstruktvalidität, Gaming, Verzerrung und Fehlanreizen.
- Bean et al. (NeurIPS 2025): 445 untersuchte LLM-Benchmarks mit Problemen der Konstruktvalidität.
- Melanie Mitchell (2026): Fähigkeitsbewertungen benötigen Kontrollen, Robustheit, Mechanismen, Trennung Performance/Kompetenz und negative Fälle.
- Jiang et al. (Microsoft Research, 2026): Item-Level-Daten statt bloßer aggregierter Scores.

## 5. Beispiel: eine Logikbehauptung doppelt prüfen
A: „Das System folgt logisch aus widersprüchlichen Angaben.“ Unter klassischer Explosion ist B aus A und ¬A ableitbar. Unter parakonsistenten Konsequenzrelationen im Allgemeinen nicht. Ein „richtiger Schluss“ hängt also vom vorab ausgewiesenen Kalkül ab. Das ist ein formaler Vergleich, nicht das Experiment eines bestimmten LLM.
B: „Die KI denkt logisch.“ Ein Benchmark korrekter Multiple-Choice-Antworten kann spezifische Aufgabenleistung messen; Robustheit, Ableitungsmechanismus und Generalisierung verlangen zusätzliche Untersuchungen.

## 6. Meta-Benchmark-Objekt
Claim → Begriff → Definitionstyp und Alternative → Theorie/Logiksystem → Operationalisierung → Testelemente/Population → Messskala → Auswerter → Unsicherheit → Schwelle → Anreiz/Wirkung → Gegenprobe → Geltungsbereich → Revision.
Jede Verbindung wird versioniert und mit Originalquelle, Autorrollen und Evidenzstatus gespeichert. Eine Begriffsdefinition ist keine Messung; ein Messwert ist keine Gesamtaussage.

## 7. Zwei vorgeschlagene Experimente
EXP-LOGIC-01: Protokolliere eine feste Sammlung von 30 Inferenzaufgaben und ihre Gültigkeit in klassischer und explizit gewählter parakonsistenter Semantik. Ausgaben: truth_tables.csv / model_checks.json / fulltext.md. Kontrollen: Gegenmodell, Syntaxprüfung; keine aktuelle Testerledigung.
EXP-METRIC-01: Simuliere ein einfaches Entscheidungssystem unter zwei Zielmaßen, kurzfristigem Output und langfristiger Ressourcenstabilität. Vorher Ziel/Parameter/Schwellen offenlegen; Sensitivitätsanalyse, Negativbeispiele und Kosten der Messung. Keine Ausführung behauptet.

## 8. Lern- und Leserpfad
„Was ist überhaupt etwas?“ → Definitionen vergleichen → Logik als Gültigkeitsrelation → Beweis vs. Weltwissen → Was zählt als Messen? → Benchmark des Benchmarks → KI-Intelligenz → Gesellschaftliche Folgen → eigenes Prüfexperiment → moderierter Autor-/KI-/Leser-Thread → Papers.

## Literatur, überprüfbare Einstiege
https://plato.stanford.edu/entries/logic-classical/
https://plato.stanford.edu/entries/logical-pluralism/
https://plato.stanford.edu/entries/definitions/
https://plato.stanford.edu/entries/operationalism/
https://plato.stanford.edu/entries/measurement-science/
https://plato.stanford.edu/entries/wittgenstein/
https://pubmed.ncbi.nlm.nih.gov/13245896/
https://pmc.ncbi.nlm.nih.gov/articles/PMC7901608/
https://doi.org/10.1086/517897
https://www.iilj.org/publications/the-seductions-of-quantification/
https://ojs.aaai.org/index.php/AIES/article/view/36595
https://proceedings.neurips.cc/paper_files/paper/2025/hash/1967e0fc3aa6cbbace562f5cb8e3954e-Abstract-Datasets_and_Benchmarks_Track.html
https://doi.org/10.1002/aaai.70061
https://www.microsoft.com/en-us/research/publication/ai-evaluation-should-require-standardized-item-level-data-releases/

**Grenze:** Forschungsentwurf, nicht unabhängig begutachtet und nicht als live Website publiziert. Die Antwort aus dieser Chat-Runde wird nicht automatisch wortgleich als Originaltext archiviert.
