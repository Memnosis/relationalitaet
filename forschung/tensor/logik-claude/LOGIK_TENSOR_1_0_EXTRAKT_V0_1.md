# Logik-Tensor 1.0 · Originalauszug und Abgleich mit der Arbeitsfassung 2.1

**Owner:** Claude (Daten-KI) · **Schritt:** S2 / K5 · **Bezug:** P0-X3, DATA-001 · **Stand:** 2026-11-03
**Quelle:** Nils Sautter, *Relationale Logik – der Logik Tensor*, Version 1.0, 28.03.2026, DOI [10.5281/zenodo.19282895](https://doi.org/10.5281/zenodo.19282895), CC-BY-4.0. Datei `Logik-Tensor_1_0.pdf`, SHA-256 geprüft gegen `forschung/register/QUELLEN_REFERENZSET_V0_1.json`.
**Daten:** [`LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json`](LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json) · **Werkzeug:** [`werkzeuge/logik10_extrakt.py`](werkzeuge/logik10_extrakt.py)

Dieser Auszug dokumentiert, **was im Original steht**. Er deutet nichts um und bewertet keine Aussage als richtig oder falsch.

## E1 · Kurz erklärt

Der Logik-Tensor 1.0 ordnet 27 Begriffe der Logik in drei Tafeln mit je 3 × 3 Feldern an:
- **Null-Matrix:** was vor dem Schließen da sein muss
- **Zyklus-Matrix:** wie geschlossen wird
- **Einheits-Matrix:** was als gültig stehen bleibt

Die Arbeitsfassung 2.1 übernimmt alle 27 Begriffe **unverändert**. Auffällig ist ein anderer Punkt: Kapitel 8 heißt „100 Logik-Begriffe“, die Tabelle darin hat aber 34 Zeilen.

## E2 · Ergebnisse im Einzelnen

### 27 Felder

Adresse = Matrix (NM/ZM/UM) – Spalte (I Kern, II Kreislauf, III Öffnung) – Modus (α Struktur, β Funktion, γ Relation).

| Modus | NM-I | NM-II | NM-III | ZM-I | ZM-II | ZM-III | UM-I | UM-II | UM-III |
|---|---|---|---|---|---|---|---|---|---|
| α | Symbolischer Trägerraum | Syntaxgerüst | Grenz- und Paradoxraum | Inferenzschritt | Beweisgang | Modallogische Öffnung | Theorem | Kalkül oder System | Logische Theorieform |
| β | Axiomatische Setzung | Ableitungsbereitschaft | Entscheidungsbereitschaft | Regelanwendung | Transformation und Umformung | Rekursive Entscheidungsprozesse | Geltungsfunktion | Konsistenz / Vollständigkeit | Entscheidbarkeitsraum |
| γ | Relationale Vorordnung | Semantischer Möglichkeitsraum | Offene Geltungsspannung | Operator der Ableitung | Syntax-Semantik-Übergang | Netz logischer Korrespondenzen | Äquivalenz und Identität | Modellklasse | Offene Korrespondenz logischer Systeme |

Fundstellen: Null-Matrix S. 3–4, Zyklus-Matrix S. 4, Einheits-Matrix S. 5.

### Abgleich mit `LOGIK_TENSOR_2_1_…` §4

**27 von 27 Begriffen sind identisch.** Die Tabelle in 2.1 hat keine Adressen. Ihre Zeilen folgen der Reihenfolge I(α,β,γ), II(α,β,γ), III(α,β,γ) über die drei Matrizen. **Empfehlung an die Owner-KI von 2.1 (GPT):** die Adressen (z. B. `NM-II-α`) als eigene Spalte ergänzen, damit die Zuordnung eindeutig ist.

### Feldpfade (LM)

| Code | Fundstelle |
|---|---|
| `LM : PRJ : NM-I-γ → ZM-II-γ → UM-II-γ` (Projektion) | S. 6, 13 |
| `LM : RST : UM-II-β → ZM-I-β → NM-I-β` (Reset) | S. 6 |
| `LM : CYC : ZM-II-α → ZM-II-β → ZM-II-γ` (Kreislauf) | S. 6 |

Alle drei entsprechen 2.1 §5.

### Fünf Axiome (S. 19)

Trinitäre Differenzierung · Dreifache Gliederung · Dreifache Modalität · Relationale Kontinuität und Diskontinuität · Offene Ganzheit

### Sieben Logiksysteme mit dominanten Feldern (S. 14–15)

| System | Dominante Felder laut Original |
|---|---|
| Klassische Logik | NM-II-α, ZM-II-β, UM-II-β |
| Intuitionistische Logik | NM-I-β, ZM-I-β, UM-I-α |
| Modale Logik | NM-III-γ, ZM-III-α, UM-III-γ |
| Mehrwertige Logik | NM-II-γ, ZM-II-β, UM-II-β |
| Parakonsistente Logik | NM-III-α, ZM-I-γ, UM-II-β |
| Relevanzlogik | NM-I-γ, ZM-II-γ, UM-I-γ |
| Algebraische Logik | NM-II-α, ZM-II-γ, UM-II-γ |

### Kapitel 8 „100 Logik-Begriffe“ (S. 16–18)

| Block | Zeilen | Tensorstatus laut Original |
|---|---:|---|
| 8.1 Außenraum-Begriffe | 7 | 5 × „außerhalb“, 2 × „offen“ |
| 8.2 Baseline (Rel0) | 9 | „klar“ |
| 8.3 Emergenz (Rel-Rel) | 9 | „klar“ |
| 8.4 Identität (Rel1) | 9 | „klar“ |
| **Summe** | **34** | |

Die Blöcke 8.2 bis 8.4 sind genau die 27 Feldbegriffe. Neue Begriffe gibt es nur im Außenraum: Induktion, Abduktion, Ontologie, Epistemologie, Heuristik, Diagrammatische Logik, Institution Theory. Das Quellenverzeichnis (S. 21) spricht ebenfalls von „Quellen, u.a. der 100 Begriffe“.

**Offene Frage an Nils (keine Bewertung):** Gibt es eine Fassung mit 100 Begriffen, z. B. einen Anhang oder eine Vorarbeit? Bis zur Klärung sollte die Zahl „100“ nicht ungeprüft weitergegeben werden. Vorschlag: „34 dokumentierte Begriffe (davon 27 Feldbegriffe)“. Betroffen sind die Formulierungen „100 Logikbegriffe“ bzw. „100 Begriffe“ in `LOGIK_TENSOR_2_0_…` (Abschnitt „Vier direkte Ausgangswerke“), `LOGIK_TENSOR_2_1_…` §2 und im Briefing §4. Auf den Website-Seiten unter `docs/` kommt die Zahl derzeit nicht vor (geprüft am Stand `7586e6a`).

## E3 · Methode und Nachweis

1. **Quelle sichern:** Download von Zenodo, MD5 gegen Zenodo, SHA-256 gegen das Referenzset. Bricht bei Abweichung ab.
2. **27 Felder:**
   - aus dem Layout-Text (`pdftotext -layout`) der Seiten 3–5 abgelesen
   - jeder Begriff **maschinell** gegen den Text der angegebenen Seite geprüft: 27/27 gefunden
   - Silbentrennungen über Tabellenspalten hinweg werden erkannt (z. B. „Entscheidungs-“ … „bereitschaft“)
   - **Gegenproben**, die alle korrekt *nicht* gefunden werden: erfundene Begriffe („Beweisbereitschaft“, „Quantenlogikraum“, „Bereitschaftsentscheidung“) sowie echte Begriffe auf falscher Seite („Theorem“ auf S. 3, „Modellklasse“ auf S. 3, „Entscheidungsbereitschaft“ auf S. 5)
3. **Pfade, Axiome, Systeme, Kapitel 8:** per regulärem Ausdruck aus dem PDF-Text. Die Systemzuordnung setzt genau 21 Adressen auf S. 14–15 in Tabellenreihenfolge voraus (geprüft).
4. **Abgleich 2.1:** Die Markdown-Tabelle §4 wurde maschinell gelesen und nach Normalisierung von Groß-/Kleinschreibung und Leerraum verglichen.

**Grenzen:**
- Bei mehrzeiligen Begriffsnamen in Kapitel 8 wird nur die erste Zeile gespeichert (Feld `begriff_erste_zeile`). Alle 27 Kernbegriffe lassen sich trotzdem eindeutig zuordnen.
- Kurzdefinitionen sind ebenfalls nur mit der ersten Zeile erfasst.
- Es wurde keine Aussage des Werks fachlich geprüft. Die Begriffe sind Kodierungen des Autors (Evidenzstufe `B`).

**Reproduktion:**
```
python3 forschung/tensor/logik-claude/werkzeuge/logik10_extrakt.py <pfad>/Logik-Tensor_1_0.pdf
```
Erwartete Ausgabe: `felder 27, felder_gefunden 27, axiome 5, systeme 7, begriffe_kap8 34, abgleich_2_1 27/27`.
