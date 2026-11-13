# Skillsammlung v0.1 · Forschung, Text, Publikation, Vertrieb, Marketing, Social Media

Die Sammlung beschreibt **alle Tätigkeiten**, die eine Publikation von der Forschung bis zur Leserin durchläuft. Jeder Skill hat Zweck, Eingabe, Ausgabe, Werkzeug, Qualitätsregel, Verantwortliche und einen Meta-Prompt der Form „Entwickle einen Prompt für …“. Die Sammlung erweitert das Methodenregister `STANDARDS_SKILLS_METHODENREGISTER_V1` (SK-NOLOSS bis SK-CONDENSE).

## Generatoren: Upgrade-Bausteine, die sich auf viele Werke anwenden lassen

Viele Schritte von Version 1.x zu 2.0 wiederholen sich in jedem Werk. Ein Werk bekommt einen **Upgrade-Vektor**: Für jeden Generator steht dort *auto*, *halbautomatisch*, *Text mit KI*, *Entscheidung* oder *entfällt*. Was nicht generierbar ist, wird als **Zwischenelement** geplant, also als eigene Forschung, Ausrichtung oder Marketingentscheidung.

| Generator | Inhalt | getragen von |
|---|---|---|
| G1 | Mindeststandard-Abgleich (alle Listen und Kapitel der alten Fassung bleiben) | SK-D01, SK-D02, SK-D03, SK-T01, SK-T09, SK-W02, SK-K02 |
| G2 | Nachrechnung und Errata-Kapitel | SK-R01, SK-T02, SK-T09, SK-M03, SK-S01, SK-K02 |
| G3 | Gemeinsame Klassenachse I Identität · II Baseline · III Emergenz | SK-D02, SK-W02 |
| G4 | Tensor mit 27 Feldern und Algebra-Lauf | SK-R03, SK-R04, SK-R05 |
| G5 | Erstbelege und Wissenschaftsgeschichte | SK-R06, SK-R07, SK-T04, SK-T06, SK-S02 |
| G6 | Neuheitsmarken: bestätigt · neu formuliert · neu | SK-R02, SK-R06, SK-R08, SK-R10, SK-T04, SK-M02, SK-S05 |
| G7 | Formel- und Dimensionsprüfung | SK-R01, SK-R03, SK-R04, SK-R09 |
| G8 | DE/EN-Paar zu einem zweisprachigen Werk zusammenführen | SK-D03, SK-T07 |
| G9 | Lesetiefen E1 · E2 · E3 | SK-T01, SK-T03, SK-T06, SK-S03 |
| G10 | Fassungen frei / Buch und Preisstufe | SK-T05, SK-T06, SK-P03, SK-V01, SK-V02, SK-V04, SK-M01, SK-W01, SK-K02 |
| G11 | Cover und Serienlayout | SK-T08, SK-P02, SK-S04, SK-W01 |
| G12 | Metadaten: DOI, Versionen, Ko-fi-Link | SK-D04, SK-D05, SK-P01, SK-P03, SK-V03, SK-M03, SK-W01 |

**Zwischenelemente** (nicht generierbar): Forschung (z. B. Nullmodell, Nachrechnung neuer Gebiete), Ausrichtung (Zielgruppe, Kontext sensibler Themen), Marketing (Leitfrage, Community-Weg), Vertrieb (Preisstufe, Bundle), Freigabe durch den Autor.

## Forschung

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-R01 | Nachrechnung von Kernrechnungen | jede nachrechenbare Stelle eines Werks unabhängig neu rechnen | Python + sympy/mpmath (Muster in forschung/register/gegenrechnung/) | jeder Fehler zweimal unabhängig gerechnet; keine Wertung von Thesen | Claude | entwurf |
| SK-R02 | Nullmodell und Permutationstest | prüfen, ob ein Muster häufiger ist als der Zufall | forschung/tensor/formeln/dschungel.py (Permutation), Periodizitätstest | Hypothese vor dem Test festlegen; Startwert fest | Claude | vorhanden |
| SK-R03 | Formelreduktion und Harvesting | Formeln auf Ministrukturen, Trinitäten und Bezugstensoren reduzieren | forschung/tensor/formeln/formel_struktur.py, dschungel.py | Zählungen aus den Daten; Rollenprüfung bei Vorhersagen | Claude | vorhanden |
| SK-R04 | Tensor aus physikalischem Modell belegen | 27 Felder eines Tensors mit Größen eines Modells belegen und prüfen | Kerntensor-Skript (privat bis Freigabe) | Einheiten aller Felder geprüft; Rückkehr-Regel je Klasse numerisch | Claude | entwurf |
| SK-R05 | Typisierte Algebra | Pfade typisieren, Regel U, Achsenregel, Vergleich und Überlagerung | forschung/tensor/algebra-claude/typalgebra.py | P1 Aussageerhalt · P2 neu · P3 reproduzierbar | Claude | vorhanden |
| SK-R06 | Stand-der-Wissenschaft-Recherche (Deep Dive) | Forschungsstand zu einer Frage mit Quellen erheben | Websuche + Quellenprüfung | nur geprüfte Quellen; Gegenposition benennen | Claude | entwurf |
| SK-R07 | Erstbeleg und Wissenschaftsgeschichte | je Begriff Person, Jahr, Werk, DOI/ISBN finden | Atlas + Recherche | Jahreszahlen nie aus dem Gedächtnis; Prüfziffer bei ISBN | Claude | entwurf |
| SK-R08 | Neuheitsprüfung | jede Aussage als bestätigt, neu formuliert oder neu einordnen | Entwurf | „neu“ nur mit Nachweis; Bestätigungen würdigend formuliert | Claude, Gegenlesung GPT | entwurf |
| SK-R09 | Fixsterne und Dimensionsprüfung | Konstanten und Größen relational aufbereiten; Formeln dimensional prüfen | forschung/tensor/formeln/dschungel.py (Dimension), Fixsterne-Liste | Werte mit Quelle (CODATA, PDG, Planck) | Claude | vorhanden |
| SK-R10 | Rollenprüfung (P1) | prüfen, ob gleichnamige Größen dieselbe Rolle haben | forschung/tensor/formeln/datensatz/rollenpruefung_v0_1.csv | zwei unabhängige Urteile; Übereinstimmung messen | Claude + GPT + Mitwirkende | vorhanden |

