# Website-P0: Didaktik, Design und Anschluss an die Forschungsarbeit
**Datum:** 03.11.2026 · **Zyklus:** KI-2026-11-03-001 · **Bearbeiter:** Website-GPT  
**Fachliches Regelwerk:** [Gemeinsamer Design-/Textstandard](../koordination/DESIGN_TEXT_PUBLIKATIONSSTANDARD_V1_2026-11-03.md) (Claude-Gegenprüfung angefordert).
**Status:** Dateien committet und statisch geprüft; Website-Browser-, GitHub-Pages-Auslieferungs-, Tastatur-/Screenreader-Abnahme noch nicht nachgewiesen. Mobile bewusst nachrangig, flexible Kartenlayoutregeln beibehalten.

## 1. Tatsächlich ausgeführte Änderungen
| P0-Arbeit | Datei | Vorheriger SHA | Commit | Ergebnis |
|---|---|---|---|---|
| Designgrammatik v1 | `docs/assets/tensor-learning-modules.css` | `1642a5c0499193af4b5fdd28fc08b01d2f839c1e` | `4306cb7c2670fa94929bdfc579db7cf77ccedc23` | serifenlose Box-/Kartenregeln, drei Lesetiefen, kleine gemeinsame Sprite-Icons, gerahmte Nachweisdiagramme und semantische Tabellen |
| WEB-B02-04 (Didaktik) | `docs/tensoralgebra.html` | `782b1945dd235f4d377e2ba96f1deabcfee6feb3` | `0b56bbbc9ce8e05a2752414f09af0ab667869d53` | Zusatz „einfach / vergleichen / Fachnachweis“; Gegenbeispiel ℤ₂₇ gegenüber (ℤ₃)³, keine Änderungen an bisherigen Fach- und Promptabschnitten |
| WEB-B02-07 (Lernnavigation) | `docs/index.html` | `0f244976ca496cff333c944bc77324a26df2ac3e` | `a9883e90f8b596028289e29ca2ffae280fd5efaa` | eigenständiger Lernpfad zu Grundlagen, Logik, Algebra, Quellen und Mitmachen; bisherige Startseitenkarten erhalten |
| WEB-B02-06 (Erklärung) | `docs/mitmachen.html` | `82fb236b8ec3e7d46d93751e653b80ad58b21977` | `8c46960afeb11e2246d6ef7d3ea73cac5dd353bd` | drei Lesetiefen getrennt von Prompt-, Agenten- und Meta-Funktionen; kein neues öffentliches KI-Rohpromptpaket erzeugt |
| WEB-B02-06 (Deep-Link) | `docs/mitmachen.html` | späterer Zwischenstand | `56a67e996ed96f29fd163286c20e47eb51afda8b`, `93aa5394341356173b392a613eac837d4f227b17` | bislang fehlenden `#WEB-PAPER-01`-Anker als Forschungsfrage eingefügt; semantisches `<ol>` nachgezogen, keinen ungetesteten Prompt als fertig behauptet |

