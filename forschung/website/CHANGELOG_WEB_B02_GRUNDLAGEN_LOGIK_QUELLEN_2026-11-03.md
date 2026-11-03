# Website-Upgrade B02 · Grundlagen, Logik-Tensor und Quellenweg
**Datum:** 03.11.2026 · **Owner:** GPT-Website · **Zyklus:** KI-2026-11-03-001  
**Status:** Drei Module implementiert und statisch geprüft; Browser-/Mobile-/Screenreader-Abnahme weiterhin offen. Nicht als vollständig fertiger Website-Zyklus ausgeben.

## 1. Änderungen, Quellen und Commits
| Task | Datei | Ursprünglicher Blob-SHA | Commit | Änderung |
|---|---|---|---|---|
| WEB-B02-02 | `docs/tensor-einfuehrung.html` | `231575c8dfdae74a1832d386a7cfb3f6b1daa6ca` | `32ca90aeea78f95aeb47cbaa73838349480154a8` | Lernpfad Datenwürfel/Graph/Tensor/Prüfung, A/B/C/G mit ursprünglichen T1/T3/T5-IDs, Modus-ponens-Beispiel; älterer sichtbarer Redaktionssatz im Footer zu neutraler Seitenangabe korrigiert |
| WEB-B02-03 | `docs/tensor-paper.html` | `7894921a5b9787228623ce2514cd19ac172b156a` | `8fff34c41577d988d14cf0512538d9e31e5a6503` | didaktischer Forschungsstand, drei historische Matrizen erhalten, Gegenmodell, Meta-Logik-Prüfkriterien und begrenzte Quellenliste |
| WEB-B02-05 (erste didaktische Sicht) | `docs/bibliothek.html` | `35e4f0ed9be42063e0b120e220a7ebee6f81c5dd` | `02d4e96410d0139b42c69e892583a573946fac92` | Erklärung Claim→relevante Quelle→Prüfstatus→Mitmachaufgabe; keine öffentliche Gesamtliste |
| Gemeinsam | `docs/assets/tensor-learning-modules.css` | neu | `f83b979a7d1ebe2c9796d1011ef5a45cf7937164` | Fachkarten, progressive Vertiefung, Fokusstil, Responsive; keine Navigations-CSS-Änderung |

## 2. Statischer Kontrolltest nach Git-Commit
**Aus tatsächlichem GitHub-Dateiabruf geprüft (neueste geprüfte Blob-SHAs):**
- `tensor-einfuehrung.html`: `8350d0e9db3390cfc35239d0eeecf65ef8dcfad5`; neuer Anker `tensor-grundlagen-heute` vorhanden; bestehender SVG-Ring, 27er-Würfel, CTA vorhanden.
- `tensor-paper.html`: `8bdc28d789da0b2f2c0574e1ec1052f6cf05b319`; `logik-forschungsstand` vorhanden, genau drei unveränderte Originalmatrix-Abschnitte.
- `bibliothek.html`: `d112ae337aa333cf58ecca29e8501bf204bd31d8`; neuer `quellen-pruefweg` vorhanden.
- `tensor-learning-modules.css`: `275a79d0e10a86103632d85afabee5c6933858e2`; gemeinsame Komponentenstile vorhanden.
- **4 neue fachübergreifende Ankerverweise** zwischen den drei Seiten auf ihren jeweiligen Zielseiten nachgewiesen.
- Jede der drei Seiten lädt weiterhin exakt **das bisherige** `tensor-hierarchy.js`; kein zweites Menü-Engine-Skript eingeführt.
- Vorher/Nachher-Stringtest: Alle drei Seiten wurden ausschließlich um ein neues `<link>` plus einen zusätzlichen Inhaltsabschnitt ergänzt; einzige gezielte Ersetzung ist der sichtbare Meta-Footer der Tensor-Einführung. Keine Originalmatrix oder Buchcover überschrieben.
- **Quellenwahl:** neues Logik-Modul verlinkt exakt drei einschlägige historische Autorenwerke (Logik-Tensor 1.0, Tensor Field Theory, Tensor Basics). Zusätzlich existierte bereits ein Original-DOI-Link auf der Seite, der erhalten blieb; somit insgesamt **vier** DOI-Linkvorkommen auf der Seite, davon eines bereits vorhanden. Keine 65er- oder 57er-Werkliste öffentlich eingebunden.

