"""
Certificate 5: full end-to-end numerical check, chaining every claim
in the proof on one independent, freshly chosen triangle:

  1. Lemma 2:  angle(MKC) = angle(NLB) = pi - alpha - x
  2. Lemma 3:  Q_K(BK) = 0  and  Q_L(CL) = 0
  3. Main claim: OM = ON

all evaluated at the actual (K, L) solving the problem's three angle
conditions, for several values of the free parameter x.
"""

import numpy as np
from common import angle_at, solve_KL, triangle_angles, circumcenter, circumradius

A = np.array([2.1, 3.7])
B = np.array([-3.4, 0.5])
C = np.array([2.8, -2.2])
M = (A + B) / 2
N = (A + C) / 2

alpha, beta, gamma = triangle_angles(A, B, C)
R = circumradius(A, B, C)
print(f"alpha={alpha:.4f} beta={beta:.4f} gamma={gamma:.4f} R={R:.4f}")
print()

guess = (1.0, 1.0)
for x in np.linspace(0.05, min(beta, gamma) - 0.05, 6):
    t, s, K, L, ier = solve_KL(A, B, C, x, guess)
    if ier != 1 or t <= 0 or s <= 0:
        print(f"x={x:.4f}  solve failed")
        continue
    guess = (t, s)

    angMKC = angle_at(K, M, C)
    angNLB = angle_at(L, N, B)
    target = np.pi - alpha - x

    common_factor = np.sin(alpha) + 2 * np.sin(alpha + x) * np.cos(x)
    Qk = (np.sin(alpha + x) * t**2 - R * np.sin(gamma) * common_factor * t
          + 2 * R**2 * np.sin(gamma) * np.sin(alpha) * np.sin(gamma - x))
    Ql = (np.sin(alpha + x) * s**2 - R * np.sin(beta) * common_factor * s
          + 2 * R**2 * np.sin(beta) * np.sin(alpha) * np.sin(beta - x))

    O = circumcenter(A, K, L)
    OM = np.linalg.norm(O - M)
    ON = np.linalg.norm(O - N)

    print(f"x={x:.4f}")
    print(f"  Lemma 2:  MKC={angMKC:.7f}  NLB={angNLB:.7f}  target={target:.7f}")
    print(f"  Lemma 3:  Q_K(BK)={Qk: .3e}   Q_L(CL)={Ql: .3e}")
    print(f"  Main:     OM={OM:.8f}  ON={ON:.8f}  OM-ON={OM-ON: .2e}")
