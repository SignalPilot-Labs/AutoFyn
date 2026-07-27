"""
Certificate 1: numerically confirms the main claim OM = ON across the
whole 1-parameter family of valid (K,L) configurations for a fixed
triangle, and shows that O (circumcenter of AKL) traces exactly the
perpendicular bisector of MN as the free parameter x varies.
"""

import numpy as np
from common import build_KL, solve_KL, circumcenter, triangle_angles

A = np.array([0.0, 0.0])
B = np.array([5.0, 0.3])
C = np.array([1.2, 4.0])
M = (A + B) / 2
N = (A + C) / 2

alpha, beta, gamma = triangle_angles(A, B, C)
print(f"Triangle angles: alpha={alpha:.4f} beta={beta:.4f} gamma={gamma:.4f}")

xs = np.linspace(0.05, min(beta, gamma) - 0.05, 8)
guess = (1.0, 1.0)
Os = []
print(f"{'x':>8} {'BK':>8} {'CL':>8} {'OM':>10} {'ON':>10} {'OM-ON':>12}")
for x in xs:
    t, s, K, L, ier = solve_KL(A, B, C, x, guess)
    if ier != 1 or t <= 0 or s <= 0:
        print(f"x={x:.4f}  solve failed")
        continue
    guess = (t, s)
    O = circumcenter(A, K, L)
    OM = np.linalg.norm(O - M)
    ON = np.linalg.norm(O - N)
    Os.append(O)
    print(f"{x:8.4f} {t:8.4f} {s:8.4f} {OM:10.6f} {ON:10.6f} {OM-ON:12.2e}")

# Check that all O's lie exactly on the perpendicular bisector of MN.
Os = np.array(Os)
MN = N - M
mid = (M + N) / 2
normal = MN / np.linalg.norm(MN)
resid = (Os - mid) @ normal
print()
print("Residuals of O from the perpendicular bisector of MN (should be ~0):")
print(resid)
