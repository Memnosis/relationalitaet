# Bürger-KI – Sprachprojekt vor User Storys
## Vollständige Pfadgrammatik, Bedeutungsübersetzung, gestufte Wissensräume und No-Loss-Prüfung

**ID:** BKI-LANG-ARCH-001 · **Stand:** 05.11.2026 · **Status:** geprüfter Architekturentwurf und konkrete Bestandsanalyse; vollständige redaktionelle und fachliche Abnahme bleibt offen.  
**Prioritätsentscheidung:** Sprache → Pfadelemente → Übersetzbarkeit → Inhalte der Vertiefung → Crosswalk → Komponenten → User Storys.  
**Übergeordnet:** [Sprachräume-Paper](../../docs/paper-buerger-ki-sprachraeume-termini-operationalisierung-claims-v0-1.md) · [Lernweg-Datenmodell](../../docs/data/bki-lernpfade-orchestrierung-v0-1.json) · [Therapieplatz-Manifest](../../docs/data/bki-therapieplatz-fuenf-blickwinkel-v0-1.json) · [Architektur-Masterplan](./MASTERPLAN_ARCHITEKTUR_LERNPFADE_CROSSWALK_SKILLS_V1_2026-11-05.md)

## 0. Grundentscheidung: Die Website ist keine KI

Das öffentliche Angebot ist zunächst ein **redaktionell und wissenschaftlich erschlossener Wissens- und Lernraum**. Es navigiert durch recherchierte Quellen und Erkenntnisse. Keine autonome individuelle KI-Beratung, keine vorgetäuschte Verständnis- oder Echtzeitfähigkeit, keine Sammlung personenbezogener Bürgerfälle. `Skill spezifiziert` ist nicht `Skill implementiert` oder `Skill fachlich validiert`. Das Wort „Bürger-KI“ benennt das Forschungsprojekt und sein Ziel, nicht eine bereits vorhandene intelligente Website.

Der Mensch soll nicht eine Fachsprache erlernen müssen, um eine konkrete Antwort zu erreichen. Fachliche Tiefe wird auf Wunsch geöffnet; auf der Oberfläche stehen die passende Frage, eine knappe zutreffende Erklärung und höchstens zwei bis drei **inhaltlich verschiedene, genau begründete** Verbindungen.

## 1. Bestand: Wo stehen wir wirklich?

Aus dem tatsächlichen Stand vom 05.11.2026:
- `docs/data/bki-lernpfade-orchestrierung-v0-1.json`: **fünf Haupteinstiege** `entry-goal, entry-knowledge, entry-help, entry-society, entry-research`; **fünf Lernpfade** `LP-01..05`; die Pfade bestehen aktuell hauptsächlich aus drei Einstiegsstationen, einem Exit-Typ und noch offenem Review.
- `docs/buerger-ki-lernpfade.html`: navigierbare Routen mit Fragen, aber vorerst keine vollständige semantische Übergangs- und Übersetzungsakte für jedes Routen-Element.
- `docs/data/bki-therapieplatz-fuenf-blickwinkel-v0-1.json`: **fünf Perspektiven** `ziel, wissen, hilfe, gesellschaft, forschung`, mit `learning`, `steps`, `cross`, `open` und fünf Spiegelungen. Der Pilot besitzt kontextuelle Quellen/Links, jedoch keine systematische Aussageäquivalenz- und Inhaltsqualitätsprüfung für alle Wechsel.
- `docs/buerger-ki-blickwinkel-therapieplatz.html`: wählt Perspektiven und rendert Schritttexte/Links; die Spiegelungs-Schaltflächen führen bislang zur Ausgangsperspektive (`from`), nicht direkt zur Zielperspektive (`to`). Das kann die versprochene Spiegelung didaktisch verfehlen und ist als Reviewpunkt zu behandeln.
- `docs/buerger-ki.html`: die historische Erzählung ist nach dem Originalsprachen-Audit wieder sichtbar; 21 historische redaktionelle Claims bleiben geschützt.
- `docs/data/bki-sprachraeume-claims-v0-1.json`: 28 neue, noch nicht freigegebene Vorschläge.
- `docs/data/glossar-kern.json`: zwölf Webdefinitionen; die 1.072 historischen Begriffe sind dort nicht vollständig vorhanden.

Dies ist eine repräsentative Bestandsprüfung der genannten Dateien, **kein** kompletter wissenschaftlicher Quellen- und Browser-Review aller Projektdateien.

## 2. Kleinstes sinnvolles Pfadelement (nicht bloß ein Link)

