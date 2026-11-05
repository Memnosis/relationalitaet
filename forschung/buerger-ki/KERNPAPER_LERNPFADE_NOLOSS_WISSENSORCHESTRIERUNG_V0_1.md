# Lernen, Handeln, Forschen – dieselben Ergebnisse sinnvoll mehrfach nutzen

## Informationsarchitektur, didaktische Wege und No-Loss-Orchestrierung für Bürger-KI und SOULution

**Kernpaper:** BKI-KERN-IA-001 · **Version:** 0.1 · 05.11.2026  
**Status:** Analyse der tatsächlich bestehenden Hauptseiten und ein erstes maschinenlesbares Routingmodell. Kein vollautomatisch ausgeführter Repo-Crosswalk, kein vollständig implementierter Skill-Compiler.  
**Datenmodell:** [Lernwege und Orchestrierungsregeln](../../docs/data/bki-lernpfade-orchestrierung-v0-1.json).  
**Grundsatz:** Ein Ergebnis hat **eine kanonische Objektidentität**, aber darf **mehrere didaktische Darstellungen** haben. Die Bürger-KI ist ein Skill- und Wissensentwicklungsprojekt, kein Sammelsystem für persönliche Bürgerfälle.

## Abstract

Die Bürger-KI ist von einem ersten Rechts-/Verwaltungspfad zu einem breiten Forschungsverbund aus Zielzerlegung, Begriffslexikon, Weisungsatlas, Hilfeorganisationen, Gesundheit/Pflege, Schulen, Ernährung, historischer Metrik und institutioneller Rechenschaft gewachsen. Eine bloße Kette weiterer Papers erzeugt nicht automatisch bessere Fähigkeiten. Die nächste Architekturaufgabe besteht darin, jedes neue Ergebnis nachvollziehbar **zu seinem fachlichen Eigentümer** zu leiten, seine Abhängigkeiten zu aktualisieren und es zugleich auf verschiedenen verständlichen Lernpfaden wiederzufinden.

Das Paper entwickelt (1) fünf Haupteinstiege, (2) fünf didaktische Lernwege, (3) sechs fachliche Filter, (4) eine zwölfteilige kanonische Objektordnung, (5) einen automatisierbaren No-Loss-Änderungsvertrag und (6) Entscheidungsregeln für **vertiefen oder verweisen**. Der bisherige Bürger-KI-Start und die Tensor-Mitmacharchitektur bleiben organisatorisch getrennt.

## 1. Bestandsaufnahme der tatsächlichen Webarchitektur

### Vorhandene nützliche Stationen

- [Bürger-KI-Übersicht](../../docs/buerger-ki.html) mit bereits sehr vielen Cards, Forschungspapern, einem Forschungsabschnitt und Aufgaben.
- [Vom Anliegen zur Lösung](../../docs/buerger-ki-weg.html): sieben Fragen und der methodische Weg vom Anliegen zu einer prüfbaren Handlung.
- [Begriffe & Ziele](../../docs/buerger-ki-ziele-lexikon.html) samt erstem [Zielpfadlabor](../../docs/buerger-ki-zielpfade.html).
- [Anwendungsfelder](../../docs/buerger-ki-anwendungsfelder.html): Lebensbereichsbezogene Einstiege.
- [Unsere gesellschaftlichen Grundlagen](../../docs/buerger-ki-grundlagen.html): System-/Infrastrukturperspektive.
- [Weisungsatlas](../../docs/buerger-ki-weisungsatlas.html): verwaltungsinterne Quellen, Behördengeltung, Länder und dokumentierte Lücken.
- [Forschungs-/Experimentierlabor](../../docs/buerger-ki-experimentierlabor.md): methodische Einordnung.
- [SOULution](../../docs/soulution.html): übergreifende Projekte und Lösungsverbund.
- [KI-Tensor-Mitmachen](../../docs/mitmachen.html): separates Projekt; **kein** Ersatz für die Bürger-KI-Werkstatt.

### Strukturproblem

