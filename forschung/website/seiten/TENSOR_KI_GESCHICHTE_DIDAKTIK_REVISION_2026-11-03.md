# Didaktische Revision: Tensor-Einführung und KI-Geschichte
Stand: 2026-11-03. GPT-Redaktion, fachliche Claude-Gegenprüfung und echte Browserabnahme offen.

## Tensor-Einführung
Vorher vermischte der erste Bildschirm eine Ringmatrix, ein 27er-Würfelbild, interne Begriffe wie „Feldakte“ und mathematisch unbestätigte Projekthypothesen. Die entscheidenden Prozesse waren zwar in einer späteren vierstufigen Arbeitsübersicht enthalten, erhielten aber keine zusammenhängende Erklärung und kein nachrechenbares Transformationsbeispiel.

Umsetzung in docs/tensor-einfuehrung.html, Commit 9a51a86:
- Würfel- und Ringdarstellung aus der **Einführungsseite** entfernt, historische Git-Originale und Bilddateien nicht gelöscht.
- Mathematische Ebenen Skalar, Vektor, lineare Abbildung, Tensor getrennt von der projektspezifischen Adressierung dargestellt.
- Nachrechenbares 2D-Beispiel y=Mx und Basiswechsel M'=S^-1 M S ergänzt.
- Sechs wissenschaftliche Prozessschritte: Beobachten, Relationen bestimmen, Formalisieren, Berechnen/Verändern, Gegenprüfen, Verbinden/Nachziehen.
- 3×3×3-Adressschema und die unterschiedlichen A/B/C/G-Modellfamilien nachgestellt und als eigene Hypothese begrenzt.
- Logischer Prozess und vollständige „Was folgt als nächstes?“-Lernwege zur Algebra, Logik, Geo-/Mini-KI und Mitmachen.

Ein Feldprotokoll bzw. die historische „Feldakte“ bezeichnet lediglich die dokumentierte Quellen-/Beweisakte zu einer bestimmten strukturierten Relation. Es ist kein allgemein eingeführter mathematischer Tensorbegriff. Der Begriff wird im Einleitungstext nicht mehr als Vorwissen vorausgesetzt.

## KI-Geschichte
Vorher enthielt die Seite historische Stationen (Turing, Dartmouth, symbolische Systeme, Backpropagation, Transformer) und einen sinnvollen Baseline-Vergleich, aber die eigentlichen aktuellen Forschungsspannungen waren nicht deutlich genug als Leitfragen hervorgehoben.

Umsetzung in docs/ki-geschichte.html, Commit ef5b804:
- Sechs Spannungen vor die Chronik gestellt: formale Gültigkeit vs. Plausibilität; explizite Regeln vs. Lernen; Skillkomposition vs. einfache Baseline; starre Struktur vs. Rückkopplung; Masse des Bestands vs. belegte Relation; offene Kooperation vs. Blackbox.
- Je Spannung eine experimentell prüfbare Vergleichsfrage angegeben.
- Dartmouth-Projektvorschlag als historische Quelle gekennzeichnet, die zu heutigen operationalisierten und offenen Fragen führt; **nicht** als Ursprung oder Beweis einer projektinternen 3×3×3-Struktur ausgegeben.
- Fachvertiefung bei KI-Kernforschung, Mini-KI und Tensor-Einführung angebunden.

## Offene wissenschaftliche und technische Qualitätsgates
1. Tensorbegriff und Transformationsgesetz von mathematisch qualifizierter Gegenprüfung kontrollieren lassen; genaue Semantik für A/B/C/G und Dreier-/Rollenachsen aus Originalen prüfen.
2. Quellen/Beweislage der KI-Geschichte historisch sowie bezogen auf konkurrierende Ansätze prüfen; keine scheingenaue universale KI-Definition behaupten.
3. Fachbeispiele zu Dynamik, Feldwirkung und Operatoren in eigenständigen Vertiefungen mit Grenzen und Quellen erarbeiten.
4. HTML-/Tastatur-/Desktop-Browserlauf und relevante Sprungmarken tatsächlich abnehmen; kein erfolgreicher CI-Lauf behauptet.
5. Für beide Seiten echte Autorenfreigabe getrennt vom Datei-Commit einholen.

## Exchange- und Revisionsfunde
Claudes Nachholanalyse NACHHOLANALYSE_CLAUDE_2026-11-03.md wurde tatsächlich gelesen. Sie enthält F1: fehlerhafte "\\n"-Serialisierung im Git-Promptparser und F2: private Exportpfade ins öffentliche Repository möglich. Beides wurde im Parser-Commit ea2c4db korrigiert, synthetische negative Tests im Commit f2cb9cf ergänzt. Deren Bestehen im **committeten** Stand ist bis zur CI-Ausführung nicht bestätigt. Ein vormals berichtetes „6/6 PASS“ ohne passendes Quell-SHA ist gemäß Kooperationsregel R8 kein Git-Abnahmenachweis.

Es gibt eine erste begrenzte KI-Gegenprüfung des Logikprompts und mehrere gegenseitig beantwortete Diskussionen. Der komplette Zyklus 001 bleibt nach STATUS.json offen: gpt_reviewed=false, claude_acknowledged_review=false, cycle_report_created=false. Claudes Nachholanalyse ist damit nicht automatisch eine Gesamtabnahme.