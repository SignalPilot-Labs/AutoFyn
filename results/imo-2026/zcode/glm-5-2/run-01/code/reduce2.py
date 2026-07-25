import pickle, sympy as sp
from sympy import symbols, expand, Poly, factor, simplify
import time
with open('/tmp/geom/poly.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']

# Reduce TGT by fB (as polynomial in G), coefficients in Q(p,q)[A,P].
# Use Poly with domain over the fraction field QQ(p,q) won't directly work; use generic polys 
# with all variables and divide by leading monomial in G with lex order G > rest.
# Simplest: use sp.div with gens=(G,) treats other symbols as coeffs (domain EX = expression).
t=time.time()
qB, rB = sp.div(Poly(TGT, G), Poly(fB, G))
print("div by fB in G: time", round(time.time()-t,2))
rB = expand(rB)
print("remainder rB: deg in G =", (Poly(rB,G).degree() if rB!=0 else -1))
print("rB terms:", len(expand(rB).as_ordered_terms()))
# Now rB depends on A,P (and p,q). Reduce by fA as poly in P.
t=time.time()
if rB != 0:
    qA, rA = sp.div(Poly(rB, P), Poly(fA, P))
    print("div by fA in P: time", round(time.time()-t,2))
    rA = expand(rA)
    print("final remainder rA:", rA if rA==0 else f"{len(expand(rA).as_ordered_terms())} terms")
    if rA != 0:
        print("rA factored:", factor(rA))
else:
    print("rB already zero!")
