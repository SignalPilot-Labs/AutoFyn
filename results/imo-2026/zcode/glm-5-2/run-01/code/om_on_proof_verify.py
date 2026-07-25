"""
Rigorous computer-verified proof that OM = ON for the configuration:

  ABC triangle, M,N midpoints of AB,AC. K in BMC, L in BNC with
    angle KBA = angle ACL,
    angle LBK = angle LNC,
    angle LCK = angle BMK.
  O = circumcentre of AKL.  Claim: OM = ON.

Strategy (polynomial ideal membership):
  - Place A=(0,0), B=(1,0), C=(p,q), q>0. Then M=(1/2,0), N=(p/2,q/2).
  - Let alpha = angle KBA = angle ACL, and write
        angle LBA = alpha + beta,   angle ACK = alpha + gamma
    (so angle LBK = beta, angle LCK = gamma).
  - Parametrize by half-angle tangent variables
        a = tan(alpha/2),   u = tan((alpha+beta)/2),   v = tan((alpha+gamma)/2).
  - Directions of the four rays BK, BL (clockwise rotations of BA) and CL, CK
    (counter-clockwise rotations of CA) become RATIONAL in (a,u,v,p,q) via the
    rational rotation form. Hence K = BK cap CK and L = BL cap CL are rational
    functions of (p,q,a,u,v).
  - The two angle conditions  angle LNC = beta  and  angle BMK = gamma, written as
        [NL,NC]/(NL,NC) = tan(beta),   [MB,MK]/(MB,MK) = tan(gamma),
    clear to polynomials condA, condB that factor as
        condA = 2 (p^2+q^2)(1+a u) * fA(a,u,p,q),
        condB = -2 (1+a v)         * fB(a,v,p,q),
    with the prefactors strictly positive, so the conditions are fA = fB = 0.
  - OM = ON is equivalent (after clearing denominators) to a polynomial T=0.
  - Gröbner-basis ideal membership:  T in <fA, fB>  over Q[p,q,a,u,v].
    Verified: the remainder of T on division by the Gröbner basis of <fA,fB>
    (lex order v>u>a>p>q) is EXACTLY 0.

Run:  python3 om_on_proof_verify.py
(Requires sympy. The Gröbner step takes ~1-2 seconds.)
"""

import math
import pickle
import time

import sympy as sp
from sympy import symbols, expand, factor, simplify, Poly, groebner, together, numer, denom

# ----------------------------------------------------------------------
# 1. Build K, L as rational functions of (p,q,a,u,v).
# ----------------------------------------------------------------------
p, q = symbols('p q')
a, u, v = symbols('a u v')          # a=tan(alpha/2), u=tan((alpha+beta)/2), v=tan((alpha+gamma)/2)


def rotCW(vec, t):
    """Clockwise rotation by angle 2*arctan(t), scaled by (1+t^2) (a positive scalar)."""
    x, y = vec
    return (expand((1 - t**2) * x + 2 * t * y),
            expand(-2 * t * x + (1 - t**2) * y))


def rotCCW(vec, t):
    """Counter-clockwise rotation by angle 2*arctan(t), scaled by (1+t^2)."""
    x, y = vec
    return (expand((1 - t**2) * x - 2 * t * y),
            expand(2 * t * x + (1 - t**2) * y))


BA = (-sp.Integer(1), sp.Integer(0))     # direction from B toward A
CA = (-p, -q)                            # direction from C toward A
dir_BK = rotCW(BA, a)                     # ray BK
dir_BL = rotCW(BA, u)                     # ray BL
dir_CL = rotCCW(CA, a)                    # ray CL
dir_CK = rotCCW(CA, v)                    # ray CK


def cross(w1, w2):
    return expand(w1[0] * w2[1] - w1[1] * w2[0])


def dot(w1, w2):
    return expand(w1[0] * w2[0] + w1[1] * w2[1])


W = (p - 1, q)                            # C - B


