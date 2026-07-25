import pickle, sympy as sp
from sympy import symbols, expand, Poly, factor, simplify
import time
with open('/tmp/geom/poly.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']

t=time.time()
qB, rB = sp.div(Poly(TGT, G), Poly(fB, G))
print("div by fB in G: time", round(time.time()-t,2))
rB = expand(sp.Poly(rB).as_expr())
print("rB deg in G:", Poly(rB,G).degree() if rB!=0 else -1, " terms:", len(rB.as_ordered_terms()) if rB!=0 else 0)
t=time.time()
if rB != 0:
    qA, rA = sp.div(Poly(rB, P), Poly(fA, P))
    print("div by fA in P: time", round(time.time()-t,2))
    rA = expand(sp.Poly(rA).as_expr())
    if rA == 0:
        print("FINAL REMAINDER = 0  ==>  TGT is in the ideal <fA, fB>  ==> OM=ON PROVED (algebraically)")
    else:
        print("rA terms:", len(rA.as_ordered_terms()))
        print("rA factored:", factor(rA))
