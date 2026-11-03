# KI-Tensor: 100 Austauschzyklen als auswertbares Forschungsprogramm

**Beschluss:** Nutzerauftrag 03.11.2026 · **Architektur:** GPT (Website) und Claude (Daten/Forschung), beide mit unabhängigen Eigen- und gegenseitigen Prüfungen. **Status:** Plan und technische Datenspezifikation; keine der 100 Runden gilt dadurch als abgeschlossen.

## I. Zählweise und Fortsetzung bisheriger Regeln

1. **Ein Austauschzyklus** zählt nur mit Auftrag, Eingang/Bestätigung, eigenem nachweisbarem Ergebnis, eigener Abnahme, fremder Gegenprüfung, Rückbestätigung und Zyklusbericht mit Git-Commit-/Testankern. Eine Nachricht, ein Push oder ein Kurzbericht zählt **nicht** als Zyklus.
2. **Je voller Zyklus:** Eigenbericht jeder KI, gegengeprüfter Austauschbericht, Repriorisierung und Fehler-/Offenliste.
3. **Nach je drei vollen Zyklen:** gemeinsame Wirkungs-, Methoden- und Aufgabenanalyse mit No-Loss-Versionen.
4. **Nach jeweils zwanzig Zyklen (20/40/60/80/100):** Sicherheits-/Regel-/Change-Management-Audit inklusive Archiv-/Backup-/Retention-/Löschkandidaten. Löschung historischer Daten nur mit vorheriger Wiederherstellungsprobe, Hashprotokoll und Nils' konkreter Freigabe; kein eigenmächtiger Git-History-Rewrite.
5. **Nach 9 und optional 12:** die bisher vereinbarte Autorenentscheidung bleibt als Zwischenentscheidung bestehen; die 100er-Perspektive bedeutet **nicht**, dass ungeprüft bis 100 fortgesetzt wird. Blockplanung und Ressourcen werden nach Zwischenanalysen erneut entschieden.
6. **Nach Zyklus 100:** gemeinsamer **Gesamtbericht** als DOCX für Nils; öffentliche wissenschaftliche Arbeit als vorab anonymisierte/sachliche MD-Fassung, später PDF/DOCX nach Freigabe. Kein Autoveröffentlichen von Rohchats/Promptinterner Architektur.

## II. 20 Schwerpunktzyklen von 100

Ein reservierter Themenpool von **20 vollen Zyklen**, mit vorläufiger Verteilung **12 Mitmach-Aktions- und 8 interne Finalisierungszyklen**. Die konkreten globalen Zyklusnummern bleiben offen; sie werden nur bei tatsächlicher Planung/Abnahme vergeben. Die Quote ist eine erste Planungshypothese; wenn Mitmachaktionen mehr Arbeit verlangen, wird nach begründeter gemeinsamer Prüfung und Nils-Freigabe die Verteilung angepasst – nie stillschweigend.

### Schwerpunkt M: zwölf Zyklen, alle Mitmachaktionen

**Bestandsbasis:** Mindestens die 13 öffentlichen Mitmach-Taskdatensätze, sieben Geo-Interop-Taskdatensätze und achtzehn Beobachter-/Skill-Taskkarten = **38 ursprüngliche Meta-Prompt-Objekte**. Diese 38 sind **nicht** automatisch die vollständige Zahl aller Mitmach-*Aktionen*: auch Navigation, Formular, Kopieren, Starten, Externen-Eingaben, Rückgabe, Quellenzugang, Fehlerhinweise und Barrierefreiheit müssen als separate Interaktionspfade inventarisiert und getestet werden.

