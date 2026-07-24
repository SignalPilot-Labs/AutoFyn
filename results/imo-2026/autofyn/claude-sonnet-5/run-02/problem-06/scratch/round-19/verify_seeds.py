import sys
from math import gcd

def build_spf(bound):
    spf = list(range(bound+1))
    i = 2
    while i*i <= bound:
        if spf[i] == i:
            for j in range(i*i, bound+1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf

def prime_factors(x, spf):
    s = set()
    while x > 1:
        p = spf[x]
        s.add(p)
        while x % p == 0:
            x //= p
    return s

def simulate(a1, n_max, spf_bound):
    spf = build_spf(spf_bound)
    a = [a1]
    used = set([a1])
    prime_bits = {}
    for p in prime_factors(a1, spf):
        prime_bits[p] = 1
    n = 1
    full_mask = 1
    while n < n_max:
        c = a[-1] + 1
        while True:
            if c in used:
                c += 1
                continue
            if c > spf_bound:
                raise RuntimeError("need bigger spf bound, c=%d" % c)
            pf = prime_factors(c, spf)
            if not pf:
                c += 1
                continue
            m = 0
            for p in pf:
                m |= prime_bits.get(p, 0)
            if m == full_mask:
                break
            c += 1
        a.append(c)
        used.add(c)
        n += 1
        full_mask = (full_mask << 1) | 1
        for p in prime_factors(c, spf):
            prime_bits[p] = prime_bits.get(p, 0) | (1 << (n - 1))
    return a

def base_type_seq(a1, n_max, spf_bound):
    spf = build_spf(spf_bound)
    a = simulate(a1, n_max, spf_bound)
    Q = prime_factors(a1, spf)
    types = []
    for x in a:
        pf = prime_factors(x, spf)
        types.append(frozenset(pf & Q))
    return types, a

if __name__ == "__main__":
    import time
    t0=time.time()
    a1 = 510510
    N = 65000
    types, a = base_type_seq(a1, N, spf_bound=6_000_000)
    print("510510 sim done in", time.time()-t0, "len", len(a), "last term", a[-1])
    from collections import defaultdict
    occ = defaultdict(list)
    for i,t in enumerate(types):
        occ[t].append(i+1)
    target1 = frozenset({2,3,5,11,13,17})
    target2 = frozenset({2,3,7,11,13,17})
    fullQ = frozenset({2,3,5,7,11,13,17})
    print("target1 occurrences (first 5):", occ.get(target1,[])[:5])
    print("target2 occurrences (first 5):", occ.get(target2,[])[:5])
    print("fullQ occurrences (first 5):", occ.get(fullQ,[])[:5])

def check_200k():
    import time
    t0=time.time()
    a1=510510
    N=200000
    types,a = base_type_seq(a1, N, spf_bound=25_000_000)
    print("510510 N=200000 sim done in", time.time()-t0, "last term", a[-1])
    from collections import defaultdict
    occ=defaultdict(list)
    for i,t in enumerate(types):
        occ[t].append(i+1)
    target1 = frozenset({2,3,5,11,13,17})
    target2 = frozenset({2,3,7,11,13,17})
    print("target1 occurrences:", occ.get(target1,[])[:10])
    print("target2 occurrences:", occ.get(target2,[])[:10])

check_200k()
