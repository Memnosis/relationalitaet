# KI-Tensor v6.8: Karten, Bestand, Abhängigkeiten

100 Fachkarten aus v67_kernatlas_fachkarten maschinell gerendert (drei Achsen, 27 Positionsraum, Fachmodell, Formeln, Messgrößen, Quellenherkunft, offene Prüfpunkte). 1.072 Glossarbegriffe mit Status exportiert. 14 bestandsorientierte Kennzahlen, 13 Quell-/Formel-/Glossar-/Relations-/Tensor-/Karten-Abhängigkeiten und 100 Quellprüfaufträge in der erhaltenen SQLite-Datenbank.

Technisch verfügbar: reproduzierbares Buildskript `build_v68.py`, ZIP `KI_Tensor_Karten_Inventar_v6_8_NoLoss.zip` mit `codebuch_v68.sqlite`, `karten/*.md`, Manifest/Hashes, CSVs.

**Einschränkungen:** 100 Karten sind keine 100 wissenschaftlich zertifizierten Tensoren. Die Übergaberegeln sind gespeichert, aber noch nicht als Hintergrund-Event-Worker/CI implementiert. Die historischen Quellenregister zählen verschiedene Dokumentarten und Versionen, keine deduplizierten wissenschaftlichen Papers. Die DLMF-Formelakten (7.622) sind mathematische Formeln, nicht 7.622 Papers. Separate SOULution-Atlasdaten sind noch nicht als eigene lokale Tabellen eingebunden.

Nächster Schritt: DOI-/Titel-/Versions-Deduplizierung, Aktualisierung betroffener Karten bei neuen geprüften Quellen und Definitionen, Verbindung zum externen Operationalisierungsatlas.
