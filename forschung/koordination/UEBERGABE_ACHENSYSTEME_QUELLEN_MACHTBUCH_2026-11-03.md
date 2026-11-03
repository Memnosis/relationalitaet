# Übergabe an Website-KI und Projektkoordination — Achsensysteme, Quellenstatus, Promptauftrag

**Stand:** 2026-11-03 · **Art:** fachlicher Übergabe-/Entscheidungsbericht · **Geltung:** KEINE Website-Implementierungsfreigabe durch diese Datei.  
**Wichtig:** Die Website wird von einer zweiten KI bearbeitet. Die hier dokumentierende KI nimmt **keine Änderungen an `docs/`, Navigationsskripten, Stylesheets oder Website-Assets** vor. Jede künftige Änderung erfolgt durch die verantwortliche Website-KI und wird mit Commit, Seitendiff, Test, Wirkung, Regression und offener Entscheidung rückgemeldet.

## 1. Verständliche Darstellung der beiden Achsenmodelle

### A. Historische neutrale Feldsprache — Tensor-Basics / Tensor v1.0 (21.03.2026)
Ein Feld wird durch **drei Klassifikationsfragen** adressiert:
1. **Grundzustand:** NM = Baseline/Rel0; ZM = Emergenz/Rel-Rel; UM = Identität/Rel1.
2. **Klassenlage:** I = Kern; II = Kreislauf; III = Öffnung.
3. **Modus:** α = Struktur; β = Funktion; γ = Relation.

Beispiel: `ZM-II-β` bedeutet *Emergenz / Kreislauf / Funktion*. Das ist eine neutrale Beschreibung eines Prozess- oder Umlaufphänomens, noch keine konkrete Algorithmus-Spezifikation. Das Originalpaper enthält die komplette neutrale 27er-Feldsprache und die methodische Trias Ont/Op/Th (Ontologie, Operation, These). Es benennt `ρ` und einen möglichen Rückoperator `ρ⁻¹`; eine Umkehrabbildung muss im Fachmodell begründet werden, nicht aus dem Symbol allein folgen.

### B. Neuere operative Triaden — Tensor 2.0, Achsenalgebra v2.3, Gesamtstudie v5.3
Hier werden drei **inhaltliche Prüfrollen** gekreuzt:
1. **T1 Beziehung:** verbunden / getrennt / unterschieden, aber bezogen.
2. **T2 Gestalt:** Ganzheit / Teil / Relation.
3. **T3 Ablauf:** Impuls / Prozess / Repräsentanz.

Beispiel: *verbunden × Teil × Prozess* bezeichnet eine mögliche Rollenbelegung, für die eine fachliche Operation und ihre Geltungsbedingungen **erst noch festzulegen und zu testen** sind. Die Studie nennt 324 offene Positionshypothesen für zwölf Grundfunktionen. Die Neuheit liegt nicht in „3×3×3=27“, sondern möglicherweise in der Fähigkeit, reale Modelle auf Operatoren, Schnittstellen, Rückkopplung und Gegenprüfungen abzubilden.

### Worin liegen die Unterschiede?
| Dimension | Historische Sprache A | Operative Triaden B | Konsequenz |
|---|---|---|---|
| Zweck | Fachübergreifende Einordnung und Vergleich | Entwurf/Prüfung von Operations- und Prozessrollen | Zwei Perspektiven, keine automatische Alternative |
| Erste Achse | Baseline → Emergenz → Identität | verbunden / getrennt / unterschieden-bezogen | Ein Ablaufzustand ist kein Beziehungsstatus |
| Zweite Achse | Kern / Kreislauf / Öffnung | Ganzheit / Teil / Relation | Eine räumliche/organisatorische Klasse ist keine Teil-Ganzes-Relation per se |
| Dritte Achse | Struktur / Funktion / Relation | Impuls / Prozess / Repräsentanz | Beschreibungstyp ist keine Prozessphase |
| Feld-ID | NM-I-α ... UM-III-γ | T1-Wert × T2-Wert × T3-Wert | IDs nicht überschreiben oder stillschweigend umetikettieren |
| Nachweis | Fachpassung, Vergleich, Ont/Op/Th | typisierte Abbildung, Invarianz, Funktionstest, Gegenmodell | Beide bleiben hypothesengebunden |

