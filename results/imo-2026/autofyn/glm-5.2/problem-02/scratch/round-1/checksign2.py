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

def angle_at(vertex, p1, p2):
    """unsigned angle at vertex between rays to p1 and p2"""
    v1 = p1 - vertex; v2 = p2 - vertex
    return math.atan2(abs(cross(v1,v2)), v1@v2)

Ad,ald,b,c = 55,25,1.0,1.2
A_=np.radians(Ad); al_=np.radians(ald)
def f(x):
    be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
be,ga=np.radians(x[0]),np.radians(x[1])
B,C,K,L,M,N,Ap=build_full(A_,al_,be,ga,b,c)
target = np.pi/2 - A_ - al_
A0 = np.array([0.0,0.0])

print(f"Config: A={Ad}°, α={ald}°, β={np.degrees(be):.4f}°, γ={np.degrees(ga):.4f}°")
print(f"target = {np.degrees(target):.4f}°")
print()

# Relabeled: B'=C, C'=B, K'=L, L'=K, M'=N, N'=M
Bp,Cp,Kp,Lp,Mp,Np = C,B,L,K,N,M
print("Relabeled config angle checks (should satisfy same hypotheses with β<->γ):")
print(f"  ∠K'B'A = ∠LCA = {np.degrees(angle_at(C, L, A0)):.4f}° (should be α={ald}°)")
print(f"  ∠AC'L' = ∠ABK = {np.degrees(angle_at(B, A0, K)):.4f}° (should be α={ald}°)")
print(f"  ∠L'B'K' = ∠KCL = {np.degrees(angle_at(C, K, L)):.4f}° (should be γ={np.degrees(ga):.4f}° = new β)")
print(f"  ∠L'N'C' = ∠KMB = {np.degrees(angle_at(M, B, K)):.4f}° (should be γ={np.degrees(ga):.4f}° = new β)")
print(f"  ∠L'C'K' = ∠KBL = {np.degrees(angle_at(B, L, K)):.4f}° (should be β={np.degrees(be):.4f}° = new γ)")
print(f"  ∠B'M'K' = ∠CNL = {np.degrees(angle_at(N, C, L)):.4f}° (should be β={np.degrees(be):.4f}° = new γ)")
print()

# Key: what does §2 say about the relabeled config?
# §2: for a CCW triangle with B' on +x and C' above, ∡(B'C', B'A') = 90 - A - α
# But B'=C is above x-axis, C'=B is on x-axis. So B' is NOT on +x.
# To apply §2, we need to ROTATE the relabeled config so B' is on +x.
# After rotation, C' will be at angle A above x (CCW).
# Let's do this rotation and check.
def rotate_to_bx(Bp, Cp, Kp, Lp, Ap):
    """Rotate so Bp is on +x axis. Return the angle of rotation applied."""
    ang_B = math.atan2(Bp[1], Bp[0])
    # We want to rotate by -ang_B so Bp goes to +x
    # But we also need Cp to be ABOVE x (CCW). If after rotation Cp is below, rotate by pi-ang_B instead.
    theta = -ang_B
    R = np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
    Cp_rot = R@Cp
    if Cp_rot[1] < 0:
        # need to also reflect or rotate by pi
        theta = np.pi - ang_B
        R = np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
        Cp_rot = R@Cp
    return theta, R

theta, R = rotate_to_bx(Bp, Cp, Kp, Lp, Ap)
Bp_r = R@Bp; Cp_r = R@Cp; Ap_r = R@Ap
print(f"After rotating relabeled config (B' on +x, C' above):")
print(f"  B'_rot = ({Bp_r[0]:.6f}, {Bp_r[1]:.6f})")
print(f"  C'_rot = ({Cp_r[0]:.6f}, {Cp_r[1]:.6f}), angle = {np.degrees(math.atan2(Cp_r[1],Cp_r[0])):.4f}° (should be {Ad}°)")
print(f"  angle ∠B'AC' (relabeled, should = A) = {np.degrees(angle_at(A0, Bp_r, Cp_r)):.4f}°")
print()

# In this rotated frame, §2 says: ∡(B'C', B'A') = 90 - A - α = target
# B'C' direction = Cp_r - Bp_r, B'A' direction = Ap_r - Bp_r
BCp = Cp_r - Bp_r; BAp = Ap_r - Bp_r
def line_angle(u, v):
    a = math.atan2(cross(u,v), u@v)
    while a > math.pi/2 + 1e-12: a -= math.pi
    while a < -math.pi/2 - 1e-12: a += math.pi
    return a
print(f"  In rotated frame: ∡(B'C', B'A') = {np.degrees(line_angle(BCp, BAp)):.4f}° (§2 says = {np.degrees(target):.4f}°)")
print()

# Now the GEOMETRIC (frame-independent) directed angle from line B'C' to line B'A'
# = directed angle from line CB to line CA'  (since B'=C, C'=B, A'=A')
# = line_angle(CB, CA') in the original frame
CB = B-C; CA_ = Ap-C
print(f"  Geometric ∡(line CB, line CA') = {np.degrees(line_angle(CB, CA_)):.4f}°")
print(f"  Geometric ∡(line BC, line CA') = {np.degrees(line_angle(C-B, CA_)):.4f}°")
print(f"  §2 predicts ∡(line B'C', B'A') = +{np.degrees(target):.4f}°")
print()
print("CRUX: The relabeled triangle has B'=C(above x), C'=B(on x).")
print("After rotating B' to +x: C' goes BELOW x (CW orientation).")
print("To make CCW, must flip, which reverses directed angles => sign flip.")
print("So §2 on the RELABELED (CCW-normalized) config gives -(target), not +target.")
