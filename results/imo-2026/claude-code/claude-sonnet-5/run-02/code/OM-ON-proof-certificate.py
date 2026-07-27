"""
Verification certificate for: Let ABC be a triangle, M,N midpoints of AB,AC.
K inside triangle BMC, L inside triangle BNC, with K inside angle LBA, L inside
angle ACK, angle KBA = angle ACL, angle LBK = angle LNC, angle LCK = angle BMK.
O = circumcenter(AKL). Prove OM = ON.

This script reproduces the two pieces of evidence behind the written proof:

  PART A (ground truth, numeric):
    Solve the THREE ORIGINAL angle conditions directly (no reformulation),
    check all four "inside" hypotheses from the problem statement, then
    check OM = ON, and separately check the two concyclicities claimed by
    the proof's key lemma (Claim 2):
        M, C, Z, K concyclic      and      N, B, Z', L concyclic
    where Z = ray CL meet line AB, Z' = ray BK meet line AC.

  PART B (exact symbolic certificate):
    In closed form (A at the origin, circumradius(ABC) = 1), build the two
    concyclicity conditions as polynomials F_K(t_K), F_L(t_L) (t_K = BK,
    t_L = CL), and build E, the polynomial form of the target vector
    identity  AO . CB = (AB^2 - AC^2)/4  (equivalent to OM = ON).
    Verify by exact polynomial division that

        E  =  Q1 * F_K  +  Q2 * F_L      (identically, zero remainder)

    which proves E = 0 whenever F_K = F_L = 0, i.e. whenever Claim 2 holds.
    This is the crux algebraic fact the proof relies on.

Run with: python3 OM-ON-proof-certificate.py
Requires: numpy, scipy, sympy
"""

import numpy as np
from scipy.optimize import brentq
import sympy as sp


# ===========================================================================
# PART A: numeric ground-truth check against the ORIGINAL problem statement
# ===========================================================================

def angle(P, V, Q):
    """Undirected angle PVQ in radians."""
    a = np.array(P) - np.array(V)
    b = np.array(Q) - np.array(V)
    c = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return np.arccos(min(1, max(-1, c)))


def circumcenter(P1, P2, P3):
    ax, ay = P1; bx, by = P2; cx, cy = P3
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay)
          + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx)
          + (cx**2 + cy**2) * (bx - ax)) / d
    return np.array([ux, uy])


