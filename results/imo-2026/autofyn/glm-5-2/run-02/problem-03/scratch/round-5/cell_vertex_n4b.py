"""
n=4 cell vertex enumeration - CORRECTED.
Level-4 dyadic (1,2,4,8,16)/31, 4 Xiang marks.
M = 9 sub-pieces total. Sum-constraints = 5. Degrees of freedom = 9-5 = 4.
=> arrangement vertices require 4 independent hyperplanes (4-tuples), not triples.
Hyperplanes: E (C(9,2)=36) + Z (9) = 45. 4-tuples per dist = C(45,4)=148995.
Distributions = C(8,4) = 70. Total 4-tuples = 70*148995 = 10429650.
Benchmarks: (a) Fraction exact, (b) numpy float (fast) + Fraction verify of candidates.
"""
import sys, time
from fractions import Fraction
from itertools import combinations
import numpy as np

LIU = [1, 2, 4, 8, 16]
N_MARKS = 4
N_PIECES_LIU = 5
D4 = 31

def distributions():
    for k1 in range(N_MARKS+1):
        for k2 in range(N_MARKS+1-k1):
            for k3 in range(N_MARKS+1-k1-k2):
                for k4 in range(N_MARKS+1-k1-k2-k3):
                    k5 = N_MARKS - k1 - k2 - k3 - k4
                    yield (k1,k2,k3,k4,k5)

def hyperplanes_for_distribution(ks):
    groups = []
    vid = 0
    for j, kj in enumerate(ks):
        for i in range(kj+1):
            groups.append((j, i, vid))
            vid += 1
    M = vid
    sum_rows = []
    for j in range(N_PIECES_LIU):
        row = [0]*M
        for (gj, i, v) in groups:
            if gj == j:
                row[v] = 1
        sum_rows.append((row, LIU[j]))
    E = []
    for a in range(M):
        for b in range(a+1, M):
            row = [0]*M
            row[a] = 1; row[b] = -1
            E.append((row, 0))
    Z = []
    for a in range(M):
        row = [0]*M
        row[a] = 1
        Z.append((row, 0))
    return M, sum_rows, E, Z

def solve_float(M, sum_rows, quad):
    A = [list(r) + [rhs] for (r, rhs) in sum_rows]
    for (r, rhs) in quad:
        A.append(list(r) + [rhs])
    A = np.array(A, dtype=float)
    # check rank
    coeff = A[:, :M]
    rhs = A[:, M]
    # need rank M
    # solve via least-squares; check residual
    try:
        sol, res, rank, sv = np.linalg.lstsq(coeff, rhs, rcond=None)
    except:
        return None
    if rank < M:
        return None
    # check residual
    if np.linalg.norm(coeff @ sol - rhs) > 1e-6:
        return None
    return sol

def main():
    t0 = time.time()
    total = 0
    feasible = 0
    candidates = []  # (ks, quad_idx, sol_float) for A < 2 candidates
    A_violations = 0
    min_A = None
    min_config = None
    # First pass: float solve, collect candidates with small A
    for ks in distributions():
        M, sum_rows, E, Z = hyperplanes_for_distribution(ks)
        all_hyp = E + Z
        for quad_idx in combinations(range(len(all_hyp)), 4):
            total += 1
            quad = [all_hyp[i] for i in quad_idx]
            sol = solve_float(M, sum_rows, quad)
            if sol is None:
                continue
            if any(s < -1e-9 for s in sol):
                continue
            feasible += 1
            s = sorted(sol, reverse=True)
            A = sum((-1)**i * v for i, v in enumerate(s))
            if min_A is None or A < min_A:
                min_A = A
                min_config = (ks, quad_idx, list(s))
            if A < 1.0 + 1e-6:
                candidates.append((ks, quad_idx, list(sol)))
            if A < 1.0 - 1e-6:
                A_violations += 1
            if total % 200000 == 0:
                el = time.time() - t0
                print(f"  progress: 4tuples={total} feasible={feasible} cand={len(candidates)} t={el:.1f}s rate={total/el:.0f}/s", flush=True)
    t1 = time.time()
    print(f"=== n=4 FLOAT pass ===")
    print(f"4-tuples examined: {total}")
    print(f"feasible (nonneg, float): {feasible}")
    print(f"candidates (A <= 1+eps): {len(candidates)}")
    print(f"A violations (A<1-eps): {A_violations}")
    print(f"min A (float): {min_A}")
    print(f"min config: {min_config}")
    print(f"total float time: {t1-t0:.1f}s, rate {total/(t1-t0):.0f}/s")
    # extrapolate exact Fraction time
    # sample 100 candidates, solve with Fraction, measure rate
    if candidates:
        t2 = time.time()
        n_verify = min(200, len(candidates))
        for (ks, quad_idx, sol_f) in candidates[:n_verify]:
            M, sum_rows, E, Z = hyperplanes_for_distribution(ks)
            all_hyp = E + Z
            quad = [all_hyp[i] for i in quad_idx]
            # build Fraction system
            Asys = [list(map(Fraction, r)) + [Fraction(rhs)] for (r, rhs) in sum_rows]
            for (r, rhs) in quad:
                Asys.append([Fraction(x) for x in r] + [Fraction(rhs)])
            # solve with Fraction gaussian elim
            # (reuse simple solver)
            _ = solve_fraction(M, Asys)
        t3 = time.time()
        rate_frac = n_verify / (t3 - t2) if t3 > t2 else 0
        print(f"Fraction verify rate: {rate_frac:.1f}/s; verifying all {len(candidates)} candidates would take {len(candidates)/rate_frac:.1f}s" if rate_frac>0 else "")

def solve_fraction(M, A):
    rows = len(A); cols = M+1
    pivot_cols = []
    r = 0
    for c in range(M):
        piv = -1
        for rr in range(r, rows):
            if A[rr][c] != 0:
                piv = rr; break
        if piv == -1: continue
        if piv != r: A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for rr in range(rows):
            if rr != r and A[rr][c] != 0:
                f = A[rr][c]
                A[rr] = [A[rr][k] - f*A[r][k] for k in range(cols)]
        pivot_cols.append(c); r += 1
        if r == rows: break
    if len(pivot_cols) != M: return None
    return [A[i][M] for i, c in enumerate(pivot_cols)]

if __name__ == "__main__":
    main()
