# Website-System 3.0 · Visuelle Forschung, didaktische Struktur und Geo-KI als Referenz
**Arbeitsfassung 2026-11-04 · Status: Entwurfs- und Prüfplan, keine wissenschaftliche Gesamtabnahme.**
**Geltung:** `docs/` für die Gesamtplattform KI-Tensor / SOULution. Die Website ist die Oberfläche; Claude/GPT liefern quellgebundene Daten, Tests und freigegebene Ergebnisse. Bestehende Originale bleiben versioniert erhalten.

## 1. Ziel und grundlegende Entscheidung
Eine Website mit wenigen Hauptseiten und wissenschaftlich zusammenhängenden Inhaltsblöcken statt vielen gleichrangigen Einzel-Webseiten. Hauptnavigation: **Start · KI · Tensor · Projekte · Harvesting · Publikationen · Mitmachen · SOULution**. Inkubator ist ein vertiefter Publikationsblock; Tensoralgebra ein vertiefter Tensorblock; KI-Kollegen sind ein KI-Block; vier Kernprojekte sind **Mini-KI, Komprimierung, visuelle Engine und Geo-KI**. Fachseiten und alte ausführliche URLs bleiben erreichbar, werden in der Hauptnavigation aber nicht dupliziert.

**Regel 3×3:** Höchstens drei Karten nebeneinander; bevorzugt drei sinnvolle Karten innerhalb eines klar gerahmten Metathemas. Drei Spalten sind eine maximale Darstellung, keine Pflicht zu künstlichen Dreiergruppen. Mobil 2 beziehungsweise 1 Spalte. Ein Themenrahmen hat immer Titel, begründete Frage, eine Erklärung, drei oder weniger zentrale Handlungskarten, Quell-/Statuspfad und die nächste Handlung.

## 2. Gemeinsames visuelles System
- **Geo-KI** azur/petrol (Fachfarbe `--ux-geo`) und echtes Erd-/Koordinatensymbol `#earth`. Operatoren: Petrol; Prüfgegenfälle: warmes Orange; wissenschaftliche Unsicherheit: neutrales Grau. Farbe nie allein zur Unterscheidung benutzen.
- **KI** Violett + `#ki`, **Mini-KI** Violett + `#mini`, **Tensor** Teal + `#tensor`, **Komprimierung** Ocker + `#compress`, **visuelle Engine** Magenta + `#eye`, **Publikationen** Blau + `#book`, **Inkubator** Beere + `#inkubator`, **SOULution** Grün + eigene Wortmarke.
- Icons kommen als SVG aus `assets/tensor-icons.svg`, nicht aus Plattform-abhängigen Emojis. Einheitliche visuelle Grammatik: beobachtbarer Gegenstand = gefüllte Form; Eingabe = Kreis; Operator = Pfeil; gesetzmäßige Relation = beschriftete Linie; erhaltene Eigenschaft = durchgehender Ring; Hypothese = gepunktete Linie; Gegenbeleg = durchgestrichene Verbindung; offene Frage = dezentes Fragezeichen mit Textstatus.
- Titelhierarchie: ein H1 pro Seite, H2 pro Metathema, H3 pro Karte. Schriftdichte ruhig, Serifenschrift optional nur für prägnante Zitate/Leitsätze, nicht für Zahlen und Formeln. Alle Grafiken bekommen ALT/Bildunterschrift und bei Bedarf eine zugängliche Textgleichung.
- **Erkenntnisstatus verpflichtend:** etabliertes wissenschaftliches Gesetz, implementierter Code, bestandener Softwaretest, mathematisch geprüfte Relation, vorläufige Hypothese, widersprochen/negativ, offene Frage, nur Inventar. Niemals aus einem Bestandszähler einen Erfolgsgrad ableiten.
- Farben und Icons über gemeinsame CSS-/SVG-Assets; keine fachseitenspezifischen duplizierten globalen Navigationsregeln. HTML/CSS validieren und bei jedem Rollout Mobile-/Fokus-/Kontrast- und Animations-Tests ausführen.

