---
akt: vorschlag
gespraech: KI-2026-11-03-001
absender: claude
empfaenger: gpt, nils
zustand: input-required
auftrag: Nils 04.11. – „Konzept analysieren, die Tensoralgebra zur Mitarbeit zu öffnen und dafür einen alten Datenbestand auf ein neues Level zu heben – wie definieren wir, wie weit die Algebra bis zur Publikation ausgearbeitet sein muss, und wie präsentieren wir das nicht nur im Rahmen von Mitmachen“
reifegrad: E1 (Konzept, nicht beschlossen)
---

# Öffnung der Tensoralgebra, Hebung des Altbestands, Publikationsreife · v0.1

**Kurz:**
- Die Algebra lässt sich öffnen. Am besten geht das über **Prüfaufgaben**, nicht über freie Beiträge.
- Die einzige Prüfung, die eine Maschine nicht leisten kann, ist **P1 (Bedeuten gleichnamige Größen dasselbe?)**. Genau dort brauchen wir Menschen.
- Bisher fehlt der Algebra vor allem ein **Nullmodell**: Ohne Zufallsvergleich sind die Muster M1–M9 noch keine Befunde.
- Für eine Publikation reicht kein Website-Bereich „Mitmachen“. Dafür eignen sich vier Formate: Datenpaper mit DOI, Methodenpreprint, Software mit Tests und ein offener Benchmark.

## 1 · Ist-Analyse: Wie offen ist die Algebra heute?

| Ebene | Stand 04.11. | Offen für Dritte? |
|---|---|---|
| Code | `typalgebra.py`, `formel_struktur.py`, `dreiecke.py`, 35 Tests, Ein-Befehl-Lauf `reproduzieren.py` | **ja**, lesbar und lauffähig, sobald sympy installiert ist |
| Daten veröffentlicht | 9 Tensoren aus Werken, 103 Gerüste (`docs/data/tensor-inventar-v10_7.json`), Top-100-Formeln, Wikidata-Aggregate | **teilweise**: Die 103 Gerüste haben **keine Pfade**, die 9 Tensoren nur wenige |
| Format | `tensor/1.0` (Schema vorhanden) | **kaum**: Bisher füllt niemand außer Claude dieses Format |
| Beitragsweg | Website-Seite Mitmachen / Inkubator (GPT) | **nein**: Es gibt keine Einreichungsform, keine automatische Prüfung und keinen Prüfpfad |
| Prüfregeln | P1–P3, Regel U, A1, Typregeln v0.2 | dokumentiert, aber über das Repo verteilt |
| Anerkennung | – | **ungeklärt**: Lizenz und Nennung von Beitragenden sind offen |

**Befund:** Für die Mitarbeit fehlen nicht die Werkzeuge. Es fehlen drei Dinge:
1. eine **kleine, klar umrissene Aufgabe**,
2. ein **Format**, das ohne Kenntnis der Autornotation ausgefüllt werden kann,
3. ein **Prüfpfad**, an dessen Ende eine Nennung steht.

## 2 · Öffnung: vier Beitragsarten, nach Einstiegshöhe gestaffelt

| Stufe | Beitragsart | Was Mitwirkende tun | Was automatisch geprüft wird | Was ein Mensch prüft |
|---|---|---|---|---|
| B1 | **Rollenprüfung (P1)** | Bei einer abgeleiteten Beziehung sagen sie, ob gleichnamige Größen dasselbe bedeuten: ja / nur Spezialfall / nein, mit Begründung | – | **zwei** unabhängige Urteile; bei Uneinigkeit entscheidet ein drittes |
| B2 | **Formel einreichen** | Formel, Größen und Gebiet als JSON nach dem Muster `FORMELN_TOP100_V0_1.json` (oder eine Wikidata-QID) | Parse, Skelett, Familie, Keime, P2 gegen den Bestand | Gebiet und Quelle |
| B3 | **Gerüst heben** | ein historisches Gerüst (3 Achsen × 3 Rollen) auf `tensor/1.0` bringen: Achsen → M/K/S, Formelanker als SymPy-Formel, Größen mit Wikidata-QID | Schema, A1, Formeltyp, Typregeln | Abbildung auf M/K/S (Fachurteil) |
| B4 | **Gegenprobe / Replikation** | einen Lauf auf eigener Maschine wiederholen oder eine eigene Implementierung schreiben | Vergleich der Ergebnis-Hashes | – |

**Warum diese Reihenfolge:** B1 braucht **kein** Wissen über die Tensor-Notation, nur Fachverstand. Das ist der niedrigste Einstieg, und die Ergebnisse sind wissenschaftlich am wertvollsten. Ein Beispiel ist das Scheindreieck Pendel–Kepler–BMI (`formeln/DREIECKE_V0_1.json`): Die Maschine hat es formal abgeleitet. Erst die Frage „Ist *Länge* hier dieselbe Länge?“ entlarvt es.

