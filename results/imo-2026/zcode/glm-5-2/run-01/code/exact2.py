import pickle, sympy as sp, time
from sympy import symbols, expand, Poly, simplify, factor
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
qB,rB=sp.div(Poly(TGT,G),Poly(fB,G))
rB_expr = rB.as_expr()
qA,rA=sp.div(Poly(rB_expr,P),Poly(fA,P))
rA_expr = rA.as_expr()
# check 1: rA_expr == 0  (the final remainder)
print("final remainder rA == 0 ?", rA_expr==0)
# check 2: rB_expr - qA.as_expr*fA == rA_expr  (i.e. rB = qA*fA + rA)
chk2 = expand(Poly(qA,P).as_expr()*fA + rA_expr - rB_expr)
print("rB = qA*fA + rA verified?", chk2==0)
# check 3: TGT - qB*fB - rB == 0
qB_expr = Poly(qB,G).as_expr()
chk3 = expand(qB_expr*fB + rB_expr - TGT)
print("TGT = qB*fB + rB verified?", chk3==0)
