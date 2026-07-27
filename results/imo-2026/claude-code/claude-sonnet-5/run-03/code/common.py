"""
Shared geometry helpers used by all verification scripts for the
"OM = ON" olympiad problem (ABC, midpoints M,N of AB,AC; points K,L
inside triangles BMC, BNC satisfying the three angle conditions).

Given a triangle A,B,C and a parameter x = angle(KBA) = angle(ACL),
`solve_KL` numerically finds the point K (on the ray from B making
angle x with BA, rotated toward C) and L (on the ray from C making
angle x with CA, rotated toward B) satisfying the two remaining
angle conditions:
    angle(LBK) = angle(LNC)
    angle(LCK) = angle(BMK)
by solving for the free distances t = BK, s = CL with scipy.
"""

import numpy as np
from scipy.optimize import fsolve


def rot(v, ang):
    c, s = np.cos(ang), np.sin(ang)
    return np.array([[c, -s], [s, c]]) @ v


def angle_at(P, Q, R):
    """Undirected angle QPR at vertex P, between rays PQ and PR."""
    u = Q - P
    v = R - P
    cu = u / np.linalg.norm(u)
    cv = v / np.linalg.norm(v)
    return np.arccos(np.clip(cu @ cv, -1, 1))


def signed_angle_dir(P, Q, R):
    """Signed angle (ccw positive) from ray PQ to ray PR."""
    u = Q - P
    v = R - P
    a1 = np.arctan2(u[1], u[0])
    a2 = np.arctan2(v[1], v[0])
    return (a2 - a1 + np.pi) % (2 * np.pi) - np.pi


def build_KL(A, B, C, x, t, s):
    """K at distance t from B on the x-ray toward C; L at distance s
    from C on the x-ray toward B."""
    dirBA = (A - B) / np.linalg.norm(A - B)
    sgn_B = np.sign(signed_angle_dir(B, A, C))
    K = B + t * rot(dirBA, sgn_B * x)

    dirCA = (A - C) / np.linalg.norm(A - C)
    sgn_C = np.sign(signed_angle_dir(C, A, B))
    L = C + s * rot(dirCA, sgn_C * x)
    return K, L


def _angle_conditions(vars, A, B, C, N, x):
    t, s = vars
    K, L = build_KL(A, B, C, x, t, s)
    M = (A + B) / 2
    e1 = angle_at(B, L, K) - angle_at(N, L, C)   # angle LBK = angle LNC
    e2 = angle_at(C, L, K) - angle_at(M, B, K)   # angle LCK = angle BMK
    return [e1, e2]


def solve_KL(A, B, C, x, guess=(1.0, 1.0)):
    """Solve for (t,s) = (BK,CL) satisfying the two remaining angle
    conditions, given x = angle(KBA) = angle(ACL). Returns (t,s,K,L,ier)."""
    N = (A + C) / 2
    vars, info, ier, msg = fsolve(
        _angle_conditions, guess, args=(A, B, C, N, x), full_output=True
    )
    t, s = vars
    K, L = build_KL(A, B, C, x, t, s)
    return t, s, K, L, ier


def circumcenter(P1, P2, P3):
    ax, ay = P1
    bx, by = P2
    cx, cy = P3
    dd = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay)
          + (cx**2 + cy**2) * (ay - by)) / dd
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx)
          + (cx**2 + cy**2) * (bx - ax)) / dd
    return np.array([ux, uy])


def circumradius(A, B, C):
    a_ = np.linalg.norm(B - C)
    b_ = np.linalg.norm(C - A)
    c_ = np.linalg.norm(A - B)
    s = (a_ + b_ + c_) / 2
    area = np.sqrt(s * (s - a_) * (s - b_) * (s - c_))
    return a_ * b_ * c_ / (4 * area)


def triangle_angles(A, B, C):
    alpha = angle_at(A, B, C)
    beta = angle_at(B, A, C)
    gamma = angle_at(C, A, B)
    return alpha, beta, gamma
