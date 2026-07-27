"""
Certificate 2: confirms Lemma 2 of the proof:

    angle(MKC) = angle(NLB) = pi - alpha - x

where alpha = angle BAC and x = angle KBA = angle ACL, for the exact
(K, L) solving the problem's three angle conditions. Checked on two
independent random triangles across the admissible range of x.
"""

import numpy as np
from common import angle_at, solve_KL, triangle_angles


def check_triangle(A, B, C, label):
    M = (A + B) / 2
    N = (A + C) / 2
    alpha, beta, gamma = triangle_angles(A, B, C)
    print(f"--- {label}: alpha={alpha:.4f} beta={beta:.4f} gamma={gamma:.4f} ---")
    guess = (1.0, 1.0)
    for x in np.linspace(0.05, min(beta, gamma) - 0.05, 6):
        t, s, K, L, ier = solve_KL(A, B, C, x, guess)
        if ier != 1 or t <= 0 or s <= 0:
            continue
        guess = (t, s)
        angMKC = angle_at(K, M, C)
        angNLB = angle_at(L, N, B)
        target = np.pi - alpha - x
        print(f"x={x:.4f}  angle(MKC)={angMKC:.7f}  angle(NLB)={angNLB:.7f}  "
              f"pi-alpha-x={target:.7f}")
    print()


check_triangle(np.array([0.0, 0.0]), np.array([5.0, 0.3]), np.array([1.2, 4.0]),
                "Triangle 1")
check_triangle(np.array([0.3, 5.1]), np.array([-2.0, -1.0]), np.array([4.5, -0.7]),
                "Triangle 2 (independent)")