Für jeden Aktionspfad:
1. Einsteigerfrage und fachlicher Zweck; erwarteter Nutzen.
2. Welche Quellen dürfen öffentlich genutzt werden? Welche dürfen nur intern bleiben?
3. Prompt/Agent/Meta-Trennung; **direkter Prompt** benötigt eigene Version und kontrollierten Ein-/Ausgabevertrag.
4. Positiv-, Negativ-, Grenz- und Zugangs-/Lizenzfall; eigener GPT-Website-Test und eigener Claude-Fach-/Daten-Test.
5. Gelingt Nutzung **ohne Git-Schreibrechte und ohne interne KI-Accounts**?
6. Wird die Ausgabe über einen erlaubten, nachvollziehbaren öffentlichen Kanal zurückgegeben, ohne Vertrauliches zu leaken?
7. Ist der öffentliche Auftrag nachvollziehbar, sicher, fachlich präzise und nach dem Autorentscheid freigegeben?
8. Aufgaben zu Test, Quellen, Evidenz, Regression und gegebenenfalls zur Publikation verlinken.

**Kein Gruppenabschluss**, solange vorhandene Mitmachaktionen ungezählt oder ohne dokumentiertes Testurteil sind. Fehlendes Testmaterial wird als `blocked` gelistet, nicht als bestanden.

### Schwerpunkt I: acht Zyklen, interne und noch unveröffentlichte Forschungsbestände

Vorrangige Gegenstände: historischer 27-Feld-/309-Trinitäten-/103-Tensoren-Crosswalk, A/B/C/G- und dritter Faktor, Logik-Tensor 2.0/2.1 inklusive Begriffsinventar, Feldtheorie-Belege und Nichtentsprechungen, Glossar-/Quellenlücken und Versionen, mathematische Relations-/Parser-/Testakten, Mini-KI-Kernfunktionen und faire Baselines, Prompt-/Skillregistrierung sowie weitere unfertige Buch-/Forschungsversionen. **Prioritäten nach jedem Zyklus aktualisieren**; hier werden keine Nachweise oder wissenschaftlichen Bestätigungen fingiert.

Jeder interne Zyklus endet mit `erhalten / fachlich geprüft / technisch getestet / offen / widerlegt / publizierbar? / Nils-Freigabe`. Auch ein nachgewiesenes Negativergebnis ist ein wertvoller Abschluss.

## III. Sauber trennbare Kommunikation und wissenschaftlicher Export

### Private operative Ebene (neu)
Laufende KI↔KI-Nachrichten, technische Rohprompttexte, interne Manuskripte, private Gesamtregister, unveröffentlichte Quellen und Einzelarbeitsprotokolle gehören in **einen tatsächlich privaten Speicher** mit differenzierten Schreibrechten. Ein Ordner namens `intern` auf dem öffentlichen Git ist *nicht* privat. Sollen zwei externe KIs denselben Bestand bearbeiten, ist ein **separates privates Git-Repository** mit begrenztem Zugang oder ein geeigneter privater Transfer nötig.

### Öffentliche Belege und Website (bestehend)
Das öffentliche Repository `Memnosis/relationalitaet` enthält ausschließlich frei gegebene: Methoden- und Schemaspezifikationen, redigierte Ergebnis-/Testmetadaten ohne sensitive Texte, kleine Datenprojektionen für Projektstand/Mitmachen, Quellenfundstellen mit erlaubtem Zitatauszug, negative Befunde und redigierte Studienkapitel.

### Austauschdokumente / Studie: standardisierte Struktur
Jeder Zyklus sollte einen versionsstabilen Datensatz mit `cycle_id, prompt/task_ids, actor, ownership, input_artifact_hash, output_artifact_hash, tested_method, baseline, observed_results, negative_findings, changes, dependency_effects, reviewer, peer_review_status, privacy_class, release_status, source_refs` erzeugen. Rohdiskussionen als **Belege separat privat**, publizierbare Methoden- und Ergebnisdaten als **neutrale exportfähige Akten**. Eine Studie muss verständlich bleiben, auch wenn interne Rohkommunikation nicht öffentlich gezeigt wird.