def intersect(d1, d2, W):
    """Point = B + (cross(W,d2)/cross(d1,d2)) * d1, returned as (num_x, num_y, den)."""
    tn = cross(W, d2)
    td = cross(d1, d2)
    return expand(td + tn * d1[0]), expand(tn * d1[1]), td


Kx, Ky, Kden = intersect(dir_BK, dir_CK, W)   # K = (Kx/Kden, Ky/Kden)
Lx, Ly, Lden = intersect(dir_BL, dir_CL, W)   # L = (Lx/Lden, Ly/Lden)


# ----------------------------------------------------------------------
# 2. The two angle conditions as polynomials condA, condB.
# ----------------------------------------------------------------------
def tan_of_diff(T, S):
    """tan( 2 (arctan T - arctan S) ), as a rational function."""
    h = (T - S) / (1 + S * T)
    return expand(2 * h / (1 - h**2))


tan_beta = together(tan_of_diff(u, a))
tan_gamma = together(tan_of_diff(v, a))
nb = expand(numer(tan_beta))    # tan(beta) = nb / db
db = expand(denom(tan_beta))
ng = expand(numer(tan_gamma))   # tan(gamma) = ng / dg
dg = expand(denom(tan_gamma))

# angle LNC = beta :  [NL,NC]/(NL,NC) = tan(beta).
# Clear denominators by using NL' = (2 Lx - p Lden, 2 Ly - q Lden) and NC' = (p, q)
# (scaling NL by 1/(2 Lden) and NC by 1/2 leaves the ratio cross/dot unchanged).
NLp = (expand(2 * Lx - p * Lden), expand(2 * Ly - q * Lden))
NCp = (p, q)
condA = expand(cross(NLp, NCp) * db - dot(NLp, NCp) * nb)

# angle BMK = gamma :  [MB,MK]/(MB,MK) = tan(gamma).
# M=(1/2,0): MB=(1/2,0), MK=(Kx/Kden - 1/2, Ky/Kden).
# cross(MB,MK)/dot(MB,MK) = (Ky/Kden) / (Kx/Kden - 1/2) = 2 Ky / (2 Kx - Kden).
MKx = expand(2 * Kx - Kden)
MKy = expand(2 * Ky)
condB = expand(MKy * dg - MKx * ng)

# Strip the strictly-positive prefactors to get the core polynomials.
fA = expand(simplify(condA / (2 * (p**2 + q**2) * (a * u + 1))))
fB = expand(simplify(condB / (-2 * (a * v + 1))))


# ----------------------------------------------------------------------
# 3. The target polynomial T :  OM = ON  <=>  T = 0.
# ----------------------------------------------------------------------
# Circumcentre O of triangle A=(0,0), K, L satisfies
#     O.K = |K|^2 / 2,    O.L = |L|^2 / 2.
# Multiply through by 2*Kden (resp. 2*Lden):
a1 = expand(2 * Kden * Kx); b1 = expand(2 * Kden * Ky); c1 = expand(Kx**2 + Ky**2)
a2 = expand(2 * Lden * Lx); b2 = expand(2 * Lden * Ly); c2 = expand(Lx**2 + Ly**2)
DET = expand(a1 * b2 - b1 * a2)                 # determinant of the 2x2 system
oxn = expand(c1 * b2 - b1 * c2)                 # ox = oxn / DET
oyn = expand(a1 * c2 - c1 * a2)                 # oy = oyn / DET

# OM = ON  <=>  |O-M|^2 = |O-N|^2  <=>  2 O.(N-M) = |N|^2 - |M|^2.
# N-M = ((p-1)/2, q/2),  |N|^2 - |M|^2 = (p^2+q^2-1)/4.
# Clearing the common denominator DET and multiplying by 4:
TGT = expand(4 * (oxn * (p - 1) + oyn * q) - (p**2 + q**2 - 1) * DET)


# ----------------------------------------------------------------------
# 4. RIGOROUS CHECK :  TGT in <fA, fB>  via Groebner basis.
# ----------------------------------------------------------------------
print("Computing Groebner basis of <fA, fB> over Q[p,q,a,u,v], lex order v>u>a>p>q ...")
t0 = time.time()
GB = groebner([fA, fB], v, u, a, p, q, order='lex')
print(f"  basis computed in {time.time()-t0:.1f}s, length {len(GB.polys)}")

