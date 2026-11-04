#!/usr/bin/env python3
"""Typisierte Tensoralgebra v0.1 · Owner: Claude · Auftrag Nils 04.11.2026.

Leitsatz (Nils): „Nicht alle Tensoren einfach miteinander multiplizieren. Zuerst eine typisierte Algebra, in der nur
kompatible Verknüpfungen zugelassen werden. Drei Prüfungen verbindlich: Erhält eine Verknüpfung die fachliche Aussage?
Entsteht eine neue mathematische Beziehung? Lässt sich diese Beziehung unabhängig reproduzieren?“

TYPEN (aus Tensor Basics, DOI 10.5281/zenodo.19152183, Abschnitte 9–13)
  Adresse   (M, K, S), M ∈ {NM, ZM, UM} (Basiszustand, geordnet), K ∈ {I, II, III} (Klasse), S ∈ {α, β, γ} (Modus)
  Feld      Adresse → Fachbegriff (+ Quelle)          – Fachaussage, KEIN mathematisches Objekt
  Pfad      Folge von Adressen mit deklariertem Typ τ ∈ {PRJ, RST, CYC, REC, …} oder ohne Typ
  Tensor    (id, Felder, Pfade, Quelle)

GEOMETRISCHE SIGNATUR eines Pfades (aus der Lage auf der M-Achse, ρ = M+1, ρ⁻¹ = M−1):
  auf   – M steigt bei jedem Schritt um 1   (ρ-Kette; verträglich mit PRJ und REC)
  ab    – M fällt bei jedem Schritt          (ρ⁻¹-Kette; verträglich mit RST)
  schicht – M konstant                       (innerhalb einer Schicht; verträglich mit CYC)
  gemischt – sonst

TYPREGELN (nur kompatible Verknüpfungen)
  T1 Ein deklarierter Typ muss seine Regel erfüllen (REGELN v0.2, aus dem Gebrauch des Autors), sonst: Typkonflikt.
  T2 Dieselbe Adressfolge mit zwei Typen: Konflikt nur, wenn einer davon seine Regel verletzt; sonst Hinweis „Mehrfachtyp“.
  T3 Verkettung p∘q nur, wenn Ende(p) = Anfang(q) und beide typverträglich sind.
  T4 Tensorvergleich nur auf dem gemeinsamen Träger (Adressen, die beide belegen).

OPERATIONEN
  vergleich(T1, T2)  → gleich | spezialfall | variante | unabhaengig | unvertraeglich   (über die typisierten Pfadmengen)
  Beziehungsart Hysterese: ρ-Kette (auf) gefolgt von ρ⁻¹-Kette (ab) gleicher Länge, die nicht zum Start zurückführt
                          ⇒ ρ⁻¹∘ρ ≠ id; Rückkehr in andere Klasse und/oder anderen Modus.
  ueberlagerung(T1, T2) → Kandidaten für neue Beziehungen: Verkettungen p∘q mit p aus T1, q aus T2, die in keinem der
                          beiden Tensoren allein vorkommen (z. B. PRJ∘RST = geschlossener Umlauf).

DREI VERBINDLICHE PRÜFUNGEN je Ergebnis
  P1 Aussageerhalt: Jeder beteiligte Pfad ist im Quelltensor so deklariert, typverträglich (T1/T2) und die Feldbegriffe
     an allen beteiligten Adressen sind belegt und bleiben unverändert (mit Quelle) erhalten.
  P2 Neue Beziehung: Das Ergebnis ist in keinem Tensor des GESAMTBESTANDS (inkl. eigener Verkettungshüllen) enthalten.
  P3 Reproduzierbarkeit: deterministisch (Hash gleich bei vertauschter Eingabe) – Stufe „eigen“; „unabhängig“ erst,
     wenn die andere KI denselben Hash mit eigenem Lauf erhält.

WICHTIGE GRENZE: Alle Fachtensoren teilen denselben 27-Adressen-Träger. „Gleiche Mathematik“ heißt hier deshalb
„gleiche typisierte Pfadstruktur“. Die Feldbegriffe tragen die Fachbedeutung, sind aber nicht Teil der Algebra.
"""
import hashlib
import itertools
import json

