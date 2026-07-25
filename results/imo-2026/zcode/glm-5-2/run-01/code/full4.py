import sympy as sp, math, pickle
from sympy import symbols, expand, factor, simplify, Poly, together, numer, denom
with open('/tmp/geom/c2.pkl','rb') as f: d=pickle.load(f)
p,q=symbols('p q');A,P,G=symbols('A P G')
for k in d: d[k]=d[k].subs({str(s):s for s in [p,q,A,P,G]})
condA=d['condA'];condB=d['condB'];Kx=d['Kx'];Ky=d['Ky'];Kden=d['Kden'];Lx=d['Lx'];Ly=d['Ly'];Lden=d['Lden']
fA=expand(simplify(condA/(2*(p**2+q**2)*(A*P+1))))
fB=expand(simplify(condB/(-2*(A*G+1))))
# Target: OM=ON <=> ox(p-1)+oy q = (p^2+q^2-1)/4 *DET, with 
# a1=2Kden Kx, b1=2Kden Ky, c1=Kx^2+Ky^2 ; a2=2Lden Lx,... 
a1=expand(2*Kden*Kx);b1=expand(2*Kden*Ky);c1=expand(Kx**2+Ky**2)
a2=expand(2*Lden*Lx);b2=expand(2*Lden*Ly);c2=expand(Lx**2+Ly**2)
DET=expand(a1*b2-b1*a2)
oxn=expand(c1*b2-b1*c2); oyn=expand(a1*c2-c1*a2)
TGT=expand(4*(oxn*(p-1)+oyn*q) - (p**2+q**2-1)*DET)
print("TGT polynomial?", TGT.is_polynomial(A,P,G,p,q), "terms:", len(expand(TGT).as_ordered_terms()))
# verify at config
Av=math.tan(math.radians(10.140977272332982)/2)
beta=math.radians(21.08047146055647);gamma=math.radians(35.582220333404194)
Pv=math.tan((math.radians(10.140977272332982)+beta)/2); Gv=math.tan((math.radians(10.140977272332982)+gamma)/2)
subs={A:Av,P:Pv,G:Gv,p:sp.Rational(1,4),q:sp.Rational(3,4)}
print("TGT at config:", float(TGT.subs(subs)), " (should be ~0)")
print("fA at config:", float(fA.subs(subs)), "fB:", float(fB.subs(subs)))
with open('/tmp/geom/poly2.pkl','wb') as f:
    pickle.dump(dict(TGT=TGT,fA=fA,fB=fB),f)
print("saved")
