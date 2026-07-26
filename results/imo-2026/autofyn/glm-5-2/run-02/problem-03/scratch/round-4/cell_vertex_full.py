"""
Full arrangement vertex enumeration for L(3) over reals.

Liu pieces (1,2,4,8) integer scale, total 15. Xiang 3 marks refine into 7 sub-pieces.
A = alt sum of sorted-desc. Want A >= 1 (= 1/15 real scale).

A is continuous + piecewise-linear in the mark-vector. The arrangement is the
piece-equality hyperplanes (two sub-pieces equal) plus piece=0 (boundary).
Vertices = points where 3 independent equalities hold.

Reformulation: the 7 sub-piece SIZES are 7 nonneg reals grouped into 4 groups
(each group sums to one of 1,2,4,8). DOF = 3. A vertex = 3 independent size-equalities.
At a vertex, the 7 sizes are determined (solve 4 sum-constraints + 3 equalities).

We enumerate:
  - all distributions (k1,k2,k3,k4), sum=3, ki>=0  (how many marks in each Liu piece)
  - all set-partitions of the 7 sub-pieces into <=4 blocks (equality groups)
  - for each, solve the linear system (4 sums + equality constraints), check nonneg,
    compute A (sorted desc, alt sum), check A >= 1.

Degenerate vertices (>=4 equalities, <=3 blocks) are limits of generic (4-block) ones,
covered by continuity; we include them anyway for safety.
"""
from fractions import Fraction as F
from itertools import product
import itertools

LIU = [F(1), F(2), F(4), F(8)]   # Liu piece sizes (integer scale)
TOTAL = F(15)
TARGET = F(1)   # A >= 1

def alt_sum(pieces):
    """A = sorted-desc alternating sum. Ties contribute 0 net (continuous extension)."""
    ps = sorted(pieces, reverse=True)
    A = F(0)
    for i,p in enumerate(ps):
        s = 1 if (i % 2 == 0) else -1
        A += s*p
    return A

# enumerate distributions
distributions = []
for k1 in range(4):
  for k2 in range(4-k1):
    for k3 in range(4-k1-k2):
      k4 = 3-k1-k2-k3
      distributions.append((k1,k2,k3,k4))

print("distributions:", len(distributions))

# For each distribution, build sub-piece labels and their group (Liu piece index)
def subpiece_groups(ks):
    """returns list of (liu_index) for each of the 7 sub-pieces."""
    groups = []
    for j,k in enumerate(ks):
        for _ in range(k+1):
            groups.append(j)
    return groups  # length 7

# set partitions of {0..6} into <=4 blocks
def set_partitions(n, max_blocks):
    """Yield partitions of {0..n-1} into lists, with <= max_blocks blocks."""
    if n == 0:
        yield []
        return
    # recursive: assign element 0..n-1
    def rec(i, blocks):
        if i == n:
            yield [list(b) for b in blocks]
            return
        # add to existing block
        for b in blocks:
            b.append(i)
            yield from rec(i+1, blocks)
            b.pop()
        # new block
        if len(blocks) < max_blocks:
            blocks.append([i])
            yield from rec(i+1, blocks)
            blocks.pop()
    yield from rec(0, [])

# Solve the vertex system for a given (distribution, partition):
# unknowns = block sizes (one per block). Constraints:
#   for each Liu piece j: sum over blocks of (count of j's subpieces in block) * size(block) = L_j
# This is a linear system. If the partition has m blocks, we have 4 equations in m unknowns.
# For a vertex (generic, m=4), 4x4 square. For m<4, overdetermined -> check consistency.
# (m>4 can't pin all DOF -> not a vertex, skip.)
#
# Additionally, blocks containing only the "fixed" (k_j=0) pieces are pre-determined,
# but the linear system handles that automatically.

import sys

