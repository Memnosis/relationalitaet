# Arbeitsanweisung BKI-WA-RED-001: Eigenständige Weisungsrekonstruktion

**Version:** 0.1 · **gültig ab:** 05.11.2026  
**Geltungsbereich:** Bürger-KI, Weisungsatlas, alle zugehörigen Skills, Agenten, Harvest-, Test-, Quellen- und Markdown-Artefakte.  
**Forschungsgrundlage:** [Gesetzeübergreifendes Rekonstruktionspaper](https://github.com/Memnosis/relationalitaet/blob/main/docs/paper-buerger-ki-gesetzeuebergreifende-weisungsrekonstruktion-v0-1.md).

## 1. Verbindlich

Unsere selbst entwickelten **Handlungsanweisungen und Skillakten enthalten keine kopierten Originaltexte** aus Gesetzen, Verwaltungsweisungen, PDF-, HTML- oder Anhangsdokumenten.

Originale bleiben bei ihrer Fundstelle. Wir dokumentieren eigene Formulierungen, Quellen-/Norm-IDs, genaue Abschnittsanker, Herkunfts-/Versionsdaten, gesetzeübergreifende Beziehungen, Geltungsbedingungen, Negativbefunde und Testresultate. Auch wenn Originaltexte rechtlich frei nutzbar wären, bleibt diese interne Projektregel bestehen.

## 2. Verarbeitung

1. Originalreferenz und zuständigen Herausgeber feststellen.
2. Dokumentart, Rechtsregime, Behördenbindung und Fassung bestimmen, soweit belegbar.
3. Original nur für die nötige Prüfung lesen; keine Volltext-Publikation und keine in die Skillakte kopierten Absätze.
4. Ausführungslogik selbständig rekonstruieren: Akteur, Handlung, Auslöser, Modus, Ausnahmen, Rechts-/Territorialgeltung.
5. Ähnliche Funktionen anderer Gesetze suchen, aber keine juristische Gleichheit voraussetzen.
6. Positive, negative und Grenztests formulieren und mindestens eine alternative Erklärung prüfen.
7. Quellenanker und Prüfurteil dokumentieren, ohne eine mögliche Rechtsfrage automatisch als entschieden zu behaupten.
8. Publikationsreife erst nach unabhängiger fachlicher Abnahme ausweisen.

## 3. Automatische Pipeline

Der [Konverter v0.2](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/weisungsatlas_atomizer.py) darf nur Struktur und Metadaten exportieren und eine leere Markdown-Rekonstruktionsvorlage anlegen. Rohsatzextrakte und automatisch ausgeschnittene Volltextatome sind unzulässig.

Tests: [test_weisungsatlas_atomizer.py](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/test_weisungsatlas_atomizer.py), [Workflow](https://github.com/Memnosis/relationalitaet/actions/workflows/bki-weisungsrekonstruktion-tests.yml). **Testabnahme weiterhin offen, bis tatsächliche CI-Ergebnisse vorliegen.**

## 4. Freigabestufen

`quelle_entdeckt → struktur_importiert → eigene_rekonstruktion → intern_gegengeprüft → fachlich_reviewed → freigegeben`.

Keine automatische Höherstufung aus Textmenge, Quellenanzahl oder Ähnlichkeit. `nicht_geprüft` ist explizit, nicht gleich `nicht_vorhanden`.

## 5. No-Loss & Synchronisation

Quellenregister, Glossar, Skill-IDs, Testakten, Versionsbezüge und abhängige Publikationen müssen bei jeder fachlichen Änderung nachgezogen werden. Die aktuellen Vorarbeiten sind [Crosswalk](https://github.com/Memnosis/relationalitaet/blob/main/docs/buerger-ki-quellen-glossar-crosswalk-weisungsatlas.md), [Paper](https://github.com/Memnosis/relationalitaet/blob/main/docs/paper-buerger-ki-gesetzeuebergreifende-weisungsrekonstruktion-v0-1.md) und [Testmatrix](https://github.com/Memnosis/relationalitaet/blob/main/docs/data/bki-gesetzeuebergreifende-tests-v0-1.json).

## 6. Nicht zulässige Schlussfolgerungen

- Eine interne Weisung ist nicht automatisch Bürgeranspruchsgrundlage.
- Gleichartige Verfahrensoperationen in VwVfG, SGB X und AO sind nicht identische Rechtsregeln.
- Eine Bundesweisung bindet nicht ohne geprüfte Kompetenzgrundlage jede Landes- oder Kommunalbehörde.
- Eine nicht auffindbare Vorschrift gilt nicht allein deshalb als nicht existent.
- Eine alte veröffentlichte Fassung ist nicht automatisch die aktuelle.

**Status der Arbeitsanweisung:** Fassung und entsprechende Konverterumstellung gespeichert; eigenständige juristische Abnahme und CI-Testnachweise offen.
