from fractions import Fraction
from itertools import combinations

LIU = [1, 2, 4, 8]
N_MARKS = 3
N_PIECES_LIU = 4

def distributions():
    for k1 in range(N_MARKS+1):
        for k2 in range(N_MARKS+1-k1):
            for k3 in range(N_MARKS+1-k1-k2):
                k4 = N_MARKS - k1 - k2 - k3
                yield (k1,k2,k3,k4)

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

frac_count = 0; int_count = 0; total = 0; min_A_frac = None
for ks in distributions():
    M, sum_rows, E, Z = hyperplanes(ks)
    all_hyp = E + Z
    for trip_idx in combinations(range(len(all_hyp)), 3):
        trip = [all_hyp[i] for i in trip_idx]
        Asys = [list(map(Fraction,r)) + [Fraction(rhs)] for (r,rhs) in sum_rows]
        for (r,rhs) in trip:
            Asys.append([Fraction(x) for x in r] + [Fraction(rhs)])
        sol = solve_fraction(M, Asys)
        if sol is None: continue
        if any(s < 0 for s in sol): continue
        total += 1
        all_int = all(s.denominator == 1 for s in sol)
        if all_int: int_count += 1
        else: frac_count += 1
        s = sorted(sol, reverse=True)
        A = Fraction(0)
        for i,v in enumerate(s):
            if i%2==0: A += v
            else: A -= v
        if min_A_frac is None or A < min_A_frac:
            min_A_frac = A
            if not all_int:
                pass
print(f"n=3 vertices: total feasible={total}, integer-valued={int_count}, fractional={frac_count}")
print(f"min A = {min_A_frac}")
# show a fractional example
for ks in distributions():
    M, sum_rows, E, Z = hyperplanes(ks)
    all_hyp = E + Z
    for trip_idx in combinations(range(len(all_hyp)), 3):
        trip = [all_hyp[i] for i in trip_idx]
        Asys = [list(map(Fraction,r)) + [Fraction(rhs)] for (r,rhs) in sum_rows]
        for (r,rhs) in trip:
            Asys.append([Fraction(x) for x in r] + [Fraction(rhs)])
        sol = solve_fraction(M, Asys)
        if sol is None: continue
        if any(s < 0 for s in sol): continue
        if not all(s.denominator==1 for s in sol):
            s = sorted(sol, reverse=True)
            A = sum((v if i%2==0 else -v) for i,v in enumerate(s))
            print(f"  fractional vertex: ks={ks} sol={sol} A={A}")
            break
    else: continue
    break
