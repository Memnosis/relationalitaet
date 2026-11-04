# WEBSITE-GESAMTKONZEPT · Upgradeauftrag nach 5 abgeschlossenen KI-Zyklen
Version: 0.1 · 2026-11-04 · Status: Konzeptgrundlage, Umsetzungsgate = 5 vollständig abgeschlossene Zyklen
Owner: GPT; fachliche Gegenprüfung: Claude; Autor-/Releasefreigabe: Nils.

## 0. Geltungsbereich und No-Loss
Gesamtwebsite https://memnosis.github.io/relationalitaet/ inklusive docs/, dashboard/, forschung/website/, Navigations-/Designsystem, Projekt-/Forschungsdashboard, Publikations-/Medienkatalog, Mitmachen und Ergebnisse, alle Fachmodule. Auch ältere Integrations-/Archivzweige, Links und Anker müssen in ein Crosswalk-Inventar, nicht blind überschrieben werden.
Verbindliche Nutzerentscheidungen: 7 Hauptgruppen Start/Forschung/Projekte/Inkubator/Publikationen/Mitmachen/SOULution; Inkubator fusionieren und fachlich differenzieren; zwei-zeiliger Claim SOULution; individuelle Fachfarben, SOULution grün, Mitmachen rot; mobile Funktion, gestufte Navigation; Publikationen originalgetreu, neue Gesamtpublikation erst nach Freigabe. Keine redaktionell-internen Hinweise auf öffentliche Seiten.

## 1. Ziel und überprüfbarer Nutzererfolg
Die Website beantwortet in höchstens wenigen Schritten: Was ist das Forschungsproblem? Was ist tatsächlich belegt? Wie wurde es getestet? Was kann ich selbst versuchen? Wo kann ich Quellen/Methoden/Arbeitsergebnisse finden? Wie gebe ich ein Ergebnis sicher zurück? Welche Grenzen gelten?
Keine Darstellung, die Adresskonvention 3×3×3 als universelles mathematisches Tensorresultat ausgibt. Evidenz sichtbar pro Claim statt pauschaler grün/roter Projektstatus.

## 2. Informationsarchitektur
Start: klare Forschungsfrage, neun SOULution-Lösungsbereiche, Einstieg entlang „verstehen / nachprüfen / beitragen / Werke lesen“.
Forschung: Tensor-Einführung ohne Würfelzwang; fachliche Trinität, Tensoralgebra, Relationen und Negativbeispiele; Logik, Feldtheorie, Geometrie, Physik und Quellenstatus; Forschungsstand und Beweisakten.
Projekte: Mini-KI als eigenes Projekt, Geo-KI, Sprach-/Semantik-KI, Wissenschaftskorpus, Daten/Komposition; Skills und APIs als vernetzte Werkzeugbibliothek, nicht als „eine KI“.
Inkubator: Schrödinger's Inkubator mit digitaler Souveränität, Open-Source-/Re-Engineering-/Sicherheitsbibliotheken, Forschungsfragen und überprüfbaren Integrationspiloten; Mitforschungs-Inkubator als differenzierter Teil.
Publikationen: getrennte Bücher, Fachpapers, Forschungseditionen, Auszüge und Medien; Originalcover, Editions-/DOI-/Lizenz-/Preis-/Zugangsspezifik, Querverweise. Kein neues Buch/PDF ohne Freigabe.
Mitmachen: Bürgerfragen, direkte Prompts, Agentenaufgaben, Meta-Prompts getrennt und nur freigegebene Texte öffentlich; Eingabe/Ausgabe/Rückgabe ohne Git-Schreibrecht, Status und Negativfälle.
SOULution: 3×3 Lösungsbereiche, Forschungsbestände, Lösungsdatenbank, War-/Situation-Room-Pilot, Verknüpfung mit Veröffentlichungen und aktiven Forschungsmodulen.

