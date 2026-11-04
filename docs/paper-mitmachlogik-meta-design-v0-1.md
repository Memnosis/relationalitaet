# Mitmachen als mehrschichtiges Interaktions- und Forschungsdesign

## Eine Meta-Analyse der Tensor-Projekte und der eigenständigen Bürger-KI

**Forschungspaper | Version 0.1 | 4. November 2026**  
**ID:** META-MITMACH-001  
**Status:** Quellengestützte Bestandsanalyse, eigenständige Designhypothesen, vorgeschlagene Experimente. Keine empirische Nutzerstudie.  
**Geltungsbereich:** Tensor, Mini-KI, Geo-KI, Harvesting, Komprimierung, visuelle Engine, KI-Kollegen, SOULution und Bürger-KI.  
**Wichtige Abgrenzung:** Bürger-KI übernimmt geeignete Mitmach-**Prinzipien**, nicht die organisatorische oder technische Anbindung an die vorhandene Tensor-Mitmachseite. Kein Bürgerdaten- oder Fallverarbeitungsprojekt.

## Abstract

„Mitmachen“ bezeichnet in den untersuchten Projekten weder einen einzigen Nutzerweg noch eine besondere Handlungsklasse. Es umfasst Orientierung, Verständnisbildung, Anwendung, Exploration, Prüfung, Verbesserung, wissenschaftliches Beitragen und Meta-Mitgestaltung. Viele dieser Tätigkeiten können sich aus den gewöhnlichen Bedürfnissen von Nutzern ergeben; sie sind aber nicht automatisch Beiträge zu einem Forschungsbestand. Analytisch müssen daher vier Sachverhalte getrennt werden: **(1) Bedürfnis/Absicht, (2) konkrete Interaktion, (3) freiwillig abgegebener Beitrag, (4) extern geprüfter Befund**. Aus dieser Trennung folgt ein mehrdimensionales Designmodell, das verschiedene Eintrittspunkte und Zielfunktionen respektiert, Forschungsergebnisse über Provenienz und Tests verbindet und weder die Bürger-KI in den Tensor-Mitmachbereich integriert noch Benutzer zu Mitwirkenden erklärt. Eine experimentelle Architektur vergleicht anschließend alternative Aufgaben- und Interaktionspfade anhand von objektiven Aufgabenresultaten, Verständnis, Aufwand, Fehlerquoten und überprüfbarer Übertragbarkeit.

## 1. Fragestellungen

1. Welche Nutzungsformen, Ziele, Rollen und Interaktionspfade sind unter „Mitmachen“ bereits zusammengefasst?
2. Welche Nutzerbedürfnisse erzeugen **potenzielle** Mitmachgelegenheiten, auch ohne expliziten Forschungswunsch?
3. Welche Operationen sind projektübergreifend wiederverwendbar, welche bleiben fach- oder projektspezifisch?
4. Wie erkennt man den Unterschied zwischen einer guten Oberfläche, einer erfolgreich gelösten Aufgabe und einem wissenschaftlich belastbaren Beitrag?
5. Welche wenigen Interaktionsmuster sind geeignet, die Vielfalt ohne Überforderung anzubieten?
6. Wie lassen sich alternative Designs und KI-Strategien an identischen Referenzaufgaben vergleichen?

## 2. Methodik und erhobener Bestand

Qualitative Architektur- und Dokumentenanalyse von GitHub-Dateien am 04.11.2026. Geprüfte Primärbestände:

