# Entscheidungen und Uneinigkeiten für Nils

**Laufend geführt** von Claude und GPT. Hier stehen nur Fragen, die die KIs nicht selbst entscheiden dürfen, und Punkte, bei denen sie sich nicht einig sind. Bitte im Chat antworten, etwa „NAV: Variante c“.

**Priorität:** P0 = blockiert Arbeit jetzt · P1 = bald nötig · P2 = kann warten

*Stand: 2026-11-03, 14:40. Die erste Fassung dieser Datei liegt in der Git-Historie (Commit `078caad`).*

---

## P0 · DEC-NAV-01 · Wie soll das Hauptmenü der Website aussehen?

**Einfach erklärt:** Zwei Arbeitsstränge haben gleichzeitig zwei verschiedene Menüs gebaut. Beide können nicht gleichzeitig laufen. Solange nicht entschieden ist, kann der große Zweig mit 160 Änderungen (Inkubator, Quellenatlas, 12 neue Seiten) nicht in die Website übernommen werden. Jede weitere Menüänderung macht das schwieriger.

| Variante | Menü | Vorteil | Nachteil |
|---|---|---|---|
| a | 5 Punkte: Start · KI & Forschung · Wissen & Werkzeuge · SOULution & Publikationen · Mitmachen | enthält schon alle 27 Seiten | der Forschungsinkubator fehlt |
| b | 7 Punkte: Start · Forschung · Projekte · Inkubator · Publikationen · Mitmachen · SOULution | wie die Website heute | 7 neue Seiten aus dem Zweig fehlen im Menü |
| c | wie a, plus „Inkubator“ | alles erreichbar | ein Punkt mehr |

**Empfehlung Claude:** c. **GPT:** verlangt ebenfalls genau ein Menü und deine Entscheidung (P0-X2); das Website-Bündel 02 nennt vorläufig b.
**Wenn nicht entschieden wird:** Der Zweig bleibt liegen, die Konflikte wachsen.

## P1 · DEC-INK-01 · Zwei Seiten heißen „Inkubator“. Was tun?

**Einfach erklärt:** Es gibt den „Forschungsinkubator“ (wie Menschen mit ihrer KI mitforschen) und „Schrödinger’s Inkubator“ (digitale Souveränität, offene Software). Inhaltlich sind das zwei verschiedene Dinge mit demselben Wort.

| Variante | Bedeutung |
|---|---|
| a | beide behalten, klar unterschiedlich benennen, gegenseitig verlinken |
| b | zu einer Seite zusammenlegen |
| c | einen davon umbenennen (welchen und wie?) |

**Empfehlung Claude:** a. **GPT:** prüft das im Website-Review (W03).
**Wenn nicht entschieden wird:** Besucher verwechseln die Seiten.

## P1 · DEC-AX-01 · Sollen die alten Achsen (A) oder die neuen (B) die anderen ersetzen?

**Einfach erklärt:** Es gibt zwei Arten, die 27 Felder zu beschreiben: die ursprüngliche neutrale Sprache (A) und die neueren Prüfrollen aus Tensor 2.0 (B, im Original T1/T3/T5). Beide KIs schlagen vor, **nichts zu ersetzen**: Beide bleiben bestehen, Übersetzungen zwischen ihnen werden einzeln geprüft.

**Empfehlung Claude und GPT (einig):** nichts ersetzen, beide getrennt behalten.
**Bitte nur bestätigen** („AX: ja“) oder widersprechen.

## P2 · DEC-PROTO-01 · Berichtsrhythmus an dich

**Einfach erklärt:** Du wünschst nach je 3 Schritten eine kurze Zusammenfassung. GPT hat zusätzlich nach je 3 vollständigen Austauschrunden eine große Analyse eingeführt.

**Vorschlag (Claude, GPT-Antwort ausstehend):** beides. Ein Kurzbericht nach je 3 Arbeitsschritten (höchstens 10 Zeilen, einfache Sprache) und die große Analyse nach je 3 vollständigen Runden.
**Bitte nur bestätigen** oder ändern.

---

## Uneinigkeiten zwischen Claude und GPT

| Thema | Claude | GPT | Stand |
|---|---|---|---|
| Menüliste in Website-Bündel 02 | nicht festlegen vor DEC-NAV-01 | Bündel nennt 7 Punkte, Prüfrahmen verlangt deine Entscheidung | Rückfrage an GPT läuft (`CLAUDE_DISKUSSION_01.md`, UE-01) |

**Bereits geeinigt:** einheitliche Status-Schreibweise ohne Umlaute; Achsen-Originalnamen T1/T3/T5 mit gekennzeichnetem Alias; alle sechs GPT-Korrekturen DR-01 bis DR-06 an Claudes Datenbefunden.

---

## Von dir benötigt (keine Entscheidung, nur eine Aktion)

- **Datei-Upload an Claude:** `CLAUDE_KI_TENSOR_STARTPAKET_ZYKLUS_001.zip` (842.482 Bytes; GPT hat es dir als Download erstellt). Darin sind Tensor 2.0 und das Logik-Tensor-2.0-Manuskript. Ohne die Datei kann Claude die Achsen B und das 2.0-Manuskript nicht prüfen.
