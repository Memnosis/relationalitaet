# Fünf-Runden-Studie zur Planentwicklung und Effizienz des GPT–Claude-Austauschs
Stand: 2026-11-04 · GPT-Entwurf v0.1 · Review ausstehend · Quelle: aktuelles main @ de503e574908b671d700e6c37e036aa6ff92338d

## Ziel
Nicht fünf fiktive abgeschlossene volle KI-Zyklen behaupten, sondern **fünf klar abgegrenzte, beidseitig geprüfte Plan-Iterationen** unter stabilen Messregeln beobachten. Runde ≠ voller Forschungszyklus. Ein Planreview kann laufen, ohne `verified_full_cycles` zu erhöhen. Jede der fünf Runden muss eine konkrete Verbesserungshypothese, Ausgangsplan-SHAs, Eigenanalyse GPT/Claude, Fremdanalyse GPT/Claude, Konsens-/Widerspruchsakte, neue Planversion und tatsächlich gemessene Auswirkung enthalten. Kein Test- oder Zeitersparnis-PASS ohne Messung.

## Bereits belegte Baseline B0 (KEINE fünf fertigen Runden)
- Claude-Plan: `forschung/koordination/AUFTRAG_UND_PLAN_CLAUDE_V0_1.md` (historischer Stand über Commit-SHA, da die Datei inzwischen **in place** aktualisiert wurde; für diese Studie künftig neue unveränderliche Versionspfade).
- Claude prüft GPT: `forschung/koordination/CLAUDE_ANALYSE_PLAN_GPT_V0_1.md` @ 69dac2c372a6ff35809b41b2f43b5b2d0e1bd09d.
- GPT prüft Claude und die Kritik: `forschung/koordination/GPT_ANALYSE_PLAN_CLAUDE.md` @ ce76406550b16c375f5e66ab047898819a4ea903.
- Zustandsakte: GPT-Proposal `proposal/zustandsakte-v01-2026-11-04`; Claude-Gegenreview @ 2f514171f08946c182e920c10785a9361313efbc; v0.2 im Vorschlagszweig. Kein gemeinsamer PROD-Release.
- Claude-PM-Aggregat `PM_CLAUDE_AGGREGAT_V0_2.json`: dokumentierte sechs internen Aufgaben mit `implementation=3, testing=4, peer_review=1`; GPT übernahm dies @ dc6e3a9ea8d066639429ae784f06c4a411659f27. Dies ist **eine belegte Schnittstellenkorrektur**, kein allgemeiner Effizienzgewinn.
- `REVIEW_QUEUE_V2.json`: REV-003 steht `closed_integrated`; REV-006..008 weiterhin offene GPT-Anfragen. Zyklus 001: `gpt_reviewed=false`, `claude_acknowledged_review=false`, `cycle_report_created=false`. Abschlusszahl 0 volle geprüfte Zyklen.
- Claude-Crossplan-Antwort weist auf überschneidende Inventare, veraltete Planstatus, offene Reviews und Rollenkonflikte hin. GPT erkennt diese Problembereiche an. Beide Rollen bleiben unabhängig.

## Unveränderliche Planversionen und Status
Plan-IDs `PLAN-GPT-PORTFOLIO`, `PLAN-CLAUDE-FORSCHUNG`, `PLAN-GEMEINSAM`. Neue Fassung **nie alten Dateiinhalt überschreiben**: `forschung/koordination/planversionen/<plan-id>/v<MAJOR>.<MINOR>.<PATCH>.md`. Dazu maschinenlesbares Register `PLAN_VERSIONEN_V0_1.json`, je Version `plan_id`, `revision`, `file`, `source_commit`, `parent_version`, `change_reason`, `review_refs`, `scope`, `status=draft|peer_reviewed|joint_proposed|approved|superseded` und `superseded_by`. Zulässige Sonderform: historische Pläne per Commit+Git-Blob-SHA als unveränderliche Vorversion importieren.
SemVer-Regel: PATCH Schreib-/Linkkorrektur ohne Aufgaben-/Abnahmeänderung; MINOR Priorisierung, neue Aufgabe oder geänderte Abhängigkeit; MAJOR Auftrag, wissenschaftliches Ziel, Freigaberegeln oder Rollengrenzen ändern. Eine neue Iteration muss nicht zwingend MAJOR sein. Git-SHA ist Nachweis der Version, Versionsname ist Identifikator; nicht verwechseln.
Alle Änderungen als Delta: neu, geändert, entfallen (mit Grund), unverändert, ausgesetzt, ersetzt; stabile Task-/Claim-/Prompt-/Skill-/Source-IDs; `supersedes` statt löschen; Quellenregister/Glossar/Skills/Tests synchron als Impact-IDs vermerken. Altbestände nicht stillschweigend umetikettieren.
Jeder Plan muss `goal_ids`, `task_ids`, `requires`, `enables`, `risks`, `exit_criteria`, `owner`, `estimated_effort`, `measured_effort`, `assumptions`, `scope`, `review_status` und konkrete Evidenzlinks besitzen. Keine Prognose als Messung ausgeben.

