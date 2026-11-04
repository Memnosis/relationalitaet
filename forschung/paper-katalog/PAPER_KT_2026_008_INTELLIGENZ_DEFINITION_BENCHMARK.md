---
id: PAPER-KT-2026-008
title: Intelligenzbehauptungen, Definitionen und Benchmark-Geltung
version: 0.1.0
date: 2026-11-04
status: research_draft_not_peer_reviewed
privacy: public_research_draft
related: [PAPER-KT-2026-007, PATH-KI-INTRO, PATH-SELF-LEARN]
---
# Ist KI intelligent? Definition, Messung, Behauptung und Geltung

## Forschungsfrage
„Ist KI intelligent?“ ist ohne Definition und Prüfdesign nicht empirisch entscheidbar. Grundfrage: Was genau wird dem System zugeschrieben, welche Definition wird verwendet, welche Aufgaben und Messwerte werden eingesetzt, und wie weit darf das Resultat verallgemeinert werden?

## Formale Prüfstruktur
Jede Befundakte speichert: `claim_id, claim_text, definition_id, operationalization_id, benchmark_id, benchmark_version, task_distribution, model_id, model_version, harness_id, tool_access, context_budget, inference_effort, sample_size, evaluator, metrics, confidence_interval, contamination_controls, human_baseline, negatives, scope_limits, evidence, source_refs, release_status`.

Logische Grenze: `score(system, benchmark, conditions)` beschreibt eine Leistung *unter Bedingungen*, keine allgemeine metaphysische Eigenschaft.

## Konkurrierende Definitionen
- Erfolg bei bekannten Aufgaben / spezialisierte Kompetenz.
- Effizientes Erlernen neuer Fähigkeiten / Vorwissen / Transfer (Chollet, ARC).
- Zielgerichtetes Entscheiden unter Umweltunsicherheit (agentische Konzeption).
- Allgemeine Transferfähigkeit über Domänen.
- Menschlich vergleichbare Fähigkeiten nach Fähigkeitsdimensionen (OECD).
- Metakognition, Selbstkontrolle, Unsicherheitskalibrierung, Fehlerkorrektur.
- Philosophische Fragen zu Verstehen, Subjektivität oder Bewusstsein: nicht aus einem Benchmark-Score ableiten.

## Benchmarkatlas: wissenschaftlicher Startbestand
| Framework / Familie | Was gemessen wird | Besondere Grenze |
|---|---|---|
| OECD AI Capability Indicators (2025) | neun menschliche Fähigkeitsdomänen | Niveaustufen sind ein Rahmen, kein universeller Intelligenzbeweis |
| Stanford HELM | mehrdimensional: Genauigkeit, Robustheit, Fairness, Kalibrierung, Effizienz etc. | ab 2026-06-01 maintenance mode; Versionen festhalten |
| ARC-AGI-2 | abstrakte Regelableitung, Generalisierung unter wenig Erfahrung | enge Aufgabenform, keine umfassende AGI-Prüfung |
| LiveBench | erneuerte objektiv auswertbare Aufgaben, Kontaminationsreduktion | versionsgebundene Domänenauswahl |
| Artificial Analysis Intelligence Index | zusammengesetzte aktuelle Spitzenfähigkeiten | Versionen wechseln Aufgaben/Schwierigkeitsmix |
| Artificial Analysis Progress Index v1 | historische Vergleichbarkeit über IRT-Linking | Schätzung mit Modellannahmen |
| METR Time Horizon | Erfolgswahrscheinlichkeit bei Aufgaben unterschiedlicher menschlicher Dauer | überwiegend Software/ML/Security, keine „Autonomiezeit“ |
| SWE-bench Verified / Pro | Repository-Fehlerbehebung | Verified durch Kontamination/fehlerhafte Tests nur eingeschränkt |
| eigene Forschungsbenchmarks | spezifische Forschungs- und Mitmachaufgaben | ohne Blindtests, unabhängige Referenzen und Baselines keine starken Schlüsse |