M = {"NM": 0, "ZM": 1, "UM": 2}
# Typregeln v0.2 – aus dem Gebrauch des Autors abgeleitet (v0.1 „CYC = innerhalb einer Schicht“ war falsch: in Logik,
# Feldtheorie und Soziation 1.9 steht CYC stets für Pfade ganz in Klasse II = Kreislauf). Konsistenz siehe typ_konsistenz().
REGELN = {
    "PRJ": lambda seq: signatur(seq) == "auf" and len({zerlege(a)[2] for a in seq}) == 1,   # ρ-Kette, Modus konstant
    "RST": lambda seq: signatur(seq) == "ab",                                                # ρ⁻¹-Kette
    "CYC": lambda seq: all(zerlege(a)[1] == "II" for a in seq),                              # ganz im Kreislauf (Klasse II)
    "REC": lambda seq: signatur(seq) in ("auf", "ab"),                                       # Rekonstruktion: gerichtete Kette
}
REGEL_TEXT = {"PRJ": "M steigt, Modus konstant", "RST": "M fällt", "CYC": "alle Adressen in Klasse II", "REC": "M steigt oder fällt"}


def zerlege(a):
    m, k, s = a.split("-")
    return m, k, s


def signatur(seq):
    ms = [M[zerlege(a)[0]] for a in seq]
    d = [b - a for a, b in zip(ms, ms[1:])]
    if all(x == 1 for x in d):
        return "auf"
    if all(x == -1 for x in d):
        return "ab"
    if all(x == 0 for x in d):
        return "schicht"
    return "gemischt"


def typpruefung(tensor):
    """T1/T2: liefert Liste der Typkonflikte eines Tensors."""
    konflikte = []
    je_folge = {}
    for p in tensor["pfade"]:
        seq, typ = tuple(p["adressen"]), p.get("typ")
        sig = signatur(seq)
        if typ and typ in REGELN and not REGELN[typ](seq):
            konflikte.append({"regel": "T1", "pfad": list(seq), "typ": typ, "signatur": sig, "verlangt": REGEL_TEXT[typ]})
        if typ:
            je_folge.setdefault(seq, set()).add(typ)
    for seq, typen in je_folge.items():
        if len(typen) > 1 and not all(REGELN.get(x, lambda s: True)(seq) for x in typen):
            konflikte.append({"regel": "T2", "pfad": list(seq), "typen": sorted(typen)})
    return konflikte


def mehrfachtypen(tensor):
    """Gleiche Folge mit mehreren, jeweils regelkonformen Typen: zulässig, aber zu klären (Hinweis, kein Konflikt)."""
    je = {}
    for p in tensor["pfade"]:
        if p.get("typ"):
            je.setdefault(tuple(p["adressen"]), set()).add(p["typ"])
    return [{"pfad": list(s), "typen": sorted(t)} for s, t in je.items() if len(t) > 1]


def typ_konsistenz(tensoren):
    """Wie konsistent verwendet der Autor jeden Pfadtyp über alle Werke? (Belege je Typ: erfüllt/gesamt)"""
    out = {}
    for t in tensoren:
        for p in t["pfade"]:
            typ = p.get("typ")
            if typ in REGELN:
                o = out.setdefault(typ, {"erfuellt": 0, "gesamt": 0, "abweichend": []})
                o["gesamt"] += 1
                if REGELN[typ](p["adressen"]):
                    o["erfuellt"] += 1
                else:
                    o["abweichend"].append({"tensor": t["id"], "pfad": p["adressen"]})
    return out


def pfadmenge(tensor):
    """Typisierte Pfade als Menge (Folge, Typ oder abgeleitete Signatur)."""
    out = set()
    for p in tensor["pfade"]:
        seq = tuple(p["adressen"])
        out.add((seq, p.get("typ") or "~" + signatur(seq)))
    return out


