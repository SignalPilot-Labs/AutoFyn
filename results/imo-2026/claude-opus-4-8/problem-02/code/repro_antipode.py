"""
Verification artifact for approach `antipode-perp-bisector` (IMO 2026 P2).

Certifies, across several triangles x several admissible alpha:
  Step 1: OM = ON  <=>  A*B = A*C  (A* = 2O - A antipode of A on circle AKL),
          and the power bridge pow(B)-pow(C) = (AB^2-AC^2)/2.
  Step 2: A*K _|_ AK  and  A*L _|_ AL  (Thales).
  Step 3 (GAP, numerically checked): angle A*BK = 90-C, angle A*CL = 90-B (alpha-independent).
  Step 4: angle A*BA = 90-C+alpha, angle A*CA = 90-B+alpha, A* inside angle BAC,
          angle A*BC = angle A*CB (isosceles) -> A*B = A*C.

Run: python3 repro_antipode.py
"""
import numpy as np
from verify_config import find_KL_for_alpha, circumcenter, angle_at


def ang(v, p, q):
    return np.degrees(angle_at(v, p, q))


TRIS = [
    ('T1', [0.5, 1.5], [0, 0], [2, 0]),
    ('T4', [0.7, 1.1], [0.2, 0.1], [1.8, 0.3]),
    ('T5', [1.0, 1.6], [0, 0], [2.4, 0.0]),
    ('T6', [0.4, 1.8], [0, 0], [1.0, 0.0]),
]


def run():
    worst = {}
    n = 0
    for name, A, B, C in TRIS:
        A = np.array(A, float); B = np.array(B, float); C = np.array(C, float)
        M = (A + B) / 2; N = (A + C) / 2
        aA = ang(A, B, C); aB = ang(B, A, C); aC = ang(C, A, B)
        for ad in [8, 15, 22, 30, 37]:
            r = find_KL_for_alpha(A, B, C, np.radians(ad))
            if r is None:
                continue
            n += 1
            K, L = r
            O = circumcenter(A, K, L); As = 2 * O - A
            R = np.linalg.norm(O - A)
            powB = np.dot(B - O, B - O) - R**2
            powC = np.dot(C - O, C - O) - R**2
            ab2 = np.dot(A - B, A - B); ac2 = np.dot(A - C, A - C)
            checks = {
                'S1  OM-ON':            np.linalg.norm(O - M) - np.linalg.norm(O - N),
                'S1  A*B-A*C':          np.linalg.norm(As - B) - np.linalg.norm(As - C),
                'S1  power bridge':     (powB - powC) - (ab2 - ac2) / 2,
                'S2  A*K.AK':           np.dot(K - A, As - K),
                'S2  A*L.AL':           np.dot(L - A, As - L),
                'S3  A*BK-(90-C)':      ang(B, As, K) - (90 - aC),
                'S3  A*CL-(90-B)':      ang(C, As, L) - (90 - aB),
                'S4  A*BA-(90-C+a)':    ang(B, As, A) - (90 - aC + ad),
                'S4  A*CA-(90-B+a)':    ang(C, As, A) - (90 - aB + ad),
                'S4  inside angleA':    (ang(A, B, As) + ang(A, C, As)) - aA,
                'S4  A*BC-A*CB':        ang(B, As, C) - ang(C, As, B),
                'C1  KBA-ACL':          ang(B, K, A) - ang(C, A, L),
            }
            for k, v in checks.items():
                worst[k] = max(worst.get(k, 0.0), abs(v))
    print(f"configs checked: {n}")
    for k in sorted(worst):
        # config solver (fsolve) resolves K,L only to ~1e-8; distance/angle residuals
        # inherit that scale. S2 dot products (evaluated at exact O) are machine-exact.
        tol = 1e-14 if k.startswith('S2') else 1e-6
        flag = 'OK ' if worst[k] < tol else 'BIG'
        print(f"  [{flag}] max |{k}| = {worst[k]:.2e}")


if __name__ == '__main__':
    run()