**Wichtig:** Das diskrete räumliche Grundmodell `V={0,1,2}³`, mit explizit gewählter Flächenadjazenz `P3□P3□P3` (54 Kanten), ist ein dritter, rein formaler Bezug. Seine mathematischen Beziehungen sind unabhängig von A und B definierbar. Es ist nicht automatisch das semantische Gesetz eines Fachgebiets.

### Was würde eine Entscheidung verändern?
- **A als einzige verbindliche Feldsprache:** bestehende historische Klassifikationen sind leichter wiederzuverwenden, aber die operative T1–T3-Forschung würde ohne saubere Zusatzachse zu einem Untermodell degradiert.
- **B als einzige verbindliche Feldsprache:** auf einzelne Prozesse leichter anzuwenden, aber ältere Feld-IDs und Aussagen würden bedeutungsmäßig verschoben; hoher No-Loss- und Migrationsaufwand.
- **A und B als getrennte Sichten mit typisiertem Crosswalk (empfohlener VORLÄUFIGER DEFAULT):** keine Datenverlustmigration, beide Erklärungen bleiben gültig als *Modelle*, Abbildungen zwischen ihnen müssen einzeln begründet werden. Das Modell gibt **keine behauptete 1:1-Übersetzung** vor.

**Für Nils jetzt keine endgültige Algebra-Abstimmung nötig.** Eine sinnvolle Zustimmung wäre lediglich: „A und B vorläufig getrennt erhalten, Crosswalk testen, keine Felder ohne Nachweis gleichsetzen.“ Über die spätere mathematische oder semantische Kanonisierung wird erst nach Vergleichsversuchen entschieden.

### Welche Fragen sind dafür tatsächlich offen?
- Welches fachliche Beispiel kann gleichzeitig unter A und B beschrieben werden, **ohne** zusätzliche Interpretationen zu erfinden?
- Welche Rollen entsprechen sich strukturell, welche nur metaphorisch, welche überhaupt nicht?
- Was bleibt bei einer Übersetzung invariant: Daten, Operator, Ausgangstyp, Inverse, Gesetz?
- Ist das dritte Element fachlich irreduzibel, oder reicht ein 2er-Modell?
- Verliert die 27er-Produktbelegung Typinformation, oder bringt sie einen nachweisbaren Vorteil gegenüber Graph/Automat/AST?

## 2. Welche Quellen werden verwendet?

**Interne Original-/Forschungsquellen (primäre Belege für den Stand des *eigenen Modells*, nicht Belege einer universellen Naturgesetzlichkeit):**
- `Tensor-Basics-Grundlagen_.md` (hochgeladen, 21.03.2026), Abschnitte 3–7 und 9–14; historische neutrale Achsen und Ont/Op/Th.
- `KI_Tensor_Gesamtarchiv_No_Loss_2026-10-29(1).md`, §§3, 4, 6–9; getrennte Achsenmodelle, Graph-/Mitte-Tests, E0–E5-Erkenntnisstufen.
- `00_Gesamtstudie_v53(1).md`, §§1–4 und 7–10; T1–T3, zwölf Funktionsfamilien, 324 Positionshypothesen, falsifizierbare Gegenmodelle.
- `00_Paper_Achsenalgebra_und_Komposition(1).md`, §§1–8; Kontaktgraph, Laplace-Kronecker-Summe, Kopplungsmodi und Grenzen des Formmodells.
- Weitere historische Unterlagen: `00_Gesamtwerk_V44(1).md`, `01_100_Welten_Prioritaeten_und_Nachweisluecken(1).csv`, `02_5_Modelle_135_Kombinationen(1).csv`, Quellen-/Glossarregister.

**Externe etablierte Mathematik-/Methodenanker aus den Papern, deren genaue Anwendung auf unsere eigenen Behauptungen noch Claim-bezogen zu prüfen ist:**
- Fong & Spivak, *Seven Sketches in Compositionality* (2019): https://arxiv.org/abs/1803.05316
- Kolda & Bader, *Tensor Decompositions and Applications* (2009): https://doi.org/10.1137/07070111X
- W3C PROV-O, https://www.w3.org/TR/prov-o/ (Entity/Activity/Agent, nicht drei mathematisch unabhängige Trinitätsachsen).
- Gene Ontology, https://geneontology.org/docs/ontology-documentation/ (drei Aspekte, keine frei austauschbaren Achsen).
- Baez/Fong/Pollard, *A Compositional Framework for Markov Processes*, https://arxiv.org/abs/1508.06448
- Graph-Laplace- und kartesische Graphprodukte: mathematische Referenzen aus Achsenalgebra v2.3.
Keiner dieser Anker allein beweist die fachübergreifende KI-Tensor-These. Externe URLs sind **hier bibliografische Ausgangspunkte**, keine dokumentierte digitale Volltextprüfung in dieser Übergabe.

