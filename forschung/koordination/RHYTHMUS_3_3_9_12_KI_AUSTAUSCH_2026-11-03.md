# Zwei-KI-Austausch: Dreieranalysen und Entscheidungsrhythmus

**Stand:** 2026-11-03 · **Autorentscheidung:** Nach je drei *vollständig* bestätigten Austauschzyklen eine Analyse; nach drei Analysen neu entscheiden; fakultativ bis zwölf Zyklen.

## Verbindliche Definitionen

- **Voller Zyklus:** dokumentierter Auftrag + Claude-Empfang + überprüfbare Claude-Lieferung + GPT-Gegenprüfung + erneute Claude-Rückbestätigung + Abschlussbericht mit Commit-IDs und offenen Fragen. Ein `accepted` allein ist **kein voller Zyklus**.
- **Blockanalyse:** untersucht **genau drei abgeschlossene Zyklen** und alle Unterschiede zwischen Ausgangs- und Endstand. Nicht bloß die Ergebnisse der drei Berichte hintereinander kopieren.
- **Grundsatzentscheidung:** nach den drei Analysen zu Zyklen 1–3, 4–6, 7–9; Entscheidung durch Nils über Prioritäten, Rollen, Automatisierung, Abbruch, Weiterführung oder optionale Zyklen 10–12.
- **Optionaler 12er-Block:** nur nach Nils' expliziter Fortführungsentscheidung. Auch Zyklen 10–12 erhalten eine Blockanalyse; dann Abschluss-/Neuentscheidung.

## Meilensteine

| Arbeit | Wann fällig? | Pflichtartefakt |
|---|---|---|
| Jede abgeschlossene Runde | nach jeder vollständig gegenseitig bestätigten Lieferung | `forschung/koordination/zyklen/<ID>/ZYKLUSBERICHT.md` |
| Analyse A1 | nach Zyklus 3 | `forschung/koordination/analysen/ANALYSE_01_ZYKLEN_01-03.md` |
| Analyse A2 | nach Zyklus 6 | `forschung/koordination/analysen/ANALYSE_02_ZYKLEN_04-06.md` |
| Analyse A3 | nach Zyklus 9 | `forschung/koordination/analysen/ANALYSE_03_ZYKLEN_07-09.md` |
| Nils-Entscheidung | nach A3 | `forschung/koordination/analysen/ENTSCHEIDUNG_NACH_9_ZYKLEN.md` (Entwurf, erst nach Nils' Antwort als genehmigt markieren) |
| Analyse A4 – optional | nach Zyklus 12 | `forschung/koordination/analysen/ANALYSE_04_ZYKLEN_10-12.md` |
| Abschluss oder Folgeprogramm | ggf. nach A4 | `forschung/koordination/analysen/ABSCHLUSS_NACH_12_ZYKLEN.md` |

## Pflichtinhalt jeder Analyse

1. **Nachweisbasis:** exakte drei Zyklus-IDs, Git-Commitreferenzen, Ausgangs- und Enddateien, Revisionsstand.
2. **Arbeitsausgang:** Was wurde tatsächlich erfüllt, partiell erledigt, widerlegt, vertagt? Keine Fortschrittsquote nur aus neuen Task-Karten.
3. **Rollenklärung:** Claude (Daten, wissenschaftliche Quellen, Glossar, formale Tests, Promptentwicklung/-analyse), GPT (Website, Navigation, Fachseiten, Design, Integration), Nils (entscheidet echte Konflikte und Publikationsfreigabe).
4. **Qualität:** Fehler/Abweichungen, redundante Bearbeitungen, verlorene Provenienz, wissenschaftliche Evidenz, technische Tests und Prompt-Tests als getrennte Spuren.
5. **Hebelwirkung:** Welche Arbeit hat nachweislich mehrere Projekte erleichtert? Welche Architektur- und Quellenlücken bleiben?
6. **Öffentlichkeit:** Welche unabhängigen Mitmach-Aufgaben sind geprüft? Welche internen Anweisungen bleiben geschützt? Keine automatische Freigabe.
7. **Nils-Entscheidungsblatt:** höchstens die wirklich offenen Richtungsentscheidungen, jeweils Alternative, Konsequenzen, Empfehlung.
8. **Folgeblock:** klare Aufgaben, Prioritäten, Zuständigkeiten, Risiken und Abnahmekriterien.

## Automatisierung und Grenzen

Die bestehende stündliche ChatGPT-Automation `6ae9db89180c819182c0a423f2250054` ist auf die neuen Meilensteine umgestellt. Sie soll nur bei **neu nachgewiesenen** vollständigen Zyklen bzw. Analysen berichten. Der GitHub-Workflow `.github/workflows/ki-austausch.yml` validiert Statusstruktur und Pflichtnachweise; er führt keine Claude-/GPT-API selbstständig aus.

Die tatsächliche Fachausführung, Gegenprüfung und Rückbestätigung bleibt ein belegpflichtiger, expliziter Vorgang. Bei fehlenden Akten weder Zyklus noch Blockanalyse als abgeschlossen markieren.

## Aktueller Status bei Anlage
- Zyklus 001: Claude-Empfangsdatei vorhanden, `status: accepted`. Fachlieferung, GPT-Gegenprüfung und Rückbestätigung bislang **nicht** vollständig belegt.
- Drei abgeschlossene Zyklen: **noch nicht nachgewiesen**.
- Erste Dreierblockanalyse: **noch nicht fällig**.

## Zuständigkeitsverweis
- Claude-Start: [Zyklus 001](CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md).
- GPT-Websitepaket: [Nächstes Website-Upgrade](../website/WEB_UPGRADE_BUENDEL_02_TENSOR_LOGIK_2026-11-03.md).
- Koordination: [Issue #3](https://github.com/Memnosis/relationalitaet/issues/3).

## Langfristige Fortschreibung – 100 Zyklen (Beschluss 03.11.2026)
Dieser ursprüngliche 3/3/9/12-Rhythmus bleibt als **Zwischensteuerung und Autoren-Entscheidungs-Gate** bestehen. Übergeordnet gilt jetzt das [100-Zyklen-Programm](PROGRAMM_100_ZYKLEN_STUDIE_UND_BEREINIGUNG_2026-11-03.md) samt [20 reservierten Themenschwerpunkten](PROGRAMM_100_ZYKLEN_MANIFEST.json) (12 Mitmach, acht intern, vorläufig), Sicherheits-/Change-Audits nach 20/40/60/80/100 **vollständig bestätigten** Zyklen und einer DOCX-Gesamtstudie nach Zyklus 100. Eine optionale Verlängerung nach Zyklus 9 oder 12 ist **nicht automatisch genehmigt**. Operative KI-Rohgespräche sind nicht Teil der öffentlichen Website; für vollständige Archivierung ist ein wirklich privater Ort erforderlich.
