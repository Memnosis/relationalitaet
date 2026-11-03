# Website-Upgrade R2 · Projektmanagement, Promptprüfungen und sichere Zusammenarbeit
**Stand:** 2026-11-03 · **Owner:** GPT Website · **Fach-/Datengegenprüfung Claude:** weitere Rückbestätigung offen · **Zyklus:** 001 nicht vollständig abgeschlossen.

## 1. Tatsächlich umgesetzte Website-Aufgaben
| Element | Aktive Datei | Verifizierter Stand |
|---|---|---|
| Öffentliche Aufgabenkarte | `docs/data/projektmanagement-public-v2.json` | 7 Website-/Gemeinschaftskarten, 6 Claude-interne Aufgaben nur als Aggregat; aus ursprünglichem 13er-Snapshot abgeleitet, noch **kein fachlich kanonischer automatischer Generator** |
| Website-Dashboard | `docs/projektmanagement.html`, `docs/assets/projektmanagement.js` | R6-Sichtquelle v2 aktiv, GPT/Claude-Wahl und Filter erhalten, keine internen Claude-Einzelkarten mehr |
| Gesamte Promptarchitektur | `docs/data/workflow-stand-v1.json`, `docs/assets/workflow-stand.js` | 82 **eindeutige IDs** aus 102 dokumentierten Vorkommen; 20 identische Dubletten, über `forschung/register/PROMPT_CROSSWALK_V0_1.json` verankert |
| Stufen der Promptprüfung | `docs/projektmanagement.html#prompt-workflow` | Konkrete R4-Stufen und der Unterschied zwischen bloßer Demonstration, unabhängiger Gegenprüfung, Vergleich und Autorenfreigabe erklärt |
| Tests/CI | `scripts/validate_pm_public_v2.py`, `scripts/validate_workflow_v2.py`, `.github/workflows/projektmanagement-check.yml` | automatische **statische** Prüfungen definiert (JSON/Referenzen/Reviewkapazität/JS-Syntax); erfolgreicher GitHub-Actions-Lauf und Desktop-Browserabnahme in dieser Sitzung **nicht nachgewiesen** |
| Reziproke Zusammenarbeit | `REGELN_ZUSAMMENARBEIT_V2_ENTWURF.md` und `GPT_DISKUSSION_06.md` | R1–R6 beiderseits dokumentiert, mit expliziten Bedingungen für unabhängige Tests, sichere öffentliche Lesesichten und max. drei offene Prüfbitten |

## 2. Wiederaufgenommene, vorher liegengebliebene Prüfbitten
- `GPT_ANTWORT.md`: Claudes S1–S3 **schriftlich** teilweise fachlich gegengeprüft, echte Reproduktion sämtlicher Tests ausstehend; `gpt_reviewed=false` im Zyklus bleibt daher bewusst.
- `GPT_LOGIK_PROMPT_02_UNABHAENGIGER_TEST.md` plus `scripts/gpt_logic02_independent.py`: eigener lokaler MP-/Gegenmodelltest exit 0; Claudes `CLAUDE_R4_VERGLEICH_LOGIK-PROMPT-02.md` bestätigt in diesem **begrenzten Umfang** Übereinstimmung. **Vollständigkeit des Hilbert-Kalküls und G3-Vergleich** nicht eigenständig aus GPTs vier Belegungen reproduziert. Keine vollständige Promptfreigabe.
- Diskussion 04 unter vollständigem korrekten Pfad `CLAUDE_DISKUSSION_04_PUBLIKATIONEN.md` gefunden und mit `GPT_DISKUSSION_04.md` schriftlich beantwortet.
- `GPT_DISKUSSION_07.md` bestätigt die erreichten R4-Grenzen und nimmt den neuen 82-ID-/102-Vorkommen-Crosswalk an.
- `REVIEW_QUEUE_V2.json` hält neue offene Reviewbitten unter der Drei-Anfragen-Grenze und trennt beantwortet von gegenseitig akzeptiert.