## 3. Forschungspriorität: Sechs Referenzwissenschaften
**Phase 1:** Geometrie, Logik, lineare Algebra, Graphentheorie. Grund: klare mathematische Träger, kontrollierbare Beispiele, Unterscheidung formaler Strukturen und interpretierter Rollen, häufig digitale Quellen und reproduzierbare Gegenproben.  
**Phase 2:** Dynamik und Chemie. Grund: reale Prozesse, zeitliche Übergänge, stöchiometrische und andere Erhaltungssätze, zusätzliche Parameter, Datenschnittstellen und fachliche Validierung.

Dies ist eine Priorisierung der **fachlichen Testarbeit**, nicht die Behauptung, diese Wissenschaften seien bereits vollständig in die Tensoralgebra integriert. Eine andere Reihenfolge kann aus neuen Quellen-/Testfunden folgen.

## 4. Neue Quellenstatus-Logik (getrennt von Evidenzqualität)
Es gibt **vier eigenständige Statuswerte**:
- `digital_verifiziert`: Wortlaut/Fundstelle tatsächlich gegen digital zugängliche Quelle geprüft (belegbar: URL/Datei, Version, Fundstelle, Prüfdatum, Prüfer, Claim-ID). Das sagt noch nichts darüber, ob eine zusätzliche eigene Hypothese wahr ist.
- `digital_nicht_erreichbar`: Quelle bibliografisch bekannt, aber in der dokumentierten Prüfung digital nicht erreichbar. Keine erdachte Fundstelle.
- `handpruefung_noetig`: Papier/Bibliothek/Scan oder fachliche Prüfung erfordert händische Einsicht; konkrete Prüfanweisung und Nachweisblatt.
- `nur_nils_digital_geprueft`: Nils hat digital geprüft; Quellnachweis/Vertraulichkeit oder fehlender öffentlicher Zugang lassen dies für andere noch nicht reproduzierbar erscheinen. Sichtbarkeit und Nils-Bestätigung gesondert dokumentieren.

**Offene Quellenprüfungen sind mögliche öffentliche Mitmach-Aufgaben**, sofern Quelle/Rechte/Personendaten und konkreter Arbeitsauftrag freigegeben sind. Eine nur von Nils geprüfte Quelle nicht als öffentlich digital verifiziert deklarieren, bevor ihr Nachweis zugänglich ist.

Jeder Quelle und jeder einzelnen Aussage werden **Quelle**, **Verfügbarkeitsstatus**, **Prüfstatus**, **Prüfer**, **Prüfdatum**, **Evidenzstatus**, **Sichtbarkeit**, **offene Prüfaufgabe** zugeordnet. Prüfung der Zugänglichkeit und wissenschaftliche Evidenz sind unterschiedliche Dimensionen.

## 5. Präzisierung zur neuen Machtbuch-Ausarbeitung
Die **Ausarbeitung des neuen Machtbuchs besteht derzeit aus Prompts und didaktisch strukturierten Forschungs-/Redaktionsaufträgen**. Es ist **nicht** automatisch ein fertig geschriebenes oder druckreifes neues Buch.

- Buchprompts nach Prompt-Ebene (Frage/Synthese), Agenten-Ebene (Rollen/Quellenprüfung), Meta-Ebene (Systemkontext und Grenzen) entwickeln, ausführen, redigieren und über Quellregister versionieren.
- Vorhandene Publikationen, Cover und Medien nicht überschreiben; neue Buchfassungen erst nach redaktionellem Entscheid.
- Die aktuellen Prompt-/Arbeitsbestände können in einem eigenen internen Register geführt werden. Nur analysierte und redaktionell freigegebene Nutzungsfassungen kommen öffentlich in Betracht.
- Die Website-KI erhält aus diesem Bericht lediglich die **Übergabeanforderungen**; daraus folgt keine Freigabe, eine neue Buchseite oder PDF zu generieren.

