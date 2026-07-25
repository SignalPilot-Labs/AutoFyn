import pickle, sympy as sp, random
from sympy import symbols, expand, Poly
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
qB,rB=sp.div(Poly(TGT,G),Poly(fB,G))
qB_expr=Poly(qB,G).as_expr(); rB_expr=rB.as_expr()
diff=expand(qB_expr*fB + rB_expr - TGT)
print("diff==0 via ==", diff==0)
print("diff terms:", len(diff.as_ordered_terms()) if diff!=0 else 0)
# numerical check of this diff at random points
random.seed(7);mx=0
for _ in range(10):
    s={A:random.uniform(.1,2),P:random.uniform(.1,2),G:random.uniform(.1,2),p:random.uniform(.1,2),q:random.uniform(.1,2)}
    mx=max(mx,abs(float(diff.subs(s))))
print("max |diff| numeric:",mx)
# Maybe the issue is that Poly(TGT,G) silently made leading coeff rational function? Check leading coeffs
pB=Poly(fB,G); print("fB leading coeff in G:", pB.LC())
pT=Poly(TGT,G); print("TGT leading coeff in G is a number?", pT.LC().is_number, " value-ish:", float(pT.LC().subs({A:1,P:1,p:1,q:1})) if not pT.LC().is_number else pT.LC())
