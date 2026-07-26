"""
Exact Fraction verification of the n=4 cell-vertex candidates.
Re-runs the float enumeration, collects candidates with A <= 1 + eps (float),
then verifies each exactly with Fraction arithmetic. Reports exact min A and violations.
"""
import time
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

def hyperplanes(ks):
    groups = []; vid = 0
    for j, kj in enumerate(ks):
        for i in range(kj+1):
            groups.append((j,i,vid)); vid += 1
    M = vid
    sum_rows = []
    for j in range(N_PIECES_LIU):
        row = [0]*M
        for (gj,i,v) in groups:
            if gj == j: row[v] = 1
        sum_rows.append((row, LIU[j]))
    E = []
    for a in range(M):
        for b in range(a+1, M):
            row = [0]*M; row[a]=1; row[b]=-1
            E.append((row, 0))
    Z = []
    for a in range(M):
        row = [0]*M; row[a]=1
        Z.append((row, 0))
    return M, sum_rows, E, Z

def solve_float(M, sum_rows, quad):
    A = [list(r)+[rhs] for (r,rhs) in sum_rows]
    for (r,rhs) in quad:
        A.append(list(r)+[rhs])
    A = np.array(A, dtype=float)
    coeff = A[:,:M]; rhs = A[:,M]
    try:
        sol, res, rank, sv = np.linalg.lstsq(coeff, rhs, rcond=None)
    except: return None
    if rank < M: return None
    if np.linalg.norm(coeff @ sol - rhs) > 1e-6: return None
    return sol

def solve_fraction(M, A):
    rows = len(A); cols = M+1
    pivot_cols = []; r = 0
    for c in range(M):
        piv = -1
        for rr in range(r, rows):
            if A[rr][c] != 0: piv = rr; break
        if piv == -1: continue
        if piv != r: A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x/pv for x in A[r]]
        for rr in range(rows):
            if rr != r and A[rr][c] != 0:
                f = A[rr][c]
                A[rr] = [A[rr][k] - f*A[r][k] for k in range(cols)]
        pivot_cols.append(c); r += 1
        if r == rows: break
    if len(pivot_cols) != M: return None
    for rr in range(r, rows):
        if A[rr][M] != 0: return None
    return [A[i][M] for i,c in enumerate(pivot_cols)]

def main():
    t0 = time.time()
    candidates = []
    feasible_float = 0
    total = 0
    for ks in distributions():
        M, sum_rows, E, Z = hyperplanes(ks)
        all_hyp = E + Z
        for quad_idx in combinations(range(len(all_hyp)), 4):
            total += 1
            quad = [all_hyp[i] for i in quad_idx]
            sol = solve_float(M, sum_rows, quad)
            if sol is None: continue
            if any(s < -1e-9 for s in sol): continue
            feasible_float += 1
            s = sorted(sol, reverse=True)
            A = sum((-1)**i * v for i,v in enumerate(s))
            if A < 1.0 + 1e-6:
                candidates.append((ks, quad_idx, list(sol)))
    t1 = time.time()
    print(f"float pass: {total} 4-tuples, {feasible_float} feasible, {len(candidates)} candidates, {t1-t0:.1f}s")
    # exact verification
    exact_min_A = None
    exact_min_config = None
    exact_violations = 0
    exact_feasible = 0
    seen_multisets = set()
    for (ks, quad_idx, sol_f) in candidates:
        M, sum_rows, E, Z = hyperplanes(ks)
        all_hyp = E + Z
        quad = [all_hyp[i] for i in quad_idx]
        Asys = [list(map(Fraction,r)) + [Fraction(rhs)] for (r,rhs) in sum_rows]
        for (r,rhs) in quad:
            Asys.append([Fraction(x) for x in r] + [Fraction(rhs)])
        sol = solve_fraction(M, Asys)
        if sol is None: continue
        if any(s < 0 for s in sol): continue
        exact_feasible += 1
        s = tuple(sorted(sol, reverse=True))
        seen_multisets.add(s)
        A = Fraction(0)
        for i,v in enumerate(s):
            if i%2==0: A += v
            else: A -= v
        if exact_min_A is None or A < exact_min_A:
            exact_min_A = A
            exact_min_config = (ks, quad_idx, s)
        if A < 1:
            exact_violations += 1
            if exact_violations <= 10:
                print(f"  EXACT VIOLATION: A={A} ks={ks} quad={quad_idx} s={s}")
    t2 = time.time()
    print(f"=== n=4 EXACT verification ===")
    print(f"candidates verified: {len(candidates)}, exact feasible: {exact_feasible}")
    print(f"distinct multisets (exact): {len(seen_multisets)}")
    print(f"min A (exact, integer scale): {exact_min_A}  (real: {exact_min_A/D4 if exact_min_A else None})")
    print(f"target: 1 (real: 1/{D4})")
    print(f"EXACT VIOLATIONS (A<1): {exact_violations}")
    print(f"min config: ks={exact_min_config[0] if exact_min_config else None}, multiset={exact_min_config[2] if exact_min_config else None}")
    # show a few distinct min multisets
    print(f"verify time: {t2-t1:.1f}s")

if __name__ == "__main__":
    main()
