---
akt: ergebnis + vorschlag
gespraech: KI-2026-11-03-001
absender: claude
empfaenger: gpt, nils
zustand: input-required
auftrag: Nils 04.11. – „Struktur analysieren, um mit Harvesting und Mustervergleich neue Tensoren zu finden, an einer geeigneten Datenbank testen; zweites Konzept zur Identifikation und Reduktion von Formeln (Ministrukturen, Tensorstrukturen); die bekanntesten 100 Formeln auf trinitäre und tensorale Strukturen analysieren“
reifegrad: E2 (reproduzierbar gerechnet, nicht extern geprüft)
---

# Konzept 2 · Formelreduktion, Ministrukturen, Tensorkeime · mit Test an 100 + 2.676 Formeln

**Kurz:**
- **Konzept 1** (die Algebra) prüft Tensoren, die es schon gibt.
- **Konzept 2** sucht Tensoren **von unten**: Formeln werden auf ihr Gerüst reduziert. Aus Formeln, die sich Größen teilen, entstehen Keime. Aus geschlossenen Dreiecken von Formeln werden neue Beziehungen **abgeleitet** und mit P1–P3 geprüft.
- **Getestet** wurde an den 100 bekanntesten Formeln und an 2.676 Formel-Einträgen aus Wikidata (CC0).
- **Ergebnis:**
  - Das Verfahren findet bekannte Gesetze **von selbst wieder**, z. B. P = F·v, ρ = c·M und molar = M·spezifisch. Damit ist es geeicht.
  - Es erzeugt auch **Scheinbeziehungen**. Die Prüfung P1 sortiert sie aus, wenn ein Mensch die Rollen prüft.
  - Einen neuen Tensor im Sinne der Werke hat es **nicht** gefunden.
  - Es hat aber einen **Tensorkandidaten** gefunden: die Bezugsgrößen-Matrix (Abschnitt 5).

## 1 · Struktur des Harvestings: die Pipeline

```
Quelle → Extraktion → Normalisierung → Reduktion → Muster → Ableitung → Prüfung → Abgleich → Befund
```

| Stufe | Was | Werkzeug | Ausgabe |
|---|---|---|---|
| Quelle | offene Formelbestände | Wikidata (P2534, P7235 + P9758), kuratierte Top-100 | Rohdaten (lokal) |
| Extraktion | Formel + Symbole + Bedeutung | `wbgetentities` (TeX), `parse_latex` | SymPy-Gleichung |
| Normalisierung | Symbol → **Größe** (Wikidata-QID), Naturkonstanten heraus | Symbolzuordnung P9758 | Größenmenge je Formel |
| Reduktion | **Skelett**: Größen → x0, x1, …; Zahlen und Konstanten → k; minimal über Umbenennung und Vorzeichen | `formel_struktur.skelett` | Ministruktur |
| Muster | **Familien** (gleiches Skelett), **Hubs** (Größen in ≥ 3 Dreigrößengesetzen), **Keime** (3 Dreigrößengesetze, paarweise verbunden) | `formel_struktur.bestand` | Kandidaten |
| Ableitung | **Dreieck**: jedes Paar teilt eine *andere* Größe → zwei Verbindungsgrößen eliminieren (Gröbner) | `dreiecke.py`, `wikidata_lauf.py` | abgeleitete Relation |
| Prüfung | P1 gleiche Rolle · P2 neu im Bestand · P3 gleiches Ergebnis über alle Eliminationswege | dieselben | Urteil |
| Abgleich | Rollen der 103 Gerüste als Größen wiedergefunden? | `bestand(…, inventar)` | Wiederfindung |
| Befund | Befundregister, Fragensammlung | – | BEF-T…, Q-… |

**Trinitär** heißt hier: Eine Gleichung verbindet **genau drei** Größen.
**Tensoral** heißt: **drei** solcher Trinitäten sind über gemeinsame Größen verbunden, mit 6–9 Größen insgesamt. Das ist dieselbe Form wie die 103 Gerüste (3 Achsen × 3 Rollen).

