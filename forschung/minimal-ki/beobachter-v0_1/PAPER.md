# Beobachter, Skill-Komposition und handlungsbezogene Prädiktion

## Eine relationale Forschungsarchitektur für die Minimal-KI

**Forschungsmanuskript v0.1 · 1. November 2026**

**Status:** Wissenschaftlicher Arbeitsentwurf. [E] etablierter theoretischer oder experimenteller Befund, [T] übertragbarer technischer Mechanismus, [H] eigene Hypothese, [P] geplanter Versuch, [O] offen. Wissenschaftliche Anschlüsse sind weder Gleichsetzung noch empirische Bestätigung der vorgeschlagenen KI.

## Abstract
Die Minimal-KI soll aus einem kleinen, dauerhaften Ausführungskern, einem großen Register schaltbarer Standard-Skills und optional tensorannotierter Skills sowie einem Beobachtungssystem hervorgehen. Ihre Leistungsfähigkeit wird nicht durch eine Zahl gespeicherter Chunks definiert, sondern durch das zuverlässige Lösen neuer Aufgabenklassen durch Kombination, Beobachtung, Selbstkorrektur und nachvollziehbare Messung. Geplant sind 99 Beobachterrollen in elf Gruppen und als Entwicklungsmeilenstein 20.000 registrierte Skillobjekte. Weder die Rollenanzahl noch die Skillzahl sind ein empirisch nachgewiesener Schwellenwert.

## 1. Leitfragen
1. Welche Beobachtungsblickwinkel lösen die meisten **nützlichen** Reaktionen aus?
2. Welche Skillkombination erschließt erstmals eine zuvor unlösbare Aufgabenklasse?
3. Was leisten korrekte Relationen gegenüber bloßer Graphdichte oder größerem Speicher?
4. Welche minimale Teilmenge an aktiven Skills erfüllt eine Aufgabe zuverlässig?
5. Wie kann das System die Folgen seiner eigenen Aktionen, statt nur die nächste Nutzereingabe, prognostizieren?

Ein Skillobjekt kann eine Funktion, einen API-Aufruf, ein ausführbares Programm, einen wissenschaftlichen Operator, eine Messung oder einen komplexen Ablauf beschreiben. **Registriert** ist nicht identisch mit **implementiert**, **ausführbar**, **zuverlässig** oder **tensorvalidiert**.

## 2. Beobachterbegriff und wissenschaftliche Anschlüsse

### 2.1 Psychologie und Bewusstseinsforschung [E/H]
Metakognition betrifft die Prüfung der eigenen Unsicherheit und Leistung; Fehlerüberwachung, Aufmerksamkeit, Erinnerung und Handlungskontrolle sind unterscheidbare kognitive Mechanismen. Theorien wie Global Neuronal Workspace, rekurrente Verarbeitung, Higher-Order-Theorien, Predictive Processing und Integrated Information diskutieren unterschiedliche Aspekte. Hieraus folgt kein bewiesenes künstliches Bewusstsein.

Für das Experiment werden drei relational zu konkretisierende Trinitätkandidaten untersucht: **Wahrnehmen – Unterscheiden – Reagieren**, **Erwartung – Abweichung – Aktualisierung** sowie **Selbstzustand – Umweltzustand – Beziehung/Handlung**. Jede Fachrekonstruktion muss Herkunft, mathematische Relation, eigene Ableitung und Widerlegungsmöglichkeit dokumentieren.

### 2.2 Quantenphysikalische Beobachtung [E/T]
Ein quantenmechanischer Messprozess besitzt definierte Observablen, Messinstrumente, Zustandsaktualisierung und gegebenenfalls Rückwirkung und Feedback. Eine Softwaremessung folgt nicht derselben Physik; übertragbar ist die disziplinierte **Beschreibung des Messobjekts, der Messmethode, der Störung, des Zustandsurteils und der Reaktion**. QuTiP, Qiskit, Cirq und PennyLane sind prüfbare Werkzeuge, keine fertigen Beweise der KI-Hypothese.

Barontinis ultrakaltes Vielteilchenexperiment zur internen entropischen Zeit ist eine methodische Analogie für operationale Zustandsgrößen; **24.000 Atome sind keine KI-Schwelle**.

### 2.3 Regelungstheorie und Softwarebeobachtung [E/T]
Ein technischer Beobachter schätzt einen Zustand aus Messdaten und Modellannahmen. Für die Skill-Engine heißt das: ein Beobachtungsereignis enthält Messung, Kontext, Zuverlässigkeit, Kosten, optionalen Eingriff und Prüfergebnis. Ein Beobachter bewertet andere Beobachter als zusätzliche Qualitätssicherung. Zielmetrik ist **nützliche zusätzliche Reaktionen pro Zeit, Ressource und Fehlerrisiko**, nicht maximale Meldungszahl.