Ein `path_element` soll folgendes beantworten:

1. **Ausgang:** Was fragt, sucht oder braucht die Person hier?
2. **Bedeutung:** Worüber sprechen wir genau; welcher Wort- oder Fachsinn gilt?
3. **Kernaussage:** Was kann die Seite mit ihrem vorhandenen Wissen nachvollziehbar sagen?
4. **Evidenz:** Welche Quelle trägt welche konkrete Aussage? Fach- und Zeitgrenzen?
5. **Unterscheidung:** Womit darf dies nicht verwechselt werden?
6. **Mögliche Folge:** Verstehen, Anwendung, Unterstützung, Schadensminderung, offene Frage.
7. **Anschluss:** Warum gerade diese zwei bis drei Links und nicht beliebige weitere?
8. **Perspektivwechsel:** Was bleibt erhalten; welche zusätzliche Frage/Annahme entsteht?
9. **Rückweg:** Was weiß die Person bei Rückkehr zum Ausgangspunkt mehr?

**Sprachstruktur jeder öffentlichen Einheit:** *Frage → knappes Verständnis → entscheidende Unterscheidung → (wahlweise) nächste Vertiefung*. Der Fachtext erklärt nicht zuerst die Informationsarchitektur.

## 3. Die fünf Lernwege: vollständige sprachliche Sollfolge und derzeitige Lücken

| Pfad | Erste Frage | Notwendige Bedeutungsstationen | Gewünschter Exit | Auditstatus |
| --- | --- | --- | --- | --- |
| `LP-01` Anliegen klären | „Was will ich erreichen?“ | Ziel → Bedingungen → Begriffe → konkrete Optionen → Gegenprobe → Ergebnisgrenze | begründete Möglichkeit mit Beleg und Grenzen | bisher 3 Haupteinstiege, Feinschritte sprachlich zu vervollständigen |
| `LP-02` Thema verstehen | „Was bedeutet das genau?“ | Benennung → Definition/Sinn → fachliche Unterschiede → Quellen → Anwendung → offene Kontroverse | verständliche Begriffskarte und Wissensgrenzen | bisher 3 Haupteinstiege, Übersetzungs-/Fachkontexte offen |
| `LP-03` Unterstützung finden | „Wer kann wobei helfen?“ | benötigte Hilfe → Hilfetyp → Zuständigkeit → Bedingungen → realistischer Zugang → Alternative | erreichbarer, quellengeprüfter Such-/Kontaktweg oder Lücke | bisher 3 Haupteinstiege, kein garantierter Echtzeitzugang |
| `LP-04` Institutionen prüfen | „Warum funktioniert es nicht wie vorgesehen?“ | gesellschaftliches Ziel → Entscheidung/Zusage → Umsetzung → Messung → Wirkung → Gegenhypothese → mögliche Korrektur/Schadensbegrenzung | nachprüfbare Systemfrage oder belegter Teilbefund | bisher 3 Haupteinstiege, Metaknoten/Begriffswechsel zu operationalisieren |
| `LP-05` Fähigkeiten entwickeln | „Was muss die Bürger-KI nachweisbar können?“ | Forschungsfrage → Quelle/Modell → Regel/Skill → Test → Gegenprobe → Ergebnis → Dokumentation/Publikation | versionierter Skill/Test oder dokumentierter Fehl-/Negativbefund | bisher 3 Haupteinstiege, kein funktionierender Universal-Skill behaupten |

Die Sollfolgen sind **didaktische semantische Schritte**, keine Pflichtformulare. Die vorhandenen `LP-...`-IDs werden nicht ersetzt. Ein Leser darf jeden Pfad abkürzen, kreuzen oder verlassen.

## 4. Die fünf Perspektiven jedes Kernthemas

| Perspektive | Kernsprache | Verdeckte Tiefe | Zwingender Übersetzungstest |
| --- | --- | --- | --- |
| `ziel` | „Was soll sich für mich ändern?“ | Ziele, Alternativen, Erfolgskriterien, Zeit, Zumutbarkeit | Wunsch ≠ fachliche Indikation ≠ rechtlicher Anspruch |
| `wissen` | „Was bedeutet das, und woher wissen wir es?“ | Glossar, Definitionen, Gegenbeispiele, Studienqualität, Versionen | Wortähnlichkeit ≠ fachliche Identität; Messwert ≠ Gesamtwirklichkeit |
| `hilfe` | „Wer hilft – und was kann die Stelle wirklich tun?“ | Zuständigkeit, Zugang, Beratungs-/Vermittlungsarten, Bedingungen | Hilfeportal ≠ tatsächliche Leistung; Kontakt ≠ Erfüllung |
| `gesellschaft` | „Wie entsteht die Lücke, und was lässt sich ändern?“ | historische Reihen, Planung, Finanzierung, Evaluation, Verantwortung | individuelle Schwierigkeit ≠ bewiesene strukturelle Ursache |
| `forschung` | „Wie könnten wir die Frage besser beantworten?“ | Quelle → These → Test → Gegenbefund → Skill → Forschungsgrenze | Testfall ≠ allgemeine Leistungsfähigkeit; Ähnlichkeit ≠ mathematischer Beweis |

