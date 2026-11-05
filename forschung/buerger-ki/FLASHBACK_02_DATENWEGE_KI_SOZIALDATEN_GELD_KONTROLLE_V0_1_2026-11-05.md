# Bürger-KI – FLASHBACK 02: Datenwege, Sozialdaten-KI, Geld und Kontrollmöglichkeiten

**ID:** BKI-FB-002 · **Stand:** 05.11.2026 · **Status:** quellenbasierter Deep-Dive-Entwurf, kein Abschlussaudit zu Gebührenaufkommen, KI-Projekten oder Rechtshistorie.  
**Vorgänger:** [Flashback 01](./FLASHBACK_01_DATEN_OPTIN_OPTOUT_MELDERECHT_EPA_V0_1_2026-11-05.md) · [Neun Ausgangsfälle](./FLASHBACK_01_RECHTSVERGLEICH_V0_1.json) · [Sprachwelten-Phasen](./SPRACHWELTEN_FACHGEBIETE_DREHPUNKTE_QUELLENPLAN_V0_1_2026-11-05.json)

## 1. Methodenupgrade: Nicht bloß „Opt-in oder Opt-out“

Ein Datenweg braucht **neun getrennte Fragen**: (1) Was wird erhoben? (2) Wer erhebt? (3) Zu welchem ursprünglichen Zweck? (4) Wer darf abrufen/empfangen? (5) Mit welcher Rechtsgrundlage? (6) Welche automatische Voreinstellung, aktiven Entscheidungsmöglichkeiten, Widersprüche und Rechtsbehelfe gibt es? (7) Was ändert sich mit neuem Gesetz/neuer Technologie? (8) Wer erhält Gebühren, Wirtschaftsnutzen oder Handlungsmacht, und welche Kosten entstehen? (9) Was weiß die betroffene Person konkret, und kann sie Handlungen nachprüfen?

**Getrennte Begriffe:** Einwilligung, Widerspruch, gesetzliche Verarbeitung ohne pauschales Vetorecht, Datenweitergabe an Dritte, kostenpflichtige Verwaltungsleistung, pseudonymisierte Forschung, Adresshandel, KI-Training und eigenständige Cloud-Übermittlung. Niemals austauschbar behandeln.

## 2. Neues Schlüsselereignis: Sozialdaten können für KI-Modelle verwendet werden

**24.12.2025 – §67c Absatz 3 SGB X** (SGB VI-Anpassungsgesetz vom 22.12.2025, BGBl. 2025 I Nr. 355, Art. 11): Seit diesem Tag enthält das SGB X eine ausdrückliche Befugnis für die Entwicklung, das Trainieren, Validieren und Testen von KI-Modellen und -Systemen auf Grundlage bereits für andere Zwecke erhobener Sozialdaten, **nur** unter den gesetzlichen Bedingungen, darunter:
- zur Erfüllung derselben gesetzlich zugewiesenen Aufgabe;
- Erforderlichkeit und Einschätzung, dass anonymisierte Daten Ergebnisse verfälschen würden;
- Pseudonymisierung;
- sachliche Zweck- und Dateneinschränkungen, technische und organisatorische Vorkehrungen, angemessene Löschfrist;
- §69 Absatz 1 Nummer 4 für erforderliche Datenübermittlung zwischen befugten Stellen unter Bezug auf §67c Absatz 3.

**Was daraus NICHT folgt:** Sozialdaten seien frei verkäuflich; jede Behörde dürfe für beliebige Firmen Modelle trainieren; ein KI-System arbeite schon flächendeckend mit diesen Daten; Rechtmäßigkeit jeder konkreten Anwendung sei bewiesen. **Was daraus als überprüfbare Frage folgt:** Wer verwendet diese Befugnis, mit welchen Daten, für welchen Fachzweck, welchen Evaluationskennzahlen, welcher Rechtsaufsicht, welchem Modellbetreiber und welchen öffentlichen Nutzen-/Schadenbefunden?

**Offizielle Primärnormen:** https://www.gesetze-im-internet.de/sgb_10/__67c.html ; https://www.gesetze-im-internet.de/sgb_10/__69.html . **Gesetzeshistorische Sekundär-Synopse:** https://www.buzer.de/gesetz/3086/al0-233126.htm . **Behördliche Erläuterung:** https://rvrecht.deutsche-rentenversicherung.de/SharedDocs/rvRecht/01_GRA_SGB/10_SGB_X/pp_0051_75/gra_sgb010_p_0069.html .