## 2. Aktueller statischer Nachtest anhand GitHub-Inhalten
- Geprüfte Seiten: `index.html`, `tensor-einfuehrung.html`, `tensor-paper.html`, `tensoralgebra.html`, `bibliothek.html`, `mitmachen.html`. Neues CSS und bestehendes Sprite ebenfalls gegen GitHub abgerufen.
- Sieben prüfbare Modulanker: `forschung-lernen`, `tensor-grundlagen-heute`, `logik-forschungsstand`, `algebra-lernpfad`, `quellen-pruefweg`, `mitmach-verstehen-pruefen`, `WEB-PAPER-01` **vorhanden**.
- **27** interne Fachseiten-Ankerreferenzen über diese sechs Seiten kontrolliert; keine festgestellten defekten statischen Anker.
- **5** Referenzen auf `HARV-05`, `WEB-GLOS-01`, `WEB-CODE-01` sind **dynamisch**; das Live-Verhalten hängt von `MITMACH_TASKS.json` und erfolgreichem Netzwerkabruf ab. Register-IDs gegen `forschung/website/MITMACH_TASKS.json` geprüft, alle drei vorhanden. Diese fünf Links sind **nicht** als statischer Browser-Erfolg gezählt.
- Alle sechs Seiten enthalten genau **ein** `tensor-hierarchy.js`-Skript.
- Das SVG-Sprite enthält die verwendeten Symbole `education` und `compass`; keine dekorativen Stockbilder eingebaut.
- In den sechs überprüften HTML-Seiten keine expliziten `Georgia`-/`Times New Roman`-/Serifenschriftanweisungen erkannt. Die neue CSS-Komponente definiert einen ausdrücklich serifenlosen Font-Stack.
- Die vorherigen `algebra-weiterentwickeln`- und `prompt-ebenen`-Anker sind geblieben. Die Änderungen an `index.html`, `tensoralgebra.html` und zunächst `mitmachen.html` erfolgten als additive CSS-/Abschnittseinfügungen.
- Das bekannte Risiko von 16 potenziellen Navigationskonflikten im Integrationszweig wurde **nicht** durch unkontrolliertes Zusammenführen verschärft; Navigation nicht bearbeitet.

## 3. Designentscheidungen und fachliche Grenzen
**Wesentlich:** Ein Text wird nicht für das Layout künstlich gekürzt. Stufe 1 erklärt allgemeinverständlich, Stufe 2 differenziert Varianten, Stufe 3 enthält Nachweise, Gegenmodelle und formale Bedingungen. Die drei Leser-Stufen sind ausdrücklich *nicht* identisch mit den operativen Schichten Prompt/Agent/Meta. Für PDF/Word/Markdown gelten die im gemeinsamen Standard dokumentierten separaten Produktions- und Prüfregeln.

**Nächste P0-Gefahr:** Auf `mitmachen.html` wird aus einem öffentlich zugänglichen JSON-Register derzeit `meta_prompt` angezeigt. Die dort vorhandenen Statusangaben `prompt-vorbereitet` sind **kein dokumentierter erfolgreicher Prompt-Test**. Vor einem öffentlichen Release neuer Aufgaben soll Claude/GPT mit Nils klären, welche Prompttexte fachlich extern freigegeben sind, welche in wirklich privaten Arbeitsraum gehören und wie das öffentliche Register ohne Informationsverlust reduziert wird. Ein UI-Ausblenden allein entfernt keine Rohdaten aus dem öffentlichen JSON.

## 4. Claudes Gegenprüfung angefordert
Claude prüft diese Git-Versionen nach W01 (Bestand), W04 (Didaktik), W05 (Semantik), W06 (Evidenz), W07 (Prompt-Ebenen), W09 (Design) und X01 (Kommunikation). Im Revier Claude bleiben Datenbestände, wissenschaftliche Promptentwicklung und der Quell-/Claimabgleich. GPT erstellt Website-/Text-Komponenten; der 3×3×3-Achsen-Crosswalk ist keine vom Webteam zu beschließende neue Fachaxiomatik.

## 5. Offene Abnahmen und nächster Schritt
- tatsächliches Deployment und Desktop-Browserlayout inklusive Fokus, Tabellen, CSS-Kontrast kontrollieren (nicht im statischen Test enthalten);
- Peer-Review von Claude gegen die neuen SHAs;
- den mehrstufigen Promptfreigabe- und Rückgabeprozess im öffentlichen Mitmachregister korrigieren, ohne Originaldaten zu löschen oder interne Rohprompts öffentlich auszuweiten;
- vor einer Navigation-Fusion Entscheidungsvorlage für die beiden Systeme und den geplanten Bestandsschutz.

**Zyklus 001 bleibt offen.** Dieser Änderungsbericht ist eine Website-Lieferung, kein beidseitig bestätigter Abschluss.
