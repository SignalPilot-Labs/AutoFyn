"""
IMO 2026 P2 configuration verifier.
Given triangle ABC with midpoints M,N of AB,AC, finds K inside BMC and L inside BNC
satisfying the three angle conditions, then verifies OM = ON (O = circumcenter of AKL).

Usage:
  python3 verify_config.py            # run built-in test triangles
  python3 verify_config.py --plot     # also save a plot (requires matplotlib)

Three angle conditions:
  (1) angle_KBA = angle_ACL = alpha   (free parameter)
  (2) angle_LBK = angle_LNC = beta    (constrained)
  (3) angle_LCK = angle_BMK = gamma   (constrained)
"""

import numpy as np
from scipy.optimize import fsolve
import warnings
warnings.filterwarnings('ignore')

def angle_at(vertex, p1, p2):
    """Unsigned angle at vertex between rays to p1 and p2, in [0, pi]."""
    u = np.array(p1, dtype=float) - np.array(vertex, dtype=float)
    v = np.array(p2, dtype=float) - np.array(vertex, dtype=float)
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    if nu < 1e-12 or nv < 1e-12:
        return 0.0
    cos_val = np.dot(u, v) / (nu * nv)
    return np.arccos(np.clip(cos_val, -1.0, 1.0))

def circumcenter(P, Q, R):
    """Circumcenter of triangle PQR."""
    ax, ay = P; bx, by = Q; cx, cy = R
    D = 2*(ax*(by - cy) + bx*(cy - ay) + cx*(ay - by))
    if abs(D) < 1e-12:
        return None
    ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
    uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
    return np.array([ux, uy])

