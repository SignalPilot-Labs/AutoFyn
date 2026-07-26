"""
EXHAUSTIVE full-arrangement vertex enumeration for L(3) over reals.

Liu pieces (1,2,4,8) integer scale, total 15. Xiang's 3 marks refine into
7 sub-pieces (grouped into 4 Liu-piece groups summing to 1,2,4,8 resp.).
A = alt sum of sorted-desc. Want A >= 1.

A is continuous + piecewise-linear in the 3 mark-parameters. The arrangement
hyperplanes (within a fixed distribution = grouping of sub-pieces into Liu
pieces) are:
  (E) piece-equality: x_a = x_b   (C(7,2)=21 of these)
  (Z) piece-zero:     x_a = 0     (7 of these; sub-piece=0 = mark at Liu mark
                                  or two marks coinciding or mark at stick end)
Vertices = points where 3 INDEPENDENT such hyperplanes meet (rank 3 on top of
the 4 sum-constraints => 7 constraints, 7 unknowns, rank 7).

We enumerate, for every distribution (k1,k2,k3,k4) sum=3:
  - every triple of hyperplanes from E ∪ Z (28 hyperplanes, C(28,3)=3276 triples)
  - solve the 7x7 exact-rational system (4 sum-rows + 3 constraint-rows)
  - if unique nonneg solution exists, compute A, check >= 1.
This is exhaustive over all arrangement vertices (incl. piece-zero vertices and
degenerate >=4-hyperplane vertices, which are limits of generic 3-hyperplane ones
but we include them directly for safety).
"""
from fractions import Fraction as F
from itertools import combinations

LIU = [F(1), F(2), F(4), F(8)]
TARGET = F(1)

def alt_sum(pieces):
    ps = sorted(pieces, reverse=True)
    A = F(0)
    for i,p in enumerate(ps):
        A += (1 if i%2==0 else -1)*p
    return A

def gauss_solve(rows, rhs, nvar):
    """Solve rows*x = rhs. rows: list of F-lists (length nvar). Return unique sol or None."""
    aug = [list(r)+[b] for r,b in zip(rows,rhs)]
    nrows = len(aug)
    piv_cols = []
    r = 0
    for c in range(nvar):
        pr = None
        for rr in range(r, nrows):
            if aug[rr][c] != 0:
                pr = rr; break
        if pr is None: continue
        aug[r], aug[pr] = aug[pr], aug[r]
        piv = aug[r][c]
        aug[r] = [x/piv for x in aug[r]]
        for rr in range(nrows):
            if rr != r and aug[rr][c] != 0:
                f = aug[rr][c]
                aug[rr] = [a-b*f for a,b in zip(aug[rr], aug[r])]
        piv_cols.append(c)
        r += 1
        if r == nrows: break
    for rr in range(r, nrows):
        if aug[rr][nvar] != 0:
            return None
    if len(piv_cols) != nvar:
        return None
    sol = [F(0)]*nvar
    for i,c in enumerate(piv_cols):
        sol[c] = aug[i][nvar]
    return sol

# enumerate distributions
distributions = []
for k1 in range(4):
  for k2 in range(4-k1):
    for k3 in range(4-k1-k2):
      k4 = 3-k1-k2-k3
      distributions.append((k1,k2,k3,k4))

# sum-constraint rows for a distribution
def sum_rows(ks):
    """Return (rows, rhs): 4 rows, each length 7. Row j has 1 in positions of
    Liu-piece-j sub-pieces, rhs = L_j."""
    groups = []
    for j,k in enumerate(ks):
        for _ in range(k+1):
            groups.append(j)
    rows = []
    rhs = []
    for j in range(4):
        row = [F(0)]*7
        for i in range(7):
            if groups[i]==j:
                row[i] = F(1)
        rows.append(row)
        rhs.append(LIU[j])
    return rows, rhs, groups

# build the 28 hyperplanes (constraints): each as (row, rhs)
# E: x_a - x_b = 0  (a<b)
# Z: x_a = 0
def hyperplanes():
    hs = []
    for a in range(7):
        for b in range(a+1,7):
            row = [F(0)]*7
            row[a] = F(1); row[b] = F(-1)
            hs.append(('E',a,b,row,F(0)))
    for a in range(7):
        row = [F(0)]*7
        row[a] = F(1)
        hs.append(('Z',a,None,row,F(0)))
    return hs

H = hyperplanes()
print("hyperplanes:", len(H))

vertices = {}   # key=piece-multiset -> (A, examples)
violations = []
minA = None
min_examples = []
n_vertices = 0
n_triples = 0
n_uniquesolved = 0

for ks in distributions:
    srows, srhs, groups = sum_rows(ks)
    for triple in combinations(range(len(H)), 3):
        n_triples += 1
        rows = [list(r) for r in srows]
        rhs = list(srhs)
        for ti in triple:
            _,_,_,r,b = H[ti]
            rows.append(list(r))
            rhs.append(b)
        sol = gauss_solve(rows, rhs, 7)
        if sol is None:
            continue
        n_uniquesolved += 1
        if any(s < 0 for s in sol):
            continue
        # also require: the 3 hyperplane constraints are genuinely among the active
        # (the solution automatically satisfies them by construction). But we also
        # require non-degeneracy of the vertex: at least 3 constraints active beyond
        # sums. This is automatic (we added 3). However, the vertex must be a genuine
        # arrangement point: the solution should satisfy the hyperplanes. (It does.)
        pieces = tuple(sol)
        A = alt_sum(pieces)
        n_vertices += 1
        key = tuple(sorted(pieces, reverse=True))
        if key not in vertices:
            vertices[key] = (A, [])
        vertices[key][1].append((ks, triple))
        if minA is None or A < minA:
            minA = A
            min_examples = [(ks, triple, pieces, A)]
        elif A == minA:
            min_examples.append((ks, triple, pieces, A))
        if A < TARGET:
            violations.append((ks, triple, pieces, A))

print("distributions:", len(distributions))
print("triples examined:", n_triples)
print("unique-solved systems:", n_uniquesolved)
print("feasible (nonneg) vertices:", n_vertices)
print("distinct piece-multisets:", len(vertices))
print("min A (integer scale):", minA, " real:", minA/15 if minA else None)
print("target:", TARGET, "real:", TARGET/15)
print("VIOLATIONS (A < 1):", len(violations))
for v in violations[:20]:
    print("  ", v)

print()
print("A-value histogram:")
from collections import Counter
cnt = Counter()
for k,v in vertices.items():
    cnt[v[0]] += 1
for val in sorted(cnt):
    print(f"  A={val}  (={val/15} real)  distinct-multisets={cnt[val]}")

print()
print("min-attaining multisets (first 20):")
shown = set()
for ks,triple,pieces,A in min_examples[:50]:
    key = tuple(sorted(pieces, reverse=True))
    if key in shown: continue
    shown.add(key)
    print(f"  pieces={list(key)}  A={A}  (ks={ks})")
    if len(shown) >= 20: break

print()
print("total distinct min-multisets:", len(set(tuple(sorted(p,reverse=True)) for ks,t,p,A in min_examples for p in [p])))
