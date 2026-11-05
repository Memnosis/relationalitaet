# Bürger-KI – Doppelungsanalyse und schlankes Sprachverfahren
## Ein konkreter No-Loss-Test des eigenen Wissensmanagements

**ID:** BKI-LANG-DEDUPE-001 · **Stand:** 2026-11-05 · **Status:** Bestandsanalyse und umsetzbarer Vorschlag, keine automatische semantische Engine oder fachliche Abnahme.  
**Primärreferenz:** [Zwischen Worten und Wirklichkeit](../../docs/paper-buerger-ki-sprachraeume-termini-operationalisierung-claims-v0-1.md), **41.303 Zeichen** (zum Prüfzeitpunkt).  
**Weitere Bestände:** [Phase 15](../../docs/buerger-ki-phase-15-sprache-uebersetzung-no-loss.md), [Sprachwelten](./SPRACHWELTEN_FACHGEBIETE_DREHPUNKTE_QUELLENPLAN_V0_1_2026-11-05.json), [vorläufige Phase-1-Fälle](./PHASE_1_SEMANTISCHE_UEBERGAENGE_V0_1.json), [Pfadelementinventar](./SPRACHPFADE_ELEMENTINVENTAR_V0_1.json).

## 1. Befund: Wir haben dieselbe fachliche Ebene mehrfach gebaut

| Ort | Was bereits dort steht | Bleibt dort | Was hier NICHT neu geschrieben wird |
| --- | --- | --- | --- |
| Sprachräume-Paper, Kap. 2–6, 9–10, 15 | Sprachräume, Termini, Bedeutungen, Operationalisierung, Perspektivwechsel, sechs Übersetzungsarten, Tests | **Kanonische fachliche Referenz** | keine erneute Volltheorie der Übersetzungsarten |
| Phase 15 | Arbeits- und Synchronisierungsschritte, Crosswalk, Auditstatus | historische Prozess- und No-Loss-Akte | keine zweite Übersetzungsontologie |
| Sprachwelt-Kartographie | Fachgebiete, Drehpunkte, Prioritäten, Darstellungszweck und Phasen | **Navigations- und Prioritätskarte** | keine detaillierten Skillimplementierungen |
| 14 Phase-1-Übergänge | Beispiele mit Quellen- und Prüfbedarf | **vorläufige Testkandidaten** | keine Behauptung, die Phase sei schon fachlich abgeschlossen |
| Code/Psychologie/Tensor | Sonderfälle von Operationalisierung, Syntax, Semantik und Invertierbarkeit | **Forschungsparkplatz** | kein pauschaler Technikbau als Pflicht vor jedem Lernweg |

**Ursache der Doppelung:** Ein Phasenübergang wurde zunächst inhaltlich erneut ausgearbeitet, ohne fachliche Referenz, Umsetzungsartefakt, Testfall und Forschungsvertiefung getrennt zu halten. Dieselbe Aussage erschien mehrfach unter neuen Überschriften. Das erschwert Quellen- und Versionssynchronisierung.

**No-Loss-Korrektur:** Nichts löschen oder still zusammenführen. Stabile Bestands-IDs und historische Papers erhalten; neue Versionen verweisen auf die Referenz. Ein wiederholter Gedanke wird mit `reuses`, eine zusätzliche Messregel mit `extends`, ein tatsächlicher Widerspruch mit `conflicts_with` markiert. Nur echte neue Erkenntnisse erhalten neue Fachakten.

## 2. Drei Bearbeitungstiefen statt einer übergroßen Sprachmaschine

**L0 – Direkter redaktioneller Übersetzungsauftrag.** Ein Mensch oder eine KI formuliert eine Aussage in einem anderen Sprachraum, notiert den Unterschied und nennt Quellenbedarf. Ergebnis: kurze, überprüfbare Karte. Keine eigene Software erforderlich.

**L1 – Strukturierte, rückprüfbare Übersetzungsakte.** Nur bei fachlich relevanten Übergängen: ursprünglicher Satz, Zielpublikum, Geltung, erhaltene Bedeutung, zusätzliche Annahme, Bedeutungsverlust, Quellenstatus, Rückübersetzung und mindestens ein Gegenbeispiel. Hier helfen Vorlagen, JSON und einfache Validatoren.

**L2 – Forschung zu Code, Psychologie, Ontologien und Tensor.** Für Fälle, in denen L0/L1 unzureichend sind: Syntax/AST, Formalisierung, relationale Algebra, psychologische Konstruktvalidität, Tests, umkehrbare bzw. nicht invertierbare Abbildungen. Separates Forschungspaket nach konkretem Fehlfall; kein automatischer Bestandteil jeder öffentlichen Seite.

**Eskalationsregel:** L0 zuerst. Zu L1, wenn ein Missverständnis Quellen, Rechte, Entscheidungen oder die Fachbedeutung betrifft. Zu L2, wenn echte Formal-, Daten-, Code- oder empirische Beweisfragen entstehen, die L1 nicht zuverlässig beantwortet.

## 3. Einfacher Mitmach-Prompt als produktiver Kern

> **Übersetze die folgende Aussage für die angegebene Perspektive oder Fachsprache, ohne sie stärker zu machen als das Original: [AUSSAGE]. Ausgangssituation: [KONTEXT]. Ziel: [ALLTAG / FACH / RECHT / GESELLSCHAFT / FORSCHUNG / CODE]. Gib (1) eine verständliche Formulierung, (2) die erhaltene Aussage, (3) neue Annahmen oder Bedeutungsverluste, (4) eine entscheidende Gegenfrage oder ein Gegenbeispiel und (5) höchstens drei konkret benötigte Quellen oder Fachprüfungen. Wenn etwas nicht gleichwertig übersetzbar ist, sage dies ausdrücklich.**

