# 100 Originalprompts: Rekonstruktion, Simulation und Mitmach-Rückgabe

**Stand:** 03.11.2026 · **Owner:** GPT Website/Workflow · **Claude:** fachliches Gegenreview ausstehend · **Status:** Code und lokale Simulation ausgeführt; echter Export mit den genau letzten 100 Originalnachrichten und echter Empfangsservice **noch nicht verfügbar**.

## A. Quellenbefund und methodischer Fehler im bisherigen 72er-Register

- `forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json` enthält **72 atomisierte Anforderungen** mit neun künstlich symmetrisch gruppierten Themenbereichen zu je acht Einträgen. Die Zuordnung eines `evidence`-Pfades ist ein Git-Dateiverweis, weder eine Originalmessage-ID noch eine tatsächliche Erledigungsprüfung.
- `original_message_id=null`, `original_text_verified=false` und `verified_exact_100_message_sequence=false` sind **korrekte**, wichtige Schutzfelder.
- Die zugehörigen 72 Git-Dateien wurden zuvor einzeln auf Vorhandensein geprüft. Daraus folgt **nicht**, dass genau 72 der letzten 100 Nutzeraufträge erfüllt wären.
- Eine Projektkontextsuche fand einzelne frühere Originalnutzeräußerungen mit Zeitstempeln und historische Chatfragmente, **aber keine exportierte, chronologisch vollständige Folge der letzten genau 100 Nachrichten mit Message-IDs**. Die vorhandenen Projektzusammenfassungen dürfen fehlende Originaltexte nicht ersetzen.
- Die eigentliche Zielgröße muss ausdrücklich festgelegt werden: letzte 100 User-Nachrichten **aller ausgewählten KI-Tensor-Projektgespräche**; nicht 100 beliebige Assistentenantworten oder automatisch 100 Nachrichten aus dem letzten Thread. Der Chat-Auswahlumfang wird separat protokolliert.

## B. Ausgeführte lokale Simulation – rein synthetische Daten

Ein privater rekonstruierbarer Parser und sechs Unittests wurden in der GPT-Ausführungsumgebung tatsächlich ausgeführt: **6/6 PASS**. Darunter ein Export mit 100 **erfundenen** Nachrichten, Auswahl ausschließlich der User-Rolle aus freigegebenen Test-Gesprächen, Sortierung nach tatsächlichem Timestamp, keine automatische Bearbeitungsfreigabe, fehlender Timestamp als Fehler und öffentlicher Export ohne Originaltexte.

Ein zusätzlicher deterministischer Stressfall modelliert absichtlich:
- 40 Nachrichten mit je einer vorhandenen Anforderung;
- 20 Nachrichten mit je **zwei** Anforderungen;
- 10 Nachrichten, die frühere Anforderungen **ändern**;
- 10 Nachrichten, die frühere Anforderungen **aufheben**;
- 20 Nachrichten mit **neuen** Anforderungen.

**Simuliertes Ergebnis:** 100 Originalnachrichten → **120 Beziehungskanten**, **72** berührte bisherige Tasks und **20 zusätzliche** Aufgabenfamilien (= 92 eindeutige Taskkennungen im fiktiven Fall). **Dies sind ausschließlich ausgedachte Testwerte und keinerlei Messung des realen KI-Tensor-Projekts.** Ein naiver 1:1-Crosswalk würde mindestens 20 zusätzliche Kanten und die 20 Änderungs-/Aufhebungsvorgänge unzureichend modellieren.

## C. Neu implementierter technischer Vorschlag

**Git-Code:** `scripts/prompt100_reconcile.py` + `scripts/test_prompt100_reconcile.py`; synthetischer CI-Workflow `.github/workflows/prompt100-synthetic-tests.yml`. Der Parser liest den offiziellen lokalen ChatGPT-Export `conversations.json` und eine **explizite private Allowlist von Chat-IDs**, berücksichtigt nur `author.role=user`, erhält Message-IDs, Zeitstempel und Originaltexte in einem **privaten** Ausgangsbestand und erzeugt transparent nur Wortüberschneidungs-**Vorschläge** zu den 72 Task-IDs.

