# Prompt-Entwürfe (Claude) · v0.2 · ENTWURF

**Änderungen gegenüber v0.1** (nach GPT-Review in `GPT_DISKUSSION_05.md` §4, alle Punkte übernommen):
- P-NEU-01: zusätzliche Ausgabefelder `source_version`, `verification_actor`, `access_method`, `checked_at`; die Bedingungen für „verifiziert“ sind präzisiert; Zitatlänge und Lizenz beachten.
- P-NEU-02: „unabhängig“ ist definiert; neu sind Synonyme, Fachgebiet, Widerspruch und `no_sufficient_source`.
- P-NEU-03: die 10-%-Vorgabe ist entfernt.
- P-NEU-04: die Nullhypothese wird ausdrücklich getestet; Bedingung (c) ist möglicher Beleg, keine Voraussetzung; G gilt nur als formaler Träger.
- P-NEU-05: Viele-zu-viele-Zuordnung; „verifiziert“ erst nach Sichtprüfung.

v0.1 bleibt unverändert erhalten: `PROMPT_ENTWUERFE_CLAUDE_V0_1.md`.

**Owner:** Claude · **Stand:** 2026-11-03 · **Status aller Entwürfe:** `public_release: not_approved`, `prompt_execution_status: not_run` · R4-Status: `peer_reviewed` (Analyse durch GPT), Eigenlauf und Simulation stehen aus
**Ablauf:** zuerst Gegenprüfung durch GPT, dann Probelauf mit Ausführungsakte (`prompt_id`, `revision`, `input_snapshot`, `tool_version`, `executed_at`, `output_hash`, Negativfall), dann Entscheidung von Nils.
**Warum diese Entwürfe:** Die 38 vorhandenen Texte sind Meta-Prompts (siehe `forschung/register/PROMPT_ANALYSE_V0_1.json`). Es fehlen direkte, prüfbare Arbeits-Prompts für die wichtigsten offenen Fragen. Bezüge: DEC-AX-01 (dritter Faktor), FRAGE-LOGIK-100 (Upgrade), C-P0-03 (Thesen), WEB-GLOS-01 (Glossar).

| ID | Ebene | Für wen | Öffentlich denkbar? | Ersetzt/ergänzt |
|---|---|---|---|---|
| P-NEU-01 Fundstelle prüfen | Prompt | Mitmachende ohne Git | ja, nach Probelauf | neu (Quellenprüfung) |
| P-NEU-02 Glossarbegriff definieren | Prompt | Mitmachende ohne Git | ja, nach Probelauf | direkter Ersatz für Meta-Prompt WEB-GLOS-01 |
| P-NEU-03 Logik-Begriffe ergänzen | Prompt + Agent | Forschung intern | nein (Upgrade-Arbeit) | FRAGE-LOGIK-100 |
| P-NEU-04 Trinitärer dritter Faktor | Agent + Meta | Forschung intern | nein | DEC-AX-01 |
| P-NEU-05 Originalthesen-Inventar | Agent | Claude intern | nein | C-P0-03 |

---

## P-NEU-01 · Eine Fundstelle prüfen

**Ziel:** Prüfe, ob eine Aussage wirklich an der angegebenen Stelle einer öffentlich zugänglichen Quelle steht. Du prüfst nur die **Fundstelle**, nicht, ob die Aussage wissenschaftlich stimmt.

**Eingabe (vom Projekt bereitgestellt):** ein Datensatz mit `claim_id`, `aussage`, Quelle (DOI oder URL) und `fundstelle` (Seite oder Abschnitt).

**Arbeitsschritte:**
1. Öffne die Quelle über DOI oder URL. Notiere Datum, Zugriffsweg und ob der Zugriff gelang.
2. Suche die Fundstelle. Zitiere höchstens zwei Sätze wörtlich, mit Seitenangabe.
3. Vergleiche: Steht die Aussage dort sinngemäß, teilweise, gar nicht oder an anderer Stelle?
4. Gegenprobe: Suche in derselben Quelle nach einer Stelle, die der Aussage widerspricht oder sie einschränkt.

**Ausgabe:**
```json
{"claim_id": "", "source_version": "", "verification_actor": "", "access_method": "doi | url | datei",
 "checked_at": "", "zugriff_gelungen": true, "zugriff_fehlergrund": "",
 "ergebnis": "gefunden | teilweise | nicht_gefunden | andere_stelle | andere_ausgabe",
 "zitat": "", "seite": null, "einschraenkung_gefunden": "", "unsicherheiten": ""}
```

**Regeln:**
- Nichts erfinden.
- „gefunden“ nur, wenn **dieselbe Ausgabe/Version**, der **Wortlaut** und die **Fundstelle** übereinstimmen. Bei einer anderen Auflage oder Version: `andere_ausgabe`.
- Ist die Quelle nicht erreichbar: `zugriff_gelungen: false` und Grund angeben.
- Zitat höchstens zwei Sätze, nur wenn die Lizenz es erlaubt, sonst nur die Fundstelle.
- Keine Bewertung der Aussage selbst.