- [Mitmachseite und didaktische Module](./mitmachen.html): Erkundung, fachliche Aufgaben, Harvesting, Prompt/Agent/Meta, Freigabestufen und Verweise auf Rückgaben.
- [Öffentliches Aufgabenregister](./data/mitmach-public-v2.json): 13 öffentliche Forschungsaufgaben; alle zum Prüfzeitpunkt mit `public_release=not_approved`, `prompt_execution_status=not_run`.
- [Mitmachkarten-Renderer](./assets/mitmachen-karten.js): Fachbereichsfilter, Vorschau, nur bei Freigabe sichtbarer direkt ausführbarer Prompt, Issue-Link, Rückgabe-Link.
- [Rückgabeseite](./mitmachen-rueckgabe.html): lokale Ergebnisakte mit Task-ID, Methode, Quellen, Befunden, Gegenbeispielen und Export; kein automatischer Empfang.
- [Geo-/Interoperabilitätsmeilensteine](../forschung/website/GEOKI_INTEROP_MEILENSTEINE.json): Entwickler- und Meta-Aufträge, Abhängigkeiten, Quellen, Definition of Done, Promptentwürfe.
- [SOULution](./soulution.html): Transfer von Forschungsmodellen zu öffentlicher Orientierung und Lösungsentwicklung.
- [Harvesting](./harvesting.html): Quellen- und Modellernte, Test, Gegenprobe, Interoperabilität.
- [Bürger-KI-Experimentierlabor](./buerger-ki-experimentierlabor.md): 8 Projektideen, 10 Aufgabenfamilien, 30 geplante Aufgaben und 6 Strategievarianten; bislang Forschungsdesign, keine Leistungsmessung.
- [Bürger-KI-Forschungswerkstatt](./buerger-ki-werkstatt.html): vier lokale Interaktionsschritte, drei deterministische Prüfstrategien mit fiktiven Verwaltungsregeln; noch kein allgemeiner KI-Dienst.
- [Bürger-KI Phase 6](./buerger-ki-phase-6-mitmachen.md): Korrektur der ursprünglichen Annahme einer gemeinsamen Mitmach-Infrastruktur; nur Designprinzipien werden übernommen.

**Grenze der Analyse:** Die Dokumente erlauben Aussagen über implementierte Mechanismen und vorgesehene Abläufe, nicht über tatsächliches Nutzerverhalten, Erfolgshäufigkeiten oder bereits erreichte wissenschaftliche Wirkung. Alle Nutzerbedürfnisse im Folgenden sind Hypothesen/Anforderungsklassen, **keine gemessenen Nutzerstatistiken**.

## 3. Acht logisch unterscheidbare Mitmachdimensionen

| Dimension | Typische Nutzeräußerung | Unmittelbares Ziel | Möglicher Forschungsanschluss |
| --- | --- | --- | --- |
| M1 Entdecken | „Was kann ich hier machen?“ | Orientierung | fehlende Navigations-/Begriffsknoten |
| M2 Verstehen | „Was bedeutet das?“ | verständliche Erklärung | didaktischer Test, Glossar |
| M3 Anwenden | „Hilf mir, X zu erreichen.“ | funktionaler Nutzen | Skill-Test und Aufgabenabdeckung |
| M4 Erkunden | „Welche Alternativen existieren?“ | neue Optionen | Harvest, Modell- und Quellenvergleich |
| M5 Prüfen | „Stimmt das?“ | Beleg, Verlässlichkeit | Gegenbeispiel, Quellen-/Evidenzakte |
| M6 Verbessern | „Das geht anders oder besser.“ | Korrektur | Änderungs- und Regressionstest |
| M7 Beitragen | „Ich habe eine Quelle oder Lösung.“ | Wissen ergänzen | Kandidat mit Provenienz und Begutachtung |
| M8 Mitgestalten | „Wieso ist das Ziel so definiert?“ | Ziele/Regeln verändern | Meta-Forschung zu Kriterien und Prioritäten |

Diese acht sind **Dimensionen**, keine zwingenden Phasen und keine numerisch bestätigte Taxonomie. Eine Interaktion kann mehrere Dimensionen zugleich betreffen. Mitmachen beginnt nicht erst mit einer registrierten Einsendung.

## 4. Vier nicht austauschbare Zustände

**Bedürfnis:** Das Anliegen einer Person (z. B. eine unklare Zuständigkeit).  
**Interaktion:** Die konkrete Nutzung einer Funktion (z. B. Zuständigkeitsfinder oder Vergleich).  
**Beitrag:** Eine bewusste, eigenständige Übermittlung eines sachlichen Verbesserungshinweises, einer Quelle oder eines Reproduktionstests.  
**Befund:** Der unabhängig geprüfte und versioniert dokumentierte Erkenntnisstand.

