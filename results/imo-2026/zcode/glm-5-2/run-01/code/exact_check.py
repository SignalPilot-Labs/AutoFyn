import pickle, sympy as sp, time
from sympy import symbols, expand, Poly, simplify
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
qB,rB=sp.div(Poly(TGT,G),Poly(fB,G))
rB_expr = rB.as_expr()
qA,rA=sp.div(Poly(rB_expr,P),Poly(fA,P))
# Symbolic exact check: expand(TGT - qB*fB - qA*fA) should be 0
t=time.time()
diff = expand(Poly(qB,G).as_expr()*fB + Poly(qA,P).as_expr()*fA - TGT)
print("exact symbolic difference == 0?", diff==0, " time:",round(time.time()-t,1),"s")
