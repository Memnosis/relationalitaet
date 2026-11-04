# Tensoratlas – Forschungsbereitstellung und Prüfung (04.11.2026)

**Status:** separater Forschungsbranch, **keine Publikationsfreigabe**. Website-Owner: GPT; Fach-/Registergegenprüfung: Claude; Redaktionsfreigabe: Nutzer. Originaldateien wurden nicht verändert.

## Umgesetzt
- `docs/data/tensoratlas-forschung-v0_1.json`: 103 historisch benannte Gerüste, 2.781 aus ihren Achsen rekombinierte Feldadressen, jeweils drei Originalrollen. Die mathematischen Feldattribute bleiben **unknown/not_run/not_verified**.
- Erneut ausgeführter vollständiger lexikalischer Vergleich: 5.253 Paare, jede der sechs Achsenpermutationen; 5.104 ohne gemeinsamen Rollenbegriff, 144 mit Treffern auf einer Achse, fünf mit Treffern auf zwei Achsen, null mit drei. 149 Kandidatenpaare werden mit konkreter Permutation gespeichert.
- Projektion der neun separaten pfadbasierten Tensorakten mit 36 Paaranalysen aus Claudes ursprünglichem Lauf. **Kein erneuter mathematischer Gegenbeweis** und kein unabhängiger P3-Nachweis.
- `docs/tensoratlas-forschung.html`: durchsuchbare Lesesicht für Tensoren, alle Feldadressen, Rollen, Fünfer-Kandidaten und separate Pfadakten. Vor dem Mergen nicht über GitHub Pages erreichbar.
- `forschung/website/test_tensoratlas_preview.py`: unabhängige Neuprüfung der Achsen, Felder, 5.253 Paarvergleiche und Referenzwerte anhand der beiden JSON-Dateien.

## Nicht gerechnet / offen
1. Die 103 historischen Gerüste enthalten Rollen/Formelanker, jedoch keine ausführbaren wissenschaftlich typisierten Feldoperatoren je Position. Ein mathematisches „Auffüllen“ von 2.781 Feldern wäre eine Erfindung.
2. Vier Chemie-Gerüste (108 zusätzliche Prüfpositionen) müssen mit nachvollziehbarer Quelle und ihren Achsen importiert werden, bevor ein 107er-Gesamtvergleich fachlich möglich ist.
3. Inversion, Vorwärts-/Rückwärtsrechnung, Grenzfälle, Erhaltungssätze, symbolische Gleichheit und numerische Gegenproben sind **operatorgebunden**. Vor einer Reife R2+ sind Operator, Träger, Domäne und Quelle pro Feld erforderlich.
4. Die 100 letzten Originalnachrichten sind nicht vollständig chronologisch verifiziert; der vorhandene Crosswalk umfasst 72 atomisierte Anforderungen, nicht 72 wörtliche Antworten. Zu jeder der letzten 24 Antworten müssen gesondert Gesprächs-ID, Anspruch, Datei, Commit, Test, Ergebnis und offene Abhängigkeit nachgetragen werden.
5. Das vorhandene Register mit 44 Aufgabenfamilien ist **kein vollständig importiertes Forschungsergebnisregister**.

## Der nächste ausführbare Fachlauf
- Jede Formelanker-Referenz in einen typisierten Gleichungsknoten überführen, mit Quellenstand und unabhängiger Modellprüfung.
- Fehlerklassen nicht verstecken: `missing_formula`, `untyped_variable`, `dimension_unknown`, `domain_unknown`, `noninvertible`, `unresolved_similarity`, `counterexample`, `passed`.
- Matrix der zwölf Rechenfamilien für **anwendbare** Felder erstellen, mit `not_applicable` statt irreführenden 0 % bei nicht definierten Operatoren.
- Gleichheit/Spezialfall/Homomorphismus/Isomorphismus nur nach konkret typisierter Abbildung und unabhängiger Gegenprobe freigeben.

## Release-Check (vor Merge nach main)
- [ ] Python-Test läuft grün; Vergleich der 149 Treffer mit Claudes Axis-Alignment-Datei dokumentiert
- [ ] Claude prüft semantische/typisierte Zuordnung von Feldrollen und Datenmodell
- [ ] Quellenregister und Glossar über stabile IDs synchronisiert
- [ ] Browser-Abnahme Desktop/Mobil, Tastatur, JS-Abschaltung, Links/Assets
- [ ] Sicherstellen, dass keine privaten Akten oder Roh-KI-Nachrichten in den Export geraten
- [ ] Wissenschaftliche Statusangaben und Zahlen mit eindeutiger Grundgesamtheit
- [ ] Explizite redaktionelle Entscheidung über Navigation und öffentliche Freigabe

## Quelle/Version
- `docs/data/tensor-inventar-v10_7.json`: 103 historische Gerüste
- `forschung/tensor/algebra-claude/ALGEBRA_LAUF_V0_1.json`: neun separate Pfadakten
- `forschung/tensor/algebra-claude/ACHSEN_ALIGNMENT_POTENZIALE_103_V0_1.json`: referenzierte 149 Kandidaten
- `forschung/register/GESAMTPROJEKT_KOMBINATIONSREGISTER_V0_1.json`: 44 Aufgabenfamilien
- `forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json`: 72 Anforderungen, originale Chronologie ungeprüft

**Veröffentlichung:** Als wissenschaftliche Arbeitsansicht vorbereitet, nicht automatisch veröffentlicht. Der jetzige Forschungsbranch in einem öffentlichen GitHub-Repository ist selbst öffentlich lesbar.
