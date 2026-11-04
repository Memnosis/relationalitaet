---
document_id: AUDIT-VORSTUFE-001
version: 0.1.0
stand: 2026-11-04
status: auditplan_mit_erstbefunden_nicht_vollstaendig
scope: Memnosis/relationalitaet, KI-Tensor/SOULution
vor_beginn: FORSCHUNG_PFLICHTENHEFT; WEBSITE_PFLICHTENHEFT
---

# Obligatorische Gesamtanalyse vor beiden Pflichtenheften

## Entscheidende Reihenfolge
0. Scope-Snapshot: Repo-Commit-SHA, Branches, veröffentlichte Pages, Inventar der Referenzarchive, Sichtbarkeit und Zugriffsgrenzen festhalten.
1. Jede öffentlich erreichbare **Seite einzeln**, jede größere definierbare **Datenmenge einzeln** erfassen; fehlende externe/private Inhalte im Inventar als `not_accessible` dokumentieren, nicht unterstellen, sie seien geprüft.
2. Je Objekt untersuchen: Ziel/Nutzer, Inhalt und Qualität, wissenschaftliche Aussagen, Quelle/Provenienz, Stand/Version, Funktionen, UX/Accessibility, Sicherheit/Rechte, technische Fehler, Abhängigkeiten, doppelte Daten und fehlende Links, Offenheit der Aufgaben.
3. Querschnitt: Navigationsgraph, Datenfluss, Doppelpflege, veraltete Zahlen, Veröffentlichungsgates, Quellenregister/Glossar/Skills/API/Prompt- und Ergebnisregister, Wiederverwendung in Website/Berichten.
4. GPT und Claude erstellen unabhängig Erstbefund und Gegengutachten; mindestens zwei tatsächliche Gegenprüfungen, Konflikte/fehlende Belege offenhalten.
5. Konsolidierte Ist-Architektur, Befundregister, Widersprüche, Priorisierung und ausdrücklich benannte Forschungslücken.
6. **Erst danach** Anforderungen ableiten: getrenntes Forschungs- und Website-Pflichtenheft mit `derived_from` Audit-ID und Test-/Abnahmekriterium. Kein Befund geht ohne Entscheidung verloren.

## Vorgesehene Objektakten
`SITE-<stable-id>`: URL/Dateipfad, Navigationsweg, Seitenrolle, Zielgruppen, Inhalt, Layout/Mobil, Abbildungen, Interaktionen, DOI/Quellen, interne/externe Links, Datenschutz/Lizenz, Datenquellen/Hashes, Status, Bugs/Inkonsistenzen, Empfehlung/Prüfbelege.
`DATA-<stable-id>`: Speicherort/Quelle, Eigentümer, Datenmodell, Version/SHA, Einträge/Bezugsobjekt/Stand, Erfassungsweg, Veränderungshistorie, Sensitivität, Lizenz, Referenzintegrität, Validierungs-/Reproduktionsstatus, Verbraucher/Exporte, No-Loss/Glossar-Sync, offene Fragen.
`FIND-...`: Auswirkung, Reproduktion, Beleg, Verantwortlichkeit, Status, Priorität, Folgeprüfung; `REQ`-Ableitung erst nach Gegenlesung.

## Mindestinventar aus bekannten Projektnachweisen – NOCH NICHT vollständig auditiert
Website-Einstiege: `docs/index.html`, `docs/soulution.html`, `docs/mitmachen.html`, `docs/thesen.html`, `docs/medien.html`, `docs/tensor-einfuehrung.html`, `docs/ki-geschichte.html`, Projektmanagementseiten und Dashboard (konkrete Pfade, aktuelle Seitenversionen beim Inventarlauf prüfen).
Datenkomplexe: `forschung/register/` (Quellen/Claims/Evidenz/Glossar/Tests/Gegenrechnungen), `forschung/koordination/` (Review-Queue, Entscheidungen, Agent Cards, Zustandsakte/Logs), `docs/data/` (Website-Projektionen), historisches No-Loss-Archiv, Promptbibliothek/-Tests/-Rückgaben, Tensor-/Trinitäten-/Relations-/Formelbestände, Publikationen/Medien, Skills/APIs und Projektmanagement-Generator.
Die historische Zahlenlage (z. B. Glossar 1.072, Feldakten 27, 12 Relationspositionen) ist **kein verifizierter aktueller Audit-Zählstand**.

## Pro Objekt verbindliche Prüfdimensionen
- (a) Vollständigkeit: alle Dateien, publizierten URLs und Verweise in manifestierter Bestandsaufnahme erfasst?
- (b) Wissenschaft: Behauptung, Rekonstruktion, Gegenprobe und Nachweis trennbar?
- (c) Aktualität: Commit, Publikationsdatum, supersedes, Zählstichtag?
- (d) Interoperabilität: Parser, JSON-Schema, IDs, Import/Export, API, Migrationskosten?
- (e) Nutzerführung: Zielgruppe, Auffindbarkeit, Verständlichkeit, Mobile, Tastatur?
- (f) Governance: Entscheidungen, Zuständigkeiten, Lizenzen, Geheimhaltung, Freigabe?
- (g) No-Loss: verwaiste Einträge, abweichende Namensgebung, Dubletten und Auswirkungsgraph?
- (h) Wirkung: welche Forschung/Website-Funktion unterstützt das Objekt wirklich?

## Akzeptanzkriterien für Auditabschluss
Alle im eingefrorenen Scope erfassten Seiten und größeren Datenkomplexe mit IDs und Akten; jede Behauptung zur Prüfung mit konkretem Beleg; Abdeckung (geprüft / nur inventarisiert / unzugänglich) separat ausgewiesen. Kritische Widersprüche stehen in einer offenen Befundliste; beide KIs haben die Gesamtanalyse wechselseitig zwei Mal behandelt. Nicht zugängliche Originale sind als Lücke sichtbar. Erst dann Freigabe zur Ableitung beider Pflichtenhefte; keine fiktiven PASS-Meldungen.

## Promptreflexion als kleines Experiment innerhalb der Vorstufe
Je eine geprüfte Objektakte der Website und der Datenbestände als Eingabe. Prompt zur Ist-Analyse: Entwurf → Peer-Kritik → Überarbeitung → zweite Gegenprüfung → Ausführung auf eingefrorenen Inputs. Analyse: neu entdeckte echte Fehler/Abhängigkeiten, verlorene oder erfundene Befunde, messbare Testbarkeit, Aufwand und Ertragsgrenze. Die Methode wird **nicht** vorab als überlegen erklärt.

## Erste vorläufige Risiken zur Gegenprüfung
- Doppelpflege von Fortschrittszahlen zwischen Claude-PM-Aggregat, Website und Dashboard.
- Mehrfachversionen von Website-/Forschungsplan ohne Supersession.
- Unterschied zwischen GitHub-Pages-Public-Safe-Ansicht und tatsächlich privaten Quellen.
- Unklare Herkunft und Bezugsgrößen von Zahlen, Cover/DOI/Lizenzabweichungen und Veröffentlichungsstatus.

Status: Auditplan und Arbeitsinventar. Keine vollständige Seiten-/Datenbestandsanalyse, kein gemeinsam angenommenes Pflichtenheft.
