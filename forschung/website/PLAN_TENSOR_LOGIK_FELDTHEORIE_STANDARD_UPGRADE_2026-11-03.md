# Website-Upgradeplan: Tensor-Einführung · Logik-Tensor · Feldtheorie · Algebra
**Stand:** 2026-11-03 · **Zuständigkeit:** ChatGPT/Website · **Datenschnittstelle:** Claude/Datenbestände · **Status:** Plan und Seitenaudit; keine öffentliche redaktionelle Freigabe von neuem wissenschaftlichem Inhalt.

## Leitentscheidung
Website-Umsetzung erfolgt wieder **hier in ChatGPT**, Datenfusion in Claude. Seiten bleiben in ihrem derzeitigen Wortlaut, ihren Medien, Adressen, Covers, Fachfarben und bestehenden Forschungszugängen erhalten, solange kein **expliziter belegter Änderungsgrund** vorliegt. Das Upgrade ist additiv, mit nachvollziehbaren Korrekturen und Vorher-/Nachher-Regression.

## 1. Tatsächlich bestehende Seiten (Repository-Audit)
| Seite | Funktion heute | Upgrade |
|---|---|---|
| `docs/tensor-einfuehrung.html` | Einfache 3×3×3-Erklärung, Ringmatrix, 27 Positionen, Einstieg, Logik-/Feldtheorie-Anschluss | Formalen Koordinatenraum vs. drei semantische Modelle unterscheiden, Lernpfade und Quellenstatus ergänzen, bestehende Grafiken erhalten |
| `docs/tensor-paper.html` | Logik-Tensor, Null-/Zyklus-/Einheitsmatrix, Feldtheorie-Auszug, Quellen-/Mitmachpfad | Drei Matrizen bewahren, Claim- und Evidenzverweise, Randgebiete, Feldtheorie-Fortschritt und getrennte Autorenversionen erklären |
| `docs/tensoralgebra.html` | Formeln, Relationen, sechs Referenzwissenschaften, Homomorphieprüfung, Mitmachauftrag, Prompt-/Agent-/Meta-Karten | Zwei konkrete algebraische Testfälle mit Gegenbeispiel, Quellen- und Test-ID, anschlussfähige Kontext-Prompts; nur nach dokumentiertem Lauf als getestet markieren |
| `docs/bibliothek.html` | Forschungsquellen, Glossar, Harvesting, Originalpublikationen und Register | Veröffentlichte vs. interne Materialien, Quellzugang und unabhängige Belegqualität als separate Facetten; keine nicht freigegebenen Dateien direkt verlinken |
| `docs/projektstand.html` | Themen- und Projektübersicht, Meilensteine/alte Kennzahlen | Reife getrennt nach Inventar, fachlichem Nachweis, Implementierung, Promptprobe, Freigabe; bereinigte Werte aus Claudes Register |
| `docs/mitmachen.html` | Didaktische Mitmachaufgaben, Geo-/Harvesting-Einstiege, Promptregel | Nur getestete/redaktionell genehmigte Aufgaben aus dem Quell-/Claimregister anzeigen; offene unabhängige Quellenprüfungen als neue Tasks |
| `docs/index.html` | Start und sechs Kernbereiche mit SOULution-Anschluss | Übersichtlichere hierarchische Einstiegspfade; keine zusätzliche unübersichtliche Kopfzeile |
| `docs/soulution.html` | Neun Forschungsbereiche und vernetzte Werkzeuge | Anschlüsse an Feldtheorie und Lösungsatlas, keine Vermischung von SOULution und KI-Tensor |
| `docs/inkubator.html` | Neuer Werkzeug-/Medieneinstieg | Komponenten und öffentliche Prüfaufträge aus freigegebenen Daten; getrennte Projekte |

**Offener Befund:** Auf `docs/tensor-paper.html` ist die hierarchische Navigations-Erweiterung noch nicht nachgewiesen eingebunden; sie verwendet älteren Header. `docs/tensor-einfuehrung.html` enthält redaktionelle Metakommentare zur Originalerhaltung im sichtbaren Text; diese sollten in ein internes Editorial-Register ausgelagert werden, ohne den historischen Inhalt zu verkürzen. **Nicht ohne Vorher-/Nachher-Diff ändern.**

