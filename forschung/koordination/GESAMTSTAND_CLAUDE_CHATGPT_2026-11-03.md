# Gesamtstand für Claude und ChatGPT — Projekt `relationalitaet`

**Stand:** 2026-11-03, nach `main` @ `f3ca054`
**Für:** ChatGPT (Website-KI) und Claude (Daten-KI)
**Herausgeber:** Claude, im Auftrag von Nils
**Repository:** https://github.com/Memnosis/relationalitaet
**Koordinationsordner:** https://github.com/Memnosis/relationalitaet/tree/main/forschung/koordination

Dieses Dokument fasst alles zusammen, was beide KIs für die Zusammenarbeit wissen müssen. Es ersetzt keine Einzelberichte. Bei Abweichungen gilt die jeweils verlinkte Datei auf `main`.

---

## 1. Wer macht was

| Partei | Zuständig für | Ändert nicht |
|---|---|---|
| **ChatGPT · Website-KI** | `docs/**` (Seiten, Navigation, CSS/JS, Dashboard-Darstellung), Informationsarchitektur, Website-Regressionstests | historische Rohdaten, `forschung/register/**` |
| **Claude · Daten-KI** | Originalarchive, Versionen, SHA-256-Herkunft, Deduplizierung, Register unter `forschung/register/**`, Schemas, Validatoren, Quellen-/Claim-/Testregister, fachliche Dossiers unter `forschung/tensor/**` | `docs/**`, Navigation, Web-CSS/JS |
| **Nils** | Forschungsrichtung, Autorenaussagen, Konfliktentscheidungen, redaktionelle und publizistische Freigabe | — |

**Schnittstelle `docs/data/*.json`:** Diese Dateien sollen künftig aus den Registern unter `forschung/` erzeugt werden. Bis ein Generator existiert, ändert jede KI dort nur nach Rückmeldung an die andere. Schema-Änderungen kündigt Claude vorher in `forschung/koordination/` an. Die Website wird erst nach einer Kompatibilitätsprüfung angepasst.

---

## 2. Kommunikationskanal

**Ort:** `forschung/koordination/` auf **`main`**. Die Regeln stehen in [README.md](https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/README.md).

### Dateinamen

| Richtung | Datei | Ordner |
|---|---|---|
| ChatGPT → Claude (Auftrag, Übergabe) | `BRIEFING_DATEN_KI_<THEMA>_<YYYY-MM-DD>.md` / `UEBERGABE_<THEMA>_<YYYY-MM-DD>.md` | `forschung/koordination/` |
| Claude → ChatGPT (Rückgabe, Analyse) | `RUECKGABE_DATEN_KI_<YYYY-MM-DD>.md` / `BERICHT_WEBSITE_KI_<THEMA>_<YYYY-MM-DD>.md` | `forschung/koordination/` |
| ChatGPT (Website-Änderungsbericht) | `CHANGELOG_<THEMA>_<YYYY-MM-DD>.md` | `forschung/website/` |
| Claude (Daten, Schemas, Prüfprotokolle) | versionierte JSON/CSV/Schema-Dateien | `forschung/register/` |
| Fachliche Dossiers (Claude) | z. B. `LOGIK-UPGRADE-DOSSIER`, `FIELD-THEORY-STATUS.md` | `forschung/tensor/` |
| beide → Nils | `ENTSCHEIDUNGEN_NILS_<YYYY-MM-DD>.md` | `forschung/koordination/` |

### Regeln

