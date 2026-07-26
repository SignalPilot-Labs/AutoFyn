"""
Vertex-certificate check for L(3) over reals.

Liu level-3 dyadic: marks at 1/15, 3/15, 7/15 -> pieces (1,2,4,8)/15.
Xiang places 3 real marks x1,x2,x3 in [0,1].
A = sum_{i} (-1)^{i+1} p_i  where p_1>=p_2>=... are the final pieces sorted descending.

Claim: A >= 1/15 for ALL real x in [0,1]^3 (with marks allowed to coincide for the
continuous extension).

We prove A is continuous + piecewise-linear on [0,1]^3 with arrangement
  H = {x_i = Liu mark} U {x_i = x_j} U {x_i = 0, x_i = 1}
and ALL arrangement vertices are grid points
  (a,b,c) with a,b,c in {0, 1/15, 3/15, 7/15, 1}.
Check A >= 1/15 at all 5^3 = 125 grid points (exact rational).
"""
from fractions import Fraction as F
from itertools import product

# Liu marks and boundary/grid values
LIU = [F(1,15), F(3,15), F(7,15)]
GRID = [F(0), F(1,15), F(3,15), F(7,15), F(1)]  # the 5 arrangement values per coord

ALPHA3 = F(1,15)

def A_value(xiang):
    """Continuous extension of A at a (possibly degenerate) mark-vector.
    Build cut-point multiset = {0,1} U Liu marks U Xiang marks, take DISTINCT
    sorted values, pieces = consecutive differences, sort descending, alt sum.
    This is the continuous extension (vanishing pieces contribute 0)."""
    cuts = set([F(0), F(1)] + list(LIU) + list(xiang))
    s = sorted(cuts)
    pieces = [s[i+1]-s[i] for i in range(len(s)-1)]
    pieces.sort(reverse=True)
    M = len(pieces)
    A = F(0)
    for i,p in enumerate(pieces):
        sign = 1 if (i % 2 == 0) else -1   # p_1 (i=0) -> +1
        A += sign * p
    return A, M, pieces

# Enumerate all 125 grid vertices
worst = None
violations = []
minA = None
min_pts = []
table = []
for (a,b,c) in product(GRID, repeat=3):
    A,M,pieces = A_value((a,b,c))
    table.append(( (a,b,c), A, M, pieces ))
    if minA is None or A < minA:
        minA = A
        min_pts = [(a,b,c)]
    elif A == minA:
        min_pts.append((a,b,c))
    if A < ALPHA3 - F(0):  # strict <
        violations.append(((a,b,c), A))

print("Total grid vertices:", len(table))
print("alpha(3) =", ALPHA3)
print("min A over grid vertices =", minA)
print("number attaining min:", len(min_pts))
print("VIOLATIONS (A < 1/15):", len(violations))
for v in violations[:10]:
    print("  ", v)

print()
print("Sample of attaining-min vertices (first 15):")
for p in min_pts[:15]:
    A,M,pieces = A_value(p)
    print(f"  {p}  A={A}  M={M}  pieces={[str(x) for x in pieces]}")

print()
print("Distinct A-values at grid vertices:")
distinct = sorted(set(t[1] for t in table))
for v in distinct:
    cnt = sum(1 for t in table if t[1]==v)
    print(f"  A={v}  count={cnt}")
