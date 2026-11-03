# Reproduktionsstatus: vorhandene Testnachweise (03.11.2026)
**Vier neue Prüfprotokolle** wurden mit bekannten Aufgaben-IDs verbunden. Es handelt sich um technische/mathematische Checks, **nicht** um getestete oder freigegebene Mitmach-Prompts.

| Test-ID | Aufgaben | Prüfgegenstand | Beobachtung / Urteil |
|---|---|---|---|
| T-MINI-PRED-001 | KI-OPS-25, KI-GF-12 | 100 Seeds × 200 Testsituationen aus v17.3 erneut ausgeführt | Mittelwerte der Belohnung stimmen überein; archivierte Accuracy ohne Vorhersage ist 0,5043, neu berechnet 0,5044; **Abweichung dokumentiert**, exakter Reproduktionsvergleich nicht bestanden |
| T-MINI-PRED-002 | KI-OPS-25, KI-GF-12 | Gepaarte Vergleichskontexte mit einfacher deterministischer Regel | Prädiktor und Regelbaseline: jeweils −0,4993; baseline ohne Schutz −2,4965. Vorteil ist **nicht** spezifischer Beweis von KI oder universeller Vorhersagekompetenz |
| T-TENSOR-GRAPH-001 | KI-TRI-01, KI-AXIS-23, KI-TEST-08 | 27 Koordinaten, Pfad- und Hamming-Nachbarschaft, Mitte | 54 bzw. 81 Kanten; im Pfadmodell trennt die gesamte Mittelschicht; im Hammingmodell nicht; Einzelzentrum ist kein globaler Schnitt |
| T-CONF-REGISTER-001 | KI-CONF-27, KI-TEST-08 | 27 Tripelpositionen und 27 äußere Vergleichskanten als CSV | 24 formale Kombinationen, drei fachlich kommentierte Sonderfälle; Integrität der Registerstruktur bestätigt, keine QCD-Validierung |

## Nachweis- und Freigabestatus
Die Ausführung erfolgte mit den im Chat bereitgestellten Quellarchiven (v17.3, Confinement-CSV) und einem unabhängig erstellten Graph-Test. Der vollständige lokale Prüflauf samt Laufdatei und JSON-Ergebnissen gehört zur Nutzersicherung und wird nicht ungeprüft als interner Programmcode öffentlich hochgeladen.

- Der Vorhersage-Test verwendet eine deterministische Umgebung mit vollständigem Zustand und einer schwachen ursprünglichen Baseline. Die Originalschleife verwendet unterschiedliche Zufallsfolgen für die Schaltzustände. Die kleine Accuracy-Abweichung wird nicht glattgerundet.
- Die Confinement-Tripel sind **keine 27 physikalisch bewiesenen Tensorpositionen**. Die drei Sonderfälle benötigen ihr eigenes Fachmodell und gültige Näherungen.
- In keiner der vier Akten existiert ein zugeordneter ausgeführter öffentlicher Prompt mit redaktioneller Freigabe.
- Die historischen 20 berichteten Achsenalgebra-Läufe wurden mit diesem Teilpaket **nicht** wiederholt.

## Nächster Gate-Schritt
Technische Testbelege in der Aufgabenliste verlinken, ungetestete Prompt-Texte getrennt führen, ein erstes freigabefähiges öffentliches Gegenbeispiel als Pilot auswählen und die Autorenentscheidungen mit konkreten Alternativen dokumentieren.
