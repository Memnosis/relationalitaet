# Gegenrechnungen (Claude)

Unabhängige Nachprüfung fremder oder älterer Rechenbehauptungen. **Prüfstufe nach ACM Artifact Badges: „repliziert“**: eigener Code, Formeln aus der Primärquelle, nicht aus dem geprüften Material. Siehe `forschung/koordination/STANDARDS_KI_AUSTAUSCH_ANALYSE_V0_1.md`.

| ID | Gegenstand | Behauptung (Quelle) | Ergebnis | Befehl |
|---|---|---|---|---|
| GR-01 | 7 DLMF-Identitäten aus KI-Tensor v6.6: 1.2.1, 1.2.3, 1.2.4, 1.2.7, 5.5.1, 5.5.2, 5.12.1 | „7 symbolische Identitätsnachweise unter Annahmen“, Grenzfall 1.2.4 bei n=0 (Zweig `ki-tensor/no-loss-audit-2026-10-31`, `ki-tensor/audit/RELATIONSNACHWEISE_v6_6.md`) | **7/7 bestätigt** (symbolisch, numerisch mit 30 Stellen, Grenzfälle). Der Grenzfall n=0 → 1 ist bestätigt. Die Kontrollprobe (falsche Identität) wird erkannt. | `python3 forschung/register/gegenrechnung/dlmf_v6_6_gegenrechnung.py` (benötigt sympy) |

| GR-02 | Rückrechnungen REV-01 bis REV-08 aus KI-Tensor v4.5/v4.6 | REV-01–03 „symbolisch bestanden“; REV-04 nur mit positiven Parametern; REV-05 SIR geschlossen; REV-06 Normierung braucht Anfangsbedingung; REV-07 nur skalares Beispiel, kein Bellman-Beweis; REV-08 Spur 1 ⇏ PSD (`ki-tensor/audit/VERIFIKATION_v4_5.md`, `_v4_6.md`) | **8/8 bestätigt**, jeweils mit Grenzfall (Bedingung verletzt → scheitert bzw. Gegenbeispiel). **REV-04 nur unter Annahme:** Die Formel ist als Nernst-Gleichung rekonstruiert; das Original liegt im nicht synchronisierten Archiv v4.5. | `python3 forschung/register/gegenrechnung/rev_rueckrechnungen.py` (sympy) |
| GR-03 | 16 Zahlenketten des Zweigs (Bestände, Relationsakten, Feldadressen, Parser-Klassen) | Zahlen in `GESAMTSTAND_v4_2`, `CROSSWALK_v4_1/4_3`, `BESTANDSAUDIT`, `GLOSSAR_RELATION_TENSOR_v4_4`, `RELATIONSCOMPILER_v6_5`, `ALGEBRA_AUTOMATION_v6_4`, `DLMF_PARSER_v5_2_metrics.json`, `DLMF_PARSER_v5_6`, dazu `IMPORTAUDIT…` auf main | **16/16 stimmig**. Jeder benutzte Wert ist wörtlich in der Quelle belegt; das Skript liest die Dateien per `git show` direkt aus dem Zweig. | `python3 forschung/register/gegenrechnung/kt_zahlenketten.py` (ohne Zusatzpakete; im Reproduktionslauf) |

**Hinweise zu GR-03:**
- Die 16 Ketten sind die prüfbaren Summen und Produkte aus den Zweigberichten. Sie ersetzen die frühere Handrechnung (`ZWEIG_KI_TENSOR_TIEFENANALYSE_V0_1.md`, „16/16“) und sind nicht zwingend dieselbe Auswahl.
- ZK-13 deutet „342 inkl. Ergänzungen“ als 309 + 21 + 12. Diese Lesart stützt sich auf die Aufteilung in v6.5 und ist eine **Interpretation**.

**Grenzen von GR-01:**
- Bestätigt ist, dass die DLMF-Identitäten unter den DLMF-Annahmen gelten. Das ist Lehrbuchwissen und wurde korrekt rekonstruiert.
- **Nicht** bestätigt ist ein Bezug zu Trinitäten oder Tensorachsen. Der Zweig selbst sagt: „0 neu validierte Trinitäten/Tensoren“, „5 rein thematische Matching-Treffer … keine Validierung einer Achse“.
- Bei der numerischen Prüfung von 5.12.1 gilt wegen Randsingularitäten der Quadratur eine Toleranz von 1e-15 (gemessen 1e-17 bis 1e-24).

Ergebnisakte: `DLMF_V6_6_GEGENRECHNUNG_ERGEBNIS.json` (sympy 1.13.3, mpmath-Version in der Datei).

**Ergebnisakten:** `REV_GEGENRECHNUNG_ERGEBNIS.json`, `ZAHLENKETTEN_ERGEBNIS.json`.

**Gesamt (präzisiert 04.11. nach GPT-Gegenanalyse):**
- **GR-01 (7 Identitäten): ACM „repliziert“.** Eigener Code, Formeln aus der Primärquelle.
- **GR-02 (8 Rückrechnungen): „repliziert“ für die rekonstruierten Standardformen.** REV-04 bleibt ein **Quellenblocker**, bis die Originalformel aus Archiv v4.5 vorliegt.
- **GR-03 (16 Zahlenketten): nur „arithmetisch und am Text belegt“.** Geprüft ist, dass die Zahlen wörtlich in den Berichten stehen und zueinander passen, **nicht**, dass das zugrunde liegende Inventar diese Zahlen tatsächlich hat. Dafür bräuchte es die SQLite- und ZIP-Archive (F5).
- **Wissenschaftlicher Nettoertrag:** Bestätigt sind Lehrbuch-Identitäten, Umformungen und Bestandssummen, also **0 neue Relationen, Trinitäten oder Tensoren**. Der Wert liegt darin, dass die Zahlen und Rechnungen des Zweigs stimmen und zitierfähig sind.
- **SKIP ist kein PASS:** Fehlt `sympy` oder der Zweig, enden die Skripte mit Exit 77, und `reproduzieren.py` meldet UNVOLLSTÄNDIG (seit 04.11.).
