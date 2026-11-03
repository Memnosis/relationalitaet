# Bericht an die Website-KI — Zusammenführung `integration/soulution-shared-core-2026-11-03` → `main`

**Stand:** 2026-11-03 · **Art:** technischer Übergabe- und Analysebericht · **Geltung:** Arbeitsanweisung für die Website-KI; KEINE inhaltliche oder redaktionelle Freigabe.
**Verfasst von:** Daten-/Qualitäts-KI (zuständig für Register, Datenqualität, Versionen). Diese KI hat **keine Datei unter `docs/` verändert** und wird es auch nicht tun (siehe `UEBERGABE_ACHENSYSTEME_QUELLEN_MACHTBUCH_2026-11-03.md`, §6, DEC-WEB-01).
**Analysierte Stände:** `main` @ `86d5da5` (13:31), Zweig @ `62ee8e5` (07:37), gemeinsame Basis `3781f12` (01.11., 17:02).

## Kopfzeile nach Kommunikationsvertrag

| Feld | Inhalt |
|---|---|
| ID | KOORD-MERGE-NAV-01 |
| Datum | 2026-11-03 |
| Originalauftrag | Nils: „Ausführliche Analyse: Zweig und `main` haben parallel die Navigation derselben Seiten umgebaut; Probe-Merge ergibt Konflikte in 16 HTML-Seiten." |
| Ausgangsdateien | 16 Seiten unter `docs/` (Liste §2), `docs/assets/tensor-hierarchy.{css,js}`, `docs/assets/prompt-layers.css`, `docs/assets/site-nav.{css,js}`, `docs/assets/tensor-navigation.css`, `docs/inkubator.html` |
| Quelle/Version | siehe „Analysierte Stände" |
| Änderung/Commit | keine Website-Änderung; nur dieser Bericht |
| Test & Ergebnis | Probe-Merge (`git merge-tree`) in Wegwerf-Arbeitskopie; tokenweiser Vergleich Basis↔`main`↔Zweig für jede Seite |
| Offene Punkte | §5 (Umsetzung), §6 (Abnahmetests) |
| Entscheidung nötig? | **Ja**, zwei: DEC-NAV-01, DEC-INK-01 (§7) |
| Website-Auswirkung | hoch: globale Navigation aller Seiten |
| Zuständige KI | Website-KI |
| Nächste Übergabe | Website-KI meldet Merge-Commit, Seitendiff, Testprotokoll und offene Punkte zurück |

## 1. Kurzbefund

- Der Probe-Merge ergibt **16 Konflikte**, aber nur **17 Konfliktstellen**: je eine pro Seite, zwei in `index.html`.
- **Ursache 1, technisch:** Die Seiten sind minifiziert. `<head>`, Seitenkopf und Navigation stehen in **einer einzigen Zeile**. Git vergleicht zeilenweise, darum kollidiert jede Änderung in dieser Zeile mit jeder anderen.
- **Ursache 2, inhaltlich:** Beide Linien haben am 03.11. unabhängig voneinander **je ein eigenes, globales Navigationsskript** gebaut. Beide ersetzen denselben `<nav>` im `header.tensor-global-nav`. Sie können **nicht gleichzeitig** aktiv sein.
- Der eigentliche Inhaltsverlust droht nur an **vier Abschnitten** auf drei Seiten (§3). Alles andere lässt sich konfliktfrei zusammenführen.

**Verbot:** Konflikte NICHT pauschal mit `--ours` oder `--theirs` lösen.
- Mit `ours` (also `main`) gehen alle Zweigänderungen an 16 Seiten verloren: Fachnavigation, Brückenabschnitte, Inkubator-Verweise.
- Mit `theirs` (also dem Zweig) gehen die vier `main`-Abschnitte verloren.

## 2. Was jede Seite seit der Basis geändert hat

Die Seiten wurden tokenweise verglichen, also Tag für Tag und Text für Text.

