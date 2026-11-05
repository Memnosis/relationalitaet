# Bürger-KI – dateibezogenes Redaktions-, Quellen- und Überarbeitungsinventar

**Stand:** 2026-11-05 · **Bereich:** Bürger-KI in `Memnosis/relationalitaet` · **Status:** in progress (erste Teilinventur)

## Unveränderliche Bereichsgrenze

Bearbeitet werden ausschließlich eindeutig der Bürger-KI zugehörige Dateien. Kein Löschen, Verschieben oder Überschreiben fremder Bestandteile. Insbesondere bleiben `docs/index.html`, `docs/mitmachen.html`, `docs/tensor-*.html`, die Tensor-Forschungsordner und gemeinsame fachübergreifende Datenregister **schreibgeschützt**. Deren Verweise dienen nur der Analyse. Auch `docs/data/skills-oeffentlich-v1.json` wird wegen seines Geo-KI-/Tensor-Anteils nicht verändert. Bei fachübergreifenden Synergien erst einen Bürger-KI-Crosswalk schreiben, dann eine gesonderte Änderung der Fremdbereiche nur nach ausdrücklichem Auftrag.

## Bewertungsmaßstab

Jeder Eintrag erhält Dateipfad, Funktion, Bearbeitungstiefe, Stärken, Fehler/Schwächen, fehlende Übergänge und Status. Statusbezeichnungen: **gesichtet** (Datei und Struktur), **analysiert** (Inhalt gezielt gelesen), **bearbeitet** (Commit nachgewiesen), **offen** (Detailprüfung/Überarbeitung ausstehend), **vorerst gut** (kein Änderungsbedarf aus der bisherigen Prüfung). Ein überprüfter Dateikopf ist keine vollständige inhaltliche Prüfung.

### A – Historische Eingangspfade (vor neuen Spezialpapern priorisieren)

| Datei | Funktion und bisheriger Befund | Kritische Aufgaben / Verbindung | Stand |
|---|---|---|---|
| `docs/assets/buerger-ki-design.css` | Frühe eigene Gestaltung, im historischen Commit-Suchlauf als ältestes einschlägiges Element gefunden | Visuell gegen neuere Bürger-KI-CI prüfen, keine automatische Vereinheitlichung | gesichtet (Historie), offen |
| `docs/buerger-ki.html` | Zentrale Gesamtseite: Rechte, Versorgung, Werkzeuge, Forschungsbrücken; zahlreiche Lernpfade und Papers verlinkt | Hohe Dichte von Inhalten: menschlichen Einstieg, Perspektivenwechsel, Wissenschaft und Technik als unterschiedliche Lesestufen ordnen; Link- und Ankertest | gesichtet (Struktur/Links), offen |
| `docs/buerger-ki-mein-recht.html` | Ursprünglicher Pfad „Mein Recht“ mit Prüfung von Anspruch, Bescheid und tatsächlicher Erfüllung; klarer praktischer Fokus | Verfahrensstadien und Grenzen präzisiert; Verbindungen zu Weg und Therapieplatz ergänzt; später Rechtsquellen und Browserdarstellung testen | **bearbeitet** – Commit `fd0e212a97708d46574b57c4621e68bc117b0b8b`; Nachtest offen |
| `docs/buerger-ki-gemeinsam.html` | Eigenständiger Gruppenpfad: vorhandene Initiativen stärken, gemeinsame Skills statt Fallverwaltung; methodische Gegenbefunde, Legitimation und nicht-automatischer Tensor-Austausch werden ausdrücklich benannt | Die Seite differenziert Einzelfall, methodischen Gruppenbeitrag, Repräsentativitätsgrenzen und Hypothesen bereits sinnvoll. Keine vorschnelle Umschreibung; später Links und §-Bezüge nachtesten | **analysiert, vorerst gut**; Browser-/Quellenprüfung offen |
| `docs/buerger-ki-grundlagen.html` | Grundrechtliche/sozialstaatliche Grundlage der Bürgerperspektive | Garantie, Gewährleistung, Zuständigkeit und faktische Wirkung getrennt erläutern; Quellensynchronisierung | gesichtet (Struktur), offen |
| `docs/buerger-ki-anwendungsfelder.html` | Übertragung wiederverwendbarer KI-Fähigkeiten auf verschiedene Lebensbereiche | Gleiches Skillprinzip vs. unterschiedliches Fachrecht; Übergänge zurück zum konkreten Anliegen | gesichtet (Struktur), offen |
| `docs/buerger-ki-weg.html` | Methodische Wegbeschreibung von Anliegen zu Lösung | Schleifen, Gegenprüfung, Abbruch/Alternative und Ergebnisbelege didaktisch ausführen | gesichtet (Struktur), offen |
| `docs/buerger-ki-gesamtstand.md` | No-Loss-Bestandsdokument, zahlreiche Phasen und Definitionen | Nicht kürzen oder als Webseite ersetzen; Aussagen nach Stand, bestätigtem Ergebnis und offenem Vorhaben entflechten | gesichtet (Gliederung), offen |
| `docs/paper-buerger-ki-originalsprache-claims-didaktik-no-loss-v0-1.md` | Bewahrung ursprünglicher Claims und bürgernaher Dramaturgie | Als verbindliche redaktionelle Prüfschicht vor Umschreibungen nutzen, Originalformulierungen erhalten | gesichtet (Gliederung), offen |

