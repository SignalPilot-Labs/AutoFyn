import numpy as np, math
from numpy import sin,cos
from scipy.optimize import fsolve

def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build_full(A,al,be,ga,b,c):
    B=np.array([c,0.0]); C=np.array([b*cos(A),b*sin(A)]); M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=cos(a),sin(a); cd_,sd_=cos(d),sin(d); det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det; return P+u*np.array([ca_,sa_])
    K=isect(B,np.pi-al,M,ga); L=isect(C,A+np.pi+al,N,A-be)
    Kx,Ky=K; Lx,Ly=L; K2=K@K; L2=L@L; det=cross(K,L)
    Ax=(Ly*K2-Ky*L2)/det; Ay=(Kx*L2-Lx*K2)/det
    return B,C,K,L,M,N,np.array([Ax,Ay])

def incid(A,al,be,ga,b,c):
    B,C,K,L,M,N,Ap=build_full(A,al,be,ga,b,c)
    dCK=np.array([cos(A+np.pi+al+ga),sin(A+np.pi+al+ga)]); incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)]); incL=cross(L-B,dBL)
    return incK,incL

def line_angle(u, v):
    a = math.atan2(cross(u,v), u@v)
    while a > math.pi/2 + 1e-12: a -= math.pi
    while a < -math.pi/2 - 1e-12: a += math.pi
    return a

# Test multiple configs to confirm: ∡(CB, CA') = -target always
configs=[(70,15,1.4,1.0),(55,25,1.0,1.2),(80,10,1.6,1.1),(45,18,0.9,1.3),(65,8,1.1,0.8),(50,30,1.3,1.0)]
print("Verifying: ∡(CB,CA') = -target (NOT +target as proof's intermediate step claims)")
print(f"{'A':>4} {'al':>4} | {'target':>8} | {'∡(CB,CA\')':>10} {'=+t?':>6} {'=-t?':>6} | {'∡(BC,CA\')':>10} | {'|A\'B|-|A\'C|':>12}")
for (Ad,ald,b,c) in configs:
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
    be,ga=np.radians(x[0]),np.radians(x[1])
    B,C,K,L,M,N,Ap=build_full(A_,al_,be,ga,b,c)
    target = np.pi/2 - A_ - al_
    CB = B-C; CA_ = Ap-C; BC = C-B
    ang_CB_CA = line_angle(CB, CA_)
    ang_BC_CA = line_angle(BC, CA_)
    dist_diff = np.linalg.norm(Ap-B) - np.linalg.norm(Ap-C)
    print(f"{Ad:4d} {ald:4d} | {np.degrees(target):8.4f} | {np.degrees(ang_CB_CA):10.4f} {abs(ang_CB_CA-target)<1e-6!s:>6} {abs(ang_CB_CA+target)<1e-6!s:>6} | {np.degrees(ang_BC_CA):10.4f} | {dist_diff:12.2e}")

print()
print("KEY FINDING: ∡(CB,CA') = -target = -(90-A-α), NOT +target.")
print("The proof's intermediate claim '∡(CB,CA') = 90-A-α' (= +target) is WRONG.")
print("The proof's final claim '∡(BC,CA') = -(90-A-α)' (= -target) is CORRECT,")
print("but reached via a spurious sign flip CB->BC (which doesn't flip sign for lines mod pi).")
print()
print("The correct derivation: the B<->C relabeling produces a CW triangle (opposite orientation).")
print("§2 is proved for CCW triangles; applying to the CW relabeled config negates the signed angle.")
print("So ∡(CB,CA') = -(90-A-α) directly. Since line CB = line BC (mod pi), ∡(BC,CA') = -(90-A-α).")
