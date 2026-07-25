import numpy as np
from scipy.optimize import fsolve

def ang(P,Q,R):
    v1 = np.array(P)-np.array(Q)
    v2 = np.array(R)-np.array(Q)
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    c = np.clip(c,-1,1)
    return np.arccos(c)

def dang(P,Q,R):
    v1 = np.array(P)-np.array(Q)
    v2 = np.array(R)-np.array(Q)
    a1 = np.arctan2(v1[1],v1[0])
    a2 = np.arctan2(v2[1],v2[0])
    d = a2-a1
    while d>np.pi: d-=2*np.pi
    while d<=-np.pi: d+=2*np.pi
    return d

A = np.array([0.2,3.1])
B = np.array([-2.0,0.0])
C = np.array([3.5,-0.3])
M = (A+B)/2
N = (A+C)/2

def eqs(vars, kx):
    ky,lx,ly = vars
    K = np.array([kx,ky])
    L = np.array([lx,ly])
    e1 = ang(K,B,A) - ang(A,C,L)
    e2 = ang(L,B,K) - ang(L,N,C)
    e3 = ang(L,C,K) - ang(B,M,K)
    return [e1,e2,e3]

K0 = np.array([-1.0,1.0])
L0 = np.array([2.0,1.0])

# find one valid solution first by scanning kx broadly
sols=[]
for kx in np.linspace(-1.9,3.0,400):
    guess=[K0[1],L0[0],L0[1]]
    sol, info, ier, msg = fsolve(eqs, guess, args=(kx,), full_output=True)
    if ier==1:
        resid=np.max(np.abs(eqs(sol,kx)))
        if resid<1e-8:
            K=np.array([kx,sol[0]]); L=np.array([sol[1],sol[2]])
            sols.append((kx,K,L))
            K0=K; L0=L

def point_in_triangle(P,A,B,C):
    def sign(P1,P2,P3):
        return (P1[0]-P3[0])*(P2[1]-P3[1]) - (P2[0]-P3[0])*(P1[1]-P3[1])
    d1 = sign(P,A,B); d2 = sign(P,B,C); d3 = sign(P,C,A)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

def inside_angle(P, V, X, Y):
    aXY = dang(X,V,Y); aXP = dang(X,V,P)
    if aXY>=0: return 0<=aXP<=aXY
    else: return aXY<=aXP<=0

valid=[]
for kx,K,L in sols:
    c1 = point_in_triangle(K,B,M,C)
    c2 = point_in_triangle(L,B,N,C)
    c3 = inside_angle(K,B,L,A)
    c4 = inside_angle(L,C,A,K)
    if c1 and c2 and c3 and c4:
        valid.append((kx,K,L))

print("valid configs:", len(valid))

def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

# inversion centered at A, radius^2 = r2
def inv(P, r2=1.0):
    v = np.array(P)-A
    d2 = np.dot(v,v)
    return A + (r2/d2)*v

print("\n--- Test 1: inversion at A, check K*,L*,B*,C* concyclic ---")
def concyclic_resid(P1,P2,P3,P4):
    def f(P): return [P[0],P[1],P[0]**2+P[1]**2,1]
    Mtx = np.array([f(P1),f(P2),f(P3),f(P4)])
    return np.linalg.det(Mtx)

for kx,K,L in valid[::5]:
    Ks=inv(K); Ls=inv(L); Bs=inv(B); Cs=inv(C)
    r = concyclic_resid(Ks,Ls,Bs,Cs)
    # normalize by coordinate scale
    print(f"kx={kx:.3f} concyclic(K*,L*,B*,C*) det={r:.4e}")

print("\n--- Test 2: inversion at A, check M*,N*,K*,L* concyclic ---")
for kx,K,L in valid[::5]:
    Ks=inv(K); Ls=inv(L); Ms=inv(M); Ns=inv(N)
    r = concyclic_resid(Ms,Ns,Ks,Ls)
    print(f"kx={kx:.3f} concyclic(M*,N*,K*,L*) det={r:.4e}")

print("\n--- Test 3: is K* , B*, M* collinear (inversion turns circle-through-A into line) ---")
def collinear_resid(P,Q,R):
    return (Q[0]-P[0])*(R[1]-P[1])-(Q[1]-P[1])*(R[0]-P[0])
for kx,K,L in valid[::5]:
    Ks=inv(K); Bs=inv(B); Ms=inv(M)
    Ls=inv(L); Cs=inv(C); Ns=inv(N)
    r1=collinear_resid(Ks,Bs,Ms)
    r2=collinear_resid(Ls,Cs,Ns)
    print(f"kx={kx:.3f} collinear(K*,B*,M*)={r1:.4e}  collinear(L*,C*,N*)={r2:.4e}")

print("\n--- Test 4: check if O lies on perp bisector of MN via radical axis of circle(A,B,C) circumcircle and circle(diam MN) ---")
def circle_center_radius_from_diam(P,Q):
    c = (P+Q)/2
    r = np.linalg.norm(P-Q)/2
    return c,r

Oabc = circumcenter(A,B,C)
Rabc = np.linalg.norm(A-Oabc)
Cmn, Rmn = circle_center_radius_from_diam(M,N)
for kx,K,L in valid[::5]:
    O = circumcenter(A,K,L)
    pow_abc = np.dot(O-Oabc,O-Oabc)-Rabc**2
    pow_mn = np.dot(O-Cmn,O-Cmn)-Rmn**2
    print(f"kx={kx:.3f} pow(O,circABC)={pow_abc:.4f} pow(O,circ-diam-MN)={pow_mn:.4f}  diff={pow_abc-pow_mn:.4f}")
