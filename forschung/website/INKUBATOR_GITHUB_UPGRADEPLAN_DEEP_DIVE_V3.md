# Schrödinger’s Inkubator – Deep Dive, Quellenarchitektur und GitHub-Upgradeplan v3

**Forschungsstand:** 03.11.2026 · **Zuordnung:** SOULution → Digitale Souveränität → Schrödinger’s Inkubator · **GitHub-Stand:** Integrationsbranch, nicht als öffentliche fertige Plattform ausgegeben.

## A. Ausgangsfrage und eigenständiges Versprechen

Das Originalkonzept verbindet Projektidee, Mitwirkende, vorhandene Programme und geteilte Infrastruktur, um mit möglichst wenigen Logins, Softwareprodukten und Mitwirkenden möglichst viele digitale Funktionen nutzbar zu machen. Die neue Hypothese lautet: Software könnte künftig wesentlich aus dem Zusammenfügen **bereits erprobter und interoperabler Kernfunktionen** entstehen, während generative KI weitere Teile der Bedienung, Anpassung oder Integration übernimmt. Ob deshalb heutige komplette Anwendungen überflüssig werden, ist gerade eine **zu testende**, keineswegs bewiesene Aussage.

Das Inkubator-Projekt schafft auch ohne KI bereits Mehrwert durch Open-Source-Auswahl, gemeinsam finanzierte Infrastruktur, Gruppenaccounts mit sauberer Rechte-/Zugriffstrennung und verteilte Kooperation.

**Nicht verwechseln:** gemeinschaftliches Hosting ≠ frei teilbare persönliche Passwörter. Für Teamarbeit sind organisationsgebundene Konten, Rollen/RBAC, OIDC/OAuth, separate Nutzeridentitäten, verschlüsselte Geheimnisse, Audit-Logs und nachvollziehbare Ausstiege zu bevorzugen.

## B. Vergleichsfelder: Was existiert bereits?

| Feld | Referenzen | Welche Leistung wir prüfen | Besondere Grenze |
|---|---|---|---|
| Europäische digitale Gemeingüter | Digital Commons EDIC, LaSuite, openDesk, MijnBureau, Sovereign Tech Agency | Gemeinsam finanzierte, interoperable, verwaltbare Softwaregrundlagen | Nationale Arbeitsplatzlösungen sind keine universelle Multi-ERP-Inkubatorplattform |
| ERP, Datenschemata und Prozessmodelle | Frappe / ERPNext, andere vollständige ERP-Kandidaten | Metadata/DocType → Formulare → Rechte → Workflows → Dashboard; API und Export | Modell- und Migrationsaufwand; Rechte-/Mandantentrennung |
| Low-/No-Code und Dashboards | Appsmith, Budibase, Directus, Baserow, NocoDB, Node-RED | UI und Funktionskomposition über bestehende Backends | Nicht jedes Projekt ist OSI-open source; verschiedene Produktklassen |
| Identitäten und Rollen | Keycloak, authentik, OIDC/OAuth, ggf. Matrix Authentication Service | Einmalige Anmeldung, Rollen, Projektmandanten, delegierte Berechtigungen | Zentraler Login ≠ automatischer Zugriff, keine Passwortweitergabe |
| Kooperation und Dateien | Nextcloud, Forgejo | Rechtekontrollierte Gruppenarbeit, Datenexport, Versionierung, selbst betreibbare Dienste | Betrieb, Backup, Support und Migration |
| Matrix | Synapse, Tuwunel, Continuwuity; Matrix-Spezifikation | Mehrere föderierte Homeserver, Räume, Events, Bridges, SSO/OIDC | Serverkapazität, Sicherheit, Moderation, Bridges und kompatible Matrix-Versionen prüfen |
| Fediverse | ActivityPub, Mastodon-ähnliche Dienste; experimentelle Forgejo-Föderation | Föderiertes Publizieren und Identität, verteilte Community | ActivityPub und Matrix erfüllen **unterschiedliche** Protokollaufgaben |
| Security-Bibliotheken | OpenSSL, libsodium, rustls | Gemeinsame geprüfte kryptografische Kernfunktionen / sichere API statt Neuentwicklung | Kein Eigenbau von Kryptografie; Versionen, Sicherheitsmeldungen, Betriebsumgebung |
| Open-Source-Supply-Chain | OpenSSF Scorecard, OSPS, SLSA, Sigstore, SBOM, OSV | Reproduzierbarkeit, Herkunft, Schwachstellen, Signaturen und Wartungsstatus | Ein Score oder Signatur alleine beweist nicht Sicherheit |
| Open-Source-Governance | Sovereign Tech Agency, Digital Commons EDIC | Dauerhafte Pflege kritischer gemeinsamer Grundbausteine | Finanzierung und Beteiligung bestehen bereits – Kooperation vor Parallelentwicklung |
| Proprietäre Kompatibilität | Samba, Wine, SAS/WPL-Urteil, EU-Software-Richtlinie | Independente Kompatibilität, Protokolle, dokumentierte APIs, Datenportabilität | Kein pauschales Kopierrecht; Art. 6 mit engen Voraussetzungen |

