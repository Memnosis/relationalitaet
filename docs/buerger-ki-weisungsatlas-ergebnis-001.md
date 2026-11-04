# Bürger-KI – Weisungsatlas Deutschland: Behördenanweisungen, Versionierung und atomare Regeln

**Ergebnisakte:** BKI-WA-001  
**Fassung:** 0.1, 5. November 2026  
**Forschungsstatus:** Erste nachgewiesene Quellenlandkarte und Konvertierungspipeline; **kein vollständiges Behördenweisungsregister und noch keine systematisch geprüften Original-PDF-Konvertierungen**.  
**Geltungsraum:** Bundesrepublik Deutschland (Bund, 16 Länder, nachgeordnete Behörden, Kommunen sowie mögliche Auslandsvollzugsstellen). Die „Weltkarte“ bezeichnet im Projekt einen mehrdimensionalen Raum aus Verwaltungsebenen, Fachgebieten und Zuständigkeiten; eine weltweite Behördenvollerfassung ist nicht behauptet.

## 1. Forschungsziel und Grenzen

Gesucht werden veröffentlichte oder rechtmäßig zugänglich gemachte **Verwaltungs- und Handlungsanweisungen**: Verwaltungsvorschriften, Erlasse, Rundschreiben, Dienstanweisungen, fachliche Weisungen, Durchführungsbestimmungen, Vollzugshinweise, Arbeitshilfen, interne Leitfäden, Verfahrenshandbücher und einschlägige fachliche FAQ. Nicht jede Bezeichnung steht für den gleichen Rechtsrang, Adressatenkreis oder dieselbe Verbindlichkeit. Gesetz, Verordnung, gerichtliche Entscheidung und behördliche Weisung bleiben eigene Dokumenttypen.

Die Frage „welche Weisung gilt für welche Behörde und welchen Zeitraum?“ kann nicht mit einer pauschalen Bundessuche beantwortet werden. Manche Anweisungen sind nicht öffentlich zugänglich, nicht digital dokumentiert oder wurden lokal verändert. **Nicht gefunden ist weder nicht existent noch außer Kraft.**

Zweck der Bürger-KI ist ein öffentliches, überprüfbares **Fachwissen- und Skill-Register**, nicht die Verarbeitung persönlicher Fälle. Die bundesweiten und regionalen Bestände sollen in nachvollziehbare Quellen- und Regelgraphen überführt werden.

## 2. Erste nachgewiesene Bestände (13 Register-Einstiege)

