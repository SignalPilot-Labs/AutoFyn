"""A3 re-check with KNOWN governing sets (period detection on short N is unreliable
for T=852; use the round-7-verified governing primes directly)."""
import math
from collections import defaultdict


def sieve_primes(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def prime_factors(x, small_primes):
    fs = set()
    y = x
    for p in small_primes:
        if p * p > y:
            break
        if y % p == 0:
            fs.add(p)
            while y % p == 0:
                y //= p
    if y > 1:
        fs.add(y)
    return fs


def prune_minimal(family):
    kept = []
    for s in sorted(family, key=len):
        if not any(t <= s for t in kept):
            kept.append(s)
    out = []
    seen = set()
    for s in kept:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def add_set_to_MT(MT, S_new):
    S_new = frozenset(S_new)
    new = []
    for T in MT:
        if T & S_new:
            new.append(T)
        else:
            for p in S_new:
                new.append(T | {p})
    return prune_minimal(new)


def mt_greedy(a1, N, sp):
    a = [0] * N
    a[0] = a1
    P0 = prime_factors(a1, sp)
    MT = prune_minimal([frozenset([p]) for p in P0])
    for step in range(1, N):
        prev = a[step - 1]
        m = prev + 1
        while True:
            Pm = prime_factors(m, sp)
            if any(t <= Pm for t in MT):
                break
            m += 1
        a[step] = m
        S_new = prime_factors(m, sp)
        MT = add_set_to_MT(MT, S_new)
    return a, MT


# a_1=375: P1={3,5}, known governing G={2,3,5,7,19} (L=3990=2*3*5*7*19)
print("A3 a_1=375, N=3000, governing G={2,3,5,7,19} (known, round-7-verified)")
sp = sieve_primes(min(375 + 3005 * 15 + 1000, 2_000_000))
a, MT = mt_greedy(375, 3000, sp)
P1 = {3, 5}
G = {2, 3, 5, 7, 19}
for r in sorted(G - P1):
    mults = 0; fails = 0
    for i in range(3000):
        if a[i] % r == 0:
            mults += 1
            k = a[i] // r
            if k % 3 != 0 and k % 5 != 0:
                fails += 1
    print(f"  r={r}: r-multiples={mults}, cofactor-fails={fails} (expect 0)")

# verify the MT stabilized to {2,3,5,7,19} and contains {3,5} as a member
mps = set()
for T in MT:
    mps |= set(T)
print(f"  final MT-prime set: {sorted(mps)} (expect [2,3,5,7,19])")
print(f"  final MT members: {sorted([sorted(t) for t in MT])}")
print(f"  {{3,5}} in MT? {frozenset([3,5]) in [frozenset(t) for t in MT]}")

# also r in P1 should FAIL (sanity)
for r in sorted(P1):
    mults = 0; fails = 0
    for i in range(3000):
        if a[i] % r == 0:
            mults += 1
            k = a[i] // r
            if k % 3 != 0 and k % 5 != 0:
                fails += 1
    print(f"  r={r} (in P1, expect fails>0): r-multiples={mults}, fails={fails}")