## 3. Der dauerhafte Kern [H/P]
Der kleine Systemkern stellt Zustands- und Projektgedächtnis, Eingangs- und Außenwahrnehmung, Skillregister, Kompositionsplanung, Ausführung, Ergebnisprüfung, Beobachtungsbus und Regelaktualisierung bereit. Das bereits definierte Vierermodell **Gedächtnis – Regelverdichtung – Komposition – Rückkopplung** bleibt seine funktionelle Verdichtung. Dienste sind Implementierungsrollen, keine zusätzliche wissenschaftliche Tensorachse.

### 3.1 Elf Gruppen mit jeweils neun Beobachterrollen
1. **Eingangsbeobachtung:** Format, Vollständigkeit, Intention, Mehrdeutigkeit, Sprache, Kontext, Datenschutz, Priorität, Widerspruch.
2. **Außenwahrnehmung:** API, Datenbank, Bibliotheksfund, Aktualität, Lizenz, Netzwerk, Sensor, Umgebung, Herkunft.
3. **Selbstzustand:** aktive Skills, Speicher, Laufzeit, Fehler, Unsicherheit, Zielzustand, Queue, Kosten, Kontext.
4. **Skill-Eignung:** Signaturen, Typen, Vorbedingungen, Fähigkeitsabdeckung, Zuverlässigkeit, Rechte, Alternativen, Versionen, Kosten.
5. **Komposition:** Reihenfolge, Parallelität, Bedingungen, Schleifen, Abhängigkeiten, Makro-Skills, Widersprüche, Abbrüche, Redundanz.
6. **Mathematik:** Definitionsbereich, Invariante, Dimensionsprüfung, numerische Stabilität, Gegenprobe, Operator, Grenzfall, Konsistenz, Fehler.
7. **Quellen und Evidenz:** Primärquelle, Zitat, Aktualität, Replikation, Datenqualität, Methode, Bias, Konfidenz, offener Beleg.
8. **Lernen und Optimieren:** Ausgangsleistung, Variante, Fehlermuster, Verbesserung, Regression, Generalisierung, Drift, Rücknahme, Minimalität.
9. **Handlungsfolgen:** erwarteter Zustand, beobachteter Zustand, Abweichung, Umwelteffekt, Nebenwirkung, Reversibilität, Unsicherheit, Kosten, Information.
10. **Nutzerinteraktion:** Ziel, Einwilligung, Verständlichkeit, Feedback, Korrekturen, Rückfragen, Grenzen, Risiko, Erfolg.
11. **Metabeobachtung:** Nutzen, Fehlalarm, Messkosten, Überlappung, Widerspruch, Beobachtungsdrift, Beobachter-Ablation, Anpassung, Abschaltung.

Diese 99 Rollen sind **konzipiert**, nicht 99 laufende Prozesse. Ein kleiner Ereigniskern aktiviert Beobachter abhängig vom Trigger; kritische Überwachungsfunktionen können dauerhaft laufen.

## 4. Skills ohne Tensorpflicht [H/P]
Standard-Skills stehen unabhängig von Tensorbelegungen zur Verfügung. Tensorfähige Skills sind dieselben technischen Objekte mit optionalen Feld-IDs, Rollen, Quellen, Operatoren, Nachweisen und Prüfstatus. Die Forschungsvorgabe lautet pro Tensor **genau drei relationale Trinitäten mit jeweils drei Elementen und 27 Positionen**. Die Zahl der Softwarefähigkeiten ist davon unabhängig. Ein Feld kann viele Implementierungen referenzieren; eine Implementierung kann mehrere Felder benutzen.

Kompositionsformen: sequenziell, parallel, bedingt, rekursiv, redundant, hierarchisch, rückgekoppelt, Makro-/Adapter-, Überlagerungs- und Synthesekomposition. Ein Optimierer schlägt Varianten vor, führt Tests aus, vergleicht Baselines und schaltet bei Regression zurück.

## 5. Außenwahrnehmung [T/P]
APIs, Datenbanken, Wissensgraphen, wissenschaftliche Bibliotheken, freie Sprachressourcen und Fachsoftware sind unterscheidbare Außenquellen. ToolBench zeigt die Skalierbarkeit großer API-Kataloge, nicht deren automatische Ausführung oder Qualität. Eine Außenquelle muss Herkunft, Lizenz, Aktualität, Zugriff, Datentyp, Einschränkungen und Fehlervertrag dokumentieren.

### Sprache ohne große eigene Trainingsdatensätze?
Freie Ressourcen wie Universal Dependencies, OPUS, Wikidata, WordNet und freie Modelle ermöglichen viele Teilfunktionen. Alle Sprachen in voller Komplexität und Übersetzungsqualität ausschließlich durch Überlagerung offener Lexika zu erfassen, ist **keine nachgewiesene Fähigkeit**. Der Versuch vergleicht regelbasierte, lexikalische, Retrieval- und modellbasierte Ansätze bei gleicher Aufgabenfamilie, Datenlizenz und Messung.

