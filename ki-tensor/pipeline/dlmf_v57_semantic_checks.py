#!/usr/bin/env python3
"""v5.7 source-matched scientific checks; no generic DLMF theorem verification."""
import sympy as s
import re
SPECIAL=re.compile(r'\\(littleo|bigO|EulerGamma|digamma|Pochhammersym|Ln|ln|sin|cos|sinh|cosh|erf|BesselJ)@{1,2}\{')
def macro_types(tex): return sorted(set(SPECIAL.findall(tex)))
z,a=s.symbols('z a',positive=True)
n,k=s.symbols('n k',integer=True,nonnegative=True)
x=s.symbols('x',real=True)
checks={
 "DLMF01601":s.simplify(s.rf(a,n)-s.gamma(a+n)/s.gamma(a)),
 "DLMF01599":s.simplify(s.digamma(z)-s.diff(s.gamma(z),z)/s.gamma(z)),
 "DLMF00003":s.simplify(s.summation(s.binomial(n,k),(k,0,n))-2**n),
 "DLMF00011":s.simplify(s.summation(a*x**k,(k,0,n-1))-a*(1-x**n)/(1-x)),
}
if __name__=="__main__":
 for key,val in checks.items(): print(key,str(val),val==0)
 # Gamma checks need positive real a,z; geometric identity has x!=1.
 # Big-O is asymptotic membership, never algebraic equality.
