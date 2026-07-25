import numpy as np
from scipy.optimize import fsolve

def ang(P,Q,R):
    # angle at Q between QP and QR, unsigned in [0,pi]
    v1 = np.array(P)-np.array(Q)
    v2 = np.array(R)-np.array(Q)
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    c = np.clip(c,-1,1)
    return np.arccos(c)

def dang(P,Q,R):
    # signed angle at Q from QP to QR, in (-pi,pi]
    v1 = np.array(P)-np.array(Q)
    v2 = np.array(R)-np.array(Q)
    a1 = np.arctan2(v1[1],v1[0])
    a2 = np.arctan2(v2[1],v2[0])
    d = a2-a1
    while d>np.pi: d-=2*np.pi
    while d<=-np.pi: d+=2*np.pi
    return d

A = np.array([0.3,2.7])
B = np.array([-1.5,0.0])
C = np.array([2.2,0.1])
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

# initial guess near known instance from prior round
K0 = np.array([-0.8239,0.3649])
L0 = np.array([1.5259,0.4272])

sols = []
for kx in np.linspace(K0[0]-0.3, K0[0]+0.3, 25):
    guess = [K0[1], L0[0], L0[1]]
    sol, info, ier, msg = fsolve(eqs, guess, args=(kx,), full_output=True)
    if ier==1:
        K = np.array([kx, sol[0]])
        L = np.array([sol[1], sol[2]])
        resid = np.max(np.abs(eqs(sol,kx)))
        sols.append((kx,K,L,resid))
        K0 = K; L0 = L

print(f"found {len(sols)} solutions")
for kx,K,L,resid in sols[::5]:
    print(kx, K, L, resid)

def point_in_triangle(P,A,B,C):
    def sign(P1,P2,P3):
        return (P1[0]-P3[0])*(P2[1]-P3[1]) - (P2[0]-P3[0])*(P1[1]-P3[1])
    d1 = sign(P,A,B)
    d2 = sign(P,B,C)
    d3 = sign(P,C,A)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

def inside_angle(P, V, X, Y):
    # is ray VP between rays VX and VY?
    aXY = dang(X,V,Y)
    aXP = dang(X,V,P)
    if aXY>=0:
        return 0<=aXP<=aXY
    else:
        return aXY<=aXP<=0

valid = []
for kx,K,L,resid in sols:
    c1 = point_in_triangle(K,B,M,C)
    c2 = point_in_triangle(L,B,N,C)
    c3 = inside_angle(K,B,L,A)
    c4 = inside_angle(L,C,A,K)
    if c1 and c2 and c3 and c4:
        valid.append((kx,K,L))

print(f"valid configs: {len(valid)} / {len(sols)}")
for kx,K,L in valid:
    print(kx,K,L)

print("\n--- Verify central identity target numerically for each valid config ---")
def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

b = B-A; c = C-A
Qshift = (np.dot(c-b,c+b))/(2*np.dot(c-b,c-b)) * (c-b)
Q = A + Qshift

for kx,K,L in valid[::4]:
    O = circumcenter(A,K,L)
    OM = np.linalg.norm(O-M)
    ON = np.linalg.norm(O-N)
    lhs = np.dot(O-A, C-B)
    rhs = (np.dot(C-A,C-A)-np.dot(B-A,B-A))/4
    # check target identity in A-origin frame: O'.(c-b) = (|c|^2-|b|^2)/4 where O' = O-A
    print(f"kx={kx:.3f}  OM-ON={OM-ON:.2e}  lhs-rhs={lhs-rhs:.2e}")

print("\nQ =", Q)
print("check A,M,N,Q concyclic and A,K,L,Q concyclic (should hold for VALID family only if central identity true)")

def concyclic_resid(P1,P2,P3,P4):
    # using the determinant test
    def f(P):
        return [P[0],P[1],P[0]**2+P[1]**2,1]
    import numpy.linalg as la
    Mtx = np.array([f(P1),f(P2),f(P3),f(P4)])
    return la.det(Mtx)

for kx,K,L in valid[::4]:
    r = concyclic_resid(A,K,L,Q)
    print(f"kx={kx:.3f} concyclic(A,K,L,Q) det={r:.4e}")

print("\n--- Trig / length ratio search across family ---")
def L2(P,Q): return np.linalg.norm(np.array(P)-np.array(Q))

print(f"{'kx':>8} {'AK':>8} {'AL':>8} {'AK/AL':>8} {'BK':>8} {'CL':>8} {'BK/CL':>8} {'MK':>8} {'NL':>8} {'MK/NL':>8} {'KL':>8}")
for kx,K,L in valid:
    AK=L2(A,K); AL=L2(A,L); BK=L2(B,K); CL=L2(C,L); MK=L2(M,K); NL=L2(N,L); KL=L2(K,L)
    print(f"{kx:8.3f} {AK:8.4f} {AL:8.4f} {AK/AL:8.4f} {BK:8.4f} {CL:8.4f} {BK/CL:8.4f} {MK:8.4f} {NL:8.4f} {MK/NL:8.4f} {KL:8.4f}")

print("\n--- Compare AK/AL to AB/AC, AC/AB ---")
AB = L2(A,B); AC = L2(A,C)
print("AB=",AB,"AC=",AC,"AB/AC=",AB/AC,"AC/AB=",AC/AB)
# check with higher precision fsolve (tighten tolerance)
from scipy.optimize import fsolve
kx = -0.8239
sol = fsolve(eqs, [0.3649,1.5259,0.4272], args=(kx,), xtol=1e-14)
K = np.array([kx, sol[0]]); L = np.array([sol[1],sol[2]])
AK=L2(A,K); AL=L2(A,L)
print("high-precision AK/AL =", AK/AL, " residual", eqs(sol,kx))