Die Bürger-KI-Seite führt zahlreiche neue fachliche Papers direkt auf. Fachliche Inhalte und Arbeitsdokumente sind sichtbarer geworden als **didaktische Entscheidungen**. Für Nutzer ist oft unklar: Was ist Einführung, was praktisches Werkzeug, was Forschungsstand, was Detailnachweis? Außerdem wiederholen sich dieselben Grundfunktionen in verschiedenen Fachgebieten, ohne dass ihre kanonische Skill- bzw. Begriffsidentität sichtbar ist.

**Schluss:** Weitere Themen direkt auf dem Startbildschirm auszubreiten würde die Orientierung verschlechtern. Deshalb fünf Haupteinstiege mit darunterliegenden Fachfiltern; Papers folgen dem Kontext und einer gesonderten Forschungsbibliothek.

## 2. Fünf Haupteinstiege statt einer Themenflut

| Einstieg | Ausgangsfrage | Bestehende Startstation | Sinnvolle Weiterführung |
| --- | --- | --- | --- |
| **Anliegen und Ziele** | Was will ich erreichen? | Vom Anliegen zur Lösung | Begriffsverständnis → Wege/Unterstützung → Ergebnisgrenze |
| **Wissen verstehen** | Was ist das und was wissen wir? | Begriffs-/Zielelexikon | Begriffsvarianten → Quellen → Fachkontext → Prüffrage |
| **Wege und Unterstützung** | Welche Option oder Hilfe ist möglich? | Weisungsatlas plus Fach-/Hilfeverzeichnisse | Zuständigkeit → Voraussetzungen → Alternativen → Hilfezugang |
| **Gesellschaft untersuchen** | Wo scheitert etwas systematisch, und weshalb? | Gesellschaftliche Grundlagen | historischer Vergleich → Messbarkeit → Rechenschaft → Gegenbefund |
| **Forschung und Werkzeuge** | Wie prüfen/entwickeln wir Fähigkeiten? | Forschungslabor und Skillbestand | Hypothese → Quellen/Tests → Ergebnis → Aufwertung |

**Navigation zählt Wege, nicht „Wissenschaftsdisziplinen“**. Gesundheit, Jugend, Sozialleistungen, Arbeitsmarkt, Bildung, Ernährung, Wohnen, Rechtsschutz usw. sind querliegende **Fachfilter**. Eine Person kann das Thema „Pflegeplatz“ vom Alltagsanliegen, von einem Fachbegriff oder von einer systemischen Unterversorgungsuntersuchung aus erreichen.

## 3. Fünf didaktische Lernpfade

### LP-01 – Von der Frage zum möglichen Handlungsweg
**Einstieg:** Alltagsproblem, Ziel oder unerfüllte Leistung.  
**Weg:** Anliegen → Zielzustand → Begriffe → Anforderungen → fachlich passende Wege/Hilfen → Grenzen und offene Rückfragen.  
**Ende des Pfades:** keine behauptete Rechtsdurchsetzung; begründete mögliche Handlungsoptionen.  
**Vertiefung:** Nur bei begründeter Frage in juristischen/medizinischen Spezialpfad; sonst Referenz und Kurzbegründung.

### LP-02 – Vom Begriff zum Verständnis
**Einstieg:** fachlicher Begriff, Behörde oder verwirrende Aussage.  
**Weg:** Lexikon → Mehrdeutigkeit/Begriffssinn → Wikipedia/Wikidata als Orientierung → Fachquellen → Anwendungsfälle.  
**Ende:** eigenerklärte Bedeutung und ihre Grenzen.  
**Vertiefung:** Bei abweichender DE/AT/CH-Bedeutung Fachrechtsvergleich, nicht paralleles Volllexikon auf jeder Seite.

### LP-03 – Von der Situation zur Unterstützung
**Einstieg:** „Wer kann helfen?“  
**Weg:** Anwendungsfeld → Ziel/Angebotsart → örtliche oder überregionale Suchquelle → Zugang, Kosten und Angebot → fachlicher Nachweis.  
**Ende:** passender, dokumentierter Kontaktweg oder ehrlich benannte Angebotslücke.  
**Vertiefung:** Anwalt, Ombudschaft, Fachverband oder Selbsthilfe als **Hilfetyp**, nicht als weitere zentrale Hauptnavigation.

