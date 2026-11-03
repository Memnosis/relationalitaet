# Probelauf 01 · LOGIK-PROMPT-02 „Korrektheit und Vollständigkeit“

**Prompt:** LOGIK-PROMPT-02 aus `forschung/tensor/LOGIK_TENSOR_2_1_FORSCHUNGS-UND_PROMPTEDITION_ENTWURF.md` (Blob `fb659e4`, Commit `f3ca054`), Fachprompt wörtlich übernommen.
**Ausgeführt von:** Claude (Daten-KI) am 2026-11-03 · **Ausführungsakte:** [`LOGIK-PROMPT-02_PROBELAUF_01.json`](LOGIK-PROMPT-02_PROBELAUF_01.json)
**Status:** Probelauf für Prüfzwecke. `public_release: not_approved`. Gegenprüfung durch GPT und Freigabe durch Nils stehen aus.

> **Fachprompt:** „Erkläre und beweise für einen exakt spezifizierten Kalkül, unter welchen Voraussetzungen syntaktische Ableitbarkeit semantische Folgerung impliziert; dokumentiere den Umfang des Satzes und einen Vergleich mit einer Logik, für die andere Resultate gelten.“

---

## Antwort

### E1 · Einfach erklärt

Ein Kalkül ist ein Regelwerk zum Umformen von Zeichenketten. Die Semantik sagt, wann eine Aussage wahr ist. **Korrektheit** heißt: Was man mit den Regeln herleiten kann, ist auch wirklich wahr. Für die klassische Aussagenlogik gilt das. In einer anderen Logik, der Gödel-Logik mit drei Wahrheitswerten, gilt es für denselben Kalkül nicht: Dort ist eines seiner Grundgesetze nicht gültig.

### E2 · Der Kalkül und der Satz

**Kalkül H** (Hilbert-System nach Łukasiewicz in der Fassung von Mendelson):
- Sprache: Aussagenvariablen, Junktoren ¬ und →
- Axiomenschemata:
  - A1: φ → (ψ → φ)
  - A2: (φ → (ψ → χ)) → ((φ → ψ) → (φ → χ))
  - A3: (¬ψ → ¬φ) → (φ → ψ)
- Regel: Modus ponens (aus φ und φ → ψ folgt ψ)
- `Γ ⊢ φ` heißt: Es gibt eine endliche Folge von Formeln, die mit φ endet; jede Zeile ist ein Axiom, ein Element von Γ oder entsteht durch Modus ponens aus früheren Zeilen.

**Semantik:** Klassische Belegungen mit zwei Wahrheitswerten. `Γ ⊨ φ` heißt: Jede Belegung, die alle Formeln aus Γ wahr macht, macht φ wahr.

**Satz (Korrektheit):** Für jede Formelmenge Γ und jede Formel φ gilt: Aus Γ ⊢ φ folgt Γ ⊨ φ.

**Beweis** durch Induktion über die Länge der Herleitung. Sei v eine Belegung, die Γ wahr macht.
1. **Axiome:** A1 bis A3 sind Tautologien, also wahr unter jeder Belegung. Ein Ersetzungsfall einer Tautologie ist wieder eine Tautologie, deshalb genügt die Prüfung auf Schema-Ebene. (Maschinell geprüft: TST-LP02-01.)
2. **Prämissen:** Formeln aus Γ sind unter v wahr, nach Voraussetzung.
3. **Modus ponens:** Sind φ und φ → ψ unter v wahr, dann ist ψ unter v wahr. (Maschinell geprüft: TST-LP02-02.)

Damit ist jede Zeile einer Herleitung unter v wahr, insbesondere die letzte. ∎

