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
