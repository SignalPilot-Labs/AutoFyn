"""Correct fast gcd-greedy via minimal transversals (MT).

Admissibility: m is admissible at step n iff P(m) (its prime-factor set) is a
transversal (hitting set) of F_n = {P(a_i) : i <= n}. Equivalently, iff P(m)
CONTAINS some minimal transversal T in MT(F_n) (as a superset: T subset P(m)).

Maintain MT(F_n) incrementally: when adding S_new = P(a_new), a transversal of
F_n ∪ {S_new} must (hit S_new) AND (hit every S in F_n). So:
  new_MT = prune_minimal( {T in MT_old : T & S_new}  ∪  {T | {p} : T in MT_old, T & S_new == empty, p in S_new} )

Verified against naive O(N^2) gcd-greedy.
"""
import math
from collections import defaultdict


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


def sieve_primes(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def prune_minimal(family):
    """Keep only inclusion-minimal sets (drop any set that has a proper subset in family)."""
    fam = [frozenset(s) for s in family]
    fam.sort(key=len)  # smallest first; a set is non-minimal iff it has a proper subset already kept
    kept = []
    for s in fam:
        if not any(t < s or t == s and t is not s for t in kept) and not any(t <= s for t in kept):
            # simpler: s is minimal iff no kept t is a proper subset of s
            pass
    # cleaner implementation
    kept = []
    for s in sorted(fam, key=len):
        if not any(t <= s for t in kept):
            kept.append(s)
    # dedup
    out = []
    seen = set()
    for s in kept:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def add_set_to_MT(MT, S_new):
    """Update MT (list of frozensets) for the addition of constraint set S_new."""
    S_new = frozenset(S_new)
    new = []
    for T in MT:
        if T & S_new:
            # T already hits S_new; stays a transversal (if still minimal)
            new.append(T)
        else:
            # T must be extended by some p in S_new to hit it
            for p in S_new:
                new.append(T | {p})
    return prune_minimal(new)


def greedy_mt(a1, N, small_primes):
    a = [0] * N
    a[0] = a1
    P0 = prime_factors(a1, small_primes)
    MT = [frozenset([p]) for p in P0]  # MT({P(a_1)}) = {{p} : p in P(a_1)}
    # Actually MT({S}) for a single set S = {{p} : p in S} (minimal transversals = singletons)
    MT = prune_minimal([{p} for p in P0])
    for step in range(1, N):
        prev = a[step - 1]
        m = prev + 1
        while True:
            Pm = prime_factors(m, small_primes)
            # admissible iff some T in MT has T subset Pm
            ok = any(t <= Pm for t in MT)
            if ok:
                break
            m += 1
        a[step] = m
        S_new = prime_factors(m, small_primes)
        MT = add_set_to_MT(MT, S_new)
    return a


def rad(a1):
    fs = set()
    x = a1
    d = 2
    while d * d <= x:
        while x % d == 0:
            fs.add(d)
            x //= d
        d += 1
    if x > 1:
        fs.add(x)
    r = 1
    for p in fs:
        r *= p
    return r


if __name__ == '__main__':
    import sys
    a1 = int(sys.argv[1]) if len(sys.argv) > 1 else 847
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 50000
    M1 = rad(a1)
    # sieve up to a1 + N*M1 + slack
    maxval = a1 + (N + 5) * M1 + 50
    small_limit = min(maxval, 5_000_000)
    sp = sieve_primes(small_limit)
    a = greedy_mt(a1, N, sp)
    d = [a[i+1]-a[i] for i in range(N-1)]
    n = len(d)
    for min_run in [300, 2000, 10000]:
        found = None
        for T in range(1, n//2):
            ok = True
            start = n - min_run
            for k in range(start, n - T):
                if d[k+T] != d[k]:
                    ok = False
                    break
            if ok:
                n0 = n - min_run
                while n0 > 0 and all(d[n0-1+j+T]==d[n0-1+j] for j in range(min(min_run, n-n0-T+1))):
                    n0 -= 1
                found = (T, n0)
                break
        T, n0 = found if found else (None, None)
        L = sum(d[n0:n0+T]) if T else None
        print(f"  min_run={min_run}: T={T}, n0={n0}, L={L}")
    for candT in [297, 594, 891, 1188, 1485, 1744, 1782, 2087, 2376, 2673]:
        run = 0
        k = n - 1 - candT
        while k >= 0 and d[k+candT]==d[k]:
            run += 1
            k -= 1
        print(f"  candidate T={candT}: longest suffix run = {run}")