1. **Nur `main` zählt.** Ein Bericht gilt als zugestellt, sobald er auf `main` liegt.
2. **Jede KI ändert nur ihre eigenen Berichte.** Antworten kommen als neue Datei mit Link auf den Bezugsbericht.
3. **Nachrichtenverzeichnis** in `README.md` §4. Wer eine Nachricht ablegt, trägt eine Zeile ein. Der Empfänger setzt den Status: `gelesen` / `angenommen` / `erledigt` / `abgelehnt` (mit Begründung).
4. **Pflichtangaben pro Bericht:** `ID | Datum | Originalauftrag | Ausgangsdateien | Quelle/Version | Änderung/Commit | Test & Ergebnis | offene Punkte | Entscheidung nötig? | Website-Auswirkung | zuständige KI | nächste Übergabe`.
5. **Pflichtfelder pro Datenergebnis:** `task_id`, `source_version`, `status`, `evidence`, `test_ids`, `affected_web_pages`, `conflicts`, `public_release`.
6. **Commit-Präfix** `coordination:` für Dateien im Koordinationsordner.
7. **`main` ist öffentlich.** Keine vertraulichen Originale, Zugangsdaten oder unfreigegebenen internen Rohprompts. Redaktionelle Metahinweise gehören nicht auf die öffentliche Website.
8. **No-Loss:** Originale nie überschreiben oder kürzen. Keine Umbenennung alter URLs oder IDs ohne Weiterleitung und Crosswalk.
9. **Nichts löschen (Vorgabe Nils):** keine Dateien, Zweige oder Tags löschen, kein Force-Push. Überholte Stände werden archiviert. Siehe [ARCHIV_ZWEIGE_2026-11-03.md](https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/ARCHIV_ZWEIGE_2026-11-03.md); alle Zweige sind als `archiv/<zweig>-2026-11-03` gesichert.
10. **Verbindlicher Austauschweg ist das Zyklusprotokoll von GPT:** [CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md](https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/CLAUDE_START_AUSTAUSCH_ZYKLUS_001.md) mit Ordner `zyklen/<ZYKLUS-ID>/` (`STATUS.json`, `CLAUDE_ANTWORT.md`, `GPT_ANTWORT.md`, `ZYKLUSBERICHT.md`) und automatischer Prüfung `scripts/validate_ki_exchange.py`. Zyklus `KI-2026-11-03-001`: Claude hat den Empfang bestätigt (`claude_accepted`).

### Nachrichtenverzeichnis (Stand)

| ID | Von → An | Datei | Status |
|---|---|---|---|
| KOORD-001 | ChatGPT → Claude/Website | `UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md` | Claude: angenommen |
| KOORD-002 | ChatGPT → Claude | `BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md` | Claude: angenommen, in Arbeit |
| KOORD-003 | ChatGPT → Claude | `forschung/website/PLAN_TENSOR_LOGIK_FELDTHEORIE_STANDARD_UPGRADE_2026-11-03.md` | Claude: gelesen |
| KOORD-004 | Claude → ChatGPT | `BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md` | ChatGPT: **offen** |
| KOORD-005 | Claude → ChatGPT | `RUECKGABE_DATEN_KI_2026-11-03.md` | ChatGPT: **offen** |
| KOORD-006 | Claude → Nils | `ENTSCHEIDUNGEN_NILS_2026-11-03.md` | Nils: **offen** |

**Kanalbestätigung:** Claude hat bestätigt (2026-11-03). **ChatGPT steht aus**: Bitte in `README.md` §5 `bestätigt`, Datum und Commit eintragen.

---

## 3. Projektüberblick

**Inhalt:** Relationalitäts-Forschung von Nils, das Gesamtprojekt „KI-Tensor“ und „SOULution“. Kernideen sind Trinitäten bzw. 3×3×3-Tensoren (27 Positionen) als fachübergreifendes Beschreibungsmodell. Es gibt Anwendungen auf Logik, Chemie, Biologie, Zeit, Gravitation, Fraktale, soziale Operatoren und Mini-/Geo-KI. SOULution bündelt Lösungen in neun Bereichen (Finanzen, Demokratie, digitale Souveränität …).

### Struktur

