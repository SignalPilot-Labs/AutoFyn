import sympy as sp
al, be, ga, B, C = sp.symbols('alpha beta gamma B C', positive=True)
A = sp.pi - B - C
a = sp.sin(A); b = sp.sin(B); c = sp.sin(C)
tK = (c/2)*sp.sin(ga)/sp.sin(al+ga)
tL = (b/2)*sp.sin(be)/sp.sin(al+be)
Ax, Ay = c*sp.cos(B), c*sp.sin(B)
Kx, Ky = tK*sp.cos(B-al), tK*sp.sin(B-al)
Lx, Ly = a - tL*sp.cos(C-al), tL*sp.sin(C-al)
Px, Py = Kx-Ax, Ky-Ay
Qx, Qy = Lx-Ax, Ly-Ay
P2 = Px**2+Py**2; Q2 = Qx**2+Qy**2
s = a/2 - c*sp.cos(B)
E = P2*Qy - Q2*Py - s*(Px*Qy - Py*Qx)
RI  = sp.sin(C)*sp.sin(ga)*sp.sin(A+2*al+ga) - 2*sp.sin(A)*sp.sin(C-al-ga)*sp.sin(al+ga)
RII = sp.sin(B)*sp.sin(be)*sp.sin(A+2*al+be) - 2*sp.sin(A)*sp.sin(B-al-be)*sp.sin(al+be)

# Candidate: lambda_II = (dE/dbe)/(dRII/dbe) evaluated symbolically, then check E - lam_I*RI - lam_II*RII
# But easier: check if E*4*sin(al+ga)*sin(al+be) equals polynomial in RI,RII with simple factors.
# Try: is E/RI (with RII formally set 0 via using form d for tL) proportional?  Let's just test the
# ansatz that lam_I = RI-coefficient depends on ga through 1/(sin(al+ga)*sin(A+2al+ga)).
# Extract lam_I via limit: lam_I = E/RI when tL uses form (d) so RII-part is 'off'? messy.
# Instead: brute least-squares fit of E = f(ga)*RI + g(be)*RII at fixed al,B,C.
import numpy as np
from numpy import sin
def Ef(alv,bev,gav,Bv,Cv):
    Av=np.pi-Bv-Cv
    av=sin(Av);bv=sin(Bv);cv=sin(Cv)
    tKv=(cv/2)*sin(gav)/sin(alv+gav); tLv=(bv/2)*sin(bev)/sin(alv+bev)
    Axv,Ayv=cv*np.cos(Bv),cv*sin(Bv)
    Kxv,Kyv=tKv*np.cos(Bv-alv),tKv*sin(Bv-alv)
    Lxv,Lyv=av-tLv*np.cos(Cv-alv),tLv*sin(Cv-alv)
    Pxv,Pyv=Kxv-Axv,Kyv-Ayv; Qxv,Qyv=Lxv-Axv,Lyv-Ayv
    P2v=Pxv**2+Pyv**2;Q2v=Qxv**2+Qyv**2; sv=av/2-cv*np.cos(Bv)
    return P2v*Qyv-Q2v*Pyv-sv*(Pxv*Qyv-Pyv*Qxv)
def RIf(alv,gav,Bv,Cv):
    Av=np.pi-Bv-Cv
    return sin(Cv)*sin(gav)*sin(Av+2*alv+gav)-2*sin(Av)*sin(Cv-alv-gav)*sin(alv+gav)
def RIIf(alv,bev,Bv,Cv):
    Av=np.pi-Bv-Cv
    return sin(Bv)*sin(bev)*sin(Av+2*alv+bev)-2*sin(Av)*sin(Bv-alv-bev)*sin(alv+bev)
# fix al,B,C. Then E(be,ga) = f(ga)*RI(ga)+g(be)*RII(be). 
# For fixed ga: E as function of be is linear in RII(be)? test: E(be)-E(be0) = g?*(RII(be)-RII(be0)) only if g const in be.
alv,Bv,Cv=0.28,1.1,0.9
gav=0.4
be1,be2,be3=0.3,0.5,0.7
for gg in [0.3,0.4,0.55]:
  rows=[]
  for bb in [0.3,0.45,0.6,0.75]:
    rows.append((RIIf(alv,bb,Bv,Cv), Ef(alv,bb,gg,Bv,Cv)))
  # fit E = A0 + g*RII  ; A0 should be f(gg)*RI(gg)
  import numpy as np
  X=np.array([[1,r[0]] for r in rows]); Y=np.array([r[1] for r in rows])
  coef,res,*_=np.linalg.lstsq(X,Y,rcond=None)
  print(f"gg={gg}: intercept A0={coef[0]:.6f}, slope g={coef[1]:.6f}, resid={res}")
  print(f"    A0/RI(gg)={coef[0]/RIf(alv,gg,Bv,Cv):.6f}")
