# Navigationsaudit und neue Informationsarchitektur · v0.3

Stand 2026-11-03 · Branch `integration/soulution-shared-core-2026-11-03` · Nicht auf `main` gemergt.

## Anlass
Die Hauptnavigation war nominell ähnlich, aber nicht funktional einheitlich. Unterschiede bestanden bei der Größe der Header, eigenständiger Fachnavigation, Scrollverhalten, CSS-Layouts und einer Seite ohne zentrale Navigation. Die wachsenden KI- und SOULution-Forschungswege einschließlich der neuen Macht-Publikation und der KI-Rechtekritik waren nicht ausreichend gegliedert.

## Neue verbindliche Informationsarchitektur

| Ebene 1 | Ebene 2: zugängliche Bereiche |
|---|---|
| Start | Übersicht der Gesamtsysteme, Orientierung |
| KI & Forschung (ausklappbar) | KI-Landkarte, Entstehung von KI aus Kernskills, Mini-KI, Geo-KI, Tensor, Algebra, Vernetzung, Kompression, Harvesting, Visuelle Engine, Tensor-Paper |
| Wissen & Werkzeuge (ausklappbar) | Bibliothek, Promptbibliothek, Glossar, Codebuch, Interoperabilität, Quellen, Aufgabenkarten, Medien, Projektstand |
| SOULution & Publikationen (ausklappbar) | Neun Forschungs-/Lösungsbereiche, Wissen Macht Wirklichkeit, KI/Kreativrechte und gesellschaftliche Rechenschaft, KI-Kritik |
| Mitmachen | Direkte Fach- und Bürgerbeteiligung, mit Fach- und Projektverweisen |

**Zuordnungsregel:** Technische Frage der KI-Entstehung → `ki-kernforschung.html`; gesamtgesellschaftliche Kritik an Trainingsdaten, Macht, kreativen Rechten und Rechenschaft → SOULution, insbesondere `soulution-ki-kreativrechte.html`.

## Technische Implementierung
- `docs/assets/site-nav.js` ist die gemeinsame zentrale Link- und Gruppendefinition.
- `docs/assets/site-nav.css` enthält die Styling- und Responsive-Regeln.
- Drei native `details/summary`-Dropdowns und direkte Start- und Mitmachen-Links; eine Offenhaltung zur gleichen Zeit, Escape und Click-outside schließen Menüs.
- Aktuelle Seite wird über `aria-current=page` markiert.
- Fallback: Auf Seiten mit alter Hauptnavigation bleiben bestehende Links sichtbar, wenn JavaScript fehlt; die neue Publikationsseite erhält eine dynamisch eingesetzte Navigation, wenn das Skript geladen ist.
- Auf erfolgreich umgestellten Seiten wird die bislang doppelte `ki-fachnavigation` nach Aktivierung des neuen Systems verborgen. Inhalts- und Metaseiten behalten ihre fachlichen Kontextlinks.

## Seitenweiser Status
Untersucht wurden diese 25 Seiten:

| Seite | Status |
|---|---|
| index | gemeinsame Navigation aktiviert |
| ki-systeme | aktiviert |
| ki-kernforschung | aktiviert |
| minimal-ki | aktiviert |
| geoki | aktiviert |
| tensor-einfuehrung | aktiviert |
| tensoralgebra | aktiviert |
| harvesting | aktiviert |
| komprimierung | aktiviert |
| vernetzung-ki | aktiviert |
| bibliothek | aktiviert |
| promptbibliothek | **nicht umgestellt:** GitHub-Schreibtool blockierte den Komplettdatei-Update, bisherige Navigation bleibt |
| projektstand | aktiviert |
| mitmachen | aktiviert |
| soulution | aktiviert |
| wissen-macht-wirklichkeit | aktiviert; zuvor keine globale Header-Navigation |
| soulution-ki-kreativrechte | aktiviert, neu |
| medien | **nicht umgestellt:** GitHub-Schreibtool blockierte den Komplettdatei-Update, bisherige Navigation bleibt |
| tensor-paper | aktiviert |
| visuelle-engine | aktiviert |
| taskkarten | aktiviert |
| quellen-und-uebergabe | aktiviert |
| interoperabilitaet | aktiviert |
| glossar | aktiviert |
| codebuch | aktiviert |
| impressum | aktiviert |

**Befund: 23/25 Seiten auf gemeinsamen Navigationsmechanismus umgestellt.** Zwei blockierte Updates sind ausdrücklich offen. Der Einbau wurde an den Quelldateien kontrolliert; Javascript-Syntaxprüfung bestanden, aber noch kein gerenderter Desktop-/Mobil-Browser- oder Screenreader-Test erfolgt.

## Leseführung
1. **KI verstehen:** Start → KI-Systeme → Kann aus Skills KI entstehen? → Mini-KI / Geo-KI / Tensor → Prüf- und Ableitungsspektrum.
2. **Gesellschaftliche Rechenschaft:** Start → SOULution → KI/Kreativrechte / Wissen Macht Wirklichkeit → Originalquellen → Bürger- und Fachmitmachen.
3. **Selbst forschen:** Mitmachen → Promptbibliothek / Bibliothek → verifizierte Kernskills → Testakten → offene Aufgaben.
4. **Publikation vertiefen:** Wissen Macht Wirklichkeit → vier Originalwerke als wiederkehrende Werkminiaturen, Forschungsmodule, SOULution und Quellenanhänge.

## Nächste Qualitätssicherung
- Beide blockierten Seiten auf denselben Navigationsmechanismus umstellen.
- Desktop-/Mobil- und Tastatur-/Screenreaderprüfung einschließlich Fokusreihenfolge, geöffneter Dropdowns, Sprungmarken und Kontrast.
- Auf GitHub Pages prüfen, dass Skript/CSS mit korrektem MIME-Typ geladen werden und keine Links ins Leere führen.
- Untermenüeinträge nach Nutzung und Relevanz ordnen; die Liste bleibt an einer Stelle pflegbar.
- Erst nach Review mit `main` zusammenführen.

## Was NICHT behauptet wird
- Die öffentliche GitHub-Pages-Seite wurde nicht veröffentlicht oder gemergt.
- Eine JavaScript-Syntaxprüfung ersetzt keinen realen Browser- und Zugänglichkeitstest.
- Die neuen KI-Rechtsberichte beweisen keine pauschale Rechtswidrigkeit aller KI-Trainingsverfahren.