## Beispiel: „Selbstlernen“
Definition D1: Verbesserung nach neuen Beispielen in derselben Unterhaltung. Test: Trainings-/Testaufgaben, Leistung vorher/nachher, gleicher Prompt; mögliche Kontextanpassung.
Definition D2: persistente Änderung über Neustart/Sessions ohne erneuten Kontext. Test: Modellzustand/externes Gedächtnis unterscheiden.
Definition D3: neue Regel zu neuem Aufgabentyp übertragen. Test: kontrollierte Distribution-Shift-Aufgaben.
Definition D4: Fähigkeit selbständig Aufgaben/Ziele/Feedback zu wählen. Test: offenes Umweltmodell mit Sicherheitsgrenzen.
Dieselben Ergebnisse können D1 stützen und D2–D4 unentschieden lassen.

## Qualität und Gültigkeit
- Konstruktvalidität: misst die Aufgabe die behauptete Eigenschaft?
- Inhaltsvalidität/Abdeckung und Sprach-/Domänenverzerrung.
- Reliabilität (Streuung über Läufe, Prompts und Modelle).
- Kontamination und Benchmark-Gaming; private/zeitversetzte Kontrollaufgaben.
- Evaluator-Fehler, Nachweis von Testfehlbewertungen.
- Konfigurationskontrolle (Werkzeuge, Webzugang, Systemprompt, Thinking-Budget, Kontext).
- Human-Baseline mit vergleichbaren Rahmenbedingungen.
- Kosten, Latenz, Energie/Compute, Lernaufwand.
- Einzelscores nicht als Endurteil; disaggregiert, Unsicherheitsintervalle und negative Fälle.

## Didaktischer Forschungsweg
Behauptung → Begriffsvarianten → Definition → Operationalisierung → Benchmarkwahl → Kontrollversuche → Resultate → Grenzen/Gegenbeispiele → Paper und Diskussion → Revision. Teilnehmende können dieselbe Aussage unter zwei Definitionen prüfen.

## Leser-/Autor-/KI-Diskussion
A: GitHub Discussions als gemeinsames thematisches Forum für Autor und Leser; eigene KI-Ergebnisse werden als klar gekennzeichnete Beiträge eingefügt.
B: Discourse oder eigenes Thread-Backend mit integrierten KI-Bots und Moderation.
C: Leser bindet seinen Agenten über eine dokumentierte Schnittstelle ein (später), mit Zustimmung, Authentifizierung, Datenschutz und Kostenkontrolle.
Ein ChatGPT-Freigabelink ist keine gemeinsame Live-Unterhaltung. Seit 09.07.2026 sind neue ChatGPT-Gruppenchats nicht mehr erstellbar.
Nicht automatisch fingieren, dass eine Botantwort vom menschlichen Autor stammt.

## No-Loss-Outputvertrag
Volltext-Paper, definitionen.json, benchmark_catalog.json, tasks.jsonl, runs.jsonl, assessments.csv, provenance/RO-Crate, erlaubte Website-Projektion. Konkrete Quellen und Originale erhalten; strukturiertes Register nur *zusätzlich*.

## Quellen
- OECD: https://www.oecd.org/en/publications/introducing-the-oecd-ai-capability-indicators_be745f04-en.html
- HELM: https://github.com/stanford-crfm/helm
- HELM Konzept: https://crfm.stanford.edu/2022/11/17/helm
- ARC-AGI-2: https://arcprize.org/arc-agi/2
- LiveBench: https://livebench.github.io/
- Artificial Analysis Index v5: https://artificialanalysis.ai/indexes/
- Progress Index: https://artificialanalysis.ai/methodology/progress-index/
- METR: https://metr.org/time-horizons/
- SWE-bench-Verified-Audit: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- GitHub Discussions: https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions
- ChatKit: https://developers.openai.com/api/docs/guides/chatkit
- ChatGPT Group Chat Retirement: https://help.openai.com/en/articles/12703475-group-chats-in-chatgpt
- ChatGPT shared links: https://help.openai.com/en/articles/7925741-sharing-conversations-and-scheduled-tasks-in-chatgpt

**Noch nicht geschehen:** Vollständige Benchmark-Originaldaten importiert; Modelle gemessen; Leser-Thread angelegt; öffentliche Freigabe.