### B – Hohe Wirkung und Synergie

| Datei | Funktion und bisheriger Befund | Kritische Aufgaben / Verbindung | Stand |
|---|---|---|---|
| `docs/buerger-ki-blickwinkel-therapieplatz.html` | Pilotfall für Perspektivwechsel, Bedarf und Lernnavigation | Menschliche Perspektive, Versorgungsrealität, Institution, Wissenschaft und Alternativpfade abgrenzen und verbinden | gesichtet (Struktur), offen |
| `docs/buerger-ki-lernpfade.html` | Forschungsnavigator und alternative Lernwege | Unterschied zwischen Lernroute, Evidenzpfad und Nutzerziel ausformulieren; Anker-/Linkprüfung | gesichtet (Struktur), offen |
| `docs/buerger-ki-forschungsbibliothek.html` | Zugang zu Forschung und Quellen | Inventarabdeckung, Rückverweise und Quellenstatus einzeln prüfen | gesichtet (Struktur), offen |
| `docs/buerger-ki-werkstatt.html` | Werkzeuge zum Fragen, Prüfen und Vergleichen | Trennung von demonstriert, implementiert, geprüft und geplant; sichtbare Ergebnisreferenzen | gesichtet (Struktur), offen |
| `docs/buerger-ki-schutzpflichten.html` | Schnittstelle zwischen Leistung, Prävention, vermeidbaren Schäden und Recht | Rechtliche Schwellen nicht aus bloßer Problembeschreibung ableiten; methodische Gegenprüfung | gesichtet (Struktur), offen |
| `docs/buerger-ki-ziele-lexikon.html` | Übersetzung von Begriffen in Ziele, Handlungswege und Metaebenen | Definitionen, Synonyme, Perspektiven und inverse Suchwege ergänzen | gesichtet (Struktur), offen |
| `docs/buerger-ki-weisungsatlas.html` | Verwaltungsbezogene Rekonstruktion von Regelungen und Weisungen | Normen/Weisungen/Praxis/individuelle Umsetzung auseinanderhalten; methodische Grenzen | gesichtet (Struktur), offen |
| `docs/buerger-ki-skillzentrum.html` | Öffentliche Brücke zwischen KI-Skills, Aufgaben und Papers | Nachgewiesene Fähigkeiten von Aufgabenideen unterscheiden; jedes Skill-Ergebnis nachweisbar zuordnen | gesichtet (Struktur), offen |

### C – Neuere fachliche Spezialtexte

| Datei | Funktion und bisheriger Befund | Kritische Aufgaben / Verbindung | Stand |
|---|---|---|---|
| `docs/buerger-ki-kaffeekraenzchen-fragen.html` | Gesprächseinstieg zu Arbeit, Erfahrungen, Fähigkeiten und Potenzial | Freiwilligkeit der Perspektiven wahren; keine Arbeitslosen-Defizitannahme | gesichtet (Struktur), offen |
| `docs/paper-potenziale-arbeitslosigkeit-unbezahlte-arbeit-innovation-2026-11-05.md` | Potenzialperspektive, unbezahlte Arbeit und Innovation | Begriffe und Messmethoden zwischen Arbeitslosigkeit, Erwerbstätigkeit, gesellschaftlichem Beitrag und Innovation trennen | gesichtet (Einleitung/Gliederung), offen |
| `docs/paper-offener-standard-arbeitsvermittlung-2026-11-05.md` | Standards, Transparenz und Fähigkeitenvermittlung | Was ist bestehender Standard, Entwurf, offene Frage oder Test? Quellen und Systemgrenzen prüfen | gesichtet (Einleitung/Gliederung), offen |
| `docs/paper-gesamtinventar-fachbereiche-skills-register-crosswalk-2026-11-05.md` | Teilinventar und Registerabgleich | Inventar nicht mit Vollständigkeitsnachweis verwechseln; Scope und Lücken kennzeichnen | gesichtet (Einleitung/Gliederung), offen |
| `docs/paper-buerger-ki-corporate-design-legende-2026-11-05.md` | Farbsystem, Marke, Statussprache | Gestaltungsfarbe strikt von Evidenzstatus trennen; bestehende Marke respektieren | gesichtet (Einleitung), offen |

