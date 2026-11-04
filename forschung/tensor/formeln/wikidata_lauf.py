#!/usr/bin/env python3
"""Harvesting-Test an einer offenen Datenbank: Wikidata-Formeln (CC0) → Ministrukturen, Hubs, Tensorkeime, Dreiecke. Owner: Claude.

Eingabe (NICHT im Repo, Rohdaten bleiben lokal):
  <ordner>/formeln_wikidata.json   {QID: {de, en, formeln:[TeX], symbole:[{symbol, groesse: QID}]}}
                                   geholt über wbgetentities: P2534 (definierende Formel), P7235 (Symbol) + Qualifikator P9758 (bedeutet)
  <ordner>/groessen_labels.json    {QID: {de, en}}
  <ordner>/abgerufen_am.txt        Abrufzeitpunkt
Ausgabe (aggregiert, ins Repo): WIKIDATA_LAUF_V0_1.json
Aufruf: python3 forschung/tensor/formeln/wikidata_lauf.py <ordner>     (benötigt sympy + antlr4 für parse_latex)
Ohne Ordner oder sympy: SKIP (Exit 77) – SKIP ist kein PASS.
"""
import collections
import importlib.util
import itertools
import json
import pathlib
import signal
import sys

if len(sys.argv) < 2 or not pathlib.Path(sys.argv[1]).is_dir():
    print("SKIP: Wikidata-Rohdaten nicht vorhanden (Ordner als Argument) – Exit 77")
    sys.exit(77)
try:
    import sympy as sp
    from sympy.parsing.latex import parse_latex
except ImportError:
    print("SKIP: sympy/parse_latex fehlt – Exit 77")
    sys.exit(77)

H = pathlib.Path(__file__).resolve().parent
W = H.parents[2]
spec = importlib.util.spec_from_file_location("fs", H / "formel_struktur.py")
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)
ORD = pathlib.Path(sys.argv[1])
F = json.loads((ORD / "formeln_wikidata.json").read_text(encoding="utf-8"))
L = json.loads((ORD / "groessen_labels.json").read_text(encoding="utf-8"))
ABRUF = (ORD / "abgerufen_am.txt").read_text().strip()

# Naturkonstanten und rein mathematische Objekte zählen nicht als Größe (Wikidata-QIDs)
KONSTANTEN_QID = {"Q2111": "Lichtgeschwindigkeit", "Q18373": "Gravitationskonstante", "Q122894": "Plancksches Wirkungsquantum",
                  "Q11663": "Boltzmann-Konstante", "Q6116": "elektrische Feldkonstante", "Q1515261": "magnetische Feldkonstante",
                  "Q182557": "Elementarladung", "Q167": "Kreiszahl π", "Q82435": "eulersche Zahl", "Q190524": "Avogadro-Konstante",
                  "Q182336": "Gaskonstante", "Q209350": "Stefan-Boltzmann-Konstante", "Q216215": "Faraday-Konstante",
                  "Q2122052": "Fallbeschleunigung (Norm)", "Q9415": "imaginäre Einheit"}


class Zeit(Exception):
    pass


def _alarm(*_):
    raise Zeit()


signal.signal(signal.SIGALRM, _alarm)


def mit_frist(fn, *a, sek=3):
    signal.alarm(sek)
    try:
        return fn(*a)
    finally:
        signal.alarm(0)


def label(q):
    x = L.get(q) or {}
    return x.get("de") or x.get("en") or q


def symbolname(tex):
    """TeX-Symbol → Name des Symbols, das parse_latex dafür erzeugt (für die Zuordnung Formel ↔ Größe)."""
    try:
        e = mit_frist(parse_latex, tex, sek=2)
    except BaseException:
        return None
    return str(e) if isinstance(e, sp.Symbol) else None