### 1. Warum Security-Bibliotheken ein Schlüsselbeispiel sind

Die eigentliche Leistung dieser Entwicklung liegt in der **Arbeitsteilung**: weniger eigenentwickelte Kryptografie, dafür breit genutzte fachlich enge Bibliotheken, automatisierte Tests, gepinnte Versionen, nachvollziehbare Signaturen, Schwachstellenverwaltung und professionelles Maintenance. Das ist exakt der Unterschied zwischen „einem Modul, das irgendetwas kann“ und „einem vertrauenswürdigen gemeinsamen Kern“. OpenSSF bietet mit Scorecard, OSPS Baseline, Sigstore und SBOM gleich mehrere voneinander zu trennende Prüfungsfamilien.

Forschungsidee: dieselbe TLS-Aufgabe mit OpenSSL / rustls in zulässigen Konfigurationen vergleichen, keine Scheinsicherheit durch Codeumfang. Projektstatus zunächst Quellen- und Lizenzanalyse; keine Live-Kryptografie-Penetrationstests behaupten.

### 2. Re-Engineering und die rechtliche Grenze

Die EU-Software-Richtlinie 2009/24/EG, Art. 5/6, und das EuGH-Urteil C-406/10 (SAS Institute/World Programming) geben rechtlich bedeutsame Unterschiede vor: Ideen, Funktionalität und Programmiersprachen sind nicht mit der geschützten konkreten Ausdrucksform gleichzusetzen; eine unter engen Voraussetzungen zulässige Analyse zur Interoperabilität ist keine allgemeine Erlaubnis zum Nachbau oder Kopieren geschützten Quellcodes.

**Prüfkette:** Funktion beschreiben → veröffentlichte Protokolle / offizielle APIs suchen → rechtmäßigen Testzugriff prüfen → unabhängige Implementierung erwägen → Tests mit legitimen Daten durchführen → Reproduzierbarkeit, Lizenzrecht und Leistungsgrenzen dokumentieren.

Samba ist ein besonders substantielles Praxisbeispiel: Es ermöglicht die Integration freier Linux/Unix-Umgebungen in Windows-/Active-Directory-Welten und wird gemeinschaftlich getragen. **Kompatibilität ersetzt dabei keine kopierte proprietäre Implementierung.**

### 3. Matrix, Fediverse und gemeinschaftlicher Betrieb

Matrix-Föderation repliziert Ereignisse zwischen Homeservern; das Fediverse verwendet vor allem ActivityPub für verteilte Veröffentlichung und soziale Aktivitäten. Eine Plattform braucht deshalb möglicherweise verschiedene Protokolladaptionen. Eine feste Zahl „benötigter Matrix-Server“ kann erst aus Gruppen, gleichzeitigen Nutzern, Medienvolumen, Retention, Moderation, Backup und administrativen Zuständigkeiten abgeleitet werden.

**Vorgeschlagene Veranstaltungsserie:**
1. Von Login, Identität und Rollen zu sinnvoller Zusammenarbeit.
2. Einen kleinen Matrix-Raum und die Föderation erklären und ausprobieren.
3. Fediverse und ActivityPub: Veröffentlichung über verschiedene Server.
4. Gemeinsame Server: Kosten, Pflichten, Moderation und Pflege.
5. Schnittstellenfest: Eine Aufgabe über ERP → Datei → Kommunikation → Dashboard übertragen.
6. Werkstatt: Bestehende offene Lösungen und gemeinschaftliche Trägerinstitutionen vergleichen.

Keine automatische Behauptung über real eingerichtete Server oder Partnerschaften.

## C. Ein wirklich gutes Quellenregister

**Drei getrennte Objekttypen:**
1. **Quellenakte** (Originalanbieter/Standard/Rechtsnorm, überprüfte URL, Datum, Fundstelle, Quellenqualität).
2. **Funktions-/Skillakte** (Kernfunktion, Input/Output, bekannte Implementierung, Bibliotheksversion, Lizenz, Test).
3. **Integrations-/Testakte** (eingebundene Schnittstelle, echte Konfiguration, Ergebnis, Gegenprobe und reproduzierbarer Nachweis).

