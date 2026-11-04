# Forschungsprogramm: Prompt-, Skill- und Agentenverdichtung
Stand: 2026-11-04 | Status: Forschungsentwurf, keine Evidenzfreigabe
Scope: neue Forschung als Zusatz zu historischen Artefakten, keine Überschreibung der Vorarbeiten.

## Forschungsfragen
F1: Welche explizit formulierbaren Fähigkeitsanforderungen enthält eine einzelne Anfrage?
F2: Wie viele davon werden nachweislich von expliziten Skills/Tools bearbeitet, wie viele werden im Modellverhalten beobachtet?
F3: Welche Kombinationen können als wiederverwendbare Skills komprimiert werden, und bei welcher Qualität/Kostenbilanz?
F4: Wann lohnt sich agentische Orchestrierung gegenüber einer einzelnen Modellanfrage oder einer deterministischen Funktion?
F5: Welche intern kausalen Mechanismen sind nur bei Open-Weight-Modellen mit Aktivierungszugriff überprüfbar?
F6: Welche historischen KI-Entwicklungswege sind tatsächlich vergleichbar, statt ältere Systeme pauschal als nicht intelligent zu bezeichnen?
F7: Wie kommunizieren Mensch, Entwickler, externe KI und die beiden Forschungs-KIs über überprüfbare, versionierte Aufgaben- und Ergebnisobjekte?

## Begriffliche Trennung
- *Anforderung/Kompetenz*: vom Prompt oder Test verlangte Leistung.
- *Skill (extern)*: portable, versionierte und ausdrücklich ausführbare/lesbare Prozedur.
- *Skill (latent)*: hypothetisch/empirisch operationalisierte modellinterne Fähigkeit, **nicht** unmittelbar aus einem Antworttext abzählbar.
- *Agent*: System mit Zustands-/Aktionsschleife, Werkzeugen, Beobachtungen und gegebenenfalls autonomer Planung; kein Synonym für eine komplexe Welt.
- *Welt/Umgebung*: Zustand, zulässige Aktionen, Beobachtungen, Dynamik, Ziele und Randbedingungen.

## Konkurrierende Hypothesen
H1: Ein kleiner Satz komprimierter Skills erzielt bei wiederholten Aufgaben gleiche Qualität mit geringerem Aufwand.
H2: Leistung stammt aus flexibler verteilter Modellrepräsentation; explizite Skillkataloge beschreiben nur die Oberfläche.
H3: Eine Mixtur aus Modell, externen Skills und dynamischer Orchestrierung ist besser als jedes isolierte System.
H4: Klassische symbolische/deterministische Systeme übertreffen generative Systeme in engen, prüfbaren Domänen.
H5: Agentische Mehrschrittprozesse erhöhen Aufwand/Fehler und sind für manche Aufgaben schlechter.
H6: Gemeinsame Operatoren und semantische Relationen erlauben domänenübergreifenden Transfer, aber nicht automatisch eine einheitliche Tensoralgebra.

## Experimentdesign — präregistrierbare Vergleichsbedingungen
Ein und dieselbe Aufgabensammlung unter:
A. Basismodell ohne Skill-Paket;
B. Basismodell + langer Originalprompt;
C. Basismodell + atomare Skills;
D. Basismodell + komprimierter Meta-Skill;
E. Agent mit Tools, Planungs-/Prüfschleife;
F. deterministische oder klassische Baseline.
Über randomisierte Aufgabenreihenfolge, feste Datensplits, Blindbewertung und Wiederholungen vergleichen.
Aufgabenfamilien: Formeln, geometrische Transformation, Quellenprüfung, Schreibrevision, Webnavigation, Datenschema; keine echten personenbezogenen Daten.
Messgrößen: Korrektheit, Reproduzierbarkeit, Kosten/Token, Latenz, Toolaufrufe, Korrekturschleifen, Fehlertyp, Transfer auf neue Domäne und Sicherheitsverletzungen.
Wichtig: Tokenzahl ist keine belastbare Zählung latenter Skills. Interne Mechanismen nur unter dokumentiertem White-Box-Zugang behaupten.
Ein Skill-Count ist je nach Zählebene (Kompetenz/Prozedur/Tool/Neuron/Circuit) etwas anderes.

