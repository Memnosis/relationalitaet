# P0-Koordination · Zenodo-Werkregister intern, relevante Quellen selektiv öffentlich
**An:** Claude (Daten-/Forschung-KI), GPT (Website) · **Zyklus:** KI-2026-11-03-001 · **Auftraggeber:** Nils · **Stand:** 03.11.2026

## Verbindliche neue Autorenanweisung
1. Die **Gesamtübersicht aller eigenen Zenodo-Werke** dient vorerst nur dem **internen Forschungs- und Versionsabgleich**. Nicht als vollständige Liste auf GitHub Pages, im öffentlichen Quellenregister oder im Git-Repository `main` spiegeln. **Auch `forschung/` in `main` ist öffentlich!**
2. Mehrere Zenodo-Einträge werden aktuell überarbeitet. **Veröffentlichungsdatum oder DOI ersetzen keinen fachlichen Aktualitäts- oder Gültigkeitsnachweis.** Alte Versionen, neue Versionen und etwaige Errata pro Werk mit eigenem Versionsgraph führen; niemals bestehende Zitate stillschweigend auf die neueste Version umbiegen.
3. Für eine **konkrete Fachseite/Claim** nur diejenigen Zenodo-/Fachquellen zeigen, deren Inhalt tatsächlich den jeweiligen Abschnitt trägt: `claim_id`, `source_id`, exakte Fundstelle, `version`, `claim_relevance`, dokumentierter `check_status`. Primärquellen etablierter Wissenschaft zusätzlich angeben; eigene Veröffentlichungen belegen zunächst den *historischen Projektstand*, nicht automatisch die Wahrheit ihrer wissenschaftlichen Aussagen.
4. Auf der Website kein „alle Werke“, keine ungeprüfte Zahl (57, 65 etc.) und keine vollständige DOI-Exportliste. Relevanz-Auswahl vor öffentlichen Quellenkarten mit nachvollziehbarer Freigabe. Ein Datensatz mit Status `not_reviewed` ist kein öffentliches Zitat.
5. **Interne Masterübersicht und Projektquellen erweitern:** Werkfamilie, Konzept-DOI, Versions-DOI, Ausgabedatum, Titel/Sprachen, Vor-/Nachfolger, Erratum/Status, Dateihash, Quelle/Urheber, Relation zu Logik-Tensor/Tensor-Basics/Feldtheorie, prüfbarer Claim, Relevanzscore und Rückgriff auf vorhandene Quellen. Geheimhaltung nicht per `internal`-Feld in öffentlichem Git simulieren. Nur ein Schema bzw. abgeleitetes, von Nils ausdrücklich freigegebenes *kleines* Referenzset darf öffentlich nach `main`.
6. Die durch Nils bereitgestellte Zenodo-Kopierübersicht ist ein **Such-/Inventarinput** und enthält teils weitreichende physikalische und biologische Behauptungen. Sie ist keine externe Validierung und kein Einzelbeleg, dass diese Behauptungen korrekt sind. In revisionsbedürftigen Einträgen die Claim- und Belegprüfung priorisieren.

## Beispiel für differenzierte Quellverwendung
- **Einführung Tensor**: Tensor Basics, DOI `10.5281/zenodo.19152183` als historische Eigenquelle. Für strenge mathematische Tensorbegriffe separate mathematische Primärliteratur (nicht die eigene Basics-Arbeit als Mathematikbeweis).
- **Logik-Tensor**: Logik-Tensor 1.0, DOI `10.5281/zenodo.19282895`, nur als Originalwerk/27er-Feldquelle und mit archivierter Originalversion; spätere interne 2.0/2.1-Arbeitsfassungen nicht als fertige freigegebene Zenodo-Veröffentlichung darstellen.
- **Feldtheorie**: Tensor Field Theory, DOI `10.5281/zenodo.19153910`, als historische Projektskizze. Die Graph-/Feldanalyse wird separat beweis- oder testbezogen geführt.

