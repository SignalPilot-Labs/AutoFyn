import sympy as sp
B,C,beta,delta=sp.symbols('B C beta delta',real=True)
A=sp.pi-B-C
a=sp.Integer(1)
# A apex
a2=2*a*sp.sin(B)*sp.sin(C)/sp.sin(A)
a1=-a+2*a*sp.sin(C)*sp.cos(B)/sp.sin(A)
# K apex, base angles (B-beta) at B, (C-beta-delta) at C
den=sp.sin(A+2*beta+delta)
k2=2*a*sp.sin(B-beta)*sp.sin(C-beta-delta)/den
k1=-a+2*a*sp.sin(C-beta-delta)*sp.cos(B-beta)/den
# target height
htar=a*sp.cot(A+beta)
# G = k1(a1-k1) + (a2-k2)(k2 - htar)  ; want G == 0 mod constraint F
G=k1*(a1-k1)+(a2-k2)*(k2-htar)
# constraint F
F=sp.sin(C)*sp.sin(delta)*sp.sin(A+2*beta+delta)-2*sp.sin(A)*sp.sin(beta+delta)*sp.sin(C-beta-delta)
# Compute ratio G/F after simplification
G2=sp.simplify(sp.expand_trig(G))
F2=sp.simplify(sp.expand_trig(F))
ratio=sp.simplify(G2/F2)
print("G/F simplified =")
sp.pprint(ratio)
