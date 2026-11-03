#!/usr/bin/env python3
"""Independent bounded semantic check for LOGIK-PROMPT-02.
Proof obligation: soundness of modus ponens for classical propositional semantics,
plus invalidity of affirming the consequent. Does NOT establish completeness of
any 3x3x3 meta logic, nor any unbounded proof calculus.
"""
from itertools import product

values=list(product((False,True),repeat=2))
def implies(a,b):return (not a) or b
sound=[]; invalid=[]
for p,q in values:
    mp_premises=(implies(p,q),p)
    sound.append((p,q,not all(mp_premises) or q))
    affirm_premises=(implies(p,q),q)
    if all(affirm_premises) and not p:invalid.append((p,q))
assert all(t[2] for t in sound), 'MP must be sound on all valuations'
assert invalid==[(False,True)],f'invalidity witness missing: {invalid}'
print('LOGIK-PROMPT-02 INDEPENDENT BOUNDED CHECK')
print('Semantics: 2-valued classical propositional logic; variables p,q.')
for p,q,valid in sound:print(f'p={int(p)} q={int(q)} p_implies_q={int(implies(p,q))} MP_valid={valid}')
print('MP global rule soundness on all 4 p,q assignments: PASS')
print('Affirming consequent invalid: p=0,q=1; (p->q)=1,q=1,p=0: PASS')
print('Logical equivalence and global completeness of any new tensor meta-logic: NOT TESTED')
