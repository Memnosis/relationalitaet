# Gemeinsamer Design-, Text- und Publikationsstandard v1.0

**Koordination:** GPT (Website/Leserführung) ↔ Claude (Daten, wissenschaftliche Texte, Prompts, Quellen)  
**Auftrag von Nils, 03.11.2026:** Keine starre Textlänge. Ausführlich, soweit Ausdifferenzierung und Allgemeinverständnis es erfordern; Fachwissen gesondert vertiefen. **Durchgängig serifenlose Schrift.** Mobile nachrangig, jedoch keine absichtlichen Funktionsbarrieren. Bestehende Inhalte und freigegebene Originale bleiben durch Änderungsnachweise geschützt. **Status:** zur wechselseitigen Gegenprüfung, nicht automatisch finale redaktionelle Freigabe.

## 1. Grundprinzip: drei Verständnistiefen und drei Arbeitsfunktionen

Eine Facheinheit ist so lang, wie sie für das tatsächliche Verständnis benötigt wird. Nicht auf bestimmte Zeichen-, Absatz- oder Seitenzahlen kürzen. Redundanz reduzieren, aber Definitionen, Voraussetzungen, Beispiele, Gegenbeispiele, historische Entwicklung und Quellen nicht entfernen.

| Ebene | Leserfrage | Pflichtinhalt | Darstellung |
|---|---|---|---|
| E1 Allgemeinverständlich | Was ist das, wozu und weshalb? | begriffliche Einführung ohne unbekannte Fachwörter, Anschauungsbeispiel, Bedeutung, Abgrenzung und eine erkennbare Anschlussfrage | Fließtext, kurze Sinnabschnitte, ein kleines Diagramm/Karte nur wenn erklärend |
| E2 Ausdifferenzierung | Welche Varianten, Grenzfälle und Relationen existieren? | Modelle/Trinitäten, Voraussetzungen, Alternativen, historische Entwicklung, Gegenfälle und Grenzen | gegliederte Fachabschnitte, vergleichende Tabellen mit angemessenen Spaltenbreiten, Relationen-/Prozessdarstellung |
| E3 Fachwissen und Nachweis | Was ist exakt belegt und reproduzierbar? | Original-Claim/Quellenfundstelle, Formalisierung, Beweis/Rechnung, Testumgebung, Gegenmodell, Evidenz-/Geltungsstatus, offene Fachfragen | aufklappbare Fachvertiefung im Web, Quellen-/Beweisakten und ggf. Anhänge in PDF/DOCX |

Die drei **Arbeitsfunktionen** sind *orthogonal*, keine drei Leser-Stufen:
- **Prompt:** klar eingrenzbare fachliche Frage und gewünschtes Ergebnis, verständliche Aufgabenbeschreibung.
- **Agent:** Rollen/Skills, Werkzeuge, I/O-Verträge, Übergabe, Validierungs- und Berechtigungsgrenzen.
- **Meta:** Rahmenbedingungen, Architektur, konkurrierende Modelle, Abhängigkeiten, Forschungsstrategie, Gegenprüfung und Systemgrenzen.
Nicht jeder Leserin alle internen Agenten-/Meta-Anweisungen zeigen. Extern nur geprüftes, eigenständig bearbeitbares Exportpaket.

## 2. Wissenschaftliche Grundarchitektur eines Textes