**Ablauf** (aus Sicht der Website: GPT; aus Sicht der Daten: Claude):

```
Einreichung (Formular/Issue-Vorlage → JSON)
  → automatische Prüfung (Schema, Parse, P2, P3; Ergebnis als Kommentar)
  → Rollenprüfung P1 durch 2 Menschen (B1-Aufgaben werden genau hieraus erzeugt)
  → Befundregister (BEF-…) mit Nennung der Beitragenden
  → Nils: Freigabe für alles, was seine Werke berührt
```

Was **nicht** geöffnet wird:
- Bewertungen von Nils' Werken (Regel: erst nach seiner Freigabe),
- private Altpakete,
- Rohprompts.

## 3 · Einen alten Datenbestand auf ein neues Level heben: das 103er-Inventar

**Warum gerade dieser Bestand:**
- Er ist **bereits öffentlich** (GPT, `docs/data/tensor-inventar-v10_7.json`). Damit ist er sofort nutzbar und hängt nicht am privaten Speicher.
- Er ist **groß genug** für Muster: 103 Gerüste mit 309 Achsen.
- Er ist **heute schwach**: keine Pfade, freier Text in den Formelankern, keine Verbindung zu externen Größen.

**Stufen (L0 → L4):**

| Stufe | Inhalt | Messbar an | Stand |
|---|---|---|---|
| L0 | Gerüst als Text (Achsen, Rollen, Modell, Formelanker) | – | **ist** (103/103) |
| L1 | Formelanker maschinenlesbar (SymPy), Formeltyp, Skelett und Familie | Anteil geparster Anker | 0/103; Formeltypen per Muster in `ANALYSE_103_V0_1.json` |
| L2 | Rollen mit **Wikidata-QIDs** verknüpft (Linked Open Data) | Anteil verknüpfter Rollen | Kandidaten: 36/309 Achsen haben mindestens 2 Rollen, die als Wikidata-Größe vorkommen (`formeln/WIKIDATA_LAUF_V0_1.json`) |
| L3 | Achsen → **M/K/S** abgebildet, A1 geprüft, `tensor/1.0`-Akte | Anteil Gerüste mit gültiger Akte | Frage Q-F06 (Abbildung Fachachse → M/K/S) offen bei GPT und Nils |
| L4 | **Pfade** erarbeitet; Typregeln, Regel U und M1–M9 laufen | Anteil Gerüste mit mindestens 3 typisierten Pfaden | 0/103 |

**Pilot:** 10 Gerüste aus Physik und Chemie, bei denen Formelanker und Wikidata-Treffer zusammenfallen. L1 und L2 macht Claude, L3 erfordert ein Fachurteil (Nils oder eine B3-Beitragende Person), L4 machen Autor und KI gemeinsam.
**Erfolgskriterium des Piloten:** 10/10 Gerüste auf L2, mindestens 5 auf L3 und mindestens 3 auf L4, sodass M1–M9 erstmals an fremden Gerüsten prüfbar werden.

**Was das neue Level bringt:**
- Die Gerüste werden mit dem Formelbestand der Welt **verbunden** (Wikidata), statt nur nebeneinander zu stehen.
- Dieselbe Größe in Gerüst A und Gerüst B ist dann **maschinell** dieselbe. Damit läuft die Dreieckssuche über alle Gerüste hinweg.

## 4 · Publikationsreife: Gates statt Gefühl

Eine Publikation braucht eine **abgegrenzte Behauptung**. Für die Algebra schlage ich diese vor:

> **Behauptung A:** Ein typisiertes Pfadsystem auf dem Adressraum (M, K, S) mit 8 Pfadtypen und Typregeln ist (i) widerspruchsfrei, (ii) entscheidbar und (iii) auf unabhängigen Tensoren nicht trivial: Die beobachteten Bindungen von Pfadtypen an Klassen treten häufiger auf als im Zufallsmodell.

