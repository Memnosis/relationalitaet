#!/usr/bin/env python3
"""Source-specific DLMF semantic checks; identities alone do not validate trinitäten."""
import sympy as s
n,k=s.symbols("n k",integer=True,nonnegative=True)
x,a=s.symbols("x a")
def binomial_sum_residual():
    return s.simplify(s.summation(s.binomial(n,k),(k,0,n))-2**n)
def alternating_sum_residual():
    return s.simplify(s.summation((-1)**k*s.binomial(n,k),(k,0,n)))
def geometric_series_residual():
    N=s.symbols("N",integer=True,positive=True)
    return s.simplify(s.summation(a*x**k,(k,0,N-1))-a*(1-x**N)/(1-x))
def special_regressions():
    z=s.symbols("z")
    return [s.simplify(s.gamma(z+1)-z*s.gamma(z)),s.simplify(s.besselj(-2,x)-s.besselj(2,x)),s.simplify(s.erf(-x)+s.erf(x))]
if __name__=="__main__":
    print("binomial",binomial_sum_residual())
    print("alternating (n>=1; may require piecewise simplification)",alternating_sum_residual())
    print("geometric (x!=1)",geometric_series_residual())
    print("special functions (regressions only)",special_regressions())