**Wichtige Konsequenz:** Ein Bürger muss nicht Forschungsakteur werden. Eine fehlgeschlagene Suchanfrage ist nicht automatisch ein öffentlicher Forschungsbeitrag. Ein eingereichter Verbesserungsvorschlag ist keine bestätigte Korrektur. Eine erfolgreiche Interaktion ist kein wissenschaftlicher Nachweis einer allgemeingültigen Methode.

## 5. Das multidimensionale Interaktionsmodell

Jede Mitmachoption lässt sich als Tupel klassifizieren:

`I = (Bedürfnis, Ziel, Fachraum, Rolle, Einstieg, Operation, Pfad, Ergebnis, Prüfniveau, Weitergabe)`.

- **Bedürfnis:** Orientierung, Erklärung, Lösung, Vertrauen, Vergleich, Kontrolle, Beitrag.
- **Ziel:** eine Antwort, praktische Möglichkeit, überprüfbare Erkenntnis, neuer Skill, verbesserter Prozess.
- **Fachraum:** Geometrie, Logik, Algebra, Verwaltung, Recht, Bildung usw.
- **Rolle:** Leser, Anwender, Fragender, Fachkundiger, Prüfer, Entwickler, KI-Agent, Mitgestalter; Rollen wechselbar.
- **Einstieg:** freie Frage, Beispiel, Kachel, konkrete Quelle, bekannte Fehlerstelle, Ergebnis, Thema, Skill.
- **Operation:** suchen, erklären, strukturieren, berechnen, transformieren, vergleichen, invertieren, prüfen, komponieren, publizieren.
- **Pfad:** linear, explorativ, verzweigt, parallel, zyklisch, mit Gegenprüfung.
- **Ergebnis:** Erklärung, Plan, Quelle, Test, Skill, Gegenbeispiel, Vorschlag, Publikation.
- **Prüfniveau:** unbeurteilt, plausibilisiert, formal/geprüft, unabhängig repliziert.
- **Weitergabe:** nur für den Nutzer sichtbar, lokal exportiert, freiwillig übermittelt, redaktionell freigegeben.

Aus diesen Dimensionen entsteht **kein einzelner universeller Mitmach-Funnel**. Der Nutzer braucht einen passenden Einstieg und kann danach in weitere Pfade wechseln oder aufhören.

## 6. Schnittmengen mit den Nutzern

| Nutzerbedürfnis | Tensor-Projekt | Bürger-KI | Gemeinsamer Kernskill |
| --- | --- | --- | --- |
| Orientierung | Fachmodelle entdecken | Leistungen/Institutionen finden | Klassifikation, Suche, Navigation |
| Verständnis | Operator/Relation erklären | Voraussetzungen/Verfahrenslogik erklären | Begriffs- und Quellenrekonstruktion |
| Zielerreichung | Form/Modell erzeugen, Relation prüfen | Handlungsmöglichkeiten entwickeln | Planen, Selektieren, Ausführen |
| Alternativen | konkurrierende Modelle | alternative Verwaltungswege | Vergleich und Entscheidungsbedingungen |
| Verlässlichkeit | Beweis, Invariante, Gegenbeispiel | gültige Quelle, Zuständigkeitsgrundlage | Beleg-, Geltungs- und Fehlerprüfung |
| Rückrechnung | Invertierbarkeit/Operatorfolge | Ziel rückwärts in Voraussetzungen und Schritte auflösen | Abhängigkeitsgraph/Rückwärtsplanung |
| Fehlermeldung | Parserfehler, Feldwiderspruch | fehlerhafte Information oder unbrauchbarer Schritt | Fehlertaxonomie/Regression |
| neue Ressourcen | Formeln, Bibliotheken, SKOS usw. | FIM, XZuFi, Open-Source-Verwaltungskomponenten | Deep Dive & Harvest |
| Weiterentwicklung | Trinitäten, Tensoren, Skills | Verwaltungs-/Bürger-Skills | Spezifikation, Test, Versionierung |
| Wirkungsfrage | erklärt Tensor etwas besser? | unterstützt KI das Bürgerziel besser? | kontrollierter Vergleich/Benchmark |