def solve_vertex(ks, partition):
    """Try to solve for block sizes. Return (sizes_dict, ok) where sizes_dict maps
    subpiece index -> size, or (None, False) if infeasible/underdetermined."""
    groups = subpiece_groups(ks)  # groups[i] = Liu index of sub-piece i
    m = len(partition)
    # block index for each sub-piece
    block_of = {}
    for bi, block in enumerate(partition):
        for sp in block:
            block_of[sp] = bi
    # Build 4 equations: for j in 0..3, sum_{sp: groups[sp]=j} size(block_of[sp]) = L_j
    # => sum_{bi} cnt[j][bi] * x[bi] = L_j   where cnt[j][bi] = # of subpieces of Liu j in block bi
    # Matrix: 4 rows, m cols
    rows = []
    rhs = []
    for j in range(4):
        row = [F(0)]*m
        for sp in range(7):
            if groups[sp] == j:
                row[block_of[sp]] += F(1)
        rows.append(row)
        rhs.append(LIU[j])
    # Solve via Gaussian elimination (4 x m)
    sol = gauss(rows, rhs, m)
    if sol is None:
        return None, False
    # map sub-piece -> size
    sizes = {}
    for sp in range(7):
        sizes[sp] = sol[block_of[sp]]
    return sizes, True

def nullspace_check(rows, m):
    """Is the system consistent and uniquely determined? Returns sol or None."""
    pass

def gauss(rows, rhs, ncol):
    """Solve rows (list of F-lists) x = rhs. Return solution (list of ncol) or None
    if no unique solution (inconsistent or underdetermined)."""
    aug = [list(r)+[b] for r,b in zip(rows,rhs)]
    nrows = len(aug)
    pivot_cols = []
    r = 0
    for c in range(ncol):
        # find pivot in col c, row >= r
        pr = None
        for rr in range(r, nrows):
            if aug[rr][c] != 0:
                pr = rr; break
        if pr is None:
            continue
        aug[r], aug[pr] = aug[pr], aug[r]
        # normalize
        piv = aug[r][c]
        aug[r] = [x/piv for x in aug[r]]
        for rr in range(nrows):
            if rr != r and aug[rr][c] != 0:
                f = aug[rr][c]
                aug[rr] = [a-b*f for a,b in zip(aug[rr], aug[r])]
        pivot_cols.append(c)
        r += 1
        if r == nrows: break
    # check consistency: rows beyond pivot rows must have 0 = rhs
    for rr in range(r, nrows):
        if aug[rr][ncol] != 0:
            return None  # inconsistent
    # check unique: need rank == ncol
    if len(pivot_cols) != ncol:
        return None  # underdetermined (not a vertex)
    sol = [F(0)]*ncol
    for i,c in enumerate(pivot_cols):
        sol[c] = aug[i][ncol]
    return sol

# Enumerate
worst = None
minA = None
min_configs = []
violations = []
vertices_checked = 0
all_A_values = {}

for ks in distributions:
    # enumerate partitions of 7 sub-pieces into <=4 blocks
    for part in set_partitions(7, 4):
        sizes, ok = solve_vertex(ks, part)
        if not ok:
            continue
        # check nonneg
        if any(s < 0 for s in sizes.values()):
            continue
        # also require it's a genuine vertex: partition has <=4 blocks (3+ equalities)
        # (we already limit to <=4 blocks)
        pieces = [sizes[i] for i in range(7)]
        # the pieces must be a valid refinement: group sums check (automatic from solve)
        A = alt_sum(pieces)
        vertices_checked += 1
        key = tuple(sorted(pieces, reverse=True))
        all_A_values[key] = all_A_values.get(key, [])
        all_A_values[key].append((ks, part))
        if minA is None or A < minA:
            minA = A
            min_configs = [(ks, part, pieces, A)]
        elif A == minA:
            min_configs.append((ks, part, pieces, A))
        if A < TARGET:
            violations.append((ks, part, pieces, A))

print("vertices checked:", vertices_checked)
print("min A (integer scale):", minA, " = ", minA/15 if minA else None, "real scale")
print("target:", TARGET, "(=", TARGET/15, "real)")
print("VIOLATIONS (A < 1):", len(violations))
for v in violations[:20]:
    print("  VIOLATION", v)

print()
print("distinct piece-multisets at vertices:", len(all_A_values))
print("distinct A values:", sorted(set(alt_sum(list(k)) for k in all_A_values)))

print()
print("configs attaining min A:")
for c in min_configs[:30]:
    ks, part, pieces, A = c
    print(f"  ks={ks} pieces={pieces} A={A} (={A/15})")

print()
print("A-value histogram (integer scale):")
from collections import Counter
cnt = Counter()
for key in all_A_values:
    cnt[alt_sum(list(key))] += 1
for v in sorted(cnt):
    print(f"  A={v}  ({v/15} real)  count={cnt[v]}")
