#!/usr/bin/env python3
"""Conservative v5.6 tokenizer preflight. No implicit mathematical proof."""
import re
DLMF_AT_RE=re.compile(r'\\[A-Za-z]+@{1,2}\{')
DERIV_RE=re.compile(r'\\deriv(?:\[[0-9]+\])?\{')
def classify(tex):
    if any(x in tex for x in (r'\dots',r'\cdots',r'\ldots')):
        return 'ELLIPSIS_NEEDS_SOURCE_PATTERN'
    if r'\begin' in tex or r'\end' in tex:return 'MATH_ENVIRONMENT'
    if DLMF_AT_RE.search(tex):return 'DLMF_FUNCTION_TYPED_REGISTRY_REQUIRED'
    if DERIV_RE.search(tex):return 'DERIVATIVE_MACRO_REQUIRES_AST'
    if tex.count('=')!=1:return 'NOT_SINGLE_EQUALITY'
    return 'LARK_REQUIRES_TEST'
def normalize_supported(tex):
    t=tex.replace(r'\tfrac',r'\frac').replace(r'\dfrac',r'\frac')
    for name in ('sin','cos','tan','ln','log','exp','Gamma','sinh','cosh'):
        t=re.sub(r'(\\'+name+r')@{1,2}\{',r'\1{',t)
    return t
