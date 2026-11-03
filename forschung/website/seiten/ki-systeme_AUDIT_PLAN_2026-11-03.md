# Seiten-Audit und nächster Upgradeplan: KI-Systeme

**Website:** [`docs/ki-systeme.html`](../../../docs/ki-systeme.html) · **Priorität:** P0 · **Stand:** 2026-11-03 · **GPT-Owner:** HTML, Inhalte, Links und CSS · **Claude-Peer:** Quellen, Tests, Status.

## Ausgangsstand – tatsächlich übernommen
Historische KI-Entwicklung und Methodenvergleich; Anschluss an Mini-KI und Logik. Die Seite wurde aus dem bereits existierenden Integrationszweig `integration/soulution-shared-core-2026-11-03` selektiv in `main` übernommen. Die frühere `site-nav.js` wurde auf die bestehende, vom Autor bestätigte siebenpunktige Navigation `tensor-hierarchy.js` umgestellt; die branch-originäre Originalstruktur blieb ansonsten bewahrt.

## Didaktische und fachliche Lücke
Zwei parallele Einführungen ki-geschichte/ki-systeme: überlappende Erzählungen müssen mit Crosslinks, Quellen und didaktischer Rollenklärung statt Ersetzung verbunden werden.

## Konkrete nächste Umsetzung
1. **P0 Bestand:** aktuelle Git-Blob-SHA, Originalanker, Texte, Links, Bilder und Source-JSON prüfen; kein Blindmerge/kein Verlust.
2. **Didaktik:** Prüfen, ob vorhandene Seiten Begriffe, Architekturklassen und Vergleichsbasis sauber abgrenzen; externes Promptbibliothek-Register NICHT importieren.
3. **Evidenz:** E1 Bedeutung/Begriffe, E2 Alternativen und historische Entwicklung, E3 belegte fachliche Aussagen/Test/Gegenprobe trennen; veröffentlichte und rekonstruierte Aussagen kennzeichnen.
4. **Gegentest:** GPT prüft Website/Desktop/Navigation; Claude prüft Ursprung, Bedeutung, Quellenstatus, Version/Lizenz und negative Befunde.
5. **Freigabe:** nur nach tatsächlich belegten Abnahmeschritten; alte PDF/Buchoriginale und nicht freigegebene Rohprompts unverändert belassen.

**Status:** Webdatei vorhanden; selektive Integration ausgeführt; Quellen-/Browser-/Fach-Gegenreview noch ausstehend. **Planreferenz:** [Upgradeprogramm 100+](../UPGRADE_100PLUS_PROMPTARCHITEKTUR_2026-11-03.md) · [alte 25-Seiten-Audits](README.md).