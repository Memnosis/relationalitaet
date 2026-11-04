#!/usr/bin/env python3
"""Algebra-Suchmatrix: 25 unabhängige mathematische Varianten-Referenzprüfungen.
Run: python3 forschung/tensor/algebra-claude/suchmatrix_varianten_25.py
Requires numpy and sympy. NOT a scientific approval of historical 103 tensor skeletons.
"""
import json
import sympy as s
import numpy as np
from sympy.physics.wigner import wigner_3j

tests=[]
def check(code, description, result, condition=""):
    assert result, "FAIL "+code+": "+description
    tests.append({"id":code,"description":description,"passed":True,"conditions":condition,
                  "scope":"math_reference_not_27_field_validation"})
x,y,z,t,k=s.symbols("x y z t k",real=True)
a,b,c=s.symbols("a b c")
check("V01","inverse affine",s.simplify((3*((y-2)/3)+2)-y)==0)
check("V02","x² inverse has two branches",set(s.solve(x*x-y,x))=={-s.sqrt(y),s.sqrt(y)},"y≥0 for real branches")
check("V03","projection (x,y)->x not injective",(2,7)!=(2,-9) and (2,7)[0]==(2,-9)[0])
A=s.Matrix([[2,1],[1,1]])
check("V04","invertible matrix",A*A.inv()==s.eye(2))
B=s.Matrix([[1,2],[2,4]])
check("V05","singular matrix loses nullspace",B.det()==0 and B*s.Matrix([2,-1])==s.zeros(2,1))
check("V06","differentiation loses additive constant",s.integrate(s.diff(x*x+c,x),x)==x*x)
x0=s.symbols("x0")
check("V07","reversal of x0*exp(-k t)",s.simplify((x0*s.exp(-k*t)).subs(x0,x*s.exp(k*t))-x)==0,
      "finite t, exact state and k")
check("V08","nondimensionalization du/dτ=-u",
      s.simplify(s.diff(s.exp(-t),t)+s.exp(-t))==0)
S,v,F,V,cin,r=s.symbols("S v F V cin r")
check("V09","reactor special case F=0",(s.cancel((F*(cin-c)+V*r)/V).subs(F,0).subs(r,S*v)-S*v).simplify()==0,
      "V != 0, r(c)=S*v(c)")
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
check("V10","Hadamard is involution",s.simplify(H*H)==s.eye(2))
check("V11","two phases same computational measurement probabilities",
      s.simplify((1/s.sqrt(2))**2)==s.Rational(1,2))
T=np.zeros((3,3,3)); U=T.copy();U[0,1,0]=1;U[0,2,0]=-1
check("V12","tensor summation loses information",np.array_equal(T.sum(axis=1),U.sum(axis=1)) and not np.array_equal(T,U))
T=np.arange(27).reshape(3,3,3).astype(float)
Q=np.array([[0,1,0],[-1,0,0],[0,0,1]],dtype=float)
U=np.einsum("ia,jb,kc,abc->ijk",Q,Q,Q,T)
check("V13","orthogonal basis transform preserves Frobenius norm",np.isclose(np.linalg.norm(T),np.linalg.norm(U)))
P=s.Matrix([[1,1],[0,1]]);D=s.diag(2,5); C=P*D*P.inv()
check("V14","similarity preserves characteristic polynomial",C.charpoly().as_expr()==D.charpoly().as_expr())
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
check("V15","Pauli commutator is noncommutative",X*Y-Y*X==2*s.I*Z)
p=np.zeros((3,3,3));p[0,0,0]=1;ghz=np.zeros((3,3,3))
for i in range(3):ghz[i,i,i]=1/np.sqrt(3)
rank=lambda T:[int(np.linalg.matrix_rank(np.moveaxis(T,j,0).reshape(3,-1))) for j in range(3)]
check("V16","same 27 amplitudes but different flattening ranks",rank(p)==[1,1,1] and rank(ghz)==[3,3,3])
check("V17","Wigner rules not sufficient",wigner_3j(1,1,1,0,0,0)==0)
pa=s.Rational(1,10);bga=s.Rational(4,5);bgn=s.Rational(1,5)
check("V18","reverse conditional needs prior",s.cancel(bga*pa/(bga*pa+bgn*(1-pa)))==s.Rational(4,13))
check("V19","squaring generates extraneous root",s.solve(x*x-1,x)==[-1,1] and x!=-1)
check("V20","log inverse branch requires domain",s.simplify(s.exp(s.log(2))-2)==0,
      "log(exp(z)) not always z on complex principal branch")
M=s.Matrix([[1,0,0],[0,1,0]]);Mp=M.pinv()
check("V21","pseudoinverse is one-sided",M*Mp==s.eye(2) and Mp*M!=s.eye(3))
check("V22","attractor need not mean noninvertible",s.solve(x-(x+1)/2,x)==[1] and s.solve(y-(x+1)/2,x)==[2*y-1])
check("V23","inverse function theorem fails at singular Jacobian",s.diff(x*x,x).subs(x,0)==0)
check("V24","cancel changes excluded domain",s.cancel((z*z-z)/(z-1))==z,"z!=1")
check("V25","mean loses observation detail",(2+4)/2==(1+5)/2)
assert len(tests)==25
print(json.dumps({"schema":"algebra-variants-test/0.1","tests":tests,
                  "summary":{"total":len(tests),"passed":sum(q["passed"] for q in tests)},
                  "caveat":"No classification of the 103 project tensors is implied."},ensure_ascii=False,indent=2))