**Umfang und Voraussetzungen:**
- Der Satz gilt für **jede** Menge Γ, auch eine unendliche, weil eine Herleitung immer endlich ist.
- Er hängt an **drei Voraussetzungen**: die Wahl der Axiome, die einzige Regel Modus ponens und die zweiwertige Semantik. Eine zusätzliche Regel wie „aus φ → ψ und ψ folgt φ“ würde die Korrektheit zerstören. (Gegenmodell p = falsch, q = wahr: TST-LP02-08.)
- **Vollständigkeit** (aus Γ ⊨ φ folgt Γ ⊢ φ) gilt für H ebenfalls. Für endliche Γ zeigte das Post (1921) für die Aussagenlogik; für beliebige Γ folgt es mit dem Kompaktheitssatz. Diese Richtung wird hier **nicht bewiesen**, nur als bekanntes Resultat angegeben. Maschinell gezeigt ist nur ein Beispiel: eine geprüfte Herleitung von p → p in 5 Zeilen (TST-LP02-03), und der Beweisprüfer lehnt fehlerhafte Herleitungen ab (TST-LP02-04).

### E2 · Vergleich mit einer Logik mit anderen Resultaten

**Gödel-Logik G3:**
- Wahrheitswerte 0, ½, 1; nur 1 gilt als „wahr“.
- Implikation: x → y = 1, wenn x ≤ y, sonst y.
- Negation: ¬x = 1, wenn x = 0, sonst 0.

Ergebnisse (alle maschinell geprüft, TST-LP02-06):

| Formel | klassisch | G3 |
|---|---|---|
| A1 | gültig | gültig |
| A2 | gültig | gültig |
| A3 (Kontraposition rückwärts) | gültig | **nicht gültig** |
| Tertium non datur p ∨ ¬p | gültig | **nicht gültig** |
| Peirce ((p → q) → p) → p | gültig | **nicht gültig** |

**Folge:** Der Kalkül H ist bezüglich der G3-Semantik **nicht korrekt**, denn er leitet A3 her, aber A3 ist in G3 nicht gültig. Korrektheit ist also keine Eigenschaft eines Kalküls allein, sondern immer eine Beziehung **zwischen Kalkül und Semantik**. Für die intuitionistische Logik, zu der G3 eine Erweiterung ist, braucht man einen anderen Kalkül und z. B. Kripke-Semantik; dort gelten wieder eigene Korrektheits- und Vollständigkeitssätze (hier nur angegeben, nicht bewiesen).

### E3 · Ungültiger Schluss als Gegenbeispiel

„Bejahung des Konsequens“ ist ungültig: Aus q und p → q folgt **nicht** p. Gegenmodell: p = falsch, q = wahr. Beide Prämissen sind wahr, die Konklusion ist falsch (TST-LP02-07).

### Bezug zum Logik-Tensor (vorsichtig)

- Der Logik-Tensor 1.0 sagt auf S. 20, die „trinitäre Deduktion“ **ersetze** den Modus ponens. Dieser Probelauf zeigt: Ob eine Regel korrekt ist, lässt sich nur gegenüber einer **angegebenen Semantik** prüfen. Das Original nennt eine solche Semantik („gültig, wenn in allen drei Matrizen konsistent zugeordnet“, S. 20), aber nicht formal genug für einen Test.
- **Folgerung für die Forschung:** Zuerst muss die Tensor-Semantik formal festgelegt werden; dann lassen sich Korrektheit und Vollständigkeit der trinitären Deduktion prüfen. Das ist ein konkreter nächster Forschungsschritt (Kandidat für LOGIK-PROMPT-06, Meta-Logik).

## Selbstbewertung des Prompts (für die Freigabe)

| Kriterium | Befund |
|---|---|
| Verständlich ohne Vorwissen | nein, Fachvorwissen in Logik nötig. Für Mitmachende eine E1-Einleitung ergänzen. |
| Klar abgegrenzt | ja, bei vorgegebenem Kalkül; ohne Vorgabe wählt jeder einen anderen Kalkül. **Vorschlag:** Kalkül H im Prompt vorgeben. |
| Prüfbar | ja: Herleitungen und Gegenmodelle sind maschinell prüfbar |
| Rückgabeformat | fehlt im Prompt; **Vorschlag:** Abschnitte Kalkül, Satz, Beweis, Umfang, Vergleich, Gegenbeispiel, Testnachweise |
| Fachlich heikel | nein (Standardwissen) |
| **Empfehlung** | nach den zwei Ergänzungen (Kalkül vorgeben, Rückgabeformat) Freigabekandidat für Fortgeschrittene |
