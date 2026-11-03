---
agent: claude
document: standards_analyse
status: vorschlag_gegenlesung_gpt_ausstehend
updated_at: 2026-11-03
auftrag: "es gibt Standards für gute Kommunikation und Austausch wie hier von 2 KI-Systemen – analysiere, was zu uns passt" (Nils, 03.11.2026)
---

# Standards für den Austausch zweier KI-Systeme: was zu uns passt

**Unsere Lage:** zwei KIs mit getrennten Bereichen (Claude: Daten, Forschung, Prompts; GPT: Website). Ein Mensch entscheidet (Nils).
- **Kanal:** Git-Dateien und ein Issue. Es gibt keinen gemeinsamen Live-Kanal.
- **Taktung:** asynchron, mit sehr unterschiedlichem Tempo (GPT am 03.11. rund 60 Schritte in 2 h).
- **Bisherige Probleme:**
  - gekreuzte Nachrichten (Anfrage nach etwas schon Geliefertem)
  - Test-PASS für einen anderen Stand als den committeten
  - lange Strecken ohne Gegenprüfung
  - Entscheidungen verteilt über viele Dateien

**Bewertung:** Passung (hoch/mittel/gering) × Aufwand (klein/mittel/groß). Übernommen wird nur, was zu Git als Kanal passt.

## Übersicht

| Standard | Herkunft | Kernidee | Passung | Aufwand | Empfehlung |
|---|---|---|---|---|---|
| **FIPA ACL** – Sprechakte (*performatives*) | IEEE FIPA, 2002 | Jede Nachricht hat einen Typ (anfragen, informieren, zusagen, ablehnen, vorschlagen, bestätigen, widersprechen, nicht verstanden) und `in-reply-to`, `conversation-id`, `reply-by` | **hoch** | klein | **übernehmen, als Kopfzeilen** |
| **A2A** (Agent2Agent) – Aufgabenzustände, Agent Card | Google, 2025, jetzt Linux Foundation | Aufgabenzustände `submitted → working → input-required → completed / failed / rejected / canceled`; jede KI beschreibt ihre Fähigkeiten in einer „Agent Card“ | **hoch** (Vokabular), gering (HTTP-Protokoll) | klein | **Zustände und Agent Card übernehmen**, Protokoll nicht |
| **ADR / MADR** (Architecture Decision Records) | Nygard 2011; MADR 3.0 | Jede Entscheidung als eigene Datei: Kontext, Optionen, Entscheidung, Folgen, Status (vorgeschlagen / angenommen / ersetzt) | **hoch** (= unser R3) | klein | **übernehmen** für Entscheidungen von Nils |
| **ACM Artifact Badges** | ACM, 2020 | Stufen: *Available → Functional → Reusable → Results Reproduced* (andere Partei, gleiche Artefakte) *→ Results Replicated* (andere Partei, unabhängige Umsetzung) | **sehr hoch** | klein | **übernehmen** als Prüfstufen für Gegenrechnung |
| **W3C PROV-O** | W3C, 2013 | Herkunft: Entität, Aktivität, Agent (`wasGeneratedBy`, `wasAttributedTo`, `wasDerivedFrom`) | hoch (schon im Profilprüfer) | klein | Commit-Trailer aus R8 auf PROV abbilden |
| **CRediT** (Contributor Roles, ANSI/NISO Z39.104-2022) | NISO | 14 Beitragsrollen (Konzept, Software, Validierung, Datenkuratierung …) | hoch für Publikationen | klein | KI-Beiträge in Werken nach CRediT ausweisen, **nicht** als Autorschaft (COPE: KI ist kein Autor) |
| **RFC 2119 / 8174** | IETF | MUSS / SOLL / KANN mit fester Bedeutung | mittel | klein | Regeltexte v3 damit schärfen |
| **Conventional Commits 1.0** + Git-Trailer | Community | `typ(bereich): betreff` + Trailer | hoch (GPT nutzt es schon: `web:`, `ci:`, `audit:`) | klein | Typen vereinheitlichen; Trailer nach R8 |
| **SemVer 2.0** | Community | Version MAJOR.MINOR.PATCH | hoch (schon im Profilprüfer) | — | beibehalten |
| **Vier-Augen-Prinzip, Blindprüfung** | GCP/GLP, Peer Review | Prüfer sieht das Ergebnis nicht vor der eigenen Prüfung | hoch (= unser R4) | — | beibehalten |
| CloudEvents 1.0 | CNCF | einheitlicher Ereignis-Umschlag (id, source, type, time) | gering | mittel | **nicht jetzt**: zu viel Technik für den Git-Kanal |
| MCP (Model Context Protocol) | Anthropic, 2024 | Werkzeug- und Kontextanbindung eines Modells | gering | — | **nicht passend**: kein Protokoll zwischen KIs |
| A2A als HTTP/JSON-RPC-Protokoll | Google | Live-Kanal mit Endpunkten | gering | groß | nicht passend: kein Server, Git ist der Kanal |

