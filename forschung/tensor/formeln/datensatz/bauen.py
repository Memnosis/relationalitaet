#!/usr/bin/env python3
"""Baut den Formelbestand (Datensatz) aus dem Wikidata-Rohabruf.

Eingabe:  wikidata_roh.json (von abruf_wikidata.py)
Ausgabe (in diesen Ordner):
  formelbestand_v0_1.jsonl   eine Zeile je Formel: Kennung, Name, TeX, Symbole→Größen, Parse-Status,
                             maschinenlesbarer Ausdruck (Symbole als G_<QID> bzw. K_<QID>), Stelligkeit,
                             Exponentenvektor (falls Monom), Skelett-Kennung
  groessen_v0_1.json         Größen: Bezeichnungen, ISQ-Dimension (P4020), Konstante ja/nein, Vorkommen
  skelette_v0_1.json         Ministrukturen (kanonische Skelette) mit Häufigkeit
Aufruf: python3 bauen.py <pfad/wikidata_roh.json>      (benötigt sympy + antlr4-python3-runtime 4.11)
"""
import collections
import hashlib
import importlib.util
import json
import pathlib
import re
import signal
import sys

try:
    import sympy as sp
    from sympy.parsing.latex import parse_latex
except ImportError:
    print("SKIP: sympy/parse_latex fehlt – Exit 77")
    sys.exit(77)

H = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("fs", H.parent / "formel_struktur.py")
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)

KONSTANTEN_QID = {"Q2111", "Q18373", "Q122894", "Q11663", "Q6116", "Q1515261", "Q182557", "Q167", "Q82435", "Q190524",
                  "Q182336", "Q209350", "Q216215", "Q2122052", "Q9415", "Q173227", "Q2101", "Q12198", "Q1131101"}
RE_KONST = re.compile(r"[Kk]onstante|constant|Kreiszahl|Eulersche Zahl|imaginäre Einheit", re.I)


class Frist(Exception):
    pass


def _alarm(*_):
    raise Frist()


signal.signal(signal.SIGALRM, _alarm)


def mit_frist(fn, *a, sek=3):
    signal.alarm(sek)
    try:
        return fn(*a)
    finally:
        signal.alarm(0)


RE_HUELLE = re.compile(r"\\(?:boldsymbol|mathbf|vec|mathrm|text|mathit|operatorname|bm|mathsf|textrm|overrightarrow)\s*\{([^{}]*)\}")
RE_WEG = re.compile(r"\\(?:displaystyle|left|right|,|;|!|quad|qquad)(?![A-Za-z])")


def saeubern(tex):
    """Entfernt reine Satzauszeichnung (Fettdruck, Vektorpfeil, Textschrift, Abstände), damit Symbole einheitlich gelesen werden."""
    alt = None
    while alt != tex:
        alt, tex = tex, RE_HUELLE.sub(lambda m: m.group(1).replace(" ", ""), tex)
    tex = RE_WEG.sub(" ", tex).replace("\\dfrac", "\\frac").replace("\\tfrac", "\\frac")
    return tex.strip().rstrip(".,; ")


def ist_konstante(q, g):
    x = g.get(q) or {}
    return q in KONSTANTEN_QID or bool(RE_KONST.search((x.get("de") or "") + " " + (x.get("en") or "")))


def symbolname(tex, cache={}):
    if tex not in cache:
        try:
            e = mit_frist(parse_latex, tex, sek=2)
            cache[tex] = str(e) if isinstance(e, sp.Symbol) else None
        except BaseException:
            cache[tex] = None
    return cache[tex]


def exponenten(eq):
    """Für Gleichungen der Form Monom = Monom: Exponentenvektor {Symbol: Exponent}, sonst None."""
    if not isinstance(eq, sp.Equality):
        return None
    # Größenkalkül: dY/dX hat die Exponentenstruktur Y·X⁻¹ (gleiche Dimension, gleiche Bezugsstruktur)
    eq = eq.replace(lambda e: isinstance(e, sp.Derivative),
                    lambda e: e.expr / sp.Mul(*[v ** c for v, c in e.variable_count]))
    try:
        q = sp.powsimp(sp.expand_power_base(eq.lhs / eq.rhs, force=True), force=True)
    except Exception:
        return None
    vek = collections.Counter()
    for faktor in sp.Mul.make_args(q):
        if faktor.is_number:
            continue
        basis, exp = faktor.as_base_exp()
        if not isinstance(basis, sp.Symbol) or not exp.is_number:
            return None
        vek[str(basis)] += sp.nsimplify(exp)
    return {k: str(v) for k, v in vek.items() if v != 0} or None


