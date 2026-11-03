# GitHub-Darstellung von Schrödinger’s Inkubator
## Seitenanalyse, Informationsarchitektur und Umsetzungsauftrag · 3. November 2026

### 1. Ist-Zustand des Integrationsbranches

Die vorhandene `docs/soulution-schroedingers-inkubator.html` ist eine inhaltlich bereits deutlich ausgebaute Seite. Sie stellt die historische Vision, Module, Open-Source-Harvesting, Grenzen der Interoperabilitätsanalyse, die vier Interoperabilitätsebenen und Bezüge zu SOULution, Mini-KI und Tensor vor. Das separate Register `forschung/soulution/digitale-souveraenitaet/SCHROEDINGERS_INKUBATOR_REGISTER_V01.json` führt die Herkunft des ursprünglichen Ein-Seiten-Blatts und fünf offene Forschungsaufträge. Die ausklappbare projektweite Navigation verweist bereits auf den Inkubator unter SOULution.

Die aktuelle Struktur hat aber vier substanzielle Lücken: **(1)** Die zwei vorhandenen Projektgrafiken und das einseitige Original-PDF sind noch nicht als nachvollziehbare Originalmedien in das Repository übernommen. **(2)** Die Seite erläutert die Technik, ohne dem Leser zuerst ein konkretes Projektbeispiel zu geben. **(3)** Der eigenständige Zusammenhang zwischen Kernpaper, Funktionsatlas, Interoperabilität und Mitmachen ist in den vorhandenen Einstiegspunkten noch nicht klar genug sichtbar. **(4)** Manche Forschungsbehauptungen und Aufgaben wirken noch wie ein Gesamtprojektstatus, obwohl die beschriebenen End-to-End-Piloten offen sind.

Die Website braucht nicht mehr Menüpunkte als bisher, sondern einen eindeutigen, didaktisch aufgebauten **Landing- und Forschungsweg**.

### 2. Verbindliche Platzierung

**Navigationsebene 1:** SOULution & Publikationen (bestehende zentrale Dropdown-Gruppe)

**Navigationsebene 2:** Schrödinger’s Inkubator – Digitale Souveränität

**Projekt-Unterstruktur:**

1. **Einführung:** Die Originalidee in einem Satz und mit einer der vorhandenen Originalgrafiken.
2. **Kernpaper:** Zusammenfassung, lesbare HTML-Vollfassung, PDF und Markdown derselben Version.
3. **Bausteinatlas:** Welche vorhandenen Programme, Bibliotheken, Schnittstellen und Kernskills sind bereits identifiziert? Mit getrennten Statusfeldern.
4. **Interoperabilität:** Vier Ebenen, konkrete Beispiele und echte Import-/Exportprüfungen.
5. **Praktische Piloten:** Eine erste funktionierende Lösung, danach ein zweiter Anwendungsfall mit demselben Kern; positive und negative Tests.
6. **Gemeinsam entwickeln:** GitHub-Aufgaben, tatsächliche offene Schnittstellen und Mitmachwege für Programmierende ebenso wie Projektpartner.
7. **Originalarchiv und Quellen:** Beide Originalgrafiken, unverändertes einseitiges Original-PDF, externe Standards, Versionen und Lizenzangaben.

Diese sieben Rubriken sind lokale Sprungmarken einer Projektseite, **keine sieben neuen Einträge in der globalen Navigation**.

### 3. Gestaltungsvorschlag

**Hero:** Originalgrafik `schroedingers-inkubator1.png` unverändert, mit knapper Leitfrage rechts oder darunter: „Wie viele digitale Vorhaben tragen dieselben geprüften Kernfunktionen?“ Die Grafik sollte nicht durch generische KI-Illustrationen ersetzt werden.

**Sekundäre Originalgrafik:** `schroedingers-inkubator.png` als eigenständige, eindeutig beschriftete Projektgrafik in der Entstehungsgeschichte.

**Kurzform vor Langform:** Erst eine allgemeinverständliche Erklärung und ein konkretes Beispiel (etwa Vereinsprojekt mit Mitgliedern, Dateien, Terminen und Lernmaterialien), anschließend Methoden und wissenschaftliche Verknüpfungen.

**Drei Leitsätze:** Gemeinsam vorhandene Software nutzen. Über Schnittstellen und Bedeutung verbinden. Wirklich ausgeführte Funktionen mit Gegenproben nachweisen.

**Projektstatus:** Keine farbigen Statusplaketten, die bloße Absichten wie fertige Ergebnisse aussehen lassen. Stattdessen Spalten „Idee“, „Kandidaten inventarisiert“, „lokal getestet“, „end-to-end integriert“, „extern reproduziert“; jeweilige Quell-ID daneben.

**Rahmen für Meta und Skills:** Die in der Promptbibliothek etablierten interoperablen Rahmen bleiben **auf der technischen GitHub-Seite**. Im Kernpaper und in der bürgerorientierten Buchdarstellung sind kurze Erklärungen, Originalquellen und Beispiele zu bevorzugen.

**Verwandte Projekte:** SOULution als Gesellschafts-/Praxisrahmen; come²unity als Matching/Kooperationsansatz; Bibliothek als nachgewiesener Modulbestand; Mini-KI als optionale Auswahl-/Kompositionsforschung; KI-Tensor als eigenständiger Ableitungs- und Relationsnachweis. Keines davon ist Voraussetzung für einen ersten praktischen Softwarepilot.

### 4. Medien- und Dateikonzept

Die öffentliche GitHub-Seite soll diese **exakten Originaldateien** erhalten, nicht neu erzeugte Ersatzgrafiken:

