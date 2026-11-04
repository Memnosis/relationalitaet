#!/usr/bin/env python3
"""Dreieckskeime → abgeleitete Beziehung (Elimination) → die drei Prüfungen. Owner: Claude.

Ein Dreieckskeim besteht aus drei trinitären Formeln A, B, C, von denen jedes Paar genau eine ANDERE Größe teilt.
Werden die drei gemeinsamen Größen eliminiert (Gröbner-Basis, lexikographisch), bleibt im Erfolgsfall eine Relation
zwischen den drei übrigen Größen – eine „Überlagerung, die eine Beziehung ergibt“.
  P1 Aussageerhalt: Die gemeinsamen Größen sind fachlich DIESELBEN (gleiches Gebiet; bei Fachgrenzen: Rollenprüfung nötig)
  P2 neu im Bestand: Die abgeleitete Relation steht nicht schon als eigene Formel im Bestand
  P3 reproduzierbar: deterministische Elimination; zweite Ableitung über eine andere Eliminationsreihenfolge gleich
Aufruf: python3 forschung/tensor/formeln/dreiecke.py   (benötigt sympy)
"""
import importlib.util
import itertools
import json
import pathlib
import sys

try:
    import sympy as sp
except ImportError:
    print("SKIP: sympy fehlt – SKIP ist kein PASS (Exit 77)")
    sys.exit(77)

H = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("fs", H / "formel_struktur.py")
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)
d = json.loads((H / "FORMELN_TOP100_V0_1.json").read_text(encoding="utf-8"))
nach_id = {f["id"]: f for f in d["formeln"]}


def nach_bedeutung(f):
    """Formel mit Symbolen = Bedeutungsnamen, damit gleiche Größen über Formeln hinweg dasselbe Symbol sind."""
    eq = fs.parse(f["formel"], f["konstanten"])
    ers = {}
    for s in eq.free_symbols:
        name = str(s)
        if name in f["groessen"]:
            ers[s] = sp.Symbol(f["groessen"][name].replace(" ", "_"), positive=True)
        elif name in f["konstanten"] or name == "pi":
            ers[s] = sp.Symbol("k_" + name, positive=True)
    e = sp.numer(sp.together(fs.ausdruck_null(eq).subs(ers)))
    if any(not p.exp.is_integer for p in e.atoms(sp.Pow)):
        # Wurzeln entfernen (Quadrieren), damit die Elimination polynomial bleibt; Lösungsmenge für positive Größen gleich
        from sympy.solvers.solvers import unrad
        u = unrad(e)
        if u:
            e = u[0]
    return sp.expand(e)


def ableiten(ids, gemeinsam, reihenfolge=0):
    """Eliminiert die Größen `gemeinsam` (in gedrehter Reihenfolge) und gibt die eliminationsfreien Relationen zurück."""
    polys = [nach_bedeutung(nach_id[i]) for i in ids]
    elim = [sp.Symbol(g.replace(" ", "_"), positive=True) for g in gemeinsam]
    elim = elim[reihenfolge:] + elim[:reihenfolge]
    rest = sorted({s for p in polys for s in p.free_symbols} - set(elim), key=str)
    gb = sp.groebner(polys, *elim, *rest, order="lex")
    return [g for g in gb.exprs if not (g.free_symbols & set(elim))]


def kern(ausdruck):
    """Entfernt Faktoren, die nur eine einzelne (positive) Größe sind – sie verschwinden für positive Größen nie."""
    _, faktoren = sp.factor_list(ausdruck)
    rest = [f for f, _ in faktoren if not (f.is_Symbol or (f.is_number))]
    return sp.Mul(*rest) if rest else None


# Rollenprüfung bei Fachgrenzen (Einschätzung Claude, E1 – zur Gegenprüfung durch GPT/Nils): bedeuten gleichnamige Größen dasselbe?
ROLLENPRUEFUNG = {
    ("F044", "F080", "F081"): {"ergebnis": "spezialfall",
        "begruendung": "Dichte-Masse = Gesamtmasse eines Körpers, Stoffmenge-Masse = Masse eines Stoffs, Konzentration-Volumen = Lösungsvolumen. "
                       "Dieselbe Rolle nur für einen REINEN Stoff: dann gilt ρ = c·M (molare Dichte). Für Lösungen falsch."},
    ("F055", "F066", "F088"): {"ergebnis": "rollenkonflikt",
        "begruendung": "Länge = Pendellänge vs. Körpergröße, Masse = Zentralmasse vs. Körpermasse, Periode = Pendel- vs. Umlaufzeit. "
                       "Formal ableitbar, fachlich ohne Aussage (Scheinbeziehung durch gleiche Wörter)."},
}


