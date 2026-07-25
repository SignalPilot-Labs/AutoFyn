import pickle, sympy as sp
from sympy import symbols, groebner, expand, Poly, factor
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
GB = groebner([fA, fB], G, P, A, p, q, order='lex')
res = GB.reduce(TGT)
print("type of reduce result:", type(res))
if isinstance(res, tuple):
    print("length:", len(res))
    print("is remainder (last or first) zero?")
    # In sympy, GroebnerBasis.reduce returns (quotients, remainder)
    quots, rem = res
    print("remainder is zero:", rem==0)
    print("remainder:", rem if rem!=0 else "0")
else:
    print("result:", res)
