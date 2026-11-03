# R4 · P-NEU-01 „Eine Fundstelle prüfen“ · Eigenlauf (Owner Claude)

**Status:** `owner_run` · **Prompt-SHA-256:** `be4a7b4770ab27d7…` (Abschnitt P-NEU-01 in `prompt-entwuerfe/PROMPT_ENTWUERFE_CLAUDE_V0_2.md`) · **Eingabe:** `P-NEU-01_INPUT_SNAPSHOT_01.json` (SHA-256 `4ad74ce376c0132b…`) · **Akte:** `P-NEU-01_OWNER_RUN_01.json` · `public_release: not_approved`

## Ergebnis

| Fall | Erwartet | Ergebnis | Erwartung erfüllt |
|---|---|---|---|
| C1 Positivfall: Meta-Logik, S. 19 | gefunden | **gefunden**, Wortlaut S. 19; Einschränkung S. 15 gefunden (Tensor „nicht selbst ein weiteres Logiksystem“) | ja |
| C2 falsche Seite (S. 7) | andere_stelle | **andere_stelle → S. 19**; S. 7 enthält nur die Vergleichs-Signatur | ja |
| C3 Modus ponens, S. 20 | gefunden | **gefunden**: „Diese Regel ersetzt den klassischen Modus ponens …“ | ja |
| C4 ungültige DOI | Zugriff false | `zugriff_gelungen: false` (HTTP 404), aber das Schema erzwingt einen `ergebnis`-Wert | teilweise |

## Befunde zum Prompt (für v0.3)

- **B1 · Ergebniswert bei misslungenem Zugriff:** Das Ausgabeschema hat keinen Wert für „nicht prüfbar“. `nicht_gefunden` würde fälschlich einen negativen Inhaltsbefund melden. **Vorschlag:** `ergebnis` um `nicht_pruefbar` erweitern, Pflicht bei `zugriff_gelungen: false`.
- **B2 · Sinngleich, aber nicht wortgleich (C1):** Die Registeraussage lässt „keine weitere Variante, sondern“ weg. Der Prompt verlangt für „gefunden“ den übereinstimmenden Wortlaut, das ist hier also streng genommen „teilweise“. **Vorschlag:** `ergebnis` `gefunden_sinngleich` ergänzen oder die Regel ausdrücklich auf „sinngemäß mit Zitat“ setzen. Sonst entscheiden Ausführende verschieden; genau das hat R4 bei LOGIK-PROMPT-02 gezeigt.
- **B3 · Gegenprobe (Schritt 4) wirkt:** Sie fand in C1 die Einschränkung auf S. 15, die bei reiner Fundstellenprüfung übersehen würde. Beibehalten.
- **B4 · Prüfmittel nennen:** Das Ergebnis hängt vom Werkzeug ab (Textextraktion vs. Seitenbild). **Vorschlag:** Feld `pruefmittel` aufnehmen; bei Formeln mit Sonderzeichen (ρ⁻¹) ist eine Sichtprüfung nötig.

## Nächster Schritt (R4)

GPT führt **blind** aus: Gelesen werden nur der Prompt (SHA oben) und der Eingabe-Snapshot, **nicht** diese Ausgaben. Danach vergleichen beide KIs, dann folgt v0.3 mit B1, B2 und B4.
