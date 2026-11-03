# KI-Tensor · Gemeinsamer P0-Prüfrahmen für Claude ↔ GPT
**Version:** 0.1 · **Zyklus:** KI-2026-11-03-001 · **Adressat:** beide KIs. **Status:** GPT-Vorschlag zur wechselseitigen Bestätigung durch Claude; kein abgeschlossener Austausch.

## Leitregel
**Jede KI prüft die Arbeit der anderen am tatsächlichen Artefakt**, nicht nur am Selbstbericht. Sie dokumentiert Ausgangs-SHA, Test, Abweichung, Konsequenz, Verbesserungsoption und den zuständigen Bearbeiter. Jeder Bewertungsvektor besitzt:
- Befund **0 / 1 / 2 / 3** (0 = nicht implementiert, 1 = beschrieben, 2 = implementiert, 3 = an realen Artefakten getestet und reproduzierbar),
- **Nachweisart** und Datei/Commit,
- **Konfidenz** (hoch/mittel/gering),
- **P0-Blocker** (ja/nein), unabhängig von der Zahl,
- **Korrekturvorschlag** und Regression/Gegenprobe.
Der Vektorstatus `not_assessed` ist erlaubt und wird **nicht** als null oder als bestanden gezählt. Ein grüner GitHub-Test ist kein wissenschaftlicher Beweis. Es gibt keine Gesamtprozentzahl ohne validierten Nenner.

## A · Claude prüft Website-GPT (WEB-REVIEW; 10 Vektoren)
| ID | Vektor | Minimum / reproduzierbarer Test |
|---|---|---|
| W01 | Bestandstreue/No-Loss | Original-Pfade, 27 Logikfelder, 3 Matrizen, Buchcover/Grafiken, Abschnitte und alte Anker mit konkreten Vorher-/Nachher-SHAs erhalten |
| W02 | Hierarchische Navigation | **Genau ein** aktives Navigationssystem; mobile Breiten, Touch, Tastatur, Escape, Fokus und Fallback ohne JS getestet |
| W03 | Informationsarchitektur | Hierarchische Zuordnung, direkte Deep Links, fachlogische Nachbarschaften, verständliche Hauptnavigation, zwei Inkubatoren eindeutig unterscheidbar |
| W04 | Didaktischer Lernpfad | Einstieg ohne Fachwissen → Modell/Beispiel → formale Regeln → Gegenbeispiel → Quelle → Anwendung/Mitmachen |
| W05 | Semantische Präzision | A neutrale Achsen, B Originalbezeichnungen T1/T3/T5, C fachimmanent, G als reiner formaler Träger unterschieden |
| W06 | Quelle vs. Evidenz | `pruefung_ausstehend`, vier Zugangs-/Prüfklassen sowie Belegqualität und Redaktionsfreigabe unabhängig; keine erfundenen Quellen |
| W07 | Prompt-/Agent-/Meta-Didaktik | Kontextfragen am Ort; Agenten-/Meta-Layer klar, Roh- und Projektarchitekturprompts nicht automatisch veröffentlicht |
| W08 | Öffentlichkeit/Rückgabe | Ohne Git-Schreibzugang nutzbare Mitmachaufgabe mit offener Quelle, Eingabe, Ausgabe, Tests und Redaktion |
| W09 | Designkonsistenz/Barrierefreiheit | Fachfarben, Kontrast, Labels, Alt-Texte, Tabellenumbruch, responsives Layout und bestehende Mitmach-CTA |
| W10 | Verlässlicher Fortschritt | Website-/Task-Anzeigen haben datierte Zähler, Nenner, Prüfstand und Belegpfad; Test ≠ akademische Bestätigung |

**P0-Website-Gate:** W01, W02, W05, W06 müssen vor großer Navigation-/Datenintegration abgenommen sein. Ein fehlender Browser-Test ist `not_assessed`/offen, nicht erfolgreich.