## 3. Seitentypen und Module
A. Forschungsübersicht: Forschungsfrage, These, Quellen, Beweis-/Widerlegungsstatus, offene Tests, verantwortliche Prüfstelle.
B. Fachseite: Begriffserklärung, anschauliches Beispiel, Formel/Operator mit Typen/Annahmen, Gegenbeispiel, Test, Herkunft, Freigabe und Mitmach-Aufgabe.
C. Forschungs-/Skillkarte: ID, Version, I/O, Geltung, Abhängigkeiten, Teststatus, Alternativen, Rückweg.
D. Task- und Bürgerfrage: verständliche Aufgabe, barrierefreie Schrittfolge, öffentlich zulässiger Prompt, Negativfall, Ergebnisformat, sichere Rückgabe.
E. Publikationskarte: Work-ID, DOI, Dokumenttyp, Cover, Ausgabe, Sprache, Quelle, Rechte/Lizenz und Öffnungs-/Verkaufsweg separat.
F. Dashboard: Aufgabenbestand, Prioritäten, abgeschlossene Tests, bestätigte/widerlegte Relationen, Gegenprüfungsstand, Zyklen und Quellenabdeckung – Nenner und Snapshot-ID zu jeder Anzeige.

## 4. Gestaltung / Interaktion
Eine einzige globale Navigation; breite adaptive Karten, klare H-Abstände, einheitliche Icons, Serifenelemente, barrierefreie Kontraste und sichtbare Fokuszustände. Mobile 320/390/768/1280px, Desktop, Touch, Keyboard, Escape, reduzierte Bewegung, no-JS-Fallback. Mitmachbutton kontextuell, niemals über Inhalt. Keine dekorativen Vollbildanzeigen statt fachlicher Werkcover; Originalcovers erhalten.

## 5. Datenvertrag
Website liest ausschließlich durch Claude/GPT geprüfte öffentliche Projektionen aus einem versionsstabilen Snapshot; PUBLIC-Projektion erlaubt keine privaten Rohprompts/Manuskripte/Personendaten. Quellenregister/Glossar/Skills/Prompt-/Testregister sind über stabile IDs verknüpft. Bei Änderung werden betroffene Seiten und Claims invalidiert; der CI-Build versagt bei defekten Links, ungültiger Referenz, unbekannter Version oder unzulässiger Lizenzannahme. Fachnachweisprüfung und Website-UI-Nachweis sind getrennt.

## 6. Prüfmatrix nach den fünf Runden
W01 Vollinventar alle Seiten, Links, Anker, Zweige und Docs vs Dashboard.
W02 eine Navigation, mobile/Keyboard/no-JS Regression.
W03 gesamte fachliche Nutzerreise Einstieg→Original→Relation→Test→Gegenprobe→Mitmachen.
W04 Behauptungssicherheit: keine Evidenzbehauptungen ohne Beleg und exakte Version.
W05 vollständiger Medien-/Büchertyp mit DOI/Lizenz/Zugang, mobile Darstellbarkeit.
W06 echte Bürgerfragen-/Prompt-Testwege und Rückgabe ohne Git-Rechte.
W07 Projektmanagement mit exakt einem freigegebenen Snapshot; keine manuellen Prozente/erfundenen 100er-Werte.
W08 Datenschutz, Publikations-/Autorenfreigabe, Browser-Sicherheit.
W09 Formeln/Diagramme semantisch und barrierefrei.
W10 Versions-/Originalerhalt, redirects, No-Loss und Retest.

## 7. Nach 5 vollständigen Zyklen zu erzeugende Artefakte
(1) Bestand aller aktuellen/Archiv-Webseiten + Problem- und Redundanzkarte;
(2) Website Gesamtarchitektur v1.0 mit Sitemap und Design-Token/Komponentenregeln;
(3) Priorisierter Migrations-/Upgradeplan inkl. Ankern, mobilen Tests, DoD;
(4) datengebundene Dashboard-/Werk-/Mitmach-Schnittstellen;
(5) GPT-Eigennachweis und Claude-Fachreview; mindestens eine Korrekturschleife;
(6) Entscheidungsvorlage nur für Autorfragen; erst dann Hauptbranch-Release.
Abbruch/Block: Nicht vorhandene private Originale werden als offene Quellen vermerkt, nicht ausgedacht. Kein War Room mit Echtweltversprechen ohne Datenmodell und demonstrierten Pilot.