**Hauptschluss:** Gemeinsam sind primär die epistemischen und technischen **Operationen**, nicht die Zielgruppen, Oberflächen, Datenbestände oder organisatorischen Veröffentlichungswege. Ein gemeinsamer Methodenvergleich ist sinnvoll; eine Zusammenlegung der Systeme folgt daraus nicht.

## 7. Bedarfsauslöser: Was kann zu „Mitmachen“ führen?

1. **Frage nicht gefunden:** fehlender Informationsknoten, Keyword oder Skill; möglicher Kandidat für Erweiterung.
2. **Erklärung missverstanden:** Bedarf an einfacherer oder anderer Darstellung, Beispielen oder Sprachvarianten.
3. **Widerspruch entdeckt:** wertvolles Gegenbeispiel, aber noch kein geprüfter Fehler.
4. **Ziel nur teilweise erreicht:** es fehlt eine Alternative oder eine Voraussetzung.
5. **Fachquelle veraltet:** Aktualisierungskandidat mit Stichtag und Originalnachweis.
6. **Nutzer findet bessere Ressource:** Harvest-Kandidat, vor Übernahme zu prüfen.
7. **Andere KI liefert anderes Ergebnis:** strukturierter Methodenvergleich statt bloßer Mehrheitsentscheidung.
8. **Ergebnis schwer überprüfbar:** Nachweis- und Provenienzlücke.
9. **Wunsch nach Automatisierung:** wiederkehrende Operation in einen Skill auslagern.
10. **Wunsch nach kreativem Spiel/Exploration:** Varianten- und Formgenerator, kontrollierter Entdeckungsraum.
11. **Nutzer will Lernmaterial:** didaktische Abzweigung; nicht notwendig Forschung.
12. **Nutzer will selbst prüfen oder programmieren:** expliziter Forschungs-/Entwicklerpfad.
13. **Frage nach gesellschaftlicher Wirksamkeit:** neuer Meta-Prüfgegenstand (z. B. tatsächlicher Nutzen einer Bürgerhilfe).
14. **Nutzer hinterfragt die Ziele des Projekts:** Meta-Design und Governance, getrennt von normalen Aufgaben.
15. **Nutzer lehnt Forschungsbeteiligung ab:** gleichwertiger Nutzungsweg ohne weitere Aufforderungen.

Diese Liste ist eine **Hypothesenliste für Nutzungsdesign**, keine personenbezogene Profilierung und keine automatisch aktivierte Datensammlung.

## 8. Sechs Pfadtypen

- **P1 Direkt:** Frage → fachlich begründete Antwort; für einfache, klare Aufgaben.
- **P2 Lernpfad:** Frage → Erklärung → Beispiel → Selbstprüfung → vertiefende Quelle.
- **P3 Handlungsweg:** Ziel → Voraussetzungen → Alternativen → priorisierte Schritte.
- **P4 Explorationspfad:** Ausgangsfrage → Harvest → Varianten → Vergleich → neue Frage.
- **P5 Prüfpfad:** Behauptung → Quelle → Geltung → Gegenbeispiel → Urteil.
- **P6 Entwicklungspfad:** Fähigkeitslücke → Spezifikation → Implementierung → Test → Gegenprüfung → Versionierung.

Diese Pfade sind kombinierbar; ein Nutzer soll aber nicht alle durchlaufen müssen. Sichtbare Verzweigungen erklären jeweils den **Nutzen** statt technische Interna zu verlangen.

## 9. Meta-Analyse der bestehenden Mitmachmechanik

### Stärken

- Verbindet didaktischen Einstieg und wissenschaftliche Quellen.
- Trennt direkte, Agenten- und Meta-Aufgaben.
- Macht wissenschaftliche Negativbefunde und Gegenproben grundsätzlich sichtbar.
- Verhindert im Kartenrenderer, dass ungeprüfte Meta-Prompts als fertige Direktprompts ausgegeben werden.
- Ermöglicht lokalen Export einer reproduzierbaren Ergebnisakte ohne Schreibrechte am Git-Repository.
- Bietet Quellen-, Task- und Ergebnis-IDs als Voraussetzung für spätere Synchronisierung.

