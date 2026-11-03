# Tiefenanalyse · Zweig `ki-tensor/no-loss-audit-2026-10-31`

**Owner:** Claude · **Schritt:** S8 · **Auftrag:** Nils, DEC-KT-01 „genauer analysieren“ · **Stand:** 2026-11-03 · **Geprüft:** `cf0bbe1`
**Ergänzt:** [`ZWEIG_KI_TENSOR_AUDIT_V0_1.md`](ZWEIG_KI_TENSOR_AUDIT_V0_1.md) (Umfang, Reproduktion der Programme)

## E1 · Kurz erklärt

Am 31.10. wurde in drei Stunden eine Kette von 18 Arbeitsständen (v3.9 bis v6.9) erzeugt.
- **Inhalt:** Bestände zählen und abgleichen, 300 Formeln aus der DLMF-Sammlung maschinell lesen, Formeln mit Achsen verknüpfen, Fachkarten und Thesenentwürfe erzeugen.
- **Ergebnis über alle Stände:** **0 neu bewiesene Trinitäten, 0 neu bewiesene Tensoren**. Bestätigt sind nur Lehrbuch-Identitäten und einige Umrechnungen.
- **Zahlen:** Alle prüfbaren Zahlen passen rechnerisch zusammen (16 von 16 Ketten).
- **Hauptwert des Zweigs:** Er erklärt viele Zahlen auf `main` und dokumentiert ehrlich, was nicht geklappt hat.

## E2 · Ergebnisse

### Die Arbeitskette

| Phase | Stände | Was gemacht wurde | Ergebnis laut Bericht |
|---|---|---|---|
| Bestand | v3.9, v4.1–v4.3 | 45 ZIP-Archive inventarisiert (1.327 Dateien); Trinitäten, Glossar und Achsen über Primärschlüssel abgeglichen | Abgleiche exakt (z. B. 297/297 Achsentexte identisch) |
| Prüfung | v4.4–v4.6 | 9 Relationsregeln und 8 Rückrechnungen (REV-01 bis 08) mit Definitionsbereich | formal unter Voraussetzungen; ausdrücklich keine extern bestätigten Modelle |
| Formel-Parser | v5.2–v5.9 | dieselben 300 DLMF-Formeln in 7 Durchgängen | v5.2: 2 symbolische Gleichheiten von 300. Danach keine Steigerung der Erfolgsquote, nur bessere Fehlerklassifikation (v5.5, v5.6, v5.8: „0 zusätzliche Parses“) |
| Verknüpfung | v6.0–v6.6 | Formeln nach Familien sortiert, 15.653 heuristische Links, Relations-Compiler, 7 DLMF-Identitäten bewiesen | 7 Identitäten unter Annahmen; „0 neu validierte Trinitäten/Tensoren“ |
| Verdichtung | v6.7–v6.9 | 100 Fachkarten, **100 Thesenentwürfe**, 100 Operationalisierungsentwürfe, 18 Skill-Spezifikationen | alles als Entwurf markiert (`DRAFT_NOT_VERIFIED`) |

### Zahlenprüfung (16/16 rechnerisch stimmig)

Auszug:
- 103 Gerüste × 3 = **309** Trinitäten
- 309 − 297 = 12 = 4 Gerüste × 3 (CORE-T1 bis T3, FACH-F001 fehlen im Review, sind aber nicht gelöscht)
- 103 × 27 = **2.781** Feldadressen (Register auf `main`); 107 × 27 = **2.889** (inklusive 4 Chemie-Trios)
- 7.622 + 898 Dubletten = **8.520**
- 309 + 12 + 9 + 12 + 675 = **1.017** Relationsakten
- 342 + 132 = **474** Aussagenakten
- Alle Parser-Klassifikationen summieren sich auf 300.

### Was das für die offenen Fragen bedeutet

1. **Register-Zahlen auf `main` (DQ-001/002):**
   - Die Zahlen 309/297, 2.781/2.889 und 1.008/1.072 sind **verschiedene Stände bzw. Umfänge, keine Fehler**. Die Erklärung steht hier; sie wird in die Register-Metadaten übernommen.
   - Glossar: v11.5 hat 1.008 Einträge, v15.4 hat 1.072.
2. **Thesen (GPT C-P0-03, `docs/thesen.html`):** Die **100 Thesenentwürfe** aus v6.9 wurden maschinell aus Fachkarten erzeugt. Sie sind **keine Originalthesen** von Nils und dürfen nicht mit ihnen vermischt werden. Das Theseninventar (P-NEU-05) trennt beide Herkünfte.
3. **„100“ ist mehrdeutig:** 100 Fachkarten, 100 Thesenentwürfe, 100 Welten, 100 Logik-Begriffe (davon 34 im Original vorhanden). Das sind vier verschiedene Mengen. Empfehlung: Die Zahl 100 öffentlich nur mit Bezugsobjekt nennen.
4. **Methodischer Befund:** Allgemeines maschinelles Parsen der DLMF-LaTeX-Formeln stagnierte nach v5.2. Ergiebig waren nur **quellengenau ausgewählte Einzelformeln mit Definitionsbereich** (v5.4, v5.9, v6.6). Für künftige Arbeit spricht das gegen eine Massenernte und für gezielte, belegte Einzelprüfungen.
5. **Fehlende Archive:** Die Berichte verweisen auf **22 Archivpakete und Programme**, die nicht in Git liegen, darunter `KI_Tensor_DLMF_Parser_v5_2…v5_7_NoLoss.zip`, `…Relationscompiler_v6_5…`, `…Karten_Inventar_v6_8…` mit `build_v68.py`, `…Thesen_Operationalisierungen_Skills_v6_9…` und `codebuch_v38/v64/v68.sqlite`. Ohne sie sind die Stände ab v5.2 nur über die Berichte nachvollziehbar. Die Pakete werden in die Dateianfrage F5 aufgenommen.

## Empfehlung zu DEC-KT-01

| Option | Bewertung |
|---|---|
| **a · in `main` übernehmen, als Archiv gekennzeichnet** | **empfohlen.** Keine Konflikte, keine sensiblen Inhalte. Die Berichte sind die einzige vollständige Erklärung vieler Register-Zahlen. Vor dem Merge kommt oben in `ki-tensor/README.md` ein Hinweis: „Arbeitsprotokoll 31.10.2026; Entwürfe ≠ Belege; Analyse siehe `forschung/register/ZWEIG_KI_TENSOR_*`“. |
| b · im Zweig lassen | Der Inhalt bleibt erhalten (zusätzlich `archiv/ki-tensor-no-loss-audit-2026-11-03`), ist aber für Leser und GPT schwer auffindbar. |
| c · nur die Berichte übernehmen, ohne Programme | nicht empfohlen; die Programme sind klein, sicher und reproduzierbar |

**Vor der Übernahme abzustimmen mit GPT:** Der Ordner `ki-tensor/` liegt im Hauptordner (Bereich `hauptordner_original`), nicht unter `docs/`. Die Website ist also nicht betroffen.