## 3. Zusätzliche Datenwelten, die nicht alle in den Haupttext gehören

| Kandidat | Regeltyp | Einordnung/Primärquelle | Offene Forschung |
| --- | --- | --- | --- |
| Sozialdaten | Erforderlichkeit, gesetzlich erlaubte Übermittlung, Sozialgeheimnis | §67a, 67b, 67d, 69 SGB X, https://www.gesetze-im-internet.de/sgb_10/__67d.html | tatsächliche Empfänger, Rechts-/KI-Zwecke, Anzahl |
| Sozialdaten → KI-Training | neue gesetzliche Befugnis ab 24.12.2025 | §67c Abs. 3, §69 Abs. 1 Nr. 4 SGB X | alle konkreten Projektanwendungen, Audit-/Diskriminierungseffekte |
| Steuerdaten/Finanzdaten | Auskunftspflicht mit Steuergeheimnis | §30 und §93 AO, https://www.gesetze-im-internet.de/ao_1977/__93.html | Rechtsgrundlagen des Kontenabrufs, Zugriffskontrollen |
| Bundesstatistik | gesetzlich definierte Auskunftspflicht, je nach Statistik | §15 BStatG https://www.gesetze-im-internet.de/bstatg_1987/__15.html | Pflicht vs freiwillig; Vergleich zur Einwilligung |
| FDZ ePA | gesetzlicher Forschungszugang, Gesamt-/Teilwiderspruch, Datencockpit | FDZGesV §8, §13 https://www.gesetze-im-internet.de/fdzgesv/__8.html ; https://www.gesetze-im-internet.de/fdzgesv/__13.html | tatsächliche Sichtbarkeit, Bedienbarkeit, Rückwirkungsgrenzen |
| Melderegister | begrenzte Auskünfte, teils gebührenpflichtig | §44 und §50 BMG | jährliche Erträge **je lokaler Behörde**, Zweck-/Kostentrennung |
| Melderegister Bundeswehr | bestimmter früherer Widerspruch seit 01.01.2026 weggefallen | kommunale Fachinformation Stuttgart, Dortmund | historische Entscheidung/Verhältnismäßigkeit/automatisierter Abruf |

**Sehr wichtige Unterscheidung:** Der Zugang zu geschützten Sozialdaten für gesetzliche Aufgaben ist rechtlich nicht dasselbe wie das Erlangen von Daten für kommerzielle Marketingzwecke; die neue KI-Befugnis muss aber selbstständig nach Erforderlichkeit, Zweck, möglicher Diskriminierung, Transparenz und Gesetzesgeschichte analysiert werden.

## 4. Geldfrage: erstmal konkretisieren, nicht behaupten

**Belegte exemplarische Entgelte:** Stadt Frankfurt am Main: Online-Abruf einfacher Melderegisterauskunft über civex-p: **10,71 Euro pro Abruf**, auch eine neutrale Antwort kann kostenpflichtig sein. Offizielle Beschreibung: https://frankfurt.de/leistungen/Gewerbe-und-Wirtschaft-8957822/GenehmigungenBescheinigungen-10136943/Auskuenfte-aus-dem-Melderegister-Online-Auskuenfte-fuer-nicht-registrierte-Anwender . Das Bundesportal nennt je nach Region andere Spannen: https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99115004001000/herausgeber/HB-S1000030000009886/region/040000000000

**Nicht abgedeckt:** Zahl der Abrufe, daraus erzielte Jahressumme, zuständiger Haushaltsträger, Kosten der Bereitstellung, Vertragsbeziehungen zu IT-Dienstleistern, Margen des Dienstanbieters, Weiterverwendung und deren ökonomischer Wert. Ohne diese Angaben **keine Aussage „die BRD verdient X mit Adressen“**.

**Neuer Erhebungsauftrag:** Stichprobe offizieller kommunaler Haushalte und Datenproduktstatistiken, getrennt nach `Melderegisterauskunft`, `Verwaltungsgebühr`, `IT-Dienstleistung`, `andere Registerleistungen`; keine Summen aus Sammelpositionen als Auskunftsgewinn ausgeben. Kommunale Gebühren laufen nicht automatisch beim Bund auf.

