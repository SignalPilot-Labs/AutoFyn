import numpy as np
from scipy.optimize import fsolve

# Triangle ABC, generic scalene
A = np.array([0.0, 0.0])
B = np.array([5.0, 0.3])
C = np.array([1.2, 4.0])

M = (A+B)/2
N = (A+C)/2

def rot(v, ang):
    c,s = np.cos(ang), np.sin(ang)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def angle_between(u,v):
    # unsigned angle between vectors u,v
    cu = u/np.linalg.norm(u)
    cv = v/np.linalg.norm(v)
    d = np.clip(np.dot(cu,cv), -1, 1)
    return np.arccos(d)

def signed_angle(u,v):
    # signed angle from u to v (rotation), in (-pi,pi]
    a1 = np.arctan2(u[1],u[0])
    a2 = np.arctan2(v[1],v[0])
    d = a2-a1
    while d>np.pi: d-=2*np.pi
    while d<=-np.pi: d+=2*np.pi
    return d

# orientation of triangle ABC
def cross(u,v):
    return u[0]*v[1]-u[1]*v[0]

orient = np.sign(cross(B-A, C-A))
print("orientation sign", orient)

def build_KL(theta, t, s):
    # theta = angle KBA = angle ACL
    # K on ray from B, direction = rotate (A-B) towards C by angle theta
    dirBA = A-B
    dirBC = C-B
    # rotate dirBA towards dirBC by angle theta (theta measured as positive going from BA to BC)
    total = angle_between(dirBA,dirBC)
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
    # angle LBK = angle LNC
    aLBK = angle_between(L-B, K-B)
    aLNC = angle_between(L-N, C-N)
    # angle LCK = angle BMK
    aLCK = angle_between(L-C, K-C)
    aBMK = angle_between(B-M, K-M)
    return [aLBK-aLNC, aLCK-aBMK]

# try to find solution for a given theta
theta0 = 0.3
# initial guesses for t,s (distances)
guess = [2.0, 2.0]
sol = fsolve(equations, guess, args=(theta0,), full_output=True)
x, info, ier, msg = sol
print("theta0 solve:", x, ier, msg)
K,L = build_KL(theta0, *x)
print("K",K,"L",L)
