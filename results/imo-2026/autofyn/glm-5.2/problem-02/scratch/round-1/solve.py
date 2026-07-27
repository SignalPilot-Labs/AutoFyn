import numpy as np, math
from numpy import sin,cos
from scipy.optimize import fsolve
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build(A,al,be,ga,b=1.0,c=1.0):
    A_=A; al_=al; be_=be; ga_=ga
    B=np.array([c,0.0]); C=np.array([b*cos(A_),b*sin(A_)])
    M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=cos(a),sin(a); cd_,sd_=cos(d),sin(d)
        det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det
        return P+u*np.array([ca_,sa_])
    K=isect(B, np.pi-al_, M, ga_)
    L=isect(C, A_+np.pi+al_, N, A_-be_)
    Kx,Ky=K; Lx,Ly=L
    K2=K@K; L2=L@L; detKL=cross(K,L)
    Ax=(Ly*K2-Ky*L2)/detKL
    Ay=(Kx*L2-Lx*K2)/detKL
    Ap=np.array([Ax,Ay]) if abs(detKL)>1e-9 else None
    return B,C,M,N,K,L,Ap

def incid(A,al,be,ga,b=1.0,c=1.0):
    # incidences: K on line CK (dir A+pi+al+ga from C), L on line BL (dir pi-al-be from B)
    A_=A; B,C,M,N,K,L,Ap=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A_+np.pi+al+ga),sin(A_+np.pi+al+ga)])
    incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)])
    incL=cross(L-B,dBL)
    return incK,incL

A_=np.radians(60); al_=np.radians(20)
# interior branch
def solve(b,c):
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    return fsolve(f,[15,15],full_output=True)
for b in [1.0]:
    x,inf,ier,msg=solve(b,1.0)
    be,ga=x
    print(f"b={b} be={be:.6f} ga={ga:.6f} resid={np.max(np.abs(inf['fvec'])):.2e}")
    B,C,M,N,K,L,Ap=build(A_,al_,np.radians(be),np.radians(ga),b,1.0)
    print(f"  |ApB|={np.linalg.norm(Ap-B):.6f} |ApC|={np.linalg.norm(Ap-C):.6f}")
    Bang=math.degrees(math.acos((-B@(C-B))/((np.linalg.norm(-B)*np.linalg.norm(C-B))))); Cang=180-60-Bang
    def dang(u,v): return math.degrees(math.atan2(cross(u,v),u@v))
    print(f"  B={Bang:.4f} C={Cang:.4f}")
    print(f"  BC->BA'={dang(C-B,Ap-B):.6f} target={math.degrees(90-A_-al_):.6f}")
    print(f"  BK->BA'={dang(K-B,Ap-B):.6f} target C-90={Cang-90:.6f}")
    # check Ap on perp-through-K and perp-through-L
    print(f"  Ap.K=|K|^2? {Ap@K} vs {K@K} ; Ap.L={Ap@L} vs {L@L}")
    print(f"  K={K} L={L} Ap={Ap}")