## 5. Rechte vs tatsächliche Wirksamkeit: Gesetzestext und Alltag auseinanderhalten

**ePA-FDZ:** FDZGesV §8 erlaubt Gesamt-/Teilwidersprüche; §13 beschreibt ein Datencockpit mit Informationen über Datenübermittlung, Zeitpunkt, verfügbare Zwecke und dokumentierten Widerspruch. Ein Widerspruch unterliegt bestimmten Umsetzungsvorgaben und differenzierten Rückwirkungen. https://www.gesetze-im-internet.de/fdzgesv/__8.html ; https://www.gesetze-im-internet.de/fdzgesv/__13.html

**Melderegister:** §50 Abs. 5 BMG erlaubt definierte Widersprüche, die das Bundesportal als grundsätzlich jederzeit und ohne Begründung darstellt. Seit 01.01.2026 entfällt dagegen das frühere Widerspruchsrecht für bestimmte Datenabrufe der Bundeswehr; davon sind andere Widerspruchskategorien nicht automatisch betroffen. https://www.stuttgart.de/organigramm/leistungen/widerspruchsrechte-nach-dem-bundesmeldegesetz-geltend-machen-uebermittlungssperre-melderegister

**Nicht gleichsetzen:** „Widerspruch möglich“ / „ohne App möglich“ / „vollständig umgesetzt“ / „frühere Daten gelöscht“ / „bereits verwendete Erkenntnisse rückholbar“. Diese Fragen brauchen **unterschiedliche** technische und empirische Nachweise.

## 6. Flashback-Vergleich mit derselben Forschungs-Suchmatrix

Datenart → verantwortlicher Akteur → ursprünglicher Zweck → geltender neuer Zweck → Übergang zum Gesetz → Empfänger → Auswahl- oder Widerspruchsregel → Kontroll-/Rechtsbehelf → möglicher Ertrag/Nutzen/Schaden → Quelle + Zeitstand → Gegenbeispiel.

**Evidenztest:** Ein früheres Recht darf nur als „abgebaut“ markiert werden, wenn die konkrete Vergleichsvorschrift und die Stichtage belegt sind. Nur weil mehrere Datenbestände KI-Funktionen ermöglichen, ist weder eine allgemeine Freigabe noch ein allgemeiner Missbrauch bewiesen.

## 7. Zwei verschiedene Veröffentlichungsformate

**Öffentlich (kurz):** „Flashback: 2025/26 änderten sich mehrere Datenregeln – welche gelten für dich?“ Dazu drei bis fünf relevante Entscheidungskarten mit Links zu aktueller Norm, Kontrollweg und historischem Wendepunkt. Sensibler Dateninput ist dafür nicht nötig.

**Forschung (tief):** historische Synopsen, Bundestagsbegründungen, Normtexte, Behörden-/IT-Rollen, Gebühren-/Kostenregisternachweis, Nutzungspraxis, Betroffenenrechte und kontrollierte Gegenhypothesen. Keine neue „Datenskandal“-Seite ohne konkrete Vorfallsquellen.

## 8. Anschluss an Bürger-KI und Tensor

Die Fälle prüfen unsere tatsächliche Übersetzbarkeit:
- Rechtssatz → Nutzerfrage → heutiger Handlungsweg (mögliche Übermittlungssperre vs kein Widerspruch);
- Normänderung → historischen Zustand → Fachclaim mit Zeitstempel;
- veröffentlichte staatliche KI-Befugnis → konkretes Test-/Auditprogramm;
- Gebühr pro Abruf → **nicht** automatisch Gewinn oder Datenverkauf;
- technische Rechtevorschrift → **nicht** automatisch wirksame Bedienoberfläche.

**Forschungsrückweg:** Quelle → Rechtsnorm → Übergangsrelation → Risikomodell → Hypothese → Test/Gegenbeispiel → freigegebene Wissenswelt/Skill. Vor Ausweitung in Tensoren die Semantik, Zeitstände und nichtäquivalenten Relationen absichern.

**Offene Aufgaben:** ursprüngliche Gesetzesbegründung für 2025 eingeführten KI-Passus im SGB X, aktuelle konkrete Nutzungen, Kommunalgebührenrechnung, unabhängige Sicherheitsprüfung, Anwenderwirksamkeit des ePA-Datencockpits, weitere Register/ID-Systeme. Keine davon als schon beantwortet markieren.
