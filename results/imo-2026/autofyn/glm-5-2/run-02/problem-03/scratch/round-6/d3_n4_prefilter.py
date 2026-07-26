"""
n=4 D3 2-adic census via float prefilter.
Collects all feasible arrangement vertices of the level-4 dyadic with
float-A <= 3 (captures the low-A fractional region where the min 5/3 lives,
and all integer-A=1,2,3 vertices), then exact-verifies with Fraction and
computes v2(A) for the fractional ones.

Reports:
  - min fractional A (exact) and example multiset
  - v2(A) distribution over the exact-verified fractional candidates
  - whether v2(A) < 0 holds (explorer's conjecture)
"""
import time
from fractions import Fraction
from itertools import combinations
from collections import Counter
import numpy as np

LIU = [1, 2, 4, 8, 16]
N_MARKS = 4
N_PIECES_LIU = 5
D4 = 31

def v2(x):
    if x == 0:
        return None
    x = abs(x)
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v

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
    total = 0
    THRESH = 3.0  # capture all vertices with float-A <= 3
    for ks in distributions():
        M, sum_rows, E, Z = hyperplanes(ks)
        all_hyp = E + Z
        for quad_idx in combinations(range(len(all_hyp)), 4):
            total += 1
            quad = [all_hyp[i] for i in quad_idx]
            sol = solve_float(M, sum_rows, quad)
            if sol is None: continue
            if any(s < -1e-9 for s in sol): continue
            s = sorted(sol, reverse=True)
            A = sum((-1)**i * v for i,v in enumerate(s))
            if A < THRESH + 1e-6:
                candidates.append((ks, quad_idx, list(sol)))
    t1 = time.time()
    print(f"float pass: {total} 4-tuples, {len(candidates)} candidates with A<={THRESH}, {t1-t0:.1f}s")
    # exact verification
    minA_int = None; minA_frac = None
    min_frac_examples = []
    n_int = 0; n_frac = 0
    n_frac_v2A_lt_0 = 0
    v2A_counter_frac = Counter()
    v2Aden_counter_frac = Counter()
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
        s = sorted(sol, reverse=True)
        A = Fraction(0)
        for i,v in enumerate(s):
            if i%2==0: A += v
            else: A -= v
        all_int = all(x.denominator == 1 for x in s)
        A_num = A.numerator; A_den = A.denominator
        if A != 0:
            v2n = v2(A_num); v2d = v2(A_den); v2A = v2n - v2d
        else:
            v2n = v2d = v2A = None
        if all_int:
            n_int += 1
            if minA_int is None or A < minA_int: minA_int = A
        else:
            n_frac += 1
            if minA_frac is None or A < minA_frac:
                minA_frac = A
                min_frac_examples = [(list(s), A, v2n, v2d, v2A)]
            elif A == minA_frac and len(min_frac_examples) < 6:
                min_frac_examples.append((list(s), A, v2n, v2d, v2A))
            if v2A is not None and v2A < 0:
                n_frac_v2A_lt_0 += 1
            if v2A is not None:
                v2A_counter_frac[v2A] += 1
                v2Aden_counter_frac[v2d] += 1
    t2 = time.time()
    print(f"=== n=4 EXACT (candidates with A<={THRESH}) ===")
    print(f"exact integer-valued: {n_int}, min A (int) = {minA_int} (real {minA_int/D4 if minA_int else None})")
    print(f"exact fractional:     {n_frac}, min A (frac) = {minA_frac} (real {minA_frac/D4 if minA_frac else None})")
    print(f"fractional (in low-A region) with v2(A) < 0: {n_frac_v2A_lt_0} / {n_frac}")
    print(f"v2(A) distribution over fractional low-A region: {dict(sorted(v2A_counter_frac.items()))}")
    print(f"v2(A_den) distribution: {dict(sorted(v2Aden_counter_frac.items()))}")
    print(f"min fractional A examples:")
    for ex in min_frac_examples:
        s, A, vn, vd, vA = ex
        print(f"    pieces={s}")
        print(f"      A={A}={float(A):.6f}, v2(A_num)={vn}, v2(A_den)={vd}, v2(A)={vA}, A_num={A.numerator}, A_den={A.denominator}")
    print(f"exact verify time: {t2-t1:.1f}s")

if __name__ == "__main__":
    main()