Bei relevanten Fachtexten in dieser sachlich sinnvollen Reihenfolge:
1. **Titel, Forschungsfrage, Nutzen, Einordnung und Grenzen** – zum Einstieg ohne Fachvorwissen.
2. **Grundbegriffe und notwendiges Vorwissen** – nicht den ganzen Fachwortschatz stillschweigend voraussetzen.
3. **Historischer und eigener Entwicklungsweg** – Originalwerke und Arbeitsstände mit Datum/Version, keine rückwirkende Umdeutung.
4. **Zustands-/Modellvergleich** – A/B/C/G oder andere Fachmodelle mit ihren jeweiligen Geltungsbedingungen, kein voreiliger Crosswalk.
5. **Ausdifferenzierung** – Teilmodelle, Fachfälle, Konsequenzen, Relationen und Sonderfälle.
6. **Formalität / tatsächlicher Test** – Formeln, Invarianten, Operatoren, Gegenrechnungen, negative Befunde.
7. **Quelle, Evidenz, Revisionsstand** – eine eigene DOI ist zuerst Originalbeleg der Autorenthese, kein unabhängiger Universalitätsbeweis.
8. **Anschluss** – Was kann der Leser lernen, überprüfen oder beitragen? Sauber abgegrenzte Prompt-/Agent-/Meta-Arbeitsaufgaben.
9. **Anhang / Codebuch / Reproduktionsakte**, wenn die Detailtiefe eine eigene Nachweisfläche benötigt.

Schreibe natürliche vollständige Sätze. Keine Arbeitsredaktion wie „Originale bleiben unverändert“, „internes Ticket“ oder „Anweisung für GPT“ im öffentlichen Buch-/Website-Fließtext; solche Hinweise stehen nur in Git-Änderungsakten. Begriffe bei der ersten Nennung definieren; Originalsprache wissenschaftlicher Quellen korrekt zitieren. Eigene Hypothesen klar als solche kennzeichnen, aber den Lesefluss nicht mit Statusetiketten überfrachten.

## 3. Typografie und Lesbarkeit – verbindlich

- **Keine Serifenschrift**, weder Überschriften noch Fließtext noch Kästen. Gemeinsame plattformfähige Sans-Stack: `system-ui, -apple-system, "Segoe UI", Arial, sans-serif`. Für Formeln passende integrierte mathematische Fonts/fachliches LaTeX; keine dekorative Serifenschrift einsetzen.
- Grundschrift Website ca. 16–18 CSS-px bei 1.5–1.7 Zeilenabstand; Fließtext-Zeilenbreite ca. 65–85 Zeichen, längere Fachformeln/Tabellen bewusst breiter. Überschriften semantisch H1/H2/H3/H4 mit deutlichen Abständen.
- Kurze Zusammenfassungen sind willkommen, ersetzen aber nicht die fachliche Ausdifferenzierung. Richtwert höchstens drei zentrale Aufgaben pro sichtbarem Kartenabschnitt, weiterführendes Wissen danach.
- Keine globalen Font-Overrides, die auf eingebettete Diagramm- oder mathematische Zeichen unnötig zugreifen; kein kostenpflichtiger oder extern nachladender Font für Grundfunktion nötig.
- **Tabellen:** ID/Nummernspalten schmal; Aussage- und Begründungsspalten erhalten den Platz; keine automatisch gleich breiten Datenspalten. Auf kleinen Bildschirmen horizontal scrollbar, nicht Daten beschneiden.
- PDF/DOCX: echte Absatz-/Überschriftenformate, Navigation/TOC wo sinnvoll, ausreichende Abstände, Seitenumbrüche vor größeren neuen Kapiteln, keine isolierten Überschriften; Text in Tabellenzellen nicht auf 5–7pt zusammendrücken.

## 4. Gestaltung: Farben, Rahmen, Bilder und Icons

### Farbfamilien
**Keine neue Farbcodierung erfinden, wenn eine Projektfarbe bereits existiert.** Die aktuellen CSS-Farbvariablen `--mini`, `--geo`, `--algebra`, `--compression`, `--visual`, `--colleagues` sowie `--tensor-accent` werden wiederverwendet. SOULution behält seinen grünen Charakter, Mitmachen die rote Akzentfarbe, Fachseiten eigene konsistente Akzente. Farbe unterscheidet *Bereiche*, niemals allein Evidenz oder Prüfstatus (zusätzlich Text/Icon).

