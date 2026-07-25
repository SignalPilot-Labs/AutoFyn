import numpy as np
from scipy.optimize import fsolve, brentq

# Triangle (scalene, matches round-1 style)
A = np.array([0.3, 2.7])
B = np.array([-1.5, 0.0])
C = np.array([2.2, 0.1])
M = (A+B)/2
N = (A+C)/2

def ang(P, Q, R):
    # angle QPR at vertex P (unsigned, in [0,pi])
    u = Q-P; v = R-P
    cosv = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
    cosv = np.clip(cosv,-1,1)
    return np.arccos(cosv)

def rot(v, theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def K_of(theta, rK):
    # K on ray from B making angle theta with BA, on the side toward interior of triangle (toward C)
    BA = A-B
    BA_dir = BA/np.linalg.norm(BA)
    # rotate BA_dir by -theta (clockwise, toward C side) -- need to determine sign by testing
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
    e1 = ang(B, L, K) - ang(N, L, C)   # hyp2: LBK = LNC
    e2 = ang(C, L, K) - ang(M, B, K)   # hyp3: LCK = BMK
    return [e1, e2]

def inside_triangle(P, X, Y, Z):
    # barycentric sign test
    def sign(p1,p2,p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    d1 = sign(P,X,Y)
    d2 = sign(P,Y,Z)
    d3 = sign(P,Z,X)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

def inside_angle(P, V, W, X):
    # is P inside angle V at vertex... actually check "K inside angle LBA" meaning
    # ray B->K between ray B->L and ray B->A
    pass

results = []
for theta_deg in np.linspace(5, 80, 60):
    theta = np.radians(theta_deg)
    # initial guess
    for rK0 in [0.5,1.0,1.5,2.0]:
        for rL0 in [0.5,1.0,1.5,2.0]:
            try:
                sol = fsolve(resid, [rK0,rL0], args=(theta,), full_output=True)
                x, info, ier, msg = sol
                if ier==1 and x[0]>0 and x[1]>0:
                    rK, rL = x
                    K = K_of(theta, rK)
                    L = L_of(theta, rL)
                    # check containments
                    inBMC = inside_triangle(K,B,M,C)
                    inBNC = inside_triangle(L,B,N,C)
                    if inBMC and inBNC:
                        results.append((theta_deg, rK, rL, K.copy(), L.copy()))
            except Exception:
                pass

# dedupe close results per theta
print(f"found {len(results)} raw solutions")
seen = {}
for theta_deg, rK, rL, K, L in results:
    key = round(theta_deg,3)
    if key not in seen:
        seen[key] = (rK,rL,K,L)

print(f"{len(seen)} unique theta values with a solution")
for k in sorted(seen)[:10]:
    rK,rL,K,L = seen[k]
    print(k, rK, rL, K, L)

def between_rays(P, X, Y, T):
    # is ray P->T between ray P->X and ray P->Y (angle test via cross product signs)
    ux, uy = X-P; vx, vy = Y-P
    tx, ty = T-P
    def cross(a,b,c,d): return a*d-b*c
    c1 = cross(ux,uy,tx,ty)
    c2 = cross(tx,ty,vx,vy)
    c3 = cross(ux,uy,vx,vy)
    # T between X,Y (going X->Y) if c1,c2 same sign as c3 (or zero)
    return (c1*c3 >= -1e-9) and (c2*c3 >= -1e-9)

good = []
for k in sorted(seen):
    rK,rL,K,L = seen[k]
    cond1 = between_rays(B, L, A, K)   # K inside angle LBA
    cond2 = between_rays(C, A, K, L)   # L inside angle ACK
    if cond1 and cond2:
        good.append((k,rK,rL,K,L))

print(f"{len(good)} solutions satisfying ALL FOUR conditions")
for k,rK,rL,K,L in good:
    print(k, K, L)