## 2 · Die 100 bekanntesten Formeln (`TOP100_ERGEBNIS_V0_1.json`)

Die Liste stammt von Claude (Schule und Grundstudium, Physik, Chemie, Mathematik, Biologie, Ökonomie). Sie ist **keine** amtliche Rangliste.

| Kennzahl | Wert |
|---|---|
| auswertbar | 100/100 |
| Stelligkeit (Anzahl Größen) | 1: 1 · 2: 21 · **3: 37** · 4: 33 · 5: 7 · 6: 1 |
| **trinitär mit 3 verschiedenen benannten Größen** | **34** |
| Typ der Trinität | Potenzgesetz (z = k·xᵃ·yᵇ) **26** · additiv 3 · nichtlinear 3 · implizit 2 · Differentialgleichung 3 |
| Familien gleicher Ministruktur | **x0 = x1·x2**: 10 Formeln (Kraft, Impuls, Arbeit, Kapazität, Wellengleichung, Drehimpuls, Drehmoment …) · **x0 = x1/x2**: 9 (Leistung, Geschwindigkeit, Druck, Dichte, Konzentration, BMI …) · 4-stelliges Produkt: 6 |
| Hubs | Masse 8 · Zeit 6 · Kraft 5 · Geschwindigkeit 5 · Fläche 3 · Arbeit 3 |
| Tensorkeime | 99 (Stern 75 · gemischt 21 · **Dreieck 3**); stark (gleiches Gebiet, ≥ 2 fachliche Verbindungen): 16 |

**Lesart:**
- **Ein Drittel** der bekanntesten Formeln ist trinitär.
- Davon sind **drei Viertel Potenzgesetze**. Das ist die Form, die sich durch Logarithmieren in eine **lineare** Dreierbeziehung verwandelt, also in eine Ebene im log-Raum.
- Die Natur der Schulformeln ist demnach überwiegend **multiplikativ-trinitär**.
- Die meisten Keime sind **Sterne**: Drei Gesetze hängen an derselben Größe, meist Masse.
- **Dreiecke** sind selten (3 von 99). Nur sie erzeugen durch Elimination **neue** Beziehungen.

### Die drei Dreiecke und was aus ihnen folgt (`DREIECKE_V0_1.json`)

| Dreieck | verbunden über | abgeleitet | P1 | P2 | P3 | Urteil |
|---|---|---|---|---|---|---|
| Arbeit · Leistung · Geschwindigkeit | Arbeit, Weg, Zeit | **P = F·v** | ja | ja | ja | **neu im Bestand** (bekannte Physik, nicht unter den 100) |
| Dichte · Stoffmenge · Konzentration | Masse, Stoffmenge, Volumen | **ρ = c·M** | eingeschränkt | ja | ja | **Spezialfall**: gilt nur für reine Stoffe |
| Pendel · Kepler 3 · BMI | Länge, Masse, Periode | g·a³ = BMI·L³·G … | **nein** | ja | **nein** | **unzulässig**: gleiche Wörter, verschiedene Rollen |

Das dritte Dreieck ist das **Lehrstück**: Formal ist es eine saubere Ableitung, fachlich ist es Unsinn. Damit ist P1 nicht Beiwerk, sondern **die** entscheidende Prüfung.

## 3 · Test an einer offenen Datenbank: Wikidata (`WIKIDATA_LAUF_V0_1.json`)

**Quelle:** Wikidata, CC0, abgerufen 2026-11-04T03:49Z. Es wurden 2.676 Einträge mit definierender Formel **und** Symbolzuordnung geladen (25 von 2.701 waren nicht ladbar). Die Rohdaten liegen nicht im Repo; das Repo enthält nur aggregierte Ergebnisse.

