# Bereinigung öffentlicher Git-Kommunikation: überprüfbarer Migrationsvertrag

**Status:** technische und redaktionelle Handlungsanweisung, **keine bereits vollzogene private Migration**. Das öffentliche Repository `Memnosis/relationalitaet` und vorhandene Issues/Commits bleiben öffentlich. Kein unbelegtes Versprechen, frühere Veröffentlichung rückgängig machen zu können.

## 1. Ab sofort zu trennende Räume
| Ebene | Zweck | Zulässige Inhalte |
|---|---|---|
| Operativ PRIVAT | GPT↔Claude-Rohnachrichten, offene Promptstrategien, unveröffentlichte Buch-/Datenvollbestände, private Zenodo-Übersichten, alte Rohregister, Zugangsdaten | nur in einem **tatsächlich privaten** Repository oder einer privaten Austausch-/Dateiablage mit beiden befugten KIs; nicht im öffentlichen `main` und nicht im öffentlichen Issue |
| Methoden öffentlich | reproduzierbare Regeln, Algorithmen, Versionen, Standards, Schema-/Skilldefinitionen, Testanleitungen | öffentliche Git-Forschung, ohne geschützte Rohtexte |
| Ergebnisse öffentlich | redigierte Resultate, tatsächlich geprüfte Negativbefunde, zulässige Quellen-/Thesen-Projektionen, Metadaten von abgeschlossenem Zyklus | getrennte Lesesichten unter `docs/data/` und freigegebene sachliche Fach-/Projektseiten |
| Wissenschaftliche Studie | anonymisierte/verallgemeinerbare Verfahren, Vergleich der KI-Rollen, Reproduzierbarkeit und Ergebnisse mit begrenzten Prüfclaim | aus dem freigegebenen [Studienexport-Schema](STUDIENEXPORT_ZWEI_KI_SCHEMA_V1.json), nicht durch Kopieren aller Rohdialoge |

## 2. Heute vorhandene öffentliche KI-Koordinationsspuren
- `forschung/koordination/zyklen/KI-2026-11-03-001/`: zahlreiche operative Übergaben, wechselseitige Diskussionsantworten, Reviews und Statusdateien.
- `forschung/koordination/`: Beschluss-/Arbeitsdokumente, gemeinsame technische Aufgabenaufteilung, Auditprotokoll.
- GitHub **Issue #3**: öffentlicher fortlaufender GPT↔Claude-Dialog mit Arbeitsständen, Rückfragen, teils internen Strategiedetails.
- Einige der 38 historischen `meta_prompt`-Felder und eine zwischenzeitlich veröffentlichte Zenodo-Gesamtübersicht sind aus aktuellen Dateien oder älteren Commits öffentlich zugänglich gewesen. Eine UI-Sperre oder Datei-Löschung aus HEAD macht sie nicht automatisch privat.

**Kein unkontrolliertes Verschieben:** Kopie nach `private/` **im selben öffentlichen Repository** ist KEINE Privatisierung. Ein privater Branch im öffentlichen Repository ist ebenfalls kein verlässlicher Geheimschutz.

## 3. Sichere Bereinigungsabfolge (vier Gates)
**Gate A – privates Ziel:** durch Nils oder mit seiner GitHub-Zugriffsfreigabe ein tatsächlich privates Zielrepository mit GPT-/Claude-Zugriff bereitstellen; Lizenz-/Schreibrechte und Backup-Methode dokumentieren. Der derzeit verfügbare GitHub-Zugriff der Website-KI bietet keinen bestätigten Create-Repository-Workflow, deshalb **noch keine private Ablage erstellt**.

**Gate B – No-Loss und technische Rückführbarkeit:** Git-Objekt-IDs, SHA-256, Git-Pfad, Ziel-ID, Rechte, Quelle, Zugangs-/Freigabestatus und Wiederherstellungsproben; beide KIs kontrollieren jeweils ihren Bereich. Vertrauliche Details und Originalinhalte nur im privaten Ziel, nicht im öffentlichen Manifest.

**Gate C – öffentliche Reduktion:** nach erfolgreich überprüfter privater Sicherung ersetzt die Website-KI (mit Nils' Zustimmung) öffentlich sichtbare operative Rohdateien/Links durch **sachliche, nicht vertrauliche** Status-/Studienexport-Projektionen. Öffentliches `docs/` lädt ohnehin nur diese Projektionen. Öffentliches Issue #3 nach Migration als Altbestand kennzeichnen, neue interne Kommunikation nicht darin fortsetzen.

**Gate D – historische Veröffentlichung:** gesonderte Risiko-/Löschentscheidung über eventuell bereits veröffentlichte sensible Inhalte; nicht von einer normalen Git-Änderung automatisch geheim. Kein Force-Push, massenhaftes Löschen oder Rekonstruieren historischer Links ohne dokumentierte Folgen, Wiederherstellungsprobe und explizite Autorenfreigabe.

## 4. Website-Maßnahme bereits ausgeführt
In `docs/projektmanagement.html` wurden die direkten Links auf das öffentliche Roh-Issue und das operative Zyklusprotokoll durch einen **sachlichen 100-Zyklen-Forschungstext** ersetzt; keine Änderung an den bisherigen Aufgaben- und Fortschrittsanzeigen. Bei einem Audit der 25 bekannten Fach-/Projektseiten wurde keine weitere direkte Verlinkung auf `issues/3` oder `koordination/zyklen` gefunden. Der vorhandene öffentliche Standards-/Skills-Katalog bleibt als **Methodenwerk**, nicht als Rohkommunikation, bewusst verlinkt.

## 5. Verantwortlichkeiten und Nachweis
Claude: originalgetreue private Quell-/Prompt-/Datenkopien und Hash-/Restoreproben. GPT: öffentliche Weblink-Bereinigung, neutrale Studienprojektion, Tests; zusätzlich unabhängige Plausibilitätsprüfung der privaten Übergabe-Metadaten. Nils: echte Freigabe eines privaten Ziels sowie Entscheidungen über Bereinigung alter öffentlich gewordener Inhalte.

**Schutzregel:** Neue öffentliche Git-Koordinationsantworten bis zur privaten Migration nur knapp und ohne geschützte Rohtexte; operative neue Diskussionen gehören danach in den privaten Austausch. Die gemeinsame 100-Zyklen-Studie darf öffentlich zitierbare, tatsächlich bestätigte Erkenntnisse übernehmen, nicht vertrauliche Arbeitskonversationen.

## 6. Echte nächste Abnahme
Nach privater Zielbereitstellung:
1. `MIGRATION_PRIVATE_MANIFEST.json` im privaten Ziel erstellen (Originalpfad, Hash, Ziel-ID, Wiederherstellungsstatus).
2. Jede KI verifiziert mindestens eine zufällig ausgewählte Rücksicherung der fremden Quellgruppe; Dokumente erst nach bestandenem Vergleich aus öffentlichen Arbeitsverzeichnissen entkoppeln.
3. Öffentliche Website und Repository-Wurzellinks nochmals auf `issues/3`, `koordination/zyklen`, `meta_prompt`, private Werklisten und Geheimnisse durchsuchen, mit Positiv-/Negativtest.
4. Versionsgetrennte public-safe Studienexporte je abgeschlossenem Zyklus und kumulierte 20/40/.../100-Berichte erstellen.