def main():
    stat = collections.Counter()
    eintraege = []
    for qid, it in F.items():
        stat["items"] += 1
        tex = next((f for f in it["formeln"] if "=" in f and "\\begin" not in f), None)
        groessen = {s["groesse"] for s in it["symbole"] if s.get("groesse")}
        variablen_q = sorted(g for g in groessen if g not in KONSTANTEN_QID)
        e = {"qid": qid, "name": it.get("de") or it.get("en") or qid, "groessen_q": variablen_q,
             "stelligkeit": len(variablen_q)}
        if tex is None:
            stat["ohne_gleichung"] += 1
            e["parse"] = "ohne_gleichung"
        else:
            try:
                eq = mit_frist(parse_latex, tex, sek=3)
                stat["geparst"] += 1
                e["parse"] = "ok"
                zuordnung = {}
                for s in it["symbole"]:
                    n = symbolname(s["symbol"])
                    if n and s.get("groesse"):
                        zuordnung[n] = s["groesse"]
                frei = {str(x) for x in eq.free_symbols}
                konst = [n for n, q in zuordnung.items() if q in KONSTANTEN_QID]
                vars_ = sorted(frei - set(konst))
                e["symbole_zugeordnet"] = len(frei & set(zuordnung)) / len(frei) if frei else 0.0
                try:
                    e["skelett"] = mit_frist(fs.skelett, eq, vars_, konst, sek=3) if len(vars_) <= 5 else None
                except BaseException:
                    e["skelett"] = None
                e["_eq"], e["_zuordnung"] = eq, zuordnung
            except BaseException:
                stat["parse_fehler"] += 1
                e["parse"] = "fehler"
        eintraege.append(e)

    # Familien gleicher Ministruktur
    fam = collections.defaultdict(list)
    for e in eintraege:
        if e.get("skelett"):
            fam[e["skelett"]].append(e["name"])
    familien = sorted(([len(v), v[:12]] for v in fam.values() if len(v) >= 2), key=lambda x: -x[0])

    # Trinitär: genau drei Größen (über die Symbolzuordnung von Wikidata, unabhängig vom Parser)
    tri = [e for e in eintraege if e["stelligkeit"] == 3]
    zaehl = collections.Counter(g for e in tri for g in e["groessen_q"])
    hubs = [[label(g), g, n] for g, n in zaehl.most_common(25)]

    # Keime: Dreiecke (jedes Paar teilt genau eine ANDERE Größe) und Sterne, über einen Nachbarschaftsgraphen
    nach_g = collections.defaultdict(set)
    for i, e in enumerate(tri):
        for g in e["groessen_q"]:
            nach_g[g].add(i)
    nachbarn = collections.defaultdict(set)
    for g, ids in nach_g.items():
        for a, b in itertools.combinations(sorted(ids), 2):
            nachbarn[a].add(b)
            nachbarn[b].add(a)
    dreiecke, sterne, gemischt = [], 0, 0
    for a in range(len(tri)):
        for b in (x for x in nachbarn[a] if x > a):
            for c in (x for x in nachbarn[a] & nachbarn[b] if x > b):
                A, B, C = (set(tri[i]["groessen_q"]) for i in (a, b, c))
                if not 6 <= len(A | B | C) <= 9:
                    continue
                ab, bc, ac = A & B, B & C, A & C
                if len(ab) == len(bc) == len(ac) == 1 and len(ab | bc | ac) == 3:
                    dreiecke.append((a, b, c, sorted(ab | bc | ac)))
                elif ab == bc == ac:
                    sterne += 1
                else:
                    gemischt += 1

    # Dreiecke ableiten (Elimination), soweit alle drei Formeln geparst und die Verbindungsgrößen zugeordnet sind
    abgeleitet = []
    for a, b, c, verb in dreiecke:
        es = [tri[i] for i in (a, b, c)]
        rec = {"formeln": [x["name"] for x in es], "qids": [x["qid"] for x in es], "verbindungen": [label(g) for g in verb]}
        if not all(x.get("parse") == "ok" for x in es):
            rec["ableitung"] = "nicht_geparst"
            abgeleitet.append(rec)
            continue
        try:
            polys, elim_alle = [], set()
            for x in es:
                ers = {sp.Symbol(n): sp.Symbol("G_" + q, positive=True) for n, q in x["_zuordnung"].items()}
                p = fs.ausdruck_null(x["_eq"]).subs(ers)
                p = sp.numer(sp.together(p))
                if any(not pw.exp.is_integer for pw in p.atoms(sp.Pow)):
                    raise ValueError("Wurzel")
                polys.append(sp.expand(p))
            ziel = [sp.Symbol("G_" + q, positive=True) for q in verb]
            if not all(any(z in p.free_symbols for p in polys) for z in ziel):
                raise ValueError("Zuordnung unvollständig")
            elim = ziel[:2]
            rest = sorted({s for p in polys for s in p.free_symbols} - set(elim), key=str)
            gb = mit_frist(lambda: sp.groebner(polys, *elim, *rest, order="lex"), sek=10)
            rel = [g for g in gb.exprs if not (g.free_symbols & set(elim))]
            kern = []
            for r in rel:
                _, fl = sp.factor_list(r)
                k = sp.Mul(*[f for f, _ in fl if not (f.is_Symbol or f.is_number)])
                if k != 1:
                    kern.append(k)
            namen = {str(s): label(str(s)[2:]) for r in kern for s in r.free_symbols if str(s).startswith("G_")}
            unzugeordnet = sorted({str(x) for r in kern for x in r.free_symbols if not str(x).startswith("G_")})
            rec["ableitung"] = ("ok_sauber" if not unzugeordnet else "ok_mit_unzugeordneten_symbolen") if kern else "keine_relation"
            rec["unzugeordnet"] = unzugeordnet
            rec["relation"] = [str(k) for k in kern][:3]
            rec["groessen"] = namen
            lesbar = []
            for k in kern:
                z = str(k)
                for sym in sorted(namen, key=len, reverse=True):
                    z = z.replace(sym, "[" + namen[sym] + "]")
                lesbar.append(z)
            rec["relation_lesbar"] = lesbar[:3]
        except BaseException as ex:
            rec["ableitung"] = f"abbruch: {type(ex).__name__}"
        abgeleitet.append(rec)

    # Wiederfindung gegen das 103er-Inventar: Achsen, von denen ≥ 2 Rollen als Wikidata-Größe (Label) vorkommen
    inv = json.loads((W / "docs/data/tensor-inventar-v10_7.json").read_text(encoding="utf-8"))["tensors"]
    alle_labels = {((L.get(q) or {}).get(s) or "").lower() for e in eintraege for q in e["groessen_q"] for s in ("de", "en")} - {""}
    rollen = [(t["id"], t["name"], a["n"], {x.lower() for x in a["elements"]}) for t in inv for a in t["axes"]]
    treffer = [{"tensor": tid, "name": n, "achse": ax, "rollen": sorted(r & alle_labels)} for tid, n, ax, r in rollen if len(r & alle_labels) >= 2]

    zus = {"items": stat["items"], "mit_gleichung": stat["items"] - stat["ohne_gleichung"], "geparst": stat["geparst"],
           "parse_fehler": stat["parse_fehler"],
           "parse_fehlerquote": round(stat["parse_fehler"] / max(1, stat["items"] - stat["ohne_gleichung"]), 3),
           "stelligkeit": dict(sorted(collections.Counter(e["stelligkeit"] for e in eintraege).items())),
           "trinitaer": len(tri), "familien_ab_2": len(familien), "groesste_familie": familien[0][0] if familien else 0,
           "keime": {"dreieck": len(dreiecke), "stern": sterne, "gemischt": gemischt},
           "dreiecke_abgeleitet": dict(collections.Counter(r["ableitung"].split(":")[0] for r in abgeleitet)),
           "wiederfindung_103": {"achsen_gesamt": len(rollen), "achsen_mit_2plus_rollen": len(treffer)}}
    out = {"schema_version": "wikidata-lauf/0.1", "owner": "claude",
           "quelle": "Wikidata (CC0), P2534 definierende Formel, P7235 Symbol, Qualifikator P9758 bedeutet", "abgerufen_am": ABRUF,
           "hinweis": "Rohdaten nicht im Repo; aggregierte Ergebnisse. Stelligkeit = Anzahl zugeordneter Größen ohne Naturkonstanten. "
                      "„Dreieck“ und „Ableitung“ sind Kandidaten; P1 (gleiche Rolle) ist NICHT automatisch geprüft.",
           "zusammenfassung": zus, "hubs": hubs, "familien": familien[:25],
           "dreiecke": abgeleitet, "wiederfindung_103": treffer}
    (H / "WIKIDATA_LAUF_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(zus, ensure_ascii=False, indent=1))
    print("Hubs:", hubs[:12])
    print("Familien:", [(n, v[:5]) for n, v in familien[:8]])
    for r in [r for r in abgeleitet if r["ableitung"] == "ok_sauber"][:40]:
        print(" ", " | ".join(r["formeln"]), "→", r["relation_lesbar"][0])
    print("Gesamt: OK")


if __name__ == "__main__":
    main()