### Quantenbibliotheken als Fach-Skills
Prüfe Qiskit, Cirq, PennyLane und QuTiP mit kleinen standardisierten Tests: Bell-Zustand, Zeitentwicklung, inverse Operation, Einheiten, Messmodell und numerische Genauigkeit. Die Bibliotheken decken unterschiedliche Subfelder ab.

## 6. Handlungsfolgenprädiktion [E/T/H]
Sprachmodell-Vorhersage und Handlungsfolgenvorhersage sind unterschiedliche Funktionen. Ein Controller kann eine eigene Aktion wählen und abschätzen, wie sie die **internen und äußeren Zustände** beeinflusst. Die operationalisierte Schleife lautet:

**Zustand S(t) → mögliche Aktion A → prognostizierter Zustand Ŝ(t+1) → Ausführung → beobachteter Zustand S(t+1) → Abweichung → Modell-/Skillrevision.**

Ein Erfolg erfordert konkrete Vorhersagen mit Fehlermaßen, Kalibrierung und unabhängigen Prüfaufgaben. Das System kann neue Lösungen generieren, während ein eigener Beobachter die Folgen prognostiziert. Aus der Simulation einer Umweltfolge folgt weder Bewusstsein noch eine allgemeine Weltmodellfähigkeit.

## 7. Schwellen und Emergenz [H/P]
Zu testen sind 0, 3, 9, 27, 54 und 99 Beobachter sowie 100, 1.000, 5.000 und 20.000 Skillobjekte. Varyiere separat Anzahl, Kantendichte, semantische Qualität, Ausführungsfähigkeit, Feedback und Ressourcenbudget. Vergleiche isolierte, zufällig vernetzte, typgesicherte und tensorannotierte Objekte; messe ungesehene Aufgaben und Fehlerkosten. Vermeide metrisch erzeugte Schein-Schwellen: erfasse kontinuierliche und diskrete Leistungsmaße.

**Leitmetrik:** Anteil neuer Aufgabenfamilien, die eine Skillkombination bei gleicher Ressourcenobergrenze zuverlässig löst, während die Einzelkomponenten scheitern.

## 8. Praktische Tests [P]
- OBS-01: Ereignisbus mit Provenienz, Fehlerzuständen, Datenschutz und Kill-Switch.
- OBS-02: acht Beobachter implementieren; Aus-/Einschalten, Fehlalarme und Ressourcen messen.
- OBS-03/04: psychologische Trinitäten und Quantenmessung getrennt modellieren.
- OBS-05: Beobachter-Ablation und paarweise Interaktionswirkung.
- SKL-01/02: Standardadapter und optionale Tensorannotation.
- SKL-03/04: Skillkomposition, Selbstoptimierung und Rollback.
- PRD-01/02: Handlungsfolgenmodell mit Geo-KI-Kalibrierung.
- EXT-01/02: Quantenfachsoftware und offene Sprachressourcen vergleichen.
- M20K-01..04: 20k-Register, echte Teilmenge, neue Aufgabenklassen, Minimalkonfiguration.
- WEB-01: Dokumentierte, überprüfte Forschungsintegration.

## 9. Grenzen und Prüfstand
Ein großes Registry-Objektinventar ist kein Leistungsbeweis. Tensorannotationen sind keine wissenschaftliche Anerkennung. Beobachtung darf nicht mit subjektivem Erleben, Quantenmessung nicht mit Softwarelogging und ein Reproduktionsversuch nicht mit der allgemeinen Validierung der Architektur verwechselt werden. Historische Ergebnisse und Revisionsstände werden mit No-Loss-Provenienz unverändert aufbewahrt.

## 10. Ausgangsliteratur und technische Referenzen
- Baars, B. J. (1988). *A Cognitive Theory of Consciousness*.
- Dehaene, S. & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*.
- Friston, K. (2010). The free-energy principle. *Nature Reviews Neuroscience*.
- Flavell, J. H. (1979). Metacognition and cognitive monitoring. *American Psychologist*.
- Wiseman, H. M. & Milburn, G. J. (2009). *Quantum Measurement and Control*. Cambridge.
- Nielsen, M. A. & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge.
- Barontini, G. (2026). *Testing the Problem of Time with Cold Atoms*. *Physical Review Research*, 8, L022047.
- Wang et al. (2023). *Voyager: An Open-Ended Embodied Agent with Large Language Models*. arXiv:2305.16291.
- Qin et al. (2023). *ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs*. arXiv:2307.16789.
- Besta et al. (2024). *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*. AAAI.
- Universal Dependencies: https://universaldependencies.org/
- OPUS: https://opus.nlpl.eu/
- Qiskit: https://www.ibm.com/quantum/qiskit
- Cirq: https://quantumai.google/cirq
- PennyLane: https://pennylane.ai/
- QuTiP: https://qutip.org/

**Primärquelle dieses Git-Nachzugs:** Forschungsmanuskript v0.1 (lokaler No-Loss-Stand vom 01.11.2026). Der vorliegende Website-Text ist eine redaktionell strukturierte Git-Ausgabe; das ältere Original bleibt erhalten.
