import numpy as np
from scipy.optimize import fsolve

A = np.array([0.3, 2.7])
B = np.array([-1.5, 0.0])
C = np.array([2.2, 0.1])
M = (A+B)/2
N = (A+C)/2

def ang(P, Q, R):
    u = Q-P; v = R-P
    cosv = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
    cosv = np.clip(cosv,-1,1)
    return np.arccos(cosv)

def rot(v, theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def K_of(theta, rK):
    BA = A-B
    BA_dir = BA/np.linalg.norm(BA)
    d = rot(BA_dir, -theta)
    return B + rK*d

def L_of(theta, rL):
    CA = A-C
    CA_dir = CA/np.linalg.norm(CA)
    d = rot(CA_dir, theta)
    return C + rL*d

def resid(x, theta):
    rK, rL = x
    K = K_of(theta, rK)
    L = L_of(theta, rL)
    e1 = ang(B, L, K) - ang(N, L, C)
    e2 = ang(C, L, K) - ang(M, B, K)
    return [e1, e2]

def inside_triangle(P, X, Y, Z):
    def sign(p1,p2,p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    d1 = sign(P,X,Y); d2 = sign(P,Y,Z); d3 = sign(P,Z,X)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

def between_rays(P, X, Y, T):
    ux, uy = X-P; vx, vy = Y-P
    tx, ty = T-P
    def cross(a,b,c,d): return a*d-b*c
    c1 = cross(ux,uy,tx,ty); c2 = cross(tx,ty,vx,vy); c3 = cross(ux,uy,vx,vy)
    return (c1*c3 >= -1e-9) and (c2*c3 >= -1e-9)

results = []
for theta_deg in np.linspace(5, 80, 150):
    theta = np.radians(theta_deg)
    for rK0 in [0.5,1.0,1.5,2.0]:
        for rL0 in [0.5,1.0,1.5,2.0]:
            try:
                sol = fsolve(resid, [rK0,rL0], args=(theta,), full_output=True)
                x, info, ier, msg = sol
                if ier==1 and x[0]>0 and x[1]>0:
                    rK, rL = x
                    K = K_of(theta, rK); L = L_of(theta, rL)
                    if inside_triangle(K,B,M,C) and inside_triangle(L,B,N,C):
                        results.append((theta_deg, rK, rL, K.copy(), L.copy()))
            except Exception:
                pass

seen = {}
for theta_deg, rK, rL, K, L in results:
    key = round(theta_deg,3)
    if key not in seen: seen[key]=(rK,rL,K,L)

good=[]
for k in sorted(seen):
    rK,rL,K,L = seen[k]
    if between_rays(B,L,A,K) and between_rays(C,A,K,L):
        good.append((k,K,L))
print(f"{len(good)} valid configs")

def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

# sanity: verify OM=ON on these configs
print("\n--- sanity OM=ON ---")
for k,K,L in good[::20]:
    O = circumcenter(A,K,L)
    print(f"theta={k:.2f} OM-ON={np.linalg.norm(O-M)-np.linalg.norm(O-N):.2e}")

def inv(P, r2=1.0):
    v = np.array(P)-A
    d2 = np.dot(v,v)
    return A + (r2/d2)*v

def concyclic_resid(P1,P2,P3,P4):
    def f(P): return [P[0],P[1],P[0]**2+P[1]**2,1]
    Mtx = np.array([f(P1),f(P2),f(P3),f(P4)])
    return np.linalg.det(Mtx)

def collinear_resid(P,Q,R):
    return (Q[0]-P[0])*(R[1]-P[1])-(Q[1]-P[1])*(R[0]-P[0])

print("\n--- Test1: inversion at A: K*,L*,B*,C* concyclic? (det, normalized) ---")
for k,K,L in good[::20]:
    Ks=inv(K); Ls=inv(L); Bs=inv(B); Cs=inv(C)
    r = concyclic_resid(Ks,Ls,Bs,Cs)
    print(f"theta={k:.2f} det={r:.4e}")

print("\n--- Test2: inversion at A: M*,N*,K*,L* concyclic? ---")
for k,K,L in good[::20]:
    Ks=inv(K); Ls=inv(L); Ms=inv(M); Ns=inv(N)
    r = concyclic_resid(Ms,Ns,Ks,Ls)
    print(f"theta={k:.2f} det={r:.4e}")

print("\n--- Test3: K*,B*,M* collinear? L*,C*,N* collinear? (circle-through-A hyps become lines under inversion) ---")
for k,K,L in good[::20]:
    Ks=inv(K); Bs=inv(B); Ms=inv(M)
    Ls=inv(L); Cs=inv(C); Ns=inv(N)
    r1=collinear_resid(Ks,Bs,Ms); r2=collinear_resid(Ls,Cs,Ns)
    print(f"theta={k:.2f} col(K*,B*,M*)={r1:.4e} col(L*,C*,N*)={r2:.4e}")

print("\n--- Test4: O relative to circumcircle(ABC) and circle(diam MN) radical axis ---")
def circle_from_diam(P,Q):
    c=(P+Q)/2; r=np.linalg.norm(P-Q)/2
    return c,r
Oabc = circumcenter(A,B,C)
Rabc = np.linalg.norm(A-Oabc)
Cmn,Rmn = circle_from_diam(M,N)
for k,K,L in good[::20]:
    O = circumcenter(A,K,L)
    pow_abc = np.dot(O-Oabc,O-Oabc)-Rabc**2
    pow_mn = np.dot(O-Cmn,O-Cmn)-Rmn**2
    print(f"theta={k:.2f} pow_abc={pow_abc:.4f} pow_mn={pow_mn:.4f} diff={pow_abc-pow_mn:.4f}")

print("\n--- Test5: does K lie on circle(A,B,M)? does L lie on circle(A,C,N)? (single-point membership, no L/K cross) ---")
for k,K,L in good[::20]:
    r1 = concyclic_resid(A,B,M,K)
    r2 = concyclic_resid(A,C,N,L)
    print(f"theta={k:.2f} K-on-circ(A,B,M)={r1:.4e}  L-on-circ(A,C,N)={r2:.4e}")

print("\n--- Test6: power of A wrt circle(K,B,M) times power of A wrt circle(L,C,N)? or ratio trends ---")
def circumcenter_radius(P,Q,R):
    O = circumcenter(P,Q,R)
    Rr = np.linalg.norm(P-O)
    return O,Rr
for k,K,L in good[::20]:
    Ok,Rk = circumcenter_radius(K,B,M)
    Ol,Rl = circumcenter_radius(L,C,N)
    powA_k = np.dot(A-Ok,A-Ok)-Rk**2
    powA_l = np.dot(A-Ol,A-Ol)-Rl**2
    print(f"theta={k:.2f} powA(KBM)={powA_k:.4f} powA(LCN)={powA_l:.4f} ratio={powA_k/powA_l:.4f}")

print("\n--- HIGH PRECISION check of Test6 constant claim ---")
for k,K,L in good:
    Ok,Rk = circumcenter_radius(K,B,M)
    Ol,Rl = circumcenter_radius(L,C,N)
    powA_k = np.dot(A-Ok,A-Ok)-Rk**2
    powA_l = np.dot(A-Ol,A-Ol)-Rl**2
    print(f"theta={k:8.3f} powA(KBM)={powA_k:.10f} powA(LCN)={powA_l:.10f}")
