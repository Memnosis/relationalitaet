# Bürger-KI · Anschlussprogramm nach Sprachphase 0–8

**Stand 2026-11-05 · Status: implementierbarer Testauftrag, keine operativ gestartete KI.**

Die **Architektur der neun Sprachphasen** wurde mit ihrem tatsächlichen Bearbeitungsstand abgeglichen. Redaktionelle Phasenfestlegung ist nicht gleich fachlicher Testabschluss. Der vollständige Crosswalk (20 Sprachwelten, 37 Nuclei, 8 Fallpiloten) liegt unter `docs/data/bki-sprach-crosswalk-final-v1.json`.

## Was nun statt weiterer paralleler Papers folgt

**VKI-PILOT-01: Eine komplette, sichere Fähigkeitskette.**

1. **Menschliches Anliegen erfassen:** „Ich verstehe eine behördliche Forderung nicht“ oder „Ich möchte aus einer Statistik ein überprüfbares Problem machen“. Ohne persönliche Daten.
2. **Einordnen:** Ziel, Fachgebiet, Prozessposition, rechts- und sprachrelevante Begriffe. Rückfrage nur bei wirklich fehlendem Kontext.
3. **Kanonische Quelle laden:** Fachquelle und Versionsstand aus Register; nicht nur eine plausible Textantwort generieren.
4. **Passenden vorhandenen Skill auswählen:** statische Regel, Quellenvergleich, Berechnung, Erklärung, Gegenprobe, Datenexport – ausdrücklich unterschiedliche Typen.
5. **Schutzgate:** Keine öffentlich eingereichten Falldaten, keine Rechtsverletzung ohne Evidenz, kein unzulässiger autonomer Rechts-/Verwaltungsakt.
6. **Handlungs- und Quellenkarte ausgeben:** verständliche Begründung, Berechnungsweg, fehlende Daten, konkrete selbstbestimmte nächste Schritte und vorhandene externe Stellen.
7. **Ergebnis lokal in interoperablem Format exportieren:** JSON mit stabiler ID, CSV soweit sachgerecht, lesbare MD-Kurzkarte; kein Pseudo-Permalink für reine lokale Ergebnisse.
8. **Testen:** synthetische Normal-, Sonder-, Fehl- und Gegenbeispielfälle; negative Befunde speichern.
9. **Review/Rückkanal:** nur methodische, veröffentlichbare Verbesserungen; menschliche Moderation vor Veröffentlichung; No-Loss-Nachzug in Glossar, Quelle, Skill, Nucleus, Website.

**Abnahmekriterien:** A) End-to-End-Lauf ohne reale Personendaten; B) gleiche Eingabe erzeugt stabil benannte und quellenbezogene Ergebnisse; C) Sicherheits-/Quellengates stoppen falsche Ausgaben; D) lokale Ausgaben sind wieder importierbar; E) negative Testfälle sind dokumentiert; F) der Browser zeigt nicht „KI läuft“, wenn nur Regeln ausgeführt wurden.

## Stabile Objektbeziehungen

`Quelle → Aussage → Datenfeld → Fehlerhypothese → Messfamilie → Schutzregel → Alternative → Test → Ergebnis → Skill → Nucleus → Sprachwelt → Lernpfad → Website`.

Ein öffentlicher Fall-Link entsteht **erst nach Review und GitHub-Publikation**. Nutzerkopierte JSON-Dateien sind kein gehosteter Datensatz; öffentliches Stimmungsbild und mehrfache Stimmabgaben erfordern separate, kontrollierte Infrastruktur.

## Phase 7/8 als Querschnitt weiterführen

Phase 7 liefert: Betreiber-/Datenkontrolle, Portabilität, Wechsel zwischen lokal und fremden Diensten, offener Standard und nachvollziehbare Governance. Phase 8 liefert: Skill-Verträge, Typisierung, Invarianten, Relationen und reproduzierbare Gegenproben. Keine neuen Nucleus-IDs aus bloßen Themennamen.

## Noch offene publizistische Arbeiten

- 49-Einträge-Forschungsbibliothek gegen aktuelle Pilot-/Metaobjekte nachführen; nur bereits **tatsächlich im Repository vorhandene** Ressourcen verlinken.
- Glossar/source crosswalk und Website-Ansichten mit denselben stabilen IDs synchronisieren.
- Tatsächliche Backend-/Browsertests des Scanners und aller Leser-Eingabeflächen dokumentieren.
- Drei Fallpiloten (Bürgergeld, Wohngeld, Elterngeld): Primärquellen-URLs und Kennzahlendefinitionen erneut prüfen, bevor konkrete Einsparungen oder Rechtsverletzungen auf der Website behauptet werden.

## Nachweisgrenzen

Die 9 Phasen sind **als Forschungsablauf redaktionell konsolidiert**, aber noch nicht alle fachlich/technisch abgenommen. 20 Sprachwelten sind Nuclei zugeordnet, nicht alle Wissensfragen beantwortet. 15 VKI-Fähigkeiten und acht Handoffs sind im vorhandenen Funktionspapier beschrieben, nicht als eigene operative KI implementiert.