## Daten

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-D01 | Listenimport aus PDF | Begriffslisten aus Spaltentext verlustfrei importieren | forschung/atlas/import_begriffe.py | Fundzeile und DOI je Eintrag; Bereinigung als eigenes Feld | Claude | vorhanden |
| SK-D02 | Register-Upgrade | Register auf 2.0 heben: Lücken, Dubletten, Klassenachse, Kennzeichnung | Register-Skript (privat bis Freigabe) | nichts löschen; jede Änderung mit Grund | Claude | entwurf |
| SK-D03 | Atlas-Verknüpfung | Synonyme, DE/EN, Pol-übergreifende Begriffe verbinden | Entwurf | Verknüpfung nur mit Begründung | Claude | entwurf |
| SK-D04 | Werk-Metadaten | DOI, Versionen, Cover, Ko-fi-Link je Werk aktuell halten | Entwurf | eine Quelle je Feld; Widersprüche markieren | Claude | entwurf |
| SK-D05 | Datensatz veröffentlichen | Datenblatt, Lizenz, Erzeugungsskript, Versionierung | forschung/tensor/formeln/datensatz/DATENBLATT.md (Muster) | FAIR; Erzeugung mit einem Befehl | Claude | vorhanden |

## Text

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-T01 | Gliederung Version 2.0 | Plan-Vorlage auf ein Werk anwenden | forschung/koordination/PROGRAMM_VERSION_2_0.md (Vorlage §5) | alle Teile der alten Fassung zugeordnet | Claude | vorhanden |
| SK-T02 | Errata-Kapitel | Korrekturen der Fassung 1.x lesbar darstellen | Entwurf | sachlich, ohne Abwertung; jede Korrektur belegt | Claude | entwurf |
| SK-T03 | Lesetiefen E1 · E2 · E3 | denselben Inhalt allgemeinverständlich, ausdifferenziert und fachlich darstellen | Standard: DESIGN_TEXT_PUBLIKATIONSSTANDARD_V1 | keine unerklärten Fachwörter in E1 | Claude, GPT | entwurf |
| SK-T04 | Würdigende Einordnung | Bestätigungen der Wissenschaft als Ehre der Geschichte formulieren | Entwurf | nie „nur bekannt“; Herkunft nennen | Claude | entwurf |
| SK-T05 | Freie Kurzfassung (wissenschaftlicher Kern) | aus der Buchfassung den knappen, vollständig belegten Kern erzeugen | Entwurf | alle Belege bleiben; nichts Wissenschaftliches fehlt | Claude | entwurf |
| SK-T06 | Buchfassung ausbauen | Geschichte, Beispiele, Erklärung, Arbeitsmaterial ergänzen | Entwurf | verständlich ohne Vorwissen; Quellen claimbezogen | Claude | entwurf |
| SK-T07 | Zweisprachigkeit DE/EN | Paare zusammenführen, Terminologie aus dem Atlas | Entwurf | gleiche Zahlen und Inhalte in beiden Sprachen | Claude | entwurf |
| SK-T08 | Formatausgabe DOCX · PDF · MD | Manuskript in die Ausgabeformate bringen | forschung/koordination/berichte/vorlage/bericht_docx.mjs, pandoc | echte Formatvorlagen, Inhaltsverzeichnis, Prüfung jeder Seite | Claude, GPT | vorhanden |
| SK-T09 | Lektorat und Konsistenz | Zählungen, Versionen, Querverweise, Terminologie prüfen | Entwurf | Zahlen nur aus Daten | Claude | entwurf |