## 3. Noch nicht abgenommen
- Reale Browserumgebung, Desktop/Mobil (auch 390 px), Touch, Tastatur, Kontrast, Screenreader.
- Die 16 Navigations-Merge-Konflikte auf dem Integrationszweig bleiben weiterhin offen. **Kein Merge** und keine Änderung an der aktiven Navigation vorgenommen.
- Claude-Fachreview zu Quellen, Begriffsdefinitionen und der neuen didaktischen Fassung noch offen.
- Die `digital_verifiziert`-Anzeige kommt erst nach Claudes Claim-/Quellenschema (DATA-003); hier ist nur eine sachliche Einführung in den Prüfweg ergänzt.
- Veröffentlichung des vollständigen Logik-Tensor-2.0-Manuskripts als Buch steht weiterhin aus; die Website erklärt vorerst den Entwicklungsstand.
- Der Zeit-/Versionsstand der Zenodo-Originale ist nicht erneut vollständig extern validiert. Auf der Website dienen die drei DOIs als historische Primärbelege des *eigenen* Projekts, nicht als Beweise seiner allgemeinen Fachbehauptungen.

## 4. Zusammenhang mit dem privaten Quellregister
Die sieben vom Autor kopierten Zenodo-Übersichten wurden in einer **lokalen privaten Arbeits-ZIP** in 65 Kandidateneinträge zerlegt, mit unveränderten Rohtexten, JSON, CSV-Titelliste und ausdrücklichem Status `metadata_verified_against_zenodo: false`. **Keine dieser 65 Zeilen wurde nach öffentliches Git kopiert.** Claude soll zusätzlich eigene Git-/Archiv-/PDF-/Fachquellen in einem gemeinsamen internen Versionsgraphen erfassen. Hierzu [Claude-Handoff](../koordination/ZYKLUS_001_ZENODO_RELEVANZ_STATT_GESAMTLISTE_2026-11-03.md).

## 5. Offene Gegenprüfung durch Claude
Bitte W01 Bestandstreue, W04 Didaktik, W05 Achsengenauigkeit, W06 Quellen-/Evidenzdifferenzierung und W09 Design/Barrierefreiheit an den genannten **Blob-SHAs** analysieren und Feedback in `CLAUDE_REVIEW_WEBSITE.md` dokumentieren. Die anderen Website-Vektoren dürfen als `not_assessed` ausgewiesen werden, solange ein echter Browser- oder Merge-Test fehlt.

**Nächste GPT-Prioritäten:** sichtbare Website-Inhalte systematisch auf redaktionelle Metahinweise prüfen; Navigation nur nach Nils-Entscheidung und Merge-Plan verändern; dann getestete Quellenkarten aus Claudes freigegebenem Leseschema in die Bibliothek integrieren.

## 6. Zusatzkorrektur im Design
Die gemeinsame CSS-Datei wurde anschließend mit Commit `38eb2c170c68542870510451a6bc0f540fcad225` korrigiert: Statt eines weißen Fallback-Hintergrunds wird auf Seiten ohne `--tensor-surface` die Systemfarbe `Canvas` verwendet. Das verhindert einen offensichtlichen Hell-/Dunkelmodus-Kontrastkonflikt der Forschungsbibliothek. **Ein echter Browser-Kontrasttest steht dennoch aus.** Neuer CSS-Blob-SHA: `1642a5c0499193af4b5fdd28fc08b01d2f839c1e`.
