#!/usr/bin/env python3
"""Reproducible 50-equation pilot. Trusted repo input ONLY: sympify is not a sandbox.
Run from repo root: python3 forschung/tensor/formeln/pilot50/run50.py
Requires SymPy; results printed as JSON, no paper/register mutations.
"""
import itertools
import json
import pathlib
import re
import sys
try:
    import sympy as s
except ImportError:
    sys.exit("SKIP: SymPy missing, no scientific PASS")
root = pathlib.Path(__file__).resolve().parent
source = json.loads((root / "FORMELN50_KORPUS_V0_1.json").read_text(encoding="utf8"))
data = source["formeln"]
assert len(data) == 50 and len({x["id"] for x in data}) == 50
def parse(expr):
    names = set(re.findall(r"\b[A-Za-z_]\w*\b", expr))
    system = {"Eq","Derivative","exp","log","sqrt","sin","cos","pi","I","Rational"}
    namespace = {n:s.Symbol(n) for n in names-system}
    for n in set(re.findall(r"([A-Za-z_]\w*)\(t\)",expr))-system:
        namespace[n] = s.Function(n)
    namespace.update(Eq=lambda a,b:s.Eq(a,b,evaluate=False),
        Derivative=s.Derivative,exp=s.exp,log=s.log,sqrt=s.sqrt,
        sin=s.sin,cos=s.cos,pi=s.pi,I=s.I,Rational=s.Rational)
    return s.sympify(expr,locals=namespace,evaluate=False)
records=[]
for f in data:
    keys=set(re.findall(r"\b[A-Za-z_]\w*\b",f["formel"]))
    roles={k:v for k,v in f["groessen"].items() if k in keys and k not in f["konstanten"]}
    try:
        eq=parse(f["formel"])
        assert isinstance(eq,s.Equality)
        status="parsed"
    except Exception as ex:
        status="parse_failed: "+str(ex)
    records.append({"id":f["id"],"symbol_count":len(roles),
        "labels":sorted(set(roles.values())),"parse_status":status,
        "domain_status":"not_reviewed"})
tri=[r for r in records if r["symbol_count"]==3]
shared={}
for a,b in itertools.combinations(tri,2):
    labels=sorted(set(a["labels"])&set(b["labels"]))
    if labels: shared[(a["id"],b["id"])]=labels
patterns=[]
for a,b,c in itertools.combinations(tri,3):
    pairs=[(a["id"],b["id"]),(a["id"],c["id"]),(b["id"],c["id"])]
    if not all(pair in shared for pair in pairs): continue
    labels=sum((shared[p] for p in pairs),[])
    distinct=len(set(labels))
    pattern="star" if distinct==1 else "strict_triangle" if distinct==3 and len(labels)==3 else "mixed"
    patterns.append({"ids":[a["id"],b["id"],c["id"]],"pattern":pattern,
                     "evidence":"candidate_only"})
F,v,m,p,E,W,d,t,P,U,R,I,V,n,M,c,rho=s.symbols("F v m p E W d t P U R I V n M c rho")
checks=[
    ("P=F*v",s.cancel((F*d/t).subs(d,v*t)-F*v)),
    ("P=R*I**2",s.cancel((U*I).subs(U,R*I)-R*I**2)),
    ("rho=c*M",s.cancel((m/V).subs(m,n*M).subs(n,c*V)-c*M)),
    ("E=p**2/(2*m)",s.cancel((m*v**2/2).subs(v,p/m)-p**2/(2*m))]
A,B,C,D,X=s.symbols("A B C D X")
checks.append(("A*B=C*D from same X",s.simplify((X-A*B)-(X-C*D)-(C*D-A*B))))
result={"schema":"pilot50-repro/0.1","sympy_version":s.__version__,
"source":source["parent_source"],"formula_results":records,
"summary":{"formulas":len(data),"parse_ok":sum(r["parse_status"]=="parsed" for r in records),
"triadic_symbol_candidates":len(tri),"shared_label_edges":len(shared),
"triple_motifs":len(patterns),"star":sum(x["pattern"]=="star" for x in patterns),
"triangle":sum(x["pattern"]=="strict_triangle" for x in patterns),
"mixed":sum(x["pattern"]=="mixed" for x in patterns),
"symbolic_checks_ok":sum(expr==0 for _,expr in checks),"expert_confirmed_tensors":0},
"relations":[{"relation":name,"residual":str(expr),"pass":expr==0}
             for name,expr in checks],
"limits":["Same word is not same scientific quantity","All motifs lack semantic review",
"All relations need domain conditions","No automated paper publication"]}
print(json.dumps(result,indent=2,ensure_ascii=False))