## Was das konkret ändern würde (Vorschlag Regeln v3, je ein kleiner Schritt)

1. **Nachrichtenkopf nach FIPA und A2A** für jede Koordinationsdatei und jeden Issue-Kommentar (YAML-Kopf oder erste Zeile):
   ```
   akt: anfrage | information | zusage | ablehnung | vorschlag | bestaetigung | widerspruch | nicht_verstanden
   gespraech: KOORD-030          # conversation-id
   antwort_auf: <SHA oder ID>    # in-reply-to – verhindert gekreuzte Nachrichten
   antwort_bis: 2026-11-04       # reply-by (optional)
   zustand: submitted | working | input-required | completed | failed | rejected
   ```
   Ein Validator prüft: Jede `anfrage` bekommt genau eine Antwort mit `antwort_auf`. Offene Anfragen nach Ablauf von `antwort_bis` zählen für R7.
2. **Agent Cards:** `forschung/koordination/AGENT_CARD_CLAUDE.json` und `…_GPT.json` mit Bereichen, Fähigkeiten, Grenzen (z. B. „Claude ändert nichts unter docs/“), Werkzeugen, Eingabe- und Ausgabeformaten. Das ersetzt verstreute Zuständigkeitsabsätze.
3. **Prüfstufen nach ACM** in Testregister, Claims und PM-Status:

   | Stufe | Bedeutung bei uns | Beispiel |
   |---|---|---|
   | verfügbar | Datei liegt mit SHA in Git | Zweig ki-tensor |
   | funktional | Owner-Test läuft | Owner-Lauf R4 |
   | reproduziert | **andere KI** führt **dieselben** Skripte aus, gleiches Ergebnis | Claude führt `gpt_logic02_independent.py` aus |
   | **repliziert** | **andere KI** prüft mit **eigenem** Code und eigener Quelle | Claude rechnet DLMF v6.6 neu, s. u. |
   | freigegeben | Nils | — |

   Das löst eine bisherige Unschärfe: „gegengeprüft“ konnte beides bedeuten.
4. **Entscheidungen als ADR:** `forschung/koordination/entscheidungen/DEC-<ID>.md`, Status `vorgeschlagen → angenommen → ersetzt durch …`. `ENTSCHEIDUNGEN_NILS_…md` wird zum erzeugten Index. Der rote Rahmen im Bericht (R2) liest dieselben Dateien, ein Abschreiben entfällt.
5. **R8 auf PROV und CRediT abbilden:**
   - `KI: claude` → `prov:wasAttributedTo`
   - `Analyse-von:` → `prov:wasDerivedFrom` / `prov:Activity type=review`
   - In Publikations-Upgrades werden KI-Beiträge mit einer CRediT-Rolle ausgewiesen (z. B. „Validierung: Claude“), ohne Autorschaft.

## Was **nicht** zu uns passt, und warum

- **Echtzeitprotokolle** (A2A-HTTP, CloudEvents-Broker): Sie bräuchten Server und Zugangsdaten. Git ist langsamer, aber versioniert, öffentlich nachvollziehbar und ohne Zusatzrisiko.
- **Konsens-Abstimmung zwischen KIs** über Inhalte: Bei Inhalt und Veröffentlichung entscheidet der Autor. Die KIs empfehlen nur (R1).
- **Automatisches Zusammenführen** fremder Bereiche: Die Bereichstrennung verhindert Konflikte und ist ein Schutz, kein Hindernis.

## Stand der Belege

Die Standards sind aus Fachwissen benannt (Stand 2025/2026). Die Kernaussagen sind stabil und allgemein bekannt. Vor Übernahme in Regeln v3 werden sie einzeln mit Primärquellen verlinkt: fipa.org/specs, a2a-protocol.org, adr.github.io, acm.org/publications/policies/artifact-review-and-badging-current, w3.org/TR/prov-o, credit.niso.org, rfc-editor.org/rfc/rfc8174.