| Seite | `main` | Zweig |
|---|---|---|
| bibliothek, geoki, glossar, harvesting, komprimierung, medien, minimal-ki, projektstand, soulution, taskkarten, tensor-einfuehrung, vernetzung-ki, visuelle-engine (13) | **nur** eingefügt: `<link rel="stylesheet" href="./assets/tensor-hierarchy.css"><script src="./assets/tensor-hierarchy.js" defer></script>` | 6–9 Änderungen, +1.400 bis +5.000 Zeichen |
| index | Einbindung wie oben **+ Abschnitt `#forschungswege`** | 6 Änderungen, +2.197 Zeichen |
| mitmachen | Einbindung wie oben **+ Abschnitt `#prompt-freigabe`** | 8 Änderungen, +5.275 Zeichen |
| tensoralgebra | Einbindung wie oben + `prompt-layers.css` **+ Abschnitte `#prompt-ebenen` und `#algebra-weiterentwickeln`** | 7 Änderungen, +1.563 Zeichen |

Typische Zweigänderungen pro Seite:
1. `<style id="ki-site-common">` im Kopf, mit den Klassen `.ki-fachnavigation` und `.ki-site-bridge`
2. umgebaute statische Hauptleiste: KI-Systeme, Bibliothek & Skills, Mitmachen ohne Klasse `tensor-nav-join`, SOULution mit `tensor-nav-soulution`
3. Einbindung von `site-nav.js` bzw. `site-nav.css`
4. Fachnavigation `<div class="ki-fachnavigation">` („Forschungswege: …")
5. Brückenabschnitt `<section class="ki-site-bridge" id="ki-forschungsfrage">` mit seitenspezifischem Text
6. auf einigen Seiten Verweise auf den Inkubator-Quellenatlas (z. B. `bibliothek.html#inkubator-quellen-bibliothek`) und auf `wissen-macht-wirklichkeit.html`

## 3. Inhalte aus `main`, die erhalten bleiben müssen

Alle vier Abschnitte stehen in `main` am Seitenende, direkt vor `</main>`. Der jeweilige Vorgängerabschnitt existiert auch im Zweig, sodass die Einfügestelle eindeutig ist.

| Seite | Abschnitt (in Reihenfolge) | Größe | Einfügen nach … |
|---|---|---:|---|
| index.html | `<section class="tensor-panel" id="forschungswege">` „Forschung verstehen, prüfen und weiterentwickeln" | 937 Z. | dem Abschnitt, der mit `SOULution-Projekt und Dokumentenregister entdecken</a></p></section>` endet; vor `</main>` |
| mitmachen.html | `<section class="tensor-panel" id="prompt-freigabe">` „Vom Forschungs-Prompt zur geprüften Mitmach-Aufgabe" | 1.029 Z. | ebenso nach `…Dokumentenregister entdecken</a></p></section>`; vor `</main>` |
| tensoralgebra.html | `<section id="prompt-ebenen">` „Eine Algebra-Frage auf drei Funktionsebenen untersuchen", **dann** `<section id="algebra-weiterentwickeln">` „Die vorhandene Tensoralgebra weiterentwickeln" | 1.990 + 2.985 Z. | im Zweig nach dem Brückenabschnitt `#ki-forschungsfrage` („Leistungsspektrum statt bloßer Tensorzahl"), vor `</main>` |

Zusätzlich gilt für `tensoralgebra.html`:
- `<link rel="stylesheet" href="./assets/prompt-layers.css">` im `<head>` behalten.
- Die beiden Abschnitte sind Ziel bestehender Links, darum dürfen ihre IDs nicht geändert werden:
  - `tensor-hierarchy.js` verweist auf `tensoralgebra.html#algebra-weiterentwickeln`.
  - `index.html` und `mitmachen.html` verweisen auf `inkubator.html` bzw. die Algebra-Abschnitte.

**Prüfvorschrift:** Nach dem Merge müssen die IDs `forschungswege`, `prompt-freigabe`, `prompt-ebenen` und `algebra-weiterentwickeln` je genau einmal vorkommen. Ihr Text muss zeichengleich mit `main` @ `86d5da5` sein.

## 4. Die zwei echten Kollisionen

### 4.1 Zwei konkurrierende Navigationsskripte

| | `main`: `tensor-hierarchy.js` + `.css` | Zweig: `site-nav.js` + `site-nav.css` (+ `tensor-navigation.css`) |
|---|---|---|
| Menü | Start · Forschung · Projekte · **Inkubator** · Publikationen · Mitmachen · SOULution (7) | Start · KI & Forschung · Wissen & Werkzeuge · SOULution & Publikationen · Mitmachen (5) |
| CSS-Klassen | `tensor-hierarchical-nav`, `tensor-nav-group`, `tensor-nav-menu` | `site-navigation` (`data-version="v2"`), `site-nav-group`, `site-menu-panel` |
| Seiten mit Skript | 17 | 27 |
| Linkziele, die im jeweils anderen Stand fehlen | `inkubator.html` | `codebuch`, `ki-systeme`, `ki-kernforschung`, `promptbibliothek`, `soulution-ki-kreativrechte`, `soulution-schroedingers-inkubator`, `soulution-weltwissen-dividende` |
| Fallback ohne JS | statischer `<nav>` bleibt | statischer `<nav>` bleibt; `.ki-fachnavigation` wird per JS ausgeblendet |

Werden beide geladen, ersetzt das zweite Skript die Navigation des ersten. Das ist nicht deterministisch gewollt. Es braucht **genau ein** globales Navigationsskript.

### 4.2 Zwei verschiedene „Inkubatoren"

- `main`: **`docs/inkubator.html` – „Forschungsinkubator"**. Abschnitte: Kompetenzfamilien als Einstieg · Wie können Menschen und ihre KI mitforschen? · Prompt-Veröffentlichung und Prüfung · Verbindungen im Gesamtprojekt.
- Zweig: **„Schrödinger’s Inkubator"** (`soulution-schroedingers-inkubator.html`, `soulution-inkubator-quellen.html`). Inhalt: digitale Souveränität, offene Software und ein Quellenatlas.

Inhaltlich sind das zwei verschiedene Objekte mit demselben Wort. Im Zweig verlinkt **keine** Seite auf `inkubator.html`. Wird nur die Zweig-Navigation übernommen, ist der Forschungsinkubator verwaist.

### 4.3 Nebenbefunde, beim Merge mit beheben

- Im Zweig laden `medien.html` und `promptbibliothek.html` **kein** Navigationsskript.
- In `main` laden `impressum.html`, `interoperabilitaet.html`, `quellen-und-uebergabe.html` und `tensor-paper.html` keins. Im Zweig sind diese vier bereits angeschlossen.
- Nach dem Merge wäre `inkubator.html` die einzige Seite mit `tensor-hierarchy.js`. Sie zeigt dann ein abweichendes Menü.

## 5. Empfohlene Umsetzung (vorbehaltlich DEC-NAV-01 / DEC-INK-01)

1. Arbeitszweig von aktuellem `main` anlegen, z. B. `website/merge-soulution-shared-core`, und den Zweig hineinmergen (kein Rebase: 160 Commits, Historie erhalten).
2. **Für die 16 Konfliktseiten:**
   - als Grundlage die Fassung des Zweigs nehmen
   - die `main`-Einbindung `tensor-hierarchy.css/js` **nicht** übernehmen
   - die vier Abschnitte aus §3 an den genannten Stellen wieder einsetzen, für `tensoralgebra` inklusive `prompt-layers.css`
   - `index.html` hat zwei Konfliktstellen; die zweite enthält `#forschungswege`
3. **Ein Navigationssystem:**
   - `site-nav.js` als einziges globales Skript verwenden
   - den Forschungsinkubator gemäß DEC-INK-01 ins Menü aufnehmen
   - `tensor-hierarchy.{js,css}` aus allen Seiten entfernen; die Dateien vorerst als archivierte Assets behalten, nicht löschen (No-Loss)
4. `inkubator.html`, `medien.html` und `promptbibliothek.html` an `site-nav.js`/`site-nav.css` anschließen und `inkubator.html` mit dem gemeinsamen Kopf versehen.
5. **Nicht anfassen:** die nur-`main`-Dateien unter `forschung/register/`, `forschung/website/`, `forschung/koordination/` und die rund 60 nur-Zweig-Dateien (Register, Piloten, Skills, Prompts, Workflow). Sie werden konfliktfrei übernommen.
6. **Empfehlung für die Zukunft:**
   - HTML nicht weiter minifiziert in einer Zeile pflegen, sondern zumindest `<head>`, `<header>`, jede `<section>` und `<footer>` auf eigene Zeilen
   - die globale Navigation **nur** im Skript pflegen, nicht zusätzlich in 27 statischen Kopien
   - parallele KIs arbeiten auf kurzlebigen Zweigen und führen spätestens täglich zusammen

## 6. Abnahmetests (vor Merge in `main` zurückmelden)

| Test | Kriterium |
|---|---|
| Konfliktmarker | `grep -rn '^<<<<<<<\|^=======$\|^>>>>>>>' docs/` liefert nichts |
| Erhalt `main`-Inhalte | die vier IDs aus §3 je genau 1×, Text identisch mit `main` @ `86d5da5` |
| Erhalt Zweig-Inhalte | `ki-forschungsfrage` und `ki-fachnavigation` auf allen 16 Seiten wie im Zweig @ `62ee8e5` |
| Ein Skript | keine Seite lädt `tensor-hierarchy.js`; alle Seiten unter `docs/` laden `site-nav.js` (Ausnahmen begründen, z. B. Weiterleitungsseiten) |
| Links | alle lokalen `href` in `docs/**/*.html` und in `site-nav.js` zeigen auf vorhandene Dateien und Anker; `inkubator.html` ist aus dem Menü erreichbar |
| Browser | Desktop und 390 px: Menü öffnet/schließt, nur eine Gruppe offen, Escape schließt, Klick außerhalb schließt, Tastatur-Fokus sichtbar, `aria-current` korrekt |
| Ohne JS | statischer Fallback-`<nav>` vorhanden und benutzbar |
| CI | `python forschung/soulution/digitale-souveraenitaet/sync_registers.py --check` grün; vorhandener `forschung/website/website_observer.py` ohne neue Fehler |

## 7. Offene Entscheidungen für Nils

| ID | Frage | Vorläufige Empfehlung |
|---|---|---|
| DEC-NAV-01 | Welche Menüstruktur gilt: 5 Punkte (Zweig) oder 7 Punkte (`main`)? | 5-Punkte-Struktur des Zweigs, ergänzt um „Inkubator" (als Hauptpunkt oder unter „Mitmachen"). Sie deckt alle 27 Seiten ab. |
| DEC-INK-01 | Wie heißen und unterscheiden sich die zwei Inkubatoren? | Beide behalten und eindeutig benennen: „Forschungsinkubator" (Mitforschen, Prompt-Freigabe) und „Schrödinger’s Inkubator · Digitale Souveränität" (Software/Quellenatlas), gegenseitig verlinkt. |

Bis zur Entscheidung darf die Website-KI die technische Zusammenführung vorbereiten, aber nicht nach `main` übernehmen.

## 8. Zuständigkeitsabgrenzung ab jetzt

- **Website-KI:** `docs/**/*.html`, `docs/assets/**`, Navigation, Dashboard-Darstellung.
- **Daten-/Qualitäts-KI:** `forschung/register/**`, Datenschemas, Versions- und Herkunftsnachweise (SHA-256, Quelle, Version), Validatoren, Dubletten- und Referenzprüfung, Prüfprotokolle.
- **Gemeinsame Schnittstelle `docs/data/*.json`:** Diese Dateien sollen künftig aus den Registern unter `forschung/` erzeugt und nicht von Hand gepflegt werden. Bis ein Generator existiert, ändert jede KI dort nur nach Rückmeldung an die andere. Schema-Änderungen werden in `forschung/koordination/` angekündigt.