**Keine Auto-Akzeptanz:** Kandidaten sind `human_required`. Eine Originalnachricht kann mehrere Tasks `creates / repeats / modifies / replaces / cancels / clarifies` oder als `not_related` abweisen. Der entscheidende Schritt ist die manuelle Entscheidung und Versionierung dieser Beziehungen, **nicht** das Auffüllen auf 100 IDs. Der derzeitige Parser schlägt Wortbeziehungen vor, erkennt semantische Änderung/Negation **noch nicht automatisch** und bestätigt keine Taskerledigungen.

**Sicherheitskonzept:** Nutzertexte niemals in öffentliches Git, Issues, Website-Daten oder CI hochladen. Im Git liegen nur der generische Algorithmus, synthetische Tests und später eine reine Aggregation **ohne** originale Nachrichten-IDs oder Wortlaute. Eine lokale private Originalakte bleibt die alleinige Quelle.

**Lokale Bedienung** (die beiden realen Eingaben bleiben außerhalb öffentlichem Git):

```bash
python scripts/prompt100_reconcile.py \
  --export /privat/conversations.json \
  --allowlist /privat/projekt-chat-ids.json \
  --requirements forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json \
  --private-out /privat/100er-originale-und-kandidaten.json \
  --public-out /privat/100er-aggregate-fuer-freigabe.json
```

Erst nach tatsächlicher Quellenfreigabe darf die öffentliche Aggregation als neue Datenversion auf die Website; keinesfalls die Private-Akte.

## D. Mitmach-Rückgabe: reale erste UI-Lösung statt bloßes Versprechen

**Website-Implementierung:** `docs/mitmachen-rueckgabe.html` mit `docs/assets/mitmachen-rueckgabe.js`, im bestehenden siebenpunktigen Hauptmenü unter *Mitmachen* und auf `docs/mitmachen.html` verlinkt. Besucher können eine **öffentliche** Aufgaben-ID, überprüfbare Prüffrage, Methode, Ergebnis, Quelle und Gegenbefund zu einem JSON-Entwurf zusammenfassen, ihn kopieren oder lokal herunterladen. Das Format ist unter `docs/data/mitmachen-ergebnis-schema-v1.json` dokumentiert.

**Behauptungsgrenzen:** `submission_status=not_submitted`, `publication_approved=false`, `independent_review=pending`. Ein Download ist keine erfolgreiche Einreichung. Der Verweis `issues/new` ist eine mögliche **manuelle** Rückgabe ohne Repository-Schreibrecht, kann aber GitHub-Login und offene Issues verlangen und veröffentlicht nur freiwillig freigegebenen Inhalt. Ein Ende-zu-Ende-Empfang mit Quittung und automatischer Forschungsakte existiert **nicht**.

**Browser-Simulation:** `scripts/verify_website_browser.mjs` enthält jetzt einen Playwright-Test, der ein synthetisches Ergebnis in das neue Formular eingibt, die generierte JSON-Datei herunterlädt, Task-ID und `not_submitted` kontrolliert und fehlende Freigabe nachweist. **Dieser neue Repo-Browserlauf wurde noch nicht erfolgreich in GitHub Actions belegt.** Ein zusätzlicher lokaler Browser-Aufruf war in der GPT-Ausführungsumgebung durch Zugriffssperren auf lokale URLs blockiert; aus dem abgebrochenen Versuch wird kein PASS.

## E. Nächster Nachweis- und Umsetzungsplan

