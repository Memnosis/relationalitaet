# Website-Bündel 02: Tensor, Logik, Feldtheorie
Stand 2026-11-03. Verantwortlich GPT (Website), Claude (Quellen, Daten, Fachtests und Promptentwicklung), Nils (fachliche und redaktionelle Entscheidungen).
**Dies ist ein Arbeitsplan, kein Bericht bereits abgeschlossener Website-Arbeiten.**

## Ausgangslage
Auf GitHub geprüft sind `docs/index.html`, `docs/tensor-einfuehrung.html`, `docs/tensor-paper.html`, `docs/tensoralgebra.html`, `docs/projektstand.html` und `docs/mitmachen.html`. Die gemeinsame Navigation ist dort als Skript eingebunden. Eine vollständige Browser-, Mobil-, Tastatur- und Screenreader-Abnahme ist bislang nicht belegt.

## Umsetzungsreihenfolge

### WEB-B02-01 — Bestehende Seite und Navigation absichern (P0)
GPT: Seiteninventar, alte Links, Seitenanker, Assets, unveränderte Bücher/Cover, Textdifferenzen; Funktion des hierarchischen Menüs, Mobilansicht, Fokus/Tastatur und Fallback prüfen. Nichts löschen/verkürzen.
**Abnahme:** technische Testakte plus Abweichungsliste und konkrete Commits. Keine Claude-Abhängigkeit.

### WEB-B02-02 — Tensor-Einführung didaktisch verbessern (P0)
GPT ergänzt auf `tensor-einfuehrung.html` einen fortschreitenden Lernpfad: Zahl → Tabelle → Datenwürfel → 27er-Graph → mathematischer Tensor. Dazu vier unterscheidbare Modelle: A = historische neutrale Achsen; B = operative Triaden (im Original T1/T3/T5); C = wissenschaftlich fachimmanente Trinitäten; G = gewählter mathematischer Träger.
**Abnahme:** Originalgrafiken, Ringmatrix und bestehende Erklärungen erhalten; 27 Adressen sind nicht 27 bestätigte Fachresultate. Claude liefert später Nachweis-Crosswalk.

### WEB-B02-03 — Logik-Tensor und Feldtheorie als aktueller Wissenschaftsstand (P0)
GPT ergänzt `tensor-paper.html` um die erkennbare Trennung Original v1.0 / heutige wissenschaftliche Weiterentwicklung. Drei ursprüngliche 3×3-Matrizen und 27 Fachpositionen bleiben, ebenso alle Originalquellen. Feldordnung, formale Nachbarschaft, dynamisches Modell und physikalische Feldtheorie nicht vermischen.
**Abnahme:** alle Originalinhalte/DOIs funktionieren, neue Aussagen haben Quellen-, Geltungs- und Prüfstatus. Claudes DATA-001/002/004 für fachliche Freigabe berücksichtigen. 2.0 und 2.1 bleiben Arbeitsmanuskripte, keine automatisch freigegebenen Bücher.

### WEB-B02-04 — Ein tatsächlicher Logik-/Algebra-Test mit Gegenmodell (P1)
GPT ergänzt ein nachrechenbares Beispiel, bevorzugt Modus ponens samt falscher Alternativableitung oder den bereits untersuchten 27er-Graphen. Test-ID, Input/Output, Quelle, Grenzen und Negativbefund sichtbar trennen.
**Abnahme:** wiederholbarer Test und keine falsche Universalitätsbehauptung. Claude liefert die Fach- und Quellenreferenzen.

### WEB-B02-05 — Vier Quellenprüfklassen und Evidenz getrennt zeigen (P1)
GPT gestaltet eine Quellkarte für `digital_verifiziert`, `digital_nicht_erreichbar`, `handpruefung_noetig`, `nur_nils_digital_geprueft`, zusätzlich `pruefung_ausstehend` vor tatsächlichem Zugriffsversuch. Wissenschaftlicher Beleg und Publikationsfreigabe sind eigenständige Angaben.
**Abnahme:** ohne datierten echten Prüfnachweis keine Behauptung „digital verifiziert“; keine vertraulichen Quellenzugänge ausgeben. Claude-Datenschema abwarten.

### WEB-B02-06 — Kontextprompts direkt an passenden Webseitenabschnitten (P1)
GPT ergänzt nutzernahe Einstiege (Verstehen/Nachrechnen/Vertiefen) und die didaktischen Funktionsebenen Prompt/Agent/Meta. Claude entwickelt und testet fachliche Prompts; Veröffentlichung erst nach nachgewiesenem echten Ausführungslauf und redaktioneller Freigabe.
**Abnahme:** eine getestete, eigenständig bearbeitbare Aufgabe mit eindeutigem Rückgabeformat für Personen ohne Git-Schreibzugriff; keine Veröffentlichung interner Architekturprompts.

### WEB-B02-07 — Dashboard, Quellen, Publikationswege (P1)
GPT verbindet `projektstand.html`, Bibliothek, Medien und Mitmachen mit freigegebenen, versionierten Register-Ansichten von Claude. Getrennte Fortschrittswerte für Inventar, Quellen, Tests, Prompts und Veröffentlichungen statt erfundener Gesamterfüllung. Nach 3/6/9 abgeschlossenen KI-Zyklen jeweils den echten Analysebericht verlinken.
**Abnahme:** datierter Zähler/Nenner, stabile IDs, Schutz vor unfreigegebenen Manuskipten und Originalen; existierende Bücher und Cover bleiben.

## Gestaltung und Qualitätsstandard
- Bestehendes Design aufwerten, nicht neu erfinden. Rote Mitmachseite, grüne SOULution-Seite, SVG-Icons, responsive Karten, Serifenelemente, bestehender unterer Mitmach-CTA erhalten.
- Navigation hierarchisch: Start, Forschung, Projekte, Inkubator, Publikationen, Mitmachen, SOULution; bisherige URLs und Deep Links stabil halten.
- Zwei Verständnistiefen: „einfach erklärt“ und „fachlich nachgewiesen“. Wissenschaftlichen Befund, Quellenverfügbarkeit und Prompt-Teststand getrennt markieren.
- Jeder Changebericht nennt Task-ID, Original-SHA, Änderung, Commit, Test, Claude-Datenrevision und offene Entscheidungen.
- Die letzten 100+ Originalbefehle bleiben ein eigenständiges P0-Audit; 44 Aufgabenfamilien sind kein nachgewiesener vollständiger 100er-Abgleich.

## Arbeitsteilung und Taktung
Sofort: WEB-B02-01, dann WEB-B02-02, WEB-B02-03 in fachlich zurückhaltender Fassung. Claudes Evidenz-/Promptberichte ermöglichen WEB-B02-04 bis -07. Erst nach dem Website-Grundupgrade folgen die weiteren unfertigen Bücher als getrennte Claude-Forschungs-/Prompt- und GPT-Publikations-/Websiteaufgaben.
Nach je drei vollständig bestätigten Austauschzyklen analysieren (3, 6, 9); nach der dritten Analyse entscheidet Nils über Fortführung und optionale Zyklen 10–12.
Siehe [Koordinationsrhythmus](../koordination/RHYTHMUS_3_3_9_12_KI_AUSTAUSCH_2026-11-03.md).
