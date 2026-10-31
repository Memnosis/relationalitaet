#!/usr/bin/env python3
"""Reproduzierbarer Kernparser für einfache DLMF-LaTeX-Gleichungen.

Usage: python dlmf_lark_verifier.py input.csv output.csv [limit]
Bewusste Grenze: symbolische Identität ist keine fachliche Trinitätenbestätigung.
"""
import csv,sys,re,signal
import sympy as sp
from sympy.parsing.latex import parse_latex

def timeout(*_): raise TimeoutError("TIMEOUT")
signal.signal(signal.SIGALRM, timeout)
def verify(row):
    tex=(row.get("content_tex") or row.get("formula") or "").strip().strip("$").rstrip(".,;")
    result={"id":row["id"],"equation_number":row.get("equation_number",""),"url":row.get("url",""),"status":"","detail":"","constraints":row.get("constraints_json","")}
    if any(s in tex for s in ("\\\\begin","\\\\end","\\\\NVar","\\\\dots")) or tex.count("=")!=1:
        result["status"]="UNSUPPORTED_OR_MULTIPLE_EQUALITIES";return result
    try:
        signal.alarm(2)
        a,b=tex.split("=",1)
        lhs=parse_latex(a,backend="lark")
        rhs=parse_latex(b,backend="lark")
        residual=sp.simplify(lhs-rhs)
        result["status"]="SYMBOLIC_ZERO_CONDITIONAL" if residual==0 else "UNDECIDED"
        result["detail"]=str(residual)[:200]
    except Exception as e:
        result["status"]="PARSER_ERROR";result["detail"]=type(e).__name__+": "+str(e)[:150]
    finally: signal.alarm(0)
    return result

def main():
    with open(sys.argv[1],encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    limit=int(sys.argv[3]) if len(sys.argv)>3 else len(rows)
    results=[verify(r) for r in rows[:limit]]
    with open(sys.argv[2],"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
    from collections import Counter
    print(dict(Counter(x["status"] for x in results)))
if __name__=="__main__": main()
