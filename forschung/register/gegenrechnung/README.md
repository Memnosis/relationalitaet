# Gegenrechnungen (Claude)

Unabhängige Nachprüfung fremder oder älterer Rechenbehauptungen. **Prüfstufe nach ACM Artifact Badges: „repliziert“**: eigener Code, Formeln aus der Primärquelle, nicht aus dem geprüften Material. Siehe `forschung/koordination/STANDARDS_KI_AUSTAUSCH_ANALYSE_V0_1.md`.

| ID | Gegenstand | Behauptung (Quelle) | Ergebnis | Befehl |
|---|---|---|---|---|
| GR-01 | 7 DLMF-Identitäten aus KI-Tensor v6.6: 1.2.1, 1.2.3, 1.2.4, 1.2.7, 5.5.1, 5.5.2, 5.12.1 | „7 symbolische Identitätsnachweise unter Annahmen“, Grenzfall 1.2.4 bei n=0 (Zweig `ki-tensor/no-loss-audit-2026-10-31`, `ki-tensor/audit/RELATIONSNACHWEISE_v6_6.md`) | **7/7 bestätigt** (symbolisch, numerisch mit 30 Stellen, Grenzfälle). Der Grenzfall n=0 → 1 ist bestätigt. Die Kontrollprobe (falsche Identität) wird erkannt. | `python3 forschung/register/gegenrechnung/dlmf_v6_6_gegenrechnung.py` (benötigt sympy) |

**Grenzen von GR-01:**
- Bestätigt ist, dass die DLMF-Identitäten unter den DLMF-Annahmen gelten. Das ist Lehrbuchwissen und wurde korrekt rekonstruiert.
- **Nicht** bestätigt ist ein Bezug zu Trinitäten oder Tensorachsen. Der Zweig selbst sagt: „0 neu validierte Trinitäten/Tensoren“, „5 rein thematische Matching-Treffer … keine Validierung einer Achse“.
- Bei der numerischen Prüfung von 5.12.1 gilt wegen Randsingularitäten der Quadratur eine Toleranz von 1e-15 (gemessen 1e-17 bis 1e-24).

Ergebnisakte: `DLMF_V6_6_GEGENRECHNUNG_ERGEBNIS.json` (sympy 1.13.3, mpmath-Version in der Datei).

**Nächste Kandidaten (je ein kleiner Schritt):**
- GR-02: Rückrechnungen REV-01 bis REV-08 (`VERIFIKATION_v4_5/4_6.md`)
- GR-03: die 16 Zahlenketten des Zweigs als Skript statt Handrechnung