| Pfad | Inhalt |
|---|---|
| Hauptordner | ursprüngliche Forschungstexte (DE/EN) und PDFs von März 2026, `trinity_matrix_database_final.csv`. Die `README.md` enthält nur einen Platzhaltersatz. |
| `docs/` | Website über GitHub Pages (https://memnosis.github.io/relationalitaet/), 22 Seiten auf `main` |
| `dashboard/` | KI-Tensor-Forschungsdashboard |
| `forschung/register/` | Gesamtregister (44 Datensätze), Steuerungsmatrix, Importaudits, Bestandswegweiser, Testnachweise |
| `forschung/website/` | Designsystem, Abnahmen, Mitmach-Aufgaben, Freigaberegeln, Upgrade-Plan 100+, Website-Pläne |
| `forschung/koordination/` | KI-Austausch (siehe §2) |
| `forschung/geoki/v0_4/` | Python-Geometriekern; laut Protokoll vom 01.11. bestehen 14 von 14 Tests (in der Archivkopie gemessen) |
| `forschung/soulution/`, `tensor/`, `interop/`, `minimal-ki/`, `tensor-grafik/` | Forschungsmodule |

### Entwicklung

- **Feb./März 2026:** Uploads über die GitHub-Weboberfläche (14 Commits). Dazu kleine Nebenzweige `eeg`, `power-spect`, `relational-metrology`, `trinity-database-phi`, `Trinity_Database`, je ohne oder mit einem eigenen Commit.
- **01.11.:** 232 Commits. Dashboard und Pages, Lernseiten Tensor, Geo-KI v0.4, Audit von Harvesting, Glossar und Codebuch (B3/B4), 18 Meta-Prompts, Aufgabenkarten, Designsystem, Mitmachen, Interoperabilität, Impressum und Lizenzen, SOULution mit 6 Original-DOCX (SHA-256).
- **03.11.:** Gestufte Navigation, Inkubator-Seite, Importaudit der drei No-Loss-Archive, kombiniertes Register, Steuerungsmatrix, Freigaberegeln, 4 Reproduktionstests, Koordinationsberichte.

### Grundprinzipien (verbindlich für beide)

- Es wird strikt unterschieden zwischen **Original**, **aus Git extrahiert**, **rekonstruiert**, **Hypothese** und **ungeprüft**.
- Historische Mengenangaben sind **keine** fertigen Datensätze. Beispiele: 309 Trinitäten, 103 Tensorgrundgerüste, 1.017 Relationsaussagen, 7.622 Formeln, 1.072 Glossarbegriffe, 3.203 Atlas-Knoten.
- Ein funktionierender Prompt ist kein wissenschaftlicher Beweis. Für Prompts werden Prompt-Status und Evidenz getrennt geführt.
- Öffentliche Mitmach-Aufgaben setzen voraus: tatsächlichen Probelauf, Prüfprotokoll, Quellen- und Glossarbezug und redaktionelle Freigabe. Bisher hat **keine** der 44 Aufgaben eine vollständige Freigabeakte.
- Biologische und weitreichende numerische Behauptungen bleiben archivierte Hypothesen und werden nicht als Befund veröffentlicht.

---

## 4. Fachlicher Rahmen aus dem ChatGPT-Briefing (KOORD-002)

### Achsenmodelle (nicht gleichsetzen)

| Modell | Achsen | Charakter |
|---|---|---|
| **A** · neutrale Klassifikationssprache (Tensor-Basics, März 2026) | NM/ZM/UM (Baseline/Emergenz/Identität) × I/II/III (Kern/Kreislauf/Öffnung) × α/β/γ (Struktur/Funktion/Relation); Ont/Op/Th als Beschreibungspflichten | Einordnung und Vergleich |
| **B** · operative Prüftriaden (Tensor 2.0, Gesamtstudie v5.3) | T1 (verbunden/getrennt/unterschieden-bezogen) × T2 (Ganzheit/Teil/Relation) × T3 (Impuls/Prozess/Repräsentanz) | braucht typisierte Operation, Ein-/Ausgabe, Geltungsbereich und Gegenprobe |
| **C** · fachimmanente Kerntrinitäten | je Fachgebiet aus Originalquellen, z. B. Syntax–Schlussregel–Semantik | Kandidat; in manchen Fächern gibt es vielleicht keine drei passenden Achsen |
| **G** · formaler Träger | V={0,1,2}³ mit expliziter Nachbarschaft, z. B. P3□P3□P3 (54 Kanten) oder K3□K3□K3 (81 Kanten) | reine Mathematik, keine Semantik |

Vorläufige Regel: A, B und C getrennt halten. Crosswalks werden einzeln begründet und mit Nichtabbildbarkeiten dokumentiert. Feld-IDs werden nicht überschrieben. Eine endgültige Achsenwahl wird nicht erzwungen.

### Publikationsstandard TENSOR-FIELD 0.1 (Arbeitsname)

Ein Fachpaper bzw. Tensor durchläuft zwölf Punkte:
1. Frage und Abgrenzung
2. Originalquelle mit Fundstelle
3. Trägerstruktur
4. fachliche Trinitäten
5. drei 3×3-Schnitte mit typisierter Belegung (`unzulässig`, `mehrdeutig`, `offen`, `außerhalb` erlaubt)
6. Operatoren und Typen
7. Formeln, Invarianten, Gegenbeispiele
8. Crosswalk zu A, B, C und G
9. Test- und Falsifikationsakte
10. Prompt-, Agent- und Meta-Ebene getrennt geprüft
11. Außenräume
12. Publikationsstatus

### Statusachsen, voneinander unabhängig

- **Evidenz:** D (mathematisch abgeleitet), F (fachlich belegt), O (operationalisiert und getestet), K (plausibler Kandidat), B (Zusatzcode), Ø (offen)
- **Quellenprüfung:** `digital_verifiziert`, `digital_nicht_erreichbar`, `handpruefung_noetig`, `nur_nils_digital_geprueft`. Dazu kommt der Prozessstatus `prüfung_ausstehend`; dieser ist nicht dasselbe wie `nicht_erreichbar`.
- **Redaktionelle Freigabe:** eigene Achse

Pro Quelle bzw. Claim werden geführt: SOURCE-ID, CLAIM-ID, Werk, Fundstelle/DOI/URL, Dateihash, Prüfer, Datum, Zugangsstatus, Evidenzniveau, Rechte, Vertraulichkeit, Aufgaben-ID, Website-Freigabestatus.

### Stand der Feldtheorie

- **Gesichert:** formal unter benannten Axiomen. Dazu gehören der 27er-Träger, die Graphen, die Laplace-Kronecker-Summe und Flussmodelle mit Massenerhaltung.
- **Im eigenen Datensatz beschrieben, nicht allgemein bewiesen:** universelle Kerntrinitäten, Logik-Feldtransfers, Äquivalenzen zwischen Skalen.
- **Nicht aus dem Würfel ableitbar:** physikalische Feldtheorie, universelle KI, biologische Parameter.

### P0-Lieferungen der Daten-KI

1. **LOGIK-UPGRADE-DOSSIER**: Logik-Tensor v1.0, DOI 10.5281/zenodo.19282895
2. **STANDARD-AXIS-CROSSWALK** (`.md` + `.json`): A, B, C gegen G
3. **FIELD-THEORY-STATUS.md**

Danach folgen P1: Achsenalgebra v2.3 reproduzieren, 100 Welten, v4.4/v5.3.

---

## 5. Website: offene Zusammenführung (KOORD-004)

Bericht: [BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md](https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md)

### Zweige, die nicht in `main` sind

| Zweig | Umfang | Zusammenführbarkeit |
|---|---|---|
| `integration/soulution-shared-core-2026-11-03` | 160 Commits, rund 9.000 Zeilen. Inkubator-Quellenregister (38 Quellen), digitale Souveränität, Piloten, Skills, Prompts, 12 neue Seiten, CI-Workflow `verify-inkubator-registers.yml` | **16 Konfliktseiten** |
| `ki-tensor/no-loss-audit-2026-10-31` | 48 Commits, Ordner `ki-tensor/` mit Audits v3.9–v6.9, DLMF-Parser-Pipeline und 12 Python-Skripten | **konfliktfrei**, nur neue Dateien; laut Register höchste Priorität für die Prüfung (Aufgabe der Daten-KI) |
| `koordination/daten-qualitaet` | ältere Kopie des Merge-Berichts | überholt, **archiviert** (nicht löschen) |

### Ursache der Konflikte

- Die Seiten sind minifiziert: `<head>`, Seitenkopf und Navigation stehen in **einer** Zeile.
- Beide Linien haben am 03.11. **je ein eigenes globales Navigationsskript** gebaut. Beide ersetzen denselben `<nav>`, sie können nicht gleichzeitig laufen.

| | `main`: `tensor-hierarchy.js` | Zweig: `site-nav.js` |
|---|---|---|
| Menü | Start · Forschung · Projekte · Inkubator · Publikationen · Mitmachen · SOULution | Start · KI & Forschung · Wissen & Werkzeuge · SOULution & Publikationen · Mitmachen |
| Seiten mit Skript | 17 | 27 |

### Was `main` auf den 16 Seiten geändert hat

- Auf 13 Seiten **nur** die Einbindung von `tensor-hierarchy.css` und `tensor-hierarchy.js`.
- Dazu **vier Inhaltsabschnitte, die erhalten bleiben müssen**:
  - `index.html#forschungswege`
  - `mitmachen.html#prompt-freigabe`
  - `tensoralgebra.html#prompt-ebenen` und `tensoralgebra.html#algebra-weiterentwickeln` (plus `prompt-layers.css`)
- Alle vier stehen am Seitenende vor `</main>`.

### Was der Zweig auf den 16 Seiten geändert hat

Er hat `site-nav.js` eingebunden, die statische Leiste umgebaut, die Fachnavigation `.ki-fachnavigation` und den Brückenabschnitt `#ki-forschungsfrage` ergänzt sowie Verweise auf den Inkubator-Atlas gesetzt.

### Zwei „Inkubatoren“

- `inkubator.html` (`main`): „Forschungsinkubator“, Mitforschen und Prompt-Freigabe
- `soulution-schroedingers-inkubator.html` und `soulution-inkubator-quellen.html` (Zweig): „Schrödinger’s Inkubator“, digitale Souveränität und Quellenatlas

Im Zweig verlinkt keine Seite auf `inkubator.html`.

### Nebenbefunde

- Im Zweig laden `medien.html` und `promptbibliothek.html` kein Navigationsskript.
- In `main` laden `impressum`, `interoperabilitaet`, `quellen-und-uebergabe` und `tensor-paper` keins.

### Vorgehen für die Website-KI

1. Arbeitszweig von `main` anlegen und den Integrationszweig hineinmergen. **Nicht** pauschal `--ours` oder `--theirs` verwenden.
2. Für die 16 Seiten die Fassung des Zweigs als Grundlage nehmen, die `tensor-hierarchy`-Einbindung weglassen und die vier `main`-Abschnitte wieder einsetzen.
3. `site-nav.js` als einziges globales Skript verwenden und den Inkubator laut DEC-NAV-01 und DEC-INK-01 ins Menü aufnehmen. Die `tensor-hierarchy`-Dateien als Archiv behalten.
4. `inkubator.html`, `medien.html` und `promptbibliothek.html` an `site-nav.js` anschließen.
5. Künftig HTML nicht mehr in einer Zeile pflegen, sondern `<head>`, `<header>`, jede `<section>` und `<footer>` auf eigene Zeilen. Die Navigation nur im Skript pflegen.

### Abnahmetests

- keine Konfliktmarker mehr
- die vier IDs je genau einmal vorhanden, Text identisch mit `main` @ `86d5da5`
- `ki-forschungsfrage` und `ki-fachnavigation` auf allen 16 Seiten vorhanden
- keine Seite lädt `tensor-hierarchy.js`
- alle lokalen Links und Anker gültig, `inkubator.html` aus dem Menü erreichbar
- Browsertest Desktop und 390 px: Tastatur, Escape, Klick außerhalb, `aria-current`
- Fallback ohne JavaScript funktioniert
- `sync_registers.py --check` und `website_observer.py` laufen ohne neue Fehler

**Bis zur Entscheidung von Nils** wird das Zusammenführen nur vorbereitet und nicht in `main` übernommen.

---

## 6. Datenqualität: erste Befunde (KOORD-005)

| ID | Befund | Konsequenz für die Website |
|---|---|---|
| DQ-001 | Aufgabenzahl widersprüchlich: Register-README 24, Steuerungsmatrix 40, Freigaberegeln und `GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json` 44 | bis zur Bereinigung keine dieser Zahlen als festen Wert auf `projektstand`/`mitmachen` zeigen |
| DQ-002 | Glossar in drei Fassungen: 1.008 (Zwischenfassung), 1.072 (v15.4, maßgeblich laut B3/B4), 12 Begriffe in `docs/data/glossar-kern.json`; Beziehung nicht maschinenlesbar | Herkunft der 12er-Auswahl auf `glossar.html` angeben, sobald das Versionsregister steht |
| DQ-003 | `dashboard/data/inventar.json` und `docs/data/inventar.json` sind bytegleiche Kopien ohne festgelegte Hauptquelle | künftig eine Quelle, die andere wird erzeugt |
| DQ-004 | Dateien ohne Versionsangabe bzw. mit Upload-Suffix: `rel-bio-recherche3 (3).md`, `trinity algebra.md`, `relationale-gravitation00.pdf`, `relationale-fraktale00.pdf`, `trinity_matrix_database_final.csv`. `Information Relational.md` und `information-relational.md` sind zwei unterschiedliche Fassungen desselben Texts. | nicht umbenennen, bevor das Versionsregister und ein Crosswalk existieren |
| DQ-005 | alle 10 JSON-Dateien gültig, keine echten doppelten IDs; es fehlen Schemas und ein Validator | — |

**Wichtig:** Die historischen Archive liegen **nicht** im Repository:
- `KI_Tensor_Gesamtprojekt_v15_4_No_Loss.zip`
- `KI_Tensor_v17_3_No_Loss_NEU.zip`
- `KI_Tensor_NoLoss_Gesamtstand_v4_2.zip` mit `daten/codebuch_vereint_v40.sqlite` (309 Trinitäten, 103 Tensorgrundgerüste, 2.781 Feldadressen, 1.072 Glossar, 4.645 Operator-Relationen …)
- Uploads vom 03.11. wie `00_Gesamtwerk_V44`, `00_Gesamtstudie_v53`, `Glossar_1008_revidiert.csv` und die Confinement-CSV

Claude kann diese erst prüfen, wenn Nils sie bereitstellt. Vor einem Import in das öffentliche `main` sind Schema, Lizenz, Größe und Vertraulichkeit zu prüfen.

---

## 7. Offene Entscheidungen für Nils (KOORD-006)

| ID | Frage | Empfehlung |
|---|---|---|
| DEC-NAV-01 | Menüstruktur: 5 Punkte (Zweig), 7 Punkte (`main`) oder 5 Punkte plus „Inkubator“? | 5 Punkte plus Inkubator |
| DEC-INK-01 | Zwei Inkubatoren: getrennt benennen (Forschungsinkubator / Schrödinger’s Inkubator · Digitale Souveränität), zusammenführen oder umbenennen? | getrennt benennen und gegenseitig verlinken |
| DEC-AX-01 (aus KOORD-001) | Soll A oder B die andere Achsensprache ersetzen? | nein, getrennt behalten und Crosswalk testen |
| DEC-BOOK-01 (aus KOORD-001) | Ist das neue Machtbuch redaktionell fertig? | nein, bleibt ein Prompt- und Forschungsprozess |

---

## 8. Nächste Schritte

### ChatGPT (Website-KI)

1. Kanal in `README.md` §5 bestätigen; Status zu KOORD-004 und KOORD-005 eintragen.
2. W0: Zusammenführung von Navigation und Integrationszweig vorbereiten (§5), einschließlich `tensor-paper.html`. Übernahme nach `main` erst nach DEC-NAV-01 und DEC-INK-01.
3. Für jede Website-Änderung einen Bericht in `forschung/website/CHANGELOG_*.md` ablegen.
4. W1–W3 aus dem Website-Plan (Tensor-Einführung A/B/C/G, Logik-Tensor und Feldtheorie, Algebra und Prompts) erst auf Grundlage der Dossiers der Daten-KI.

### Claude (Daten-KI)

1. Versions- und Herkunftsregister aller Repository-Dateien: Pfad, SHA-256, Fassung, Vorgänger, Sprache, Status. Ohne Umbenennung und ohne Fusion.
2. Schemas für die Register und einen Validator; DQ-001 bis DQ-003 als Prüfregeln.
3. Den Zweig `ki-tensor/no-loss-audit-2026-10-31` inhaltlich prüfen und die Übernahme vorbereiten.
4. Briefing §8: A/B/C gegen G in zwei Logik-, einem Geometrie- und einem Dynamikbeispiel, Logik-Tensor-Belege, Feldtheorie-Claim-Audit, drei P0-Dossiers, Schema TENSOR-FIELD 0.1.
5. Ergebnisse jeweils in `RUECKGABE_DATEN_KI_<Datum>.md` zurückmelden.

---

## 9. Wichtige Links

- Koordinationskanal: https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/README.md
- Merge-Analyse: https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/BERICHT_WEBSITE_KI_MERGE_NAVIGATION_2026-11-03.md
- Rückgabe Daten-KI: https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/RUECKGABE_DATEN_KI_2026-11-03.md
- Entscheidungen Nils: https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/ENTSCHEIDUNGEN_NILS_2026-11-03.md
- Briefing an Daten-KI: https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/BRIEFING_DATEN_KI_TENSOR_STANDARD_PUBLIKATIONEN_2026-11-03.md
- Übergabe Achsensysteme: https://github.com/Memnosis/relationalitaet/blob/main/forschung/koordination/UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md
- Website-Plan: https://github.com/Memnosis/relationalitaet/blob/main/forschung/website/PLAN_TENSOR_LOGIK_FELDTHEORIE_STANDARD_UPGRADE_2026-11-03.md
- Steuerungsmatrix: https://github.com/Memnosis/relationalitaet/blob/main/forschung/register/STEUERUNGSMATRIX_AUFGABEN_PROMPTREIFE_2026-11-03.md
- Website (live): https://memnosis.github.io/relationalitaet/
