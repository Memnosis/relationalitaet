#!/usr/bin/env python3
"""Targeted regression examples. Does not claim fully sourced DLMF proofs."""
import sympy as s
n,k=s.symbols("n k",integer=True,nonnegative=True)
a,b,x=s.symbols("a b x")
# Pascal recurrence is symbolic, the following are finite regression checks
assert s.simplify(s.binomial(n+1,k)-s.binomial(n,k)-s.binomial(n,k-1))==0
for N in range(13):
    assert s.expand((a+b)**N-s.Add(*[s.binomial(N,i)*a**(N-i)*b**i for i in range(N+1)]))==0
    assert sum(s.binomial(N,i) for i in range(N+1))==2**N
    if N: assert sum((-1)**i*s.binomial(N,i) for i in range(N+1))==0
assert s.simplify(a*(1-x**(n+1))/(1-x)-a*(1-x**n)/(1-x)-a*x**n)==0
# Inverse reconstruction from geometric sum fails when x^N==1, x!=1
assert s.simplify((s.Integer(1)-(-1)**2)/(s.Integer(1)-(-1)))==0
print("v5.5 finite + symbolic regression examples passed")
