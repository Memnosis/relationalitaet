# B3/B4 – Harvesting, Codebuch, Glossar, Quellen: Ergebnisbilanz (01.11.2026)

## Bereits geleistete Forschung und genaue Fundorte

| Arbeitsfeld | Gefundenes Ergebnis | Historischer Fundort | Noch zu überprüfen |
|---|---|---|---|
| Formel-Harvesting | DLMF-Formeln als strukturierte JSON-Datensammlung; Gesamtdatei 29.168.452 Byte | `KI_Tensor_NoLoss_Gesamtstand_v4_2(1).zip!originalarchive/One-Json-Object-Per-Math-Exprression.zip!dlmf-chapters-OneJsonObjectPerMathExpr/oneJsonFileForAllDLMF/dlmf.json` | Anzahl tatsächlich ausgewerteter Formeln und Relationsnachweise |
| Formel → Trinität | Historische Pipeline und Kandidatenarbeit | `TDR01_Formel2Trinitaet_v1_4.zip` in verschachtelten Archiven | Ausgabedateien/Quellenanker/Validierung je Trinität |
| 400 Formeln / 1000 Trinitäten | Historische Ausbauarbeit | `TDR01_Ausbau_400_Formeln_1000_Trinitaeten_v2_6.zip` | Zahlen im Dateinamen sind keine bestätigten gültigen Ergebnisse |
| Wissenschaftsmining | Fachübergreifende Ernte- und Verknüpfungsarbeit | `TDR01_Wissenschaftsmining_v2_7_NoLoss.zip` | Ergebniszeilen, Konflikte, fachliche Prüfbarkeit |
| Mathematische Analyse | 107 Profile und 5.671 Paarpositionen | `KI_Tensor_Mathematische_Gesamtanalyse_v3_1/TENSOR_107_MATH_SIGNATURES.csv` und `PAIRS_5671.csv` | tatsächliche isomorphieerhaltende Abbildungen |
| Codebuch-Objekte | IDs für SRC, MOD, TRI, TEN, REL, OPR, SKL, TST | `KI_Tensor_9_Publikationen_Algebra_Codebuch_Tests_v0_1.zip!KI_Tensor_Publikationssystem_v1/CODEBUCH.md` | Fusion der historischen Objektdefinitionen |
| Codebuch-Import v17.3 | 11 Tensor-Slots, 297 Feldadressen, technische DB-Prüfungen bestanden | `KI_Tensor_Codebuch_v17_3_Import_NoLoss_2026-10-31(1).zip` | 0 Rohdatensätze, 0 Glossareinträge in der geprüften Import-DB; historischer Vollimport nicht abgeschlossen |
| Glossar | **1.072** annotierte Datensätze, davon **9** als redaktionell geprüft und **1.063** offen | `KI_Tensor_Gesamtprojekt_v15_4_No_Loss(3).zip!KI_Tensor_v15_4_Gesamtprojekt_Audit/Glossar_1072_v15_4_qualitaetsannotiert.csv` | Quellenkonflikte und externe Einzelvalidierungen |
| Quellen / Relation | 174 Objekte, 216 Quellkanten, 27 Auditzellen, 18 Relationsclaims gemäß Eigenmetriken | `KI_Tensor_Quellen_Relationsaudit_v0_8.zip!METRICS.json` | Linkstärke / Aussage- und Belegprüfung |

**Wichtige Korrektur:** Das zuvor präsentierte Glossar mit 1.008 Einträgen ist eine historische Zwischenfassung. Die neueste konkret geprüfte v15.4-Quelldatei enthält 1.072 Einträge samt Definitions- und Quellenprüffeldern.

**Unterscheidung der Befunde:** Ein geerntetes Formelobjekt ist keine validierte Trinität. 216 Quellkanten sind keine 216 unabhängig bestätigten Beweise. 5.671 Tensorpaarpositionen sind keine nachgewiesenen Isomorphismen.

## Stand der Integration

**Erledigt:** Original-Dateifundorte aufgelöst, Glossar v15.4 ausgelesen und lokal als vollständige CSV plus JSON gesichert, Quellen-Audit-Metriken gegen die Originaldateien geprüft, bestehende Codebuch-Schema- und Importstände getrennt dokumentiert.

**B3 noch offen:** Batchweise Zusammenführung aller historischen Ernteausgaben mit Quell-IDs, Hashes, Duplikaten, konkreten Trinitätkandidaten und Auswertungs-/Falsifikationsstatus.

**B4 noch offen:** Vollständige Datenübernahme in die versionierte Codebuch-Datenbank samt Konfliktprotokoll sowie Einzelprüfung der 1.072 Glossareinträge und ihrer Fachquellen.

Die Ausgangsarchive bleiben unverändert. Der vollständige v15.4-Glossar-Export wurde als lokales Integrationspaket erstellt; im Git liegt zunächst diese geprüfte Ergebnisbilanz.
