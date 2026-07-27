import numpy as np
from scipy.optimize import fsolve

A = np.array([0.0, 0.0])
B = np.array([5.0, 0.3])
C = np.array([1.2, 4.0])

M = (A+B)/2
N = (A+C)/2

def rot(v, ang):
    c,s = np.cos(ang), np.sin(ang)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def angle_between(u,v):
    cu = u/np.linalg.norm(u)
    cv = v/np.linalg.norm(v)
    d = np.clip(np.dot(cu,cv), -1, 1)
    return np.arccos(d)

def signed_angle(u,v):
    a1 = np.arctan2(u[1],u[0])
    a2 = np.arctan2(v[1],v[0])
    d = a2-a1
    while d>np.pi: d-=2*np.pi
    while d<=-np.pi: d+=2*np.pi
    return d

def cross(u,v):
    return u[0]*v[1]-u[1]*v[0]

def point_in_triangle(P, X, Y, Z):
    d1 = cross(Y-X, P-X)
    d2 = cross(Z-Y, P-Y)
    d3 = cross(X-Z, P-Z)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

def build_KL(theta, t, s):
    dirBA = A-B
    dirBC = C-B
    sgn = np.sign(signed_angle(dirBA,dirBC))
    dir1 = rot(dirBA, sgn*theta)
    K = B + t*dir1/np.linalg.norm(dir1)

    dirCA = A-C
    dirCB = B-C
    sgn2 = np.sign(signed_angle(dirCA,dirCB))
    dir2 = rot(dirCA, sgn2*theta)
    L = C + s*dir2/np.linalg.norm(dir2)
    return K, L

def equations(vars, theta):
    t,s = vars
    K,L = build_KL(theta,t,s)
    aLBK = angle_between(L-B, K-B)
    aLNC = angle_between(L-N, C-N)
    aLCK = angle_between(L-C, K-C)
    aBMK = angle_between(B-M, K-M)
    return [aLBK-aLNC, aLCK-aBMK]

def circumcenter(P,Q,R):
    ax,ay = P; bx,by=Q; cx,cy=R
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

guess = [2.0, 2.0]
results = []
for theta in np.linspace(0.05, 1.0, 40):
    sol, info, ier, msg = fsolve(equations, guess, args=(theta,), full_output=True)
    if ier != 1:
        continue
    t,s = sol
    if t<=0 or s<=0:
        continue
    K,L = build_KL(theta, t, s)
    inBMC = point_in_triangle(K,B,M,C)
    inBNC = point_in_triangle(L,B,N,C)
    if not (inBMC and inBNC):
        continue
    # check K inside angle LBA: ray BK between BA and BL
    # check L inside angle ACK: ray CL between CA and CK
    angBA = np.arctan2(*(A-B)[::-1])
    angBK = np.arctan2(*(K-B)[::-1])
    angBL = np.arctan2(*(L-B)[::-1])
    def between(angMid_target, ang1, ang2):
        # check angle target lies between ang1 and ang2 going the "short way" appropriately;
        # use signed_angle relative
        d1 = signed_angle(np.array([np.cos(ang1),np.sin(ang1)]), np.array([np.cos(angMid_target),np.sin(angMid_target)]))
        d2 = signed_angle(np.array([np.cos(ang1),np.sin(ang1)]), np.array([np.cos(ang2),np.sin(ang2)]))
        return (d1>0 and d1<d2) or (d1<0 and d1>d2)
    cond1 = between(angBK, angBA, angBL)

    angCA = np.arctan2(*(A-C)[::-1])
    angCK = np.arctan2(*(K-C)[::-1])
    angCL = np.arctan2(*(L-C)[::-1])
    cond2 = between(angCL, angCA, angCK)

    O = circumcenter(A,K,L)
    OM = np.linalg.norm(O-M)
    ON = np.linalg.norm(O-N)
    results.append((theta,t,s,cond1,cond2,OM,ON,OM-ON))
    guess = [t,s]

for r in results:
    print(f"theta={r[0]:.3f} t={r[1]:.3f} s={r[2]:.3f} cond1={r[3]} cond2={r[4]} OM={r[5]:.5f} ON={r[6]:.5f} diff={r[7]:.2e}")

print()
print("Testing spiral similarity hypothesis: is (K-A)/(B-A) == (L-A)/(C-A) ?")
guess = [2.0, 2.0]
for theta in np.linspace(0.05, 0.95, 10):
    sol, info, ier, msg = fsolve(equations, guess, args=(theta,), full_output=True)
    if ier != 1:
        continue
    t,s = sol
    K,L = build_KL(theta, t, s)
    guess=[t,s]
    Kc = complex(*(K-A))
    Lc = complex(*(L-A))
    Bc = complex(*(B-A))
    Cc = complex(*(C-A))
    r1 = Kc/Bc
    r2 = Lc/Cc
    print(f"theta={theta:.3f}  K/B={r1:.5f}  L/C={r2:.5f}  ratio diff={abs(r1-r2):.2e}")
