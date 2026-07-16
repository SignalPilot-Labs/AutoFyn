import sympy as sp
al,u,w,B,C = sp.symbols('alpha u w B C', positive=True)
A=sp.pi-B-C
# u-relation: cot_ACK = cot(al+gamma), cot gamma=(cot u-cot al)/2
cot_ACK = sp.sin(B)*sp.sin(al+u)/(sp.sin(C)*sp.sin(al)*sp.sin(B+C+u)) + sp.cos(B+C+u)/sp.sin(B+C+u)
cotg=(sp.cot(u)-sp.cot(al))/2
# cot(al+gamma) = (cot al*cot gamma -1)/(cot al+cot gamma)
cot_apg=(sp.cot(al)*cotg-1)/(sp.cot(al)+cotg)
Ru_raw=sp.simplify(cot_ACK-cot_apg)
Ru_num=sp.together(Ru_raw)
Ru_num=sp.fraction(sp.cancel(Ru_num))[0]
Ru_num=sp.expand_trig(Ru_num)
Ru_num=sp.simplify(Ru_num)
print("Ru_num=",Ru_num)