## 3. Nächste GPT-Website-Reihenfolge (nach den laufenden P0-Gegenprüfungen)
**W-P0-01: Echte Desktop-/JS-Abnahme des Projektmanagements.**
- Prüfe im Browser die Serverauslieferung von HTML/JS/JSON, Umschaltung `GPT/Claude/Beide`, Links, dynamische Statusgruppen und Ausfallmeldungen.
- Kontrolliere, dass `Claude` keine einzelnen internen Aufgaben rendert, sondern nur den Aggregattext. Ein alter öffentliches JSON im Git-Repository bleibt jedoch historisch erreichbar.
- Bestehen der statischen JSON-/JS-Syntaxprüfung ersetzt diesen Browserlauf nicht.

**W-P0-02: Claude-generiertes Kanonregister `pm-public-curated/0.2` integrieren.**
- Claude erzeugt Status aus wirklichen Claim-/Test-/Commitakten einschließlich Negativfällen und `evidence_commit`; GPT validiert Quellversion, JSON Schema, Release, Links/Flags und integriert diffbasiert in v2.
- Solange diese Übergabe fehlt, sind die 7/6-Stände ein explizit **provisorischer Snapshot**.

**W-P0-03: Siebenpunktige Hauptnavigation verlustfrei zusammenführen.**
- Bestehender Autorenentscheid DEC-NAV-01=b. Beide Skript-/Navigationsvarianten, 16 Konfliktseiten, geschützte Anker, alle Buch-/Grafikverweise vor Migration inventarisieren.
- Nur geprüfte additive Integration; nach Merge Navigation, Links, Fachfarben und Start-/Mitmachenpfad neu testen.

**W-P1-01: Inkubator differenziert fusionieren.** Menschen-/KI-Mitwirkung, Open-Source-Reengineering, Bibliotheken/Skills und wissenschaftliche Tests als erkennbare Bereiche, nicht als beliebig vermischte Liste.

**W-P1-02: Wissenschaftliche Fachkarten aus freigegebenen Claims.** Logik, Tensor/Feld, Geo-KI, Mini-KI, SOULution und Buchverweise aus geprüften Quellen-/Evidenzdaten; unveröffentlichte Buchversionen nicht als fertige Bücher ausgeben.

## 4. Nächste Claude-Reihenfolge
**D-P0-01:** Eigene DATA-Abnahme und gemeinsamer Zyklus-001-Review fortführen, R4-v2-Probe mit vollständig spezifiziertem Kalkül.  
**D-P0-02:** 82 eindeutige Prompts, 102 Vorkommen, 20 identische Duplikate und 15 separat bezeichnete Folgeverfahren mit Freigabe-/Teststatus im Nachweisregister verbinden.  
**D-P0-03:** Belegbasierten PM-Generator und `web-lesesicht/0.2` fachlich validieren; interne Einzelpositionen schützen; autorisierte Web-Projektion mit SHA liefern.  
**D-P1-01:** Fehlende Tensor-2.0-/historische Archive, Thesen-/Glossar-/Feldbelege und ein Werk-Upgradeplan pro Originalpublikation; private Gesamtkorpora nicht nach öffentliches `main`.

## 5. Workflow-Schnittstelle und Verantwortung
`Claude Quelle/Tests → public-safe Generator (Version/SHA) → GPT Schema-/Regressionstest → Website → unabhängiger Claude-Fachreview → ggf. Nils' Freigabe`.

**Review-Sperre R5:** maximal drei offene Prüfbitten an die andere KI; Antworten auf vorhandene Prüfbitten vor neuem Arbeitsauftrag. **Bericht R2:** ein DOCX an Nils im Wechsel der Berichtserstellung (Bericht 04 Claude, Bericht 05 GPT), von beiden geprüft. Kein vorzeitiger gemeinsamer Bericht ohne Gegenlesung.

## 6. Begrenzung und Risikohinweis
- Der freie Container konnte GitHub nicht direkt klonen (DNS-Auflösung fehlgeschlagen), deshalb ist `forschung/register/reproduzieren.py` (7/7) in der GPT-Umgebung nicht als eigener Lauf bestätigt. Die lokale LOGIK-PROMPT-02-Gegenprobe ist tatsächlich ausgeführt; das ist eine andere Prüfspur.
- Die frühere `docs/data/projektmanagement-v1.json` bleibt in Git erhalten und die öffentliche Historie ist nicht privat. Keine eigenmächtige destruktive Bereinigung ohne private Sicherung und Autorenfreigabe.
- Source-Counts der Website sind kein Beweis vollständiger Praxisprüfung; die vollständige neue Promptbibliothek liegt teilweise in einem Integrationszweig.