### LP-04 – Vom gesellschaftlichen Problem zur überprüfbaren Rechenschaft
**Einstieg:** Versorgungslücke, Fehlerkultur, historische Entwicklung, Qualitäts- oder Personalfrage.  
**Weg:** Problemgeschichte → Definitions-/Metrikgeschichte → Warnungen/Entscheidungen → reale Umsetzung → Folgen, Unsicherheit und mögliche Verantwortung.  
**Ende:** nachvollziehbare Erkenntnis oder konkret dokumentierte Erkenntnislücke.  
**Vertiefung:** Corona als dokumentierter **Stresstest und Referenzzeitraum**, nur wenn er die konkrete historische Fragestellung verbessert; nicht als Querschnittsthema, das alle Wege verdrängt.

### LP-05 – Von einer Forschungsfrage zur besseren KI-Fähigkeit
**Einstieg:** Fehler, widersprüchliche Quelle, fehlendes Werkzeug oder neue Relation.  
**Weg:** Forschungsfrage → Quelle/Glossar → Test oder Gegenbeispiel → mögliche Regel-/Skilländerung → fachliche Prüfung → Publikationsstatus.  
**Ende:** neuer oder korrigierter kanonischer Wissens-/Skillstand, nicht bloß ein weiteres Paper.  
**Vertiefung:** technische Beschreibung nur dort, wo Implementierung oder Prüfung nötig ist; öffentlich didaktisch die Wirkung erklären.

## 4. Große Übersichten – minimaler sichtbarer Aufbau

**Ebene 0 (Start):** Bürger-KI in 2–3 Sätzen; fünf große Einstiege; eine freie Such-/Begriffsfunktion; ein sichtbarer Verweis auf den Forschungsstand.

**Ebene 1 (je Hauptbereich):** Eine didaktische Einführung, ein typisches Beispiel, 3–6 Unterthemen/Methoden, Verweise auf Werkzeuge und „mehr erfahren“.

**Ebene 2 (Fachbereich):** knappe Zusammenfassung des Problems, Quellenstatus, relevante Ziele/Organisationen/Skills, historische Entwicklung und ausgewählte kritische Fragen.

**Ebene 3 (Deep Dive):** spezifische Rechts-/Gesundheits-/Bildungs-/Sozial-/Messmethodik, Primärquellen und Gegenbeispiele; keine erneute allgemeine Einführung.

**Ebene 4 (Forschungsakte):** vollständige Rekonstruktion, Änderungen, Tests, Abgrenzungen, negative Befunde, maschinenlesbare Register, historische Fassungen.

**Keine weiteren Menüebenen für jede neue Quellfamilie.** Die Tiefe erfolgt durch kontextbezogene Fachkarten, Querverweise und filterbare Bibliothek.

## 5. Ein Ergebnis – eine Eigentümerschaft, viele Darstellungen

| Objekt | Kanonischer Eigentümer | Wiederverwendung |
| --- | --- | --- |
| Quellenfund / Dokumentfassung | Quellenregister | Glossar, Skill, Paper, Fachkarte |
| Fachbegriff / Sinn | Glossar/Konzeptregister | Einführung, Lexikon, Erklärung, Suchfilter |
| Ziel und Erfolgskriterium | Zieleatlas | Alltagsweg, Fallvariante, Wirkungsfrage |
| Norm-/Behörden-/Funktionsrelation | Relationsregister | Rechtsatlas, Praxis, Fachpapier, Skill |
| Hilfsorganisation und Dienst | Anbieterregister | Hilfe-, Jugend-, Gesundheits-, Pflegepfade |
| Messbegriff und Methodenbruch | Metrikregister | Arbeitsmarkt, Bildung, Kliniken, Evaluation |
| überprüfbare Fähigkeit | Skillregister | Anwendung, Lernen, Forschung |
| Test und Gegenbeispiel | Testregister | Skillakte, Wissenschaft, Qualitätsbericht |
| bestätigter/negativer/offener Befund | Ergebnisregister | Fachkarte, Projektstand, Paper |
| Argumentation und Synthese | Paper-Bibliothek | Vertiefung, Literaturpfad |
| Didaktische Darstellung | Lernmodulregister | mehrere Lernwege; keine zweite Fachwahrheit |