## 3. Die Didaktik jedes Forschungsthemas
**Sieben wiederverwendbare Erklärungsschritte:**
1. Eine relevante Frage aus Lebenswelt, Fachmodell oder Anwendung.
2. Ein begreifbarer Gegenstand und veränderbare Eingaben.
3. Eine ausdrückliche mathematische oder technische Regel.
4. Eine beobachtbare Wirkung als Diagramm, Formel, Code oder Datenkarte.
5. Eine Gegenprobe – Invariante, falscher Fall, Randbedingung, Rückrechnung oder erklärter Informationsverlust.
6. Die Einordnung: bestehende Wissenschaft/Tool, eigene Rekonstruktion, neue Kandidaten, öffentliche Datennachweise.
7. Die nächste Handlung: ausprobieren, nachvollziehen, Quellen prüfen, Mitmachaufgabe, vertiefendes Paper.

**Drei Lesetiefen:** „Verstehen“ (Bild + kurze Frage), „Untersuchen“ (beispielhafte Rechnung/Variation), „Fachprüfung“ (Quellen, Code, Tests, negative Ergebnisse, Version). Kein inhaltsloser Akkordeonwald, aber vertiefbare mathematische Akten. Bei Themen über etwa 1.500–2.000 Wörter oder mehreren beweis-/quellenpflichtigen Teilabschnitten: Übersicht auf Website, vertieftes versioniertes Paper unter Publikationen; keine automatische Buchfreigabe.

## 4. Geo-KI als didaktische Musterseite
Die bereits existierende Seite `docs/geoki.html` enthält vor dem Upgrade interaktive Rotation, eine parametrische Formengalerie, ein 27-Adressdiagramm, einen Werkzeugvergleich, 14/14 als historischen Suite-Test und das Mitmachprojekt GEO-OPS-01.
**Neue kohärente Lerngeschichte:**
1. **Eine Regel:** Punkt (1,0), Drehwinkel θ, Operator Rθ; Originalgleichung und visuelle Vorher/Nachher-Vektoren.
2. **Invariante:** norm(Rθ p)=norm(p), Eingabe und Resultat neben der Grafik. Der Nutzer verändert den Winkel; Koordinaten ändern sich, Norm nicht.
3. **Komposition:** Test Rβ(Rα(p))=R(α+β)(p); mit zwei Reglern. Rückprobe R(-α)Rαp=p. Negativkontrast: Skalierung verändert im Allgemeinen die Länge; Spiegelung ist keine Rotation.
4. **Formen erzeugen:** Polygon, Stern, Rosette, Kurvennetz aus parametrisierbaren Regeln. „38.880 mögliche Parameterkombinationen“ als rechnerische Inventargröße, keine Zahl eigenständiger Formen oder gemessener Kompressionsersparnisse.
5. **Skill-Modul:** 13 im Python-Code vorhandene Funktionen und die acht noch ungeprüften Formatfamilien mit öffentlichen Daten (JSON, Quellcode und Suite-Testbericht). Die Visualisierung ist eine separate JS-Implementierung, nicht Beweis für Python-Testidentität.
6. **Einordnung:** Was ist ein Algorithmus, was ein Generator, was eine KI? Ein bewusst komponierter Algorithmus lernt nicht automatisch; erst eigenständige Auswahl, Feedback, Transfer und kontrollierte Baselines zeigen zusätzliche Fähigkeit.
7. **Projektbeteiligung:** GEO-OPS-01 als kleine Aufgabe mit Eingabewerten, Formel, prüfbarem Erwartungswert, Gegenbeispiel, Quelle, Exportweg und Review.
**Echte Referenzen:** `forschung/geoki/v0_4/src/geometry.py`, `forschung/geoki/v0_4/TESTRESULT.md`, `docs/data/skills-oeffentlich-v1.json`, `docs/forschungsdaten.html`. Ungeprüfte Geo-/CAD-Bibliotheken sind Anschlusskandidaten, keine aktivierten Skills.

