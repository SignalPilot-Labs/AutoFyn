"""
Brute-force verification for IMO Problem 3 (Liu Bang / Xiang Yu stick game).

Claimed answer:  c(n) = 2^n / (2^{n+1} - 1),
achieved by Liu Bang cutting the stick into pieces proportional to 2^n, ..., 2, 1.

Model checked here (an exact reduction proved in solution.md):
  - After all cuts, optimal alternate claiming gives Liu Bang exactly the
    "odd-index sum" O(Q) = q1 + q3 + q5 + ...  of the sorted parts (Lemma 1).
  - So the game value is  max_{A partitions} min_{B refinements with <= n cuts} O(Q).

This script discretizes lengths to an integer grid (Liu Bang's pieces on a
coarser sub-grid so Xiang Yu's integer cuts retain full power for the relevant
halving / difference strategies) and computes the exact max-min on that grid.

Expected results:
  n=1, L=12  :  max-min =  8  (= 2/3 * 12),  unique optimum (8,4)      ~ (2,1)
  n=2, L=140 :  max-min = 80  (= 4/7 * 140), unique optimum (80,40,20) ~ (4,2,1)
  n=3, L=120 :  geometric A=(64,32,16,8) gives min = 64 (= 8/15 * 120),
                and a coarse full scan over A finds nothing better.
"""
import time

def oddsum(parts):
    ps = sorted(parts, reverse=True)
    return sum(ps[0::2])

def minB(pieces, cuts):
    """Min over Xiang Yu's <= `cuts` integer-position cuts of the odd-index sum."""
    start = tuple(sorted(pieces, reverse=True))
    memo = {}
    def rec(state, k):
        key = (state, k)
        if key in memo:
            return memo[key]
        best = oddsum(state)
        if k > 0:
            lst = list(state)
            seen_vals = set()
            for idx, v in enumerate(lst):
                if v in seen_vals or v < 2:
                    continue
                seen_vals.add(v)
                rest = lst[:idx] + lst[idx + 1:]
                for i in range(1, v // 2 + 1):
                    child = tuple(sorted(rest + [i, v - i], reverse=True))
                    r = rec(child, k - 1)
                    if r < best:
                        best = r
        memo[key] = best
        return best
    return rec(start, cuts)

def partitions(total, parts, mult, maxv=None):
    """All nonincreasing tuples of `parts` positive multiples of `mult` summing to `total`."""
    if maxv is None:
        maxv = total
    if parts == 1:
        if 0 < total <= maxv and total % mult == 0:
            yield (total,)
        return
    v = min(maxv, total - mult * (parts - 1))
    v -= v % mult
    while v >= mult and v * parts >= total:
        for rest in partitions(total - v, parts - 1, mult, v):
            yield (v,) + rest
        v -= mult

def scan(n, L, mult):
    best = (-1, None)
    for A in partitions(L, n + 1, mult):
        val = minB(A, n)
        if val > best[0]:
            best = (val, [A])
        elif val == best[0]:
            best[1].append(A)
    return best

if __name__ == "__main__":
    t0 = time.time()

    t = time.time()
    v, arg = scan(1, 12, 2)
    print(f"n=1, L=12  : max-min = {v}/12   at {arg}   expected 8/12  = 2/3    "
          f"[{time.time()-t:.1f}s]")
    assert v == 8 and arg == [(8, 4)]

    t = time.time()
    v, arg = scan(2, 140, 4)
    print(f"n=2, L=140 : max-min = {v}/140  at {arg}   expected 80/140 = 4/7   "
          f"[{time.time()-t:.1f}s]")
    assert v == 80 and arg == [(80, 40, 20)]

    t = time.time()
    v = minB((64, 32, 16, 8), 3)
    print(f"n=3, L=120 : geometric A=(64,32,16,8) -> min = {v}/120  "
          f"expected 64/120 = 8/15   [{time.time()-t:.1f}s]")
    assert v == 64

    t = time.time()
    v, arg = scan(3, 120, 8)
    print(f"n=3, L=120 : coarse full scan -> max-min = {v}/120  at {arg}   "
          f"[{time.time()-t:.1f}s]")
    assert v == 64 and arg == [(64, 32, 16, 8)]

    print(f"\nAll checks passed. Total verification runtime: {time.time()-t0:.1f}s")