def in_triangle(P, A, B, C):
    """True if P is strictly inside triangle ABC."""
    def sign(p1, p2, p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    d1, d2, d3 = sign(P, A, B), sign(P, B, C), sign(P, C, A)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

def check_qualitative(A, B, C, K, L):
    """
    Check the qualitative conditions:
      - K inside angle LBA (angle at B between BL and BA contains K)
      - L inside angle ACK (angle at C between CA and CK contains L)
    Returns (k_in_angle_LBA, l_in_angle_ACK).
    """
    # K inside angle LBA: the angular region at B swept from BL to BA (smaller arc)
    # Equivalently: angle KBA < angle LBA
    ang_KBA = angle_at(B, K, A)
    ang_LBA = angle_at(B, L, A)
    k_in = ang_KBA < ang_LBA - 1e-6

    # L inside angle ACK: angle ACL < angle ACK
    ang_ACL = angle_at(C, A, L)
    ang_ACK = angle_at(C, A, K)
    l_in = ang_ACL < ang_ACK - 1e-6

    return k_in, l_in

def angle_residuals(A, B, C, K, L):
    """
    Compute residuals for the three angle conditions.
    Returns (r1, r2, r3) which should all be 0 for a valid configuration.
    r1 = angle_KBA - angle_ACL
    r2 = angle_LBK - angle_LNC
    r3 = angle_LCK - angle_BMK
    """
    M = (A + B) / 2
    N = (A + C) / 2
    r1 = angle_at(B, K, A) - angle_at(C, A, L)
    r2 = angle_at(B, L, K) - angle_at(N, L, C)
    r3 = angle_at(C, L, K) - angle_at(M, B, K)
    return r1, r2, r3

def find_KL_for_alpha(A, B, C, alpha, n_starts=6):
    """
    Given triangle ABC and alpha = angle_KBA = angle_ACL,
    solve for (t_K, t_L) such that K = B + t_K*Kdir and L = C + t_L*Ldir
    satisfy conditions (2) and (3).
    Returns (K, L) or None if not found.
    """
    M = (A + B) / 2
    N = (A + C) / 2
    BA_angle = np.arctan2((A-B)[1], (A-B)[0])
    CA_angle = np.arctan2((A-C)[1], (A-C)[0])
    Kdir = np.array([np.cos(BA_angle - alpha), np.sin(BA_angle - alpha)])
    Ldir = np.array([np.cos(CA_angle + alpha), np.sin(CA_angle + alpha)])

    def eqs(params):
        tK, tL = params
        K = B + tK * Kdir
        L = C + tL * Ldir
        r2 = angle_at(B, L, K) - angle_at(N, L, C)
        r3 = angle_at(C, L, K) - angle_at(M, B, K)
        return [r2, r3]

    for t0 in [(0.5, 0.5), (0.2, 0.8), (0.8, 0.3), (0.3, 0.6), (0.4, 0.4), (0.6, 0.6)]:
        try:
            sol = fsolve(eqs, t0, full_output=True)
            x, _, ier, _ = sol
            tK, tL = x
            if tK <= 1e-4 or tL <= 1e-4:
                continue
            K = B + tK * Kdir
            L = C + tL * Ldir
            resid = max(abs(r) for r in eqs(x))
            if resid < 1e-8 and K[1] > 1e-4 and L[1] > 1e-4:
                if in_triangle(K, B, M, C) and in_triangle(L, B, N, C):
                    return K, L
        except Exception:
            pass
    return None

def verify_triangle(A, B, C, n_alpha=10, verbose=True):
    """
    For the triangle with given vertices, verify OM = ON across a range of alpha values.
    Returns list of (alpha_deg, K, L, O, OM, ON, max_resid).
    """
    M = (A + B) / 2
    N = (A + C) / 2
    BA_angle = np.arctan2((A-B)[1], (A-B)[0])

    results = []
    prev = None
    alpha_max = BA_angle  # alpha < angle_ABC for K to be inside triangle

    for alpha_deg in np.linspace(3, np.degrees(alpha_max) * 0.85, n_alpha):
        alpha = np.radians(alpha_deg)

        res = find_KL_for_alpha(A, B, C, alpha)
        if res is None:
            continue
        K, L = res

        r1, r2, r3 = angle_residuals(A, B, C, K, L)
        max_resid = max(abs(r1), abs(r2), abs(r3))
        if max_resid > 1e-6:
            continue

        k_in, l_in = check_qualitative(A, B, C, K, L)

        O = circumcenter(A, K, L)
        if O is None:
            continue

        OM = np.linalg.norm(O - M)
        ON = np.linalg.norm(O - N)

        results.append((alpha_deg, K, L, O, OM, ON, max_resid))

        if verbose:
            diff = abs(OM - ON)
            print(f"  alpha={alpha_deg:5.1f}°: K=({K[0]:.4f},{K[1]:.4f})  "
                  f"L=({L[0]:.4f},{L[1]:.4f})  "
                  f"O=({O[0]:.4f},{O[1]:.4f})  "
                  f"OM={OM:.6f}  ON={ON:.6f}  |OM-ON|={diff:.2e}  "
                  f"K_in_angle={k_in}  L_in_angle={l_in}")

    return results

def run_tests():
    triangles = [
        ("Scalene 1", np.array([0.5, 1.5]), np.array([0.0, 0.0]), np.array([2.0, 0.0])),
        ("Scalene 2", np.array([1.0, 2.0]), np.array([0.0, 0.0]), np.array([3.0, 0.0])),
        ("Scalene 3", np.array([0.3, 1.2]), np.array([0.0, 0.0]), np.array([1.5, 0.0])),
        ("Scalene 4 (general)", np.array([0.7, 1.1]), np.array([0.2, 0.1]), np.array([1.8, 0.3])),
    ]

    all_ok = True
    for name, A, B, C in triangles:
        M = (A + B) / 2
        N = (A + C) / 2
        mid_MN = (M + N) / 2
        print(f"\n=== {name} ===")
        print(f"A={A}, B={B}, C={C}")
        print(f"M={M}, N={N}, midpoint(MN)={mid_MN}")

        results = verify_triangle(A, B, C, n_alpha=8)

        if not results:
            print("  WARNING: no solutions found!")
            all_ok = False
            continue

        # Key check: OM = ON for all solutions
        max_diff = max(abs(OM - ON) for _, _, _, _, OM, ON, _ in results)
        # Key structural fact: O_x = midpoint_x(MN) for all solutions
        Ox_vals = [O[0] for _, _, _, O, _, _, _ in results]
        Ox_dev = max(abs(Ox - mid_MN[0]) for Ox in Ox_vals)

        print(f"  Found {len(results)} solutions. Max |OM-ON| = {max_diff:.2e}")
        print(f"  O_x always = {mid_MN[0]:.6f}? Max deviation = {Ox_dev:.2e}")

        if max_diff > 1e-6:
            print("  FAIL: OM ≠ ON!")
            all_ok = False
        else:
            print("  PASS: OM = ON confirmed.")

    print("\n" + ("ALL TESTS PASSED" if all_ok else "SOME TESTS FAILED"))
    return all_ok

if __name__ == "__main__":
    import sys
    run_tests()
