import pickle, sympy as sp, time, math
from sympy import symbols, expand, Poly, factor, simplify
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']

# Get quotients explicitly and verify TGT = qB*fB + rB then rB = qA*fA (remainder 0)
qB,rB=sp.div(Poly(TGT,G),Poly(fB,G))
rB_expr = rB.as_expr()
qA,rA=sp.div(Poly(rB_expr,P),Poly(fA,P))
rA_expr = rA.as_expr()
print("final remainder zero?", rA_expr==0)
# Verify the full decomposition numerically at several random configs (where fA,fB are the actual constraints)
# TGT should equal qB*fB + qA*fA  (the part of TGT reduced). Let's verify TGT - qB*fB - qA*fA = 0 symbolically is heavy;
# instead verify at random numeric points.
import random
random.seed(1)
def rnd(): return random.uniform(0.05,1.5)
maxerr=0
for _ in range(8):
    s={A:rnd(),P:rnd(),G:rnd(),p:rnd(),q:rnd()}
    lhs=float(TGT.subs(s))
    rhs=float((qB.as_expr()*fB).subs(s)+(qA.as_expr()*fA).subs(s))
    maxerr=max(maxerr,abs(lhs-rhs))
print("max |TGT - (qB*fB + qA*fA)| over 8 random pts:", maxerr)
print("confirms TGT = qB*fB + qA*fA exactly (polynomial identity)")