**Querverbindungen:** Jede Perspektive braucht mindestens eine sachlich präzise Weiterführung in eine andere Perspektive, mit explizitem Erkenntnisgewinn. Bloße Schaltfläche ohne Mehrwert reicht nicht.

## 5. Übersetzbarkeit nicht pauschal, sondern nach Elementen prüfen

`TR-01` Lebenswelt → Fachfrage; `TR-02` Fachbegriff → Klartext; `TR-03` Institution → Wirkung; `TR-04` Quelle/Messgröße → prüfbare These; `TR-05` Fach-/Relationsmodell → Lernweg; `TR-06` natürliche Sprachen / Rechtsräume → kontextabhängiger Vergleich.

Jeder Übersetzungsversuch hat genau eine `translation_id`, `source_element_id`, `target_element_id`, `direction`, `retained_meaning`, `added_assumptions`, `omitted_meaning`, `equivalence_status`, `source_ids`, `counterexample`, `review_status`. Erlaubte Befunde: `exact_in_context`, `partial_overlap`, `broader`, `narrower`, `analogy_only`, `contradiction`, `not_equivalent`, `unassessed`.

### Elementarer Beispieltest

- Ausgang: „Ich finde keinen Therapieplatz.“
- Zielübersetzung `ziel → wissen`: „Welche Art der Behandlung wird benötigt und was gilt als Behandlungsbeginn?“
- `wissen → hilfe`: „Welche Einrichtung leistet Beratung, vermittelt Termine oder bietet Behandlung?“
- `hilfe → gesellschaft`: „Wie erfassen wir geeignete regionale Versorgung, ohne einzelne Kontakte als Erfüllung zu zählen?“
- `gesellschaft → forschung`: „Welche Wartezeitdefinitionen und Beobachtungen sind überhaupt vergleichbar?“
- Rückweg `forschung → ziel`: „Welche Grenzen der Datenlage beeinflussen die ursprüngliche Frage; welche Hilfeoption bleibt unabhängig davon?“

Diese Kette stellt **Fragen zur Übersetzung**, keine 1:1 semantischen Gleichheiten. Ihr Zweck ist gerade, zusätzliche Bedingungen und Grenzen sichtbar zu machen.

## 6. Ausklappbare Wissensräume: verbergen dürfen sie nur, was sie tatsächlich enthalten

Die geschlossene Ebene ist eine Einladung mit **konkreter Aussage**, keine Leerstelle mit „Mehr erfahren“. Jedes ausklappbare Element hat einen erkennbaren Gegenstand, eine Vorab-Angabe der Tiefe und eine inhaltlich ausreichende Innenstruktur.

### Modultyp `definition_world`: „Was bedeutet dieser Begriff?“

Geschlossen: 1-Satz-Erklärung + „Begriffe und Unterschiede ansehen“.  
Geöffnet: Originaldefinition mit Kontext, 2–4 benachbarte Begriffssinne, mindestens ein echtes Beispiel, eine Abgrenzung/Gegenbeispiel, ein Primärquellenlink, Rückverweis auf Anwendung. Fachsinn mit ungelöstem Quellenstatus nicht als feste Definition präsentieren.

### Modultyp `path_world`: „Welche Wege gibt es?“

Geschlossen: Fragestellung + Umfang der Optionen.  
Geöffnet: Voraussetzungen, Schrittunterschiede, mögliche Alternativen, Ausnahmen, Grenzen und die 2–3 passendsten quellengeprüften Links. Keine vorgetäuschte Live-Verfügbarkeit.

### Modultyp `evidence_world`: „Was sagen die Quellen wirklich?“

