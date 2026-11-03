# Gesamtprojekt · kombinierte Forschungsregister

Stand 2026-11-03. Dieses Verzeichnis ist ein **neuer kombinierter Index**; keine vorgetäuschte vollständige Übernahme der historischen Originalbestände.

## Vorhandener maschinenlesbarer Einstieg

[GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json](GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json) verbindet **24 unterschiedliche Aufgaben-IDs** aus drei Kategorien:

| Herkunft | Datensätze | Sicherheits-/Evidenzstatus |
|---|---:|---|
| Bereits in GitHub strukturierte Geo-KI-/Interop-Aufgaben | 7 | Aufgaben und vorbereitete Meta-Prompts, keine behauptete Abnahme |
| Bereits in GitHub beschriebene SOULution-Module | 6 | Planungs-/Prüfaufgaben, keine ausgeführte Simulation |
| Neu abgeleitete historische Rekonstruktionsaufträge | 11 | Nur Inventar- und Prüfaufträge; historische Einzeldaten müssen noch importiert oder rekonstruiert werden |

Die Summen 309 Trinitäten, 103 Tensorgrundgerüste, 1.017 Relationsaussagen, 7.622 Formeln, 1.072 Glossarbegriffe und 3.203 Atlas-Nodes sind **historische Mengenangaben**, nicht 13.000 fertig integrierte Datensätze. Keine nicht belegten Feldinhalte wurden erzeugt.

## Kombinationsprinzip

1. Originale niemals überschreiben; historische Versionen mit Hash, Originalpfad und Herkunft führen.
2. Einheitliche stabile IDs und Relationen verweisen auf Quellen, Fachbegriffe, mathematische Modelle, Skills, APIs, Tests, Ergebnisse und Publikationen.
3. Unterscheidung **Original**, **aus vorhandenem GitHub-Objekt extrahiert**, **rekonstruiert**, **Hypothese** und **ungeprüft**.
4. Ein Prompt hat Einstiegstiefe (Seitenfrage, Mitmachen, Forschungsinfrastruktur), Funktionsebene (Prompt, Agent, Meta) und Freigabestatus.
5. Jede öffentliche Mitmach-Aufgabe benötigt dokumentierten Probelauf, Prüfprotokoll und redaktionelle Freigabe.
6. Exporte und externe Rückgaben müssen Referenzen auf Glossar-/Quellen-/Versionstände tragen. Neue Ergebnisse werden nicht ungeprüft als Evidenz übernommen.

## Fortsetzung — Priorität

- Audit des historischen Branches `ki-tensor/no-loss-audit-2026-10-31` und der vorhandenen Archive mit Inhalts- und Versionscrosswalk.
- Vorhandene komplette Codebuch-/Glossar-/Formel-/Atlas-Datensätze in ihre jeweiligen Register importieren; bisherige Kennzahlen nicht als Inhalt ausgeben.
- Schemas, Validator, Duplikat-/Referenzprüfung und Ereignisnachzug implementieren.
- Pilot Tensoralgebra: mathematischer Rechentest, Gegenbeispiel, Quellenanbindung, geprüfter Prompt und öffentliche Freigabe.
- Website-Ansichten daraus generieren und vollständigen Browser-/Navigationstest durchführen.

Verknüpft: [Upgrade 100+](../website/UPGRADE_100PLUS_PROMPTARCHITEKTUR_2026-11-03.md), [Geo-KI-Aufgaben](../website/GEOKI_INTEROP_MEILENSTEINE.json), [SOULution-Forschungsmodule](../soulution/FIN_DEM_ROOM_FORSCHUNGSMODULE_V4.md).


## GPT-Altbestand in diesem Ordner (gekennzeichnet 04.11.2026)

Am Vormittag des 03.11.2026, vor der endgültigen Rollenteilung, hat GPT einige Dateien in diesem Ordner angelegt (Commits `3f08e8f`, `36fd709`, `7bf298e`, `66082b8`, `badfe60`), unter anderem `GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json` (44 Aufgabenfamilien) sowie Import- und Testnachzugsberichte.
- Sie bleiben unverändert erhalten (no-loss).
- Owner ist ab jetzt Claude; Änderungen daran laufen über Claude.
- Ihre Zahlen stehen mit Herkunft in `BESTANDSZAHLEN_V0_1.json`.
- Fachliche Einstufungen darin (z. B. Evidenzgrade E0–E4 für Thesen) gelten als **Vorschlag GPT**, bis Claude sie gegen das Vokabular (`schema/vokabular.json`) geprüft hat.
