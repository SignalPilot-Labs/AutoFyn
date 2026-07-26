"""
D3 2-adic census (fast, no determinant computation).

KEY OBSERVATION: at an arrangement vertex the pieces p_i = det_i / L where
L = det(active subsystem). The advantage
    A = sum_{i} c_i p_i = (sum_i c_i det_i) / L = num / L.
After reducing A = A_num / A_den, we have A = num/L = A_num/A_den in lowest
terms, so num = A_num * k and L = A_den * k for some positive integer k (signs
absorbed). Hence
    v2(num) - v2(L) = v2(A_num) - v2(A_den) = v2(A).
The explorer's conjecture "v2(num) < v2(L) at every fractional vertex" is
therefore EQUIVALENT to "v2(A) < 0", i.e. "A has a factor of 2 in its reduced
denominator" (A is not a 2-adic integer). This is a property of A alone and
needs no determinant.

We compute for every feasible arrangement vertex of the level-n dyadic
(n=3,4):
  - pieces p_i (exact Fraction)
  - A = alt-sum of sorted pieces (Fraction, reduced)
  - whether vertex is integer-valued (all p_i integers)
  - v2(A) = v2(A_num) - v2(A_den)
  - whether A >= 1
Signature reported.
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter

def v2(x):
    """2-adic valuation of a nonzero integer. Returns None for 0."""
    if x == 0:
        return None
    x = abs(x)
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v

def run(LIU, N_MARKS, D):
    NPL = len(LIU)

    def distributions():
        def comp(n, k):
            if k == 1:
                yield (n,); return
            for i in range(n+1):
                for rest in comp(n-i, k-1):
                    yield (i,) + rest
        yield from comp(N_MARKS, NPL)

    def solve_exact(M, B, b):
        A = [[Fraction(B[i][j]) for j in range(M)] + [Fraction(b[i])] for i in range(M)]
        rows = M; cols = M+1
        pivot_cols = []; r = 0
        for c in range(M):
            piv = -1
            for rr in range(r, rows):
                if A[rr][c] != 0:
                    piv = rr; break
            if piv == -1:
                continue
            if piv != r:
                A[r], A[piv] = A[piv], A[r]
            pv = A[r][c]
            A[r] = [x/pv for x in A[r]]
            for rr in range(rows):
                if rr != r and A[rr][c] != 0:
                    f = A[rr][c]
                    A[rr] = [A[rr][k] - f*A[r][k] for k in range(cols)]
            pivot_cols.append(c); r += 1
            if r == rows:
                break
        if len(pivot_cols) != M:
            return None
        for rr in range(r, rows):
            if A[rr][M] != 0:
                return None
        return [A[i][M] for i, c in enumerate(pivot_cols)]

    def build_rows(ks, hyp_idx):
        groups = []; vid = 0
        for j, kj in enumerate(ks):
            for i in range(kj+1):
                groups.append((j, i, vid)); vid += 1
        M = vid
        sum_rows = []
        for j in range(NPL):
            row = [0]*M
            for (gj, i, v) in groups:
                if gj == j:
                    row[v] = 1
            sum_rows.append((row, LIU[j]))
        E = []
        for a in range(M):
            for b_ in range(a+1, M):
                row = [0]*M; row[a] = 1; row[b_] = -1
                E.append((row, 0))
        Z = []
        for a in range(M):
            row = [0]*M; row[a] = 1
            Z.append((row, 0))
        all_hyp = E + Z
        trip = [all_hyp[i] for i in hyp_idx]
        rows_b = [(list(r), rhs) for (r, rhs) in sum_rows]
        for (r, rhs) in trip:
            rows_b.append((list(r), rhs))
        B = [r for (r, _) in rows_b]
        b = [rhs for (_, rhs) in rows_b]
        return M, B, b

    minA_int = None; minA_frac = None
    n_vertices = 0; n_int = 0; n_frac = 0
    n_frac_A_ge_1 = 0
    n_frac_v2A_lt_0 = 0       # v2(num) < v2(L) equivalent
    v2L_counter_frac = Counter()    # v2(A_den) distribution (proxy for v2(L) modulo k)
    v2A_counter_frac = Counter()
    min_frac_examples = []
    A_values_frac = []

    for ks in distributions():
        # count subpieces
        vid = 0
        for j, kj in enumerate(ks):
            vid += kj+1
        M = vid
        nE = M*(M-1)//2
        nZ = M
        nH = nE + nZ
        for hyp_idx in combinations(range(nH), N_MARKS):
            M2, B, b = build_rows(ks, hyp_idx)
            assert M2 == M
            sol = solve_exact(M, B, b)
            if sol is None:
                continue
            if any(s < 0 for s in sol):
                continue
            n_vertices += 1
            s = sorted(sol, reverse=True)
            A = Fraction(0)
            for i, v in enumerate(s):
                if i % 2 == 0:
                    A += v
                else:
                    A -= v
            all_int = all(x.denominator == 1 for x in s)
            A_num = A.numerator
            A_den = A.denominator
            if A == 0:
                v2A = None
                v2n = None; v2d = None
            else:
                v2n = v2(A_num)
                v2d = v2(A_den)
                v2A = v2n - v2d
            if all_int:
                n_int += 1
                if minA_int is None or A < minA_int:
                    minA_int = A
            else:
                n_frac += 1
                if minA_frac is None or A < minA_frac:
                    minA_frac = A
                    min_frac_examples = [(list(s), A, v2n, v2d, v2A)]
                elif A == minA_frac and len(min_frac_examples) < 8:
                    min_frac_examples.append((list(s), A, v2n, v2d, v2A))
                if A >= 1:
                    n_frac_A_ge_1 += 1
                if A != 0 and v2A is not None and v2A < 0:
                    n_frac_v2A_lt_0 += 1
                v2L_counter_frac[v2d] += 1   # v2(A_den) = "v2(L) - v2(k)"
                v2A_counter_frac[v2A] += 1
                A_values_frac.append((A, v2A, v2n, v2d))

    print(f"=== n={N_MARKS}, D={D}, LIU={LIU} ===")
    print(f"total feasible vertices: {n_vertices}")
    print(f"  integer-valued: {n_int},  min A (int)  = {minA_int} (real {minA_int/D if minA_int else None})")
    print(f"  fractional:     {n_frac}, min A (frac) = {minA_frac} (real {minA_frac/D if minA_frac else None})")
    print(f"fractional vertices with A >= 1 : {n_frac_A_ge_1} / {n_frac}")
    print(f"fractional vertices with v2(A) < 0 (equiv v2(num) < v2(L)): {n_frac_v2A_lt_0} / {n_frac}")
    print(f"distribution of v2(A_den) at fractional vertices: {dict(sorted(v2L_counter_frac.items()))}")
    print(f"distribution of v2(A) at fractional vertices: {dict(sorted(v2A_counter_frac.items()))}")
    # min A examples
    print(f"min fractional A examples (pieces, A, v2(A_num), v2(A_den), v2(A)):")
    for ex in min_frac_examples:
        s, A, vn, vd, vA = ex
        print(f"    pieces={s}")
        print(f"      A={A}={float(A):.6f}, v2(A_num)={vn}, v2(A_den)={vd}, v2(A)={vA}, A_num={A.numerator}, A_den={A.denominator}")
    # also: are there fractional vertices with v2(A) >= 0? (A is a 2-adic integer)
    n_frac_v2A_ge_0 = sum(c for v, c in v2A_counter_frac.items() if v is not None and v >= 0)
    print(f"fractional vertices with v2(A) >= 0 (A is a 2-adic integer): {n_frac_v2A_ge_0}")
    # if any, list them
    if n_frac_v2A_ge_0 > 0:
        print("  examples of fractional vertices with v2(A) >= 0:")
        cnt = 0
        for (A, vA, vn, vd) in A_values_frac:
            if vA is not None and vA >= 0:
                print(f"    A={A}, v2(A)={vA}, v2(A_num)={vn}, v2(A_den)={vd}")
                cnt += 1
                if cnt >= 20:
                    break
    return


if __name__ == "__main__":
    print("### n=3 census ###")
    run([1, 2, 4, 8], 3, 15)
    print()
    print("### n=4 census ###")
    run([1, 2, 4, 8, 16], 4, 31)