| ID | Ebene | Quelle / Nutzen | Format und Abdeckungsgrenze |
| --- | --- | --- | --- |
| W-001 | Bund | [Verwaltungsvorschriften im Internet](https://www.verwaltungsvorschriften-im-internet.de/) – ressortübergreifende Verwaltungsvorschriften | HTML/XML bzw. PDF je Dokument; keine Sammlung aller hausinternen Weisungen |
| W-002 | Bund | [Bundes-VwV nach Normgeber](https://www.verwaltungsvorschriften-im-internet.de/erlassstellen.html) | Ersteller-/Ressortregister und historische Ressortnamen |
| W-003 | Bund/BA | [BA SGB-II-Weisungen nach Rechtsnorm](https://www.arbeitsagentur.de/ueber-uns/veroeffentlichungen/gesetze-und-weisungen/sgbii-grundsicherung) | viele PDF-Weisungen, historische/neue Fassungen nebeneinander |
| W-004 | Bund/BA | [BA Einzelweisungen und Jahrgänge](https://www.arbeitsagentur.de/ueber-uns/veroeffentlichungen/weisungen) | fortlaufende Weisungskennungen und Jahresarchiv |
| W-005 | Bund/BMF | [Anwendungserlass zur Abgabenordnung](https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Steuerverwaltungu-Steuerrecht/Abgabeordnung/AO_Anwendungserlass_AEAO/ao_anwendungserlass_aeao.html) | Änderungs-BMF-Schreiben, Versionskette |
| W-006 | Baden-Württemberg | [Erlasse und Anwendungshinweise Migration](https://jum.baden-wuerttemberg.de/de/migration/erlasse-und-anwendungshinweise) | ausdrücklich als PDF veröffentlichte ministerielle Hinweise |
| W-007 | Brandenburg | [BRAVORS Fundstellennachweis Verwaltungsvorschriften](https://bravors.brandenburg.de/de/vorschriften_fundstellennachweis_verwaltungsvorschriften) | Rechts-/Fundstellenkatalog |
| W-008 | Brandenburg | [Kommunalaufsicht: Runderlasse und Rundschreiben](https://mik.brandenburg.de/mik/de/kommunales/runderlasse-rundschreiben/) | PDF und BRAVORS-Verweise |
| W-009 | Hamburg | [Transparenzportal](https://suche.transparenz.hamburg.de/) | getrennte Kategorien für Dienstanweisungen und Verwaltungsvorschriften |
| W-010 | Hessen | [Hessenrecht](https://justizministerium.hessen.de/buergerservice/hessenrecht) | Landesrecht und erfasste Verwaltungsvorschriften |
| W-011 | NRW | [Veröffentlichungsrichtlinien, Fassung ab 01.12.2025](https://recht.nrw.de/lrmb/verwaltungsvorschrift/01122025-richtlinien-fuer-die-gestaltung-den-erlass-und-die/) | explizites Fassungsdatum und Änderungskette |
| W-012 | Sachsen | [REVOSax: Positivliste geltender VwV der Staatsregierung](https://revosax.sachsen.de/vorschrift/21440-VwV-geltende-VwV-StR) | Liste mit explizitem Ausnahmehinweis für nicht öffentlich bestimmte sicherheitsrelevante Weisungen |
| W-013 | NRW/kommunal | [FragDenStaat: Anforderung hausinterner Jobcenter-Weisungen](https://fragdenstaat.de/anfrage/saemtliche-dienstanweisungen-internen-weisungen-und-arbeitshilfen-des-jobcenters-ab-2005/) | dokumentierter IFG-Anfrage- und Schriftwechsel, **kein nachgewiesener Vollbestand** |

**Forschungsbefund:** Die BA veröffentlicht nicht nur aktuelle Weisungen, sondern führt einen historischen Jahrgangszugang und ausdrücklich die Möglichkeit späterer Änderungen an. Im Bundes-VwV-Register ist zu beachten, dass bestimmte Sachmaterien in separaten Fachdatenbanken geführt werden. Die Frage nach „allen Bundesweisungen“ braucht also **mehrere parallele Harvest-Kanäle**.

Sachsen benennt ausdrücklich nicht veröffentlichte Vorschriften aus Sicherheitsgründen. Für den Atlas sind diese als mögliche **Bestandslücke / Zugänglichkeitsgrenze**, nicht als fehlende Dokumente, zu kennzeichnen.

## 3. Flächenatlas und Institutionenebenen

Die Dateien [Atlas-JSON](./data/bki-weisungsatlas-v0-1.json) und [Atlas-Oberfläche](./buerger-ki-weisungsatlas.html) führen alle 16 Bundesländer. Stand der ersten Quellenrecherche: **6 Länder mit konkret nachgewiesenem Einstieg; 10 Länder noch nicht systematisch untersucht**. Eine leere Landeskachel heißt ausschließlich `not_researched`. Dies ist kein Negativbefund zur tatsächlichen Existenz.

Die spätere Vollstruktur benötigt außerdem:
- **Bund:** Ressort, Ministerium, Bundesoberbehörde, Behörde mit eigenem Geschäftsbereich, Bundesagentur, Familienkasse usw.
- **Land:** Landesministerium, Landesoberbehörde, Mittelbehörde, Polizei-/Schul-/Sozial-/Ausländer-/Kommunalaufsicht.
- **Kreis und Kommune:** Kreisverwaltung, kreisfreie Stadt, Jobcenter (Trägermodell und örtliche Befugnisse), örtliche Fachämter.
- **Fachliche Reichweite:** Welche Behördentypen müssen die Weisung anwenden, welche haben nur informierende Hinweise?
- **Territorium:** Bundesland, Regierungsbezirk, Kreis, Gemeinde sowie mögliche grenzüberschreitende Rechts-/Vollzugsbezüge.
- **Zeitdimension:** erlassen, veröffentlicht, in Kraft, geändert, aufgehoben, historisch angewendet.
- **Publikationsraum:** amtliches Portal, ministerielle Website, Transparenzregister, Auskunftsarchiv (z. B. FragDenStaat), sonstige Sekundärquelle.

**Nicht mit einer Landkarte verwechseln:** Der Vollzugsraum ist nicht allein eine geografische Fläche. Bundesweite, fachgebundene, behördeninterne und kommunale Weisungen können denselben Ort überlagern.

## 4. Dokumentregister – versionierter Vertrag

```json
{
  "document_id": "BKI-W-BA-SGBII-0042",
  "title": "Beispielbezeichnung – kein reales Dokument",
  "document_type": "fachliche_weisung",
  "issuer_org_id": null,
  "recipient_org_ids": [],
  "jurisdictions": ["DE"],
  "topics": ["soziales"],
  "norm_refs": [],
  "source_url": null,
  "archive_urls": [],
  "published_at": null,
  "valid_from": null,
  "valid_until": null,
  "supersedes": [],
  "superseded_by": [],
  "retrieved_at": null,
  "source_sha256": null,
  "source_format": "pdf",
  "permission": "not_assessed",
  "completeness": "unknown",
  "conversion": "not_started",
  "evidence_status": "not_reviewed"
}
```

Ein **Dokument** kann viele **Fassungen** haben; eine **Fassung** mehrere **Dateien** und verschiedene Fundstellen. Abrufdatum ist kein Inkrafttretensdatum. Ein Dokument im FragDenStaat-Anhang ist nicht automatisch amtlich bestätigt oder aktuell.

## 5. PDF/Web → Markdown → atomare Anweisungen

`Originalfundstelle → Rechteprüfung → Datei/Snapshot + SHA-256 → Text-/Layout-Extraktion → Markdown mit Seiten-/Abschnittsankern → segmentierte Norm-/Anweisungskandidaten → fachliche Klassifikation → Inversions-/Grenztests → verifizierte Regelakte → Skill-Anschluss`.

**Technische Erstimplementierung:** [weisungsatlas_atomizer.py](https://github.com/Memnosis/relationalitaet/blob/main/forschung/buerger-ki/weisungsatlas_atomizer.py). Akzeptiert lokale HTML/TXT/PDF-Dateien, bewahrt Ursprungs-URL, Herausgeber, Abrufdatum, SHA-256 und Abschnitts-/Seitenanker. Erkennt sprachliche **Kandidaten** über Modalwörter („muss“, „soll“, „darf“, „wenn“, „sofern“ usw.). Die Ausgabe besteht aus Markdown und atomaren Kandidaten-JSON.

**Grenzen:** Noch nicht gegen reale Amts-PDFs getestet; keine OCR für Scans, keine Tabellen-/Fußnotenrekonstruktion und keine geprüfte Regelinterpretation. Bei nicht eindeutig erkennbarer Anweisung dürfen aus syntaktischen Stichwörtern keine verbindlichen Regeln konstruiert werden. Das Skript gibt **keine Freigabe zur öffentlichen Wiederveröffentlichung fremder Volltexte**; Lizenz und Nutzungsrechte sind separat zu prüfen. Insbesondere weist die Bundesagentur für Arbeit für ihre Weisungen auf Urheberschutz und Nutzungsbeschränkungen hin. Für öffentliches GitHub zunächst nur Index, Fundstelle, eigene kurze Analyse, Metadaten und erlaubte Auszüge.

### Atomvertrag

Jede atomare Aussage braucht nach Fachprüfung:
- **Regel- und Versions-ID**, Originalfundstelle (Seite, Überschrift, Absatz, Textanker, Dokument-Hash).
- **Veranlasser/Akteur** und **Adressat** der Weisung, konkrete Handlung, Bedingung, Ausnahme, Frist und ggf. Ermessen.
- **Modus**: Pflicht / Verbot / Erlaubnis / Empfehlung / interne Ablaufregel / rein informative Aussage.
- **Geltung**: Rechtsnormbezug, Territorium, Behördenebene, Behördenart, Fachaufgabe, Zeitraum.
- **Rang und Konflikt**: Gesetz vor Verwaltungsvorschrift; erkennbare Kollisionen, Abweichungen und Nachfolger.
- **Test**: Positivfall, Negativfall, Grenzfall, Rückfrage bei fehlenden Tatbestandsmerkmalen.
- **Status**: maschineller Kandidat → redaktionell geprüft → fachlich gegengeprüft → freigegeben / widerlegt / ersetzt.

Atomisieren bedeutet nicht, den ursprünglichen Kontext zu verlieren. Jede Auskopplung muss zur Originalpassage zurückführbar sein.

## 6. Erste atomisierte Probe – GGO § 69 (paraphrasierte Kandidaten)

**Original:** [Gemeinsame Geschäftsordnung der Bundesministerien, § 69](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_21072009_O11313012.htm) (Bundesregelung; hier anhand der öffentlich abrufbaren HTML-Fassung ausgewertet, **keine vollständige Markdown-Transkription**).

| Kandidat | Atomarer Sinn (eigene Kurzrekonstruktion) | Auslöser / Folge | Prüfstatus |
| --- | --- | --- | --- |
| GGO-69-A | Vorschriften mit allgemeiner verwaltungsinterner Bindungswirkung sollen entsprechend als Verwaltungsvorschriften bezeichnet sein und den fachlichen Gegenstand kenntlich machen. | Erstellung einer abstrakt-generellen internen Regel | `paraphrase_needs_review` |
| GGO-69-B | Für ihre Vorbereitung ist auf das einschlägige BMI-Handbuch zurückzugreifen. | Vorbereitung eines Verwaltungsvorschriftenentwurfs | `paraphrase_needs_review` |
| GGO-69-C | Bei neuen Verwaltungsvorschriften ist die Notwendigkeit zu begründen und eine Verringerung/Vereinfachung des Bestands anzustreben. | Neuregelung / Bestandsprüfung | `paraphrase_needs_review` |

**Achtung:** Dies ist eine Demonstration des Datenmodells, nicht eine juristisch geprüfte Auslegung von § 69 GGO. Für eine verwendbare Skillregel braucht es die vollständige Originalpassage, Geltungsprüfung und Gegenprobe.

## 7. Harvest- und Versionierungslogik

**Systematische Quellenentdeckung:**
1. Öffentliche Verzeichnisse mit stabilen URLs und Listeninhalten inventarisieren.
2. Dokumente, amtliche Fundstellen, Fassungshinweise, IDs, Anhänge und Änderungsbezüge extrahieren.
3. FragDenStaat-Anfragen als **ergänzenden Fundkanal** registrieren, inklusive Behördenantwort, Offenlegung und geschwärzten Anhängen; keine Behauptung, jeder Antrag habe vollständige Akten erzeugt.
4. Quelle und Datei getrennt kennzeichnen; PDF, HTML, XML, gescannte Anlagen und Dubletten nach Hash/Struktur erkennen.
5. Bei jeder neuen Fassung die atomaren Regelakte mit `unchanged / amended / added / repealed / unverified` vergleichen.
6. Unklare Quellen, fehlerhafte Downloads und Behörden ohne offene Bestände als Arbeitspakete dokumentieren.

**Wartung:** Die Weltkarte wird niemals pauschal als „aktuell“ ausgezeichnet. Jede Fundstelle bekommt ihren letzten nachweisbaren Such-/Abrufzeitpunkt und Status; regionale Lücken werden sichtbar belassen.

## 8. Acht Pilotprojekte

| ID | Projekt / prüfbares Ziel | Abnahme |
| --- | --- | --- |
| WA-P01 | Bundes-VwV-Ressortregister inventarisieren | Fundstellen-IDs und dokumentierte Ausschlüsse |
| WA-P02 | BA-Weisungsbestände nach Rechtsnorm und Jahrgang listen | konsolidierter Versionen-/Nachfolgergraph |
| WA-P03 | 16 Länder-Publikationsräume erfassen | mindestens ein amtlicher Einstieg je Land oder begründete Lücke |
| WA-P04 | FragDenStaat-Weisungsarchiv erschließen | Anfragen/Anhänge getrennt; Verfügbarkeit und Herkunft |
| WA-P05 | PDF-/HTML-Markdown-Pipeline testen | nachgeprüfte Absatz-/Seiten- und Tabellenrekonstruktion |
| WA-P06 | Weisungen atomisieren und typisieren | 100 fachlich geprüfte Regelakte aus mehreren Rechtsgebieten |
| WA-P07 | Geltungs-/Konfliktgraph bauen | 10 echte Gegenproben zu Fassungen, Ausnahmen und örtlicher Reichweite |
| WA-P08 | Bürger-KI-Skilltests | Quelle → Regel → Handlung; unabhängige Baseline und Prüfer |

## 9. Erste Ergebnismetriken

**Tatsächlich in Version 0.1:** 13 dokumentierte Quellen-Einstiege; 16 Landesknoten; 6 Länder mit belegtem Portal-/Spezialeinstieg, 10 Länder mit noch offener Recherche; ein programmgesteuerter Konvertierungs- und Kandidatenatomisierungs-Prototyp; drei paraphrasierte, noch ungeprüfte GGO-§69-Regelkandidaten.

**Nicht vorhanden/bestätigt:** vollständige Dokumentbestände der Bundesressorts, alle Anweisungen der Länder, heruntergeladene amtliche PDF-Korpora, geprüfte PDF→Markdown-Konvertierungen, 100 freigegebene Regelatome, behördenübergreifende vollständige Zuständigkeitskarte und nachgewiesene Live-Aktualisierung.

**Forschungsstatus:** ein erster, konkret referenzierbarer Weisungsatlas mit Importdesign und dokumentierten Negativbefunden. Er ist **kein vollständiger Bund-Länder-Weisungskatalog**.

## 10. No-Loss und nächste Etappe

`Behördenknoten → Publikationsregister → Quelldokument → Fassung → PDF/HTML/XML → Markdown → Textanker → Regelkandidat → geprüfte Regel → Behörden-/Geltungsrelation → Skill → Test → Ergebnisbericht`.

Register für Behörden, Quellen, Glossar, Skills und Testfälle tragen stabile IDs; bei Änderung eines Dokuments werden betroffene Regelakte, Tests und Publikationen neu bewertet. Eine öffentliche Antwort muss ausweisen: Dokumentstand und tatsächliche Reichweite bekannt / unbekannt.

**Nächste konkrete Abnahme:** 1 BA-Weisungs-PDF, 1 Landeserlass-PDF und 1 amtliche Bundes-HTML-VwV rechts-/lizenzgerecht lokal extrahieren und fachlich stichprobenprüfen. Dann originalgetreue Markdown-Struktur und unabhängige atomare Regelauswertung vergleichen. Erst so wird aus dem derzeitigen Erstinventar ein belastbarer Regelbestand.

---

*Quellenstand 05.11.2026; der Bericht enthält bewusst keine unbelegte Anzahl aller Weisungen und keine pauschale Behauptung ihrer Aktualität.*