t0 = time.time()
_quotients, remainder = GB.reduce(TGT)
print(f"  reduction done in {time.time()-t0:.1f}s")
print(f"  remainder of TGT mod <fA,fB> = {remainder}")
assert remainder == 0, "IDEAL MEMBERSHIP FAILED"
print("\nTGT in <fA, fB>  ==>  whenever the angle conditions hold (fA=fB=0),")
print("                       TGT = 0, i.e.  OM = ON.   [PROVED]")


# ----------------------------------------------------------------------
# 5. Independent numerical sanity check on random triangles.
# ----------------------------------------------------------------------
print("\n--- numerical sanity check (independent of the algebra above) ---")
import random
import numpy as np
from scipy.optimize import fsolve


def angf(w1, w2):
    c = np.dot(w1, w2) / (np.linalg.norm(w1) * np.linalg.norm(w2) + 1e-300)
    return np.arccos(max(-1.0, min(1.0, c)))


def signedf(w1, w2):
    return w1[0] * w2[1] - w1[1] * w2[0]


def betweenf(ba, bl, bk):
    return signedf(ba, bk) * signedf(ba, bl) >= 0 and signedf(bk, bl) * signedf(ba, bl) >= 0


def in_tri(P, X, Y, Z):
    s1 = signedf(Y - X, P - X); s2 = signedf(Z - Y, P - Y); s3 = signedf(X - Z, P - Z)
    return (s1 > 0 and s2 > 0 and s3 > 0) or (s1 < 0 and s2 < 0 and s3 < 0)


def circumcenter(A, K, L):
    ax, ay = A; kx, ky = K; lx, ly = L
    D = 2 * (ax * (ky - ly) + kx * (ly - ay) + lx * (ay - ky))
    ux = ((ax**2 + ay**2) * (ky - ly) + (kx**2 + ky**2) * (ly - ay) + (lx**2 + ly**2) * (ay - ky)) / D
    uy = ((ax**2 + ay**2) * (lx - kx) + (kx**2 + ky**2) * (ax - lx) + (lx**2 + ly**2) * (kx - ax)) / D
    return np.array([ux, uy])


random.seed(0)
ok = tot = 0
for _ in range(40):
    pv = random.uniform(0.2, 2.5); qv = random.uniform(0.3, 2.5)
    A = np.array([0., 0.]); B = np.array([1., 0.]); C = np.array([pv, qv])
    M = (A + B) / 2; N = (A + C) / 2

    def eqs(vars, lam):
        kx, ky, lx, ly = vars
        K = np.array([kx, ky]); L = np.array([lx, ly])
        return [angf(K - B, A - B) - angf(A - C, L - C),
                angf(L - B, K - B) - angf(L - N, C - N),
                angf(L - C, K - C) - angf(B - M, K - M),
                kx - lam]

    found = False
    for lam in np.linspace(0.3, 0.8, 12):
        for g0 in ([lam, 0.1, 0.2, 0.4], [lam, 0.2, 0.5, 0.3]):
            try:
                x, info, ier, _ = fsolve(eqs, g0, args=(lam,), full_output=True)
                if ier == 1 and np.max(np.abs(info['fvec'])) < 1e-9:
                    K = x[:2]; L = x[2:]
                    if (in_tri(K, B, M, C) and in_tri(L, B, N, C)
                            and betweenf(A - B, L - B, K - B) and betweenf(A - C, K - C, L - C)):
                        O = circumcenter(A, K, L)
                        tot += 1
                        if abs(np.linalg.norm(O - M) - np.linalg.norm(O - N)) < 1e-7:
                            ok += 1
                        found = True
                        break
            except Exception:
                pass
        if found:
            break

print(f"valid configurations tested: {tot};  |OM-ON| < 1e-7 in all: {ok == tot} ({ok}/{tot})")
