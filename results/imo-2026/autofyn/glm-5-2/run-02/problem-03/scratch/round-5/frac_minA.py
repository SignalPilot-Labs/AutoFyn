from fractions import Fraction
from itertools import combinations

def run(LIU, N_MARKS, D):
    NPL = len(LIU)
    def distributions():
        # compositions of N_MARKS into NPL parts
        def comp(n, k):
            if k==1: yield (n,); return
            for i in range(n+1):
                for rest in comp(n-i, k-1):
                    yield (i,)+rest
        yield from comp(N_MARKS, NPL)
    def hyperplanes(ks):
        groups = []; vid = 0
        for j, kj in enumerate(ks):
            for i in range(kj+1):
                groups.append((j,i,vid)); vid += 1
        M = vid
        sum_rows = []
        for j in range(NPL):
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
    minA_frac = None; minA_int = None
    for ks in distributions():
        M, sum_rows, E, Z = hyperplanes(ks)
        all_hyp = E + Z
        for idx in combinations(range(len(all_hyp)), N_MARKS):
            trip = [all_hyp[i] for i in idx]
            Asys = [list(map(Fraction,r)) + [Fraction(rhs)] for (r,rhs) in sum_rows]
            for (r,rhs) in trip:
                Asys.append([Fraction(x) for x in r] + [Fraction(rhs)])
            sol = solve_fraction(M, Asys)
            if sol is None: continue
            if any(s < 0 for s in sol): continue
            s = sorted(sol, reverse=True)
            A = Fraction(0)
            for i,v in enumerate(s):
                if i%2==0: A += v
                else: A -= v
            all_int = all(x.denominator==1 for x in s)
            if all_int:
                if minA_int is None or A < minA_int: minA_int = A
            else:
                if minA_frac is None or A < minA_frac: minA_frac = A
    print(f"n={N_MARKS}: min A over INTEGER vertices = {minA_int}, min A over FRACTIONAL vertices = {minA_frac} (real: {minA_frac/D if minA_frac else None})")

run([1,2,4,8], 3, 15)
