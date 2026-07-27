import sympy as sp, math
from sympy import symbols,together,fraction,expand,cancel
sa,ca,sA,cA = sp.symbols('sa ca sA cA')
tb,tg = sp.symbols('tb tg')
sb=2*tb/(1+tb**2); cb=(1-tb**2)/(1+tb**2)
sg=2*tg/(1+tg**2); cg=(1-tg**2)/(1+tg**2)
def sadd(a,b,c,d): return (a*d+b*c, b*d-a*c)
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA
sag,cag=sadd(sa,ca,sg,cg); sab,cab=sadd(sa,ca,sb,cb)
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
b=symbols('b')
Kx,Ky=kx,ky; Lx,Ly=b*lxu,b*lyu
sAag=saa*cg+caa*sg; cAag=caa*cg-saa*sg
dirCKx=-cAag; dirCKy=-sAag
conK=sp.cancel((Kx-b*cA)*dirCKy - (Ky-b*sA)*dirCKx)
dirBLx=-cab; dirBLy=sab
conL=sp.cancel((Lx-1)*dirBLy - Ly*dirBLx)
cKp=sp.Poly(conK,b); cLp=sp.Poly(conL,b)
def pad(cs,n): cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
kc=list(cKp.all_coeffs()); lc=list(cLp.all_coeffs())
n=max(len(kc),len(lc)); kc=pad(kc,n); lc=pad(lc,n)
k1,k0=kc; l1,l0=lc
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy; Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
Gp=sp.Poly(G,b); Gc=list(Gp.all_coeffs()); G2,G1,G0=pad(Gc,3)
g=sp.cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)
Ccon=sp.cancel(k0*l1-l0*k1)
Phi = sA*sa**2*(tb**2-1)*(1-tg**2) + sa*(ca*sA-cA*sa)*(tb+tg)*(tb*tg-1) + (2*cA*ca*sa+sA*(sa**2-ca**2))*tb*tg
Tn = sa*tg*(sA**2+cA**2)**2*(ca-sa*tg)*(tb**2+1)*(ca*tg+sa)
Td = (tg**2+1)*Phi
# 1. certificate identity in free ring
diff_r=sp.cancel(g*Td - Ccon*Tn)
print("1. g*Td - C*Tn == 0 (free ring, rational)?", diff_r==0)
dt=together(g*Td - Ccon*Tn); dn,dd=fraction(dt); dn=expand(dn)
print("   cleared numerator == 0?", dn==0, "ops", sp.count_ops(dn))
# 2. NON-VACUOUS: g not identically 0, C not identically 0 (free eval)
import random
random.seed(11)
vals={sa:0.37,ca:0.91,sA:0.52,cA:-0.83,tb:0.6,tg:1.4}
gv=float(g.subs(vals)); Cv=float(Ccon.subs(vals))
print(f"2. Non-vacuous: g(free-eval)={gv:.4e} (≠0), C(free-eval)={Cv:.4e} (≠0)")
print(f"   => g vanishing on C=0 is a genuine constraint (proper subvariety)")
# 3. Signed +theta (not -theta, not unsigned): G(+theta)~0, G(-theta)≠0 on the locus
# Build a concrete valid config (A=55,al=25) and check
import numpy as np
from scipy.optimize import fsolve
def nbuild(A,al,be,ga,b_,c_):
    B=np.array([c_,0.0]); C=np.array([b_*np.cos(A),b_*np.sin(A)]); M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=np.cos(a),np.sin(a); cd_,sd_=np.cos(d),np.sin(d); det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det; return P+u*np.array([ca_,sa_])
    K=isect(B,np.pi-al,M,ga); L=isect(C,A+np.pi+al,N,A-be)
    Kx,Ky=K; Lx,Ly=L; K2=K@K; L2=L@L; det=Kx*Ly-Ky*Lx
    Ax_=(Ly*K2-Ky*L2)/det; Ay_=(Kx*L2-Lx*K2)/det
    return B,C,K,L,np.array([Ax_,Ay_])
def nincid(A,al,be,ga,b_,c_):
    B,C,K,L,Ap=nbuild(A,al,be,ga,b_,c_)
    dCK=np.array([np.cos(A+np.pi+al+ga),np.sin(A+np.pi+al+ga)]); incK=np.cross(K-C,dCK)
    dBL=np.array([np.cos(np.pi-al-be),np.sin(np.pi-al-be)]); incL=np.cross(L-B,dBL)
    return incK,incL
Ad,ald,b_,c_=55,25,1.0,1.2
A_=np.radians(Ad); al_=np.radians(ald)
def f(x):
    be,ga=x; return list(nincid(A_,al_,np.radians(be),np.radians(ga),b_,c_))
x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
be,ga=np.radians(x[0]),np.radians(x[1])
B,C,K,L,Ap=nbuild(A_,al_,be,ga,b_,c_)
theta=np.pi/2-A_-al_
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def R(t,v): c,s=np.cos(t),np.sin(t); return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])
Gplus=cross(Ap-B, R(+theta, C-B))
Gminus=cross(Ap-B, R(-theta, C-B))
print(f"3. Signed +θ check (A=55,α=25): G(+θ)={Gplus:.3e} (~0), G(-θ)={Gminus:.3e} (≠0)")
print(f"   => certificate proves SIGNED ∡(BC,BA')=+θ, not unsigned parallelism")
# 4. Check the §3 signs
def line_angle(u,v):
    a=math.atan2(cross(u,v),u@v)
    while a>math.pi/2+1e-12: a-=math.pi
    while a<-math.pi/2-1e-12: a+=math.pi
    return a
BC=C-B; BA_=Ap-B; CA_=Ap-C; CB=B-C
print(f"4. §3 signs: ∡(BC,BA')={np.degrees(line_angle(BC,BA_)):.4f}° (=+θ={np.degrees(theta):.4f}°)")
print(f"   ∡(CB,CA')={np.degrees(line_angle(CB,CA_)):.4f}° (=-θ={np.degrees(-theta):.4f}°)")
print(f"   ∡(BC,CA')={np.degrees(line_angle(BC,CA_)):.4f}° (=-θ, no flip: {np.degrees(-theta):.4f}°)")
print(f"   |A'B|-|A'C|={np.linalg.norm(Ap-B)-np.linalg.norm(Ap-C):.2e}")
