# Pilot-50: Ernte von berühmten und komplexen Formeln bis zu Algebra-, Tensor- und Publikationsakten
**Stand 2026-11-04 · Forschungsprotokoll v0.1 · GPT-Pilot · Status: strukturgeprüft und punktuell symbolisch nachgerechnet, nicht fachlich abgenommen**

## 1. Ausgangslage und Frage
Nils verlangt, dass auch KI-Analysen **automatisch** in der richtigen wissenschaftlichen Sammlung landen und die Tensoralgebra über ein wachsendes Evidenzregister lernt. Die Prüfung setzt hierfür 50 aus Claudes existierendem Top-100-Formelsatz ausgewählte, bekannte und in unterschiedlicher Weise anspruchsvolle Gleichungen ein. Die Auswahl umfasst sieben Fachgebiete (5 Mathematik, 28 Physik, 8 Chemie, 5 Biologie, 2 Informatik, 1 Statistik, 1 Ökonomie). Sie ist **keine objektive Rangliste der 50 schwierigsten Gleichungen der Menschheitsgeschichte**. Dem Quellmaterial fehlen beispielsweise vollständig ausformulierte Einstein-Feldgleichungen, Yang-Mills, Navier–Stokes als PDE, Schrödinger-Eigenwertsysteme und Riemannsche Zeta-Identitäten. Diese dürfen nicht ohne neue, korrekt belegte Quellen erfunden werden.

## 2. Unveränderte Quellen und gespeicherte Artefakte
- `FORMELN50_KORPUS_V0_1.json`: exakt 50 Auswahlobjekte aus `forschung/tensor/formeln/FORMELN_TOP100_V0_1.json` inklusive Original-IDs, Formelausdrücken, überlieferter Größenbenennungen und konstanter Symbole; Archiv-BLOB-ID und Selektionsbegründung.
- `PILOT50_STRUKTURERGEBNIS_V0_1.json`: alle 50 Rolle/Symbol-Kandidaten, Identifizierungsstatus und 39 gleiche-Begriffe-Kanten; keine semantische Freigabe.
- `PILOT50_GRAPHMUSTER_V0_1.json`: 33 Dreierverbände mit Topologie und offenem Evidenzstatus.
- `forschung/tensor/algebra-claude/FORMELN50_GPT_RELATIONEN_V0_1.json`: vier positive, aus bekannten Gleichungen gewonnene Relationen, ein abstrakter Stern-Eliminationsnachweis sowie sechs konkrete Prüf-/Gegenbefunde.
- `run50.py`: reproduzierbarer SymPy-Test mit den vorhandenen 50 Formeldaten; der ursprüngliche GPT-Gegenlauf wurde lokal mit SymPy 1.14.0 und 50 originalgetreu übernommenen Gleichungsstrings ausgeführt (50/50 als Gleichungen parsebar). Ein vollständiger reproduzierter Zweitlauf des *Github-Skripts* und ein unabhängiges Algebra-Backend sind vor abschließender Freigabe separat zu prüfen.
- `forschung/koordination/harvest_antwort.py`: explizite Markdown-Antworten/Analysen in eine **No-Loss-Forschungsakte** mit Kandidatenfacetten und Änderungsbedarfen umwandeln; keine heimliche Chatschnittstelle.

