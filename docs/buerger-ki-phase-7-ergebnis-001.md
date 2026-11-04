# Bürger-KI · Phase 7 – Erste fachliche Pilotakte

**ID:** BKI-ADM-RESULT-001 · **Version:** 0.1 · **Datum:** 2026-11-04  
**Status:** Quellengebundener Redaktionsbestand + lokaler Konsistenztest; **keine juristische Freigabe, keine echte KI-Ausführung, keine FIM-API-Integration, kein unabhängiges Ergebnis-Audit**.

## 1. Nachvollziehbare Ausgangslage

Drei Verwaltungsleistungen wurden aus amtlichen Originalinformationen in eine stark reduzierte, feste Teststruktur überführt.

| Leistungs-ID | Gegenstand | Quellen |
| --- | --- | --- |
| BK-ADM-01 | Führungszeugnis, persönliche/Online-/Auslandsbeantragung | [Bundesamt für Justiz](https://bundesjustizamt.de/DE/Themen/ZentraleRegister/Fuehrungszeugnis/Fragen/Fragen_node.html?docId=259056) · [Bundesportal](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99049001001000) |
| BK-ADM-02 | Meldebescheinigung, elektronische Erteilung, regionale Kostenangaben | [§ 18 BMG](https://www.gesetze-im-internet.de/bmg/__18.html) · [Regionalbeispiel Brandenburg/Cottbus](https://verwaltung.bund.de/leistungsverzeichnis/DE/leistung/99115009001000/herausgeber/BB-126755977/region/120520000000) |
| BK-ADM-03 | Gewerbeanmeldung, Änderungen, Abgrenzung zu weiteren Erlaubnissen | [§ 14 GewO](https://www.gesetze-im-internet.de/gewo/__14.html) · [Bundesportal](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99050012104000) |

Das ist **kein vollständiger importierter FIM-Katalog** und keine regional belastbare Zuständigkeitsdatenbank. Leistungsangaben dienen hier als eingegrenzte Fachbeispiele. Originalquellen sind für tatsächliche Verfahren zu prüfen.

**Artefakte:**
- [Datensatz mit drei Leistungen, sechs Quellen-IDs und neun Fallkarten](./data/bki-verwaltung-pilot-v0-1.json)
- [Interaktive Verwaltungspilot-Seite](./buerger-ki-verwaltungspilot.html)
- [Allgemeiner Experimentierplan](./buerger-ki-experimentierlabor.md)

## 2. Testanordnung

- S0: erste Regel des Leistungsbereichs auswählen (bewusst naive Baseline).
- S1: Regel auswählen, deren Anfrageanlass zum synthetischen Testfall passt.
- S2: S1 und zusätzliche Prüfung, ob die zitierte Quellen-ID im Datensatz existiert.

**Ergebniskriterien:** Sollregel richtig gewählt und Quellenverweis intern referenziell gültig. **Nicht getestet** wurde, ob die Quellen alle juristischen Voraussetzungen vollständig stützen oder der Rat lokal passt.

## 3. Tatsächlich durchgeführter Register-Konsistenztest

Die im JSON enthaltenen neun Fälle und drei Strategien wurden gegen ihre hinterlegten Sollregel-IDs ausgewertet (insgesamt 27 Strategie-Fall-Paare):

| Strategie | Richtige Sollregel-ID | Bekannte Quellen-IDs | Interpretation |
| --- | --- | --- | --- |
| S0 | **3/9** | **9/9** | Absichtlich schwache Baseline: gleiche Standardregel ignoriert Sonderfälle |
| S1 | **9/9** | **9/9** | Im selbst erstellten Regelbestand konsistente Fallzuordnung |
| S2 | **9/9** | **9/9** | Ergänzende Quellen-ID-Konsistenzprüfung; noch keine unabhängige fachliche Gegenprüfung |

Die 9/9 der Strategien S1 und S2 sind **kein Beweis von 100 % fachlicher Zuverlässigkeit**, weil Sollantworten und Regelentscheidungen derselben konstruierten Referenzstruktur entstammen. Übertragbarkeit auf reale Bürgerfragen ist nicht nachgewiesen.

## 4. Wertvolle negative Befunde

1. S0 kann sämtliche Quellen-IDs formal korrekt nennen und trotzdem die falsche Regel auswählen: **Quellenexistenz ist nicht Quellenbelegtreue**.
2. S2 prüft bisher nur Quellen-ID-Existenz und leistet keine unabhängige semantische oder rechtliche Prüfung.
3. Lokale Bearbeitung/Zuständigkeit kann sich nach Region unterscheiden; ohne orts- und zeitbezogene Fachdaten keine belastbare Einzelbehörden-Nennung.
4. FIM-/PVOG-Standards sind als Anschlussziele bekannt, aber kein Live-Datenadapter wurde implementiert.
5. Ein echter LLM-Strategievergleich, Browser-End-to-End-Lauf und unabhängiges Expertenreview sind weiterhin offen.

## 5. No-Loss-Crosswalk

`Bürgerfrage → BK-ADM-Leistung → Originalquelle → Regel-ID → Testfall-ID → Strategie → beobachtete Zuordnung → Abweichung → Skill-Kandidat → Prüfung`.

Nicht verwechseln:
- **Testkorpus vorhanden** ≠ Fachkorpus unabhängig freigegeben.
- **Frontend im Repository vorhanden** ≠ Browser-End-to-End getestet.
- **Konsistenztest ausgeführt** ≠ echte LLM-Strategien validiert.
- **Verwendbare Quellen-URL** ≠ automatischer Datenimport.

## 6. Nächste Priorität

Den vorhandenen Bestand durch mindestens eine **versionierte echte amtliche Leistungsdatenquelle** mit dokumentierter Schnittstelle, kontrollierter Geltung und korrekter regionaler Zuordnung ersetzen bzw. ergänzen. Vor einem KI-Vergleich Goldstandards unabhängig redaktionell überprüfen und Gegenbeispiele ergänzen.

**Fortschritts-Gates:** G01–G03 bleiben dokumentiert; G04 (quellengeprüftes Fachkorpus) ist **in Arbeit**, G05–G10 offen. Gesamtzähler bleibt **3/10**, bis die unabhängigen fachlichen Abnahmekriterien erreicht sind.
