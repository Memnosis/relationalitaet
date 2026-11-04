#!/usr/bin/env python3
"""Konzept 2 · Identifikation und Reduktion von Formeln auf gemeinsame Ministrukturen, Triaden und Tensorkeime.
Owner: Claude. Auftrag Nils 04.11.2026.

Für jede Formel (SymPy-Gleichung):
  variablen   freie Größen ohne Konstanten (Zahlen, π, deklarierte Naturkonstanten)
  stelligkeit Anzahl der Variablen n
  trinitaer   n == 3: eine Relation verbindet genau drei Größen (Dreigrößengesetz)
  triadentyp  für n == 3: „potenzgesetz“ (z = k·x^a·y^b, log-linear), „additiv“ (linear), „nichtlinear“
  dynamik     enthält eine Zeitableitung (Differentialgleichung)
  skelett     Ministruktur: Gleichung mit Platzhaltern x0, x1, … statt Größen, Zahlen/Konstanten → k;
              über alle Umbenennungen minimiert → F = m·a, U = R·I, p = m·v haben dasselbe Skelett
Über den Bestand:
  familien    Formeln mit gleichem Skelett (gemeinsame Ministruktur über Fachgrenzen)
  hubs        Größen, die in ≥ 3 trinitären Formeln vorkommen
  tensorkeime drei trinitäre Formeln, paarweise über gemeinsame Größen verbunden, zusammen 6–9 Größen
              (Struktur „3 Achsen × 3 Rollen“, wie die 103 Gerüste) – KANDIDATEN, kein Tensorbeweis
              Form „stern“: alle Paare teilen dieselbe Größe; „dreieck“: jedes Paar teilt eine ANDERE Größe
              (geschlossene Trinität aus Trinitäten, z. B. Arbeit–Leistung–Geschwindigkeit über Arbeit, Zeit, Weg)
"""
import collections
import itertools
import json
import re

import sympy as sp

GENERISCH = {"Zeit", "Länge", "Fläche", "Volumen", "Konstante", "Abstand", "Radius", "time", "length", "area", "volume"}
NATURKONSTANTEN = {"c", "G", "h", "hbar", "kB", "eps0", "mu0", "sigma", "R", "F_", "H0", "b", "g"}


def parse(formel, konstanten=(), ist_latex=False):
    if ist_latex:
        from sympy.parsing.latex import parse_latex
        ausdruck = parse_latex(formel)
    else:
        ns = {name: sp.Symbol(name) for name in re.findall(r"[A-Za-z_]\w*", formel)
              if name not in {"Eq", "Derivative", "exp", "log", "sqrt", "sin", "cos", "pi", "I", "Rational"}}
        for fn in set(re.findall(r"([A-Za-z_]\w*)\(t\)", formel)):
            ns[fn] = sp.Function(fn)
        ns.update({"pi": sp.pi, "I": sp.I})
        ausdruck = sp.sympify(formel, locals=ns)
    return ausdruck


def variablen(eq, konstanten=()):
    k = set(konstanten) | {"pi"}
    sym = {s for s in eq.free_symbols if str(s) not in k}
    funcs = {f.func for f in eq.atoms(sp.Function) if isinstance(f.func, sp.core.function.UndefinedFunction)}
    namen = {str(s) for s in sym} | {str(f) for f in funcs}
    return sorted(namen)


def ausdruck_null(eq):
    if isinstance(eq, sp.Equality):
        return eq.lhs - eq.rhs
    return eq


def triadentyp(eq, vars_):
    """Klassifiziert eine Dreigrößenrelation: wird eine Variable explizit als Funktion der beiden anderen dargestellt?"""
    if len(vars_) != 3 or eq.atoms(sp.Derivative):
        return None
    e = ausdruck_null(eq)
    syms = {str(s): s for s in e.free_symbols}
    if not all(v in syms for v in vars_):
        return "implizit"
    for ziel in vars_:
        try:
            loes = sp.solve(e, syms[ziel])
        except Exception:
            continue
        if len(loes) != 1:
            continue
        g = loes[0]
        andere = [syms[v] for v in vars_ if v != ziel]
        X, Y = sp.symbols("X Y", real=True)
        gl = sp.expand_log(sp.log(g.subs({andere[0]: sp.exp(X), andere[1]: sp.exp(Y)})), force=True)
        if all(sp.simplify(sp.diff(gl, a, b)) == 0 for a, b in [(X, X), (Y, Y), (X, Y)]):
            return "potenzgesetz"
        if all(sp.simplify(sp.diff(g, a, b)) == 0 for a, b in [(andere[0], andere[0]), (andere[1], andere[1]), (andere[0], andere[1])]):
            return "additiv"
        return "nichtlinear"
    return "implizit"