## 3. Auswertung der 50 Formeln (tatsächlich berechnete Kandidaten)
| Strukturmerkmal | Ergebnis | Bedeutung |
|---|---:|---|
| Selektierte Quelldatensätze | 50 | Kuratierte, nicht repräsentative Teilstichprobe |
| SymPy-Gleichungseinlesung, unabhängige lokale Implementierung | 50/50 | Syntax, **nicht** physikalische Wahrheit |
| Gleichungen mit exakt drei erfassten Variablenschlüsseln | 21 | Trinitäts**kandidaten**, inklusive nichtlinearer/DGL-Sonderfälle |
| Je 1/2/3/4/5/6 Symbole | 1 / 7 / 21 / 14 / 6 / 1 | Nur quellmetadatengestützte Arity |
| Formeln mit mehrfacher gleichlautender Rollenbeschreibung | 11 | Begriffsgleichheit != Identität der mathematischen Größe |
| Differentialgleichungen | 5 | Separater Dynamik-/Zustandsraum-Skill erforderlich |
| Kanten bei gleichen Beschreibungswörtern | 39 | Unbewiesene Graphkandidaten |
| Paarweise verbundene 3er-Formelmuster | 33 | 23 Sterne / 2 strenge Dreiecke / 8 gemischte |
| Vier bekannte Relationen separat symbolisch bestätigt | 4 | Algebra, **noch keine allgemeine Fachabnahme** |
| Abstrakte Stern-Elimination separat bestätigt | 1 | Methodennachweis, keine neue Formel des 50er-Korpus |
| Markierte fachliche/semantische Risiken | 6 | Review- und Gegenprüfauftrag |
| Mathematisch voll belegte Projekt-Tensoren mit 27 Positionen | 0 | Kein automatisch generiertes Tensorfeld als bewiesen ausgeben |

**Die strengen Formeldreiecke:** `F025+F026+F027` und `F044+F080+F081`. Das elektrische Beispiel `F031+F032+F033` ist graphisch gemischt: Zwei gemeinsame Variablenpaare und die Stromstärke erzeugen mehr als eine Kante; die daraus folgende Relation `P=R I²` ist schon F033.

## 4. Algebra-Ergebnisse – belegte Rechenwege und Domains
**R1 Arbeit/Leistung/Geschwindigkeit:** `W=F*s`, `P=W/t`, `v=s/t` => `P=F*v`. Eingeschränkte skalare Bewegung entlang der Kraft; allgemein `P=F·v` als Skalarprodukt und Leistung ist zeitliche Arbeitsrate. `t != 0` für Quotientendefinition.
**R2 Elektrik:** `U=R*I`, `P=U*I` => `P=R*I**2`. Ohmsches Modell; **Bereits in der Ausgangssammlung F033**. Eignet sich als Rückgewinnungs-/Konsistenzprobe.
**R3 Stoffmenge:** `rho=m/V`, `n=m/M`, `c=n/V` => `rho=c*M`. Gleiche stoffliche Komponente und konsistentes Volumen; für Lösungen ist die Gesamtdichte nicht pauschal `c_i M_i`.
**R4 Impuls/kinetische Energie:** `p=m*v`, `E_kin=m*v**2/2` => `E_kin=p**2/(2*m)`, `m!=0`, nichtrelativistische Näherung.
**R5 Stern (abstraktes Negativargument gegen Nur-Dreiecke):** `X=A*B` und `X=C*D` => `A*B=C*D`, wenn X tatsächlich identisch ist. Diese zwei Gleichungen sind eine allgemeine algebraische **Methode**, kein Beleg dafür, dass alle 23 gefundenen Wortsternmotive gültig sind.

Alle fünf separaten Rechenkontrollen ergaben Residuum null in einem eigenständigen lokalen Python-Skript mit SymPy 1.14.0. Das ist eine **getrennte Implementierung auf demselben symbolischen Backend**, keine vollständig unabhängige Formelbeweismaschine.

## 5. Negativfunde für das neue Algebra- und Quellenregister
- `F065` Heisenberg-Unschärferelation als reine Gleichheit im Originalkorpus; übliche allgemeine Relation ist eine untere Schranke (`>=`). Der historische Wortlaut braucht Quellen- und Kontextprüfung.
- `F023` und `F037`: „Energie“ bezeichnet kinetische und Ruheenergie; derselbe Mengenname darf nicht als gleiche physikalische Größe verknüpft werden.
- `F021` und `F080`: Masse in Newtons Dynamik und molarer Stoffmengenrechnung muss erst nach Bezugssystem und identischem Träger geprüft werden.
- `F005`: nur einer von zwei Wurzelzweigen, (a \neq 0), Diskriminante und reell/komplex unterscheiden.
- `F006`: (V-E+F=2) ist an geeignete Topologie (insbesondere Geschlecht null) gebunden, nicht für alle geometrischen Flächen.
- `F017` und `F018`: exponentielles und logistisches Wachstumsmodell sind unterschiedliche Dynamiken; identische Variablennamen ersetzen keine Modellwahl.

