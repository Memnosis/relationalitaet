# No-Loss-Importaudit: drei wiederbereitgestellte KI-Tensor-Archive
Stand 2026-11-03 · Datenquelle: drei im Chat erneut hochgeladene ZIP-Dateien · Status: **Dateianalyse**, nicht GitHub-Import der Binärbestände.

## Tatsächlich geprüfte Archive
| Upload | ZIP-Einträge | verschachtelte ZIPs | unkomprimierte Bytes | Integrität |
|---|---:|---:|---:|---|
| KI_Tensor_Gesamtprojekt_v15_4_No_Loss(4).zip | 215 | 37 | 19.408.770 | CRC OK |
| KI_Tensor_v17_3_No_Loss_NEU(3).zip | 8 (inkl. Verzeichnis) | 2 | 7.129.633 | CRC OK |
| KI_Tensor_NoLoss_Gesamtstand_v4_2(2).zip | 56 | 51 | 60.270.473 | CRC OK |

Das v4.2-Paket enthält `originalarchive/KI_Tensor_Gesamtprojekt_v15_4_No_Loss(2).zip` (5.359.149 Bytes) mit identischem SHA-256 wie der gesonderte Upload v15.4: `3945edd1e7df2d66eb50eb73708ba9bc08a68da12385b9d765c5b2389f7aa6b6`. Im v4.2-Paket gibt es kein v17.2-Archiv auf der obersten Einlagerungsebene; v17.3 ist als weitere Entwicklungsreihe separat zu integrieren.

## Maschinenlesbarer Ist-Bestand in v4.2
Datei: `daten/codebuch_vereint_v40.sqlite` (11.010.048 Bytes).
Tatsächlich gezählte Tabellen:
- `v115__v107_tensorgrundgerueste`: 103
- `v115__v107_trinitaeten`: 309
- `v115__v107_feldadressen`: 2.781
- `historisch_trinitaten`: 309
- `glossar_v154`: 1.072
- `operator_relations`: 4.645
- `axis_source_links`: 6.225
- `original_triplets`: 675
- `discovery_addon`: 921
- `historisch_formeln`: 104
- `crosswalk`: 309
- `tensor_candidates`: 3
- `tensor_fields`: 81
- `source_archives`: 45

Achtung: Mehrere dieser Tabellen sind historische Versionen / doppelte Sichten. Zeilensummen nicht zu Zahl eindeutiger Fachobjekte addieren; 3 Tensor-Kandidaten und 81 Felder sind keine wissenschaftlich bestätigten Tensorbeweise.

## v17.3: konkret neuer Inhalt
- `v17_3/vorhersage.py`: ein reproduzierbar zu testender Vorhersage-Demonstrator.
- `v17_3/test_ergebnisse.csv`: laut Dokumentation 100 Seeds mit je zwei Schaltzuständen.
- `v17_3/ergebnis.json`: archivierte aggregierte Versuchswerte, in dieser Auditfassung nicht neu berechnet.
- `v17_3/CODEBUCH_NACHTRAG.md`: Hypothesen und Einschränkungen, ausdrücklich kein Beleg für allgemeine Intelligenz.
- Zwei verschachtelte historische ZIPs mit v17.2 und kompakter Ergänzung; äußere ZIPs und die eingebettete v17.2-ZIP wurden CRC-geprüft.

## Import- und Kombinationsregeln
1. Originalarchive unverändert versionieren, mit SHA-256; nicht die fachlichen Inhalte überschreiben.
2. v4.2-SQLite als vorhandene maschinenlesbare Ausgangsbasis verwenden, nicht die Tabellen neu ausdenken.
3. v15.4 als bereits bytegleich eingebettet deduplizieren.
4. v17.3 ergänzend importieren, mit eigenen Vorhersage-Skill-, Test- und Tensor-Kandidaten-IDs.
5. Quellen, Glossar, Achsen, Relation, Feld, Test, Skill, Prompt und Publikation über stabile IDs verbinden.
6. Historische Zeilen, eigene Rekonstruktion und getestete Beweise strikt getrennt halten.
7. GitHub-Datenimport erst nach Schema-/Lizenz-/Größen-/Sensitivitätsprüfung; dieses Markdown ist nur das Audit, nicht die Binärübertragung.

## Nächste konkrete Abnahme
- SQLite-Schema in kanonische Registertabellen mit Historienbezügen übersetzen.
- Differenzen zwischen vorhandenen Versionsfamilien auswerten.
- 27 priorisierte Feldakten und 12 Relationspositionen quellenbezogen prüfen.
- v17.3-Test unter dokumentierter kontrollierter Ausführung wiederholen und mit fairer Regelbaseline vergleichen.
- Automatischen Nachzug in Website, Glossar, Quellen und Prompt-Export testen.
