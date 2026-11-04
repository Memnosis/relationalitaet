# DATEN-, WISSENS- UND MEDIENGESAMTKONZEPT · Upgradeauftrag nach 5 abgeschlossenen KI-Zyklen
Version: 0.1 · 2026-11-04 · Status: Konzeptgrundlage, Umsetzungsgate = 5 vollständig abgeschlossene Zyklen
Owner: Claude (Quellen/Daten/Evidenz); GPT (Medien-UX, öffentliche Sichten, Seitenintegration). Beide prüfen alle Teilbereiche gegenseitig.

## 0. Bestände, Provenienz, Rechte
Inventarisieren: Originalarchive/44 Stände, Quellenregister, Glossar 1072 historische Einträge, 309 Trinitäten/103 Gerüste, 27 Feldakten und 12 Relations-IDs, 107 Operator-/Trägerprofile, 1017 historische Relationsakten, 7622 DLMF-Formeln, Prompt-Crosswalk 82 IDs/102 Vorkommen, 65 Zenodo-Werke als datierter Snapshot, Cover/Abbildungen, Medienressourcen und bisherige Buch-/Forschungs-PDF/DOCX/MD-Versionen. Zahlen erhalten explizite Bedeutung, Bezugsobjekt, Zeitpunkt und Quelle. Bestände sind *nicht automatisch fachlich verifiziert*. Private Manuskripte, Rohprompts und Nutzerergebnisse verbleiben in echtem privatem Speicher, nicht im öffentlichen Git.

## 1. Datenarchitektur
Quellformatregister (Originale nie überschreiben) → stabile IDs, Content-/Version-SHA und Crosswalk → fachliche Entitäten: Quelle, Werk, Modell, Formel, Relation, These, Trinität, Tensor, Feld, Glossar, Skill, Prompt, Test, Beweisakte, Medienobjekt, Publikation, Autorenentscheidung → No-Loss-Graph → Ereignis-/Zustandsakte → nachweisbasierter Projektstand → freigegebene öffentliche Lesesichten für Website/Reports/API.
Daten-Owner ändern ihre Bereiche; Review-Events fremder KI ersetzen nie die eigene Ownerakte. Bei Diskrepanzen bleibt der Widerspruch mit Provenienz und Entscheidungspfad sichtbar.

## 2. Wissenschaft und Prüfstufen
Original-/Extrakt-/Rekonstruktions-/Hypothesenstatus getrennt. Evidenz D/F/O/K/B/offen und Prüfqualifikation: ungetestet, Eigenprüfung, gegengeprüft, reproduziert, unabhängig repliziert, widerlegt, unklar. Test erfordert Input-/Skript-SHA, Geltungsbedingungen, Umwelt/Tool-Version, tatsächlichen Exitcode, Gegen-/Grenzfälle und Ergebnis-Scope. SKIP kein PASS. Replizierte bekannte DLMF-Identität kein neu bestätigter Tensor. Relationsfamilien und negative Beispiele systematisch in die Wissensstruktur aufnehmen.

## 3. Change-Impact-Compiler
Jede neue/ersetzte Quelle, Definition, Formel, Relation, Prompt-/Skillversion oder externes Mitmacherergebnis ermittelt alle abhängigen Thesen, Operationalisierungen, Glossareinträge, Formeln, Trinitäten, Tensorpositionen, Tests, Erklärungen und Webmodule. Validator markiert `stale`/Blocker, erzeugt überprüfbare Nachprüfaufträge, protokolliert Original und Folgeversion; keine stille Ersetzung. Nachfolge-/Isomorphie-/Homomorphie-/Teilstruktur-/Nichtabbildbarkeitsrelationen getrennt typisieren.

