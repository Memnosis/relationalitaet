# Mitmachen – Integrations- und Abnahmebericht v1 · 2026-11-01

## Umgesetzt
- Eigene Seite `docs/mitmachen.html` mit relationaler Einführung, Didaktik für **alle sechs Bereiche**, Taskkarten, vollständigen Meta-Prompts, kopierbaren URLs, GitHub-Issue-Übergaben und ausführlichem Harvesting-Forschungs-/Aufgabenabschnitt.
- `forschung/website/MITMACH_TASKS.json` enthält **13 zusätzliche Aufgaben** inklusive WEB-GLOS-01 und WEB-CODE-01, sechs Harvesting-Tasks und Fachbeispielen. Das bestehende 18er-Minimal-KI-Taskregister bleibt erhalten; keine Doppelzählung oder Zusammenführung als 31 wissenschaftlich abgenommene Tasks.
- Rote `Mitmachen`-Taste auf **13/13 HTML-Seiten** in `docs` und zusätzlich auf `dashboard/index.html`. Rotes Design ausschließlich für Mitarbeit, keine Umcodierung von Fachfarben.
- Im Zwölfer-Web-Kurzglossar: Links zum zuständigen Integrations-Task auf jeder Begriffskarte. Kontext-Hover ergänzend mit Link zur Aufgabenkarte.
- Forschungsbibliothek, Übergabeportal und Harvestingseite mit direkten Mitmach-Verweisen.
- Promptquellen verweisen auf nachweisbare Git-Dateien/Reports; historische Original-ZIP-Dateien werden nicht fälschlich als öffentliche Downloads bezeichnet.

## Datenprüfung
- 13 GitHub-Pages HTML-Dateien: alle mit rotem Stylesheet und Mitmachen-Zugang, keine verbotene interne Bezeichnung in den geprüften HTML-Dateien.
- 13 neue Task-IDs, sechs Fachbereiche, alle Prompts mit ausgeschriebenen URLs.
- Integrationstasks `WEB-GLOS-01` und `WEB-CODE-01` sind dokumentiert.
- Die historischen 1.072 Glossarbegriffe sind **nicht** vollständig publiziert; momentan zwölf redaktionelle Kurzdefinitionen.
- 106 historische PM-Tasks sind **noch nicht** über einen ID-Crosswalk an der öffentlichen Mitmachen-Übersicht.
- Funktionsprüfung im Live-Browser, JS-Kopieren, Issues und Tastatur/Touch: **noch nicht durchgeführt**.

## Öffentliche Fundstellen
- https://memnosis.github.io/relationalitaet/mitmachen.html
- https://memnosis.github.io/relationalitaet/mitmachen.html#WEB-GLOS-01
- https://memnosis.github.io/relationalitaet/mitmachen.html#WEB-CODE-01
- https://memnosis.github.io/relationalitaet/mitmachen.html#HARV-01
- https://memnosis.github.io/relationalitaet/glossar.html
- https://memnosis.github.io/relationalitaet/harvesting.html
- https://memnosis.github.io/relationalitaet/taskkarten.html

## Nächste fachliche Abnahmen
1. Originalarchiv-Import und Belegprüfung für alle 1.072 Glossareinträge sowie historisches Codebuch; stabile Objekt-IDs mit fachlichen Gegenproben.
2. Crosswalk der 106 historischen PM-Aufgaben gegen bestehende 18 plus 13 Aufgaben auf Git.
3. Dynamische Taskkarten im Browser bedienen, Mitmach-Link prüfen, Glossar-Hover und Tastatur prüfen.
4. Die komplette Erntepipeline und weiteren Bibliotheken/Sprachen systematisch testen, ohne validierte Ergebnisse vorzutäuschen.
