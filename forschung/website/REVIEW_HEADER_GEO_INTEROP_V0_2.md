# Website-Upgrade: Navigation, Bildgestaltung, Geo-KI und Interoperabilität
**Stand:** 2026-11-01 · **Version:** v0.2

## Gegenprüfung gegen die letzten Wünsche
1. **Hauptnavigation:** alle 16 geprüften Website-Seiten verwenden einen gemeinsamen schwarzen Header, dasselbe kleine weiße Tensor-Signet und dieselben Kernlinks; ausführbare Datei `docs/assets/tensor-navigation.css`.
2. **Mitmachen im Posterdesign:** Überarbeiteter burgunderfarbener Hero, sechs Pastell-Fachbereichskarten mit eigenen SVG-Icons, rote Mitmach-Einladungen. Die auf `body.join-page` begrenzte Gesamtgestaltung wird nicht auf Fachseiten übertragen.
3. **Geo-KI-Meilenstein:** `GEO-M1`: Generieren → Komponieren → Prüfen → Exportieren. Vollständiger Meta-Prompt samt Quellen, Eingaben, Operatoren, Rückprüfung, Negativtests, DoD und No-Loss-Rückgabe.
4. **Format- und Standardharvesting:** acht interoperable Forschungsfamilien, mehr als vier Geometriebibliotheken, Formate vom 2D-Pfad bis zum Forschungsdatensatz. Register und wissenschaftlich-technisches Paper verlinkt; sechs weitere Aufgaben als Ausgangsprompts.
5. **Tensor-Paper:** Original Logik-Tensor DOI https://doi.org/10.5281/zenodo.19282895 ist verlinkt. Neue `docs/tensor-paper.html` führt die drei beschrifteten 3×3-Matrizen und spätere Prüfstände vor. Der bisher längere interne Paper-Entwurf wurde noch nicht byteidentisch auf Git übertragen: die Git-Publikation ist ausdrücklich eine redaktionelle Auszugfassung.
6. **Links, Bilder, Diagramme:** SVG-Icons auf Mitmachen; separate Medienbibliothek und Diagramm-SVGs bleiben in `docs/medien.html`.

## Audit
- **16/16** geprüfte HTML-Seiten: gemeinsamer Header, CSS-Einbindung, genau eine H1 und keine fehlenden lokalen statischen Linkziele unter den bekannten Repository-Pfaden.
- Keine verbotenen Altformulierungen in den 16 geprüften Seiten.
- Live-Browser, mobile Gestaltung, Tastaturnavigation, Grafikpositionen und Clipboard nach Deployment sind **nicht** automatisiert getestet.
- API/Format-Adapter sind noch nicht eingebaut: das Papier beschreibt Forschungs- und Implementierungskandidaten.
- Historischer PM-Crosswalk von 106 Aufgaben bleibt offen.

## Fundstellen
- https://memnosis.github.io/relationalitaet/mitmachen.html
- https://memnosis.github.io/relationalitaet/interoperabilitaet.html
- https://memnosis.github.io/relationalitaet/tensor-paper.html
- https://memnosis.github.io/relationalitaet/geoki.html
- https://github.com/Memnosis/relationalitaet/blob/main/forschung/website/GEOKI_INTEROP_MEILENSTEINE.json
- https://github.com/Memnosis/relationalitaet/blob/main/forschung/interop/FORMAT_SKILLS_REGISTER_V0_1.json
- https://github.com/Memnosis/relationalitaet/blob/main/forschung/interop/PAPER_INTEROPERABILITAET_SKILLS_V0_1.md
