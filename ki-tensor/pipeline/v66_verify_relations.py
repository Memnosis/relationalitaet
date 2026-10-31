#!/usr/bin/env python3
"""Recompute 7 DLMF source-linked mathematical identities under stated domains."""
import sympy as s
n,k=s.symbols('n k',integer=True,nonnegative=True)
z=s.symbols('z')
a,b=s.symbols('a b',positive=True)
checks={
'1.2.1':s.binomial(n,k)-s.binomial(n,n-k),
'1.2.3':s.summation(s.binomial(n,k),(k,0,n))-2**n,
'1.2.4':s.summation((-1)**k*s.binomial(n,k),(k,0,n)),
'1.2.7':s.binomial(z+1,k)-s.binomial(z,k)-s.binomial(z,k-1),
'5.5.1':s.gamma(z+1)-z*s.gamma(z),
'5.5.2':s.digamma(z+1)-s.digamma(z)-1/z,
'5.12.1':s.beta(a,b)-s.gamma(a)*s.gamma(b)/s.gamma(a+b)
}
for key,value in checks.items():
 residual=s.simplify(s.combsimp(s.expand_func(value)))
 assert residual==0,(key,residual)
 print('conditional symbolic zero',key)
assert s.summation((-1)**k*s.binomial(0,k),(k,0,0))==1
print('counterexample to n=0 extension of DLMF 1.2.4 verified')
