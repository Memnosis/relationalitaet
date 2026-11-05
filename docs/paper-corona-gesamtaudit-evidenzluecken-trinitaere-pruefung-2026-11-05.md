# Corona-Forschung: Qualitätsrevision sämtlicher Analysefamilien
**v0.1 · 05.11.2026 · ausschließlich Corona-Fachfragen, kein fachfremder Einzelinhalt**

## Prüfprinzip
Für jede Behauptung: Quelle, `published_at`, `knowledge_cutoff`, `event_date`, Originalversion, Überarbeitungen, Population, Exposition/Maßnahme, Outcome, Nenner, Lage anderer Messgrößen, Unsicherheit, Gegenbeleg und zeitgenössisch realistische Alternativen. GRADE pro definierter medizinischer Outcome-Frage, statistische Datenqualität/Provenienz unabhängig davon. Extrem Pro/Contra als Hypothesentest, nicht gleiche Evidenzgewichtung.

## Themenaudit: bisherige Schwächen
| Cluster | Bisheriger belastbarer Anker | Hauptschwäche | offener Deep Dive |
|---|---|---|---|
| Inzidenz/PCR/Dunkelziffer | RKI-Meldereihen, Serologiequellen | Testzugang, geänderte Erfassung, regionale Nichtvergleichbarkeit | Datensatz- und Versionenatlas |
| Todesursachen/Übersterblichkeit | WHO GHE/Destatis, Modellvergleiche | Referenzbaseline, ICD, Altersstandard, Meldeverzug | Sensitivitätsvergleich |
| Obduktionen | nationales COVID-Obduktionsregister, WHO-Europa | Auswahleffekte, historische Länderabdeckung | Gesamtquote und Diagnoseänderungen |
| Impfungen | EMA/PEI und Kohortenstudien | Alter, Dosis, Expositionszeit, Vorimmunität, klinischer Endpunkt | risikospezifische Nutzen/Schaden-Reihen |
| Myokarditis | Reviews/Register/zeitnahe Warnstände | Meldung versus Diagnose, Langzeit-Endpunkte und Medienclaim | Risiko je Gruppe und Zeitpunkt |
| Maskenpflicht | Cochrane, Labor/Beobachtung | individueller Filtereffekt ≠ Gesamtwirkung einer Pflicht | Länderzeitreihen und reale Compliance |
| Maskenatteste/Klassenklima | Gerichtsentscheidungen, Einzelfälle | Zahl tatsächlicher Bedarfe/Ablehnungen fehlt, keine repräsentative Klassenklimareihe | Nenner und Schulerfahrungen |
| Hitze und Masken | PPE-Surveys, kleine Crossoverstudien | Gesunde Erwachsene ≠ vulnerable ältere Menschen; Maskenanteil nicht isoliert | Hitzeexposition, Synkopen, Risikogruppen |
| Schulische Folgen | IQB/IGLU | Masken ≠ Distanzunterricht, Vortrend, soziale Auswahl | Länder- und Alterskohorten |
| Lockdowns/Kontaktregeln | historische Maßnahmenakten | Bündelüberlagerungen, freiwillige Verhaltensänderung | kausale Kontrollgruppen |
| Tests und Abrechnung | Bundesrechnungshof | Budget ≠ Schaden/Nettoverlust ≠ epidemiologischer Nutzen | Einzelzahlung/Prüfquote/Nettofolgen |
| Krankenhauskapazitäten | BMG, DIVI, Rechnungshof | gemeldet ≠ tatsächlich betreibbar, wechselnde Definition | Personal, Belegung, Transfers |
| Berufsförderung und Boni | Pflegebonus, Ausbildungsprämien | Anspruch ≠ Auszahlung; kein Berufsgruppenvergleich | COR-BER-01 vollständige Matrix |
| Warnsysteme | WHO/RKI/EMA/PEI Zeitreihen | Rückschaufehler, fehlende originaldatierte Schwellen | historischer Blindtest |
| Medien und Faktenchecks | zehn konkrete Kandidaten | keine Volltextaudits, Reichweiten/Änderungen offen | MED-001 bis 010 Versionen |
| Recht/Verhältnismäßigkeit | Gesetz/gerichtliche Akten | richterliches Ergebnis ≠ empirischer Wirkungsnachweis | Akten- und Normversionsvergleich |
| Beschaffung/Finanzrisiken | BRH/Regierungsantworten | Streitwert ≠ Schuld; Bedarf zu Beginn umstritten | Zahlungs-/Urteils-/Vernichtungskarte |
| Gesamtnutzen/Kollateralschäden | fachliche Teilakten | inkompatible Endpunkte; kein universelles Schadensäquivalent | multikriterielle Sensitivitätsanalyse |

## Querschnittlicher Benchmark-Vertrag
Jedes `measure` erhält `unit`, `numerator`, `denominator`, `period`, `region`, `population`, `method_version`, `source_revision`, `confidence_interval`, `risk_of_bias`, `knowledge_cutoff`, `comparison_guard`, `GRADE_if_applicable`. Ohne kompatible Felder kein automatischer Vergleich.
Ein medialer Wortlaut zum Datum X wird nur gegen den zum Datum X verfügbaren Nachweis bewertet; spätere Forschung bildet eigene Korrekturschicht.
Negative Evidenz und Datenlücken sind eigenständige Ergebnisakten. Kein Abwesenheitsbeweis aus nicht gefundener Quelle.

## Referenzen
- [Corona-Messatlas](./data/bki-corona-messvergleich-medienpilot-v0-2.json)
- [Vertiefung Masken](./paper-corona-maskenpraxis-hitze-befreiung-2026-11-05.md)
- [Corona-Zeitverlauf](./buerger-ki-corona-zeitverlauf.html)
- [Benchmark-Crosswalk](./paper-benchmarks-evidenz-zeitkontext-crosswalk-2026-11-05.md)
- [Historische Fallprüfungen](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/EVIDENTE_EVIDENZ_HISTORISCHE_KOHORTE_CORONA_TIEFENTEST_2026-11-05.md)

**Stand:** Gesamtinventar der Schwächen und Prüfschritte, keine Vollmetaanalyse; fachliche Evidenzgrade pro Ausgangsclaim sind noch zu berechnen.
