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

def dang_line(u,v):
    """directed angle from LINE u to LINE v, mod pi, in (-pi/2, pi/2]"""
    return math.atan2(cross(u,v),u@v)

def dang_ray(u,v):
    """directed angle from RAY u to RAY v, mod 2pi"""
    return math.atan2(cross(u,v),u@v)

def incid(A,al,be,ga,b,c):
    B,C,K,L,Ap=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A+np.pi+al+ga),sin(A+np.pi+al+ga)]); incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)]); incL=cross(L-B,dBL)
    return incK,incL

configs=[(70,15,1.4,1.0),(55,25,1.0,1.2),(80,10,1.6,1.1),(45,18,0.9,1.3),(65,8,1.1,0.8),(50,30,1.3,1.0),(40,20,1.0,1.5),(75,12,1.2,0.9)]
print(f"{'A':>4} {'al':>4} {'b':>4} {'c':>4} | {'BC->BA(line)':>13} {'BC->CA(line)':>13} {'90-A-al':>10} | {'-(90-A-al)':>11} | {'BC->BA(ray)':>12} {'CB->CA(ray)':>12} {'BC->CA(ray)':>12}")
for (Ad,ald,b,c) in configs:
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
    be,ga=x[0],x[1]
    B,C,K,L,Ap=build(A_,al_,np.radians(be),np.radians(ga),b,c)
    BC=C-B; BA_=Ap-B; CA_=Ap-C; CB=B-C
    target = np.pi/2 - A_ - al_
    # line convention mod pi
    ang_BA_line = dang_line(BC, BA_)
    ang_CA_line = dang_line(BC, CA_)
    # ray convention mod 2pi
    ang_BA_ray = dang_ray(BC, BA_)
    ang_CB_CA_ray = dang_ray(CB, CA_)
    ang_BC_CA_ray = dang_ray(BC, CA_)
    print(f"{Ad:4d} {ald:4d} {b:4.1f} {c:4.1f} | {ang_BA_line:13.6f} {ang_CA_line:13.6f} {target:10.6f} | {-target:11.6f} | {ang_BA_ray:12.6f} {ang_CB_CA_ray:12.6f} {ang_BC_CA_ray:12.6f}")
print()
print("Key question: is dang_line(BC, CA') = +target or -target?")