**Nicht mehrere Wahrheiten pflegen:** Eine neue Quelle darf die Bedeutung eines bestehenden Fachbegriffs verändern; dann werden die betroffenen Darstellungen über stabile IDs neu erzeugt oder als überprüfungsbedürftig markiert. Das Paper wird als historische Argumentationsfassung erhalten.

## 6. Änderungscompiler und No-Loss-Orchestrierung

### Eingang eines neuen Ergebnisses

Ein Ergebnisobjekt benötigt mindestens:

```json
{
  "event_id": "BKI-EVT-EXAMPLE",
  "source_ids": ["BKI-SRC-..."],
  "research_question_ids": ["BKI-RQ-..."],
  "object_type": "finding",
  "changed_object_ids": ["BKI-FIND-..."],
  "change_kind": "new|corrected|contradicted|superseded",
  "evidence_status": "established|limited|incomparable|missing|unassessed|conflicted|unattributable",
  "proposed_destinations": ["source_register", "skill_register"],
  "impact_ids": ["BKI-GL-...", "BKI-TEST-..."],
  "human_review": "pending",
  "original_text_stored": false
}
```

### Routingentscheidung

1. **`upgrade_existing`** – ein bereits existierender Begriff, Skill, Test, Befund oder Quellenstand erhält neue Evidenz, Ausnahmen oder Versionen.
2. **`add_relation`** – neue, eigenständig begründete Verbindung zwischen bestehenden Objekten.
3. **`new_module`** – erst wenn eine neue Nutzerfrage, Zielklasse oder eigenständige Erklärung entsteht, die sich nicht als bestehender Unterpunkt erklären lässt.
4. **`appendix_only`** – tieferes Paper, historische Tabelle, Daten-/Methodennachweis ohne neue öffentlich notwendige Hauptseite.
5. **`hold_unverified`** – kein öffentlicher Fachschluss, wenn Definition, Rechtsraum, Quelle oder Prüfung fehlen.

**Paper nicht als Auffangbehälter:** Das Paper kann die Gesamtargumentation tragen, aber die konkreten Quellen, neuen Begriffssinne, möglichen Skills, Tests und negativen Befunde müssen in deren kanonische Register eingetragen werden. Die Veröffentlichung **ohne** Nachzug wird als unvollständige Integration sichtbar.

### Technische Pflichtkette

`Eingang → identifizieren → deduplizieren → klassifizieren → Provenienz → Vergleich/Relationsprüfung → Abhängigkeiten → Prüfschritt → Registeränderung → Lernweg-/Website-Projektion → Publikationsakte → Änderungshistorie`.

Dazu sollte ein CI-/Compilerlauf künftig prüfen:
- Quellen-ID existent, Version bzw. Stand bekannt;
- kein stilles Zusammenlegen widersprüchlicher Begriffssinne;
- alle neue Skillbehauptungen besitzen mindestens einen realen Teststatus;
- Quelländerung markiert abhängige Artikel/Skills und historischen Vergleich als recheck;
- Hauptseiten/Deep-Dive-Links verweisen auf existierende Pfade;
- auch **negative** und **unentscheidbare** Ergebnisse bleiben gespeichert;
- keine Originaltextkopien in eigene Handlungsanweisungen;
- keine irreführende Fortschrittsquote aus der Anzahl der Papers.

Diese automatisierte Orchestrierung ist **in dieser v0.1 noch nicht vollständig implementiert**. Das Manifest ist die erste maschinenlesbare Sollstruktur.

## 7. Wo Inhalte wiederkehren – und wo nicht duplizieren

