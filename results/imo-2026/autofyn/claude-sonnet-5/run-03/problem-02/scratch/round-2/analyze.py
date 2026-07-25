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
    return np.arccos(np.clip(cosv,-1,1))

def rot(v, theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def K_of(theta, rK):
    BA_dir = (A-B)/np.linalg.norm(A-B)
    return B + rK*rot(BA_dir, -theta)

def L_of(theta, rL):
    CA_dir = (A-C)/np.linalg.norm(A-C)
    return C + rL*rot(CA_dir, theta)

def resid(x, theta):
    rK, rL = x
    K = K_of(theta, rK); L = L_of(theta, rL)
    e1 = ang(B, L, K) - ang(N, L, C)
    e2 = ang(C, L, K) - ang(M, B, K)
    return [e1, e2]

def circumcenter(P1,P2,P3):
    ax,ay=P1; bx,by=P2; cx,cy=P3
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

# Q = reflection of A in perp bisector of MN
def Qpoint():
    b = B-A; c = C-A  # vectors from A
    # solve using formula from lemma: Q = (c-b).(c+b)/(2|c-b|^2) * (c-b), position from A
    num = np.dot(c-b, c+b)
    den = 2*np.dot(c-b,c-b)
    Qvec = (num/den)*(c-b)
    return A + Qvec

Q = Qpoint()

family = []
for theta_deg in np.linspace(5, 70, 260):
    theta = np.radians(theta_deg)
    for rK0 in [0.5,1.0,1.5]:
        for rL0 in [0.5,1.0,1.5]:
            sol, info, ier, msg = fsolve(resid, [rK0,rL0], args=(theta,), full_output=True)
            if ier==1 and sol[0]>0 and sol[1]>0:
                rK, rL = sol
                K = K_of(theta, rK); L = L_of(theta, rL)
                family.append((theta_deg, K, L))
                break
        else:
            continue
        break

print(f"Family size: {len(family)}")

Ovals = []
for theta_deg, K, L in family:
    O = circumcenter(A,K,L)
    OM = np.linalg.norm(O-M); ON = np.linalg.norm(O-N)
    Ovals.append((theta_deg,K,L,O,OM,ON))

# check OM=ON
maxdiff = max(abs(om-on) for _,_,_,_,om,on in Ovals)
print("max |OM-ON| over family:", maxdiff)

print("Q =", Q)

# Test 1: is Q on circle(AKL) i.e. A,K,L,Q concyclic (should hold per current gap)
def concyclic_err(P1,P2,P3,P4):
    O = circumcenter(P1,P2,P3)
    r = np.linalg.norm(O-P1)
    return abs(np.linalg.norm(O-P4)-r)

for theta_deg,K,L,O,om,on in Ovals[:5]:
    e = concyclic_err(A,K,L,Q)
    print(f"theta={theta_deg:.2f}  concyclic(A,K,L,Q) err={e:.3e}")

print("\n--- Locus tests: does K (or L) trace a fixed circle as theta varies? ---")
Ks = np.array([K for _,K,_,_,_,_ in Ovals])
Ls = np.array([L for _,_,L,_,_,_ in Ovals])

def fit_circle(pts):
    # algebraic circle fit: x^2+y^2 + D x + E y + F = 0
    x = pts[:,0]; y = pts[:,1]
    Amat = np.column_stack([x,y,np.ones_like(x)])
    b = -(x**2+y**2)
    sol, res, rank, sv = np.linalg.lstsq(Amat,b,rcond=None)
    D,E,F = sol
    cx,cy = -D/2,-E/2
    r = np.sqrt(cx**2+cy**2-F)
    # residuals
    resid = np.sqrt((x-cx)**2+(y-cy)**2) - r
    return (cx,cy,r), resid

(cxK,cyK,rK),residK = fit_circle(Ks[:50])
print("K locus best-fit circle center,r:", cxK,cyK,rK, "max resid:", np.max(np.abs(residK)))
(cxL,cyL,rL),residL = fit_circle(Ls[:50])
print("L locus best-fit circle center,r:", cxL,cyL,rL, "max resid:", np.max(np.abs(residL)))

print("\n--- Test candidate spiral similarity centered at K sending B->L (angle+ratio) ---")
for theta_deg,K,L,O,om,on in Ovals[::40]:
    angBKL = ang(K,B,L)  # not quite; need directed
    KB = np.linalg.norm(K-B); KL=np.linalg.norm(K-L)
    print(f"theta={theta_deg:.1f} |KB|/|KL|={KB/KL:.4f}")