## Historische Forschungswege
Symbolische KI/Logik und Suche; statistische Verfahren; neuronale Netze/Backpropagation; tiefe CNNs; Transformer und selbstüberwachtes Vortraining; Skalierung/Daten-Rechenbudget; Instruction-Tuning/Präferenzoptimierung; Tool-Use/Agenten; Mechanistic Interpretability; hybride/neurosymbolische Systeme. Bewertung nicht nach „intelligent/uninteressant“, sondern nach Ziel, Benchmark, Verallgemeinerung, Kosten und Fehlermodus.

## Zugang zu „KI-Code“ — zu unterscheidende Schichten
1. Trainings- und Inferenzsoftware;
2. Architektur und Tokenizer;
3. Gewichte/Checkpoints;
4. Trainingsdaten und Datenherkunft;
5. Optimierer/Hyperparameter/Trainingsverlauf;
6. Inferenz-Harness, Tools, Systemkonfiguration;
7. Interne Aktivierungen/Gradienten und Interventionszugang;
8. Nur API-Eingabe/-Ausgabe (Black Box).
Die Behauptung „man kommt nicht an den KI-Code“ ist ohne Modell- und Schichtbezug falsch. Es gibt Open-Source-, Open-Weight- und proprietäre Varianten. Rechtliche Lizenz- und Zugriffsmöglichkeiten getrennt untersuchen.

## Versioniertes Ausgabepaket je Versuch
- `research_report.md`: vollständiger Kontext, Methoden, Gegenargumente, Negativergebnisse.
- `protocol.json`: genaue Konfiguration, Quellen, Prompt-/Skill-Versionen, Privacy-Klasse.
- `requests.jsonl`: pseudonymisierte/consentierte Aufgaben, Kompetenzannotation.
- `runs.jsonl`: Ergebnis, Messwerte, Fehler; kein ungeprüfter Chat-Export.
- `skill_graph.json`: Skills, Kompositionen, Abhängigkeiten und Alternativen.
- `analysis.csv`: aggregierbare Messwerte und Unsicherheiten.
- `reproduction.py`: Prüfprogramm mit Testdatensatz.
- `ro-crate-metadata.json`: Gesamtobjekt und externe Literatur.
- `public_projection.json`: redigierte Website-Sicht nach Freigabe.
Jede Quelle/Glossar-/Skilländerung löst einen Impact-Nachzug aus. Alte Versionen bleiben unverändert.

## Quellen / Startlektüre
- Vaswani et al. (2017): https://arxiv.org/abs/1706.03762
- Kaplan et al. (2020): https://openai.com/index/scaling-laws-for-neural-language-models/
- ReAct (ICLR 2023): https://mlanthology.org/iclr/2023/yao2023iclr-react/
- Anthropic circuit tracing (2025): https://www.anthropic.com/research/tracing-thoughts-language-model
- Agent Skills survey (Google Research 2026): https://research.google/pubs/a-survey-on-agent-skills-externalized-procedural-knowledge-in-language-models/
- Microsoft skill lifecycle (2026): https://www.microsoft.com/en-us/research/publication/from-raw-experience-to-skill-consumption-a-systematic-study-of-model-generated-agent-skills/
- Open Source AI Definition: https://opensource.org/ai/open-source-ai-definition

## Freigaberegel
Originale niemals als erledigt markieren, ohne Originalfundstelle, SHA, spezifischen Test und Gegenprüfung. Öffentliche Git-Dateien sind öffentlich – keine privaten KIsynchronisationen oder unveröffentlichten Rohdialoge dort ablegen.
