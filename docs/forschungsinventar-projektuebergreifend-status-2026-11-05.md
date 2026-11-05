# KI-Tensor / SOULution / Bürger-KI – Bestandsinventar, Datenbeziehungen und Lücken

**Bestandsprüfung · 5. November 2026 · Status: erste projektübergreifende Konsolidierung, kein vollständiger automatischer Repository-Crawl.**

## Kurzbefund
**Ja, es gibt eine sinnvolle Inventarisierungsbasis. Nein, es gibt noch kein vollständiges, konsistent verknüpftes Projektinventar.** Die bisherigen Kataloge erfassen verschiedene fachliche Ebenen, jedoch nicht durchgehend mit einer eindeutigen kanonischen ID, Quellenstand, Testhistorie und abhängigen Publikationsstellen.

## Vorhandene Bausteine
| Inventar/Ort | Stärken | Grenze |
|---|---|---|
| [Projektinventar und Standards-Crosswalk](./paper-gesamtinventar-fachbereiche-skills-register-crosswalk-2026-11-05.md) | Gemeinsame Fachbereiche, Standards, Register und Fehlstellen | Überblick statt vollständiger Objektlisten |
| [Bürger-KI-Redaktionsinventar](./buerger-ki-redaktionsinventar-2026-11-05.md) | Dateiweise Funktion, Zuständigkeit, Prüflücken | Erste Teilinventur, keine E2E-Abnahme |
| [Projektmanagement](./projektmanagement.html) | Aufgaben, Forschungsstand, Handlungsreihenfolge | Kein vollständiger, automatisch synchronisierter Objektgraph |
| [Forschungsdaten](./forschungsdaten.html) | Historische Tensorgerüste, Trinitäten und veröffentlichte Datensätze | Historisches Adressinventar ist kein Nachweis bestätigter Feldrelationen |
| [Bürger-KI-Forschungsbibliothek](./buerger-ki-forschungsbibliothek.html) | Auffindbarkeit nach Themen | Kuratierter Index, ausdrücklich nicht vollständiges Repository-Inventar |
| [Corona-Forschungsedition](./buerger-ki-corona-gesamtansicht.html) | Thematische Bündel, Papers, Quellen, Evidenzgrenzen | Deep Dives und unabhängige Validierung teilweise offen |
| [Corona-Quellenatlas](./paper-corona-quellen-datenbanken-status-fruehwarnung-v0-1.md) | Getrennte Datenbanken, historische Statusberichte, Frühwarn- und Prüfquellen | Vollständige Claim-zu-Quellenverknüpfung fehlt |

## Ein gemeinsamer Objektvertrag
Jeder künftige Forschungsbaustein soll mindestens `canonical_id`, `namespace`, `project`, `object_type`, `title`, `source_path`, `source_version`, `created_at`, `review_status`, `depends_on[]`, `source_refs[]`, `claim_ids[]`, `test_ids[]` und `publication_refs[]` erhalten. Identische Kurzkennungen unterschiedlicher Katalogstände sind nicht automatisch identisch.

## Beziehungen, die noch nicht überall durchgängig funktionieren
`Quelle → Beobachtung → Begriff → Frage → Aussage/These → Operator/Skill → Test/Gegenprobe → Resultat → Evidenzgrad → Publikationsstelle`.

Für Corona kommt die historische Dimension hinzu:
`event_date → knowledge_available_at → published_at → source_revision → measure_definition → decision_date → outcome_observed_at`.

## Qualitäts- und No-Loss-Regeln
1. Historische Originale und alte Versionen bleiben erreichbar; Dubletten werden markiert, nicht ohne Crosswalk gelöscht.
2. Ein Homepage-Link beweist weder Quellenqualität noch Browser-Funktion.
3. Reifegrad eines Dokuments getrennt vom Evidenzgrad seiner Aussagen ausweisen.
4. Nach Änderungen müssen Quellenregister, Glossar, Thesen, Skills, Testfälle und öffentlich sichtbare Verweise synchron nachgezogen werden.
5. Bürger-KI verarbeitet im Projekt keine persönlichen Fallbestände. Gemeinsame Module sind Wissens- und Forschungswerkzeuge.
6. Zusammenführungen nach Projekt, Fachgegenstand, Objektfunktion und Perspektive; Tensorrelationen nur mit typisierten mathematischen Voraussetzungen übernehmen.

## Priorität für die Umsetzung
**P0:** Dateiinventar automatisiert aus Repository und Branches generieren; Dateien einzeln klassifizieren (Quelle, Paper, Daten, Skill, App, Bild, Archiv, Entwurf), die kanonischen Eigentümer zuordnen.  
**P1:** Bestehende Register über geprüfte IDs verbinden und historische Kollisionen ausdrücklich dokumentieren.  
**P2:** Pro Paper Claim-/Quellenmatrix, Prüfmethode, Reifegrad und Veröffentlichungsstand nachziehen.  
**P3:** Browser-/Linktests und Änderungscompiler je Objekt, nicht bloß pauschal pro Seite.

**Schluss:** Die bisherige Inventarisierung ist nützlich und keine Nullarbeit. Ihre Schwäche ist die Zersplitterung in mehrere Register ohne vollständigen No-Loss-Gesamtgraphen.
