import sympy as sp, pickle, numpy as np, random
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
d = pickle.load(open('sol.pkl','rb'))
Xs=sp.sympify(d['Xs']); Ys=sp.sympify(d['Ys']); Zs=sp.sympify(d['Zs'])
D = k*lb - kb*l
TN = 2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb - b*bb)*D
num = sp.expand(sp.numer(sp.cancel(sp.together(TN.subs({kb:Ys, lb:Zs})))))
R = sp.cancel(Ys*Zs - Xs); Rnum = sp.expand(sp.numer(sp.together(R)))
print("factor Rnum:")
fR = sp.factor(Rnum); print(fR)
print("factor num:")
fN = sp.factor(num); print(fN)
