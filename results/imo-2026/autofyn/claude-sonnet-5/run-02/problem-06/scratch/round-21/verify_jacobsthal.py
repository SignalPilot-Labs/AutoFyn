import sympy
from sympy import gcd, factorint

def omega(n):
    return len(factorint(n))

def jacobsthal_g_bruteforce(M, search_range=200000):
    # find max gap between consecutive integers coprime to M (i.e. g(M))
    # search over a window; M could be huge, so instead compute via CRT residues mod rad(M) if small enough
    rad = 1
    for p in factorint(M):
        rad *= p
    if rad > 20_000_000:
        return None  # too big to brute force
    coprimes = [x for x in range(1, rad+1) if gcd(x, rad) == 1]
    if not coprimes:
        return None
    maxgap = 0
    for i in range(len(coprimes)):
        nxt = coprimes[(i+1) % len(coprimes)]
        cur = coprimes[i]
        gap = (nxt - cur) if nxt > cur else (nxt + rad - cur)
        maxgap = max(maxgap, gap)
    return maxgap

# Test various composite M, check g(M) <= 2^omega(M)
import random
tests = [6, 30, 210, 2310, 30030, 510510, 10010, 9699690]
for M in tests:
    w = omega(M)
    g = jacobsthal_g_bruteforce(M)
    print(f"M={M} omega={w} g(M)={g} 2^omega={2**w} holds={g is not None and g<=2**w}")

# random composite numbers with many small prime factors up to omega ~7-8
primes = [2,3,5,7,11,13,17,19,23]
import itertools
for r in range(1,8):
    M = 1
    for p in primes[:r]:
        M*=p
    w = omega(M)
    g = jacobsthal_g_bruteforce(M)
    print(f"primorial r={r} M={M} omega={w} g={g} 2^omega={2**w} holds={g<=2**w}")
