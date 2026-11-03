# Mitmachaufgaben: Ausführung vor Prompt-Delegation

**Testserie:** 2026-11-03 · **Branch:** `integration/soulution-shared-core-2026-11-03` · **Status:** sechs Fachaufgaben teilweise ausgeführt, ein eigener Geo-M1-Meilenstein teilweise ausgeführt. Kein Merge in `main`.

## Problem der bisherigen Taskkarten
Die Formulierung **„Entwickle einen Prompt für …“** produziert erst eine weitere Anweisung. Wenn Quellen, Quellcode und Testverfahren bereits verfügbar sind, muss die Engine stattdessen zuerst **selbst ausführen**, dann **prüfen** und nur den verbleibenden, präzise beschriebenen Bedarf als Mitmachaufgabe weitergeben.

### Neue Ausführungsreihenfolge
1. Task-ID und Ergebnisvertrag lesen, bereits existierende Daten und Skills suchen.
2. Quellenzugriff und Eingabetyp prüfen; vorherige gültige Nachweise wiederverwenden.
3. Vorhandene Funktionen mit echten, reproduzierbaren Eingaben ausführen.
4. Positive Tests, Gegenproben, Dokumentversion und bekannte Grenzen protokollieren.
5. Teilresultate in gemeinsamen Registern ablegen; nie als Gesamtabschluss ausweisen.
6. Nur **Restaufgabe** mit konkreter fehlender Quelle, Eingabe, Test und Abnahme veröffentlichen.
7. Erst bei begründeter Forschungsfrage einen Optimierungs-/Meta-Prompt ergänzen.

## Durchgeführte Serie

| ID | Was selbst ausgeführt wurde | Ergebnis | Warum nicht vollständig abgeschlossen? |
|---|---|---|---|
| WEB-GLOS-01 | Web-Glossar aus Git gelesen, Definitionen, Codes, IDs, Quellen-/Redaktionsstatus validiert, Webansicht verbessert | 12/12 Datensätze strukturell geprüft, 12 stabile Anker | Historische 1.008-Zeilen-CSV aus v15.4 nicht in Git; 1.072 ist ein separater historischer Inventarstand. Bibliotheksdatei durch Suchindex auffindbar, aber Rohbyte-Materialisierung abgewiesen |
| WEB-CODE-01 | Aus zwölf vorhandenen Begriffsakten einen typisierten Codebuchindex mit eigenem HTML-Viewer erzeugt | 14 Typcodes, 12 geprüfte *strukturelle* Typverweise; Graph mit JSON-Akte | Historisches Gesamtkodebuch und geprüfte Relation-IDs nicht importiert |
| GEO-OPS-01 | Historisches Geo-KI-v0.4-Modul und seine 14 Originaltests erneut ausgeführt, fünf Tests für Verkettung, Inverse, affine Äquivalenz und Negativfälle ergänzt | 19/19 bestandene Softwaretests | Weitere Operatorfamilien und robuste Geometriefälle offen |
| GEO-M1 (separates Register) | 2D-Rotationsmodell numerisch rückgeprüft und denselben Fall als SVG und JSON ausgegeben | Teilweise End-to-End: Eingabe → Operator → Nachweis → SVG/JSON | Noch keine universelle typisierte SVG-Exportpipeline und keine vollständige semantische Rückrekonstruktion |
| KOMP-01 | Physik-Kompressionsbenchmark mit realem lokalem Code wiederholt | 7 Modellakten, 32 Prüfresultate, exakte Rückkodierung; 3062 B JSON, 2441 B Wörterbuch; gzip 1236 B Original vs. 1243 B Wörterbuch | Der einfach verdichtete Bestand ist *nicht* besser als gzip; keine Tensorfunktion validiert |
| VIS-01 | Exakt 27 Feldadressen generiert, eindeutige IDs und Rückadressierung geprüft, barrierearm beschriebenes SVG erzeugt | 4/4 Strukturtests, 27/27 Positionen | Strukturgraph ist keine fachliche Tensorprüfung; Relationsvisualisierung offen |
| MINI-OBS-01 | Synthetischer unabhängiger Referenzbeobachter auf absichtlich fehlerhaften Integer-Skill angewandt | 10.000 Eingaben, 588 absichtliche Fehler, 588 erkannt, keine falsch positiven; Mehraufwand protokolliert | Test besitzt Prüf-Orakel; kein autonomes Lernen, keine universelle Fehlererkennung, Zeitkosten nur Mikrobenchmark |