**Quelle ist nicht Integration.** Eine gefundene Bibliotheksseite beweist weder Installierbarkeit noch Lizenzkompatibilität oder sichere Verarbeitung. Quellenakten werden über stabile IDs referenziert, nicht mehrfach in jedem Projekt kopiert.

Angelegte Dateien:
- `forschung/soulution/digitale-souveraenitaet/INKUBATOR_QUELLENREGISTER_V1.json` – 38 eindeutige Quellen mit getrenntem Lese- und Integrationsstatus, einer erhaltenen Alias-ID.
- `forschung/soulution/digitale-souveraenitaet/INKUBATOR_SKILL_API_SYNC_V1.json` – Projekt-Referenzgraph aus bestehenden Skill-/Aufgabenlisten, Inkubator-Modulen und externen Schnittstellenkandidaten.
- `forschung/soulution/shared/skills-v0.1.json` – vorhandene sechs Kandidaten **bleiben** Kandidaten.
- `forschung/website/MITMACH_TASKS.json` – 13 Aufgaben behalten ursprüngliche IDs, Nachweise und offene Ausführung.
- `docs/data/inventar.json` – historische lokale Archive bleiben `local_only`, keine nachträgliche Scheinmigration.

**Aktuelle Abdeckung:** 38 Quellen; 25 Inhalte tatsächlich in öffentlicher Recherche gesichtet, 13 nur Quellenadressen; 0 real installierte Fremdkomponenten und 0 komplette API-/Lizenztests in dieser Serie. 6 Skillkandidaten, 13 Mitmachaufgaben, 7 Module und 28 erfasste mögliche Schnittstellenkandidaten sind als Datenobjekte referenziert.

## D. Upgrade der GitHub-Website

### D1. Informationsarchitektur

*SOULution → Digitale Souveränität → Schrödinger’s Inkubator* ist der thematische Einstieg. Dort erscheinen:
- Kurze Einstiegserklärung und **unveränderte** Originalgrafiken, breit im Textbereich.
- „Was ist schon möglich?“ als verständliche Gegenüberstellung real vorhandener Programme.
- Sechs Funktionsräume mit Beispielabläufen: Zugang, ERP/Dashboard, Kommunikation, Lernen, Finanzen/Shop, Betrieb.
- Links **Kernpaper lesen**, **Quellen und vergleichbare Projekte**, **gemeinsam forschen**.
- Sachlicher Forschungsstatus ohne interne Redaktionsanweisungen.

Die **ausführliche Quellen- und Vergleichsbibliothek** ist eine eigene verlinkte Fachseite und JSON-Datenquelle. Forschungsprompts, Testdaten, Verantwortlichkeiten und API-Schemata bleiben in Fachregistern. Der universelle Navigationsaufbau zeigt **SOULution/Digitale Souveränität**; in der globalen Navigation wird keine neue Buch-Veröffentlichung „Wissen, Macht und Wirklichkeit“ vorgetäuscht.

### D2. Visueller Aufbau

- Grafiken sind über die Breite des tatsächlichen Inhaltsbereichs einzusetzen (`max-width:100%; height:auto; object-fit:contain`). Originalsätze und Bildelemente nicht neu interpretieren.
- Einheitliche, aus Originalgrafiken abgeleitete Farb- und Typografieregeln; Icons bleiben konsistent.
- SVG-Diagramme: Daten/Funktion/Adapter/Betrieb. Interaktive Graphen erst mit echten Relationen.
- Kein „Originalpublikationen bleiben unverändert“, kein Hinweis „Branch noch nicht live“ und keine Entwickler-Task-ID im Lesertext.
- Auf der Webseite gehören *Wissen, Macht und Wirklichkeit* und der Quellen-/Medien-Entwurf vorerst nur in die **Quellen- und Medienliste**, nicht als neues eigenständiges Buch mit Cover und PDF.

### D3. Arbeitspakete und Abnahme (geordnet)

