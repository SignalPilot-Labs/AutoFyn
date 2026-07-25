import pickle, sympy as sp, time
from sympy import symbols, groebner, expand, Poly
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
print("computing groebner basis of <fA, fB> over Q[p,q,A,P,G], lex order G > P > A > p > q ...")
t=time.time()
GB = groebner([fA, fB], G, P, A, p, q, order='lex')
print("groebner computed in", round(time.time()-t,1),"s, basis size:", len(GB.polys))
t=time.time()
rem = GB.reduce(TGT)
print("reduction time:", round(time.time()-t,1),"s")
print("remainder of TGT:", "ZERO (=> TGT in ideal => OM=ON PROVED)" if rem==0 else "NONZERO")
if rem != 0:
    print(sp.factor(rem))