| Priorität | Arbeitspaket | Besitzer und echte Abnahme |
|---|---|---|
| **P0** | Parser an realem **privatem** Originalexport mit expliziter Projekt-Chat-Allowlist verwenden; 100 chronologische Quellen-IDs und Fehlstellen prüfen | GPT Eigennachweis, Originaltexte und Umfang von Nils geprüft; keine Git-Veröffentlichung |
| **P0** | Jeden Vorschlag mit `creates/repeats/modifies/replaces/cancels/clarifies` oder `not_related` manuell verifizieren | GPT/Autor, später Claude Gegenprüfung der wissenschaftlichen Aufgaben |
| **P0** | 72 Grundaufträge gegen neu gefundene und aufgehobene Anforderungen abgleichen; historische Versionen unverändert bewahren | GPT Anforderungen; Claude Daten-/Claim-Crosswalk |
| **P0** | Workflow `prompt100-synthetic-tests.yml` und `website-browser-smoke.yml` tatsächlich starten/Joblogs prüfen; Fehler korrigieren, erst dann Teststatus freigeben | GPT Website/Tests |
| **P0** | Mitmach-Ergebnisformat über drei Beispiele (positiv, negativ, unzureichende Quelle) simulieren; manuelle GitHub-Issue-Einreichung nur mit ausdrücklich freigegebenem Inhalt | GPT E2E-Frontend; echter Rückkanal/Quittung noch zu entwickeln |
| **P1** | Sicheren, unabhängigen Rückkanal mit Empfangs-ID, Datenschutz, Rate-Limits, Validierung und nachvollziehbarer Moderation entwickeln | später gemeinsam und mit Architektur-/Autorenentscheidung |
| **P1** | Quellen-/Test-/Task-Gesamtmetriken erst nach belastbarem Nenner publizieren | Claude Fachregister → GPT Public-Schema → Autorenfreigabe |

## F. Fortschrittsmetriken getrennt halten

**Originalnachrichten-Abdeckung** = verifizierte echte Quellnachrichten / 100. **Zuordnungsqualität** = manuell geprüfte Nachricht↔Aufgabe-Kanten / alle vorgeschlagenen Kanten. **Taskabdeckung** = Aufgaben mit belegter Originalherkunft / aktuell geführte Aufgaben. **Umsetzungsgrad** = Aufgaben mit ausgeführtem Test / in Scope befindliche Aufgaben. **Gegengeprüfter Abschluss** = tatsächlich fremdgeprüfte Aufgaben mit ggf. Autorfreigabe / dafür vorgesehene Aufgaben. Keine dieser Zahlen darf aus bloßer Dateiexistenz gefolgert werden.

**Status heute:** 72 bestehende atomisierte Anforderungen sind dokumentiert und mit Dateien referenziert; **100 originale Nutzertexte und ihre vollständige Aufgabenbeziehung sind noch nicht verifiziert.** Der neue Parser und die Simulationsdaten ermöglichen die Rekonstruktion, sobald die private Originalquelle zugänglich ist.

## G. Nachgezogene Verbesserung: echte unterschiedliche Statuswerte statt Scheinerledigung
Die Ausgangsdatei enthält 72 Tasks mit einer großen Vielfalt freier `status`-Texte. Um die Planung ohne Datenverlust zu ermöglichen, wurde **zusätzlich** `forschung/website/ANFORDERUNGSSTATUS_NORMALISIERUNG_V1.json` angelegt (Commit `c456faa`). Der Originalstatus bleibt je Task unverändert. Eine **heuristische, nicht unabhängig bestätigte** Klasse wird nur für die nächste Prüfwarteschlange vorgeschlagen:
- 23 `artifact_present_not_accepted` (Datei/Umsetzung behauptet, fachliche Abnahme fehlt);
- 22 `open_or_blocked`;
- 13 `partial_or_unclear`;
- 8 `planned_or_documented`;
- 6 `test_or_review_incomplete`.