### Karten und Rahmen
- Außenrahmen dezent, leichte Rundung, Innenabstand; Unterkarten mit linkem Farbstreifen als Orientierung. Kein bunt gefüllter „Summary-Kasten“ mit Signalcharakter.
- Ein Themenblock enthält eine vollständige Sinn-Einheit. Ein aufklappbarer Fachabschnitt `<details>` ist sinnvoll bei zusätzlicher E3-Tiefe, nicht zum Verbergen unverzichtbarer E1-Grundinformationen.
- Icons verwenden ein gemeinsames bestehendes SVG-Sprite `docs/assets/media/research-icons.svg`, bevorzugt als kleine Kontextmarker statt große Illustrationen. Mini-Bilder nur dort, wo sie Sachverhalte zeigen: 3×3-Matrix, 27er-Graph, Formel-Pfad, Prozessübergang. Keine Stockgrafik ohne erklärenden Mehrwert.
- Bilder mit Alttext/Quelle/Lizenz, keine unlesbaren Mini-Abbildungen, keine neu erfundenen Cover. Originalgrafiken nicht ohne Autorentscheidung austauschen.

### Inhaltsdiagramme
Immer einen **fachlich erklärten Zusammenhang** zeigen, nicht bloße Dekoration. Einheitliche Diagrammgrammatik:
- Elemente/Träger als Knoten, definierte Relationen als beschriftete Pfeile;
- Zustand/Prozess/Ergebnis unterscheidbar, Geltungsgrenzen ausdrücklich sichtbar;
- unbestätigte Pfeile als Hypothesen beschreiben, Test und Gegenbeispiel als eigene Schritte;
- bei Tensoren historische Null/Zyklus/Einheits-Matrizen und heutige Achsenmodelle nicht visuell vermischen.

## 5. Website-Regeln

Bestehende Seiten bewahren und additiv verbessern. Hauptpfad: Start → Grundlagen → Fachbeispiel → Mathematik / Quelle / Test → freigegebene Mitmachaufgabe. Deep Links und historische Anker erhalten. Navigation nie gleichzeitig durch zwei konkurrierende Skripte betreiben; Integrationszweig nicht ungeprüft mergen.

**Desktop-Erklärung hat zunächst Priorität**, anschließend Barrierefreiheit/Regression und Mobile. Trotzdem bereits jetzt flexibles Layout ohne Überlauf und Bedienbarkeit mit Tastatur. Keine funktionierenden Mobilfunktionen absichtlich entfernen.

Quellen im sichtbaren Artikel **claimbezogen**; gesamte in Überarbeitung befindliche Zenodo-/Eigenwerkübersicht bleibt in einem tatsächlich privaten Arbeitsraum und umfasst auch Git-/Archiv-/Fremdquellen. Das öffentliche Repo `main` ist kein privater Speicher.

## 6. Regeln für Markdown

- H1 nur Dokumenttitel; H2 Kapitel, H3 Unterkapitel. Definitionen und Thesen vollständig ausformulieren, keine Tabelle als Ersatz für notwendige Argumentation.
- Formeln in LaTeX-Blöcken mit Definitionen sämtlicher Symbole, Einheiten und Geltung. Tabellen nur bei echtem Vergleichsnutzen.
- Quellen-/Claim-IDs in unveränderlicher Version, Datum, Autoren- und Rechteangaben; Markdown-Links testbar; Arbeitsstatus separat zum Fließtext.
- Exportfähige Metadaten vorn (Titel, Autor, Version, Datum, Quellen-/Evidenzstatus, original_work_id, review_status), aber keine internen Geheimnisse öffentlich.

## 7. Regeln für Word (DOCX)