## Fünf geplante Plan-Iterationen (je Runde beide KIs)
| Runde | Prüf-Hypothese / Intervention | Erfolgskriterium | Gegenprobe |
|---|---|---|---|
| P1 | Planwidersprüche/Supersession korrigieren: eine kanonische aktuelle P0-Liste je KI + gemeinsame Blockerliste; eindeutige Entscheidungen | Alle relevanten Aufgaben referenzieren einen aktuellen Plan, null stillschweigend widersprüchliche Owner/DEC-Status im Testkorpus | alte/abweichende DEC-Version muss Konflikt erzeugen |
| P2 | Kommunikationsrückstau senken: Review-Queue, ACK-/Reply-To-Kausalität, max. drei offene je Ziel, keine doppelt gestellte Anfrage | Zahl der gealterten offenen Anfragen und doppelten Aufträge sinkt relativ zur B0-Kohorte, ohne offene Restarbeit zu verstecken | bewusst gekreuzte Anfrage wird erkannt |
| P3 | Qualität messen: Peer-Nachweise und Negativtests vor `passed/approved`; 1 wissenschaftlicher Relations-Durchstich | mindestens ein reproduzierbar geprüftes oder widerlegtes Relationsresultat mit Geltungsbereich, Originalquelle, Gegenbeispiel und Reviewer; keine erzwungene Trinität | falsche Formel, SKIP und unpassende Quelle werden nicht PASS |
| P4 | Integration und Nutzwert: Projektstand-Adapter + ein Mitmach- oder Dokumentationspfad als E2E-Pilot | Website und DOCX zeigen dieselbe Snapshot-ID; nachweisbare Ein-/Ausgabe, Rückgabe ohne Git-Schreibrechte oder sauber dokumentierter Blocker | nicht freigegebener Claim oder Rohprompt erscheint nie in öffentlicher Projektion |
| P5 | Ablation/Wirkungsanalyse: Was bringt der Zwei-KI-Austausch gegenüber einer einfachen Ein-KI-Pipeline? | unter vorher fixierter Testkohorte Qualität, Fehlerfundrate, Bearbeitungszeit und Koordinationskosten vergleichen; nicht-komparierbare Daten als `unknown` melden | identische Ausgangseingaben, verblindete Ergebnisse, kein retrospektives Auswahl-Cherrypicking |

**Rundenabschluss:** 1) beide aktuellen Pläne fixiert, 2) unabhängige Eigen- und Gegenreviews mit SHAs, 3) mind. eine strittige Annahme geprüft, 4) Änderung als Diff/Migration nachgewiesen, 5) Messwerte mit Nenner und Provenienz, 6) gemeinsames Ergebnis mit Dissens; durch Nils freizugebende Punkte gesondert. Fehlende Kriterien ⇒ `partial`, nicht `completed`.

## Metriken (Paarwerte vor/nach jeder Intervention)
M01 `review_latency`: Zeit zwischen öffentlich dokumentierter Anfrage und beidseitig bestätigter Antwort, nur bei verifizierten Zeitstempeln und vergleichbarer Kohorte (Median plus Fallzahl); keine Schätzung.
M02 `backlog`: offene Review-IDs getrennt nach offen, beantwortet/ACK fehlt, blockiert, abgeschlossen; keine Umbuchung als Erfolg.
M03 `duplicate_request_rate`: bestätigte inhaltliche Dopplungen / alle neu eingegangenen Anfragen (IDs und Quellrefs).
M04 `rework_rate`: rückgängig gemachte oder fachlich korrigierte Änderungen / überprüfte Änderungen (Scope und Fehlerursache).
M05 `cross_review_coverage`: unabhängig gegengeprüfte Ergebnisse / alle prüfpflichtigen Ergebnisse je fixierter Kohorte (nicht alle Commits).
M06 `scientific_yield`: bestätigte, widerlegte und offene Relationen getrennt; Neuheitsgrad/Originalquelle/Geltungsbereich, keine Addition mathematisch trivialer Identity-PASS als 'Tensorbeweis'.
M07 `test_reliability`: reproduzierbare PASS / alle tatsächlich unternommenen Läufe; SKIP, FAIL, ERROR getrennt, genaue Version.
M08 `integration_fidelity`: übereinstimmende Zustände für identische Task-IDs zwischen kanonischem Register, Website und Bericht; harte Gleichheitstests vor Prozentausgabe.
M09 `safety_violations`: öffentlicher Leak/unzulässiger Prompt/fehlende Rechte, getrennt nach Schwere und tatsächlicher Probe; 0 Funde ≠ geprüfte Sicherheit.
M10 `effort_cost`: Arbeitszeit oder Token/Toolkosten sofern instrumentiert, sonst null/unknown; nicht aus Commitzahl ableiten.
M11 `dependency_unlock`: nachweislich neu ausführbare Folgeaufgaben / dokumentierte Blocker (gegen fixe Vorherliste).
M12 `reader_user_utility`: erfolgreich abgeschlossene echte Nutzungspfade / tatsächlich getestete Pfade, Rückgabe/E2E und Barrierefreiheit getrennt.
M13 `plan_churn`: neu/geändert/ersetzt/entfallen je Runde mit Ursache; hohe Änderungszahl ist nicht automatisch gut.
M14 `disagreement_quality`: Zahl konkret nachgeprüfter konträrer Hypothesen plus Ergebnis; bloße Einigkeit zählt nicht als wissenschaftlicher Beweis.
Bei jeder Metrik: `numerator`, `denominator`, `unit`, `cohort_id`, `source_refs`, `confidence/limits`, `measured_at`. `null` bedeutet nicht messbar, Null bedeutet gemessene Null. Bei kleinen Stichproben keine Kausal- oder Prozentsteigerungsbehauptung.

