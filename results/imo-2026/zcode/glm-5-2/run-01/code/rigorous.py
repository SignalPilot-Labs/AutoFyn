import pickle, sympy as sp, time
from sympy import symbols, expand, Poly, QQ
from sympy.polys.fields import FracField
# Use a fraction field K = QQ(p,q,A,P) and do Euclidean division in K[G].
with open('/tmp/geom/poly2.pkl','rb') as f: d=pickle.load(f)
# rebuild symbols
symstr=['p','q','A','P']
# Create FracField over QQ with these as generators, plus G as the poly variable.
from sympy import Symbol
FF = FracField(QQ, (Symbol("p"),Symbol("q"),Symbol("A"),Symbol("P")))
G_sym = symbols('G')
# Convert sympy expressions to FF elements is messy. Instead, use Poly with domain='EX' but 
# provide generator G and let others be EX coefficients - that's what we did.
# 
# The REAL clean check: verify TGT - qB*fB - rB is identically zero by substituting and using 
# a different method: compute it as Poly in G and confirm zero coefficients after substitution 
# via Poly over EX. Let me directly use groebner over the full ring Q[A,P,G,p,q] with lex order.
from sympy import groebner
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']
print("computing groebner basis of <fA,fB> over Q[A,P,G,p,q] lex (G,P,A,p,q)...")
t=time.time()
G_basis = groebner([fA,fB], G, P, A, p, q, order='lex')
print("groebner time:", round(time.time()-t,1),"s; basis length:", len(G_basis.polys))
# reduce TGT
rem = G_basis.reduce(TGT)
print("remainder of TGT mod Groebner basis:", "ZERO" if rem==0 else "NONZERO")
print(rem if rem!=0 else "")
