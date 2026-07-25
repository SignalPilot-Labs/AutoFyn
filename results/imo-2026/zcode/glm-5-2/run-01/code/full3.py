import sympy as sp, math, pickle
from sympy import symbols, expand, factor, simplify, Poly, together, numer, denom
p,q = symbols('p q'); A,P,G = symbols('A P G')
def rotCW(v,t):
    x,y=v; return (expand((1-t**2)*x + 2*t*y), expand(-2*t*x + (1-t**2)*y))
def rotCCW(v,t):
    x,y=v; return (expand((1-t**2)*x - 2*t*y), expand(2*t*x + (1-t**2)*y))
BA=(-sp.Integer(1),sp.Integer(0)); CA=(-p,-q)
dir_BK=rotCW(BA,A); dir_BL=rotCW(BA,P)
dir_CL=rotCCW(CA,A); dir_CK=rotCCW(CA,G)
def cross(u,v): return expand(u[0]*v[1]-u[1]*v[0])
def dot(u,v): return expand(u[0]*v[0]+u[1]*v[1])
W=(p-1,q)
def get_point(d1,d2,W):
    tn=cross(W,d2); td=cross(d1,d2)
    return expand(td+tn*d1[0]), expand(tn*d1[1]), td
Kx,Ky,Kden = get_point(dir_BK,dir_CK,W)
Lx,Ly,Lden = get_point(dir_BL,dir_CL,W)

def tan_diff(T,S):  # tan(2(arctan T - arctan S)) rational
    h=(T-S)/(1+S*T); return expand(2*h/(1-h**2))
tan_beta = together(tan_diff(P,A)); tan_gamma = together(tan_diff(G,A))
nb=expand(numer(tan_beta)); db=expand(denom(tan_beta))
ng=expand(numer(tan_gamma)); dg=expand(denom(tan_gamma))

# condA: ang LNC = beta. NL=L-N, NC=C-N=(p/2,q/2).
# Use NL'=(2Lx-p Lden, 2Ly - q Lden) over (2 Lden); NC'=(p,q) over 2. cross/dot ratio = tan_beta.
NLp=(expand(2*Lx-p*Lden), expand(2*Ly-q*Lden)); NCp=(p,q)
crA=cross(NLp,NCp); dtA=dot(NLp,NCp)
condA=expand(crA*db - dtA*nb)
# condB: ang BMK = gamma. M=(1/2,0). MB=(1/2,0). MK=(Kx/Kden-1/2, Ky/Kden).
# cross(MB,MK)=(1/2)(Ky/Kden). dot=(1/2)(Kx/Kden-1/2). ratio = Ky/(Kx - Kden/2) = 2Ky/(2Kx-Kden).
MKx=expand(2*Kx-Kden); MKy=expand(2*Ky)
condB=expand(MKy*dg - MKx*ng)

# verify condA,condB vanish at config
Av=math.tan(math.radians(10.140977272332982)/2)
beta=math.radians(21.08047146055647);gamma=math.radians(35.582220333404194)
Pv=math.tan((math.radians(10.140977272332982)+beta)/2); Gv=math.tan((math.radians(10.140977272332982)+gamma)/2)
subs={A:Av,P:Pv,G:Gv,p:sp.Rational(1,4),q:sp.Rational(3,4)}
print("condA at config:", float(condA.subs(subs)))
print("condB at config:", float(condB.subs(subs)))
print("condA factors preview:", factor(condA))
print("condB factors preview:", factor(condB))
with open('/tmp/geom/c2.pkl','wb') as f:
    pickle.dump(dict(condA=condA,condB=condB,Kx=Kx,Ky=Ky,Kden=Kden,Lx=Lx,Ly=Ly,Lden=Lden),f)