def main():
    erg = [fs.analysiere(f) for f in d["formeln"]]
    b = fs.bestand(erg)
    mengen = {f["id"]: set(e["groessen"]) for f, e in zip(d["formeln"], erg)}
    ausgabe = []
    for k in b["dreiecke"]:
        gem = k["verbindungen"]
        # zwei der drei Verbindungsgrößen eliminieren (drei Wahlen) → Kernrelation; P3: alle Wahlen liefern dieselbe
        kerne = {}
        for paar in itertools.combinations(gem, 2):
            ks = {str(sp.expand(x)) for x in (kern(y) for y in ableiten(k["formeln"], list(paar))) if x is not None}
            ks2 = {str(sp.expand(x)) for x in (kern(y) for y in ableiten(k["formeln"], list(paar), 1)) if x is not None}
            kerne[" + ".join(paar)] = {"relationen": sorted(ks), "reihenfolge_stabil": ks == ks2}
        alle = [frozenset(v["relationen"]) for v in kerne.values()]
        p3 = len(set(alle)) == 1 and all(v["reihenfolge_stabil"] for v in kerne.values())
        relation = sorted(alle[0]) if p3 else sorted(set().union(*alle))
        groessen_rel = sorted({str(s).replace("_", " ") for r in relation for s in sp.sympify(r).free_symbols if not str(s).startswith("k_")})
        p1 = k["gleiches_gebiet"]
        schon = [i for i, m in mengen.items() if m == set(groessen_rel)]
        p2 = not schon
        rp = ROLLENPRUEFUNG.get(tuple(k["formeln"]))
        if not p1 and rp and rp["ergebnis"] == "spezialfall":
            p1 = "eingeschraenkt"
        if p1 is False:
            urteil = "unzulaessige_verknuepfung" if rp else "rollenpruefung_noetig"
        elif p1 == "eingeschraenkt":
            urteil = "spezialfall_gueltig" if (p2 and p3) else "spezialfall_unklar"
        elif not p3:
            urteil = "nicht_reproduziert"
        elif not p2:
            urteil = "bekannt_im_bestand"
        else:
            urteil = "neue_beziehung_im_bestand"
        ausgabe.append({"keim": k["namen"], "formeln": k["formeln"], "gemeinsame_groessen": gem,
                        "abgeleitet": relation, "groessen_der_ableitung": groessen_rel, "eliminationen": kerne,
                        "P1_aussageerhalt": p1,
                        "rollenpruefung": rp,
                        "P1_hinweis": None if p1 is True else "Fachgrenze: gleichnamige Größen haben verschiedene Rollen – Ableitung formal gültig, fachlich ohne Aussage",
                        "P2_neu_im_bestand": p2, "P2_vorhanden_in": schon, "P3_reproduzierbar": p3, "urteil": urteil,
                        "lesart": "„neu im Bestand“ heißt: nicht als eigene Formel unter den 100; es heißt NICHT neu für die Wissenschaft."})
    out = {"schema_version": "dreiecke/0.2", "owner": "claude", "quelle": "FORMELN_TOP100_V0_1.json",
           "verfahren": "Gröbner-Basis (lex), je zwei der drei Verbindungsgrößen eliminiert, Einzelgrößen-Faktoren entfernt", "ergebnisse": ausgabe}
    (H / "DREIECKE_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for a in ausgabe:
        print(f"{' – '.join(a['keim'])} {a['formeln']}\n   → {a['abgeleitet']}   P1 {a['P1_aussageerhalt']}  P2 {a['P2_neu_im_bestand']}  P3 {a['P3_reproduzierbar']}  ⇒ {a['urteil']}")
    print("Gesamt: OK")


if __name__ == "__main__":
    main()