| Querschnittsfunktion | Wiederkehrende Orte | Kanonische Umsetzung |
| --- | --- | --- |
| Begriff erklären | Anliegen, Recht, Medizin, Schule, Gesellschaft | eine Konzept-ID; fachspezifische Sinne |
| Ziel definieren | Anspruch, Pflegeplatz, Schulbildung, Beratung | eine Ziel-ID mit Kontextvarianten |
| Quellen prüfen | Fachportal, Lexikon, Weisungen, Datenstudien | Quellen-ID + Fundstelle + Quellenrolle |
| Messbarkeit/Definition | Arbeitslosigkeit, Krankenhaus, Bildung, Ernährung | Metrik-ID + eigene historische Version |
| Zuständigkeit/Verantwortung | Jugendamt, Gesundheitsamt, Steuerverwaltung | Institutionsrelation + Zeit/Region |
| Unterversorgung | Therapie, Pflege, Schulen, Hilfeangebote | gemeinsamer Suchoperator, unterschiedliche Wirkungskriterien |
| Alternativen und Hilfe | Anwaltsseiten, Selbsthilfe, Vereine, öffentliche Träger | Anbieter-/Dienst-ID und Zugang |
| Fehler-/Lernkultur | Corona, Kliniken, Bildung, Steuervollzug | Warnung → Maßnahme → Retest, nicht ein fertiger universeller Score |

Beispiel: Das Methodenthema „Was bedeutet eine 20 % veränderte Quote?“ wird **einmal** erklärt, dann bei Arbeitslosigkeit, Schulabschlüssen, Krankenhausbetten oder Ernährung mit den jeweiligen konkreten Daten erneut angewendet. Fachspezifika bleiben in Fachkarten.

## 8. Wann ein Fass aufmachen – wann verweisen?

**Einen neuen Teilbereich eröffnen, wenn mindestens eines zutrifft:**
- eigenständige Nutzerzielklasse oder eine neue entscheidende Handlung;
- andere fachliche Geltungsregeln, Risiken, Quellen oder Helfernetze;
- eine methodisch nicht übertragbare Messgröße, Schadensklasse oder besondere historische Quelle;
- genügend belegte Forschung für eine eigene verständliche Einführung;
- ein eigenständiges Werkzeug oder überprüfbarer Skill mit eigener Entwicklung.

**Vertiefung verlinken, wenn:**
- der andere Themenraum bereits eine kanonische Erklärung enthält;
- die Frage nur einen Aspekt des aktuellen Lernziels betrifft;
- ein Einzelfall oder historisches Ereignis eine Regel illustriert;
- eine fremde Disziplin zusätzliche Kontextbelege liefert, aber keinen neuen Handlungspfad eröffnet;
- der Beitrag im Kern Quellen-/Prüfdetail und keine didaktisch andere Aufgabe ist.

**Nur Paper/Anhang, wenn:**
- es sich um vollständige Literatur-/Quellentabellen oder Herleitungsdetails handelt;
- ein Befund noch offen, widersprüchlich oder nur Hypothese ist;
- längere historische Fassungen im Forschungsbestand erhalten bleiben sollen;
- keine neue geprüfte Kompetenz, Zielklasse oder wesentliche Begriffsunterscheidung daraus folgt.

**Keine eigenständige Corona-Startseite**, solange die konkrete Forschung den Stresstest nur als Vergleichszeitraum für Infrastruktur, Messbarkeit und institutionelles Lernen braucht. Gleiches gilt für einzelne Krankenhausträger oder Beratungsunternehmen: relevanter Fallbeleg im Fachpfad, nicht automatisch Hauptnavigationspunkt.

## 9. Trennung von Bürger-KI, SOULution und Tensor

**Bürger-KI:** Nutzerziele, Hilfszugänge, wissenschaftlich geprüfte Bürger-Skills und gesellschaftliche Aufgaben. Eigene Werkstatt/Beiträge.

**SOULution:** übergeordnetes Verbindungssystem für Forschungs- und Lösungsbereiche. Fachprojekte werden als Module erklärt und miteinander verlinkt, nicht inhaltlich in der SOULution-Startseite vollständig wiederholt.