```
docs/assets/inkubator/schroedingers-inkubator1.png
docs/assets/inkubator/schroedingers-inkubator.png
docs/assets/inkubator/schroedingers-inkubator-originalblatt.pdf
```

Dazu die gleichen Versionsfassungen des Kernpapers:

```
docs/soulution-schroedingers-inkubator.html                # Einstiegsseite
docs/soulution-schroedingers-inkubator-kernpaper.html      # lesbare HTML-Fassung
docs/assets/inkubator/INKUBATOR_KERNPAPER_V1.pdf          # digitaler PDF-Volltext
forschung/soulution/digitale-souveraenitaet/INKUBATOR_KERNPAPER_V1.md
forschung/soulution/digitale-souveraenitaet/SCHROEDINGERS_INKUBATOR_REGISTER_V01.json
```

Der Satz der beiden Grafiken wurde lokal erfolgreich durchgeführt. **Die Binärdateien sind noch nicht in den GitHub-Branch übertragen.** Daher dürfen im öffentlichen Branch vor dem Asset-Upload keine als vorhanden behaupteten Cover oder PDF-Links aktiviert werden. Ein vollständiges, lokales Paket mit den exakt verwendeten Originalen liegt bereit.

### 5. Zwei zielgruppengerechte Einstiegspfade

**Bürger und Projektgruppen:** Idee → konkreter Alltagseinsatz → gemeinsame Infrastruktur → Nutzen, Kosten und Verantwortung → Mitmachen. Hier braucht es keine Schnittstellen- oder Tensorbegriffe.

**Forschende und Entwickelnde:** Originalquelle → Kernpaper → Bausteinliste → technische/semantische/organisatorische/rechtliche Interoperabilität → reproduzierbare Piloten → Skillkomposition → optionaler Tensor-Leistungstest. Die volle Detailtiefe ist hier sinnvoll.

Die neue Macht-Publikation erhält lediglich einen thematisch passenden Werkhinweis auf digitale Souveränität und gemeinsame Infrastruktur; sie soll keine internen Modul-IDs oder Implementierungstabellen übernehmen.

### 6. Konkrete Implementationsschritte

| Schritt | Änderung | Abnahme |
|---|---|---|
| 1 | Originalmedien mit ihren Prüfsummen und Nutzungsinformationen ins Repo | unveränderte Bilddaten, Links erreichbar |
| 2 | V1-Kernpaper in `forschung/` als kanonische Markdown-Datei | Versionsvergleich mit PDF/HTML; keine Textabweichung |
| 3 | HTML-Volltext und PDF im `docs/`-Bereich veröffentlichen | beide auf GitHub Pages lesbar, Originalgrafiken korrekt |
| 4 | Vorhandene Projektseite in kompaktes Landing mit sieben Ankern verwandeln | keine doppelten vollständigen Kernpapertexte |
| 5 | Bausteinregister mit Statusmodell und Quellenreferenz anbinden | keine vorgeschlagenen Skills als ausgeführte kennzeichnen |
| 6 | Verweise von SOULution, Bibliothek, Interoperabilität, Mini-KI und Mitmachen prüfen | keine verwaisten Links oder falschen Projektzuordnungen |
| 7 | Desktop, Mobil, Tastatur, Kontrast, Alt-Texte und PDF-Lesbarkeit prüfen | dokumentierte QA mit offenen Restpunkten |
| 8 | Nach Review Integrationsbranch mit `main` zusammenführen | erst dann öffentliche Live-URL als veröffentlicht ausgeben |

### 7. Tests und Schutz gegen Informationsverlust

Ein Gesamtinventar der Repository-Dateien ist nur nach vollständigem Checkout und unter Einbeziehung der historischen als `local_only` markierten Bestände möglich. Der projektweite Dateiprüfer `forschung/website/AUDIT_ALLE_DATEIEN.py` ist dafür vorgesehen. Ohne tatsächlichen Lauf über den vollständigen Bestand darf kein vollständiger No-Loss-Abgleich behauptet werden.

Vor dem Merge müssen insbesondere folgende Risiken geprüft werden:

- Die neue zentrale Dropdown-Navigation darf bestehende Navigation und Projektanker nicht unzugänglich machen.
- Die Original-Bilder dürfen nicht beim Upload umkomprimiert oder durch generierte Motive ersetzt werden.
- Das historische Ein-Seiten-Blatt darf nicht nachträglich als vollständiges technisches Architekturpaper ausgegeben werden.
- Die neue Software-Zukunftsthese darf nicht als bereits bewiesene Branchenentwicklung erscheinen.
- Open Source, freie Information, proprietäre Schnittstellen und rechtmäßig begrenzte Dekompilierung dürfen nicht vermischt werden.
- Eine funktionierende Skillkette darf nicht als Beweis einer eigenständig lernenden KI gelten.
- Eine 27-Felder-Skizze darf nicht als fachlich validierter Tensor geführt werden.

### 8. Ergebnis der Analyse

**Der Inkubator verdient auf GitHub einen eigenen Projekt-Lernpfad unter SOULution.** Das Kernpaper bildet die wissenschaftliche Mitte; die Originalgrafiken schaffen Wiedererkennung; der Bausteinatlas und die reproduzierbaren Piloten liefern den tatsächlichen Forschungsfortschritt. Die projektübergreifende Interoperabilität verbindet den Inkubator mit Bibliothek, Mini-KI und KI-Tensor, ohne die Eigenständigkeit der Ansätze aufzugeben.

**Stand:** Konzeption und digital gesetzte Paperfassungen vorhanden. Eine vollständige modulare Plattform, quellenvalidierte Modulbibliothek und bestandene End-to-End-Piloten werden nicht behauptet. Vollständige GitHub-Veröffentlichung einschließlich binärer Originalmedien steht aus.