Diese Akten müssen erhalten bleiben, **auch wenn alle fünf positiven symbolischen Tests erfolgreich waren**.

## 6. Prozesszustände: Was haben die 50 wirklich erreicht?
| Gate | Status / Zahl | Nächste zwingende Handlung |
|---|---|---|
| S0 Ursprung/Provenienz | 50 originalgetreu kopierte Quellenformeln | DOI-/Fachquelle pro Formel nachziehen |
| S1 Parser | 50/50 im lokalen SymPy-Kurzlauf | Claude-Pipeline für denselben Eingabestand separat laufen lassen |
| S2 Fachsemantik + Einheit | 0 vollständige Prüfnachweise | Größenidentität, Referenzkörper, Einheiten und Definitionsbereiche typisieren |
| S3 Kanonische Normalform | Strukturmerkmale und Rollen gespeichert; **keine** universell beweiserhaltende Normalform | domain-erhaltende Normalisierung testen |
| S4 Mustergraph | 21 Dreierkandidaten, 39 Kanten, 33 3er-Verbände | falsche Gleichnamigkeit/Gegenmodelle automatisch aussortieren |
| S5 Ableitung | 4 bekannte Relationen + 1 abstrakter Sternnachweis | für weitere Muster mathematische Herleitungen versuchen, Abbruchgründe speichern |
| S6 Gegenprüfung | 6 Negativ-/Risikofunde | systematische Feld-/Fachexpertenprüfung |
| S7 unabhängige Reproduktion | getrennte Python-Skriptrechnung auf SymPy; kein Zweit-Backend | unabhängige Rechnung und eingefrorener Rohdatensatz |
| S8 3 Trinitäten / 27 Feldpositionen | 0 abgeschlossene Tensoren | gemeinsame mathematische Operatoren und negative Felder dokumentieren |
| S9 wissenschaftliche Fachabnahme | 0 Gesamtfreigaben | Reviewer/Quellen prüfen |
| S10 Publikation | öffentliche Entwurfsakten, keine bestätigte neue wissenschaftliche Publikation | Redaktionsfreigabe nach FPP-01 |

**Jeder Status besitzt rückwärts gerichtete Kanten**, z. B. F065 → Quellenkorrektur → Formelbestandsversion → neue Ableitung → Papers mit betroffener Formel neu prüfen. Keine Ergebnisse löschen.

## 7. Was wird unter welchen Vektoren gesammelt?
Die vorläufigen Facetten sind **Ordnungshilfen, keine Tensorachsen ohne Beweis**:
1. **Objektart:** SRC, FORM, MOD, REL, TRI, TEN, FIEL, TEST, PROOF, SKILL, ANALYSIS, PAPER.
2. **Fachgebiet und Kontext:** Mathematik/Physik/Chemie/Biologie/Informatik/Statistik/Ökonomie; Modell, Träger, Zeit, Bestand.
3. **Mathematische Signatur:** Variable und Rolle, Dimension, Operator, Algebra/Graphmuster, Domain, Invariante, Umkehrbarkeit.
4. **Prüfung/Evidenz:** Strukturstatus, Rechenstatus, Fachevidenz, Gegenbefund, externe Replikation, Neuheitsgrad.
5. **Herkunft:** Quellen-IDs, Formelfundstellen, Autor/KI, Versionen, Input-/Code-/Ergebnis-Hash.
6. **Abhängigkeiten und Ziele:** betroffene Algebra-Paper, Tensor-IDs, Skills, Glossar/Quellen, Methodenpaper, Website, freigegebene Releases.
7. **Forschungswert:** bekannt und rekonstruiert, neue Korpusbeziehung, neue wissenschaftliche Behauptung, widerlegt, offen.

Die Facetten werden über typisierte Kanten als **Mehrfachzuordnung** verwendet, nicht als starres `eine Erkenntnis → eine Datei`.