def main():
    if len(sys.argv) < 2 or not pathlib.Path(sys.argv[1]).is_file():
        print("SKIP: wikidata_roh.json nicht angegeben – Exit 77")
        sys.exit(77)
    roh = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    G = roh["groessen"]
    vorkommen = collections.Counter()
    skelette = collections.defaultdict(list)
    zeilen = []
    for qid in sorted(roh["items"], key=lambda q: int(q[1:]) if q[1:].isdigit() else 0):
        it = roh["items"][qid]
        tex = next((f for f in it["formeln"] if "=" in f and "\\begin" not in f), None)
        zuord = {}
        for s in it["symbole"]:
            n = symbolname(saeubern(s["symbol"]))
            if n and s.get("groesse"):
                zuord.setdefault(n, s["groesse"])
                zuord.setdefault("d" + n, s["groesse"])  # Differential dQ wie Q
        gq = sorted({s["groesse"] for s in it["symbole"] if s.get("groesse")})
        var = [q for q in gq if not ist_konstante(q, G)]
        z = {"id": qid, "name_de": it.get("de"), "name_en": it.get("en"), "formel_tex": tex, "formeln_tex": it["formeln"],
             "symbole": it["symbole"], "groessen": var, "konstanten": [q for q in gq if q not in var],
             "stelligkeit": len(var), "trinitaer": len(var) == 3, "parse": None, "ausdruck": None,
             "exponenten": None, "skelett": None, "symbole_zugeordnet": None}
        for q in var:
            vorkommen[q] += 1
        if tex is None:
            z["parse"] = "ohne_gleichung"
        else:
            try:
                eq = mit_frist(parse_latex, saeubern(tex), sek=3)
                ers = {sp.Symbol(n): sp.Symbol(("K_" if ist_konstante(q, G) else "G_") + q) for n, q in zuord.items()}
                eq2 = eq.xreplace({s: ers.get(sp.Symbol(str(s)), s) for s in eq.atoms(sp.Symbol)})  # auch gebundene Variablen (dm/dV)
                frei = [str(s) for s in eq2.atoms(sp.Symbol)]
                z["parse"] = "ok"
                z["ausdruck"] = str(eq2)
                z["ausdruck_srepr"] = sp.srepr(eq2)  # verlustfrei wieder einlesbar: sympy.parse_expr / eval mit sympy-Namensraum
                z["symbole_zugeordnet"] = round(sum(f.startswith(("G_", "K_")) for f in frei) / len(frei), 3) if frei else 1.0
                ex = exponenten(eq2)
                if ex and all(k.startswith(("G_", "K_")) for k in ex):
                    z["exponenten"] = {k: v for k, v in ex.items() if k.startswith("G_")}
                vars_ = sorted(f for f in frei if not f.startswith("K_"))
                konst = sorted(f for f in frei if f.startswith("K_"))
                if len(vars_) <= 5:
                    try:
                        sk = mit_frist(fs.skelett, eq2, vars_, konst, sek=3)
                    except BaseException:
                        sk = None
                    if sk:
                        sid = "S" + hashlib.sha1(sk.encode()).hexdigest()[:8]
                        z["skelett"] = sid
                        skelette[sid].append(qid)
                        skelette[sid + "#text"] = sk
            except BaseException as ex:
                z["parse"] = "fehler"
                z["parse_fehler"] = type(ex).__name__
        zeilen.append(z)
    with (H / "formelbestand_v0_1.jsonl").open("w", encoding="utf-8") as f:
        for z in zeilen:
            f.write(json.dumps(z, ensure_ascii=False, sort_keys=True) + "\n")
    gr = {q: {"de": x.get("de"), "en": x.get("en"), "dimension": x.get("dimension"), "konstante": ist_konstante(q, G),
              "vorkommen": vorkommen.get(q, 0)} for q, x in sorted(G.items())}
    (H / "groessen_v0_1.json").write_text(json.dumps({"quelle": roh["quelle"], "abgerufen_am": roh["abgerufen_am"], "groessen": gr},
                                                     ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    sk = {k: {"skelett": skelette[k + "#text"], "anzahl": len(v), "formeln": v} for k, v in skelette.items() if not k.endswith("#text")}
    sk = dict(sorted(sk.items(), key=lambda kv: -kv[1]["anzahl"]))
    (H / "skelette_v0_1.json").write_text(json.dumps(sk, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    st = collections.Counter(z["parse"] for z in zeilen)
    print(f"Formeln {len(zeilen)} · Parse {dict(st)} · Monome {sum(1 for z in zeilen if z['exponenten'])} · "
          f"Größen {len(gr)} (mit Dimension {sum(1 for x in gr.values() if x['dimension'])}) · Skelette {len(sk)}")
    print("Gesamt: OK")


if __name__ == "__main__":
    main()