**Abnahme:** Das Projekt bildet das Ergebnis auf die Werte `digital_verifiziert`, `digital_nicht_erreichbar` oder `handpruefung_noetig` ab (`vokabular.json`).

**Geplanter Probelauf:** `CLM-LOGIK10-METALOGIK` (Positivfall, S. 19) und eine absichtlich falsche Seitenangabe (Negativfall).

---

## P-NEU-02 · Einen Glossarbegriff definieren

**Ziel:** Für **einen** Fachbegriff aus dem Projektglossar eine kurze, belegte Definition vorschlagen.

**Eingabe:** Begriff, bisherige Projekt-Kurzdefinition (falls vorhanden), Fachgebiet.

**Arbeitsschritte:**
1. Suche **zwei unabhängige Fachquellen** (Lehrbuch, Fachlexikon, Übersichtsartikel), bevorzugt frei zugänglich. **Unabhängig** heißt: verschiedene Autoren bzw. Herausgeber, und keine Quelle schreibt die andere ab oder zitiert nur die andere.
2. Formuliere eine Definition in höchstens drei Sätzen, allgemeinverständlich (Lesetiefe E1).
3. Ergänze eine fachliche Präzisierung (E2) mit Quelle.
4. Vergleiche mit der Projekt-Kurzdefinition: deckungsgleich, enger, weiter oder abweichend? Begründe.
5. Nenne Synonyme und das Fachgebiet. Widersprechen sich die Quellen, beschreibe den Widerspruch, statt ihn aufzulösen.
6. Findest du keine zwei unabhängigen Quellen, gib `no_sufficient_source` zurück. Das ist ein gültiges Ergebnis.

**Ausgabe:**
```json
{"begriff": "", "fachgebiet": "", "synonyme": [], "definition_e1": "", "praezisierung_e2": "",
 "widerspruch_zwischen_quellen": "", "status": "ok | no_sufficient_source",
 "quellen": [{"angabe": "", "url_oder_doi": "", "fundstelle": ""}],
 "vergleich_projekt": "gleich | enger | weiter | abweichend", "begruendung": ""}
```

**Regeln:** Keine erfundenen Quellen. Nicht frei zugängliche Quellen kennzeichnen. Die Projektdefinition nicht ändern, sondern nur vergleichen.

**Abnahme:** zwei überprüfbare Fundstellen; Vergleich begründet.

**Geplanter Probelauf:** „Syntaxgerüst“ und „Institution Theory“ (Außenraum-Begriff, Status „offen“).

---

## P-NEU-03 · Logik-Tensor: Begriffe auf ein vollständiges Inventar ergänzen

**Kontext:** Kapitel 8 des Logik-Tensors 1.0 kündigt 100 Begriffe an und enthält 34 (27 Feldbegriffe und 7 Außenraum-Begriffe). Nils wünscht ein Upgrade.

**Ziel:** Kandidaten für weitere Logikbegriffe vorschlagen und je Begriff begründen, wo er im Tensor liegt **oder warum er außerhalb liegt**.

**Eingabe:** `forschung/tensor/logik-claude/LOGIK_TENSOR_1_0_EXTRAKT_V0_1.json` (27 Felder, 34 Begriffe, 7 Logiksysteme, Axiome).

**Arbeitsschritte:**
1. Sammle Standardbegriffe der Logik aus mindestens drei Fachquellen (z. B. Lehrbuch der mathematischen Logik, Stanford Encyclopedia of Philosophy, Handbuch Beweistheorie).
2. Entferne Begriffe, die schon unter den 34 vorkommen, auch als Synonym.
3. Ordne jeden Kandidaten **einem** Feld zu (Adresse wie `ZM-II-β`), begründe mit der Felddefinition, nenne eine **alternative** Zuordnung oder `außerhalb` mit Grund.
4. Markiere unsichere Zuordnungen (`mehrdeutig`) statt sie zu erzwingen.

**Ausgabe:** Tabelle `begriff | kurzdefinition | quelle | adresse_oder_ausserhalb | alternative | begruendung | sicherheit (hoch/mittel/gering)`.

**Regeln:** Ziel ist ein **begründetes** Inventar, nicht genau 100. Weniger gut begründete Begriffe sind besser als viele erzwungene. Originalzuordnungen der 27 Feldbegriffe bleiben unverändert.

**Abnahme:** Jeder Kandidat hat eine Quelle. **Alle** begründet mehrdeutigen oder nicht zuordenbaren Kandidaten sind dokumentiert, ohne Zielquote (0 % oder 40 % sind gleichermaßen zulässig). Ein Fachprüfer kann jede Zuordnung nachvollziehen.

---

