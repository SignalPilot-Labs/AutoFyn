import pickle, sympy as sp
from sympy import symbols, expand, factor, degree, Poly, groebner, Rational, simplify, collect
with open('/tmp/geom/conds.pkl','rb') as f:
    d=pickle.load(f)
condA=d['condA']; condB=d['condB']
Kx,Ky,Kden=d['Kx'],d['Ky'],d['Kden']
Lx,Ly,Lden=d['Lx'],d['Ly'],d['Lden']
A,P,G,p,q = symbols('A P G p q')
condA = condA.subs({str(s):s for s in [A,P,G,p,q]})
condB = condB.subs({str(s):s for s in [A,P,G,p,q]})
# condA has prefactor (p^2+q^2)(AP+1) which is generically nonzero. Divide it out.
condA_red = sp.simplify(condA / ((p**2+q**2)*(A*P+1)))
condA_red = expand(condA_red)
condB_red = sp.simplify(condB / ((A*G+1)))
condB_red = expand(condB_red)
print("degree of condA_red in P:", degree(condA_red, P))
print("degree of condB_red in G:", degree(condB_red, G))
# Collect as polynomial in P (should be linear -> solves P)
polyA = Poly(condA_red, P)
print("\ncondA_red as poly in P, coefficients:")
for i,c in enumerate(polyA.all_coeffs()):
    print(f"  P^{polyA.degree()-i}:", factor(c))

print("\n--- factoring condA_red ---")
print("condA_red factored:", factor(condA_red))
print("\n--- factoring condB_red ---")
print("condB_red factored:", factor(condB_red))