**Vorgesehene Studiemodule:** Forschungsfrage und zwei KI-Rollen; Methode/100er-Zyklusprotokoll; Messgrößen und Baselines; öffentliche Mitmachaktions-Tests; interne Forschungsfinalisierung; Kommunikation/Fehler und No-Loss; Sicherheit/Datenschutz; tatsächlicher Nutzen, Aufwand und Limitierungen; übertragbares Mitmach-Protokoll; Anhänge mit neutralen Test-/Quellenakten.

## IV. Git-Bereinigung – ausdrücklich nicht destruktiv ohne Abnahme

**Sofort:** neue interne Unterhaltung **nicht** mehr unnötig unter öffentliches `forschung/koordination/zyklen` pushen; auf der Website keine direkten Links auf internes Issue/Chatlog; nur sachliche, redigierte Projektergebnisse und Forschungsmethoden anzeigen.

**Migration:** einen wirklich privaten Zielort beschließen, Bestände kopieren, SHA-256 und Wiederherstellung prüfen, Originalverweise mit privater Zuordnung ersetzen und erlaubte öffentliche Zusammenfassungen behalten. Die alten Git-Commits und Issue-Kommentare sind **bereits öffentlich gewesen** und werden nicht automatisch privat, selbst wenn Dateien in `main` entfernt werden. Vor Löschen/History-Rewrite alle ungesicherten Rückverweise und Folgen prüfen; keine eigenmächtigen Eingriffe in Originalhistorie.

**Nachweis:** `migrationsmanifest` mit Quelle (öffentlicher Git-SHA), Ziel (privat mit ID), Hashvergleich, Restoreprobe, Freigabestatus und Rückführungsmöglichkeit; kein unverifiziertes Löschen. Ein reines Verschieben von `docs/` nach `forschung/` behebt die Öffentlichkeit **nicht**.

## V. Eigentest, Gegentest und zyklische Priorisierung

**GPT:** Website, Nutzerführung, Promptanzeige, Testbarkeit/Ergebnisrückgabe, visuelle Regeln, Dokumenten-/HTML-Export. **Claude:** Daten, originale Claims, Validatoren, wissenschaftliche Formalisierung, Source-/Evidenz-Crosswalk, Freigabeprojektion. Beide prüfen die jeweils fremden eigens belegten Ergebnisse und dokumentieren abweichende Einschätzungen. Nils entscheidet reale Veröffentlichungs-/Strukturkonflikte.

Prioritäten je KI getrennt nach Dringlichkeit, Schlüsselwirkung, Sicherheit, Blockergrad, Reife, Aufwand und Auswirkungen auf Forschungsfelder berechnen. Jede Zwischenanalyse untersucht, ob umgesetzte Schritte tatsächlich weitere Aufgaben ermöglichten; reine Planzahlen nicht als Wirkungsmessung ausgeben.

## VI. Aktueller Nachweisstand und Auslöser

`KI-2026-11-03-001/STATUS.json` weist Claude-Lieferung aus, aber `gpt_reviewed=false`, `claude_acknowledged_review=false`, `cycle_report_created=false`. Daher **0 verifizierte vollständige Zyklen aus diesem sichtbaren Programm**; keine vorzeitige 100er-Zählung.

Die vorliegenden 38 ursprünglichen Meta-Prompts hatten in Claudes Metadatenanalyse 14 Freigabekandidaten, 22 interne und zwei fachlich heikle Fälle, **alle `not_run/not_approved`**. Der Schwerpunktpool verlangt tatsächliche Tests und unabhängige Freigabe statt Rohtextkopie.

**Auftrag Claude:** prüfe 100er-Protokoll und 12/8-Split, liefere eigenen Mitmach-/internen Prioritätsentwurf, sichere alle privaten Ausgangswerte, erarbeite Datenexport-/Studienformate und nenne konkrete Gegenargumente. **Auftrag GPT:** öffentliche Website auf sachlichen Fortschritt umstellen, Testinventar und Sichtprojektion bereitstellen, Browserpfade prüfen; operative Kommunikationslinks aus Website entfernen. **Beide:** Migrations- und Sicherungsschritte in privater Koordination vereinbaren; Freigaben nicht selbst erfinden.