## 4. Medien- und Veröffentlichungsmodell
Typen: Buch, Paper, Forschungsedition, Preprint, Auszug, Arbeitsstand, Cover, Grafik/Diagramm, Bildbibliothek, Werbung/Anzeige, Datensatz, interaktives Modul. Werk (logische Identität) getrennt von Edition/Datei/Medienobjekt: DOI-Version/Concept-DOI, Datum, Sprache, Coverquelle, Dateihash, Zugangsweg (Open Access, bezahlt, auf Wunsch kostenfrei), Werk-Lizenz (nicht pauschal Website-Lizenz), Rechte Dritter, Zitierform, Freigabe, Vorschau/Thumbnail, Relationen (gehört_zu, übersetzung_von, auszug_aus, ersetzt).
Bücherkarten mit bestehenden Cover-Originalen, keine erfundenen Titel/Cover. Nichts hinter der kostenpflichtigen Schranke als frei behaupten. Vollformat-A4-Anzeigen nur wo gewünscht, eindeutige Medienherkunft. Öffentliches Potenzial und sonstige Texte nur mit verifiziertem DOI und Lizenz.

## 5. Öffentliche Daten und Rückgaben
Public-first Allowlist-Export; nie private vollständige Liste mit lediglich roten Flags. Nur tatsächlich freigegebene und lizenzgerechte Einträge. Externe Nutzer können freigegebene Aufgaben mit eigener KI lösen; Ergebnisrückgabe im definierten Format (ID, Input-Snapshot, Output-/Quellenlinks, Zustimmungs-/Rechteerklärung, Version, Prüfer, fachlicher Status), zunächst private Moderation, dann mögliche Freigabe. Keine anonyme Datensammlung ohne Datenschutzkonzept. Trennung Nutzerbeitrag als Quelle vs geprüfter wissenschaftlicher Claim.

## 6. Medienverwaltung als Datenproblem
Jedes Medienobjekt mit media_id, work_id, variant, original_sha256, source_path, rights_holder, license, attribution, alt_text, language, file_type, dimensions, creation/source status, release_decision. Ziel: Originalcover automatisch zuordnen; Thumbnail/Druckvarianten ohne No-Loss; keine verwaisten Coverlinks. Bildquelle muss prüfbar sein, keine generative Ersatzillustration für Originalpublikation.

## 7. Architekturtests
D01 alle bestehenden IDs/Versionen erhalten; Quell-/Werk-/Medien-Crosswalk vollständig oder als offene Lücke.
D02 Daten-Rebuild deterministisch mit Snapshot-ID und JCS, fremder Gegenlauf gleich.
D03 keine Freigabe aus bloßer Dateiexistenz oder Teilreview.
D04 ein neuer oder geänderter DOI aktualisiert tatsächlich alle betroffenen Web-/Buchkarten.
D05 Änderung einer Glossardefinition invalidiert abhängige Thesen/Prompts/Tensorfelder.
D06 öffentliches Exportformat enthält keine privaten Daten und keine unfreigegebenen Prompts.
D07 widersprüchliche Quellen/Claims bleiben als Konfliktakten sichtbar.
D08 kein SKIP als PASS, fehlender Quell-SHA blockiert.
D09 identisches Buch mit mehreren Editionen/Covern dedupliziert ohne Versionsverlust.
D10 externe Mitmacher-Rückgabe wird nur nach Provenienz-/Lizenz-/Prüfung als Forschungsdaten akzeptiert.
D11 Automatischer Medien-Lizenz-/Attributionscheck und mobile Coverzuordnung.
D12 Website, Bericht und öffentliche API verweisen auf denselben Snapshot-ID und denselben semantischen Status.

## 8. Nach 5 vollständigen Zyklen zu erzeugende Artefakte
(1) Daten-/Medien-Vollinventar mit Dubletten/Versionen/fehlenden Originalen;
(2) kanonisches Wissens-/Evidenz-/Medien-Schema und dokumentierte Legacy-Adapter;
(3) funktionsfähiger Change-Impact-Compiler + Regressionstests;
(4) öffentliches Werk-/Publikations-/Medienregister und privater Gesamtbestand;
(5) validierter Export für Site/DOCX/API und externer Rückgabeprozess;
(6) Claude-Eigenaudit und GPT-UX-/Konsistenzreview plus gemeinsame Korrekturrunde;
(7) konsolidierte priorisierte Migrationsliste, Autorfreigaben separat.
Wichtig: Fünf-Runden-Meilenstein ist Konzept- und Integrationsreview, keine automatische Veröffentlichung privater Werke.
