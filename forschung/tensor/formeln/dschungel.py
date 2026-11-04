#!/usr/bin/env python3
"""Trinitäten und Tensoren im Formelbestand: Katalog, Bezugsoperatoren, Bezugstensoren, Ergänzungen, Nullmodell.

Eingabe:  datensatz/formelbestand_v0_1.jsonl, datensatz/groessen_v0_1.json   (erzeugt von datensatz/bauen.py)
Ausgabe:  datensatz/trinitaeten_v0_1.csv, datensatz/bezugstensoren_v0_1.json, datensatz/ergaenzungen_v0_1.csv,
          DSCHUNGEL_ERGEBNIS_V0_1.json (Zusammenfassung)
Aufruf:   python3 forschung/tensor/formeln/dschungel.py [--permutationen N] [--datensatz ORDNER]      (nur Standardbibliothek)

Begriffe
  Trinität        Formel, die genau drei (nicht konstante) Größen verbindet.
  multiplikativ   Trinität der Form X^a · Y^b · Z^c = konst (Potenzgesetz); Signatur = |a|:|b|:|c| normiert.
  additiv         Trinität der Form X = ±Y ± Z (lineare Bilanz).
  Bezugskante     X → Y über K: aus einer multiplikativen Trinität mit Y = konst · K^s · X  (K „bezieht“ X auf Y).
  Bezugsoperator  Größe K, die viele Bezugskanten trägt (z. B. Masse: spezifisch → absolut).
  Zeile           X → Y über K1, X → Z über K3, Y → Z über K2; verträglich nur bei der Schließung
                  K3^s3 = K1^s1 · K2^s2 – einer Trinität zwischen den drei Operatoren, die im Bestand stehen muss.
  Bezugstensor    Operator-Schließung (K1, K2, K3) mit ≥ 2 Zeilen, von denen je ≥ 2 Kanten belegt sind: ein 3 × n-Gerüst, dessen Spalten
                  über die drei Operatoren ineinander übergehen und dessen Zyklus exakt zurückkehrt.
  Ergänzung       Zeile eines Bezugstensors, in der genau eine der drei Kanten im Bestand fehlt; sie folgt
                  algebraisch aus den beiden vorhandenen Kanten und der Schließung (Vorhersage einer Formel).
"""
import collections
import csv
import itertools
import json
import pathlib
import random
import re
import sys
from fractions import Fraction

H = pathlib.Path(__file__).resolve().parent
D = pathlib.Path(sys.argv[sys.argv.index("--datensatz") + 1]) if "--datensatz" in sys.argv else H / "datensatz"
AUS = H if D == H / "datensatz" else D
if not (D / "formelbestand_v0_1.jsonl").exists():
    print("SKIP: datensatz/formelbestand_v0_1.jsonl fehlt (erst datensatz/bauen.py) – Exit 77")
    sys.exit(77)