### Spannungen und Fehlermöglichkeiten

- **Ebenenverwechslung:** Begriffserklärung, Arbeitsauftrag und Forschungstest können wie ein einziger Beitrag wirken.
- **Navigationslast:** Bereich, Rolle, Prompt-Typ und Prüfstatus konkurrieren als Einstieg.
- **Zieldivergenz:** Nutzer wollen ein Ergebnis; Forschende wollen einen validen Nachweis. Beides darf nicht gleichgesetzt werden.
- **Scheinerfolg:** Kopierfunktion, Export und Issue-Link können mit angenommener wissenschaftlicher Mitarbeit verwechselt werden.
- **Unvollständiger Rückkanal:** Lokaler Export ist noch keine bestätigte Einsendung, Begutachtung oder sichtbare Rückmeldung.
- **Überabstraktion:** Gleicher Prozessname (z. B. „Prüfung“) bedeutet nicht identische mathematische oder rechtliche Operation.
- **Mangelnde Wirkungsmessung:** Die Zahl angelegter Karten misst weder Verständlichkeit noch gelöste Aufgaben.
- **Prompt-Fetisch:** Immer mehr Prompts können ohne unabhängige Ergebnisse und Versionierung zu mehr Komplexität führen.

### Entwurfsfolgerung

Die sichtbare Nutzeroberfläche sollte nur wenige verständliche **Absichten** anbieten; komplexe Fach- und Meta-Arbeit gehört in kontextuelle Vertiefungen. Das Design muss den Status eines Ergebnisses (Vorschlag vs. Test vs. Nachweis) unmissverständlich zeigen.

## 10. Die Bürger-KI: eigenständige Anwendung derselben Prinzipien

Die Bürger-KI-Werkstatt kann die vier Interaktionen **Fragen → Ausprobieren → Vergleichen → Verbessern** als lernbare Oberfläche verwenden. Sie verarbeitet keine persönlichen Bürgerakten. Der derzeitige Prototyp ordnet freie Eingaben nur Stichwörtlich zu vorbereiteten synthetischen Fällen zu und führt lokale regelbasierte Strategien aus.

### Nutzungsmodus

- Frage oder Ziel formulieren.
- Geeigneten Verwaltungs-/Fachskill und belegte Alternativen finden.
- Bei Bedarf Begründung, Quelle, Unsicherheit und Varianten öffnen.
- Ergebnis für eigenen Zweck verwenden; **keine Mitwirkungspflicht**.

### Forschungsmodus

- Allgemeine, fiktive Referenzaufgabe wählen.
- Mindestens zwei Strategien mit identischer Aufgaben- und Quellenlage vergleichen.
- Fehler und Beleglücken prüfen.
- Änderung als versionierten, überprüfbaren Vorschlag formulieren.
- Unabhängige Prüfung vor Übernahme in eine gemeinsame Skillbibliothek.

**Nicht vorgesehen:** Automatisch publizierte Bürgeranfragen, Nutzung realer persönlicher Anliegen als Trainingsbeiträge oder unkontrollierte Übernahme von KI-Antworten als geprüfte Regeln.

## 11. Wissenschaftliche Evaluation: vier unterschiedliche Erfolgsarten

| Erfolgsebene | Beispiel für Messgröße | Was damit *nicht* bewiesen ist |
| --- | --- | --- |
| Usability | Aufgabe verstanden, wenige Fehlklicks, Zeit bis zur Orientierung | fachliche Richtigkeit |
| Aufgabennutzen | Ziel im definierten Test erreicht, relevante Wege abgedeckt | unabhängige Reproduzierbarkeit |
| Evidenzqualität | korrekte Quellenbezüge, Gegenproben bestanden | tatsächlicher Nutzen in allen Lebenslagen |
| Forschungsfortschritt | validierter neuer Skill/Gegenbefund, stabile Regression | automatisch hohe Nutzung oder Zugänglichkeit |