## 8. Harvesting von KI-Antworten (was tatsächlich automatisch möglich ist)
Mit `forschung/koordination/harvest_antwort.py` existiert ein **expliziter, verlustfreier Import** von Markdown-Antworten und KI-Analysen:
- Eine Antwort wird mit SHA-256, Akteur, optionaler Quell-URL, vollständigem Rohtext und Abschnitts-IDs gesichert.
- Jeder Abschnitt erhält **Kandidatenfacetten** (Algebra, Tensor, Skills, Quellen, Glossar, Methode, Paper, Website) und mögliche Zielakten.
- Die Auswertung erzeugt nur einen **FPP-Entwurf**: `not_assessed` für wissenschaftlichen Status; Daten bleiben privat, bis eine separate Freigabe vorliegt.
- Weiterer Compiler führt Dublettenabgleich, fachliche Behauptungsextraktion, IDs, Gegenproben, Paper-Impact und Freigabe aus. Dieser Teil ist **noch nicht fertig implementiert**.
**Wesentliche Systemgrenze:** ChatGPT- und Claude-Antworten werden nicht automatisch allein durch ihre Existenz im Chat in GitHub gespeichert. Erforderlich ist ein expliziter Export bzw. eine integrierte Übergabeschnittstelle und ein aktivierter Repo-Workflow. Ein GitHub-Kommentar ist noch kein Claude-ACK.

## 9. Konkreter No-Loss-Nachziehplan des Batches
**Primärakten gespeichert:** 50 Rohformeln im Pilotkorpus, 50 Strukturdatensätze, 33 Muster-IDs, fünf Rechen-/Methodennachweise, sechs Risikofunde.
**Algebra:** `FORMELN50_GPT_RELATIONEN_V0_1.json`; vier formal gültige Substitutionsbeziehungen samt Domain, Stern-Elimination als Methodenskill.
**Harvesting:** dieser Bericht und die Musterdateien; Lernparameter Fehlmuster und Parser-/Graphmetriken.
**Tensor:** zwei konkrete trinitäre Kandidatenverbünde, noch **nicht** drei eigenständige mathematische Trinitäten als belegter 27er-Tensor.
**Quellen/Glossar:** Änderungsbedarf für F065, Modellkontexte und Einheiten; **kein** ungeprüfter Merge in Altbestände.
**Skillbibliothek:** Bedarf an `equation_parser`, `quantity_identity`, `domain_guard`, `symbolic_elimination`, `graph_motifs`, `counterexample`, `repro_runner`, `impact_router`. Bereits vorhandene Parser/SymPy-Algebrafunktionen wiederverwenden.
**Papers:** Algebra erhält bestätigungsbedürftige Relationen, Methoden-/Strukturpaper erhält Ergebnisse zur Such- und Fehlerstruktur, Tensorgrundlagenwerk erst nach eigener Tensorprüfung.
**Website:** Übersicht mit Prüfgrenzen verlinken, aber keine 33 Tensoren oder neue wissenschaftliche Gesetze behaupten.

## 10. Nächster wissenschaftlicher Zyklus
1. Gegenlauf von Claudes Formelskelett und Triadengraph auf exakt denselben 50.
2. S2: echte Größen-IDs und Dimensions-/Kontextgraph; 39 Kanten bereinigen.
3. S5: alle überlebenden Stern-/Dreieck-/gemischten Verbände algorithmisch eliminieren, Fehlschläge protokollieren.
4. S6: absichtlich falsche Kollisionen und unzulässige Fallgleichsetzungen mit Goldstandard prüfen.
5. S8: die besten Verbände T1→T2→T3 mit Operatorbrücken und 27 geprüften Positionen versehen; Gegenfälle und leere Positionen nicht verstecken.
6. FPP-01-Impact-Compiler aus den realen Primärakten bauen und zuerst **nur** Änderungsentwürfe generieren.
7. Nach Claudes Review/Redaktionsfreigabe Versionen der Algebra, Glossare, Quellenregister und Fachpaper aus den Akten aktualisieren.

**Gesamturteil:** Die Methode kann bekannte Dreierbeziehungen und neue (im Bestand fehlende) Ausdrücke auffinden; der Engpass bleibt semantische Typisierung und wissenschaftliche Geltung, nicht die Zahl der Muster. Die Speicherung in den vorgesehenen Fachbereichen wurde für diesen Pilot gestartet, eine vollautomatische Kette bis zur Publikationsfreigabe ist noch nicht fertig.
