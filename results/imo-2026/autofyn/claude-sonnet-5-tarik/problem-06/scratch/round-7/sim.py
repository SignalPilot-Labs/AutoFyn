import sys
from sympy import primerange, factorint

def simulate(a1, n_terms, report_every=None):
    """Generate a1..a_{n_terms} via the greedy admissibility rule.
    Returns list a[1..n_terms] (1-indexed via a[0] unused)."""
    a = [None, a1]
    prime_mask = {}  # prime -> bitmask over indices (bit i-1 <-> index i)
    fac1 = factorint(a1)
    for p in fac1:
        prime_mask[p] = 1  # bit 0 set (index 1)
    full_mask = 1  # after 1 term
    n = 1
    cur = a1
    while n < n_terms:
        cand = cur + 1
        while True:
            f = factorint(cand)
            primes = list(f.keys())
            m = 0
            for p in primes:
                m |= prime_mask.get(p, 0)
            if m == full_mask:
                # admissible
                break
            cand += 1
        n += 1
        a.append(cand)
        cur = cand
        newbit = 1 << (n - 1)
        for p in factorint(cand):
            prime_mask[p] = prime_mask.get(p, 0) | newbit
        full_mask |= newbit
        if report_every and n % report_every == 0:
            print(f"  ...n={n}, a_n={cur}", file=sys.stderr)
    return a

def rad(x):
    return frozenset(factorint(x).keys())

if __name__ == "__main__":
    import json
    a1 = int(sys.argv[1])
    n_terms = int(sys.argv[2])
    out = sys.argv[3] if len(sys.argv) > 3 else None
    a = simulate(a1, n_terms, report_every=500)
    if out:
        with open(out, "w") as f:
            json.dump(a[1:], f)
    else:
        print(a[1:20])