## Messung, Nachweise und Grenzen
- `docs/data/glossar-kern.json` ist ein **12er Vorschau-Register**; die Einträge sind redaktionell, nicht quellenvalidierte historische Glossarbegriffe.
- `docs/data/codebuch-web-index.json` ist ein **Web-Crosswalk**, kein importiertes Gesamt-Codebuch.
- `forschung/geoki/v0_4/tests/test_composition_extension.py` reproduziert die fünf zusätzlichen Tests; v0.4-Altstand bleibt erhalten.
- `forschung/website/ausfuehrung/GEO_OPS_M1_TEST_V01.json`, `VIS27_STRUKTURTEST_V01.json`, `MINI_OBS_TEST_V01.json` sind maschinenlesbare Testzusammenfassungen.
- `forschung/minimal-ki/beobachter-v0_1/TEST_MINIOBS_SYNTHETIC.py` ist ausführbar; das Verhältnis der Mikro-Laufzeiten ist **nicht** als zuverlässige Leistungskennzahl generalisierbar.
- Der Kompressionstest kommt aus dem vorhandenen Physik-Pilot `SOULution_Physik_Tensor_Vorpruefung_v03.zip` im Gespräch. Die ursprünglichen Modelldateien liegen derzeit nicht vollständig als Git-Codebestand vor.
- `docs/assets/media/tensor_27_structure_only.svg` bezeichnet die 27 Positionen bewusst als **nicht wissenschaftlich belegte Inhalte**.
- `docs/mitmachen.html` zeigt Teilresultate, Restaufgaben und Nachweislinks neben ursprünglichen Meta-Prompts. **Die GitHub-Pages-Website läuft auf `main`; Branch-Änderungen sind noch nicht live.**

## Noch nicht selbst abgeschlossen: Priorität für weitere Serien

| ID | Warum nicht jetzt abgeschlossen? | Kleinstmöglicher nächster Selbsttest |
|---|---|---|
| HARV-01 | DLMF-v3.0–v3.5-Originalarchive und Datensatz-Versionen als `local_only` markiert | Eine echte Versionsdatei verfügbar machen, Signaturen zählen und Deltas mit Quellen testen |
| HARV-02 | Wissenschaftsmining-v2.7 und Codebuch-v3.7/v3.8-Originale nicht als ausführbares Paket eingebunden | Kleinsten historischen Verarbeitungs-Schritt mit Originaldatensatz isoliert erneut ausführen |
| HARV-03 | Physikbibliotheken teilweise lokal getestet; Qiskit/Cirq/PennyLane/QuTiP und deren Lizenzen/Versionen nicht als komplette Testmatrix bearbeitet | Je ein vorhandenes, versionsgenaues Operatorbeispiel mit Gegenprobe |
| HARV-04 | Korpusdownloads, Lizenzangaben und Abdeckung nicht als kontrollierte Auswahl vorbereitet | Eine frei verfügbare Sprachquelle mit vollständigem Metadatensatz testen |
| HARV-05 | Dreierbeziehungen müssen fachwissenschaftlich begründet werden | Eine belegte Familie mit Träger, Operator, Rückrechnung und Gegenbeispiel gegen das historische Register prüfen |
| HARV-06 | Mehrere externe Skill-/API-Kataloge, unterschiedliche Authentisierung und Nutzungsbedingungen | Einen vorhandenen Katalog mit Format, Lizenz, Aufruf und Test protokollieren |
| KOL-01 | Identische Aufgaben an mehrere tatsächlich verbundene Modelle/Agenten zu vergeben ist noch nicht möglich | Zwei vorhandene ausführbare Umgebungen mit identischem Datensatz und Prüforakel vergleichen |

## Strukturelle Konsequenz
**Task → Verfügbarkeit prüfen → existierende Skillfunktion ausführen → Ergebnisakte → Gegenprobe → Restaufgabe**. Die restlichen Prompts sind keine Misserfolge. Sie sind nur dann sinnvoll, wenn sie auf einen dokumentierten Blocker oder eine neue, fachlich offene Hypothese zielen. Ein erfolgreich getesteter Skill kann auf der Mitmachseite weiter als Vertiefung erscheinen, aber nicht als unverrichtete Grundaufgabe.

## Offene Qualitätssicherung
Einen realen GitHub-Pages-Browser- und Mobiltest sowie den vollständigen historischen Glossar-Import liefert diese Serie noch nicht. Die Codebuch-Webansicht ist mit den zwölf zur Verfügung stehenden Webbegriffen testbar; die vollständige wissenschaftliche Datenintegration bleibt offen.
