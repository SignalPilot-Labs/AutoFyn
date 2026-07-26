"""
Feasibility probe for n=4 cell-complex vertex enumeration.
Liu level-4 dyadic: (1, 2, 4, 8, 16)/31, total 31 (integer units).
4 Xiang marks -> 5 sub-pieces per Liu piece if all 4 land in one piece,
total sub-pieces = 4 + 5 = 9.
For each distribution (k_1,...,k_5), sum k_j = 4, # sub-pieces = 9.
Arrangement: E (piece-equality) = C(9,2)=36, Z (piece-zero)=9 -> 45 hyperplanes.
Triples per distribution: C(45,3)=14190. Distributions: C(8,4)=70.
Total triples: 70 * 14190 = 993300.
"""
import sys, time
from fractions import Fraction
from itertools import combinations

# Liu pieces (integer units, total 31)
LIU = [1, 2, 4, 8, 16]
N_MARKS = 4
N_PIECES_LIU = 5  # = len(LIU)
D4 = 31

# enumerate distributions (k_1,...,k_5) nonneg sum=4
def distributions():
    for k1 in range(N_MARKS+1):
        for k2 in range(N_MARKS+1-k1):
            for k3 in range(N_MARKS+1-k1-k2):
                for k4 in range(N_MARKS+1-k1-k2-k3):
                    k5 = N_MARKS - k1 - k2 - k3 - k4
                    yield (k1,k2,k3,k4,k5)

# For a distribution (k_1,..,k_5), the sub-pieces are grouped:
# piece-j group has (k_j+1) sub-pieces summing to LIU[j].
# Variables: enumerate them flat with a (group, idx) label.
# Total #variables M = sum (k_j+1) = 9.

# Hyperplanes:
#  E: s_a = s_b for distinct variables a,b (regardless of group)
#  Z: s_a = 0 for each variable a
# Sum-constraints: 5 (one per group)

def hyperplanes_for_distribution(ks):
    # build variable list: var_id = (group_j, idx_within_group)
    groups = []
    vid = 0
    var_group = []
    for j, kj in enumerate(ks):
        for i in range(kj+1):
            groups.append((j, i, vid))
            var_group.append(j)
            vid += 1
    M = vid  # = 9
    # sum constraint rows: for each group j, sum of its vars = LIU[j]
    sum_rows = []
    for j in range(N_PIECES_LIU):
        row = [Fraction(0)]*M
        for (gj, i, v) in groups:
            if gj == j:
                row[v] = Fraction(1)
        sum_rows.append((row, Fraction(LIU[j])))
    # E hyperplanes: s_a - s_b = 0
    E = []
    for a in range(M):
        for b in range(a+1, M):
            row = [Fraction(0)]*M
            row[a] = Fraction(1)
            row[b] = Fraction(-1)
            E.append((row, Fraction(0)))
    # Z hyperplanes: s_a = 0
    Z = []
    for a in range(M):
        row = [Fraction(0)]*M
        row[a] = Fraction(1)
        Z.append((row, Fraction(0)))
    return M, sum_rows, E, Z, var_group

def solve_system(M, sum_rows, triple):
    # build augmented matrix
    A = [list(r) + [rhs] for (r, rhs) in sum_rows]
    for (r, rhs) in triple:
        A.append(list(r) + [rhs])
    # Gaussian elimination on A (rows = M+? , cols = M+1)
    # need exactly M independent rows for unique solution
    rows = len(A)
    cols = M + 1
    # use Fraction arithmetic
    pivot_cols = []
    r = 0
    for c in range(M):
        # find pivot in column c, row >= r
        piv = -1
        for rr in range(r, rows):
            if A[rr][c] != 0:
                piv = rr
                break
        if piv == -1:
            continue
        if piv != r:
            A[r], A[piv] = A[piv], A[r]
        # normalize
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        # eliminate
        for rr in range(rows):
            if rr != r and A[rr][c] != 0:
                f = A[rr][c]
                A[rr] = [A[rr][k] - f * A[r][k] for k in range(cols)]
        pivot_cols.append(c)
        r += 1
        if r == rows:
            break
    # check rank == M
    if len(pivot_cols) != M:
        return None  # underdetermined or inconsistent
    # check consistency: any row with all zeros in coeff but nonzero rhs?
    for rr in range(r, rows):
        if A[rr][M] != 0:
            return None  # inconsistent
    # extract solution
    sol = [Fraction(0)]*M
    for i, c in enumerate(pivot_cols):
        sol[c] = A[i][M]
    return sol

def main():
    t0 = time.time()
    total_triples = 0
    unique_solved = 0
    feasible = 0
    violations = 0
    min_A = None
    min_config = None
    distinct_multisets = set()
    for ks in distributions():
        M, sum_rows, E, Z, var_group = hyperplanes_for_distribution(ks)
        all_hyp = E + Z
        # enumerate triples
        for triple_idx in combinations(range(len(all_hyp)), 3):
            total_triples += 1
            triple = [all_hyp[i] for i in triple_idx]
            sol = solve_system(M, sum_rows, triple)
            if sol is None:
                continue
            unique_solved += 1
            # feasibility: all nonneg
            if any(s < 0 for s in sol):
                continue
            feasible += 1
            # compute A = alt-sum of sorted-desc sub-pieces
            s = sorted(sol, reverse=True)
            # remove zeros? Actually zeros are valid (they're degenerate)
            # A = sum_{i=0}^{M-1} (-1)^i s[i]
            A = Fraction(0)
            for i, v in enumerate(s):
                if i % 2 == 0:
                    A += v
                else:
                    A -= v
            ms = tuple(s)
            distinct_multisets.add(tuple(Fraction(x) for x in ms))
            if min_A is None or A < min_A:
                min_A = A
                min_config = (ks, triple_idx, ms)
            if A < 1:  # target alpha(4)*D(4) = 1
                violations += 1
                if violations <= 5:
                    print("VIOLATION:", A, ks, triple_idx, ms)
            if total_triples % 50000 == 0:
                el = time.time() - t0
                print(f"  progress: triples={total_triples} feasible={feasible} t={el:.1f}s", flush=True)
    t1 = time.time()
    print("=== n=4 cell vertex enumeration ===")
    print(f"distributions: 70")
    print(f"triples examined: {total_triples}")
    print(f"unique-solved systems: {unique_solved}")
    print(f"feasible (nonneg) vertices: {feasible}")
    print(f"distinct piece-multisets: {len(distinct_multisets)}")
    print(f"min A (integer scale): {min_A}  (real: {min_A/D4 if min_A else None})")
    print(f"target: 1 (real: 1/31)")
    print(f"VIOLATIONS (A<1): {violations}")
    print(f"min config: {min_config}")
    print(f"total time: {t1-t0:.1f}s")

if __name__ == "__main__":
    main()
