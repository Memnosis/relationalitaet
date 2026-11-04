# Bürger-KI · Designgrammatik und Darstellungsregeln v1.0
**Stand:** 2026-11-04 · **Geltungsbereich:** `docs/buerger-ki*.html` und `docs/assets/buerger-ki-design.css`. Kein Eingriff in globale Tensor- oder SOULution-Styles. **Ziel:** Erkenntnisse ohne Verlust überführen, ohne die Website in ein Textarchiv zu verwandeln.

## 1. Prinzip: Farbe bezeichnet Bedeutung – nicht Qualität
Die Bürger-KI-Grundfarbe ist ein ruhiges, dunkles Grün (`#176f63` auf hellem Hintergrund). Sekundärfarben werden **einheitlich nach Themenfamilie**, nicht zur dekorativen Abwechslung verwendet. Gleiche Farbe darf keine widersprüchlichen Bedeutungen erhalten.

| Thema | Kennung | Hell-Modus-Farbe | Iconmotiv |
|---|---|---|---|
| P01 Mein Recht | `right` | `#176f63` | Waage |
| P02 Unser gemeinsames Problem | `community` | `#365e9c` | Menschen/Netz |
| P03 Gesellschaftliche Grundlagen | `society` | `#71538f` | Institution/Säule |
| P04 Lernen | `learning` | `#906219` | Buch/Kompass |
| P05 Skills | `skills` | `#28768a` | Werkzeug/Verbindung |
| P06 Benchmark | `benchmark` | `#4f5f7f` | Messleiste |
| P07 Evidenz | `evidence` | `#6a597d` | Lupe/Beleg |
| P08 Lösungen | `solution` | `#33764d` | Weg/Verbesserung |
| Querschnitt Prävention/Kultur | `prevention` | `#916039` | Dialog/Schutz |

**Wichtig:** Status „verifiziert“, „offen“, „widerlegt“ ist **nicht durch dieselbe Pfadfarbe kodiert**. Status braucht immer ein ausgeschriebenes Label, optional ein zusätzliches Icon. Keine farbige Gesamtbewertung, ohne dass das Testurteil belegt ist. Keine voreiligen grünen Häkchen.

## 2. Typografie und Rhythmus
- Verständliche Systemschrift, Mindestbasis 16 px, Fließtext 1.68, Maximalbreite Hauptinhalt 1160 px.
- Überschriften mit abgestufter Größenordnung und korrekter `h1 → h2 → h3`-Hierarchie; pro Seite genau ein `h1`.
- Abschnittsabstand 40–68 px, Karteninnenabstand 18–24 px. Kurze Absätze statt Textwände.
- Lange juristische Nachweise in Deep-Dives, nicht unaufgefordert als Ganztext auf der Startseite.
- Listen für Schritte, Tabellen für echte Vergleiche, Diagramme für Relationen und Prozesse; keine willkürliche Dekoration.
- Mobile: Karten einspaltig, Navigation umbrechen, Tabellen horizontal lesbar, Touch-Ziele mindestens 40 px. Dunkelmodus und `prefers-reduced-motion` beachten.

## 3. Boxengrammatik
| Komponente | Zweck | Pflichtinhalt |
|---|---|---|
| `.hero` | Eine zentrale Frage oder These einführen | Kicker, Titel, Kurzbeschreibung, nächster Einstieg |
| `.card` | Ein Themen-/Werkzeugobjekt | sprechender Titel, Zweck, nächster Schritt oder Link |
| `.bk-topic.bk-path-card[data-topic]` | Thematische Navigation | Pfad, Icon, Beschreibung und echte Zielseite |
| `.bk-case` | Durchgehende Fallakte | Szenario, Kontext, Ziel, Status, Nachweise |
| `.bk-steps` / `.bk-step` | Chronologischer Ablauf | tatsächliche Reihenfolge und Übergangsbedingungen |
| `.bk-evidence-note` | Quellen-, Evidenz- und Prüfgrenzen | Was ist belegt? Was ist offen? |
| `.bk-method-note` | Methodik, Definition und Gegenprobe | Wie wurde geprüft? Was könnte die Aussage widerlegen? |
| `.note` | sachliche Orientierung | präzise Kernaussage |
| `.warning` | Risiko / mögliche Fehlinterpretation | konkrete Gefahr und Vorgehensweise |
| `.bk-status[data-status]` | Forschungsstatus | Klartext, Stand, Test- bzw. Quellenbezug |
| `details/summary` | Zusätzliche Vertiefung | vorausgehende Kurzfassung; keine kritischen Kerninformationen ausschließlich verstecken |

Keine Verschachtelung endloser Boxen. Maximal eine klare Hauptaktion pro sichtbarer Karte. Keine dekorativen farbgefüllten „Fazit“-Kästen.

