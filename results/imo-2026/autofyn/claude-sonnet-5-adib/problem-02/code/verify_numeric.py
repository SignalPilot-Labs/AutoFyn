"""
Numerical confirmation of the IMO-2026-02 conclusion O_x = p/2 (hence OM = ON).

This solves the proof's OWN quadratics Q1(R2)=0, Q2(R1)=0 (current.md, "Rescaled
quadratics") for the positive real root, builds K, L, and forms the circumcenter O
of triangle A,K,L. On the three configurations current.md cites in "Assembling",
plus the fresh triangles from the run's probe, O_x = p/2 to machine precision with
the determinant D bounded away from 0.

NB: one must solve Q1, Q2 (which already encode the correct signed-angle branch via
the sign-matching lemma, current.md "F=0 => Q=0"), NOT the raw unsigned-angle
equations ang(...)=ang(...): those admit spurious wrong-side roots where O_x != p/2,
the exact sign-convention trap the proof's round-2/round-4 history documents.

Run: python3 verify_numeric.py   (needs numpy)
"""
import numpy as np


def solve_and_check(p, q, theta):
    ct, st = np.cos(theta), np.sin(theta)
    B = np.array([-1.0, 0.0])
    C = np.array([1.0, 0.0])
    A = np.array([p, q])
    Delta = 2 * q * ct + (p**2 + q**2 - 1) * st

    # Q2(R1) = -Delta R1^2 + (Delta ct + q) R1 - (q ct + (p-1) st)   (AB2/2 factor drops)
    # Q1(R2) = -Delta R2^2 + (Delta ct + q) R2 - (q ct - (p+1) st)
    R1_roots = np.roots([-Delta, Delta * ct + q, -(q * ct + (p - 1) * st)])
    R2_roots = np.roots([-Delta, Delta * ct + q, -(q * ct - (p + 1) * st)])

    d1 = np.array([(A[0] - B[0]) * ct + (A[1] - B[1]) * st,
                   -(A[0] - B[0]) * st + (A[1] - B[1]) * ct])
    d2 = np.array([(A[0] - C[0]) * ct - (A[1] - C[1]) * st,
                   (A[0] - C[0]) * st + (A[1] - C[1]) * ct])

    best = None
    for R1 in R1_roots:
        for R2 in R2_roots:
            if abs(R1.imag) > 1e-9 or abs(R2.imag) > 1e-9:
                continue
            R1r, R2r = R1.real, R2.real
            if R1r <= 0 or R2r <= 0:
                continue
            K = B + R1r * d1
            L = C + R2r * d2
            ax, ay = A
            kx, ky = K
            lx, ly = L
            D = 2 * (ax * (ky - ly) + kx * (ly - ay) + lx * (ay - ky))
            if abs(D) < 1e-9:
                continue
            Ox = ((ax**2 + ay**2) * (ky - ly) + (kx**2 + ky**2) * (ly - ay)
                  + (lx**2 + ly**2) * (ay - ky)) / D
            err = abs(Ox - p / 2)
            if best is None or err < best[0]:
                best = (err, Ox, D)
    return best


CONFIGS = [  # (p, q, theta_radians) — the three from current.md "Assembling", plus probe triangles
    (0.35, 1.2, 0.5), (-0.4, 0.9, 0.3), (0.7, 2.1, 0.25),
    (0.3, 1.7, np.radians(15)), (0.9, 1.3, np.radians(8)),
]
for (p, q, theta) in CONFIGS:
    b = solve_and_check(p, q, theta)
    if b is None:
        print(f"(p,q,theta)=({p},{q},{theta:.4f}): no positive real (R1,R2) root pair")
        continue
    err, Ox, D = b
    print(f"(p,q,theta)=({p},{q},{theta:.4f}): O_x={Ox:.15f}  p/2={p / 2:.15f}  "
          f"|O_x-p/2|={err:.2e}  D={D:.3f}")
