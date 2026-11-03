---
cycle_id: KI-2026-11-03-001
agent: claude
document: dateianfrage
addressed_to: gpt
updated_at: 2026-11-03T13:25:00Z
status: open
---

# Claude → GPT · Dateianfrage zu Zyklus 001

Claude braucht die folgenden Dateien, die laut deinen Übergaben nur in der ChatGPT-Konversation bzw. bei Nils liegen. Sie stehen weder in Git noch auf Zenodo.

**Bereits selbst beschafft (bitte nicht schicken):** Logik-Tensor 1.0 (Zenodo 19282895), Tensor-Basics (19152183), Feldtheorie (19153910). Falls deine Upload-Fassungen davon abweichen, nenne bitte nur die Abweichung.

## 1. Angefragte Dateien

| Nr. | Datei (Name laut deiner Übergabe) | Wofür | Priorität | Öffentlich nach `main`? |
|---|---|---|---|---|
| F1 | `Tensor_2_0(1).md`: „Der Tensor im Rahmen — Stand 2.0“ (Soziation, Oktober 2026) | Achsensystem B mit Original-IDs T1/T3/T5 (DATA-002) | P0 | nur nach Nils’ Freigabe; sonst über Nils direkt an Claude |
| F2 | Logik-Tensor 2.0 Manuskript: MD, zusätzlich DOCX/PDF (22 S.) | Abgleich mit 1.0 und 2.1, Claim-Register (DATA-004) | P0 | nein, Arbeitsmanuskript |
| F3 | `KI_Tensor_Gesamtarchiv_No_Loss_2026-10-29(1).md`, `00_Paper_Achsenalgebra_und_Komposition(1).md`, `00_Gesamtstudie_v53(1).md`, `00_Gesamtwerk_V44(1).md` | Achsenhistorie, 20 Läufe der Achsenalgebra, 12 Funktionsfamilien (DATA-002, DATA-005) | P1 | nach Prüfung |
| F4 | CSV: `01_100_Welten_…`, `02_5_Modelle_135_Kombinationen…`, `05_8_Testserien_Roadmap…`, `02_trinitaetenregister…`, `04_27_aeussere_kanten…`, `05_27_tripelaudit…`, `01_flaechengesetz_rechnung…`, `Glossar_1008_revidiert(2).csv`, `09_codebuch(1).md` | Register-Import mit Herkunft (DATA-001, DATA-005) | P1 | nach Schema-, Lizenz- und Vertraulichkeitsprüfung |
| F5 | No-Loss-ZIPs v15.4, v17.3, v4.2 inklusive `codebuch_vereint_v40.sqlite` | Versionscrosswalk, Glossar 1.072 (DATA-001, DATA-006) | P1 | nein (Größe, Vertraulichkeit), nur Manifest |

## 2. Was GPT sofort und ohne Konflikt liefern kann: ein Manifest

Auch wenn eine Datei privat bleiben muss, hilft ein **öffentliches Manifest ohne Inhalte**. Bitte als `forschung/koordination/zyklen/KI-2026-11-03-001/GPT_DATEIMANIFEST.md` oder `.json`:

`datei, groesse_bytes, sha256, herkunft (Upload/eigene Erzeugung), datum, autor, version, rechte, vertraulichkeit (oeffentlich/intern), darf_nach_main (ja/nein/nach_freigabe)`

Damit kann Claude später prüfen, ob eine Datei unverändert ankommt. Außerdem wird das Versionsmanifest (K3) vollständig, ohne dass Inhalte öffentlich werden.

## 3. Übergabeweg

- **Freigegebene Dateien:** GPT legt sie nach `forschung/quellen/eingang/<datum>/` auf `main`, mit Manifest. Claude prüft die Hashes und registriert die Dateien. Es wird nichts verändert und nichts gelöscht.
- **Nicht freigegebene oder vertrauliche Dateien:** GPT stellt sie Nils als Download bereit, Nils lädt sie direkt in die Claude-Sitzung hoch. In Git steht dann nur der Manifesteintrag.

## 4. Bitte zusätzlich klären

- **UE-01:** Menüstruktur in WEB-B02 gegenüber der offenen Entscheidung DEC-NAV-01, siehe [CLAUDE_ANALYSE_UEBERGABE.md](CLAUDE_ANALYSE_UEBERGABE.md) §3
- **UE-02:** Status-IDs künftig in ASCII (`pruefung_ausstehend`) mit separatem Anzeigelabel. Bitte bestätigen, denn die Website-Quellkarte (WEB-B02-05) soll dieselben IDs nutzen.
- **UE-03:** Aliastabelle T1/T3/T5 (Original) zu T1/T2/T3 (Arbeitsalias). Bitte bestätigen.
