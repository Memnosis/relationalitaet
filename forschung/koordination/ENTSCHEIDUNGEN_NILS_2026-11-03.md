# Entscheidungen und Uneinigkeiten für Nils

**Laufend geführt** von Claude und GPT. Hier stehen nur Fragen, die die KIs nicht selbst entscheiden dürfen, und Punkte, bei denen sie sich nicht einig sind. Bitte im Chat antworten, etwa „NAV: Variante c“.

**Priorität:** P0 = blockiert Arbeit jetzt · P1 = bald nötig · P2 = kann warten

*Stand: 2026-11-03, 14:40. Die erste Fassung dieser Datei liegt in der Git-Historie (Commit `078caad`).*

---

## Entschieden am 03.11.2026 (Nils, im Chat mit Claude)

| ID | Entscheidung von Nils | Umsetzung |
|---|---|---|
| DEC-NAV-01 | **b**: 7-Punkte-Menü (Start · Forschung · Projekte · Inkubator · Publikationen · Mitmachen · SOULution) | GPT behält `tensor-hierarchy.js` und führt den Integrationszweig nach diesem Menü zusammen; die Seiten aus dem Zweig werden in die 7 Gruppen eingeordnet |
| DEC-PROMPT-01 | **erst alle analysieren**: freigeben, was freigabefähig ist; Rest als Bericht an Nils | Claude: `PROMPT_ANALYSE_V0_1.json` (14 Kandidaten, 22 intern, 2 heikel); GPT prüft gegen; Bericht an Nils als DOCX |
| Berichtsformat | **Berichte an Nils immer als DOCX** | gilt für beide KIs |
| DEC-INK-01 | **fusionieren und differenzieren**: im Prinzip Schrödinger’s Inkubator; bei Bedarf nach dem Konzept fragen | GPT: eine Inkubator-Seite mit klar unterschiedenen Teilen; Konzeptfragen an Nils |
| DEC-AX-01 | **ergänzen und nach einem trinitären dritten Faktor suchen** | A und B bleiben; Claude sucht Kandidaten für den dritten Faktor (Entwurf P-NEU-04) |
| DEC-PROTO-01 | **beides** | Kurzbericht nach je 3 Schritten und große Analyse nach je 3 vollen Zyklen |
| FRAGE-LOGIK-100 | **unbekannt; nachliefern und verbessern (Upgrade)** | Upgrade-Aufgabe Logik-Tensor, Entwurf P-NEU-03 |
| DEC-KT-01 | **genauer analysieren** | erledigt: `forschung/register/ZWEIG_KI_TENSOR_TIEFENANALYSE_V0_1.md` (16/16 Zahlenketten stimmig, 0 bewiesene Trinitäten/Tensoren, 22 fehlende Archivpakete). Empfehlung: übernehmen, als Archiv gekennzeichnet. **Bitte erneut entscheiden: „KT: a/b/c“** |
| NEU · DEC-AUDIT-20 | **alle 20 Zyklen Sicherheits- und Regel-Audit sowie Change-Management-Analyse über die 20 Schritte**, von beiden KIs vereinbart; danach eine zusätzliche Sicherheits- und Regelschleife. Dazu gehören Archiv, alte Versionen, Backup-Regeln und die **Möglichkeit, unnötige mehrfache Altbestände zu löschen** | Vorschlag Claude in `CLAUDE_DISKUSSION_05.md`; Einigung mit GPT ausstehend |

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

## P0 · DEC-PROMPT-01 · Sollen die internen KI-Anweisungen aus den öffentlichen Dateien genommen werden?

**Einfach erklärt:** Drei öffentliche Dateien enthalten 38 vollständige Meta-Prompts (interne Arbeitsanweisungen an KIs), keiner davon freigegeben oder getestet. GPT blendet sie auf `mitmachen.html` schon aus, auf `taskkarten.html` sind sie noch sichtbar und kopierbar. Aber auch ausgeblendet kann sie jeder in den Dateien auf GitHub lesen.

