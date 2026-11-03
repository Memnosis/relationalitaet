# ENTWURF für Nils · Freigabe erster Logik-Tensor-Aussagen für die Website

**Status:** Entwurf nach R1. **Zuerst analysiert GPT**, erst danach geht die Vorlage an Nils. · **Erstellt:** Claude, 2026-11-03

## Für Nils (Format R3)

| Feld | Inhalt |
|---|---|
| **Worum geht es?** | Die Website darf Quellenangaben zum Logik-Tensor nur aus freigegebenen Aussagen zeigen. Bisher ist keine Aussage freigegeben, deshalb bleibt die Quellenanzeige leer. |
| **Warum jetzt?** | Die technische Lesesicht ist fertig und getestet (`forschung/register/werkzeuge/lesesicht.py`). GPT kann die Logik-Seite erst mit belegten Quellenkarten aufwerten, wenn es freigegebene Einträge gibt. |
| **Vorgeschlagener Umfang** | **35 rein dokumentarische Aussagen** aus deinem eigenen, bereits veröffentlichten Werk (Zenodo, CC-BY-4.0): 27 Feldzuordnungen, 3 Pfade, 5 Axiome. Jede sagt nur „so steht es im Original, Seite X“. Alle sind maschinell und per Sichtprüfung der Seite bestätigt. |
| **Nicht enthalten** | starke inhaltliche Thesen (Meta-Logik, Einbettung aller Logiken, Ersatz des Modus ponens): Sie bleiben „offen“ und unveröffentlicht |
| **Option a** | alle 35 freigeben → GPT kann auf `tensor-paper.html` eine belegte Feldtabelle mit Seitenangaben zeigen |
| **Option b** | nur die 27 Feldzuordnungen freigeben → Feldtabelle ja, Pfade und Axiome nein |
| **Option c** | nichts freigeben → Seite bleibt ohne Quellenkarten |
| **Empfehlung Claude** | a: Die Inhalte sind ohnehin öffentlich (Zenodo); die Freigabe betrifft nur die Darstellung mit Fundstelle |
| **Empfehlung GPT** | *ausstehend* |
| **Wenn nicht entschieden** | Die Logik-Seite zeigt weiter keine belegten Quellenkarten. |
| **Antwortformat** | „FREIGABE-LOGIK: a“ (oder b/c) |
| **Hintergrund** | `forschung/tensor/logik-claude/LOGIK_CLAIMREGISTER_V0_1.json`, `LOGIK_TENSOR_1_0_EXTRAKT_V0_1.md` |

## Für GPT (Analyse nach R1)

Bitte prüfen und in `GPT_DISKUSSION_07.md` vermerken:
1. Passt die Seitenzuordnung `forschung/register/oeffentlich/SEITENZUORDNUNG_V0_1.json` (z. B. Feldaussagen → `tensor-paper#logik-forschungsstand`)?
2. Erfüllt die Lesesicht v0.2 deine Feldliste (`GPT_DISKUSSION_02_ZENODO` §5)? Test: `forschung/register/tests/test_lesesicht.py`.
3. Deine Empfehlung a, b oder c mit Begründung.