def nur_folgen(pm):
    return {s for s, _ in pm}


def huelle(tensor):
    """Eigene Verkettungshülle: alle Verkettungen deklarierter Pfade desselben Tensors (eine Stufe)."""
    ps = [tuple(p["adressen"]) for p in tensor["pfade"]]
    h = set(ps)
    for p, q in itertools.product(ps, repeat=2):
        if p[-1] == q[0] and p != q:
            h.add(p + q[1:])
    return h


def vergleich(t1, t2):
    k1, k2 = typpruefung(t1), typpruefung(t2)
    a, b = pfadmenge(t1), pfadmenge(t2)
    fa, fb = nur_folgen(a), nur_folgen(b)
    if not fa or not fb:
        return {"klasse": "unbestimmt", "grund": "mindestens ein Tensor ohne deklarierte Pfade", "typkonflikte": k1 + k2}
    gemeinsam = fa & fb
    varianten = []
    for p, q in itertools.product(fa, fb):
        if p != q and len(p) == len(q) and p[0] == q[0] and sum(x != y for x, y in zip(p, q)) == 1 and signatur(p) == signatur(q):
            varianten.append({"t1": list(p), "t2": list(q)})
    if fa == fb:
        klasse = "gleich"
    elif fa < fb:
        klasse = "spezialfall_t1_in_t2"
    elif fb < fa:
        klasse = "spezialfall_t2_in_t1"
    elif varianten:
        klasse = "variante"
    elif gemeinsam:
        klasse = "teilweise_gleich"
    else:
        klasse = "unabhaengig"
    if k1 or k2:
        klasse = klasse + "+typkonflikt"
    return {"klasse": klasse, "gemeinsame_pfade": sorted(map(list, gemeinsam)), "varianten": varianten,
            "typkonflikte": k1 + k2}


def ueberlagerung(t1, t2):
    """Kandidaten neuer Beziehungen durch typverträgliche Verkettung über Tensorgrenzen; mit P1–P3."""
    kand = []
    k1 = {tuple(k["pfad"]) for k in typpruefung(t1)}
    k2 = {tuple(k["pfad"]) for k in typpruefung(t2)}
    h1, h2 = huelle(t1), huelle(t2)
    for (x, tx, kx, hx), (y, ty, ky, hy) in [((t1, "t1", k1, h1), (t2, "t2", k2, h2)), ((t2, "t2", k2, h2), (t1, "t1", k1, h1))]:
        for p in x["pfade"]:
            for q in y["pfade"]:
                ps, qs = tuple(p["adressen"]), tuple(q["adressen"])
                if ps[-1] != qs[0] or ps == qs:
                    continue
                neu = ps + qs[1:]
                # P1 Aussageerhalt
                p1_typ = ps not in kx and qs not in ky
                p1_felder = all(a in x["felder"] for a in ps) and all(a in y["felder"] for a in qs)
                p1 = p1_typ and p1_felder
                # P2 neue Beziehung
                p2 = neu not in hx and neu not in hy and neu not in {tuple(z["adressen"]) for z in x["pfade"] + y["pfade"]}
                geschlossen = neu[0] == neu[-1]
                # Umkehrbarkeit: ist q die exakte Rückwärtsfolge von p? Wenn eine ρ-Kette (auf) von einer ρ⁻¹-Kette (ab)
                # gefolgt wird, die NICHT zum Start zurückführt, ist ρ⁻¹∘ρ ≠ id (Hysterese: Rückkehr in andere Klasse/Modus).
                sig_p, sig_q = signatur(ps), signatur(qs)
                hysterese = sig_p == "auf" and sig_q == "ab" and len(ps) == len(qs) and qs != ps[::-1]
                abweichung = None
                if hysterese:
                    s0, e0 = zerlege(neu[0]), zerlege(neu[-1])
                    abweichung = {"start": neu[0], "ende": neu[-1], "klasse": [s0[1], e0[1]], "modus": [s0[2], e0[2]]}
                kand.append({"verkettung": list(neu), "aus": [x["id"], y["id"]],
                             "typen": [p.get("typ") or "~" + signatur(ps), q.get("typ") or "~" + signatur(qs)],
                             "geschlossener_umlauf": geschlossen, "hysterese": hysterese, "hysterese_abweichung": abweichung,
                             "P1_aussageerhalt": p1, "P1_detail": {"typ_ok": p1_typ, "felder_belegt": p1_felder},
                             "P2_neu": p2})
    uniq = {json.dumps(k, sort_keys=True, ensure_ascii=False): k for k in kand}
    return sorted(uniq.values(), key=lambda k: (k["verkettung"], k["aus"]))