| Gate | Was erfüllt sein muss | Messgröße / Schwelle | Stand |
|---|---|---|---|
| **G1 Formal** | Typsystem, Operationen, Regeln vollständig definiert; Gegenbeispiele getestet | jede Regel mit positivem **und** negativem Test; keine Regel ohne Test | weitgehend (23 + 12 Tests); Regel CYC wurde einmal korrigiert |
| **G2 Reproduzierbar** | Ein Befehl erzeugt alle Zahlen; Versionen gepinnt; DOI | `reproduzieren.py` grün auf frischer Maschine; Zenodo-Snapshot | Ein-Befehl-Lauf **ja**; Pinning und DOI **nein** |
| **G3 Extern belegt** | Muster an einem **Bestand, der nicht zur Regelbildung diente**, mit **Nullmodell** | M1–M9 an mindestens 30 Tensoren mit Pfaden; Permutationstest (Klassen zufällig vertauscht), p < 0,01, Hypothesen **vorab** festgelegt | **nein**: n ≤ 4 je Muster, kein Nullmodell |
| **G4 Repliziert** | unabhängige Implementierung oder unabhängiger Lauf | GPT-Gegenlauf **und** mindestens eine externe Person (B4) | GPT-Gegenlauf nur für LOGIK-02 |
| **G5 Fachlich geprüft** | P1-Urteile mit Übereinstimmung | mindestens 2 Prüfende je Urteil, Cohen's κ ≥ 0,6 | nicht begonnen |
| **G6 Eingeordnet** | Abgrenzung zu bekannter Mathematik | Bezüge: Dimensionsanalyse (Buckingham-Π), Gröbner-Elimination, Formelsuche (zbMATH, MathWebSearch), symbolische Regression (AI Feynman), Kategorientheorie und Typsysteme | Stichworte gesammelt, Text fehlt |

**Mindestumfang für eine erste Publikation:** G1 + G2 + G3 + G6, mit G4 durch GPT.
G5 kann als **offene Frage** im Text stehen, mit B1 als Einladung.

**Was ausdrücklich NICHT behauptet werden darf:**
- „neue Physik“. Alles, was die Dreieckssuche bisher fand, ist bekannte Physik: P = F·v, ρ = c·M, molar = M·spezifisch.
- Das ist trotzdem ein **Befund**: **Wiederentdeckung als Validierung**. Ein Werkzeug, das bekannte Gesetze aus einer Datenbank wieder ableitet, ohne sie zu kennen, ist geeicht.

## 5 · Präsentation über „Mitmachen“ hinaus

| Form | Inhalt | Wo | Wer | Reife nötig |
|---|---|---|---|---|
| **Datenpaper + Datensatz mit DOI** | 103 Gerüste auf L2/L3, Top-100, Wikidata-Aggregate, Schema `tensor/1.0` | Zenodo (vorhandene Community), Zeitschrift für Datenpaper | Claude Daten, GPT Darstellung, Nils Autor | G2 |
| **Methodenpreprint** | Behauptung A, Gates G1–G3, G6; Formelreduktion und Dreiecke als zweiter Teil | Zenodo / arXiv-Kategorie nach Nils' Wahl | Nils Autor; KIs als Werkzeug ausgewiesen | G1–G3, G6 |
| **Software** | `typalgebra`, `formel_struktur`, Tests, Ein-Befehl-Lauf | Repo + Software-DOI; ggf. Software-Journal | Claude | G1, G2 |
| **Offener Benchmark** „Dreiecke“ | Aufgabe: aus N Formeln die gültigen Dreiecke finden und die Scheindreiecke verwerfen; Goldstandard aus P1-Urteilen | Repo + Website | Claude Daten, GPT Seite | G5 teilweise |
| **Interaktiver Explorer** | Skelett-Familien, Hubs, Dreiecke anklickbar; 27er-Würfel mit Pfaden | Website (GPT) | GPT | G2 |
| **Notebook** | ein Lauf zum Nachvollziehen im Browser | Repo | Claude | G2 |
| **Rückgabe an Wikidata** | abgeleitete Beziehungen, die dort fehlen, als **Vorschlag** an die Community (CC0) | Wikidata-Diskussionsseiten | nach Nils' Freigabe | G5 für die Einzelfälle |
| **Vortrag/Poster, Lehrmodul** | „Trinitäten in 2.676 Formeln“ | Tagung, Schule/Hochschule | Nils | G3 |

**Empfehlung:**
1. **Zuerst** das Datenpaper mit DOI. Es braucht nur G2 und macht den Altbestand zitierbar.
2. **Dann** den Methodenpreprint, sobald G3 steht. G3 hängt am Piloten L4 und am Nullmodell.
3. „Mitmachen“ läuft **parallel** und speist G5. Es ist ein Zulieferer der Publikation, nicht ihr Ersatz.

## 6 · Nächste Schritte

| # | Schritt | Wer | hängt an |
|---|---|---|---|
| 1 | Nullmodell (Permutationstest) für M1–M9 in `muster.py` | Claude | – |
| 2 | Pilot L1/L2 an 10 Gerüsten | Claude | – |
| 3 | Issue-Vorlage + JSON-Muster für B1/B2 | Claude (Daten), GPT (Seite) | Nils' Freigabe der Öffnung |
| 4 | Abbildung Fachachse → M/K/S (L3) | Nils / GPT (F6) | Q-F06 |
| 5 | Versionen pinnen, Zenodo-Snapshot vorbereiten | Claude | Nils (DOI, Lizenz) |

Fragen an Nils (in der Fragensammlung): **Q-P01** Öffnung B1–B4 ja/nein, **Q-P02** Lizenz für Beiträge Dritter, **Q-P03** Reihenfolge Datenpaper → Preprint.
