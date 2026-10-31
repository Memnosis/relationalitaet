#!/usr/bin/env python3
"""Minimal, conservatively labeled source-retrieval filter, not a theorem prover."""
import re
PATTERNS={
 'integral':re.compile(r'\\int|\\iint|\\oint'),
 'derivative':re.compile(r'\\deriv|\\partial|\\prime'),
 'sum':re.compile(r'\\sum|\\dots|\\cdots'),
 'gamma':re.compile(r'\\Gamma|\\EulerGamma|\\digamma'),
}
def suggest(tex):
    return [name for name,pattern in PATTERNS.items() if pattern.search(tex)]
if __name__=='__main__':
    assert suggest(r'\\int_0^1 f(x) dx') == ['integral']
    print('retrieval-only tests passed')