## Publikation

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-P01 | Zenodo-Neuversion | neue Version unter der Konzept-DOI anlegen | Entwurf (Nils lädt hoch) | Konzept-DOI bleibt; Änderungsnotiz verweist auf Errata | Nils, Vorbereitung Claude | entwurf |
| SK-P02 | Cover und Serienlayout | Reihen erkennbar gestalten (Farbe, Icon, Typografie) | Designsystem (GPT) | keine neuen Farbcodes; Originalcover nur mit Freigabe ersetzen | GPT | entwurf |
| SK-P03 | Ko-fi-Produktseite | Angebot ehrlich beschreiben: frei vs. Buch, Updates, Preis | Entwurf | was frei ist, wird genannt; Update-Versprechen definiert | Claude, Nils | entwurf |

## Vertrieb

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-V01 | Preisstufe zuordnen | Werk einer Stufe zuordnen: frei · Buch · Arbeitsmaterial · Lizenz · Bundle · Förderkreis | Entwurf (Preise privat) | gleiche Stufe = gleicher Preisrahmen | Nils, Beratung Claude | entwurf |
| SK-V02 | Bundle und Sammelband | Reihen bündeln, inklusive aller künftigen Upgrades | Entwurf | Inhalt und Update-Umfang eindeutig | Claude, Nils | entwurf |
| SK-V03 | Update-Benachrichtigung | Käuferinnen über neue Versionen informieren | Entwurf | was neu ist, in drei Sätzen | Claude | entwurf |
| SK-V04 | Zugang auf Anfrage | sensible Werke kontextgebunden zugänglich machen | Entwurf | Kontext vor Zugang; keine Geheimnis-Signale | Nils | entwurf |

## Marketing

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-M01 | Zielgruppe und Leitfrage | je Reihe die Menschen und ihre Frage bestimmen | Entwurf | Frage statt Produkt | Claude, Nils | entwurf |
| SK-M02 | Positionierung | einordnen, was das Werk leistet und was nicht | Entwurf | keine Neuheitsbehauptung ohne Nachweis | Claude | entwurf |
| SK-M03 | Ankündigung einer Neuversion | Version 2.0 vorstellen: was neu, was korrigiert | Entwurf | Korrekturen offen nennen | Claude | entwurf |
| SK-M04 | Wirkungsmessung | Downloads, Ko-fi, Newsletter, Reichweite auswerten | Entwurf | nur echte Zahlen; Quelle je Zahl | Claude | entwurf |

## Social Media

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-S01 | Werkstattbericht | monatlich zeigen, was sich 1.x → 2.0 geändert hat | Entwurf | Fehler offen benennen | Claude | entwurf |
| SK-S02 | Begriff der Woche | einen Atlas-Begriff mit Geschichte und Bezug erklären | forschung/atlas/daten/begriffe_v0_1.jsonl (Quelle) | Erstbeleg nennen | Claude | vorhanden |
| SK-S03 | Beitrag aus Paper | Kernaussage plattformgerecht aufbereiten | Entwurf | eine Aussage je Beitrag; Link zur freien Fassung | Claude | entwurf |
| SK-S04 | Beitragsgrafik | Grafik im Designsystem zu einem Beitrag | Designsystem (GPT) | Daten- und Quellenstand in der Grafik | GPT | entwurf |
| SK-S05 | Community und Mitmachen | Fragen beantworten, Mitmach-Aufgaben anbieten (Rollenprüfung, Atlas) | docs/mitmachen.html (GPT) | Bewertungen von Werken nur nach Freigabe | GPT, Claude | vorhanden |

## Website

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-W01 | Seite Version 2.0 pflegen | Stand je Werk, Errata, frei/Buch, Atlas-Einstieg | GPT (Auftrag Issue #3) | bestehende Seiten unverändert | GPT | entwurf |
| SK-W02 | Atlas-Seite | Suche und Filter über Pol, Klasse, Domäne | GPT | Herkunft je Eintrag sichtbar | GPT | entwurf |

## Koordination

| ID | Skill | Zweck | Werkzeug | Qualitätsregel | Owner | Status |
|---|---|---|---|---|---|---|
| SK-K01 | Bericht mit rotem Rahmen | Entscheidungen kurz oben, Erklärungen im Anhang | forschung/koordination/berichte/vorlage/bericht_docx.mjs | R2: jede Entscheidung mit Optionen, Empfehlung, Folgen | Claude, GPT | vorhanden |
| SK-K02 | Upgrade-Planung je Werk | Upgrade-Vektor, Zwischenelemente, Priorität bestimmen | Upgradeplan-Skript (privat) | Zenodo-Gesamtübersicht bleibt privat | Claude | entwurf |

## Meta-Prompts

Alle Meta-Prompts stehen in `SKILLSAMMLUNG_V0_1.json` (Feld `meta_prompt`). Aus jedem entsteht nach dem Designstandard ein ausführbarer Arbeits-Prompt mit Ziel, Quellen, Schritten, Tests, Gegenprobe und Abnahme.

## Nächste Schritte

1. GPT ergänzt eigene Skills für Website, Design und Didaktik und gleicht sie mit `docs/data/skills-oeffentlich-v1.json` ab.
2. Aus den 32 Skills mit Status *entwurf* werden ausführbare Arbeits-Prompts, beginnend mit SK-T01, SK-T02, SK-R08 und SK-M01.
3. Häufig genutzte Skills werden als wiederverwendbare Agenten-Skills im Repo hinterlegt.
