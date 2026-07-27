"""
Certificate 3: confirms Lemma 3 of the proof: that t = BK and s = CL
satisfy the explicit quadratics

  Q_K(t) = sin(a+x) t^2 - R sin(g) [sin(a) + 2 sin(a+x) cos(x)] t
           + 2 R^2 sin(g) sin(a) sin(g-x)                          = 0

  Q_L(s) = sin(a+x) s^2 - R sin(b) [sin(a) + 2 sin(a+x) cos(x)] s
           + 2 R^2 sin(b) sin(a) sin(b-x)                          = 0

where a,b,g = angle A, angle B, angle C and R = circumradius of ABC.
(R appears because these were originally derived after normalizing
the circumradius to 1; reinserting R restores dimensional / scale
consistency for an arbitrary triangle.)
"""

import numpy as np
from common import solve_KL, triangle_angles, circumradius


def check_triangle(A, B, C, label):
    alpha, beta, gamma = triangle_angles(A, B, C)
    R = circumradius(A, B, C)
    print(f"--- {label}: alpha={alpha:.4f} beta={beta:.4f} gamma={gamma:.4f} R={R:.4f} ---")
    guess = (1.0, 1.0)
    for x in np.linspace(0.05, min(beta, gamma) - 0.05, 6):
        t, s, K, L, ier = solve_KL(A, B, C, x, guess)
        if ier != 1 or t <= 0 or s <= 0:
            continue
        guess = (t, s)

        common_factor = np.sin(alpha) + 2 * np.sin(alpha + x) * np.cos(x)

        Qk = (np.sin(alpha + x) * t**2
              - R * np.sin(gamma) * common_factor * t
              + 2 * R**2 * np.sin(gamma) * np.sin(alpha) * np.sin(gamma - x))

        Ql = (np.sin(alpha + x) * s**2
              - R * np.sin(beta) * common_factor * s
              + 2 * R**2 * np.sin(beta) * np.sin(alpha) * np.sin(beta - x))

        print(f"x={x:.4f}  Q_K(BK)={Qk: .3e}   Q_L(CL)={Ql: .3e}")
    print()


check_triangle(np.array([0.0, 0.0]), np.array([5.0, 0.3]), np.array([1.2, 4.0]),
                "Triangle 1")
check_triangle(np.array([0.3, 5.1]), np.array([-2.0, -1.0]), np.array([4.5, -0.7]),
                "Triangle 2 (independent)")