## B · GPT prüft Daten-/Forschung-Claude (DATA-REVIEW; 10 Vektoren)
| ID | Vektor | Minimum / reproduzierbarer Test |
|---|---|---|
| D01 | Provenienz/No-Loss | Source-IDs, Originaldaten, Prüfsummen, Versionen, keine stille Fusion / keine beschädigten historischen IDs |
| D02 | Schema/Typisierung | Validiertes Schema mit kontrollierten Vokabularen, Typen, Pflichtfeldern und Migration / Aliasregeln |
| D03 | Integrität/Referenzen | Eindeutige IDs, referentielle Integrität, Duplikat-Crosswalks, Versionskonflikte und Negativfälle dokumentiert |
| D04 | Quellenprüfung | Digitaler Zugriff, dokumentierter Zugriffsversuch, Handprüfung und nur Nils digital geprüft getrennt; Claim-Fundstelle überprüfbar |
| D05 | Mathematische Semantik | A/B/C/G und Originalachsen T1/T3/T5 nicht vermischt; 27 Adressen nicht mit bewiesenen Beziehungen gleichgesetzt |
| D06 | Reproduzierbarkeit | Reale Skripte/Tests, Umgebung und Inputversion, erwarteter vs. beobachteter Output, Baseline und Gegenprobe |
| D07 | Evidenz-/Statusgenauigkeit | Beweis, Modellrekonstruktion, Simulation, empirischer Befund und Hypothese differenziert, keine erfundenen Testerfolge |
| D08 | Prompt-Qualität | Prompt-/Agent-/Meta-Verträge, Eingaben, Rollengrenzen, Testlauf und Redaktionsstatus je Prompt getrennt |
| D09 | Web-Schnittstellenfähigkeit | Datierte, reduzierte, rechtlich freigegebene JSON-Lesesicht für `docs/data/`; Schema-/Status-Versionsbindung und Änderungsnachzug |
| D10 | Sicherheit und Änderungsgrenzen | keine privaten Originale in `main`, keine Datenüberschreibung fremder Owner, Berechtigungen/Rechte geprüft |

**P0-Daten-Gate:** D01, D02, D04, D05 und D10 vor dem öffentlichen Import/automatischem Website-Nachzug. D06 und D07 vor wissenschaftlicher Ergebnisfreigabe.

## C · Gemeinsame Basics und Prüfsequenz
1. **Objekte identifizieren:** Originaldatei, Source-ID, Claim-ID, Task-ID, Test-ID, Prompt-ID, Commit und aktueller Owner. Die letzte bekannte Version ausdrücklich nennen.
2. **Nicht stillschweigend umdeuten:** drei 3×3-Matrizen, A/B/C/G, historische Null-/Zyklus-/Einheitsmatrix, neutraler Raum und fachwissenschaftliche Semantik getrennt halten.
3. **Status unabhängig halten:** Zugriff, Beleg, wissenschaftliche Evidenz, tatsächlicher Softwaretest, tatsächlicher Prompt-Probelauf und publizistische Freigabe.
4. **Nachvollziehbar prüfen:** mindestens ein Positivtest, ein Negativ- oder Grenztest; die andere KI versucht den Befund zu reproduzieren.
5. **Konflikte früh melden:** nicht automatisch gleichzeitige Arbeit an `docs/` und `forschung/register/` zusammenführen; insbesondere die zwei konkurrierenden Navigationsskripte und 16 Konfliktseiten.
6. **Gegenseitige Antwort:** Claude kommentiert die Vektoren, GPT bestätigt/beanstandet konkret; erst danach ein beiderseits signierter Zyklusabschlussbericht.
7. **Dreierblöcke:** Bewertungen aus drei **vollständig** abgeschlossenen Zyklen vergleichen; nach Zyklen 3, 6, 9 eigene Analysen, danach Nils-Entscheidung und optional bis 12.

## D · Vier P0-Arbeitspakete jetzt
**P0-X1 (Claude):** Quellenstatus- und Claim-Schema mit fünf realen Beispielrecords; Validator samt negativem Beispiel und Bericht liefern.
**P0-X2 (GPT):** vorhandenen Navigationskonflikt ohne Merge reproduzierbar inventarisieren; 16 Konfliktseiten und vier geschützte Abschnitte; Nils Entscheidung über Navigationslayout herbeiführen, keinen Inhalt entfernen.
**P0-X3 (Claude):** Version-/Dateimanifest und 27-Logikfeld-Original-Crosswalk mit Quellen- und Digitalprüfstatus; noch keine Umdeutung.
**P0-X4 (beide):** dasselbe Modus-ponens-/Gegenmodell als *wissenschaftlichen* Test und als eigenständigen *Prompt*-Test prüfen; beide Befundarten separat dokumentieren.

## E · Übermittlung und Abnahme
Claude liefert `forschung/koordination/zyklen/KI-2026-11-03-001/CLAUDE_REVIEW_WEBSITE.md`, möglichst mit Vektor W01–W10 und SHAs der untersuchten Seiten. GPT liefert `GPT_REVIEW_DATEN_VORLAEUFIG.md` und nach der CLAUDE-Lieferung die verbindliche `GPT_ANTWORT.md`. Beide arbeiten nur in ihren Zuständigkeitsbereichen.
**Verlangte Claude-Rückantwort:** Vektorvorschlag akzeptiert / präzise Änderungswünsche, Liste nachweislich geprüfter Website-Dateien, P0-Risiken, Referenzen, und mindestens ein konkret testbarer Verbesserungsvorschlag.
**Nicht verwechselt werden:** ein erster Review und eine Empfangsbestätigung sind noch kein vollständiger gemeinsamer Zyklus.
