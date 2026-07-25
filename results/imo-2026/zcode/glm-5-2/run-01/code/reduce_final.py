import pickle, sympy as sp, time
from sympy import symbols, expand, Poly, factor, groebner
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
print("deg: TGT in G",Poly(TGT,G).degree(),"in P",Poly(TGT,P).degree(),"in A",Poly(TGT,A).degree())
print("fA in P",Poly(fA,P).degree()," fB in G",Poly(fB,G).degree())
# Reduction: fB only involves G,A. Reduce TGT mod fB as poly in G.
t=time.time()
qB,rB=sp.div(Poly(TGT,G),Poly(fB,G))
print("div by fB:",round(time.time()-t,2),"s; remainder deg in G:", (Poly(rB,G).degree() if rB!=0 else -1))
rB=expand(rB.as_expr() if hasattr(rB,'as_expr') else rB)
if rB==0:
    print("REMAINDER ZERO after fB alone!")
else:
    qA,rA=sp.div(Poly(rB,P),Poly(fA,P))
    rA=expand(rA.as_expr() if hasattr(rA,'as_expr') else rA)
    print("after fA: remainder", "ZERO!" if rA==0 else f"{len(rA.as_ordered_terms())} terms")
    if rA!=0:
        print("factor:", factor(rA))
