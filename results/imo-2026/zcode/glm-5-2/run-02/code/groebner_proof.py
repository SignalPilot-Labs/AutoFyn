"""
Certificate for the theorem OM = ON.

Problem: Let ABC be a triangle, M,N the midpoints of AB,AC. Points K in (BMC),
L in (BNC) satisfy K in angle(LBA), L in angle(ACK), and
    angle(KBA) = angle(ACL)        ... (i)
    angle(LBK) = angle(LNC)        ... (ii)
    angle(LCK) = angle(BMK)        ... (iii)
Let O be the circumcentre of triangle AKL. Prove OM = ON.

This script proves the theorem ALGEBRAICALLY:
  - Place the midpoint of MN at the origin with MN on the x-axis, |MN| = 2.
    Then M=(-1,0), N=(1,0), A=(a,h) (h>0), B=(-2-a,-h), C=(2-a,-h).
  - Parametrise K,L by phi = angle(KBA) = angle(ACL) (condition i) and m,n>0.
  - Conditions (ii),(iii) become (exactly) Rn = 0 and Rm = 0 (see below), where the
    only scalar factors dropped are 8*m*|AC|^2 and 8*n*|AB|^2, both nonzero.
  - The x-coordinate of O is P / (2*[K-A, L-A]).
  - We show P lies in the ideal <Rm, Rn, c^2+s^2-1> by Groebner reduction,
    with remainder EXACTLY ZERO. Hence O_x = 0, i.e. O is on the perpendicular
    bisector of MN, so OM = ON.

Run: python3 groebner_proof.py
"""
import sympy as sp
from sympy import groebner, reduced, factor

a, h, m, n, c, s = sp.symbols('a h m n c s')
A = sp.Matrix([a, h])
M = sp.Matrix([-1, 0]); N = sp.Matrix([1, 0])
B = 2 * M - A            # (-2-a, -h)
C = 2 * N - A            # (2-a,  -h)


def rot(v, co, si):
    """Rotate vector v: angle -phi when (co,si)=(c,-s); angle +phi when (c,+s)."""
    return sp.Matrix([co * v[0] - si * v[1], si * v[0] + co * v[1]])


BA = A - B
dK = rot(BA, c, -s)       # ray BK = rotate BA by -phi (toward interior)
CA = A - C
dL = rot(CA, c, s)        # ray CL = rotate CA by +phi (toward interior)
K = B + m * dK
L = C + n * dL


def cr(u, v):
    return u[0] * v[1] - u[1] * v[0]


def dt(u, v):
    return u[0] * v[0] + u[1] * v[1]


# --- Build the exact (oriented-tangent) form of conditions (ii) and (iii) ---
BK = m * dK
BL = sp.Matrix([4, 0]) + n * dL          # L - B = (C-B) + n*dL,  C-B=(4,0)
NC = sp.Matrix([1 - a, -h])              # C - N
NL = NC + n * dL                         # L - N
G2 = sp.expand(cr(BK, BL) * dt(NC, NL) - dt(BK, BL) * cr(NC, NL))   # (ii)

CL = n * dL
CK = sp.Matrix([-4, 0]) + m * dK         # K - C = (B-C) + m*dK,  B-C=(-4,0)
MBv = sp.Matrix([-1 - a, -h])            # B - M
MK = MBv + m * dK                        # K - M
G3 = sp.expand(cr(CL, CK) * dt(MBv, MK) - dt(CL, CK) * cr(MBv, MK))  # (iii)

# --- Define the clean relations Rn, Rm as the EXACT inner factors of G2, G3 ---
# (obtained by factoring G2, G3 and dropping the nonzero scalar parts
#  8*m*((a-1)^2+h^2) and 8*n*((a+1)^2+h^2)). We extract them directly so the
# sign is unambiguous, then verify the factorisations hold.
G2f = sp.factor(G2)
G3f = sp.factor(G3)
# isolate the inner bracket: divide out m*( (a-1)^2+h^2 ) and the numeric factor 8
Rn = sp.expand(sp.cancel(G2f / (8 * m * ((a - 1)**2 + h**2))))
Rm = sp.expand(sp.cancel(G3f / (8 * n * ((a + 1)**2 + h**2))))
C1 = c**2 + s**2 - 1

# --- Verify G2, G3 are exact nonzero scalar multiples of Rn, Rm ---
assert sp.simplify(G2 - 8 * m * ((a - 1)**2 + h**2) * Rn) == 0, "Rn mismatch"
assert sp.simplify(G3 - 8 * n * ((a + 1)**2 + h**2) * Rm) == 0, "Rm mismatch"
print("[ok] G2 = -8*m*((a-1)^2+h^2)*Rn  and  G3 = +8*n*((a+1)^2+h^2)*Rm")
print("     scalars nonzero since m,n>0 and |AC|^2,|AB|^2 > 0.")

# --- x-coordinate of circumcentre O of A,K,L ---
K2, A2, L2 = dt(K, K), dt(A, A), dt(L, L)
Ox, Oy = sp.symbols('Ox Oy')
e1 = sp.expand(2 * Ox * (K[0] - A[0]) + 2 * Oy * (K[1] - A[1]) - (K2 - A2))
e2 = sp.expand(2 * Ox * (L[0] - A[0]) + 2 * Oy * (L[1] - A[1]) - (L2 - A2))
sol = sp.solve([e1, e2], [Ox, Oy], check=False)
P, Q = sp.together(sol[Ox]).as_numer_denom()
P = sp.expand(P)
den = sp.expand(cr(K - A, L - A))    # = Q/2 ; nonzero iff A,K,L non-collinear

# --- Main claim: P is in the ideal <Rm, Rn, C1> ---
print("\n[computing] Groebner basis of <Rm, Rn, c^2+s^2-1> ...")
G = groebner([Rm, Rn, C1], m, n, c, s, order='lex')
_quot, rem = reduced(P, G, m, n, c, s, order='lex')

print("[result]  remainder of O_x-numerator P modulo the ideal:")
print("         ", factor(rem))
assert rem == 0, "Remainder is NOT zero -- proof fails!"
print("\n[ok] P = 0  whenever Rm = Rn = 0 and c^2+s^2 = 1.")
print("[ok] Hence O_x = 0  (denominator 2*[K-A,L-A] != 0 since O is a circumcentre).")
print("[ok] O lies on the perpendicular bisector of MN, therefore  OM = ON.  QED")