def kanon(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def lauf(tensoren):
    """Alle Paare: Vergleich + Überlagerung + P3 (Determinismus über vertauschte Reihenfolge)."""
    ergebnisse = []
    huellen = {t["id"]: huelle(t) for t in tensoren}
    for t1, t2 in itertools.combinations(sorted(tensoren, key=lambda t: t["id"]), 2):
        v = vergleich(t1, t2)
        u = ueberlagerung(t1, t2)
        v_rev = vergleich(t2, t1)
        u_rev = ueberlagerung(t2, t1)
        p3 = kanon(sorted(json.dumps(k, sort_keys=True, ensure_ascii=False) for k in u)) == kanon(sorted(json.dumps(k, sort_keys=True, ensure_ascii=False) for k in u_rev)) \
            and v["klasse"].split("+")[0].replace("t1_in_t2", "X").replace("t2_in_t1", "X") == v_rev["klasse"].split("+")[0].replace("t1_in_t2", "X").replace("t2_in_t1", "X")
        for k in u:
            k["P3_reproduzierbar"] = "eigen" if p3 else "NEIN"
            # P2 streng: neu gegenüber dem GESAMTBESTAND (Hüllen aller Tensoren), nicht nur gegenüber den zwei Eingaben
            schon = [t["id"] for t in tensoren if tuple(k["verkettung"]) in huellen[t["id"]]]
            k["P2_neu_korpus"] = k["P2_neu"] and not schon
            k["bereits_enthalten_in"] = schon
            k["gilt_als_neue_beziehung"] = k["P1_aussageerhalt"] and k["P2_neu_korpus"] and p3
        ergebnisse.append({"paar": [t1["id"], t2["id"]], "vergleich": v, "ueberlagerung": u, "P3_deterministisch": p3})
    return ergebnisse


def achsen_pruefung(achsen):
    """Strukturregel A1 (Achsenunabhängigkeit, Anlass GPT-Befund FACH-F054): Zwei Achsen eines Tensors dürfen nicht
    dieselbe Rollenfolge tragen; sonst sind M, K, S nicht unabhängig und das 27er-Gitter fällt auf weniger Felder zusammen.
    Rückgabe: Liste der Verstöße (leer = in Ordnung). Ein Verstoß ist ein Warnsignal, kein Beweis eines Fachfehlers."""
    norm = [tuple(r.strip().lower() for r in a["rollen"]) for a in achsen]
    out = []
    for i, j in itertools.combinations(range(len(norm)), 2):
        if norm[i] == norm[j]:
            out.append({"regel": "A1", "achsen": [achsen[i]["dimension"], achsen[j]["dimension"]], "rollen": list(achsen[i]["rollen"]),
                        "folge": "Felder (x, y, z) und (z, y, x) fallen inhaltlich zusammen; effektiv höchstens 18 statt 27 unterscheidbare Felder"})
        elif set(norm[i]) & set(norm[j]):
            out.append({"regel": "A1-teil", "achsen": [achsen[i]["dimension"], achsen[j]["dimension"]], "gemeinsam": sorted(set(norm[i]) & set(norm[j]))})
    return out