Z = [json.loads(l) for l in (D / "formelbestand_v0_1.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
GR = json.loads((D / "groessen_v0_1.json").read_text(encoding="utf-8"))["groessen"]
PERM = int(sys.argv[sys.argv.index("--permutationen") + 1]) if "--permutationen" in sys.argv else 200


def lab(q):
    x = GR.get(q) or {}
    return x.get("de") or x.get("en") or q


def q_aus(sym):
    return sym[2:] if sym.startswith("G_") else sym


# ---------- 1 Trinitäten klassifizieren ----------
RE_SYM = re.compile(r"\b([GK]_Q\d+|[A-Za-z]\w*)\b")
FUNKTIONEN = {"Eq", "Derivative", "log", "exp", "sqrt", "sin", "cos", "tan", "Sum", "Product", "Integral", "Limit", "Abs",
              "conjugate", "re", "im", "I", "pi", "E", "oo", "True", "False", "Rational", "Integer", "Float", "Symbol", "Mul",
              "Add", "Pow", "Function", "Tuple", "factorial", "atan", "asin", "acos", "sinh", "cosh", "tanh", "Max", "Min"}


def additiv(z):
    """X = ±Y ± Z: genau drei G-Symbole, keine weiteren freien Symbole, nur + und −, keine Produkte zwischen Größen."""
    a = z.get("ausdruck") or ""
    if not a.startswith("Eq(") or any(t in a for t in ("Derivative", "log", "exp", "**", "Sum", "Integral", "sqrt")):
        return False
    namen = set(RE_SYM.findall(a)) - FUNKTIONEN
    gs = {n for n in namen if n.startswith("G_")}
    if len(gs) != 3 or namen - gs - {n for n in namen if n.startswith("K_")}:
        return False
    rumpf = a[3:-1]
    return not re.search(r"G_Q\d+\s*[*/]\s*G_Q\d+", rumpf)


def signatur(ex):
    w = [abs(Fraction(v)) for v in ex.values()]
    m = min(w)
    return ":".join(str(x) for x in sorted(v / m for v in w))


trinitaeten = []
for z in Z:
    if not z["trinitaer"]:
        continue
    ex = z.get("exponenten") or {}
    if len(ex) == 3:
        typ, sig = "multiplikativ", signatur(ex)
    elif z["parse"] == "ok" and additiv(z):
        typ, sig = "additiv", "1:1:1 (Summe)"
    elif z["parse"] == "ok" and "Derivative" in (z.get("ausdruck") or ""):
        typ, sig = "dynamisch", None
    elif z["parse"] == "ok":
        typ, sig = "andere", None
    else:
        typ, sig = "nicht_gelesen", None
    trinitaeten.append({"id": z["id"], "name": z["name_de"] or z["name_en"], "groessen": [lab(q) for q in z["groessen"]],
                        "qids": z["groessen"], "typ": typ, "signatur": sig, "formel_tex": z["formel_tex"]})
typen = collections.Counter(t["typ"] for t in trinitaeten)
signaturen = collections.Counter(t["signatur"] for t in trinitaeten if t["typ"] == "multiplikativ")

# ---------- 2 Bezugskanten und Bezugsoperatoren ----------


def kanten_aus(formeln):
    """formeln: Liste (id, {qid: Fraction}) – liefert {(X, Y): {(K, s, id)}} für Y = konst · K^s · X."""
    k = collections.defaultdict(set)
    for fid, ex in formeln:
        if len(ex) != 3:
            continue
        for K in ex:
            X, Y = [q for q in ex if q != K]
            if ex[X] == -ex[Y]:
                a = ex[X]
                s = ex[K] / a
                # a·logX − a·logY + v_K·logK = 0  →  logY = logX + (v_K/a)·logK
                k[(X, Y)].add((K, s, fid))
                k[(Y, X)].add((K, -s, fid))
    return k


mult = [(z["id"], {q_aus(k): Fraction(v) for k, v in z["exponenten"].items()}) for z in Z
        if z.get("exponenten") and len(z["exponenten"]) == 3 and z["trinitaer"]]
KANTEN = kanten_aus(mult)
op_zaehl = collections.Counter()
for (X, Y), ks in KANTEN.items():
    for K, s, _ in ks:
        if X < Y:
            op_zaehl[K] += 1
operatoren = [{"operator": lab(K), "qid": K, "kanten": n} for K, n in op_zaehl.most_common(25)]

# ---------- 3 Bezugstensoren: Operator-Schließung (eine Trinität im Bestand) + Zeilen aus Bezugskanten ----------


def tensoren(formeln, kanten):
    """Für jede multiplikative Trinität W(K1, K2, K3) als Schließung: alle Zeilen (X, Y, Z), in denen mindestens zwei
    der drei Kanten X–Y (über K1), X–Z (über K3), Y–Z (über K2) im Bestand stehen und mit W verträglich sind."""
    schl = collections.defaultdict(list)          # Operatorpaar → [(Formel-ID, Vektor)]
    for fid, w in formeln:
        if len(w) == 3:
            for a, b in itertools.permutations(w, 2):
                schl[(a, b)].append((fid, w))
    aus = collections.defaultdict(list)
    for (X, Y), ks in kanten.items():
        for K, s, f in ks:
            aus[X].append((Y, K, s, f))
    zeilen = collections.defaultdict(dict)       # Schließungs-ID → {frozenset(X,Y,Z): Eintrag}
    for X, liste in aus.items():
        for (Y, K1, s1, f1), (Zq, K3, s3, f3) in itertools.permutations(liste, 2):
            if Y == Zq or K1 == K3 or f1 == f3 or {K1, K3} & {X, Y, Zq}:
                continue
            for wid, w in schl.get((K1, K3), ()):
                if wid in (f1, f3):
                    continue
                lam = w[K3] / s3
                if w[K1] != -lam * s1:
                    continue
                K2 = next(k for k in w if k not in (K1, K3))
                if K2 in (X, Y, Zq):
                    continue
                s2 = -w[K2] / lam
                # logZ − logY = s3·logK3 − s1·logK1 = s2·logK2   (Schließung W)
                vorhanden = [f for (K, s, f) in kanten.get((Y, Zq), ()) if K == K2 and s == s2]
                key = frozenset((X, Y, Zq))
                alt = zeilen[wid].get(key)
                eintrag = {"X": X, "Y": Y, "Z": Zq, "K1": K1, "K2": K2, "K3": K3, "s2": s2,
                           "formeln": [f1, f3] + vorhanden[:1], "vollstaendig": bool(vorhanden)}
                if alt is None or (eintrag["vollstaendig"] and not alt["vollstaendig"]):
                    zeilen[wid][key] = eintrag
    return zeilen


ZEILEN = tensoren(mult, KANTEN)
mult_d = dict(mult)
bezugstensoren = []
for wid, zs in sorted(ZEILEN.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    w = mult_d[wid]
    voll = sum(1 for e in zs.values() if e["vollstaendig"])
    bezugstensoren.append({
        "schliessung_formel": wid, "operatoren": [lab(k) for k in w], "operator_qids": list(w),
        "schliessung": " · ".join(f"[{lab(k)}]^{v}" for k, v in w.items()) + " = konst",
        "anzahl_zeilen": len(zs), "zeilen_vollstaendig": voll,
        "zeilen": [{"groessen": [lab(e["Y"]), lab(e["X"]), lab(e["Z"])], "qids": [e["Y"], e["X"], e["Z"]],
                    "ueber": [lab(e["K1"]), lab(e["K3"]), lab(e["K2"])], "formeln": e["formeln"],
                    "vollstaendig": e["vollstaendig"]} for e in zs.values()]})
bezugstensoren = [t for t in bezugstensoren if t["anzahl_zeilen"] >= 2]

# ---------- 4 Ergänzungen: unvollständige Zeilen → vorhergesagte Formel Z = konst · K2^s2 · Y ----------
ergaenzungen = []
gesehen = set()
for t in bezugstensoren:
    for wid in [t["schliessung_formel"]]:
        for e in ZEILEN[wid].values():
            if e["vollstaendig"]:
                continue
            k = (e["Y"], e["Z"], e["K2"])
            if k in gesehen or (e["Z"], e["Y"], e["K2"]) in gesehen:
                continue
            gesehen.add(k)
            # „parallel“: Y und Z sind beide über ihre EIGENE definierende Formel auf dieselbe Basis X bezogen
            # (z. B. spezifische und molare Wärmekapazität aus C) – Rollen stabil; sonst „kette“ – Rollenprüfung nötig
            art = "parallel" if set(e["formeln"][:2]) == {e["Y"], e["Z"]} else "kette"
            ergaenzungen.append({"tensor": t["schliessung"], "von": lab(e["Y"]), "nach": lab(e["Z"]), "ueber": lab(e["K2"]),
                                 "exponent": str(e["s2"]), "art": art, "von_qid": e["Y"], "nach_qid": e["Z"], "ueber_qid": e["K2"],
                                 "abgeleitet_aus": f"{e['formeln'][0]}, {e['formeln'][1]}, Schließung {wid}"})

# ---------- 5 Dimensionsprüfung (ISQ-Dimension P4020, falls vorhanden) ----------
BASIS = {"L": 0, "M": 1, "T": 2, "I": 3, "Θ": 4, "\\Theta": 4, "N": 5, "J": 6}
RE_DIM = re.compile(r"\\mathsf\s*\{\s*(\\Theta|[LMTINJΘ])\s*\}\s*(?:\^\s*\{?\s*(-?\s*\d+(?:/\d+)?)\s*\}?)?")


def dimension(q):
    d = (GR.get(q) or {}).get("dimension")
    if not d:
        return None
    v = [Fraction(0)] * 7
    if re.fullmatch(r"1|(?:[LMTINJΘ](?:\^-?\d+(?:/\d+)?)?\s*)+", d.strip()):   # normierte Form „L^2 M T^-3“
        for b, e in re.findall(r"([LMTINJΘ])(?:\^(-?\d+(?:/\d+)?))?", d):
            v[BASIS[b]] += Fraction(e) if e else 1
        return v
    gefunden = False
    for b, e in RE_DIM.findall(d):
        v[BASIS[b]] += Fraction(e.replace(" ", "")) if e else 1
        gefunden = True
    if not gefunden and not re.search(r"\b1\b|dimensionless", d):
        return None
    return v


def dim_konsistent(ex):
    ds = {q: dimension(q) for q in ex}
    if any(v is None for v in ds.values()):
        return None
    return all(sum(Fraction(ex[q]) * ds[q][i] for q in ex) == 0 for i in range(7))


dim_formeln = collections.Counter()
dim_inkonsistent = []
for z in Z:
    # nur vollständig gelesene Potenzgesetze: alle Symbole zugeordnet, alle Größen im Exponentenvektor
    if z.get("exponenten") and not z["konstanten"] and z.get("symbole_zugeordnet") == 1.0 and len(z["exponenten"]) == z["stelligkeit"]:
        r = dim_konsistent({q_aus(k): v for k, v in z["exponenten"].items()})
        dim_formeln[{True: "konsistent", False: "inkonsistent", None: "ohne_dimension"}[r]] += 1
        if r is False:
            dim_inkonsistent.append({"id": z["id"], "name": z["name_de"] or z["name_en"], "formel_tex": z["formel_tex"]})
for e in ergaenzungen:
    # vorhergesagte Kante: nach = konst · ueber^s · von – Dimension prüfen über beide Vorzeichen
    r = dim_konsistent({e["nach_qid"]: Fraction(1), e["von_qid"]: Fraction(-1), e["ueber_qid"]: -Fraction(e["exponent"])})
    e["dimension"] = {True: "konsistent", False: "inkonsistent", None: "ohne_dimension"}[r]
dim_erg = collections.Counter(e["dimension"] for e in ergaenzungen)

# ---------- 6 Nullmodell: Größen-Etiketten zufällig vertauschen (Häufigkeit und Exponentenmuster bleiben) ----------


def zaehle(formeln):
    t = tensoren(formeln, kanten_aus(formeln))
    return (sum(1 for v in t.values() for e in v.values() if e["vollstaendig"]) // 1,
            sum(1 for v in t.values() if len(v) >= 3))


beob = zaehle(mult)
rng = random.Random(20261104)
slots = [q for _, ex in mult for q in ex]
null = []
for _ in range(PERM):
    rng.shuffle(slots)
    it = iter(slots)
    neu = []
    for fid, ex in mult:
        werte = list(ex.values())
        qs = [next(it) for _ in werte]
        if len(set(qs)) == 3:
            neu.append((fid, dict(zip(qs, werte))))
    null.append(zaehle(neu))


def stat(i):
    xs = [n[i] for n in null]
    mu = sum(xs) / len(xs)
    sd = (sum((x - mu) ** 2 for x in xs) / max(1, len(xs) - 1)) ** 0.5
    p = (1 + sum(x >= beob[i] for x in xs)) / (1 + len(xs))
    return {"beobachtet": beob[i], "null_mittel": round(mu, 2), "null_sd": round(sd, 2), "null_max": max(xs),
            "z": round((beob[i] - mu) / sd, 1) if sd else None, "p_empirisch": round(p, 4), "permutationen": len(xs)}


nullmodell = {"vollstaendige_zeilen": stat(0), "bezugstensoren_ab_3_zeilen": stat(1)}

# ---------- Ausgabe ----------
with (D / "trinitaeten_v0_1.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "name", "typ", "signatur", "groesse_1", "groesse_2", "groesse_3", "qids", "formel_tex"])
    for t in sorted(trinitaeten, key=lambda t: (t["typ"], t["signatur"] or "", t["name"] or "")):
        g = (t["groessen"] + ["", "", ""])[:3]
        w.writerow([t["id"], t["name"], t["typ"], t["signatur"] or "", *g, " ".join(t["qids"]), t["formel_tex"] or ""])
(D / "bezugstensoren_v0_1.json").write_text(json.dumps(bezugstensoren, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
with (D / "ergaenzungen_v0_1.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tensor", "von", "nach", "ueber", "exponent", "art", "dimension", "abgeleitet_aus", "von_qid", "nach_qid", "ueber_qid"])
    for e in ergaenzungen:
        w.writerow([e["tensor"], e["von"], e["nach"], e["ueber"], e["exponent"], e["art"], e["dimension"], e["abgeleitet_aus"], e["von_qid"], e["nach_qid"], e["ueber_qid"]])

parse = collections.Counter(z["parse"] for z in Z)
zus = {"formeln": len(Z), "parse": dict(parse), "trinitaeten": len(trinitaeten), "trinitaeten_anteil": round(len(trinitaeten) / len(Z), 3),
       "trinitaetstypen": dict(typen.most_common()), "signaturen_multiplikativ": dict(signaturen.most_common(12)),
       "bezugskanten": sum(len(v) for v in KANTEN.values()) // 2, "bezugsoperatoren_top": operatoren[:12],
       "bezugstensoren_ab_2_zeilen": len(bezugstensoren),
       "bezugstensoren_ab_3_zeilen": sum(1 for t in bezugstensoren if t["anzahl_zeilen"] >= 3),
       "zeilen_gesamt": sum(t["anzahl_zeilen"] for t in bezugstensoren),
       "zeilen_vollstaendig": sum(t["zeilen_vollstaendig"] for t in bezugstensoren),
       "ergaenzungen": len(ergaenzungen), "ergaenzungen_art": dict(collections.Counter(e["art"] for e in ergaenzungen)), "ergaenzungen_dimension": dict(dim_erg), "dimension_formeln": dict(dim_formeln),
       "nullmodell": nullmodell, "dimension_inkonsistent": dim_inkonsistent}
meta = json.loads((D / "groessen_v0_1.json").read_text(encoding="utf-8"))
(AUS / "DSCHUNGEL_ERGEBNIS_V0_1.json").write_text(json.dumps({"schema_version": "dschungel/0.1", "quelle": meta.get("quelle"),
    "abgerufen_am": meta.get("abgerufen_am"), "zusammenfassung": zus,
    "beispiele_multiplikativ": [t for t in trinitaeten if t["typ"] == "multiplikativ"][:40],
    "beispiele_additiv": [t for t in trinitaeten if t["typ"] == "additiv"][:25],
    "bezugstensoren_top": bezugstensoren[:25], "ergaenzungen_top": ergaenzungen[:60]}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(zus, ensure_ascii=False, indent=1))
for t in bezugstensoren[:15]:
    print(f"\n[{t['anzahl_zeilen']} Zeilen, {t['zeilen_vollstaendig']} vollständig] {t['schliessung']}  ({t['schliessung_formel']})")
    for z in t["zeilen"][:6]:
        print("    ", " | ".join(z["groessen"]), "  über", z["ueber"], "✓" if z["vollstaendig"] else "○")
print("\nErgänzungen:", [(e["von"], "→", e["nach"], "über", e["ueber"], e["dimension"]) for e in ergaenzungen[:15]])
print("Gesamt: OK")