## Claude P0 (DATA-007 · Ergänzung zur laufenden B1/B2)
- Interne vollständige Quellenübersicht / Versionsgraph **privat**, Rechte/Publikationsphase klären; Nutzer erhält die vollständige Übersicht nur über geeigneten privaten Transport.
- Auf öffentlichem Git nur Arbeitsvertrag `source_family + canonical_version + versions + proof_claims + relevance_for_page + review_required + approved_public_refs` (Schemafelder ohne vertrauliche Inhalte) und höchstens tatsächlich freigegebene Beispiel-DOIs.
- Zenodo-Metadatenabruf, Prüfsumme eines PDFs, tatsächliche Seite und Urheberschaft voneinander unterscheiden. Änderungen von Originalen unter DOI nicht als ungeprüft identisch übernehmen.
- Rückmeldung an GPT als kleine datierte, überprüfbare **Web-Lesesicht**, getrennt für `tensor-einfuehrung`, `tensor-paper`, `tensoralgebra`, `bibliothek`. Bei noch nicht geprüften Fassungen kein Quelleninhalt generieren, der Beweiskraft suggeriert.
- In der Antwort `CLAUDE_DISKUSSION_02_ZENODO.md` die Übernahme und offene Nachweise bestätigen. Kein künstlicher Zyklusabschluss.

## GPT P0 (WEB-B02-02/03)
- Bestehende Fachseiten additiv um ein didaktisches Grundlagenmodul und um eine explizite Unterscheidung von Original, formaler Mathematik, Hypothese und Nachweis aufwerten.
- Auf Fachseiten nur unmittelbar einschlägige drei historischen Originalwerke nennen; keine Gesamtliste der Zenodo-Werke und keine erfundenen „digital verifiziert“-Angaben.
- Mehrstufige Navigation und konkurrierende Integration vor Entscheidung `DEC-NAV-01` unangetastet lassen.
- Vorher-/Nachher-Gleichheit vorhandener Matrizen, Grafiken, URLs, Skripte und Anker statisch prüfen. Browser-/Mobile-Test gesondert offen lassen.
- Änderungen als `WEB-B02-02/03` und unter `forschung/website/CHANGELOG...` mit Commit dokumentieren.

## Gemeinsame Prüffragen
1. Was muss eine Leserin im Kapitel wirklich wissen, um den nächsten Schritt zu verstehen?
2. Ist die Quelle für diesen **Claim** einschlägig, oder lediglich „Werk aus demselben Projekt“?
3. Ist das Werk, seine DOI-Version und der Zugang nachgewiesen? Ist die wissenschaftliche Aussage selbst belegt?
4. Könnte eine zusätzliche DOI- oder Statusliste den Leser verwirren, obwohl sie in der internen Suche nützt?
5. Wer korrigiert referenzierte Claims, wenn Zenodo-Versionen erneuert werden?

**Austauschpflicht:** Jede KI überprüft Ergebnisse der anderen anhand des gemeinsamen W01–W10/D01–D10/X01-Rahmens. Nach tatsächlich abgeschlossenem Zyklus `ZYKLUSBERICHT.md`, nach drei vollständigen Zyklen übergreifende Analyse.

## Ergänzung: Internes Quellenregister über Zenodo hinaus
Die interne Arbeitsübersicht umfasst **alle** Herkunftsklassen: (1) Zenodo-Vorpublikationen mit Versionen, (2) originale eigene GitHub-Dateien und Commits, (3) historische ZIP-/SQLite-/CSV-/MD-Bestände, (4) eigene Arbeitsmanuskripte und Vorpublikationen außerhalb von Git, (5) wissenschaftliche Fremdquellen (Fachartikel, Bücher, Datenbanken, Standards), (6) tatsächlich ausgeführte Code-/Testartefakte und deren Inputs. Alle Einträge erhalten einen eigenen `origin_kind` und verknüpfen ihre Herkunft mit Claim- und Test-IDs. Die interne Übersicht ist **nicht** automatisch öffentlich, auch wenn einzelne Ursprungswerke öffentlich zugänglich sind.

**Neu vom Autor gelieferter Rohinput:** sieben mehrteilige Zenodo-Kopierlisten mit **65 segmentierten Kandidateneinträgen** (inklusive Versionen und mehreren Sprachfassungen). GPT hat dafür eine *private, nicht nach Git hochgeladene* ZIP-Arbeitsübersicht mit Originalkopiertext, JSON-Kandidaten und Titelliste vorbereitet. Die Zahl 65 bezieht sich nur auf die Segmentierung des angelieferten Materials, **nicht** auf 65 geprüfte, eindeutige Publikationen. Frühere von Claude recherchierte 57 Werke und der 65er-Auszug sind bis zur Vollständigkeits-, Dubletten- und Versionsprüfung nicht als widersprüchlich zu behandeln. Claude erhält die privaten Bytes durch Nils direkt und bestätigt sie anhand einer eigenen Prüfsumme.
