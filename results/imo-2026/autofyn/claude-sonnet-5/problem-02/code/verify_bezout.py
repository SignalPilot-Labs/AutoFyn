"""
Symbolic verification of the load-bearing algebra in the IMO-2026-02 proof.

Reconstructed from the formulas stated verbatim in ../current.md:
  - the quadratics Q1(R2), Q2(R1)                     (current.md, "Rescaled quadratics")
  - the Bezout identity  Delta*T = P1*Q2 + P2*Q1      (current.md, "The Bezout identity")

It confirms the three claims the proof asserts from computation:
  (1) Q1, Q2 built from the raw Cross/Dot definitions equal the stated closed forms.
  (2) Delta*T - (P1*Q2 + P2*Q1) is divisible by (cos^2 t + sin^2 t - 1), i.e. the
      identity holds on the trig variety (remainder exactly 0); and it is FALSE as a
      free-symbol identity (matching current.md's honest "not unconditional" note).
  (3) both sides equal -543110611/1250000 at the Pythagorean point
      (cos t, sin t) = (3/5, 4/5), (p,q,R1,R2) = (3/10, 11/5, 13/4, 5/3).

Run: python3 verify_bezout.py   (needs sympy)
"""
import sympy as sp

p, q, ct, st, R1, R2 = sp.symbols("p q ct st R1 R2", real=True)


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


# Configuration (current.md "Setup"): B=(-1,0), C=(1,0), A=(p,q); K on ray from B, L on ray from C.
B = sp.Matrix([-1, 0])
C = sp.Matrix([1, 0])
A = sp.Matrix([p, q])
M = (A + B) / 2
N = (A + C) / 2
AB = A - B
AC = A - C
# d1 = (A-B) rotated by -theta, d2 = (A-C) rotated by +theta   (current.md, "Corrected rescaling")
d1 = sp.Matrix([AB[0] * ct + AB[1] * st, -AB[0] * st + AB[1] * ct])
d2 = sp.Matrix([AC[0] * ct - AC[1] * st, AC[0] * st + AC[1] * ct])
K = B + R1 * d1
L = C + R2 * d2

# (1) Raw quadratics from Lemma T1's Cross*Dot - Cross*Dot form, vs stated closed forms.
Q2_raw = sp.expand(cross(B - M, K - M) * dot(d2, K - C) - cross(d2, K - C) * dot(B - M, K - M))
Q1_raw = sp.expand(cross(d1, L - B) * dot(C - N, L - N) - cross(C - N, L - N) * dot(d1, L - B))

Delta = 2 * q * ct + (p**2 + q**2 - 1) * st
AB2 = (p + 1) ** 2 + q**2
AC2 = (p - 1) ** 2 + q**2
Q2_closed = (AB2 / 2) * (-Delta * R1**2 + (Delta * ct + q) * R1 - (q * ct + (p - 1) * st))
Q1_closed = (AC2 / 2) * (-Delta * R2**2 + (Delta * ct + q) * R2 - (q * ct - (p + 1) * st))

# raw and closed forms agree only on the trig variety cos^2+sin^2=1; check via remainder.
q2_ok = sp.rem(sp.expand(Q2_raw - Q2_closed), ct**2 + st**2 - 1, ct) == 0
q1_ok = sp.rem(sp.expand(Q1_raw - Q1_closed), ct**2 + st**2 - 1, ct) == 0
print("(1) Q2 raw == closed form (mod cos^2+sin^2-1):", q2_ok)
print("(1) Q1 raw == closed form (mod cos^2+sin^2-1):", q1_ok)

# (2) Bezout identity: Delta*T = P1*Q2 + P2*Q1, with T = 2[Nx - (p/2) D].
ax, ay = A
kx, ky = K
lx, ly = L
D = sp.expand(2 * (ax * (ky - ly) + kx * (ly - ay) + lx * (ay - ky)))
Nx = sp.expand(
    (ax**2 + ay**2) * (ky - ly) + (kx**2 + ky**2) * (ly - ay) + (lx**2 + ly**2) * (ay - ky)
)
T = sp.expand(2 * (Nx - (p * sp.Rational(1, 2)) * D))

P1 = 4 * q - 4 * R2 * (q * ct + (p - 1) * st)
P2 = -4 * q + 4 * R1 * (q * ct - (p + 1) * st)

diff = sp.expand(Delta * T - (P1 * Q2_closed + P2 * Q1_closed))
_, remainder = sp.div(sp.Poly(diff, ct), sp.Poly(ct**2 + st**2 - 1, ct))
print("(2) remainder of Delta*T-(P1*Q2+P2*Q1) by (cos^2+sin^2-1):", sp.simplify(remainder.as_expr()))
print("(2) identity is NON-trivial off the variety (diff not identically 0):", sp.expand(diff) != 0)

# (3) Numeric spot-check at the Pythagorean point stated in current.md.
pt = {p: sp.Rational(3, 10), q: sp.Rational(11, 5), ct: sp.Rational(3, 5), st: sp.Rational(4, 5),
      R1: sp.Rational(13, 4), R2: sp.Rational(5, 3)}
lhs = sp.nsimplify((Delta * T).subs(pt))
rhs = sp.nsimplify((P1 * Q2_closed + P2 * Q1_closed).subs(pt))
print("(3) LHS Delta*T           =", lhs)
print("(3) RHS P1*Q2+P2*Q1       =", rhs)
print("(3) both == -543110611/1250000:", lhs == rhs == sp.Rational(-543110611, 1250000))
