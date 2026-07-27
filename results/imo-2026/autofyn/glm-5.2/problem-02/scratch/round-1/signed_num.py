"""Numerical check: does the certificate hold for -theta?
If +theta holds on locus but -theta doesn't, §2 is SIGNED."""
import numpy as np, math
from numpy import sin,cos
from scipy.optimize import fsolve

def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build(A,al,be,ga,b,c):
    B=np.array([c,0.0]); C=np.array([b*cos(A),b*sin(A)]); M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=cos(a),sin(a); cd_,sd_=cos(d),sin(d); det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det; return P+u*np.array([ca_,sa_])
    K=isect(B,np.pi-al,M,ga); L=isect(C,A+np.pi+al,N,A-be)
    Kx,Ky=K; Lx,Ly=L; K2=K@K; L2=L@L; det=cross(K,L)
    Ax=(Ly*K2-Ky*L2)/det; Ay=(Kx*L2-Lx*K2)/det
    return B,C,K,L,np.array([Ax,Ay])

def incid(A,al,be,ga,b,c):
    B,C,K,L,Ap=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A+np.pi+al+ga),sin(A+np.pi+al+ga)]); incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)]); incL=cross(L-B,dBL)
    return incK,incL

def rotate(v, theta):
    c, s = cos(theta), sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

configs=[(70,15,1.4,1.0),(55,25,1.0,1.2),(45,18,0.9,1.3)]
print("Checking if G=0 holds for +theta but NOT -theta (=> SIGNED):")
for (Ad,ald,b,c) in configs:
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
    be,ga=np.radians(x[0]),np.radians(x[1])
    B,C,K,L,Ap=build(A_,al_,be,ga,b,c)
    target = np.pi/2 - A_ - al_
    CB = C-B; BAp = Ap-B
    # G_pos = BAp x R_{+target}(CB)
    G_pos = cross(BAp, rotate(CB, target))
    # G_neg = BAp x R_{-target}(CB)
    G_neg = cross(BAp, rotate(CB, -target))
    print(f"  A={Ad},al={ald}: G(+theta)={G_pos:.2e}  G(-theta)={G_neg:.2e}  => {'SIGNED (+theta)' if abs(G_pos)<1e-8 and abs(G_neg)>1e-6 else '??'}")