## 4. Icongrammatik
Icons tragen die *Art* eines Objekts (Recht=Waage, Gemeinschaft=Menschen, Forschung=Lupe), nicht eine nicht belegte Bewertung. Gleicher Begriff bekommt überall dasselbe Motiv. 20–24 px in Karten, 16–20 px in Navigationslabels; einheitliche Strichstärke ca. 1.7. In wiederholten Karten SVG mit `aria-hidden=true` und **sichtbarem Text**. Keine Emojis als Ersatz für konsistente Fachsymbole. Vorhandene `tensor-icons.svg` dürfen für gleichbedeutende Symbole referenziert werden, jedoch ohne die globale Datei zu ändern. Separates eigenes SVG-Set nur bei echtem Bedarf.

## 5. Wissenschaftliche Semantik und No-Loss
Jede tiefgehende Node-Akte besitzt ID, Definition, Quelle, Geltungsbereich/Zeit, Behauptung, Gegenposition, Operation/Skill, Test, Evidenzstatus, Version, verknüpfte Seiten. Der öffentliche Text darf gekürzt werden; der Wissensbestand nicht. Unterschiedliche Pfade verlinken denselben Eintrag statt voneinander abweichender Versionen.

**Unbedingt trennen:**
1. Rechtlich verbindliche Norm (Primärquelle und Rechtsstand).
2. Beobachteter Fakt (Messmethode und Geltungsbereich).
3. Interpretation und Hypothese (Gegenbelege).
4. Ziel-/Wertentscheidung (keine Tatsachenbehauptung).
5. Vorschlag / Experiment (noch nicht belegte Wirkung).
6. Gemessener Effekt (Baseline, Nenner, Unsicherheit).

## 6. Diagrammgrammatik
- **Prozess:** gerichtete Schritte mit eindeutigen Ein-/Ausgängen.
- **Relation:** verbundene Nodes mit benannten Kanten (z.B. verpflichtet, beruht auf, widerlegt, erfordert).
- **Vergleich:** gleiche Skala und eindeutige Einheit.
- **Zeit:** Achse und Zeitraum sind explizit angegeben.
- **Ergebnis:** Soll, Ist und Messmethode nebeneinander.
- **Ungewissheit:** fehlende Daten/Unsicherheitsband sichtbar lassen.
- Keine 3×3×3-Würfel als Dekoration und keine rein metaphorischen „Tensor“-Zahlen.

## 7. Rechte, Gesundheit, Datenschutz
- Die Website ist derzeit **kein Chatbot, keine individuelle Fallberatung und kein Patientenakten-Backend**.
- Eigenes Ordnen von Daten kann lokal oder analog erfolgen. Keine automatische Upload- oder Gruppendatenfunktion erfinden.
- Keine Gesundheitsakte öffentlich in Issues, Gruppenforen oder Feedback-Felder lenken.
- Akute Hilfen und niedrigschwellige Einstiegsmöglichkeiten sichtbar; kein Lernzwang.
- Keine vermeintliche Rechtsverletzung, Diagnose oder „nachgewiesene Unterversorgung“ allein mit einer Farbbewertung behaupten.

## 8. Komponenten und Implementierung
- Zentrale Bürger-KI-Stile: `docs/assets/buerger-ki-design.css`
- Seiten werden durch `body.bk-page` eindeutig abgegrenzt. Thematische Komponenten: `.bk-topic[data-topic]`.
- Die vorhandenen globalen Tensor-CSS-Dateien bleiben unverändert; Bürger-KI kann sie ergänzen.
- Jedes neue UI-Element muss semantisch, per Tastatur und mobil nutzbar sein.
- Bei der Übernahme in einzelne Wissenspfade stets die Component-Tokens statt neuer Inline-Farbwerte verwenden.

## 9. Abnahmetests
1. Jede Seite hat ein `h1` und korrekte Verzeichnis-/Pfadnavigation.
2. Links zeigen auf existierende, zur Freigabe vorgesehene Seiten; keine kaputten Anker.
3. Kontraste für Fließtext und Bedienelemente nach WCAG AA prüfen; Farbe nie allein bedeutungstragend.
4. Tastatur, Fokus, Mobilansicht, Druck und Dunkelmodus testen.
5. No-Loss: Absätze nur nach Quell- und ID-Abgleich zusammenführen.
6. Interne Begriffe, Quellenregister und Glossar im Bürger-KI-Bestand synchron nachziehen.
7. Testdaten als Simulation kennzeichnen; keine fingierten Wirkungsnachweise.
8. Status von Skills und Tensor-Kandidaten nicht durch Design „aufwerten“.
9. Geänderte Bürger-KI-Dateien dokumentieren; keine Änderungen an fremden Projekten.

**Status:** Regeln und CSS umgesetzt; systematischer Browser- und WCAG-Test, vollständige Wissensmigration sowie zusätzliche Pfade stehen noch aus.