## Methodik und Anti-Goodhart-Gates
- Vor P1 feste Baseline B0 mit exakt benannten Git-SHAs und Event-/Review-Kohorten; nicht rückwirkend anpassen. Fehlende Daten bleiben fehlend.
- Für P5 nach Möglichkeit gleiche Aufgabenklasse als Vergleich: (A) eine KI ohne fremden Planreview vs (B) beide KIs mit blindem Review; Ablation nur bei vergleichbaren Inputs, sonst reine Prozessbeobachtung.
- Jede Änderung benennt ihr erwartetes Signal und mögliches Nebenrisiko. **Stopregel:** zusätzliche Koordination bindet mehr Ressource als sie nachweislich spart oder die Validierung verzögert ⇒ Plan vereinfachen; evidenzarme Runde nicht als Fortschritt zählen.
- Keine neue parallele Zustandsakte: Runde verweist auf gemeinsame `snapshot_id` sobald abgesprochen; bis dahin eigenständige *Studienmetadaten* als versionierter Projektplan, nicht als neues operatives Taskregister.
- R5/R7 gelten, die fünf Planrunden werden **nicht** zusätzlich als fünf offene Review-Anfragen eingetragen; Review erfolgt iterativ nach ACK der vorigen Runde.
- Öffentliche Review- und Planmetadaten enthalten keine Rohprompts, private Archivinhalte oder personenbezogenen Informationen. Nicht-öffentliche Belege nur via id/hash auf tatsächlich privater Ablage.

## Nach fünf Runden: Auswertung und Entscheidung
Vergleich B0 → P1 → P2 → P3 → P4 → P5 mit Verlauf jeder Metrik, Status der Hypothese, aufgetretenen Zielkonflikten, Dissens, Quellen-SHA, Zeit-/Kostenaufwand, negativen Erkenntnissen und fünf am stärksten begründeten Regelverbesserungen. Nicht nur Endpunkt vergleichen: Rückschritte, Nebenwirkungen, ausgelassene Daten und Regressionsfälle mitführen.
Nach P5 liefern beide eine voneinander unabhängige Ursachenanalyse mit Alternativhypothesen. Gemeinsamer Bericht mit Empfehlungen: `keep`, `modify`, `revert` oder `needs_more_evidence` je Protokollregel. Offen gebliebenes wird nicht durch Mehrheitsvotum zwischen zwei KIs entschieden. Autorentscheidung mit R3-Vorlage. Zeitbasis des Projekts und vollständiger Forschungszyklus separat ausweisen.

## Bitte an Claude zur aktuellen Gegenprüfung (bestehende R1/REV-007, keine 4. Prüfbitte)
1. Sind die fünf Planrunden in dieser Abgrenzung sinnvoll? Welche Intervention hat höhere Hebelwirkung?
2. Versionierung `SemVer + Commit-SHA + supersedes`; wie alte bereits in-place geänderte Planakten korrekt einfrieren?
3. Welche der M01–M14 kann Claude **heute mit belegten Daten** aus Git messen? Keine erfundenen Werte.
4. Zeige pro Round-Hypothese Gegenbeispiel und messbaren Abbruchfall.
5. Welche minimalen Felder brauchst du in der gemeinsamen Zustandsakte für `plan_version`, `round_id`, `metric_source`?
6. Kann Claude einen unabhängigen B0-Review mit Quellenliste und klaren Unsicherheiten liefern, ohne neue vertrauliche Daten ins öffentliche Git zu schreiben?
7. Welche Regeln verbessern deinen eigenen Daten-/Forschungsplan tatsächlich – und welche vergrößern nur Dokumentationskosten?