### D – Nur lesend geprüfte Grenzdateien (außerhalb des Bearbeitungsumfangs)

| Datei | Warum betrachtet | Stand |
|---|---|---|
| `docs/index.html` | Übergeordnete Navigation und Verknüpfung zur Bürger-KI | gelesen; **nicht verändern** |
| `docs/mitmachen.html` | Projektübergreifende Verlinkung auf Bürger-KI | gelesen; **nicht verändern** |
| `docs/data/skills-oeffentlich-v1.json` | Gemeinsames Skillregister mit Geo-KI-Inhalten; keine isolierte Bürger-KI-Datei | gelesen; **nicht verändern** |

## Redaktionelle Grundsätze – gesondert vom publizierten Text

1. Die ältesten Elemente vor den neuen Spezialpapern prüfen, damit alte Bedeutungen, gute Überschriften, ursprüngliche Metaphern, alternative Sichtweisen und Entwicklungsstufen erhalten bleiben.
2. **Befund, Interpretation, normative Bewertung, Rechtslage, Forschungsfrage, implementierter Skill, getestetes Ergebnis und zukünftiger Ausbau** nicht ineinander verdichten.
3. Hinweise wie „wird ergänzt“, „später“, „geplant“, „noch einbauen“ nicht blind zu abgeschlossenen Tatsachen umschreiben: erst prüfen, ob das Objekt real vorhanden ist. Nur dann gegenwartsbezogen formulieren, andernfalls als offene Aufgabe im Inventar führen.
4. Nicht nur neue Links: fachliche Brückentexte schreiben, die sagen, **warum** der nächste Blickwinkel sinnvoll ist, was derselbe Zusammenhang erklärt und wo die Analogie endet.
5. Keine erfundenen Vollständigkeitsgrade, Qualitätsmetriken, Tests oder Quellen. Rückverweise mit stabilen Pfaden; Quellen und Glossar in einer Bürger-KI-Crosswalk-Tabelle nachziehen, gemeinsame Register selbst nicht verändern.
6. Die Bürger-KI entwickelt öffentlich nutzbare KI-Fähigkeiten; sie erhebt und verarbeitet im Rahmen dieser Website keine persönlichen Bürgerfälle. Unpassende, hypothetische Datenschutzversprechen nicht als Selbstbeschreibung einbauen.
7. Jeder spätere Eingriff erhält eigenen Status (gesichtet/analysiert/bearbeitet/Browser-geprüft/finalisiert) und einen Git-Commit oder eine explizite Feststellung „kein Eingriff“.

## Noch nicht gesichtete bzw. noch nicht vollständig inventarisierte Gruppen

Weitere Bürger-KI-Phasenpapiere, `forschung/buerger-ki/` (Kernpaper, Python-Module, Tests), Datendateien und experimentelle Apps sowie die vollständige historische Uploadfolge sind **nicht vollständig erfasst**. Vor Aussage einer Gesamtinventur: Repository-Baum aller einschlägigen Pfade und Original-Commitdaten ermitteln; keine Vollständigkeit aus dem Homepage-Linkgraphen ableiten.

## Änderungsprotokoll

- 2026-11-05: `docs/buerger-ki-mein-recht.html`: zusätzliche Rechts-/Verfahrens-/Erfüllungsdifferenzierung, Grenzen und didaktische Verweise. Commit `fd0e212a97708d46574b57c4621e68bc117b0b8b`.
- 2026-11-05: dieses Bürger-KI-Redaktionsinventar neu angelegt. Keine Löschung, keine Änderung an Tensor- oder übergeordneten Seiten.

**Gesamtstatus:** Teilinventur angelegt; eine frühe Bürger-KI-Seite inhaltlich überarbeitet; Vollinventur, übrige Detailanalysen und Browser-Nachtests offen.
