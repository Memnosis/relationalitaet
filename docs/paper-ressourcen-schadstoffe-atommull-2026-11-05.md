# Ressourcen statt Müll – Materialwert, Schadstoffe und intergenerationelle Folgekosten
**Forschungsstand v0.1 · 05.11.2026 · eigenständiges Ressourcen-Paper**

## Leitfrage
„Es gibt keinen Müll, nur Ressourcen“ wird als Strategie der Rückgewinnung geprüft, nicht als durch Umdefinition bereits gelöste Problemlage. Material kann toxisch, vermischt, thermodynamisch zu aufwendig zu trennen oder wirtschaftlich mit negativem Nettowert sein.

## Mengen und Nenner
Destatis meldet für **Deutschland 2024** rund **365 Mio. t Abfälle** insgesamt, darunter 182,8 Mio. t Bau- und Abbruchabfälle sowie 49,3 Mio. t Siedlungsabfälle. Haushaltsnahe Abfälle, Siedlungsabfälle und gesamter Stoffstrom sind nicht gleichzusetzen.
Quelle https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/06/PD26_185_321.html
UBA: https://www.umweltbundesamt.de/daten/umweltzustand-trends/ressourcen-abfall/abfallaufkommen

## Konkrete dokumentierte Preisreferenzen – keine pauschalen Müllpreise
Die deutsche BDSV meldete September 2026 ab Station nach Schrottsorten: Sorte 1: **254,6 EUR/t**, Sorten 2/8: **294,6 EUR/t**, Sorte 3: **289,0 EUR/t**, Sorte 4: **302,9 EUR/t**, Sorte 5: **246,5 EUR/t**. Diese Werte gelten für definierte handelbare Schrottsorten, nicht für die Gesamttonnage des Abfalls. Quelle https://www.bdsv.org/unser-service/markt-preise/
Eurostat berichtet für 2025 EU-weite Preisindikatoren von **88 EUR/t Glas**, **154 EUR/t Papier/Pappe**, **308 EUR/t Kunststoffe** (unterschiedliche Handelsströme und statistische Grenzen). Quelle https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Recycling_%E2%80%93_secondary_material_price_indicator
Die Multiplikation des gesamten deutschen Abfalls mit einem solchen Preis wäre eine unzulässige Hochrechnung.

## Nettowert-Modell
`realisierbarer Nettowert = rückgewinnbare verwertbare Masse × sorten- und qualitätsbezogener Preis − Sammlung − Sortierung − Transport − Behandlung − Gefahrenstoffentsorgung − Investition/Finanzierung + nachweislich vermiedene Kosten`.
Zudem sind vermiedene Treibhausgasemissionen, Primärressourcenverbrauch, Freisetzung von Schadstoffen und soziale Effekte getrennte, nicht automatisch monetarisierte Endpunkte.

## Schadstoffe und Verzögerungen
Anerkennung ist mehrstufig: erster klinischer/technischer Hinweis → wissenschaftlich belastbare Ursachenzuordnung → regulatorische Beschränkung → vollständiges Verbot → Schadensfeststellung/Anerkennung im Einzelfall → Sanierung → Kostentragung. Latenz zwischen Exposition und Krankheit ist eine andere Zeitmessung als Verzögerung der Regulierung.
Konkretes Beispiel **Asbest**: erste Hinweise auf Asbestose etwa 1907; epidemiologische Lungenkrebsbefunde in den 1950ern, Mesotheliomzusammenhang in den frühen 1960ern, erste Schutzvorschriften in Deutschland 1972, umfassendes Verbot 1993. Laut BAuA durchschnittliche medizinische Latenz der asbestassoziierten Krebserkrankung über 30 Jahre. Die Auswahl des Startjahres verändert die regulatorische „Dauer bis Anerkennung“ erheblich. Quellen https://www.baua.de/DE/Themen/Chemikalien-Biostoffe/Gefahrstoffe/Informationsportal-Asbest/Asbest_node und https://www.ncbi.nlm.nih.gov/books/NBK20322/
Weitere Kandidaten für identische Karten: Blei, PCB, PFAS, Contergan, Benzol; derzeit **keine vergleichbaren, verifizierten Zeitabstände** in diesem Arbeitsstand. Es ist methodisch falsch, aus einer prominenten Stichprobe einen durchschnittlichen Anerkennungsverzug aller Stoffe zu berechnen.

