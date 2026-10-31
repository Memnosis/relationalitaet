#!/usr/bin/env python3
import re
import sympy as s
from sympy.parsing.latex import parse_latex
def verify(tex):
 t=tex.strip().strip("$").rstrip(".,;").replace(r"\tfrac",r"\frac").replace(r"\dfrac",r"\frac").replace(r"\EulerGamma",r"\Gamma")
 if re.search(r"\\(?:dots|cdots|ldots|vdots|ddots|begin|end|Wigner|Weierstrass|Pochhammer)",t):return "UNSUPPORTED",None
 if t.count("=")!=1:return "NOT_SINGLE_EQUATION",None
 a,b=t.split("=")
 lhs,rhs=parse_latex(a,backend="lark"),parse_latex(b,backend="lark")
 if not isinstance(lhs,s.Basic) or not isinstance(rhs,s.Basic):return "AMBIGUOUS",None
 residual=s.simplify(lhs-rhs)
 return ("SYMBOLIC_ZERO_UNDER_PARSER_ASSUMPTIONS" if residual==0 else "NOT_PROVED"),str(residual)
# This routine does not establish original source domains, inverses or original theory validity.