| Kennzahl | Wert | Anmerkung |
|---|---|---|
| Einträge | 2.676 | – |
| mit Gleichung (=) | 2.143 | Rest: Ungleichungen, Logik, Definitionen ohne = |
| geparst | 1.803 | **Parse-Fehlerquote 15,9 %** (340); ehrlich ausgewiesen |
| Stelligkeit 3 (**trinitär**) | **884** (33 %) | dasselbe Drittel wie bei den Top-100 |
| Familien ≥ 2 | 108; größte 180 (Typ x0 = x1·x2 bzw. x0 = x1/x2) | gleiche Ministruktur über alle Fächer |
| Hubs | Dauer 50 · Masse 41 · Fläche 26 · Volumen 21 · Temperatur 14 · Wellenlänge 14 · Dichte 12 · Stoffmenge 12 · Kraft 11 | – |
| Keime | Stern 37.759 · gemischt 2.084 · **Dreieck 239** | – |
| Dreiecke abgeleitet | **sauber 49** · mit nicht zugeordneten Symbolen 35 · Abbruch (Wurzeln, Zeitlimit, unvollständige Zuordnung) 100 · nicht geparst 54 · ohne Relation 1 | Abbrüche sind Werkzeuggrenzen, keine Befunde |
| Wiederfindung 103er-Inventar | **36 von 309 Achsen** haben ≥ 2 Rollen, die als Wikidata-Größe vorkommen | vor allem Mathematik (Analysis: Ableitung, Grenzwert, Integral – alle drei) |

**Beispiele sauberer Ableitungen** (alle bekannte Physik und Chemie, also Eichung):
- Lichtstärke = Beleuchtungsstärke · r² (über den Raumwinkel)
- Belichtung = Beleuchtungsstärke · Dauer
- molare X = molare Masse · spezifische X, für X = Entropie, innere Energie, freie Energie, Gibbs-Energie, Enthalpie, Wärmekapazität (**6 Dreiecke, eine Struktur**)
- molare Masse = Dichte · molares Volumen
- Oberflächenspannung = Beschleunigung · längenbezogene Masse (formal sauber, **P1 fraglich**: Rollenprüfung nötig)

## 4 · Muster, die auffallen

| # | Muster | Beleg | Reife |
|---|---|---|---|
| FM1 | **Ein Drittel aller Formeln ist trinitär**, in beiden Beständen | Top-100: 34–37 %; Wikidata: 33 % | E2 (zwei unabhängige Bestände, kein Nullmodell) |
| FM2 | Trinitäten sind überwiegend **Potenzgesetze** (log-linear) | 26/34 | E2 (nur Top-100) |
| FM3 | Wenige **Ministrukturen** tragen fast alles: x0 = x1·x2 und x0 = x1/x2 | größte Familien in beiden Beständen | E2 |
| FM4 | **Sterne** um Hub-Größen (Masse, Dauer) sind häufig, **Dreiecke** selten (≈ 0,6 %) | 239 von 42.082 Keimen | E2 |
| FM5 | Dreiecke erzeugen nur dann gültige Beziehungen, wenn die Verbindungsgrößen **dieselbe Rolle** haben | Pendel/Kepler/BMI vs. P = F·v | E2, P1 menschlich |
| FM6 | **Umrechnungsgrößen** (molare Masse, Dichte, r² des Raumwinkels, Dauer) erzeugen ganze **Familien** paralleler Dreiecke | 7 Dreiecke über die molare Masse, 6 über die Dichte, 6 über den Raumwinkel | E2 → **Tensorkandidat** |

## 5 · Tensorkandidat aus dem Harvesting: die Bezugsgrößen-Matrix

Aus FM6 ergibt sich eine Struktur aus **3 Bezügen** × **n Größen**, verbunden durch **3 Umrechnungsgrößen**:

