import pickle, sympy as sp
from sympy import symbols, expand, factor, Poly, groebner, Rational, simplify, together, numer, denom, cancel
with open('/tmp/geom/conds.pkl','rb') as f:
    d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
condA=d['condA']; condB=d['condB']; Kx=d['Kx']; Ky=d['Ky']; Kden=d['Kden']; Lx=d['Lx']; Ly=d['Ly']; Lden=d['Lden']

# Redo target as pure polynomial. 
# O satisfies: ox*Kx+oy*Ky = (Kx^2+Ky^2)/(2 Kden)   ... (1)
#              ox*Lx+oy*Ly = (Lx^2+Ly^2)/(2 Lden)   ... (2)
# Multiply (1) by 2*Kden: 2*Kden*(ox*Kx+oy*Ky) = Kx^2+Ky^2
# Multiply (2) by 2*Lden: 2*Lden*(ox*Lx+oy*Ly) = Lx^2+Ly^2
# These are linear in ox,oy with polynomial coeffs. Solve:
# a1 ox + b1 oy = c1 ; a2 ox + b2 oy = c2
a1=expand(2*Kden*Kx); b1=expand(2*Kden*Ky); c1=expand(Kx**2+Ky**2)
a2=expand(2*Lden*Lx); b2=expand(2*Lden*Ly); c2=expand(Lx**2+Ly**2)
DET=expand(a1*b2-a1*b2 + a1*b2 - b1*a2)  # = a1*b2 - b1*a2
DET=expand(a1*b2 - b1*a2)
oxn = expand(c1*b2 - b1*c2)  # ox = oxn/DET
oyn = expand(a1*c2 - c1*a2)  # oy = oyn/DET
# OM=ON <=> ox(p-1)+oy q = (p^2+q^2-1)/4 * (DET cancels):
# oxn(p-1)+oyn q = (p^2+q^2-1)/4 * DET
TGT = expand(oxn*(p-1) + oyn*q - (p**2+q**2-1)*DET/4)
# ensure integer: multiply by 4
TGT = expand(4*TGT)
print("TGT is polynomial?", TGT.is_polynomial(A,P,G,p,q))
print("TGT terms:", len(expand(TGT).as_ordered_terms()))
print("deg in G:", Poly(TGT,G).degree(), "deg in P:", Poly(TGT,P).degree(), "deg in A:", Poly(TGT,A).degree())

fA = expand(sp.simplify(condA / (-2*(p**2+q**2)*(A*P+1))))
fB = expand(sp.simplify(condB / (-2*(A*G+1))))
with open('/tmp/geom/poly.pkl','wb') as f:
    pickle.dump(dict(TGT=TGT,fA=fA,fB=fB),f)
print("saved")
