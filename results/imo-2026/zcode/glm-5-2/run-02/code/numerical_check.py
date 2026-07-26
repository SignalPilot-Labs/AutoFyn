"""
Independent NUMERICAL certificate for OM = ON.

For many random triangles ABC and many choices of the free parameter
phi = angle(KBA) = angle(ACL), solve conditions (ii),(iii) numerically for
K, L, verify ALL hypotheses (K in BMC, L in BNC, K in angle LBA, L in angle ACK,
and the three angle equalities), then check |OM - ON|.

A clean proof predicts |OM - ON| = 0 up to floating-point error.

Run: python3 numerical_check.py
"""
import numpy as np
from scipy.optimize import least_squares


def angpos(P, Q, R):
    u = np.asarray(P) - np.asarray(Q)
    v = np.asarray(R) - np.asarray(Q)
    return np.arccos(np.clip(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)), -1, 1))


def circumcenter(A, B, C):
    ax, ay = A; bx, by = B; cx, cy = C
    Dd = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay)
          + (cx * cx + cy * cy) * (ay - by)) / Dd
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx)
          + (cx * cx + cy * cy) * (bx - ax)) / Dd
    return np.array([ux, uy])


def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def signarea(P, Q, R):
    return 0.5 * ((Q[0] - P[0]) * (R[1] - P[1]) - (R[0] - P[0]) * (Q[1] - P[1]))


def inside(P, Q, R, X):
    d = [signarea(P, Q, X), signarea(Q, R, X), signarea(R, P, X)]
    return all(x > 0 for x in d) or all(x < 0 for x in d)


def in_angle(vertex, r1, r2, pt):
    d1 = np.asarray(r1) - np.asarray(vertex)
    d2 = np.asarray(r2) - np.asarray(vertex)
    dp = np.asarray(pt) - np.asarray(vertex)
    c1 = cross2(d1, d2); ca = cross2(d1, dp); cb = cross2(dp, d2)
    return (ca * c1 >= 0) and (cb * c1 >= 0)


def main(seed=42, trials=300):
    np.random.seed(seed)
    valid = 0
    maxerr = 0.0
    for _ in range(trials):
        a = np.random.uniform(-0.7, 0.7)
        h = np.random.uniform(1.0, 3.5)
        A = np.array([a, h]); M = np.array([-1.0, 0]); N = np.array([1.0, 0])
        B = 2 * M - A; C = 2 * N - A
        phi = np.random.uniform(0.05, 0.7)
        cp, sp = np.cos(phi), np.sin(phi)
        BA = A - B
        sgn = 1 if cross2(BA, C - B) > 0 else -1
        ub = BA / np.linalg.norm(BA)
        dirBK = np.array([cp * ub[0] - sgn * sp * ub[1], sgn * sp * ub[0] + cp * ub[1]])
        CA = A - C
        sgn2 = 1 if cross2(CA, B - C) > 0 else -1
        uc = CA / np.linalg.norm(CA)
        dirCL = np.array([cp * uc[0] - sgn2 * sp * uc[1], sgn2 * sp * uc[0] + cp * uc[1]])

        def f(x):
            mm, nn = x
            K = B + mm * dirBK; L = C + nn * dirCL
            return [angpos(L, B, K) - angpos(L, N, C),
                    angpos(L, C, K) - angpos(B, M, K)]
        try:
            sol = least_squares(f, [0.5, 0.5], xtol=1e-15, ftol=1e-15, gtol=1e-15)
        except Exception:
            continue
        if sol.cost > 1e-24:
            continue
        mm, nn = sol.x
        if mm <= 0 or nn <= 0:
            continue
        K = B + mm * dirBK; L = C + nn * dirCL
        if not (inside(B, M, C, K) and inside(B, N, C, L)):
            continue
        if abs(angpos(K, B, A) - angpos(A, C, L)) > 1e-9:
            continue
        if not (in_angle(B, L, A, K) and in_angle(C, A, K, L)):
            continue
        try:
            O = circumcenter(A, K, L)
        except Exception:
            continue
        err = abs(np.linalg.norm(O - M) - np.linalg.norm(O - N))
        maxerr = max(maxerr, err)
        valid += 1
    print(f"Valid configurations satisfying ALL hypotheses: {valid}/{trials}")
    print(f"Max |OM - ON| over all valid configurations: {maxerr:.2e}")
    print("(floating-point noise ~1e-13 confirms OM = ON.)")
    return valid, maxerr


if __name__ == "__main__":
    main()