| Phase | Umsetzung | Prüfbare Abnahme |
|---|---|---|
| P0 · Quellen | Quellenregister, Dubletten, Originalbelege, Versions- und Rechtsstatus | IDs eindeutig, Quelle getrennt von Softwareintegration, keine erfundenen Tests |
| P1 · Navigation | Inkubator als SOULution-Vertiefung; Querverweise von Bibliothek, Mini-KI, Interoperabilität; keine redundante Hauptnavigation | dieselben Menüs und funktionierenden Links auf jeder erfassten Seite |
| P2 · Medien | Originalgrafiken aus dem vorhandenen Material als richtige Dateien unter `docs/assets/media/inkubator/`, Kernpaper als Markdown und ggf. PDF | Bilddateien existieren tatsächlich, responsiv vollbreit, kein fehlender Download |
| P3 · Quellenatlas | öffentliche Quellen-/Vergleichsseite mit Such- und Kategorieansicht aus JSON | 38 source IDs zugänglich, jeder externe Link korrekt gekennzeichnet |
| P4 · Synchronisation | bestehende Skill-, API- und Registerreferenzen zu kanonischen IDs verknüpfen | referenzielle Integrität, `local_only` und Kandidaten bleiben erhalten |
| P5 · Sicherheit/Legalität | OSPS, Scorecard, Lizenzprüfung, SBOM, BSI-/Datenschutzanforderungen im Piloten | dokumentierte Gegenproben, keine ungeprüfte Rechtsfreigabe |
| P6 · Piloten | ein festes End-to-End-Szenario über Identität, Daten, Oberfläche, Kommunikation | wiederholbarer Lauf, Export-Rücktest und echte Fehlerakte |
| P7 · Kooperation | Matrix/Fediverse-Betriebsmodelle und Veranstaltungsserie | realistische Betriebs-/Kostenprofile; keine fiktiven Serverzahlen |
| P8 · Qualität | Desktop, Mobil, Tastatur, Linkscanner, README und PR-Abnahme | keine kritischen Links, CI erfolgreich, fachliche Freigabe |
| P9 · Freigabe | Review + Merge, erst danach GitHub Pages | auf `main` technisch erreichbar, nicht nur im Arbeitsbranch |

**Wichtig:** Nicht alle Bereiche müssen zur selben Zeit live geschaltet werden; Quellen-/Atlas-Seiten können früher veröffentlicht werden als eine Plattform, die personenbezogene Nutzerkonten benötigt.

## E. Messbarer Pilot zur Zukunft der Software

Aufgabe: Ein kleiner Projektverbund erhält Rollen, Aufgaben, Dateiablage, gemeinsame Kommunikation und eine statusfähige Benutzeroberfläche. Wir vergleichen:
- A: vorhandene Komplettlösung;
- B: vorhandene frei nutzbare Kernmodule mit Adapter;
- C: gleiche Module mit einem dokumentierten automatisierten Orchestrator;
- D: optional tensorierte, fachlich validierte Funktionen.

Metriken: vollständiger Aufgabenerfolg; fachliche und technische Fehler; Export-/Rückimportqualität; Einrichtung, Betrieb und Wartung; Ressourcenbedarf; Sicherheit und Rechte; Portabilität; neu erschlossene Aufgabenklassen. Der Mehrwert von Tensorrelationen wird separat anhand zusätzlicher **gesicherter Ableitungen** geprüft. Nullresultate gehören in den Ergebnisbericht.

## F. Noch offene Grenzen und nächste Selbsttests

- Vollständiger Repository-Filescan wurde bisher nicht ausgeführt; ein Skript zur lokalen Vollerhebung ist vorhanden, aber nicht als Abschlussnachweis verwendbar.
- Die originale Inkubator-Grafik und das PDF müssen als echte Bild-/PDF-Dateien in den GitHub-Branch, nicht als erfundene Pfade. Der vollständige Text der zweiten Kernpaperfassung liegt bereits als Markdown vor.
- Kein externer ERP-Server oder Matrix-Homeserver wurde in dieser Serie tatsächlich betrieben.
- Die sechs zentralen Skillregistereinträge sind Kandidaten; die hier erzeugten Verweise sind strukturell getestet, nicht als komplette ausführbare Integrationen validiert.
- Die genaue Lizenz von n8n, einzelnen ERP-/Low-Code-Anwendungen und den Versionsständen ist vor konkreter Implementation erneut zu prüfen.

## G. Direkte Einstiegspunkte

1. `docs/soulution-schroedingers-inkubator.html` – Fachlanding.
2. `forschung/soulution/digitale-souveraenitaet/SCHROEDINGERS_INKUBATOR_KERNPAPER_V2.md` – umfangreiches Kernpaper.
3. `forschung/soulution/digitale-souveraenitaet/INKUBATOR_QUELLENREGISTER_V1.json` – kanonische Quellen.
4. `forschung/soulution/digitale-souveraenitaet/INKUBATOR_SKILL_API_SYNC_V1.json` – Referenzen.
5. `forschung/website/AUDIT_ALLE_DATEIEN.py` – Vollcheckout-Audit, vor Releasetest ausführen.
