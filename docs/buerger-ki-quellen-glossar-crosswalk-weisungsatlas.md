# Bürger-KI · Quellen-/Glossar-Crosswalk zur gesetzeübergreifenden Weisungsrekonstruktion

**ID:** BKI-WA-CROSSWALK-001 · **Stand:** 05.11.2026 · **Status:** projektbezogene Ergänzung; kein globaler Glossar-Import behauptet.  
**Projektregel:** BKI-WA-RED-001 – keine Originaltexte in eigenen Handlungsanweisungen.

## Begriffe zur Synchronisierung

| Begriff-ID | Begriff | Eigene präzisierende Definition | Prüfhinweis |
| --- | --- | --- | --- |
| BKI-GL-WA-01 | Weisung | Durch befugte Stelle an einen bestimmten Verwaltungsträger gerichtete Vorgabe; interne Geltung ist gesondert zu prüfen | Nicht jede Richtlinie bindet jede Behörde |
| BKI-GL-WA-02 | Verwaltungsvorschrift | Abstrakt-generelle verwaltungsinterne Regelung; Bezeichnung und Wirkung hängen von Herkunft und Rechtsgrundlage ab | Nicht automatisch Bürger-Anspruchsnorm |
| BKI-GL-WA-03 | Funktionsfamilie | Vergleichbare Verfahrensoperation, die unter verschiedenen Gesetzen vorkommt | Funktionsgleichheit ≠ Normgleichheit |
| BKI-GL-WA-04 | Rechtsregime | Fachlich und zeitlich anwendbarer Komplex von Normen und Verfahrensregeln | VwVfG/SGB X/AO und Landesrecht trennen |
| BKI-GL-WA-05 | Geltungsrelation | Belegt, welche Norm/Weisung welche Behörde, Region, Aufgabe und Zeit betrifft | Nicht aus bloßem Dokumenttitel ableiten |
| BKI-GL-WA-06 | Eigene Rekonstruktion | Fachliche, in selbstständiger Sprache formulierte abstrakte Modellbeschreibung | Quellenreferenz und eigenständiger Prüfstatus |
| BKI-GL-WA-07 | Atomare Regelakte | Prüfkandidat mit Akteur, Handlung, Auslöser, Ausnahme, Reichweite und Originalfundstelle | Noch kein freigegebener Skill |
| BKI-GL-WA-08 | Nichtentsprechung | Belegter Unterschied zwischen scheinbar ähnlichen Handlungsregeln | Wichtiger Negativbefund |
| BKI-GL-WA-09 | Fassungsgraph | Beziehungen zwischen dokumentierten Rechts-/Weisungsversionen | Abrufdatum nicht Inkrafttreten |
| BKI-GL-WA-10 | Quellenanker | Externe Original-URL samt präziser Fundstelle und Versionsbezug | Keine Originaltextkopie erforderlich |

## Quellenfamilien und Testanschluss

- BKI-SRC-GG: [Art. 20/83/84/85 GG](https://www.gesetze-im-internet.de/gg/BJNR000010949.html) – Behördliche Gesetzesbindung, Kompetenz- und Vollzugsformen.
- BKI-SRC-VWVFG: [VwVfG](https://www.gesetze-im-internet.de/vwvfg/BJNR012530976.html) – allgemeine Verwaltungsverfahrensregeln mit Anwendungsgrenzen.
- BKI-SRC-SGBX: [SGB X](https://www.gesetze-im-internet.de/sgb_10/BJNR114690980.html) und [SGB I](https://www.gesetze-im-internet.de/sgb_1/BJNR030150975.html) – Sozialverfahrensrechte und Sozialleistungszugang.
- BKI-SRC-AO: [AO](https://www.gesetze-im-internet.de/ao_1977/BJNR006130976.html) – steuerliche Fachverfahrensregeln.
- BKI-SRC-GGO: [GGO](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_21072009_O11313012.htm) – Bundesministerien und Verwaltungsvorschriften.
- BKI-SRC-IFG: [IFG](https://www.gesetze-im-internet.de/ifg/) – Bundesinformationszugang und Ausnahmen.
- BKI-SRC-URHG: [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html) – urheberrechtliche Abgrenzung amtlicher Werke, unabhängig von strengerer interner Projektregel.

**Nachzugspfad:** Paper BKI-WA-PAPER-002 → Funktionsfamilien BKI-F01–F06 → [Testdatensatz](./data/bki-gesetzeuebergreifende-tests-v0-1.json) → unabhängige Prüfung → Skillregister → Veröffentlichungsstand. Der übergreifende zentrale Glossar-/Quellenregister-Sync ist weiterhin ein technischer Folgeauftrag; diese Akte stellt dafür die stabile Übergabestruktur bereit.

## Erweiterung 05.11.2026: Begriff–Ziel–Wiki-Crosswalk (BKI-ZHA)

**Kernpaper:** [BKI-KERN-ZHA-001](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/KERNPAPER_ZIEL_HANDLUNGSATLAS_LEXIKON_META_V0_1.md).  
**Register:** [Lexikon-/Zielkernel](./data/bki-ziele-lexikon-kernel-v0-1.json) mit BKI-C001–C012, BKI-G001–G008 und BKI-ZHA-T01–T06.  
**UI:** [Lexikon und Ziele](./buerger-ki-ziele-lexikon.html).

### Synchronisierungsregeln
- Die existierenden Einträge **BKI-GL-WA-01 bis -10** bleiben als bisherige Facheinträge erhalten; die neuen **BKI-C001 bis C012** sind **eigene Konzept-/Sinn-IDs**, keine stille Umnummerierung der Gesamtglossarbegriffe.
- Begriffsähnlichkeiten, Aliasformen und ein Wikipedia-Link erzeugen **keine** bestätigte Glossaridentität. Der dazu nötige Crosswalk bleibt `not_reviewed`.
- FIM-Leistungsobjekt und FIM-Verrichtung sind ausdrücklich getrennt. So auch Bewilligung und tatsächliche Leistungserfüllung sowie deutsche Jugendamts- und schweizerische KESB-Aufgaben.
- Wikidata-Q-IDs fehlen bewusst, bis Entität, Fachbedeutung und Rechtsraum tatsächlich überprüft sind.
- Projektweite Synchronisation des historischen vollständigen Glossars und Quellenregisters **ist offen**; diese Akte ist der dokumentierte Übergabepunkt, nicht die Behauptung eines automatischen Abgleichs.
- Eigene Rekonstruktionen ohne Originaltextkopie bleiben verbindlich. Externe Lexikon- und Wiki-URLs sind Zusatzquellen, amtliche Norm-/FIM-Quellen bleiben getrennt vermerkt.

**Neue Quellengruppen:**
- FIM-Fachglossar: https://docs.fitko.de/fim/docs/leistungen_neu/klickpfad/erlaeuterungen/begriffe/
- MediaWiki API: https://www.mediawiki.org/wiki/API:REST_API
- Wikidata Datenzugriff: https://www.wikidata.org/wiki/Help:Data_access
- Europäische Rechtsglossare: https://e-justice.europa.eu/topics/legislation-and-case-law/glossaries-and-translations_de?language=de

**Neue Prüfung:** Kein automatischer Import fremder Wiki-Texte in die interne Handlungsbibliothek. Der Pilot enthält eigene didaktische Definitionen und externe URLs.
