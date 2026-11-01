# Forschungsbestände · Codebuch, Glossar, Quellen und Harvesting

Stand: 2026-11-01. Dieses Register ist ein **Wegweiser** zu nachgewiesenen historischen Beständen, kein neu erfundener Forschungsstand.

| Bereich | Gesicherter Originalfund | Prüfbefund | Git-Stand |
|---|---|---|---|
| Codebuch-Objektsystem | `KI_Tensor_Publikationssystem_v1/CODEBUCH.md` | Schema SRC/MOD/ELM/TRI/TEN/FLD/REL/OPR/TH/TST/PRF/SKL/PUB/VER; keine vollständige historische Fusion | Dieser Wegweiser |
| Codebuch-Import | `KI_Tensor_Codebuch_v17_3_Import_NoLoss_2026-10-31(1).zip` | 297 Adressen, 11 vorläufige Tensor-Kandidaten; Glossar/Sources/Trinitates/Skills im geprüften SQLite jeweils 0 | Import-ZIP lokal |
| Glossar | `KI_Tensor_Gesamtprojekt_v15_4_No_Loss(3).zip/Glossar_1008_revidiert.csv` | 1.008 Zeilen, davon 935 als Definitionslücke markiert, 46 redaktionell ohne Einzelnachweis, 27 donor-nah aber nicht fachvalidiert | Original lokal |
| Größeres historisches Glossarinventar | No-Loss-Register | Historisch 1.072 Einträge vermerkt; Abgleich zu 1.008-Zeilen-Fassung offen | Lokal |
| Quellen | `KI_Tensor_Publikationssystem_v1/QUELLEN.md`, `KI_Tensor_Quellen_Relationsaudit_v0_8` und v11–v13 Quellenregister | Quellenliste und Quellenrelationen verstreut; keine vollständige DOI/Version/Feld-Matrix | Teilregister lokal |
| Harvesting | Historische `TDR01_Wissenschaftsmining_v2_7_NoLoss.zip`, `TDR01_Formel2Trinitaet_v1_4.zip`, DLMF-/Formelernte-Pakete | Arbeit wurde gemacht; Gesamtresultat und Dubletten-/Nachweisstatus sind noch zu konsolidieren | Verschachtelte Archive lokal |
| Tensorprüfung | Mathematische Gesamtanalyse v3.1 | 107 Prüfprofile, 5.671 Paarpositionen | Forschungsarchive lokal |

## Nächster Integrationsschritt

1. Harvesting-Originale und importierte Kandidaten unter stabilen IDs abgleichen; **nicht** neu harvesten, was bereits vorhanden ist.
2. Glossar in getrennte Ebenen indexieren: Originaldefinition, redaktioneller Stand, fachgeprüfte Definition, Quellenlink.
3. Quellen mit konkreten Aussagen/Modellen verknüpfen; bibliografischer Link allein gilt nicht als wissenschaftlicher Beleg.
4. Codebuch-Import mit No-Loss-Quellen erneut aufsetzen, Import-Batches protokollieren und konfliktfrei versionieren.
5. Erst geprüfte Datensätze kontextbezogen in die Lehrseiten übernehmen.

Das lokal erstellte Integrationspaket enthält unveränderte Kopien des 1.008er Glossars, des Publikations-Codebuchs, der Auswahlquellen und des Relationsaudits sowie einen zusätzlichen JSON-Glossarindex.