## 2. Publikations- und Seitentopologie
**Drei Publikationsformen nicht verwechseln:**
- Originalpublikationen (ggf. Zenodo/Original-PDF) bleiben unangetastet und behalten die Originalreferenz.
- **Neues wissenschaftliches Upgradepaper** mit eigener Versionsnummer und eindeutig dokumentierten Unterschieden.
- Leserorientierte **Website-Fachseite**, welche die Erkenntnis erklärt, Originale zitiert und zu Tests/Forschung führt.

Vorschlag für einen zusammenhängenden Leserpfad:
Start → Tensor verstehen (Grundschema) → Logik-Tensor & Feldtheorie (exemplarisches Original) → Tensoralgebra (reproduzierbare Mathematik) → Wissenschaftsvergleich / die drei Kandidatensysteme (A/B/C) → Forschungsstatus → getestete Mitmachaufgabe.

Das ist zunächst ein Navigationskonzept. Existierende Direktlinks und Hierarchie müssen weiter funktionieren. Ein neues eigenständiges Standardkapitel kann später als Forschungsseite sinnvoll sein; bestehende Fachseiten bleiben bestehen.

## 3. Vier Phasen des Website-Upgrades
### W0 · Bestandssicherung und Navigation (P0)
- HTML/Links/Anker/Assets erfassen, Seiten-Versionen und Design abgleichen.
- Mehrstufige Navigation (Forschung, Projekte, Publikationen, Mitmachen) auf allen relevanten Seiten einheitlich einbinden, inklusive `tensor-paper.html`.
- Desktop/Mobil/Touch/Tastatur/Screenreader-Fall testen; Fallback ohne JS, keine doppelten aktiven Menüs.
- Redaktionsinterne Metasätze auf öffentlichen Seiten identifizieren und gezielt entfernen/auslagern.
**Abnahme:** keine Regression von URLs, Bilder/Cover, Abschnitten oder Nutzungsfunktionen.

### W1 · Tensor verstehen: Modellklarheit (P0)
- Bereits vorhandene Erklärung behalten und ergänzen: Geometrie G, neutrale Sprache A, operative Triaden B, fachimmanente Trinitäten C, Beschreibungspflicht Ont/Op/Th.
- Je ein anschauliches Beispiel und klare Evidenzgrenze; Unterschied von 27 Koordinaten und 27 wissenschaftlich belegten Feldern.
- Drei 3×3-Matrizen auf `tensor-paper.html` erhalten, zusätzlich Quellen- und Vergleichsmodi anbieten.
**Abnahme:** ein Leser kann nach der Einführung die vier Objekttypen trennen.

### W2 · Logik-Tensor und Feldtheorie als ausgearbeitete Fachseiten (P0/P1)
- Logik-Tensor als erstes exemplarisches vollständiges Kapitel: Syntax, Schlussbeziehung und Semantik mit Originalbelegen; Randgebiete Typen-/Beweis-/Modelltheorie, Automaten/Programmsemantik als Anschlüsse.
- Feldtheorie-Begriff: **Ordnung von Feldern** vs. **mathematisch definierte Feldgrößen** vs. **dynamisches Feld** vs. **physikalische Feldtheorie** transparent trennen.
- Feldaussagen mit Belegarten versehen: Originalpaper / Fachquelle / formal abgeleitet / eigene Zuordnung / offene Hypothese.
- Fachliche Freigabe aus Claudes Dossiers als Bedingung, keine generierten Beweise oder Zitate erfinden.
**Abnahme:** jede zentrale Aussage verweist auf Quelle/Claim; Gegenmodell oder Grenzfall sichtbar.

