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

def cross2(u,v):
    return u[0]*v[1]-u[1]*v[0]

guess=[2.0,2.0]
for theta in np.linspace(0.05,0.95,10):
    sol, info, ier, msg = fsolve(equations, guess, args=(theta,), full_output=True)
    if ier!=1: continue
    t,s = sol
    K,L = build_KL(theta,t,s)
    guess=[t,s]
    u = K-A
    v = L-A
    D = C-B
    det = cross2(u,v)
    p = cross2(D,v)/det
    q = cross2(u,D)/det
    AK2 = np.dot(u,u)
    AL2 = np.dot(v,v)
    AB2 = np.dot(B-A,B-A)
    AC2 = np.dot(C-A,C-A)
    lhs = 2*p*AK2 + 2*q*AL2
    rhs = AC2-AB2
    print(f"theta={theta:.3f} p={p:.4f} q={q:.4f} lhs={lhs:.5f} rhs={rhs:.5f} diff={lhs-rhs:.2e}")