Geschlossen: eine belastbar eingegrenzte Aussage + Hinweis auf Unsicherheit.  
Geöffnet: Originalquelle/Fundstelle, Begriffs-/Methodenstand, Population/Nenner, Gegenbefund, konkurrierende Deutung, Zeit-/Rechtsraum, Methodengrenzen und passende Paper-Vertiefung.

### Modultyp `perspective_world`: „Anders betrachtet“

Geschlossen: „Was ändert sich, wenn wir das aus Sicht der ... betrachten?“  
Geöffnet: Ausgangs- und Zielsicht, gleichbleibendes Anliegen, gewonnene Einsicht, Verlorenes, neue Annahme, passende Querverbindung und Rückweg. Kein Etikettenwechsel ohne neue Erkenntnis.

### Modultyp `meta_world`: „Die größere Frage“

Geschlossen: präzise Systemfrage mit Relevanz für den konkreten Pfad.  
Geöffnet: weitere fachliche Herkunftspfade, Gemeinsamkeiten und Unterschiede, nachgewiesene/ungeprüfte Erklärungen, realistische Ansatzpunkte und Grenzen/Schadensbegrenzung, Rückwege. Gemeinsamer Knoten ≠ gleiche Ursache.

### Modultyp `research_world`: „Wie prüfen wir das?“

Geschlossen: Untersuchungsziel und Evidenzstatus.  
Geöffnet: These, Quellenrolle, Operationalisierung, Tests, Gegenfälle, Negativbefunde, Methode, verlinkte Forschungsakte, Skillstatus. Ein wissenschaftliches Detail gilt nicht allein wegen seiner Existenz als bestanden.

### Modultyp `source_world`: „Die wichtigsten Verbindungen“

Geschlossen: Zwei bis drei *kontextgenaue* Ressourcen mit kurzen individuellen Nutzenhinweisen; wenn weniger belastbare Quellen vorhanden sind, weniger anzeigen.  
Geöffnet: Warum diese Quellen gewählt wurden, Geltung und Zugangsstand, verwandte Quellen und der Link zur Gesamtrecherche. Nicht drei redundante Suchportale. Quellen müssen redaktionell recherchiert/überprüft sein; ein bloß vorhandenes URL-Feld reicht nicht.

### Interaktionsvertrag

- Standardmäßig geschlossen, aber mit **in sich vollständigem** hilfreichem Teaser; essentielle Informationen/Notfallhinweise nicht exklusiv verstecken.
- Für einfache Vertiefungen native HTML-`details/summary`, sofern Semantik und Bedienbarkeit genügen; komplexere Ansichten mit ausdrücklich tastatur- und screenreaderfähigem Verhalten.
- Ein einzelnes Element kann innen weitere *fachlich notwendige* Abschnitte besitzen; **keine endlose verschachtelte Klickkaskade**. Spätestens bei eigenständigem Thema oder langem Paper externer/vernetzter Deep-Dive-Link.
- Geschlossener und geöffneter Zustand müssen beide sprachlich sinnvoll sein. Keine leeren Panels, noch nicht vorhandenen Weltinhalte oder rhetorischen Versprechen auf später.
- Ausgewählte 2–3 Kontextlinks und der zurückhaltende Link zur vollständigen Quellenübersicht bleiben Bestandteil der Seitenlogik.

## 7. Konkrete redaktionelle Abnahme: Wann ist eine Welt wirklich gehaltvoll?

**Pflichtfelder für jeden öffentlichen Weltblock:**
`element_id`, `topic_id`, `lens_id`, `world_type`, `title`, `teaser`, `substantive_sections`, `key_distinction`, `sources`, `context_links`, `known_limits`, `review_status`.

**Abnahmefragen:**
1. Beantwortet der geöffnete Block mindestens eine neue, konkrete Frage, die der Teaser verspricht?
2. Kann man eine belastbare Unterscheidung oder Handlungsmöglichkeit aus ihm mitnehmen?
3. Ist für jede konkrete Fachbehauptung die passende Quelle/Status nachvollziehbar?
4. Werden Unterschiede der Perspektiven *erklärt* statt nur verlinkt?
5. Kann man zur Ausgangsfrage zurück oder in den fachlich richtigen Deep Dive weitergehen?
6. Enthält er nicht bloß eine Linkliste, ein anderes Label oder ein paraphrasiertes Werbeversprechen?
7. Ist das Element auch ohne JS als Text/Link erreichbar und ohne Maus bedienbar?
8. Ist ein nicht untersuchtes Thema als offene Frage und nicht als ausgearbeitete Welt gekennzeichnet?

