#!/usr/bin/env python3
"""Musteranalyse über alle typisierten Pfade und Signaturen der veröffentlichten Tensoren. Owner: Claude.
Jede Mustervermutung wird einzeln mit Fallzahl n geprüft. Bei kleinem n ist ein Muster eine VERMUTUNG (Reifegrad E1/E2),
keine Regel. Mehr Tensoren (die 103 historischen) sind nötig, um Muster zu bestätigen oder zu widerlegen.
Aufruf: python3 forschung/tensor/algebra-claude/muster.py [--json]
"""
import collections
import importlib.util
import json
import pathlib
import sys

H = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("typalgebra", H / "typalgebra.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)
d = json.loads((H / "TENSOREN_PUBLIKATIONEN_V0_1.json").read_text(encoding="utf-8"))
ZENTRUM = "ZM-II-β"  # geometrische Mitte des 3×3×3-Würfels (mittlere Schicht, mittlere Klasse, mittlerer Modus)

# eindeutige typisierte Pfade (Tensor, Folge, Typ)
pfade = sorted({(t["id"], tuple(p["adressen"]), p["typ"]) for t in d["tensoren"] for p in t["pfade"] if p.get("typ")})
je_typ = collections.defaultdict(list)
for tid, seq, typ in pfade:
    je_typ[typ].append((tid, seq))


def k(a):
    return ta.zerlege(a)[1]


def s(a):
    return ta.zerlege(a)[2]


def m(a):
    return ta.zerlege(a)[0]


def pruefe(name, typ, bedingung, beschreibung):
    faelle = je_typ.get(typ, [])
    treffer = [f for f in faelle if bedingung(f[1])]
    return {"muster": name, "typ": typ, "beschreibung": beschreibung, "n": len(faelle), "erfuellt": len(treffer),
            "ausnahmen": [{"tensor": t, "pfad": list(q)} for t, q in faelle if (t, q) not in treffer],
            "status": "ohne_faelle" if not faelle else ("bestaetigt_im_korpus" if len(treffer) == len(faelle) else "teilweise")}


MUSTER = [
    pruefe("M1 Projektion entspringt NM-I-γ", "PRJ", lambda q: q[0] == "NM-I-γ", "Jede Projektion beginnt in Basis-Kern-Relation (latente Ganzheit)"),
    pruefe("M2 Projektion bleibt im Modus γ", "PRJ", lambda q: all(s(a) == "γ" for a in q), "Projektion ist eine Relationsbewegung"),
    pruefe("M3 Projektion endet in UM", "PRJ", lambda q: m(q[-1]) == "UM", "Projektion endet in der Identität"),
    pruefe("M4 Zyklus liegt ganz in Klasse II", "CYC", lambda q: all(k(a) == "II" for a in q), "Zyklus = Kreislauf-Klasse"),
    pruefe("M5 Zyklus geht durch die Würfelmitte ZM-II-β", "CYC", lambda q: ZENTRUM in q, "jeder Kreislauf passiert das Zentrum des Tensors"),
    pruefe("M6 Traversal liegt ganz in Klasse III", "TRV", lambda q: all(k(a) == "III" for a in q), "Traversal = Öffnungs-Klasse"),
    pruefe("M7 Reset endet in NM", "RST", lambda q: m(q[-1]) == "NM", "Reset führt in die Basis"),
    pruefe("M8 Reset wechselt die Klasse", "RST", lambda q: k(q[0]) != k(q[-1]), "Reset ist keine exakte Umkehr (vgl. Regel U)"),
    pruefe("M9 Rekonstruktion liegt in Klasse II", "REC", lambda q: all(k(a) == "II" for a in q), "Rekonstruktion im Kreislauf"),
]

# Signaturen gegen Pfade
sig_pruef = []
for t in d["tensoren"]:
    for sg in t.get("signaturen", []):
        ziel = {"HM": "T-HOLO", "ZM": "T-ZYKLUS", "LM": "T-LOGIK", "Bedeutungsformung": "T-BF"}.get(sg["name"], t["id"])
        tt = next((x for x in d["tensoren"] if x["id"] == ziel), None)
        typen_pfade = sorted({p["typ"] for p in (tt["pfade"] if tt else []) if p.get("typ")})
        ax_da = bool(sg["ax"]) and any(tuple(p["adressen"]) == tuple(sg["ax"]) for p in (tt["pfade"] if tt else []))
        sig_pruef.append({"signatur": sg["name"], "deklarierte_typen": sg["typen"], "typen_in_pfaden": typen_pfade,
                          "pfadtypen_nicht_in_signatur": sorted(set(typen_pfade) - set(sg["typen"])),
                          "signaturtypen_ohne_pfad": sorted(set(sg["typen"]) - set(typen_pfade)),
                          "ax": sg["ax"], "ax_als_pfad_belegt": ax_da if sg["ax"] else None, "quelle": t["id"]})

# Zentrums-Statistik: wie oft liegt welche Adresse auf typisierten Pfaden?
haeufig = collections.Counter(a for _, q, _ in pfade for a in q)
out = {"schema_version": "muster/0.1", "pfade_typisiert": len(pfade), "typen": {t: len(v) for t, v in sorted(je_typ.items())},
       "muster": MUSTER, "signaturen": sig_pruef, "haeufigste_adressen": haeufig.most_common(6),
       "hinweis": "Kleine Fallzahlen: Muster sind Vermutungen (E1/E2), bis die 103 historischen Tensoren geprüft sind."}
(H / "MUSTER_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
if "--json" in sys.argv:
    print(json.dumps(out, ensure_ascii=False, indent=1))
else:
    print("Typisierte Pfade:", out["pfade_typisiert"], out["typen"])
    for mu in MUSTER:
        print(f"{mu['muster']:48} {mu['erfuellt']}/{mu['n']}  {mu['status']}  {('Ausnahmen: ' + str([' → '.join(a['pfad']) + ' (' + a['tensor'] + ')' for a in mu['ausnahmen']])) if mu['ausnahmen'] else ''}")
    for sgp in sig_pruef:
        print(f"SIG[{sgp['signatur']}] deklariert {sgp['deklarierte_typen']} | in Pfaden {sgp['typen_in_pfaden']} | fehlt in SIG {sgp['pfadtypen_nicht_in_signatur']} | ohne Pfad {sgp['signaturtypen_ohne_pfad']} | AX belegt {sgp['ax_als_pfad_belegt']}")
    print("Häufigste Adressen auf Pfaden:", out["haeufigste_adressen"])
    print("Gesamt: OK")