**Forschungsdesign MMD-EXP-01:** Drei Varianten derselben Einstiegsaufgabe vergleichen: (A) Kacheln nach Fachbereichen, (B) Einstieg über Nutzerabsichten, (C) freie Frage mit dynamisch vorgeschlagenen Pfaden. Identische, synthetische Aufgaben: „Quelle finden“, „Fehler prüfen“, „Handlung vorbereiten“. Randomisierte Reihenfolge, vorgegebene Sollresultate, Erfassung von Erfolgsrate, Verständnisfehlern, Zeit, Abbruch und unnötigen Pfadwechseln. Keine vorweggenommenen Werte.

**MMD-EXP-02:** Sichtbare Modus-Trennung „Nutzen“ vs. „Mitforschen“ gegen eine einzige universelle Oberfläche vergleichen. Ziel: Wird der Unterschied zwischen eigener Nutzung, Vorschlag und geprüfter Forschung besser verstanden?

**MMD-EXP-03:** Dieselbe Aufgabe über Direktpfad, Lernpfad, Prüfpfad und Explorationspfad bearbeiten. Bewerten: Genauigkeit, relevante Alternativen, kognitive Belastung, Belegtreue und Bearbeitungsaufwand.

**MMD-EXP-04:** Zwei verschiedene KI-Strategien auf identischen Referenzaufgaben: Direktantwort vs. Skill-Kette mit unabhängiger Prüfung. Keine Vermischung mit A/B-Tests der Benutzeroberfläche: Interaktionsdesign und Algorithmusleistung werden getrennt kontrolliert.

**MMD-EXP-05:** Metadaten prüfen: Kann ein freiwillig eingereichter reproduzierbarer Beitrag ohne Rückfragen korrekt identifiziert, ausgeführt, eingeordnet und gegengeprüft werden?

Kleine Pilotstudien prüfen zunächst Durchführbarkeit; größere Stichproben und geeignete Auswertung sind nötig, bevor allgemeine Aussagen über Nutzerpräferenzen oder Qualität gemacht werden können.

## 12. Ein schlankes Schema für Mitmachgelegenheiten

```json
{
  "id": "MMD-OPP-001",
  "user_intent": "verify",
  "project": "buerger-ki",
  "entry": "question",
  "path_type": "P5",
  "goal": "claim_source_check",
  "skill_ids": ["BKI-V07"],
  "task_ids": ["BKI-T09-A"],
  "sources": [],
  "output_contract": "claim-evidence-verdict/0.1",
  "participation": "optional",
  "contribution_channel": "local_export",
  "contribution_received": false,
  "evidence_status": "design_only",
  "approval_status": "not_approved"
}
```

Die tatsächlichen Aufgabenversionen und Quellen müssen versioniert sein. Menschliche Bedürfnisse und Absichten dienen hier zur **Gestaltung** einer Interaktion, nicht zur automatischen Speicherung persönlicher Nutzerprofile.

## 13. Wie weit reichen gemeinsame Projektmethoden?

Übergreifend lassen sich wiederverwenden: Bedarfsklassifikation, Aufgabenvertrag, Quellenprovenienz, Begriffsregister, Skill-IDs, Testmethoden, Versionierung, Gegenproben, Ergebnisstatus, No-Loss und Kompetenzvergleich.

Projektgebunden bleiben: Bürger-KI-Oberfläche und Verwaltungswissen; Tensoralgebra mit 3×3×3; Geo-KI-Operatoren; Publikations- und Mitmachnavigation; konkrete Rechte-/Verfahrensentscheidungen. Übertragbarkeit von Skills muss **positiv geprüft**, nicht aus ähnlicher Sprache abgeleitet werden.

Die Meta-Forschung kann Ähnlichkeiten von **Zielen, Operationen, Pfaden und Ergebnisformen** klassifizieren. Ob sich daraus eine mathematische Tensorstruktur ergibt, erfordert eigene Beweise beziehungsweise Gegenbeispiele.