def in_triangle(P, X, Y, Z):
    def s(p1, p2, p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    d1, d2, d3 = s(P, X, Y), s(P, Y, Z), s(P, Z, X)
    return not ((d1 < 0 or d2 < 0 or d3 < 0) and (d1 > 0 or d2 > 0 or d3 > 0))


def ray_between(P, V, Q1, Q2):
    """Is ray V->P strictly between rays V->Q1 and V->Q2?"""
    a1, a2, a12 = angle(Q1, V, P), angle(P, V, Q2), angle(Q1, V, Q2)
    return abs(a1 + a2 - a12) < 1e-9


def solve_original_conditions(A, B, C, theta):
    """Solve the THREE conditions of the problem directly (no lemmas used)."""
    A, B, C = map(lambda p: np.array(p, float), (A, B, C))
    M, N = (A + B) / 2, (A + C) / 2

    vA = A - B
    dirBK = np.arctan2(vA[1], vA[0]) - theta
    K_of = lambda k: B + k * np.array([np.cos(dirBK), np.sin(dirBK)])

    vA2 = A - C
    dirCL = np.arctan2(vA2[1], vA2[0]) + theta
    L_of = lambda l: C + l * np.array([np.cos(dirCL), np.sin(dirCL)])

    # condition (3): angle LCK = angle BMK  -> pins K (independent of l)
    f = lambda k: angle(B, M, K_of(k)) - angle(L_of(1.0), C, K_of(k))
    K = K_of(brentq(f, 1e-6, 30))

    # condition (2): angle LBK = angle LNC  -> pins L (independent of k)
    g = lambda l: angle(L_of(l), B, K) - angle(L_of(l), N, C)
    L = L_of(brentq(g, 1e-6, 30))

    return A, B, C, M, N, K, L


def part_A(A, B, C, theta_deg, label):
    print(f"--- Part A: {label}  (theta = {theta_deg} deg) ---")
    A, B, C, M, N, K, L = solve_original_conditions(A, B, C, np.radians(theta_deg))
    alpha = angle(B, A, C)

    # the three GIVEN conditions, checked directly
    print("  angle KBA vs angle ACL      :", np.degrees(angle(K, B, A)), np.degrees(angle(A, C, L)))
    print("  angle LBK vs angle LNC      :", np.degrees(angle(L, B, K)), np.degrees(angle(L, N, C)))
    print("  angle LCK vs angle BMK      :", np.degrees(angle(L, C, K)), np.degrees(angle(B, M, K)))

    # the four GIVEN configuration hypotheses
    print("  K inside triangle BMC       :", in_triangle(K, B, M, C))
    print("  L inside triangle BNC       :", in_triangle(L, B, N, C))
    print("  K inside angle LBA          :", ray_between(K, B, L, A))
    print("  L inside angle ACK          :", ray_between(L, C, A, K))

    # the proof's key lemma (Claim 2): M,C,Z,K and N,B,Z',L concyclic
    def line_ray_intersect(P0, dirv, Q0, Q1):
        Mtx = np.array([[dirv[0], -(Q1-Q0)[0]], [dirv[1], -(Q1-Q0)[1]]])
        t, s = np.linalg.solve(Mtx, Q0 - P0)
        return P0 + t * dirv

    vA = A - B
    dirCL = np.array([np.cos(np.arctan2((A-C)[1], (A-C)[0]) + np.radians(theta_deg)),
                       np.sin(np.arctan2((A-C)[1], (A-C)[0]) + np.radians(theta_deg))])
    Z = line_ray_intersect(C, dirCL, A, B)
    dirBK = np.array([np.cos(np.arctan2(vA[1], vA[0]) - np.radians(theta_deg)),
                       np.sin(np.arctan2(vA[1], vA[0]) - np.radians(theta_deg))])
    Zp = line_ray_intersect(B, dirBK, A, C)

    def concyclic_det(P1, P2, P3, P4):
        row = lambda P: [P[0]**2 + P[1]**2, P[0], P[1], 1]
        return np.linalg.det(np.array([row(P1), row(P2), row(P3), row(P4)]))

    print("  M,C,Z,K concyclic  (det~0)  :", concyclic_det(M, C, Z, K))
    print("  N,B,Z',L concyclic (det~0)  :", concyclic_det(N, B, Zp, L))
    print("  angle AZC vs pi-alpha-theta :", np.degrees(angle(A, Z, C)),
          180 - np.degrees(alpha) - theta_deg)

    O = circumcenter(A, K, L)
    OM, ON = np.linalg.norm(O - M), np.linalg.norm(O - N)
    print(f"  OM = {OM:.12f}   ON = {ON:.12f}   |OM-ON| = {abs(OM-ON):.2e}")
    print()


part_A((0, 3), (-2, 0), (4, 0), 20, "scalene triangle #1")
part_A((1.5, 4.2), (-2.3, -0.5), (3.7, -1.1), 12, "scalene triangle #2")


# ===========================================================================
# PART B: exact symbolic certificate for the algebraic core of the proof
# ===========================================================================

print("=" * 70)
print("Part B: exact symbolic identity  E = Q1*F_K + Q2*F_L")
print("=" * 70)

ca, sa, cb, sb, ct, st, tK, tL = sp.symbols('ca sa cb sb ct st tK tL', real=True)
# ca,sa = cos(alpha),sin(alpha); cb,sb = cos(beta),sin(beta); ct,st = cos(theta),sin(theta)
# gamma = pi - alpha - beta ;  A is placed at the origin, circumradius(ABC) = 1

sg = sa*cb + ca*sb                      # sin(gamma)

A = sp.Matrix([0, 0])
B = sp.Matrix([2*sg, 0])                # AB = 2 sin(gamma)
C = sp.Matrix([2*sb*ca, 2*sb*sa])       # AC = 2 sin(beta), at angle alpha from AB
M, N = B/2, C/2

dirBK = sp.Matrix([-ct, st])                                   # ray BK direction
dirCL = sp.Matrix([sa*st - ca*ct, -sa*ct - ca*st])              # ray CL direction

K = B + tK*dirBK
L = C + tL*dirCL

# Z = ray CL meet line AB (the x-axis);  Z' = ray BK meet line AC
tZ = sp.together(-C[1]/dirCL[1])
Z = sp.Matrix([sp.simplify(C[0] + tZ*dirCL[0]), 0])

t_, u_ = sp.symbols('t_ u_', real=True)
sol = sp.solve([sp.Eq((B + t_*dirBK)[0], u_*C[0]),
                sp.Eq((B + t_*dirBK)[1], u_*C[1])], [t_, u_])
Zp = sp.simplify(B + sol[t_]*dirBK)

def concyclic_det(P1, P2, P3, P4):
    row = lambda P: [P[0]**2 + P[1]**2, P[0], P[1], 1]
    return sp.Matrix([row(P1), row(P2), row(P3), row(P4)]).det()

F_K = sp.expand(concyclic_det(M, C, Z, K))     # Lemma (Claim 2) for K, as a poly in tK
F_L = sp.expand(concyclic_det(N, B, Zp, L))    # Lemma (Claim 2) for L, as a poly in tL

Kx, Ky = K; Lx, Ly = L; Bx, By = B; Cx, Cy = C
K2, L2 = sp.expand(Kx**2+Ky**2), sp.expand(Lx**2+Ly**2)
D = sp.expand(Kx*Ly - Ky*Lx)
B2, C2 = sp.expand(Bx**2+By**2), sp.expand(Cx**2+Cy**2)

# E = polynomial (denominator-cleared) form of  AO.CB = (AB^2-AC^2)/4   <=>  OM=ON
E = sp.expand(2*((K2*Ly - L2*Ky)*(Bx-Cx) + (Kx*L2 - Lx*K2)*(By-Cy)) - D*(B2 - C2))

q1, r1 = sp.div(sp.Poly(E, tK), sp.Poly(F_K, tK))
r1e = sp.expand(r1.as_expr())
q2, r2 = sp.div(sp.Poly(r1e, tL), sp.Poly(F_L, tL))
r2e = sp.expand(r2.as_expr())

print("deg_tK(F_K) =", sp.degree(F_K, tK), "   deg_tL(F_L) =", sp.degree(F_L, tL))
print("remainder of E mod (F_K, F_L), fully reduced:", r2e)
print("=> E lies in the ideal <F_K, F_L>:", r2e == 0)