## Atomenergie und Endlagerung
Seit 2017 gilt eine Aufgabenteilung: Betreiber tragen Rückbau und Verpackung; Fonds KENFO finanziert die staatliche Zwischen- und Endlagerung. Einmalige Betreiberzahlung **24,1 Mrd. EUR 2017** einschließlich Risikoaufschlag. Vermögen Ende 2025 **25,6 Mrd. EUR** und kumulierte Entsorgungsauszahlungen **5,3 Mrd. EUR**. Trennung Fondsbestand, Rückstellungen, Steuerförderung, zukünftige Kosten, unentschiedene Haftung, tatsächliche Rechtsansprüche. Quellen https://www.kenfo.de/ueber-den-kenfo und https://www.bundeswirtschaftsministerium.de/Redaktion/DE/Artikel/Energie/kernenergie-stilllegung-rueckbau-kernkraftwerke.html
Für „virtuellen historischen Strompreis“ ist eine definierte Energiegesamtmenge (kWh) nach Jahr, Preisniveau, Diskontrate, Kostenabgrenzung und Behandlung von Forderungen/Schulden nötig. Formel nur als `(zurechenbare reale historische + abgezinste zukünftige Nettokosten) / zugeordnete erzeugte kWh`. Historische Subventionen sind nicht zwingend heute offene Schulden. Nicht entschiedene Schadensersatzforderungen dürfen nur als Szenario, nicht als Bilanzschuld ausgewiesen werden.

## Wiederverwendbare Forschungsakte
`material_id / hazardous_substance_id / mass / contamination / purity / region / observation_year / price_date / price_type / process / recovery_yield / all_in_cost / net_value / source_id / uncertainty / evidence_status / transformation_audit`.
Zeitliche Schadstoffkarte: `first_signal / evidence_threshold / regulatory_warning / first_protection / ban / latency / officially_recognized_cases / remediation_cost / financing_status`. Leere Felder sind ausdrücklich Ergebnisse von Recherchegrenzen, nicht Nullen.

## Querverweise
[Benchmark- und Evidenzarchitektur](./paper-benchmarks-evidenz-zeitkontext-crosswalk-2026-11-05.md), [Forschungsbibliothek](./bibliothek.html), [Mitmachen](./mitmachen.html).
**Status:** geprüfte exemplarische Quellen und Rechenmodell, noch kein vollständiger Stoffstrom-Kostenatlas.

## Kommunale Einnahmen aus Hausmüll: Bruttoerlös ist nicht Nettogewinn
Grundsatz: Kommunen können aus Altpapier, Metall, bestimmten Kunststoffen, Bioabfall/Biogas und Wärme Einnahmen erzielen, aber Hausmüllentsorgung verursacht auch Sammlung, Personal, Sortierung, Transport, Verbrennung, Reststoffbehandlung, Nachsorge und Kapitalaufwand. Die gesetzlichen Müllgebühren dienen regelmäßig der Deckung dieser Kosten, keine generelle Einnahmenfreiheit für Haushalte (https://verwaltungsportal.hessen.de/leistung?leistung_id=L100001_8967107).
**Beispiel AWISTA Starnberg 2025:** 81 % Umsatz durch gebührenpflichtige Leistungen, 19 % durch Papier/Metall/Kartonagen und andere Wertstoffe. Wertstoffvermarktung −554.000 EUR gegenüber Vorjahr (−16 %). Jahresfehlbetrag −492.000 EUR. Die Abfallgebühren wurden zum 01.01.2026 erhöht. Quelle https://www.awista-starnberg.de/das-unternehmen/aktuelles/details/awista-starnberg-ku-zieht-bilanz-fuer-das-wirtschaftsjahr-2025
**Beispiel St. Ingbert:** Papierverkauf 2020 131.000 EUR, 2022 425.000 EUR, 2024 rund 268.000 EUR; Gebühreneinnahmen im Plan 2026 rund 3,187 Mio. EUR. Quelle https://ratsinfo-st-ingbert.ego-saar.de/allris-public/wicket/resource/org.apache.wicket.Application/doc1375096.pdf . Das ist eine Erlöszeitreihe, kein Gewinnbeweis.
**Benchmark:** `kommunaler Nettoertrag = stoffliche Verkaufs- und Energieerlöse + Gebühren/sonstige Entgelte - alle zurechenbaren Betriebs-/Finanzierungs-/Nachsorgekosten`. Alternativ: `stofflicher Nettowert ohne Gebühren = Verkaufserlöse - stoffbezogene Rückgewinnungs-/Sammlungs-/Transportkosten`. Beide Größen strikt getrennt. Gebühren sind eine Finanzierung der Entsorgungsleistung, kein intrinsischer Marktwert des Stoffes.
**Forschung:** Fallstudien mit Gebührenkalkulation, Betriebsergebnis, Stoffpreis und Rückgewinnungsquote je Kommune; Prüfung, ob besseres Sortieren den Gebührenbedarf tatsächlich senkt und unter welchen Bedingungen ein echter Nettogewinn ohne Gebühren erzielt werden könnte.
