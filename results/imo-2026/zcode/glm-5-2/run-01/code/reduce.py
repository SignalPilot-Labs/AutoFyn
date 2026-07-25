import pickle, sympy as sp
from sympy import symbols, expand, factor, Poly, groebner, Rational, simplify, cancel, lcm
with open('/tmp/geom/target.pkl','rb') as f:
    d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TARGET=d['TARGET']; condA=d['condA']; condB=d['condB']
# Strip the known nonzero factors from condA, condB to get core polynomials.
# condA = -2 (p^2+q^2)(AP+1) * fA(A,P,p,q)
# condB = -2 (AG+1) * fB(A,G,p,q)
fA = sp.simplify(condA / (-2*(p**2+q**2)*(A*P+1))); fA=expand(fA)
fB = sp.simplify(condB / (-2*(A*G+1))); fB=expand(fB)
print("fA deg in P:", Poly(fA,P).degree(), " deg in A:", Poly(fA,A).degree())
print("fB deg in G:", Poly(fB,G).degree(), " deg in A:", Poly(fB,A).degree())

# Since fA depends on (A,P) only and fB on (A,G) only, and TARGET depends on (A,P,G),
# ideal membership I = <fA, fB> in Q(p,q)[A,P,G].
# Reduction: divide TARGET by fB as poly in G (with coeffs in Q(p,q)[A,P]) -> remainder r1 in Q(p,q)[A,P].
# Then divide r1 by fA as poly in P -> remainder r2. If r2=0 -> membership.
# Use Poly with lex order G>P>A... but coeffs rational in p,q. Use sp.ring? 
# Let's use the 'groebner' over the field Q(p,q) -- sympy handles via fraction field? 
# Simpler: work over Z[p,q,A,P,G] but that's heavy. 
# Try: reduce TARGET mod fB in G first.
import time
t=time.time()
pG = Poly(TARGET, G)
print("TARGET deg in G:", pG.degree(), " time:", round(time.time()-t,2))
pB = Poly(fB, G)
print("fB deg in G:", pB.degree())
# remainder of TARGET divided by fB (single poly) in variable G:
t=time.time()
r1, q1 = sp.div(Poly(TARGET,G), Poly(fB,G), domain='EX')
print("div by fB in G done, time", round(time.time()-t,2), " remainder deg in G:", Poly(r1,G).degree() if r1!=0 else -1)
r1 = expand(r1)
print("r1 free symbols:", r1.free_symbols)
print("r1 terms:", len(expand(r1).as_ordered_terms()))
with open('/tmp/geom/r1.pkl','wb') as f:
    pickle.dump(dict(r1=r1, fA=fA), f)
