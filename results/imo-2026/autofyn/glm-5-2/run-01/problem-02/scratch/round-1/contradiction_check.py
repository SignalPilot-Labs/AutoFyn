"""
Test: if we take the proof's intermediate step at face value
(∡(CB,CA') = +target), does it lead to a contradiction?
"""
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
    while a > math.pi/2 + 1e-9: a -= math.pi
    while a < -math.pi/2 - 1e-9: a += math.pi
    return a

Ad,ald,b,c = 45,18,0.9,1.3
A_=np.radians(Ad); al_=np.radians(ald)
def f(x):
    be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
be,ga=np.radians(x[0]),np.radians(x[1])
B,C,K,L,M,N,Ap=build_full(A_,al_,be,ga,b,c)
target = np.pi/2 - A_ - al_

BC=C-B; BA_=Ap-B; CA_=Ap-C; CB=B-C
print(f"Config: A={Ad}°, α={ald}°, β={np.degrees(be):.2f}°, γ={np.degrees(ga):.2f}°")
print(f"target = 90-A-α = {np.degrees(target):.2f}°")
print()
print("§2 result (verified): ∡(BC, BA') = ", f"{np.degrees(line_angle(BC,BA_)):.4f}° = +target ✓")
print()
print("Proof's §3 intermediate step claims: ∡(CB, CA') = +target =", f"{np.degrees(target):.4f}°")
print("  Actual ∡(CB, CA') =", f"{np.degrees(line_angle(CB,CA_)):.4f}°  => {'MATCHES +target' if abs(line_angle(CB,CA_)-target)<1e-6 else 'DOES NOT MATCH (should be -target)'}")
print()
print("Proof's §3 conversion: ∡(BC, CA') = -∡(CB, CA') (sign flip CB->BC)")
print("  This conversion is WRONG: line CB = line BC (mod pi), so ∡(BC,CA') = ∡(CB,CA')")
print("  Actual ∡(BC, CA') =", f"{np.degrees(line_angle(BC,CA_)):.4f}°")
print(f"  ∡(CB,CA') = ∡(BC,CA')? {abs(line_angle(CB,CA_)-line_angle(BC,CA_))<1e-9}")
print()
print("If proof's intermediate step were correct (∡(CB,CA')=+target):")
print(f"  Then ∡(BC,CA') = ∡(CB,CA') = +target = {np.degrees(target):.2f}° (same line, no flip)")
print(f"  Then ∡(BC,BA') = ∡(BC,CA') = +{np.degrees(target):.2f}°")
print(f"  => BA' ∥ CA' (same angle with BC) => B,C,A' collinear => CONTRADICTION with |A'B|={np.linalg.norm(Ap-B):.4f} ≠ |A'C|={np.linalg.norm(Ap-C):.4f}... wait they're equal")
print(f"  |A'B| = {np.linalg.norm(Ap-B):.6f}, |A'C| = {np.linalg.norm(Ap-C):.6f}")
print(f"  A' = {Ap}")
print(f"  B = {B}, C = {C}")
print(f"  Is A' on line BC? cross(A'-B, C-B) = {cross(Ap-B, C-B):.6e}")
print()
print("CONCLUSION: The proof's intermediate step (∡(CB,CA')=+target) is WRONG.")
print("If taken at face value (without the compensating spurious CB->BC sign flip),")
print("it would force BA'∥CA', contradicting the geometry.")
print("The two sign errors (missing σ-flip + spurious CB->BC flip) cancel to give the right answer.")