## 14. Praktische Designentscheidungen

1. Kein allgemeines „Mitmachen“ als verpflichtender Hauptpfad. Der Einstieg erfolgt über das **Bedürfnis**.
2. „Nutzen“, „Prüfen“ und „Weiterentwickeln“ sind sichtbare, kontextabhängige Wahlmöglichkeiten.
3. Freiwillige Forschungseinreichungen müssen klar als **Vorschlag**, **unabhängig geprüft** oder **freigegeben** gekennzeichnet sein.
4. Ein Fehler oder nicht erreichter Zweck wird als nützlicher Befund behandelbar, aber nie ungefragt veröffentlicht.
5. Jede Mitmachgelegenheit zeigt eine **konkrete kleine Aufgabe und ihren erwarteten Nutzen**, nicht nur einen abstrakten Meta-Prompt.
6. Nicht die Zahl der Teilnehmenden oder Prompts, sondern abgeschlossene, überprüfbare Ziele und valide Erkenntnisgewinne sind die zentrale Leistungsmetrik.
7. Projektübergreifende Gemeinsamkeiten bleiben auf Methoden-/Forschungsniveau; keine organisatorische Zusammenlegung der Bürger-KI und Tensor-Mitmachseite.

## 15. Forschungsagenda und nächste Version

**A – Bestandsinventar vervollständigen:** Alle Einstiegspunkte, Karten, direkten Prompts, Agenten-Aufträge, Meta-Aufträge, Quellzugänge, Exporte und tatsächlichen Rückgabepfade mit stabilen IDs erheben.

**B – Pfadgraph ableiten:** Von jedem Nutzerbedarf zu möglichen Aktionen, Ergebnisse, Prüfungen und Abbrüchen; Redundanzen und Sackgassen sichtbar machen.

**C – Pilotstudie MMD-EXP-01:** Drei unterschiedliche Einstiege an gleichen Aufgaben testen; menschliche Nutzungsdaten erst nach bewusstem Studiendesign, nicht aus Alltagsanfragen ableiten.

**D – Bürger-KI isoliert evaluieren:** Eigene vierstufige Werkstatt mit getrenntem Nutzungs-/Forschungsmodus. Zuerst synthetische Fälle, danach geprüfte Verwaltungsquellen und echte KI-Strategien.

**E – Meta-Abgleich mit der Tensorforschung:** Operator- und Pfadtypen nach formalen Eigenschaften klassifizieren, vermeintliche Gleichheiten durch Negativfälle widerlegen und nur belegte gemeinsame Strukturen übernehmen.

**Noch offen:** Vollständiges Inventar aller historischen Mitmachaktionen, Nutzertests, repräsentative Stichprobe, verifizierte technische End-to-End-Tests, empirischer Wirksamkeitsvergleich.

## Fazit

Mitmachen ist keine einzelne Funktion, sondern ein **Möglichkeitsraum unterschiedlicher Beteiligungstiefen**. Die entscheidende Designfrage lautet nicht, wie man möglichst viele Menschen zu formellen Forschungsbeiträgen führt, sondern wie jede Person ihr eigenes Ziel erreichen kann und – **wenn gewünscht** – verständliche Wege zur Prüfung, Verbesserung und Forschung findet. Gemeinsame Methoden zwischen Tensor-Projekten und Bürger-KI sollten deshalb an der Ebene von **Operationen, Prüfkriterien, Ergebnisverträgen und Evidenz** untersucht werden; ihre unterschiedlichen fachlichen und organisatorischen Kontexte bleiben erhalten.

---

### Stand und Provenienz

Dieses Paper ist eine konzeptionelle Synthese aus den oben verlinkten Projektdateien. Die empirischen Hypothesen und 5 Pilotstudien sind **nicht durchgeführt**. Der bestehende Bürger-KI-Prototyp enthält ausschließlich deterministische lokale Beispielregeln. Eine verbindliche Publikationsfreigabe ist mit der Speicherung dieser Arbeitsfassung nicht verbunden.