**Reviewstatus:** `inventory_only` → `draft` → `sources_reviewed` → `language_reviewed` → `fach_reviewed` → `approved_for_publication`. Die Stufen sind keine automatischen Prozentwerte.

## 8. Quellen- und Deep-Dive-Landschaft aus dem Bestand

| Inhaltsebene | Hauptfundort | Anschluss im Sprachprojekt |
| --- | --- | --- |
| Ausgang/Story | `docs/buerger-ki.html`, `buerger-ki-weg.html` | 1-Satz-Fragen, Ziel und Wahlmöglichkeiten |
| Fünf Lernwege | `docs/buerger-ki-lernpfade.html`, `docs/data/bki-lernpfade-orchestrierung-v0-1.json` | sprachliche Feinfolge `LP-01..05` |
| Fünf Themenperspektiven | `docs/buerger-ki-blickwinkel-therapieplatz.html`, `docs/data/bki-therapieplatz-fuenf-blickwinkel-v0-1.json` | Übersetzung je `lens_id` und `step.id` |
| Begriffe/Ziele | `docs/buerger-ki-ziele-lexikon.html`, `docs/data/bki-ziele-lexikon-kernel-v0-1.json` | Sinntrennung, `BKI-C...`, `BKI-G...` |
| Hilfe und institutionelle Wege | `docs/buerger-ki-anwendungsfelder.html`, `docs/buerger-ki-weisungsatlas.html` | Zuständigkeit vs. reales Angebot |
| Gesellschaft/Metafragen | `docs/buerger-ki-gemeinsam.html`, `docs/buerger-ki-grundlagen.html` | Meta- und Schadensminderungspfad |
| Quellen und Langformen | `docs/buerger-ki-forschungsbibliothek.html`, `docs/data/bki-forschungsbibliothek-v0-1.json` | kuratierte Einstiegsauswahl, kein Gesamtarchiv |
| Sprache und Semantik | `docs/paper-buerger-ki-sprachraeume-termini-operationalisierung-claims-v0-1.md` | Methoden- und Übersetzungsnorm des Projekts |
| Skills | `docs/buerger-ki-skill-deep-dive.md`, `forschung/buerger-ki/` | Prüfstatus von Fähigkeiten getrennt |
| No-Loss/Register | `forschung/register/schema/claim.schema.json`, `docs/data/glossar-kern.json`, Forschungsregister | stabile Originalreferenzen, kein unkontrollierter Merge |

**Quellenrolle:** interne Papers als Forschungsarbeiten, offizielle Fachquellen als Sachbelege, Einführungsseiten als didaktische Sicht, Skills als Fähigkeiten mit eigenem Reifegrad. Nicht alles als „Quelle“ im selben Sinn behandeln.

## 9. Konkrete Bestandslücken und Nacharbeiten

**L01** Fünf `LP`-Routen sind sprachlich eher abstrakte Navigationssequenzen als vollständige Frage→Einsicht→Ergebnis-Wege.  
**L02** Die fünf Therapie-Perspektiven besitzen viele nützliche Quellen und Unterscheidungen, aber noch keinen geprüften Satz von Bedeutungs- und Verlustakten.  
**L03** Spiegelungen dokumentieren `from/to`, während die UI-Schaltfläche bislang `from` öffnet: Zweck und Verhalten prüfen, dann gezielt zur wirklich neuen Perspektive führen.  
**L04** Tiefe ist uneinheitlich: manche Schritte nennen konkrete externe Quellen, andere nur ein internes Paper oder eine allgemeine Methodenseite. Jedes konkrete Erkenntnisversprechen braucht passenden Inhalt.  
**L05** Der 1.072er Originalglossarbestand und das Webglossar sind noch nicht vollständig semantisch querverbunden.  
**L06** Die 21 geschützten alten und 28 neuen Claims haben noch kein vollständig geprüftes Platzierungs-/Wirkungsmodell pro Pfadelement.  
**L07** Die Frage „Wo führt dieser Weg hin?“ braucht vier sichtbare Ausgänge: mögliche Lösung, Schadensbegrenzung, Metafrage, belegte Grenze.  
**L08** Statt eines großen Gesamtgraphen braucht jede Welt eine kleine, nachvollziehbare 1-Hop-Kontextliste.  
**L09** Keine der geplanten Weltkomponenten ist allein durch dieses Papier implementiert oder im Browser fachlich abgenommen.

### Reproduzierbarer Struktur-Schnelltest (05.11.2026)

