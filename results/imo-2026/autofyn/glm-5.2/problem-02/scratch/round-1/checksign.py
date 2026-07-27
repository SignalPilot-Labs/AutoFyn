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

# Single config
Ad,ald,b,c = 55,25,1.0,1.2
A_=np.radians(Ad); al_=np.radians(ald)
def f(x):
    be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
be,ga=np.radians(x[0]),np.radians(x[1])
B,C,K,L,Ap=build(A_,al_,be,ga,b,c)
target = np.pi/2 - A_ - al_
print(f"Config: A={Ad}°, α={ald}°, β={np.degrees(be):.4f}°, γ={np.degrees(ga):.4f}°, b={b}, c={c}")
print(f"target = 90-A-α = {np.degrees(target):.4f}° = {target:.6f} rad")
print()
# Vectors
BC = C-B; BA_ = Ap-B; CA_ = Ap-C; CB = B-C
# The line direction of BC: use the unit vector (C-B)/|C-B|
# For LINES mod pi, the angle between two lines u,v is atan2(|cross|, dot) ... no.
# Directed angle from LINE u to LINE v mod pi = atan2(cross(u,v), dot(u,v)) reduced to (-pi/2, pi/2]

def line_angle(u, v):
    """directed angle from line u to line v, mod pi, in (-pi/2, pi/2]"""
    a = math.atan2(cross(u,v), u@v)
    # reduce to (-pi/2, pi/2]
    while a > math.pi/2 + 1e-12: a -= math.pi
    while a < -math.pi/2 - 1e-12: a += math.pi
    return a

print("LINE convention (mod pi, in (-pi/2, pi/2]):")
print(f"  ∡(BC, BA') = {np.degrees(line_angle(BC, BA_)):.4f}°  (§2 claims = {np.degrees(target):.4f}°)")
print(f"  ∡(CB, CA') = {np.degrees(line_angle(CB, CA_)):.4f}°")
print(f"  ∡(BC, CA') = {np.degrees(line_angle(BC, CA_)):.4f}°  (proof claims = {np.degrees(-target):.4f}°)")
print(f"  ∡(BC, BA') - ∡(BC, CA') = {np.degrees(line_angle(BC,BA_)-line_angle(BC,CA_)):.4f}° (if 0 => BA'∥CA')")
print()
# Check: is A' on perp bisector of BC?
midBC = (B+C)/2
perpBC = np.array([-BC[1], BC[0]])  # perpendicular to BC
print(f"|A'B| = {np.linalg.norm(Ap-B):.10f}")
print(f"|A'C| = {np.linalg.norm(Ap-C):.10f}")
print(f"|A'B|-|A'C| = {np.linalg.norm(Ap-B)-np.linalg.norm(Ap-C):.2e}")
print()
# Now check: does the RELABELED config satisfy the hypotheses AND give ∡(CB,CA')=+target via §2?
# Relabeled: B'=C, C'=B, K'=L, L'=K, M'=N, N'=M, A'=same. β'=γ, γ'=β.
# Check all hypotheses for relabeled config:
B2,C2,K2,L2,M2,N2 = C,B,L,K,N,M
A2 = A_  # same angle
# ∠KBA = ∠ACL: ∠K2 B2 A = ∠A C2 L2 => ∠L C A = ∠A B K
# Check ∠LCA (= angle at C from L to A) and ∠ABK (= angle at B from A to K)
def angle_at(vertex, p1, p2):
    v1 = p1 - vertex; v2 = p2 - vertex
    return math.atan2(abs(cross(v1,v2)), v1@v2)
a1 = angle_at(C2, K2, np.array([0,0]))  # ∠K2 B2 A... wait B2=C(old). ∠K2 B2 A = ∠L C A
# Actually let me just check the 3 equalities for the relabeled config directly.
# ∠K'B'A = ∠A'C'L' => ∠LCA = ∠ABK  
# Original: ∠KBA=∠ACL=α. After relabel: ∠K'B'A=∠LCA=α ✓ (same as ∠ACL=α), ∠A'C'L'=∠ABK=α ✓
print("Relabeled config angle checks:")
print(f"  ∠K'B'A = ∠LCA = {np.degrees(angle_at(C, L, np.array([0,0]))):.4f}° (should be α={ald}°)")
print(f"  ∠AC'L' = ∠ABK = {np.degrees(angle_at(B, np.array([0,0]), K)):.4f}° (should be α={ald}°)")
print(f"  ∠L'B'K' = ∠KCL = {np.degrees(angle_at(C, K, L)):.4f}° (should be γ'={np.degrees(ga):.4f}°)")
print(f"  ∠L'N'C' = ∠KMB = {np.degrees(angle_at(M, B, K)):.4f}° (should be γ'={np.degrees(ga):.4f}°)")
print(f"  ∠L'C'K' = ∠KBL = {np.degrees(angle_at(B, L, K)):.4f}° (should be β'={np.degrees(be):.4f}°)")
print(f"  ∠B'M'K' = ∠CNL = {np.degrees(angle_at(N, C, L)):.4f}° (should be β'={np.degrees(be):.4f}°)")
