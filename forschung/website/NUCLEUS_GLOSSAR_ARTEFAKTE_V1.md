# Tensor – progressive Nucleus- und Forschungsartefakt-Darstellung v1.2

Stand: 2026-11-01. Additiver Website-Nachzug, keine Löschung historischer Quellen.

## Gestaltungsregel
Je länger eine Fachseite, desto häufiger verdichtet sie das Wesentliche in zusammenfassenden Nucleus-Karten mit einem zentralen Zusammenhang, Teilkernen, expliziten Abhängigkeiten und Rückverweisen. Pastellflächen bedeuten Zusammengehörigkeit, nicht Evidenzstatus. Nucleus-Übersichten stehen an semantisch sinnvollen Übergängen und am unteren Ende längerer Abschnitte – nicht als künstliche Dekoration.

## Komponenten
- `tensor-nucleus`: zusammenhängender Kern mit optionalem fachlichem Farbton, responsive Teilkerne.
- `tensor-gloss`: Tastatur- und Hover-Kurzdefinition mit permanentem Link `glossar.html#ID`.
- `tensor-artifact`: aufbereitete CSV-Vorschau oder quellengenaues Codebeispiel mit Original-Link, Lesehilfe und horizontalem Überlauf.
- `tensor-output`: tatsächliches Ergebnis mit Geltungsbereich, Testnummer und Quellenlink.
- `glossar.html`: erster Index der Codebuch- und Glossarbegriffe, mit ausdrücklichem Hinweis auf den unvollständigen historischen Import.

## Tatsächlich integrierte Seiten
- `docs/harvesting.html`: Ernte-Nucleus, Ergebnis-/CSV-Vorschau, auditierter Output.
- `docs/minimal-ki.html`: vier Grundfunktionen als Nuclei, Codeausschnitt aus Geo-KI, geprüfter Testoutput.
- `docs/tensor-einfuehrung.html`: 3×3×3-Kernübersicht zusätzlich zum Donut.
- `docs/bibliothek.html`: Quellen/Glossar/Codebuch als Rahmen und Navigationskern.
- `docs/glossar.html`: neuer kuratierter Web-Index mit zwölf Kurzdefinitionen.

## Wissenschaftliche Integrität
Die 12 Webdefinitionen sind **neu redaktionell formuliert**. Sie sind nicht identisch mit oder Ersatz für 1.072 Glossareinträge des qualitätsannotierten historischen Archivs v15.4. Keine fiktiven Quellenanker für die noch nicht auf Git importierten Glossarbegriffe. CSV-Tabellen auf der Site zeigen belegte historische Ergebniszahlen; sie geben nicht vor, eine vorhandene Original-CSV 1:1 darzustellen. Der Codebeispiel-Link führt zum gesicherten Python-Original im Git-Repository.

## Weiter offen
1. Vollständigen Import der 1.072 historischen Begriffe mit Herkunft, Version, Quellen und Definitionen abnehmen.
2. Eigenes, quellengenaues maschinenlesbares Codebuch und begriffsbezogene Feld-IDs bereitstellen.
3. Weitere geeignete Seiten nach Inhaltsanalyse mit Nuclei und 1–2 aussagekräftigen Diagrammen ausstatten.
4. Tooltip-Verhalten im Browser auf Mobile, Tastatur und Screenreader prüfen; bei Bedarf echte Button-/Popover-Komponente ergänzen.
5. Einbindung echter CSV-Artefakte mit Datensatzdownload und Tabellenfilter statt nur Auszügen.
6. Auto-Prüfungen für Glossar-Linkziele, Bildalternativen, Code-Lizenzen und unbelegte Outputs.

## Abnahmestand
Alle acht relevanten Git-Dateien vom Connector aus lesbar; vier geänderte Fachseiten enthalten Nucleus-Styling, drei davon Kontextglossare; Glossar-Kernindex enthält 12 Datensätze. Ein visueller Browsertest wurde noch nicht durchgeführt.