**KI-Tensor:** eigenständige formale Forschungsprogramme, Tensoralgebra, Trinitäten, Parser, Relationen, Mini-KI usw. Die gemeinsamen Such-/Prüfmethoden können Schnittstellen erhalten, ohne dass Bürger-KI-Forschung automatisch ein neuer Tensor oder ein Teil des Tensor-Mitmachen-Systems wird.

**Gemeinsame Infrastruktur:** stabile Quellen-/Glossar-/Relations-/Skill-/Test-IDs, Provenienz, Versionierung, Projektzuordnung und geprüfte Interoperabilität. **Organisations- und Mitmachwege bleiben getrennt.**

## 10. Produktive Migration statt erneuter Totalumbau

**Schritt 1 – Sofort:** Dieses Paper, das Manifest und ein neuer Lernwege-Navigator als **Hub**, der bestehende Einstiegsseiten verwendet. Keine Löschung historischer Papers.

**Schritt 2 – Bestands-Crosswalk:** Jede relevante bestehende Bürger-KI-Seite erhält genau einen kanonischen Eigentümer, zugeordnete Lernwege und Fachfilter. Der aktuelle große Forschungsbibliotheksblock wird in der Startseite künftig auf wenige priorisierte Verweise zurückgeführt.

**Schritt 3 – Register-Nachzug:** Bei jedem Paper prüfen, welche neue Quelle, Konzept, Relation, Ziel, Skill, Test oder offene Frage tatsächlich entstanden ist. Bestehende Eigentümerobjekte aktualisieren und Mehrfachstandorte verlinken.

**Schritt 4 – Dependency-Compiler:** Versionsänderungen lösen für abhängige Darstellungen Recheck-Flags aus. Automatisierte Verlinkungs-/Schema-/Provenienz-Tests schaffen eine technische Minimalabnahme.

**Schritt 5 – Didaktische Nutzung:** Je Lernpfad 1–2 konkrete Beispiele mit bewusstem Rückweg zur Übersicht; Nutzerführung und Verständnis überprüfen. Erst danach weitere Unterseiten entstehen lassen.

## 11. Übersicht über den erreichten Zustand

| Bestandteil | Jetzt | Offen |
| --- | --- | --- |
| 5 Hauptbereiche | im Manifest definiert | plattformweite Navigationsvereinheitlichung |
| 5 Lernwege | Reihenfolgen und Zwecke definiert | vollständige durchgehende didaktische Umsetzung |
| Fachfilter | 6 erste Fächergruppen | ausdifferenzierte Thema-/Skill-Zuordnung |
| Kanonische Objekte | 12 Klassen beschrieben | bestehende Dateien/IDs vollständig gemappt |
| Routingregeln | 8 Änderungsfälle modelliert | implementierter Änderungscompiler |
| Wiederverwendung | 6 Querschnittsfunktionen modelliert | automatische Crosswalk-Validierung |
| Papers/Quellen | zahlreiche vorhandene Einzelakten | normalisierte Ergebnis- und Beweiskarten |
| Fortschritt | Inventar und Status transparent | keine wissenschaftliche Qualität aus Objektanzahl ableiten |

**Gesamtaussage:** Die Bürger-KI braucht keine weitere unübersichtliche Hauptnavigationsstruktur. Sie braucht einen verlässlichen **Kern aus wiederverwendbaren Wissens- und Skillobjekten** und mehrere verständliche Wege durch denselben Kern.

*No-Loss bedeutet nicht, jeden Text überall zu zeigen – sondern jede relevante Erkenntnis, Quelle, Version, Einschränkung und Weiterverwendung an der richtigen Stelle wieder auffindbar und prüfbar zu machen.*

## 12. Die entscheidende didaktische Präzisierung: Das Kernthema ist der Anker

Die fünf Hauptbereiche sind **nicht fünf voneinander isolierte Themenarchive**. Sie sind zugleich die **fünf wiederkehrenden Perspektiven auf jedes fachlich identifizierte Kernthema**. Der Leser soll über jeden Zugang in dasselbe Thema eintreten und danach die Perspektive wechseln können. Fachliche Inhalte bleiben am kanonischen Besitzer; die Darstellung arrangiert sie entsprechend der jeweiligen Frage.

