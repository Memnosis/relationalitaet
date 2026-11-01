# SOULution · Tiefenplanung Website und Publikationsfamilie v0.1
Stand: 2026-11-01 · Status: Entwicklungsplan, nicht als implementierte Module ausweisen.

## Leitidee
**Wissen verbinden. Lösungen möglich machen.**
Die bestehende Seite `docs/soulution.html` bleibt als Überblick erhalten. Neun bestehende Fachbereiche und ihre Farben/Icons werden nicht umcodiert. Ziel ist eine relationale, maschinenlesbar unterlegte Lösungsplattform mit überprüfbarer Evidenz, Forschung, Operationalisierungen, Skills, Mitmacharbeiten und Publikationen.

## Informationsarchitektur
1. Hero: zwei Zeilen, Kurzdefinition, zwei Einstiegspfade (Lösung suchen, Forschungsaufgabe übernehmen).
2. Neun vernetzte Forschungs- und Lösungsbereiche (gleichberechtigt, semantische Icons, Fachfarbe nur als Akzent).
3. Lösungspfad: Problem → Lösungsfunktion → Methode/Operationalisierung → Evidenz → Implementierung → Plattform/Daten → Voraussetzungen/Risiken → nächster Schritt.
4. Verbundene Forschungswerkzeuge: Harvesting, Minimal-KI, Tensor, relationale Algebra, Interoperabilität, Visualisierung, Codebuch; Status als vorhanden/prototypisch/Kandidat.
5. Forschungsbestände und Publikationen: Karten mit Quelle, Provenienz, Version, Evidenz, Fortschritt, maschinenlesbarem Register und Mitmach-Task.
6. Projekt- und Fortschrittsansicht: echte Werte aus maschinenlesbarem Register statt statischer Prozentbehauptungen.
7. Mitmachen: persistenter, tastaturbedienbarer Zugang am unteren Bildschirmrand, nicht über anderen Inhalten.
8. Archiv/Originale: No-Loss und eindeutige Verfügbarkeit; Originaldonoren nicht stillschweigend überschreiben.

## Neue Fachfamilie: Öffentliche Finanzsimulationen
Donor: `Wirtschafts-Simulationen-und-andere-Mafia-Spiele_final1.pdf`, 483 Seiten, 28.05.2026. In der laufenden Arbeit daraus erzeugt (noch nicht auf Git importiert):
- SOULution_Wirtschafts_Simulationen_Kurzfassung.docx und .pdf sowie .md
- SOULution_Wirtschafts_Simulationen_Quellenregister.json (aus PDF extrahierte Web-Quellkandidaten mit PDF-Seiten; URL-Prüfung ausstehend)
- SOULution_Wirtschafts_Simulationen_18_Arbeitsfelder.json (18 Aufgaben aus Anhang D, jeweils mit offenem Entwicklungsstatus)

Fachlicher Kern: Haushalt → Leistungen → Haushalte → Konsum/Wohnen/Energie → Branchen → mögliche Steuer-/Abgaben-Rückflüsse. Szenarien für Rente, Grundeinkommen, öffentliche Vermögen/PPP, Steuern, Geldschöpfung, Verwaltungs- und Mangelfolgekosten.
**Schutz vor Scheingenauigkeit:** beobachtet vs. berechnet vs. modelliert vs. unbekannt; Umsatz ≠ Gewinn; keine Identifikation einzelner Transfer-Euros bei konkreten Unternehmen ohne Transaktionsdaten.

## Maschinenschema pro Forschungsobjekt
`id, title, area_id, problem, solution_function, methods[], operationalizations[], evidence[], implementations[], platforms[], sources[], assumptions[], risks[], skills[], tests[], tasks[], status, progress_basis, provenance, version, updated_at`.

## Entwicklungsphasen
- P0: No-Loss-Quellen, Objekt-IDs, Quellvalidierung, JSON-Schema und Inhalts-Crosswalk; vorhandene Website bewahren.
- P1: Finanzsimulation als Projekt-/Publikationskarte, Fachfarben/Icons und relationale Brücken zu SOULution-Bereich 05 und 07.
- P2: neun Bereichs-Unterseiten, filterbarer Methoden-/Operationalisierungskatalog, echte Fortschrittsberechnung.
- P3: Pilot-Datensatz Bundeshaushalt + ein Sozialflussmodell, dokumentierte Parameter und Negativtests.
- P4: Szenarien, Exporte, reproduzierbare Berechnung und Mitwirkungsworkflow.

## Abnahme je Modul
Quellen, Jahr, Lizenz, Ebene und Datenstatus sichtbar; WCAG 2.2 AA; mobile & Tastaturprüfung; fehlende Links; CI mit JSON-Schema, Quelle-Daten-Referenzen, HTML-Linktests, Screenshots; keine neue Zahlenbehauptung ohne Datensatz und Test.

## Nächste Git-Integrationsschritte
1. Die vier neu erzeugten Daten/Publikationsdateien geprüft und mit hashfähigem Originalmanifest in einen dedizierten Unterordner übernehmen (nicht direkt die bestehende SOULution-Seite ersetzen).
2. Projektkarte und Link in `docs/soulution.html` ergänzen.
3. `docs/projektstand.html` und `docs/mitmachen.html` anhand der Datenregister verknüpfen.
4. Browserabnahme dokumentieren.
