# Seiten-Audit und nächster Upgradeplan: Codebuch-Webindex

**Website:** [`docs/codebuch.html`](../../../docs/codebuch.html) · **Priorität:** P0 · **Stand:** 2026-11-03 · **GPT-Owner:** HTML, Inhalte, Links und CSS · **Claude-Peer:** Quellen, Tests, Status.

## Ausgangsstand – tatsächlich übernommen
Kompakter typisierter Webindex mit 12 Begriffsknoten aus Integrationszweig. Die Seite wurde aus dem bereits existierenden Integrationszweig `integration/soulution-shared-core-2026-11-03` selektiv in `main` übernommen. Die frühere `site-nav.js` wurde auf die bestehende, vom Autor bestätigte siebenpunktige Navigation `tensor-hierarchy.js` umgestellt; die branch-originäre Originalstruktur blieb ansonsten bewahrt.

## Didaktische und fachliche Lücke
Der 12er-Webindex ist nicht das historische Glossar mit 1.072 Einträgen; live Datenschema/Filter und Lesestatus noch nicht browsergeprüft.

## Konkrete nächste Umsetzung
1. **P0 Bestand:** aktuelle Git-Blob-SHA, Originalanker, Texte, Links, Bilder und Source-JSON prüfen; kein Blindmerge/kein Verlust.
2. **Didaktik:** Quellen-Versionsstatus an Claudes Glossar-Crosswalk anbinden, keine falsche Vollständigkeit.
3. **Evidenz:** E1 Bedeutung/Begriffe, E2 Alternativen und historische Entwicklung, E3 belegte fachliche Aussagen/Test/Gegenprobe trennen; veröffentlichte und rekonstruierte Aussagen kennzeichnen.
4. **Gegentest:** GPT prüft Website/Desktop/Navigation; Claude prüft Ursprung, Bedeutung, Quellenstatus, Version/Lizenz und negative Befunde.
5. **Freigabe:** nur nach tatsächlich belegten Abnahmeschritten; alte PDF/Buchoriginale und nicht freigegebene Rohprompts unverändert belassen.

**Status:** Webdatei vorhanden; selektive Integration ausgeführt; Quellen-/Browser-/Fach-Gegenreview noch ausstehend. **Planreferenz:** [Upgradeprogramm 100+](../UPGRADE_100PLUS_PROMPTARCHITEKTUR_2026-11-03.md) · [alte 25-Seiten-Audits](README.md).