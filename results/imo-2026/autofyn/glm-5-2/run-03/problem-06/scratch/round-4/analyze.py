from math import gcd, prod
from collections import defaultdict

def greedy(a1, N):
    a = [a1]
    for _ in range(N-1):
        cur = a[-1]
        m = cur + 1
        while True:
            if all(gcd(m, x) > 1 for x in a):
                a.append(m)
                break
            m += 1
    return a

def diffs(a): return [a[i+1]-a[i] for i in range(len(a)-1)]

def window_determinism(d, Wmax=12):
    """For each W, check if (d[n-W+1..n]) -> d[n+1] is a function in the tail.
    Return minimal W (if any <= Wmax) such that no two equal windows have different next values."""
    n = len(d)
    for W in range(1, Wmax+1):
        seen = {}
        conflict = False
        for i in range(W, n-1):
            key = tuple(d[i-W:i])
            if key in seen and seen[key] != d[i]:
                conflict = True
                break
            seen[key] = d[i]
        if not conflict:
            return W, len(seen)
    return None, None

for a1 in [15, 35, 77, 91, 143, 65, 221]:
    N = 6000
    a = greedy(a1, N)
    d = diffs(a)
    print(f"=== a1={a1} ===")
    print("d[0:60]:", d[:60])
    W, nstates = window_determinism(d)
    print(f"minimal window W={W}, #distinct windows={nstates}")
    # also: distinct values of d
    print("distinct increments:", sorted(set(d)))
    # period
    for T in range(1, 200):
        ok = all(d[-200+k+T]==d[-200+k] for k in range(150))
        if ok:
            print(f"period T={T}, L={sum(d[-T:])}")
            break
    print()
