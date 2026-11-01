# SOULution · Wirtschafts- und Demokratiesimulationen — Forschungsaufgaben
Stand 2026-11-01 · Forschungsedition v4: 29 PDF-Seiten einschließlich Originalcover und zweier Anzeigen; 27 redaktionelle Seiten. Kein implementiertes Simulationssystem.

## Aufgaben mit wiederverwendbaren IDs
| ID | Forschungsmodul | Abnahme |
|---|---|---|
| FIN-OPS-01 | Bundeshaushalt / Quellenharmonisierung | offene Beispieldaten, Datenjahr, Einheit, Klassifikation, Lizenz und Importtest |
| FIN-OPS-02 | Wohnkosten-Sankey | reproduzierbare Rechnung, Parameter, Fehlergrenzen und lesbare Tabelle |
| DEM-OPS-01 | Demokratieportal-Vergleich | Pol.is, Decidim, CONSUL: strukturierte Funktionsmatrix, Datenschutz, Verfahrensanschluss |
| DEM-OPS-02 | öffentliche Gemeinsamkeiten / Minderheiten | freiwillige Testdaten, Biasprüfung, Differenz von Stichprobe/Mehrheit und sichtbare Gegenpositionen |
| ROOM-OPS-01 | Situation Room | öffentliche Lage, Probleme, Quellen, Zeit, Akteure, Varianten, Evidenz und Revision |
| ROOM-OPS-02 | War Room | Rollen, Tasks, Lieferobjekte, Abnahmen, Crosswalk und Fortschrittsbericht |

## Pipeline
Öffentliches Kernproblem → Lösungsfunktion → Methode / Operationalisierung → wissenschaftliche Evidenz → Implementierung / Skill → Datenplattform → Bedingungen / Risiken → Test → dokumentierte öffentliche Entscheidung und Korrekturmöglichkeit.

## Sechs reproduzierbare Prompts
1. **Quelleninventur.** Erschließe bereitgestellte Haushalt-/Sozial-/Konsumdaten nach ID, Herkunft, Jahr, Lizenz, Raum, Einheit, Kategorie, Evidenz, Aktualität, verbundene Objekt-IDs. Fehlende Angaben nicht erfinden. JSON plus Prüfbericht.
2. **Relations-Compiler.** Erzeuge typisierte Relationskanten zwischen Zahlung, Empfängerklasse, Konsum und Branche. Trenne belegte Transaktion von statistisch abgeleitetem Modell, Szenario und unbekannt. Gib Formeln, Sensitivität, Gegenprobe und Tests aus.
3. **Demokratiewerkzeuge.** Vergleiche Pol.is, Decidim und CONSUL anhand: Abstimmung, deliberative Funktionen, Konsens, Moderation, Barrierefreiheit, Hosting, Exporte, API, Lizenzen, Datenschutz, institutionelle Rechenschaft; belege jedes Feld.
4. **Situation Room.** Gestalte für einen abgegrenzten kommunalen Wohnkostenfall öffentliche Datenansicht mit Zeitachse, Maßnahmen, Alternativen, Fragen, Annahmen und Quellen; ohne individualisierende Personenprofile.
5. **War Room.** Leite aus den offenen Daten- und Evidenzlücken GitHub-Tasks mit ID, Abhängigkeit, Methodik, Skill, erwarteter Datei, Test und Abnahme ab. Trenne »geplant«, »in Arbeit«, »getestet«, »abgenommen«.
6. **No-Loss-Publikation.** Vergleiche Originalwerk, Forschungsedition, JSON-Register und Website, markiere bewahrt, gekürzt, ausgelagert und noch fehlend. Quellen und Originalversionen bleiben unverändert.

## Software und regulatorische Quellen (zu prüfen beim konkreten Import)
- Pol.is: https://pol.is/ · https://github.com/compdemocracy/polis
- Decidim: https://docs.decidim.org/ · https://github.com/decidim/decidim
- CONSUL Democracy: https://consuldemocracy.org/ · https://github.com/consuldemocracy/consuldemocracy
- Cambridge Analytica / FTC: https://www.ftc.gov/legal-library/browse/cases-proceedings/182-3107-cambridge-analytica-llc-matter

## Anschlüsse
- [SOULution](../../docs/soulution.html)
- [Mitmachen](../../docs/mitmachen.html)
- [Projektstand](../../docs/projektstand.html)

**Evidenzstatus:** Dies ist ein Planungs- und Aufgabenregister. Kein realer Wohnkosten-Sankey, keine Portalinstallation und kein Situation-Room-Demonstrator sind dadurch ausgeführt.
