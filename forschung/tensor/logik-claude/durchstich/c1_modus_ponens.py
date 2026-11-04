#!/usr/bin/env python3
"""Wissenschaftlicher Durchstich C1 · „Die trinitäre Deduktion ersetzt den klassischen Modus ponens“
(Logik-Tensor 1.0, S. 20, Abschnitt 9.3; CLM-LOGIK10-MODUS-PONENS). Owner: Claude. Plan v0.3, P1-1.

Formalisierung so wörtlich wie möglich (Zitate in C1_MODUS_PONENS.md):
  Ausdruck  = (inhalt, schicht, modus) mit schicht ∈ {Rel0, RelRel, Rel1}, modus ∈ {α, β, γ}
  ρ         : Rel0 → RelRel, RelRel → Rel1            („Überführt … aus Rel0 in Rel-Rel bzw. aus Rel-Rel in Rel1“)
  ρ⁻¹       : Rel1 → Rel0                             („Führt eine manifeste Form (Rel1) zurück in … (Rel0)“)
  Regel TD  : für A in Rel0 mit Modus α:  A ⊢ ρ(A),  ρ(A) ⊢ ρ²(A),  ρ²(A) ⊢ ρ⁻¹(ρ²(A))
              (Lesart L1: „ρ⁻¹(A)“ im Text als ρ⁻¹ der manifesten Form; die wörtliche Lesart ρ⁻¹(A) mit A in Rel0
               ist nach der eigenen Definition von ρ⁻¹ nicht typisiert → Befund T1)

Geprüft wird die übliche Bedeutung von „ersetzt den Modus ponens“: Die Regel leistet dasselbe Schließen,
d. h. aus Prämissen folgen dieselben Inhalte. Gegenstand ist NUR diese Lesart (Scope), nicht die ontologische These.

Aufruf: python3 forschung/tensor/logik-claude/durchstich/c1_modus_ponens.py [--json]
"""
import itertools
import json
import sys

SCHICHTEN = ("Rel0", "RelRel", "Rel1")


def imp(a, b):
    return ("->", a, b)


def rho(x):
    inhalt, schicht, modus = x
    if schicht == "Rel0":
        return (inhalt, "RelRel", modus)
    if schicht == "RelRel":
        return (inhalt, "Rel1", modus)
    return None  # ρ auf Rel1 im Text nicht definiert


def rho_inv(x):
    inhalt, schicht, modus = x
    return (inhalt, "Rel0", modus) if schicht == "Rel1" else None  # nur auf Rel1 definiert


def td_schritte(x):
    """Alle in einem Schritt mit der trinitären Deduktion (Lesart L1) ableitbaren Ausdrücke."""
    out = set()
    inhalt, schicht, modus = x
    if schicht == "Rel0" and modus == "α":
        out.add(rho(x))
    if schicht == "RelRel":
        out.add(rho(x))
    if schicht == "Rel1":
        r = rho_inv(x)
        if r:
            out.add(r)
    return {y for y in out if y}


def mp_schritte(menge, nur_schicht=None):
    """Modus ponens: aus φ und φ→ψ folgt ψ (optional nur innerhalb einer Schicht, Lesart L2: MP im Vollzug)."""
    out = set()
    for (a, sa, ma), (b, sb, mb) in itertools.product(menge, repeat=2):
        if isinstance(b, tuple) and b[0] == "->" and b[1] == a and sa == sb and ma == mb:
            if nur_schicht is None or sa == nur_schicht:
                out.add((b[2], sa, ma))
    return out


def huelle(start, mit_td=True, mp=None, max_runden=50):
    m = set(start)
    for _ in range(max_runden):
        neu = set()
        if mit_td:
            for x in m:
                neu |= td_schritte(x)
        if mp is not None:
            neu |= mp_schritte(m, nur_schicht=mp if mp != "alle" else None)
        if neu <= m:
            break
        m |= neu
    return m


def inhalte(m):
    return {x[0] for x in m}


ergebnisse = {}

# T1 Typisierung: wörtlich „ρ²(A) ⊢ ρ⁻¹(A)“ mit A in Rel0
A = ("p", "Rel0", "α")
ergebnisse["T1_woertlich_rho_inv_auf_A_typisiert"] = rho_inv(A) is not None  # erwartet False → Unschärfe im Text

# T2 Zyklus schließt sich: ρ⁻¹(ρ²(A)) = A
ergebnisse["T2_zyklus_schliesst"] = rho_inv(rho(rho(A))) == A