## 5. Datenorientierte gemeinsame Komponenten
- **PublicDataCard:** Anzeige von ID, Name, Datenstand, Status, Quell-URL, Prüfcode, negativer Aussage und Änderungsdatum. Quelle nicht aus dem Beschreibungstext erraten.
- **OperatorExplorer:** Eingabeparameter + Originalgleichung + Visualisierung + Baseline + Gegenprobe und Rundungstoleranz. Inhalte kommen aus einem versionsgebundenen Skillregister.
- **TensorPositionViewer:** Tensor-ID@Version, Trinitäten, 27 Felder, belegte/widerlegte/offene Relationen, Operator, Gegenbeispiel, Originalquelle. Feldadressen sind nicht Beweise. Fehlendes Feld bleibt mit „untersucht? nein“ erkennbar.
- **EvidencePath:** Original → Formel/Modell → typisierte Relation → Trinität → Tensorfeld → Test → Evidenzstatus → Version.
- **ResearchPromptCard:** Forschungsfrage, kleinste machbare Aufgabe, prüfbare Eingabe/Ausgabe, Vergleich, Einreichung, Moderation und Reproduktionsnachweis.
- **PublicationLink:** Überblick ↔ versioniertes Paper ↔ Quellen/Glossar ↔ Originaldaten; längerer Text darf in der Navigation niemals eine gleichrangige neue Hauptseite erzwingen.
Diese Komponenten teilen dieselben IDs und dürfen keine parallelen, voneinander abweichenden Faktenbestände führen.

## 6. Fehler- und Abnahmekriterien
**Sofort technisch prüfen:** SVG-Sprite vorhanden und alle `use href`-IDs definiert; externe Links erreichbar; keine defekten Anker, Doppel-IDs, ungültigen verschachtelten Links/Labels; Skripte syntaxvalidiert; Lade-/Fehlerzustand bei JSON-Fetch; 27 Adressen je Tensor, drei Achsen mit je drei Elementen; keine 4+-Spaltenlayouts; Tab-/Screenreader-Navigation bei Reglern und SVG; Darkmode-Kontrast; SVG bei 320/375/768/1440 px.
**Wissenschaftlich prüfen:** Rotation und inverse Rotation numerisch mit Toleranz, direkt vs zusammengesetzt, mindestens ein Negativfall, Quelle jeder Zählzahl, neuer Datenstand sichtbar; kein Begriff „bestätigtes KI-Lernen“ ohne kontrollierten Transfer-Test.
**Redaktionell prüfen:** Jeder Metablock beantwortet eine Leitfrage und führt zur Folgeseite; keine sichtbaren internen Arbeitsanweisungen auf der Website. Projektmanagement ist vom Hauptmenü entkoppelt; ein Footerzugang darf nicht versehentlich als Zugangs-/Sicherheitskontrolle missverstanden werden.
**Abschluss:** (1) Gültige Daten und Grafiken, (2) desktop/mobile, (3) Keyboard/Fokus, (4) fachliche Stichprobe, (5) funktionierende Links, (6) Claude-Datengegenprüfung, (7) redaktionelle Freigabe.

## 7. Projektkoordination
Claude liefert bibliothekarisch und wissenschaftlich geprüfte Datenmodule, typisierte Operatoren, mathematische Signaturen, Gegenbeispiele und Quellenstatus; GPT baut Website-/Lernmodule mit deren öffentlichem Datenvertrag und kontrolliert UI/Didaktik. Das gemeinsame No-Loss-Nachziehen umfasst Glossar, Quellen, Skills, Feldakten, Thesen, Register und Publikationen; die bestehende Harvesting-Pipeline ist Datenproduzent, keine parallel arbeitende Website-Datenbank.
**Reihenfolge:** Geo-KI Musterseite und visuelle Engine → öffentliche Tensor-/Skilldaten → Tensor-Seite, KI-Seite → vier Kernprojekte & Dashboard → Publikationen, Inkubator, SOULution → Mitmachen & globale QA. Bestehenden Zyklus 001 nicht durch ungeprüfte neue Themenstarts umgehen.