## P-NEU-04 · Den trinitären dritten Faktor zu den Achsensystemen A und B suchen

**Kontext:** Es gibt zwei Achsensysteme: A (NM/ZM/UM × I/II/III × α/β/γ, Tensor-Basics) und B (T1 Beziehung, T3 Gestalt, T5 Ablauf, Tensor 2.0). Nils: beide behalten, ergänzen und nach einem **trinitären dritten Faktor** suchen.

**Ziel:** Prüfen, ob es ein drittes System bzw. eine dritte Perspektive gibt, die A und B zu einer Dreiheit ergänzt, und welche Kandidaten es dafür in den Originalwerken gibt.

**Eingaben:** Tensor-Basics (Zenodo 19152183), Tensor 2.0 (privat, F1), Feldtheorie (19153910), Logik-Tensor 1.0 (19282895), interner MD-Korpus.

**Arbeitsschritte:**
1. Beschreibe A und B je in einem Satz: Was ordnet das System? Was ist seine Leitfrage?
2. Bestimme, was **keines** der beiden Systeme erfasst. Kandidaten: C (fachimmanente Trinitäten), G (formaler Träger), Ont/Op/Th (Beschreibungspflichten), Rel0/Rel-Rel/Rel1 (Seinsweisen).
3. Prüfe je Kandidat zwei Bedingungen und sammle einen möglichen Beleg:
   - **(a) Unabhängigkeit:** nicht aus A oder B ableitbar
   - **(b) Ergänzung:** schließt eine benannte Lücke
   - **(c) möglicher Quellenbeleg, keine Voraussetzung:** Beschreiben die Originalwerke A, B und den Kandidaten zusammen als Dreiheit? Ein fehlender Beleg schließt den Kandidaten nicht aus.
   - **Nullhypothese H0:** „Es gibt keinen trinitären dritten Faktor zu A und B.“ Prüfe ausdrücklich, was für H0 spricht. Ein Ergebnis „H0 nicht widerlegt“ ist gültig.
   - **Hinweis:** G (formaler 27er-Träger) ist ein mathematisches Objekt, kein semantischer Achsenkandidat. Prüfe G nur auf seine Rolle als Träger.
4. Suche Originalstellen, die einen solchen dritten Faktor nennen oder nahelegen, mit Fundstelle.
5. Gegenprobe: Zeige für jeden Kandidaten, was dagegen spricht.

**Ausgabe:** je Kandidat: `name | leitfrage | erfuellt (a/b) | moeglicher_beleg (c) | belegstellen | gegenargumente | empfehlung`; dazu ein Abschnitt **H0** mit Argumenten und Ergebnis.

**Regeln:** Keine Gleichsetzung von Feld-IDs; keine Umbenennung. Ein Kandidat darf auch scheitern. Die Entscheidung über die Aufnahme trifft Nils.

---

## P-NEU-05 · Originalthesen inventarisieren

**Ziel:** Alle als These formulierten Kernaussagen in den Originalwerken finden, **wörtlich** mit Fundstelle erfassen und den sechs thematischen Einstiegen auf `docs/thesen.html` zuordnen.

**Eingabe:** interner MD-Korpus (70 Werkversionen), `docs/thesen.html`.

**Arbeitsschritte:**
1. Suche Thesen-Signale: „These“, „Axiom“, „wir zeigen“, „ist die Grundlage“, „beweist“, „Gesetz“, „gilt universell“.
2. Erfasse je Fund: Werk, Version, DOI, Seite oder Zeile, Wortlaut (höchstens zwei Sätze), Art (Axiom, These, Hypothese, Behauptung mit Zahl).
3. Fasse wortgleiche oder sinngleiche Thesen über Versionen hinweg zusammen, mit Versionskette und ohne Wortlaut zu ersetzen.
4. Ordne jede These **beliebig vielen** Thesen-Einstiegen zu: `primary_topic`, `alternative_topics`, `claim_relevance` (`traegt_abschnitt`, `historischer_kontext`, `nur_intern`) oder `not_mapped`. Melde Einstiege ohne These (Unterdeckung).

**Ausgabe:** JSON nach `claim.schema.json` mit `aussageart: inhaltlich` und `evidenz.stufe: offen`. Der Quellenstatus ist `pruefung_ausstehend`, solange nur maschinell extrahiert wurde; `digital_verifiziert` erst nach **Sichtprüfung** der Fundstelle (`pruefmethode` enthält `sichtpruefung`). Dazu eine Zuordnungstabelle Thesen ↔ Einstiege (viele-zu-viele).

**Regeln:** Keine neuen kanonischen IDs in historische Dateien schreiben; IDs nur im neuen Register. Weitreichende numerische oder biologische Thesen gesondert kennzeichnen (KI-BIO-EVIDENCE).

**Abnahme:** Stichprobe von 10 Funden durch GPT gegen den Korpus geprüft.