Dies sind **Klassifikationen von Altstatus-Strings**, keine unabhängigen Prüfresultate. In diesem zusätzlichen Register sind **0 eigenständig dokumentierte Abschlussabnahmen** gespeichert; daraus folgt nicht, dass in der Welt keine Arbeit abgeschlossen wäre.

Die lokale Quellparser-Version berücksichtigt jetzt außerdem mehrere nummerierte `conversations*.json`-Dateien und den ZIP-Export. **Sechs von sechs** lokalen Unit-Tests bestanden; Git-Ausführung und Actions-Bericht bleiben separat offen.

### Sicherheits- und Revisionshinweise
- Ein ChatGPT-Export kann vertrauliche Daten anderer Gespräche enthalten; zum Abgleich werden ausschließlich explizit ausgewählte Projektchat-IDs verwendet. Die private `conversations.json` oder ZIP-Datei wird nicht auf `main` veröffentlicht.
- Durch rein lexikalisches Matching werden einzelne Fachbegriffe möglicherweise zu schwach oder falsch erkannt. Nullfunde sind Suchhinweise und kein Nachweis, dass eine neue Aufgabe entstanden ist.
- Browser-Download und JSON-Schema der neuen öffentlichen Rückgabeseite wurden in den Playwright-Code aufgenommen; eine bestätigte echte End-to-End-Einreichung **existiert weiterhin nicht**.

## H. Sicherheit und Wiederverwendbarkeit der öffentlichen Mitmachkarten

Bei der Prüfung der echten `docs/mitmachen.html` wurde ein Problem des älteren Schemas festgestellt: Der Client bezog alle 13 Aufgaben direkt aus `forschung/website/MITMACH_TASKS.json`, welches auch `meta_prompt`-Texte und interne Quellenlisten enthält. **Ein UI-Gate verschleiert solche Daten nicht vor öffentlichem Zugriff.**

**Nachgezogene Website-Änderungen:**
- `docs/data/mitmach-public-v2.json` – 13 öffentliche IDs mit Titeln und Themen, **ohne** `meta_prompt`, unveröffentlichte Quellen-URLs oder angeblich erfolgreiche Prompt-Ausführung.
- `docs/assets/mitmachen-karten.js` – neuer Renderer greift ausschließlich auf diese bereinigte Projektion zu; ein direkter Prompt könnte in einer späteren Revision nur mit ausdrücklich dokumentiertem `approved` und `passed` erscheinen.
- `docs/mitmachen.html` – alten Inlinereader entfernt, auf bereinigte Datenansicht umgestellt und irreführende Kopieranweisung zu Roh-Metaprompts korrigiert.
- `docs/quellen-und-uebergabe.html` – direkter Rohregister-Link durch Taskkarten-Ansicht mit Freigabestatus ersetzt.
- Die Karte verlinkt eine **lokale** Ergebnisvorbereitung mit automatisch übernommener, validierter Task-ID und optional einen manuell zu eröffnenden GitHub-Issue-Dialog, **ohne** fremde unveröffentlichte Ziele oder Quellenlisten vorzufüllen.
- `scripts/verify_website_browser.mjs` – ergänzt um 13 gerenderte Karten, **keine** Rohprompt-Texte, Ergebnislink und Export-JSON-Status. Der tatsächliche CI-Lauf bleibt offen.
- `forschung/website/seiten/mitmachen-rueckgabe_AUDIT_PLAN_2026-11-03.md` – eigener Nachweis für die neue **34. Website-Seite**; Index und statischer Auditumfang wurden nachgezogen.

**Nicht behoben:** Das alte Rohregister bleibt in `main` und möglicherweise in der Git-Historie öffentlich erreichbar. Für tatsächliche Zugangsbeschränkung müssen Originaldaten in ein externes privates Ziel kopiert und nach Hash-/Restoreprobe sowie Autorenfreigabe die öffentliche Geschichte risikobewertet bereinigt werden; eine neue öffentliche Projektionsdatei allein ist **keine Privatisierung**.