def skelett(eq, vars_, konstanten=()):
    """Kanonische Ministruktur: Größen → x0.., Zahlen und Konstanten → k; minimal über Umbenennungen und Vorzeichen."""
    e = ausdruck_null(eq)
    konst = {s: sp.Symbol("k") for s in e.free_symbols if str(s) in set(konstanten) | {"pi"}}
    e = e.subs(konst)
    syms = [s for s in e.free_symbols if str(s) in vars_]
    funcs = sorted({f.func for f in e.atoms(sp.Function) if isinstance(f.func, sp.core.function.UndefinedFunction)}, key=str)
    if len(syms) + len(funcs) > 6:
        return None
    best = None
    for perm in itertools.permutations(range(len(syms))):
        ers = {s: sp.Symbol(f"x{perm[i]}") for i, s in enumerate(sorted(syms, key=str))}
        ers_f = {f: sp.Function(f"f{i}") for i, f in enumerate(funcs)}
        z = e.subs(ers)
        for f, g in ers_f.items():
            z = z.replace(f, g)
        for vz in (z, -z):
            s = re.sub(r"(?<![\w.])\d+(\.\d+)?(?![\w.])", "k", sp.srepr(sp.expand(vz)))
            if best is None or len(s) < len(best) or (len(s) == len(best) and s < best):
                best = s
    return best


def analysiere(eintrag, ist_latex=False):
    try:
        eq = parse(eintrag["formel"], eintrag.get("konstanten", []), ist_latex)
    except Exception as ex:
        return {"id": eintrag["id"], "fehler": f"parse: {type(ex).__name__}"}
    v = variablen(eq, eintrag.get("konstanten", []))
    erg = {"id": eintrag["id"], "name": eintrag.get("name"), "gebiet": eintrag.get("gebiet"),
           "variablen": v, "stelligkeit": len(v), "dynamik": bool(eq.atoms(sp.Derivative)),
           "trinitaer": len(v) == 3}
    try:
        erg["triadentyp"] = triadentyp(eq, v)
    except Exception:
        erg["triadentyp"] = "unbestimmt"
    try:
        erg["skelett"] = skelett(eq, v, eintrag.get("konstanten", []))
    except Exception:
        erg["skelett"] = None
    bed = eintrag.get("groessen", {})
    erg["groessen"] = sorted({bed.get(x, x) for x in v})
    return erg


def bestand(ergebnisse, inventar=None):
    ok = [e for e in ergebnisse if "fehler" not in e]
    fam = collections.defaultdict(list)
    for e in ok:
        if e.get("skelett"):
            fam[e["skelett"]].append(e["id"])
    familien = sorted(([k, v] for k, v in fam.items() if len(v) >= 2), key=lambda kv: -len(kv[1]))
    tri = [e for e in ok if e["trinitaer"] and len(e["groessen"]) == 3]
    zaehl = collections.Counter(g for e in tri for g in e["groessen"])
    hubs = [(g, n) for g, n in zaehl.most_common() if n >= 3]
    keime = []
    for a, b, c in itertools.combinations(tri, 3):
        A, B, C = set(a["groessen"]), set(b["groessen"]), set(c["groessen"])
        if A & B and B & C and A & C and 6 <= len(A | B | C) <= 9 and len({a["id"], b["id"], c["id"]}) == 3:
            verb = A & B | B & C | A & C
            fachlich = verb - GENERISCH
            gleiches_gebiet = len({a.get("gebiet"), b.get("gebiet"), c.get("gebiet")}) == 1
            ab, bc, ac = A & B, B & C, A & C
            form = "dreieck" if (len(ab) == len(bc) == len(ac) == 1 and len(ab | bc | ac) == 3) else ("stern" if ab == bc == ac else "gemischt")
            keime.append({"form": form, "formeln": [a["id"], b["id"], c["id"]], "namen": [a.get("name"), b.get("name"), c.get("name")],
                          "achsen": [a["groessen"], b["groessen"], c["groessen"]], "groessen": len(A | B | C),
                          "verbindungen": sorted(verb), "fachliche_verbindungen": sorted(fachlich),
                          "gleiches_gebiet": gleiches_gebiet, "stark": bool(fachlich) and gleiches_gebiet and len(fachlich) >= 2})
    keime.sort(key=lambda k: (-k["groessen"], k["formeln"]))
    wiederfindung = None
    if inventar:
        rollen = [(t["id"], t["name"], a["n"], {x.lower() for x in a["elements"]}) for t in inventar for a in t["axes"]]
        alle_g = {g.lower() for e in ok for g in e["groessen"]}
        treffer = [(tid, n, ax) for tid, n, ax, r in rollen if len(r & alle_g) >= 2]
        wiederfindung = {"achsen_gesamt": len(rollen), "achsen_mit_2plus_rollen_als_groesse": len(treffer),
                         "beispiele": [{"tensor": t, "name": n, "achse": ax} for t, n, ax in treffer[:15]]}
    return {"formeln": len(ergebnisse), "auswertbar": len(ok), "trinitaer": len(tri) if tri else sum(e["trinitaer"] for e in ok),
            "stelligkeit": dict(sorted(collections.Counter(e["stelligkeit"] for e in ok).items())),
            "triadentypen": dict(collections.Counter(e.get("triadentyp") for e in ok if e["trinitaer"])),
            "dynamik": sum(e["dynamik"] for e in ok), "familien": familien, "hubs": hubs,
            "tensorkeime": keime, "tensorkeime_anzahl": len(keime), "tensorkeime_stark": [k for k in keime if k["stark"]], "keimformen": dict(collections.Counter(k["form"] for k in keime)), "dreiecke": [k for k in keime if k["form"] == "dreieck"], "wiederfindung_103": wiederfindung}