| Größe ↓ \ Bezug → | je Masse (spezifisch) | je Stoffmenge (molar) | je Volumen (Dichte) |
|---|---|---|---|
| Energie / Enthalpie | spezifische Enthalpie | molare Enthalpie | Energiedichte |
| Entropie | spezifische Entropie | molare Entropie | Entropiedichte |
| Wärmekapazität | spezifische Wärmekapazität | molare Wärmekapazität | Wärmespeicherzahl |

Die Umrechnungen lauten: molar = **M** · spezifisch, volumenbezogen = **ρ** · spezifisch, molar = **Vm** · volumenbezogen. Dazu gehört die Schließungsbedingung **M = ρ · Vm**, die als Dreieck **unabhängig gefunden** wurde (molare Masse · molares Volumen · Dichte). Die Spalte „je Volumen“ ist ebenfalls belegt: Wärmespeicherzahl = ρ · spezifische Wärmekapazität, Aktivitätskonzentration = ρ · spezifische Aktivität, Massenkonzentration = ρ · Massenanteil (6 Dreiecke über die Dichte).

**Warum das tensoral ist:**
- drei Bezüge × drei Größen = ein 3×3-Gerüst;
- die Umrechnungen bilden einen **geschlossenen Zyklus** (spezifisch → molar → volumenbezogen → spezifisch), dessen Produkt 1 ergibt;
- das entspricht **Regel U Klasse I** (exakte Rückkehr).

**Was es NICHT ist:** neue Physik. Die Struktur ist in der Thermodynamik als „intensive Bezugsgrößen“ bekannt.
**Was es zeigt:** Das Harvesting kann ein Gerüst der Form 3 × 3 aus einer Datenbank **ohne Vorwissen rekonstruieren**. Das ist die Probe, die Nils mit „neue Tensoren finden“ gemeint hat. An diesem Kandidaten kann man das Verfahren vorführen.

**Prüfschritt (offen):** Abbildung auf M/K/S und Abgleich mit den 103 Gerüsten (gibt es eines mit „spezifisch / molar / volumenbezogen“?). Dafür ist die Frage **Q-F08** eingetragen.

## 6 · Grenzen

- **P1 ist nicht automatisiert.** Gleiche QID heißt nicht gleiche Rolle (Masse des Körpers ≠ Zentralmasse). Rollenprüfung siehe Öffnungskonzept, Beitragsart B1.
- **Parse und Zuordnung:** 15,9 % der Formeln scheitern am Parser. Ableitungen brechen bei Wurzeln und bei Zeitlimits ab (100 von 239). Punkt-Ableitungen (ẋ) werden als Symbol gelesen.
- **Kein Nullmodell:** FM1–FM6 sind Häufigkeiten, keine Tests. Der nächste Schritt ist ein Vergleich mit zufällig gemischten Größenmengen.
- **„Neu im Bestand“ ≠ neu für die Wissenschaft.** Alle bisherigen Ableitungen sind bekannt.
- **Auswahlverzerrung:** Wikidata bildet vor allem Größen nach ISO 80000 ab. Viele Formeln der Werke (Soziation, Holographie) haben dort kein Gegenstück.

## 7 · Dateien

| Datei | Inhalt |
|---|---|
| `formel_struktur.py` | Konzept 2: parse, Variablen, Triadentyp, Skelett, Bestand (Familien, Hubs, Keime, Dreiecke, Wiederfindung) |
| `FORMELN_TOP100_V0_1.json` / `top100_lauf.py` / `TOP100_ERGEBNIS_V0_1.json` | Top-100 |
| `dreiecke.py` / `DREIECKE_V0_1.json` | Ableitung + P1–P3 |
| `wikidata_lauf.py` / `WIKIDATA_LAUF_V0_1.json` | Harvesting-Test (Rohdaten lokal; ohne sie SKIP, Exit 77) |
| `tests/test_formel_struktur.py` | 12 Tests, im Ein-Befehl-Lauf `forschung/register/reproduzieren.py` |
