"""Explore the 12 distinct min multisets at n=4 and characterize them."""
from fractions import Fraction
from itertools import combinations

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

# Collect ALL min multisets (those with exact A == 1)
import numpy as np

min_multisets = []
for ks in distributions():
    M, sum_rows, E, Z = hyperplanes(ks)
    all_hyp = E + Z
    for quad_idx in combinations(range(len(all_hyp)), 4):
        quad = [all_hyp[i] for i in quad_idx]
        # exact directly (slower but we only need min ones; use float prefilter)
        A_float = [list(r)+[rhs] for (r,rhs) in sum_rows]
        for (r,rhs) in quad:
            A_float.append(list(r)+[rhs])
        A_arr = np.array(A_float, dtype=float)
        coeff = A_arr[:,:M]; rhs = A_arr[:,M]
        try:
            sol, res, rank, sv = np.linalg.lstsq(coeff, rhs, rcond=None)
        except: continue
        if rank < M: continue
        if np.linalg.norm(coeff @ sol - rhs) > 1e-6: continue
        if any(s < -1e-9 for s in sol): continue
        s = sorted(sol, reverse=True)
        A_val = sum((-1)**i * v for i,v in enumerate(s))
        if A_val < 1.0 + 1e-6:
            # exact verify
            Asys = [list(map(Fraction,r)) + [Fraction(rhs)] for (r,rhs) in sum_rows]
            for (r,rhs) in quad:
                Asys.append([Fraction(x) for x in r] + [Fraction(rhs)])
            sol_ex = solve_fraction(M, Asys)
            if sol_ex is None: continue
            if any(s < 0 for s in sol_ex): continue
            s_ex = tuple(sorted(sol_ex, reverse=True))
            A_ex = sum((-1)**i * v for i,v in enumerate(s_ex)) if False else Fraction(0)
            for i,v in enumerate(s_ex):
                if i%2==0: A_ex += v
                else: A_ex -= v
            if A_ex == 1:
                min_multisets.append((ks, s_ex))

# dedupe
seen = set()
unique_mins = []
for ks, s in min_multisets:
    if s not in seen:
        seen.add(s)
        unique_mins.append((ks, s))

print(f"Unique min multisets (A=1) at n=4: {len(unique_mins)}")
for ks, s in sorted(unique_mins, key=lambda x: x[1]):
    print(f"  ks={ks}  multiset={tuple(int(x) for x in s)}  sum={sum(s)}")