**Erster implementierter Anker:** [Bürger-KI · Blickwinkel Therapieplatz](../../docs/buerger-ki-blickwinkel-therapieplatz.html), versioniert als [Themenmodell](../../docs/data/bki-therapieplatz-fuenf-blickwinkel-v0-1.json).

### Fünf fachbezogene Fragen – Beispiel Therapieplatz

1. **Anliegen und Ziele:** Was bedeutet es für einen Menschen, eine geeignete Behandlung tatsächlich zu erhalten? Erfolg ist nicht lediglich irgendein Termin.
2. **Wissen verstehen:** Was unterscheiden Sprechstunde, Probatorik, Regelbehandlung und unterschiedlich definierte Wartezeitangaben?
3. **Wege und Unterstützung:** Welche Stellen helfen bei Terminvermittlung, Patientenrechten oder Versorgungsproblemen, und wo enden ihre Leistungen?
4. **Gesellschaft untersuchen:** Welche regionalen und historischen Versorgungsstrukturen, Kapazitäten, Ungleichheiten und Messlücken existieren?
5. **Forschung und Werkzeuge:** Welche wiederverwendbaren Skills brauchen wir, um Begriffe zu klären, Methodenbrüche zu erkennen, Alternativen zu erschließen und den Stand der Evidenz korrekt anzuzeigen?

**Jeder Blickwinkel enthält:** menschliche Einstiegsfrage, didaktische Kernerkenntnisse aus dem vorhandenen Bestand, eine nachvollziehbare Folge von Quellen- und Vertiefungsschritten, ungelöste Fragen, alternative Perspektiven und einen Rückweg in die gemeinsame Übersicht. Die fachlich entscheidenden Inhalte sollen nicht allein in Anhangspapern verborgen bleiben. Ein Paper enthält Begründung und Belegführung, der Lernpfad die sinnvolle Reihenfolge und den Übergang.

### Didaktischer Mehrwert von Spiegelungen

- **Vom Menschen her:** Ziel, Voraussetzungen, tatsächlich erreichte Versorgung.
- **Vom Fachbegriff her:** Definition, Geltung, historische Vergleichbarkeit.
- **Von der Organisation her:** Welche Art Hilfe liefert der Ansprechpartner tatsächlich?
- **Von der Infrastruktur her:** Warum ist Leistung möglicherweise nicht erreichbar?
- **Vom Forschungsinstrument her:** Was ist nachweisbar und welche neue Fähigkeit entsteht daraus?

Ein Perspektivwechsel öffnet eine **neue Frage**, nicht eine Kopie derselben Erklärung. An geeigneter Stelle wird auf den bereits erläuterten Begriff, die bestehende Quelle, die Fachkarte oder das Forschungspaper verwiesen.

### Themenvertrag für weitere Kernthemen

Eine neue Fachseite wird nicht allein aufgrund eines neuen Forschungs-Papers oder Stichworts angelegt. Erforderlich sind (a) ein von Menschen verständliches Thema oder Problem, (b) die fünf unterscheidbaren Blickwinkel, (c) ausgewählte, quellengebundene Kerninhalte und begründete weiterführende Schritte, (d) ausgewiesene Alternativen/Spiegelungen, (e) explizite Grenzen und (f) stabile Links auf Quellen-, Ziel-, Begriff-, Skill- und Befundobjekte.

Das Modell kann anschließend beispielsweise auf **Pflegeplatz**, **Jugendamt**, **Wohnen**, **Schulversorgung**, **Behördenentscheidung**, **Steuerprüfung**, **Ernährung** oder **historische Arbeitslosenmessung** übertragen werden. Die Beispiele sind **Kandidaten**, keine bereits vollständig ausgeführten Themenpfade.

**Aktueller technischer Status:** Eine erste Themenseite und das zugrunde liegende JSON-Modell wurden im Repository erstellt. Der vollständige automatisierte No-Loss-Compiler und die fachliche Prüfung aller externen Quellenverknüpfungen bleiben offen.