## 6. Abstimmung mit der zweiten KI — eindeutige Zuständigkeit

**Hier:** Forschungsmodelle erklären und vergleichen, Quellenstatus und Aufgabenregister fachlich entwickeln, Tests und Entscheidungen protokollieren, Git-Berichte für Abstimmung anlegen.  
**Zweite KI:** Website-Seiten, Navigation, CSS/JS, Projektansichten und Dashboard implementieren; dabei die bestehenden Inhalte bewahren, neue Aufgaben erst nach Veröffentlichungsgate freigeben.  
**Nils:** Wahl der Forschungsprioritäten, Konfliktentscheidungen, redaktionelle/publizistische Freigabe. Ohne akuten Konflikt ist keine manuelle Freigabe einfacher Forschungs- und Rechenarbeiten nötig.

### Kommunikationsvertrag
Für jedes nachfolgende Arbeitspaket dokumentieren:
`ID | Datum | Originalauftrag | Ausgangsdateien | Quelle/Version | Änderung/Commit | Test & Ergebnis | offene Punkte | Entscheidung nötig? | Website-Auswirkung | zuständige KI | nächste Übergabe`.

**An die Website-KI aus diesem Dokument:**
1. Bestehende `docs/`-Inhalte nicht ersetzen oder kürzen.
2. Quellenstatus als separate Facetten von Evidenz und Promptfreigabe führen; vor Gestaltung die Datenstruktur mit dem Forschungsregister koordinieren.
3. Prompt-Karten nach konkretem Kontext und nach Prompt-/Agent-/Meta-Ebene ergänzen; keine ungeprüften Meta-Entwürfe als geprüfte Mitmach-Prompts kennzeichnen.
4. Priorisierte öffentliche Quellenprüfungen können eigene Mitmach-Aufgaben werden; interne Architektur-Crosswalks nicht als offene Entwicklungsanleitung veröffentlichen.
5. Änderungen nur durch Website-KI durchführen, mit Regressionstests und Git-Bericht zurückmelden.
6. Neue Machtbuch-Ausarbeitung weiterhin als **Prompt-/Forschungsprozess** behandeln; keine automatische Buchpublikation.
7. Dieses Dokument ist eine Aufgaben-Übergabe und kein Seitentext; redaktionelle Metahinweise gehören nicht auf die öffentliche Website.

## 7. Offene Entscheidungen und empfohlenes Vorgehen

| ID | Frage an Nils | Vorläufige Empfehlung | Wann endgültig entscheiden? |
|---|---|---|---|
| DEC-AX-01 | Soll A oder B die andere Achsensprache ersetzen? | **Nein.** Beide getrennt versionieren, Crosswalk prüfen. | Erst nach Beispielen/Tests |
| DEC-SCI-01 | Welche Wissenschaften zuerst? | Geometrie, Logik, lineare Algebra, Graphentheorie; dann Dynamik, Chemie. | Arbeitsreihenfolge kann sofort als Standard gelten |
| DEC-SRC-01 | Welche Quellen stehen nur Nils digital offen? | Separaten Status führen, keine externe Vollprüfung behaupten. | Bei konkreter Quelle |
| DEC-BOOK-01 | Ist neues Machtbuch redaktionell fertig? | **Nein**, derzeit Prompt-Ausarbeitung. | Nach Kapitel-/Prompt-Review |
| DEC-WEB-01 | Wer bearbeitet Website? | **Nur zweite KI**; hier Berichte und Nachweise. | Bereits durch Nutzer festgelegt |

### Unmittelbare technische Anschlussarbeiten ohne Website-Eingriff
- Datenvertrag für Quellenstatus und Claim-Quellenprüfung erstellen; vorhandenes Glossar-/Quellenregister darauf abgleichen.
- Zwei bis vier echte Achsen-Crosswalk-Beispiele mit Nichtentsprechungen, Testbedingungen und Herkunft dokumentieren.
- Berichte/Tests mit stabilen IDs an die bestehenden Forschungsaufgaben anschließen.
- Prüffähige Quellenlücken als öffentliche Teilaufgaben vorbereiten; noch nicht veröffentlichen.
