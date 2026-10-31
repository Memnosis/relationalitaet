#!/usr/bin/env python3
"""A genuinely executable small mathematical regression core, not a generic DLMF parser."""
import sympy as s
z=s.Symbol('z')
k=s.Symbol('k',integer=True,positive=True)
m=s.Symbol('m',integer=True,nonnegative=True)
n=s.Symbol('n',integer=True,positive=True)
a,x=s.symbols('a x')
pascal=s.simplify(s.expand_func(s.binomial(z+1,k)-s.binomial(z,k)-s.binomial(z,k-1)))
partial_sum_step=s.simplify(s.expand_func((-1)**(m+1)*s.binomial(z,m+1)-((-1)**(m+1)*s.binomial(z-1,m+1)-(-1)**m*s.binomial(z-1,m))))
geometric_step=s.simplify(s.cancel(a*(1-x**(n+1))/(1-x)-a*(1-x**n)/(1-x)-a*x**n))
assert pascal==partial_sum_step==geometric_step==0
assert s.binomial(1,0)-s.binomial(1,1)==0
assert s.binomial(0,0)==1
assert sum([2*(-1)**j for j in range(2)])==sum([7*(-1)**j for j in range(2)])==0
print('3 exact symbolic step/identity checks and 2 boundary assertions passed; source-domain proof remains open')
