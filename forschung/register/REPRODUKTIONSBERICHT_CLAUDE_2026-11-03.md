# Reproduktionsbericht Claude-Prüfungen

- Zeit: 2026-11-04T00:16:50+00:00
- Commit: `de503e574908b671d700e6c37e036aa6ff92338d`
- Python: 3.13.18

| Prüfung | Skript (SHA-256, 12 Zeichen) | Exit | Ergebnis |
|---|---|---|---|
| Validator Claims (6 positiv, 7 negativ) | `forschung/register/pruefen.py` `a548882c5921` | 0 | ja |
| Logik-Aussagenregister (48) | `forschung/register/pruefen.py` `a548882c5921` | 0 | ja |
| Standard-Profile (FAIR/PROV/SemVer/DCAT) + Negativprobe | `forschung/register/profile/profile_pruefen.py` `3f0ee2714dc4` | 0 | ja |
| Formale Tests K4 (8) | `forschung/tensor/logik-claude/tests/test_formal_k4.py` `bc8f455b23cb` | 0 | ja |
| Probelauf LOGIK-PROMPT-02 (8) | `forschung/tensor/logik-claude/tests/test_logik_prompt02.py` `9b09cd69386a` | 0 | ja |
| Lesesicht v0.2 (5) | `forschung/register/tests/test_lesesicht.py` `d997491b8bec` | 0 | ja |
| PM-Status aus Nachweisen (5) | `forschung/register/tests/test_pm_status.py` `a1583fbe9b39` | 0 | ja |
| Abwesenheit R7: 10 Beiträge ohne Feedback (8) | `forschung/koordination/tests/test_abwesenheit.py` `70c4eac36f04` | 0 | ja |
| Berichtsgenerator roter Rahmen R2 (5) | `forschung/koordination/tests/test_bericht_vorlage.py` `6bd9cdbf963b` | 0 | ja |
| Gegenrechnung GR-03: 16 Zahlenketten ki-tensor | `forschung/register/gegenrechnung/kt_zahlenketten.py` `b985dca20f74` | 0 | ja |
| Gegenrechnung GR-01: 7 DLMF-Identitäten (sympy) | `forschung/register/gegenrechnung/dlmf_v6_6_gegenrechnung.py` `448ba272fd6e` | 0 | ja |
| Gegenrechnung GR-02: REV-01..08 (sympy) | `forschung/register/gegenrechnung/rev_rueckrechnungen.py` `4e6749a0284d` | 0 | ja |
| GPT-Gegenlauf LOGIK-PROMPT-02 (Kontrolle) | `scripts/gpt_logic02_independent.py` `d93bb6935ab7` | 0 | ja |

**Gesamt: alle Prüfungen bestanden**

## Nur mit öffentlicher Zenodo-PDF nachvollziehbar

1. `Logik-Tensor_1_0.pdf` von https://doi.org/10.5281/zenodo.19282895 laden, MD5 laut Zenodo prüfen.
2. `python3 forschung/tensor/logik-claude/werkzeuge/logik10_extrakt.py <pdf>` → erwartet `felder 27, felder_gefunden 27, axiome 5, systeme 7, begriffe_kap8 34, abgleich_2_1 27/27`.
3. Sichtprüfung: Seiten 3–6 und 14–20 der PDF gegen `LOGIK_TENSOR_1_0_EXTRAKT_V0_1.md`.