- Einheitliche Vorlagen: Titel, Untertitel, Abstract, H1–H3, Grundtext, Bildunterschrift, Formel, Quelle, Anhang. Für alle Text-Styles dieselbe serifenlose Fontfamilie.
- Klickbares Inhaltsverzeichnis aus echten Überschriftenfeldern statt manuell geschriebener Seitenzahlen; Header/Footers mit kurzem Werktitel und Seitenzahlen; bei umfangreichen Arbeiten Glossar und Literaturverzeichnis.
- Tabellen auto-fit nur kontrolliert, schmale Nummern-/Statusspalten; Wiederholung Tabellenkopf, Tabellen nicht ungewollt zerreißen; Bildunterschriften und Quellen am Bild.
- Abschnitts- und Seitenumbruch-Regeln festlegen, Bild-/Tabellennummern und Querverweise pflegen. DOCX ist **bearbeitbare Quelle**, nicht nur konvertiertes PDF.

## 8. Regeln für PDF

- PDF aus der finalen Manuskriptversion erzeugen, nicht ein anderes redaktionelles Universum. Sans-Schriften, lesbare Formeln, verlinkte Quellen, Inhaltsverzeichnis/Bookmarks und wo möglich PDF-Tagging.
- A4 mit vernünftigen Rändern für Buch-/Paper-Ausgabe; randlose Vollseiten nur für ausdrücklich als Anzeigen/Cover vorgesehene Elemente.
- Diagramme und Bilder auf sinnvolle Auflösung, scharfe Vektorgrafiken bevorzugen; keine Überschneidung oder abgeschnittene Fußnoten, Tabellen, Formeln.
- Vor Versand/rendering: jede Seite auf Umbrüche, Leerseiten, kleine Schrift, Alt-/Bildunterschrift, Daten- und Versionskonsistenz prüfen. PDF-Seitenzahl ist **kein Inhaltsqualitätsmaß**.
- Bei Veröffentlichung DOI-/Originalversionen sowie Errata getrennt verlinken; fertige Bücher erst nach Autorenfreigabe, Arbeitsmanuskripte als Arbeitsfassung kennzeichnen.

## 9. Gegenseitiges Prüfverfahren / Fehlerklassen

Claude prüft GPT auf didaktische Vollständigkeit, fachlich korrekte Begriffe, Quellenbezug, Textumfang, Gestaltungsregeln, originalgetreue Darstellung und fehlende Gegenmodelle (W01–W10 + X01). GPT prüft Claude auf No-Loss, Quellen-/Claimstatus, operatorische Formalisierung, Testreproduzierbarkeit, Textebenen, Daten-/Web-Schnittstellen und Publikationsrisiken (D01–D10 + X01).

Mängel klassifizieren: `blocker`, `fachfehler`, `didaktische_luecke`, `gestaltungsfehler`, `editorial`, `offene_hypothese`. Jede Korrektur benennt SHAs, Gegenprobe und Regression. Jeder voll abgeschlossene Austausch wird separat berichtet; nach je drei vollen Zyklen übergreifende Analyse, nach drei Analysen Nils-Entscheidung (optional bis zwölf).

## 10. Konkrete Anwendung im nächsten Paket
GPT: `tensoralgebra.html` um E1/E2/E3 und Quellen-/Beweisgrenzen aufwerten; `index.html` mit einer kompakten Einstiegskarte zum aktuellen Lernpfad verbinden; `mitmachen.html` um die Regel E1/E2/E3 × Prompt/Agent/Meta und externe Rückgabe erklären, ohne ungeprüfte öffentliche Prompt-Texte.
Claude: dasselbe Raster für Logik-Tensor 2.0/2.1, die 27 Claim-/Feldakte und die nächsten Buchmanuskripte anwenden; genaue Quellen und die von GPT benötigten kleinen freigegebenen Lesesichten liefern.

**Rückantwort Claude:** unter `forschung/koordination/zyklen/KI-2026-11-03-001/CLAUDE_REVIEW_DESIGN_TEXT_V1.md`, mit mindestens drei Positiv-/Negativbeispielen, Änderungswünschen und gemeinsamer Release-Empfehlung. Ein Dokument in Git ist eine Gegenprüfung, kein vollständiger Zyklusabschluss.