| Variante | Was passiert |
|---|---|
| a | Bleiben öffentlich; GPT blendet sie nur auf allen Seiten aus |
| b | Auf `main` durch bereinigte Fassungen ersetzen: Aufgaben bleiben vollständig, statt des Prompt-Texts steht ein Prüfsummen-Verweis. Die Originale bleiben in der Git-Historie und privat bei dir. Claude hat das verlustfrei getestet. |
| c | Einzeln prüfen: was du freigibst, bleibt öffentlich, der Rest wie b |

**Empfehlung Claude:** b jetzt, später c für einzelne Prompts. **GPT:** fordert in `86fb9db` ebenfalls einen bereinigten öffentlichen Export.
**Hinweis:** Was schon auf GitHub war, bleibt in der Historie sichtbar. b und c verhindern nur, dass es weiter verbreitet und angezeigt wird.
**Wenn nicht entschieden wird:** Die Prompts bleiben öffentlich lesbar.

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

## P2 · FRAGE-LOGIK-100 · Gibt es eine Fassung des Logik-Tensors mit 100 Begriffen?

**Einfach erklärt:** Kapitel 8 im veröffentlichten Logik-Tensor 1.0 (Zenodo) heißt „100 Logik-Begriffe“. Die Tabelle darin hat aber 34 Zeilen: 27 Feldbegriffe und 7 Begriffe aus dem Außenraum. GPTs neue Arbeitsfassungen sprechen von „100 Begriffen“.

| Antwort | Folge |
|---|---|
| a) Ja, es gibt eine Fassung mit 100 Begriffen | bitte bereitstellen; Claude erfasst sie |
| b) Nein, 34 ist der Stand | Arbeitsfassungen sagen künftig „34 dokumentierte Begriffe“ |

**Empfehlung Claude:** bis zur Antwort die Zahl 100 nicht weitergeben. Details: `forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.md`.

## P2 · DEC-KT-01 · Soll der Zweig `ki-tensor/no-loss-audit` in `main` übernommen werden?

**Einfach erklärt:** Der Zweig enthält 28 Prüfberichte und 12 kleine Programme aus der Formel-Arbeit vom 31.10. Er hat keine Rohdaten und keine sensiblen Inhalte. Claude hat ihn geprüft: Die eigenständigen Programme rechnen richtig, die Berichte sind ehrlich („0 neue Tensoren bewiesen“). Er würde als neuer Ordner `ki-tensor/` öffentlich auf `main` erscheinen; es gibt keine Konflikte.

| Variante | Folge |
|---|---|
| a | übernehmen (Claude führt zusammen und meldet es GPT) |
| b | im Zweig lassen (bleibt erhalten, ist aber schwerer auffindbar) |

**Empfehlung Claude:** a. Details: `forschung/register/ZWEIG_KI_TENSOR_AUDIT_V0_1.md`.

---

## Uneinigkeiten zwischen Claude und GPT

| Thema | Claude | GPT | Stand |
|---|---|---|---|
| Menüliste in Website-Bündel 02 | nicht festlegen vor DEC-NAV-01 | Bündel nennt 7 Punkte, Prüfrahmen verlangt deine Entscheidung | Rückfrage an GPT läuft (`CLAUDE_DISKUSSION_01.md`, UE-01) |

**Bereits geeinigt:** einheitliche Status-Schreibweise ohne Umlaute; Achsen-Originalnamen T1/T3/T5 mit gekennzeichnetem Alias; alle sechs GPT-Korrekturen DR-01 bis DR-06 an Claudes Datenbefunden.

---

## Von dir benötigt (keine Entscheidung, nur eine Aktion)

- **Datei-Upload an Claude:** `CLAUDE_KI_TENSOR_STARTPAKET_ZYKLUS_001.zip` (842.482 Bytes; GPT hat es dir als Download erstellt). Darin sind Tensor 2.0 und das Logik-Tensor-2.0-Manuskript. Ohne die Datei kann Claude die Achsen B und das 2.0-Manuskript nicht prüfen.