Im GitHub-`main`-Baum geprüft: Die fünf `main_entries.page`-Ziele sind als Repository-Dateien vorhanden. Bei den 14 Therapieplatz-Schrittlinks sind sämtliche **neun relativen internen Ziele** im aktuellen `docs/`-Baum vorhanden; fünf weitere Ziele sind externe URLs und wurden in diesem Schritt **nicht live auf Erreichbarkeit oder fachlichen Inhalt geprüft**. Alle fünf Spiegelungen besitzen existierende `from`- und `to`-Linsen-IDs. **Davon getrennt** bleibt die beobachtete UI-Frage: Der Spiegelungsbutton öffnet `from` statt `to`. Existierende Links und IDs sind kein Qualitätsnachweis für die Frage, ob die gewählte Vertiefung fachlich passend und substanziell ist.

## 10. Umsetzungsreihenfolge vor jeder neuen User Story

**S1 – Sprachinventar**: Alle fünf `LP`-Routen und fünf Therapie-`lenses` in einer separaten Element-/Übergangsmatrix erfassen; bestehende IDs unverändert. Für jede Station Frage, Bedeutung, Erkenntnis, Quellenrolle, Anschluss und Lücke dokumentieren.

**S2 – Redaktionelle Vollständigkeit**: Fehlende Sätze, echte Zwischenfragen, Exit-/Rückwegtexte und Auswahl der wichtigsten Bedeutungsunterschiede erarbeiten. Fachlich offene Aussagen als solche markieren.

**S3 – Übersetzbarkeitsprüfung**: Jedes bestehende `cross` und jede `mirror`-Relation mit dem `TR`-Schema prüfen; gewonnene Einsicht und begrenzte Gleichwertigkeit dokumentieren. Vor allem die fünf Therapie-Spiegelungen in beide Richtungen testen.

**S4 – Weltinventar**: Vorhandenes Fachmaterial den sieben Weltmodulen zuordnen. Erst Inhalte und Quellen identifizieren, dann passende Details-Komponenten implementieren. Nur durch Quellen/Review belegte Blöcke öffentlich ausklappbar anbieten.

**S5 – Kompakte Linkkuratur**: Pro Seite *und Abschnitt* 2–3 wirklich unterschiedliche, genau passende Verbindungen recherchieren, jeweils Nutzen, Quellenrolle und Prüfdatum registrieren. Ein vierter Link führt dezent zur Gesamtübersicht. Kein generischer automatischer Linkspam.

**S6 – Technische Komponenten und QA**: Komponenten für `definition_world` etc. mit `details`-/List-Fallback, Kontraktprüfung, Hashes/No-Loss-Impact und Mobile-/Keyboard-/Browsertests. Die Startseite bleibt zunächst unverändert.

**S7 – Endabnahme der Sprache**: Nur wenn jeder Pfad sprachlich kohärent, jede Überleitung sachlich tragfähig und jeder geöffnete Block gehaltvoll ist, in die nächsten User Storys und ein breiteres Site-Rollout gehen. Offene Fachfragen müssen nicht erfunden abgeschlossen werden; sie erhalten eigenständige, aussagekräftige Forschungsausgänge.

## 11. Verbindliche Architekturabnahme

- Fünf `LP`-IDs + fünf Therapie-Linsen haben je eine vollständig inventarisierte Frage-/Bedeutungs-/Erkenntniskette mit eindeutigem Status.
- Jedes bestehende Perspektiv-`cross` und jede `mirror`-Relation hat eine geprüfte oder ausdrücklich offene semantische Übergangsakte.
- Kein freigegebenes ausklappbares Element ohne gehaltvollen Inhalt, fachliche Grenzen und angemessene Quellen-/Vertiefungsreferenzen.
- Keine KI-Selbstzuschreibung der Website, keine erfundenen Echtzeit- oder Beratungsfähigkeiten.
- 21 historische Claims und Referenzen unverändert; neue Claims bleiben bis Freigabe vorgeschlagen.
- Wiederkehrende Fachinformationen bleiben unter derselben Eigentümer-ID; Sprachvarianten sind Projektionen, keine neue Fachwahrheit.
- No-Loss-Änderungsprotokoll, interne Link-/Anker-Prüfung und echte Browserabnahme vor Freigabe.
- User Storys beginnen **erst nach** dieser fachlichen Sprach- und Wissensraumabnahme.

**Endzustand:** Nicht „alle Seiten besitzen viele Links“, sondern: Jeder sichtbare Link führt in eine fachlich passende, substanziell erschlossene Welt – und jeder Rückweg erklärt, was der Mensch daraus gelernt hat.
