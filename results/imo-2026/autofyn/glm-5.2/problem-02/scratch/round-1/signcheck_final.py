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
    return B,C,K,L,M,N,np.array([Ax,Ay])

def incid(A,al,be,ga,b,c):
    B,C,K,L,M,N,Ap=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A+np.pi+al+ga),sin(A+np.pi+al+ga)]); incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)]); incL=cross(L-B,dBL)
    return incK,incL

def line_angle(u, v):
    a = math.atan2(cross(u,v), u@v)
    while a > math.pi/2 + 1e-12: a -= math.pi
    while a < -math.pi/2 - 1e-12: a += math.pi
    return a

configs=[(70,15,1.4,1.0),(55,25,1.0,1.2),(80,10,1.6,1.1),(45,18,0.9,1.3),(65,8,1.1,0.8),(50,30,1.3,1.0),(35,20,1.0,1.0),(75,5,1.2,0.9)]
print(f"{'A':>4} {'al':>4} {'theta':>8} | {'BAsign':>10} {'CB.CA':>10} {'BC.CA':>10} | {'|A B|-|A C|':>14}")
for (Ad,ald,b,c) in configs:
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
    be,ga=np.radians(x[0]),np.radians(x[1])
    B,C,K,L,M,N,Ap=build(A_,al_,be,ga,b,c)
    target = np.pi/2 - A_ - al_
    BC=C-B; BA_=Ap-B; CA_=Ap-C; CB=B-C
    s1 = line_angle(BC, BA_)           # §2: should be +theta
    s2 = line_angle(CB, CA_)           # corrected §3: should be -theta
    s3 = line_angle(BC, CA_)           # no-flip step: should be -theta (= s2)
    diff = np.linalg.norm(Ap-B)-np.linalg.norm(Ap-C)
    print(f"{Ad:>4} {ald:>4} {np.degrees(target):>8.3f} | {np.degrees(s1):>10.4f} {np.degrees(s2):>10.4f} {np.degrees(s3):>10.4f} | {diff:>14.2e}")
