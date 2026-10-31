#!/usr/bin/env python3
"""Typed subexpression extraction. This does NOT parse or verify full equations."""
import re
PAT=re.compile(r'\\(EulerGamma|digamma|Pochhammersym|erf|sin|cos|ln|exp|littleo|bigO)@{1,2}\{')
KINDS={'EulerGamma':'SPECIAL_GAMMA','digamma':'SPECIAL_DIGAMMA','Pochhammersym':'SPECIAL_RISING_FACTORIAL','erf':'SPECIAL_ERROR_FUNCTION','sin':'ELEMENTARY_TRIG','cos':'ELEMENTARY_TRIG','ln':'ELEMENTARY_LOG','exp':'ELEMENTARY_EXP','littleo':'ASYMPTOTIC_LITTLE_O','bigO':'ASYMPTOTIC_BIG_O'}
def typed_nodes(tex):
    found=[]
    for match in PAT.finditer(tex):
        depth=1;i=match.end()
        while i<len(tex) and depth:
            if tex[i]=='{':depth+=1
            if tex[i]=='}':depth-=1
            i+=1
        if depth:continue
        found.append({'type':KINDS[match.group(1)],'macro':match.group(1),'argument_tex':tex[match.end():i-1],'start':match.start(),'end':i})
    return found
if __name__=='__main__':
    assert typed_nodes(r'\EulerGamma@{z+1}')[0]['argument_tex']=='z+1'
    assert typed_nodes(r'\ln@{\EulerGamma@{z}}')[0]['argument_tex']==r'\EulerGamma@{z}'
    print("Typed subexpression extraction self-tests passed")