### W3 · Algebra, Quellen, didaktische Prompts, Mitmachen (P1)
- Mathematikdarstellung und reproduzierbare Tests auf `tensoralgebra.html` mit test_id/status und Rückrechenbeispielen.
- Kontextprompt auf jeder geeigneten Fachstelle in den drei Tiefen Verstehen, Testen, Vertiefen; thematisch Prompt-/Agent-/Meta-Funktionen als getrennte Perspektiven.
- Nur geprüfte Promptpakete als „ausgeführt/getestet“ bezeichnen. Freigabe setzt Eingabe, Output, Modellversion, Fehleranalyse und redaktionelle Entscheidung voraus.
- Vier Quellenzugangsklassen (digital verifiziert; digital nicht erreichbar; händisch prüfen; nur Nils digital geprüft) getrennt von Evidenz und Veröffentlichung; zusätzlich `prüfung_ausstehend` als vorgelagerter Prozess.
**Abnahme:** wenigstens ein vollständiger publizierbarer Logik- oder Algebra-Pilot; geschlossene Rückführung aus öffentlicher Taskkarte zu getesteter Forschungsakte.

## 4. Neue Designgrammatik
- Fachfarbe/Fachgrafiken erhalten; ein leicht erkennbarer Dreiklang **Quelle / Operation / Gegenprobe** kann jeden Fachabschnitt begleiten.
- Anwendungsmodi A/B/C/G als dezente Reiter oder aufklappbare Vergleichsabschnitte – **nicht** vier neue konkurrierende Header-Navigationen.
- Prompt-, Agent- und Metaebene mit ikonischen, barrierearmen Karten und expliziten Teststatus; Farbe niemals alleiniger Status.
- Zwei Ansichten: „Einfach erklärt“ und „Fachlicher Nachweis“ als progressive Vertiefung auf derselben Fachseite.
- Feld- und Graphvisualisierungen nutzen originale SVGs/Diagramme, verlinkte Quellen und Alttexte; interaktive Visualisierung nur zusätzlich.
- Bei Beweisbehauptungen zwingende Trennung: bewiesen unter Modellaxiomen / Simulation / empirischer Befund / Hypothese.

## 5. Git-Abstimmung und Commitstandard
- Claude liefert `forschung/koordination/RUECKGABE_DATEN_KI_*.md` und versionierte `forschung/register/...`-Objekte.
- ChatGPT legt für jede Website-Teiländerung einen kurzen Report in `forschung/website/CHANGELOG_*.md` ab: geänderte Datei, Original-SHA, Commit, inhaltlicher Anlass, Quellen-/Datenversion, Testnachweise, regressionsgefährdete Inhalte, nächste Freigabe.
- Keine direkte Bearbeitung der fachlichen Originaldaten durch die Website-KI. Keine Umbenennung alter URLs oder IDs ohne Redirect und Crosswalk.
- Falls Claude die Datenverträge verändert, wird das Web erst nach Schema-/Kompatibilitätsprüfung aktualisiert.
- Hier erstellte Dokumente sind Koordinationsberichte, **keine** unmittelbar zu publizierenden Website-Absätze.

## 6. Erste umzuse tzende Pakete
1. W0 Bestandsschutz/Navigation incl. `tensor-paper.html`, Tests.
2. W1 Tensor-Einführung um A/B/C/G erweitern, Fakten- und Quellenstatus dokumentieren.
3. W2 Logik-Tensor/Feldtheorie-Erklärung anhand der bestehenden drei Matrizen aufwerten, noch keine unbeglaubigten neuen Fachbehauptungen.
4. W3 bereits abgenommene algebraische Beispiele und geprüfte Kontextprompts integrieren.
5. Gesamtprojekt-/Publikations-Dashboard mit Claudes Evidenz- und Aufgabenregister verbinden.

## 7. P0-Entscheidungen
**Keine endgültige Achsenwahl erzwingen.** A/B/C und G als getrennte Modelle sichtbar halten, nur typisierte und belegte Übersetzungen zulassen. Die Website ist nicht der Ort, die mathematischen Modellentscheidungen vorwegzunehmen. Buch-/Paper-Originale in ihren bisherigen Referenzen erhalten. Die neue Machtbuch-Ausarbeitung bleibt zunächst ein Prompt-/Forschungsprozess und wird nicht automatisch als neues freigegebenes Buch ausgegeben.

**Verweise:** [Daten-KI-Briefing](../koordination/BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md) · [Vorherige Übergabe](../koordination/UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md).