Die Promptausgabe ist **ein Kandidat**, kein validierter Fachbefund. Für Öffentlichkeit Fachquellen/Review, für Code ggf. Tests, für rechtliche Behauptungen einschlägige Norm und Geltungsraum nachziehen.

**Noch kürzer, für einen Bürger-KI-Pfad:**
> „Erkläre diesen Satz aus einer anderen Perspektive. Was verändert sich, was darf ich daraus gerade nicht schließen, und wo kann ich das nachprüfen?“

## 4. Beispiel: Ein Satz genügt für einen nützlichen Test

**Ausgang:** „Ich finde keinen Therapieplatz.“
- **Alltag → Hilfe:** „Welche konkreten Such- und Vermittlungswege kommen für die gesuchte Behandlung infrage?“
- **Alltag → Wissen:** „Welche Leistungen sind Sprechstunde, Akutbehandlung, Probatorik und längerfristige Psychotherapie?“
- **Alltag → Gesellschaft:** „Welche Daten würden zeigen, dass geeignete Behandlungen für eine definierte Gruppe tatsächlich nicht zugänglich sind?“
- **Zurück:** „Was habe ich über meinen möglichen nächsten Schritt erfahren?“

Die drei Übersetzungen sind **andere Fragen**, keine synonymen Sätze. Ihre zusätzlichen Fachannahmen und Grenzen müssen sichtbar sein. Keine medizinische Indikation, Kausalität oder Pflichtverletzung wird dadurch bewiesen.

## 5. Wie der Mitmach-Auftrag in die bestehende Forschung gelangt

`Ausgangssatz → übersetzte Frage → Semantik-/Gegenprobe → Quellenbedarf → [freigegebene] Pfadkarte`.

Wenn der Auftrag eine offene Frage erzeugt, kann er als **Forschungsauftrag** weitergeleitet werden, ohne den ursprünglichen Satz oder seine Kontextgrenzen zu verlieren.

- `BKI-LANG-TASK`: konkrete Aufgabe oder Mitmach-Prompt, Status `proposed`.
- `BKI-LANG-CASE`: Übersetzungsbeispiel, Quellenstatus und mögliche Fehler.
- `BKI-TR`: erst bei strukturiertem Prüfbedarf; bestehender reservierter Namensraum wiederverwenden.
- `BKI-TEST`: nur bei wirklich definiertem Gegenbeispiel oder Test; keine fiktive bestandene Prüfung.
- `BKI-XW`: nur geprüfte, getypte Relationen.
- `SRC`/Glossar/Claims/Skills: **Originaleigenschaft bleibt** beim jeweiligen bestehenden Register.

Keine zusätzliche universelle Datenbank. Keine Doppelpflege von Definitionen. Der No-Loss-Compiler muss einen neuen oder geänderten Übersetzungsfall dem Eigentümerregister zuordnen, bevor ein öffentlicher Claim geändert wird.

## 6. Forschung parken, ohne sie zu verlieren

| Forschungsfrage | Wann sie sinnvoll zu öffnen ist | Vorher genügt |
| --- | --- | --- |
| psychologisches Konstrukt ↔ Codevariable | eine konkrete fachlich unklare Operationalisierung | L0/L1, Theoriebegriff und Unterscheidung |
| unterschiedliche natürliche Sprachen/Rechtsräume | tatsächlich vergleichende oder internationale Fragestellung | ein expliziter Rechtsraum im Kontext |
| AST/Parser und typsichere Skill-DSL | mehrere tatsächlich notwendige wiederkehrende Übersetzungen | Prompt und JSON-Prüfung |
| formale Umkehrbarkeit / Tensoralgebra | definierter Operator, Definitionsbereich und Gegenfall | Bedeutungsverlust und Gegenbeispiel in Worten |
| LLM-Evaluation/Bias/Robustheit | reproduzierbare Fälle, Benchmarkbedarf | fachlich gegengeprüfte Beispiele |
| semantische Ontologie-/Graphautomatik | genügend überprüfte Begriffe und Relationstypen | kuratierte Links und bestehende IDs |

**Forschungsrückweg:** Nach Sprachphase und ihrer Abnahme den geplanten Deep Dive zu Skills, Datenbanken, Schnittstellen, Formalisierung und Tensor durchführen. Er bezieht konkrete Fehlerfälle und funktionierende Übersetzungsmethoden ein.

## 7. Phasen-Gate korrigieren

Die Phasenkartographie hat **neun Stufen, Phase 0–8**. Vor **SW-PH-1** steht jetzt ein kleines `SW-PRE-LANG`-Gate, ohne zehnte Hauptphase:

1. Primärreferenz des Sprachräume-Papers festlegen.
2. Doppelungen als Crosswalk und nicht als zweite Fachdatenbank behandeln.
3. L0-Prompt und einfache Reviewkarte fachlich/technisch als MVP freigeben.
4. **Erst dann** die vorhandenen 14 Beispiele durch Phase 1 testen.

Das Register der 14 Fälle bleibt bis dahin `pre_phase_material_not_validated`. Kein „Phase 1 bestanden“ ohne tatsächliche inhaltliche und fachliche Gegenproben.

## 8. Ergebnis

Die erste hilfreiche Bürger-KI-Sprachfunktion ist **kein großer automatisierter Übersetzungsdienst**, sondern eine gute Frage, ein präziser Prompt, eine fachlich verantwortbare Gegenprobe und ein nachvollziehbarer Link. Wiederkehrende Aufgaben lassen sich später in Skills verdichten; aufwendige Code-/Psychologie-Forschung bleibt sichtbar, aber sie blockiert nicht die menschliche Nutzung.