# T3 Invariante: TD erzeugt nie einen neuen Inhalt (erschöpfend über alle Startmengen aus einem kleinen Universum)
atome = ["p", "q", "r"]
formeln = atome + [imp(a, b) for a in atome for b in atome if a != b]
universum = [(f, s, m) for f in formeln for s in SCHICHTEN for m in ("α", "β", "γ")]
invariante = True
geprueft = 0
for k in (1, 2, 3):
    for start in itertools.combinations(universum, k):
        geprueft += 1
        if not inhalte(huelle(start, mit_td=True)) <= inhalte(start):
            invariante = False
            break
ergebnisse["T3_td_erzeugt_nie_neuen_inhalt"] = invariante
ergebnisse["T3_gepruefte_startmengen"] = geprueft

# T4 Gegenbeispiel: Γ = {p, p→q} in Rel0/α. Klassisch folgt q, mit TD allein nicht.
G = {("p", "Rel0", "α"), (imp("p", "q"), "Rel0", "α")}
ergebnisse["T4_klassisch_q_ableitbar"] = "q" in inhalte(huelle(G, mit_td=False, mp="alle"))
ergebnisse["T4_td_allein_q_ableitbar"] = "q" in inhalte(huelle(G, mit_td=True, mp=None))

# T5 Kontrolle (Lesart L2): MP nur im Vollzug (RelRel) + TD → q wird ableitbar und durchläuft den Zyklus
H = huelle(G, mit_td=True, mp="RelRel")
ergebnisse["T5_mp_im_vollzug_plus_td_q_ableitbar"] = "q" in inhalte(H)
ergebnisse["T5_q_in_allen_schichten"] = all(("q", s, "α") in H for s in SCHICHTEN)

# T6 Kontrollprobe des Prüfers: dieselbe Invariantenprüfung (T3) mit einer absichtlich kaputten Regel,
#    die neuen Inhalt erzeugt, MUSS die Verletzung finden – sonst wäre T3 wertlos.
def huelle_mit(regel, start, runden=10):
    m = set(start)
    for _ in range(runden):
        neu = set().union(*(regel(x) for x in m)) if m else set()
        if neu <= m:
            break
        m |= neu
    return m
kaputte_regel = lambda x: td_schritte(x) | {(imp(x[0], x[0]), x[1], x[2])}  # erzeugt φ→φ: neuer Inhalt
verstoss_gefunden = any(not inhalte(huelle_mit(kaputte_regel, [u])) <= inhalte([u]) for u in universum)
ergebnisse["T6_pruefer_erkennt_inhaltsaenderung"] = verstoss_gefunden

erwartet = {"T1_woertlich_rho_inv_auf_A_typisiert": False, "T2_zyklus_schliesst": True, "T3_td_erzeugt_nie_neuen_inhalt": True,
            "T4_klassisch_q_ableitbar": True, "T4_td_allein_q_ableitbar": False, "T5_mp_im_vollzug_plus_td_q_ableitbar": True,
            "T5_q_in_allen_schichten": True, "T6_pruefer_erkennt_inhaltsaenderung": True}
ok = all(ergebnisse[k] == v for k, v in erwartet.items())
urteil = {
    "claim": "CLM-LOGIK10-MODUS-PONENS",
    "lesart_geprueft": "„ersetzt“ = leistet dasselbe inhaltliche Schließen wie der Modus ponens",
    "science": "contradicted_with_scope" if ok else "inconclusive",
    "kurz": "Die trinitäre Deduktion ist eine einstellige Schichtregel: Sie bewegt einen Ausdruck durch Rel0 → Rel-Rel → Rel1 → Rel0, ändert aber nie seinen Inhalt (T3). Aus {p, p→q} folgt mit ihr allein nicht q (T4). Sie ersetzt den Modus ponens daher nicht. Verträglich ist die Lesart L2: Inhaltliches Schließen (z. B. Modus ponens) findet im Vollzug Rel-Rel statt, und die trinitäre Bewegung trägt das Ergebnis durch alle Schichten (T5).",
    "reifegrad": "E2 (eigene Probe); E3 erst nach Gegenprüfung durch GPT",
    "belegart": "D (formale Ableitung im Modell)",
}
if "--json" in sys.argv:
    print(json.dumps({"schema_version": "durchstich/0.1", "ergebnisse": ergebnisse, "erwartet": erwartet, "alle_wie_erwartet": ok, "urteil": urteil}, ensure_ascii=False, indent=1))
else:
    for k, v in ergebnisse.items():
        e = erwartet.get(k)
        print(f"{'OK ' if e is None or v == e else 'ABW'} {k}: {v}")
    print("Urteil:", urteil["science"], "·", urteil["reifegrad"])
    print("Gesamt:", "OK" if ok else "FEHLER")
sys.exit(0 if ok else 1)
