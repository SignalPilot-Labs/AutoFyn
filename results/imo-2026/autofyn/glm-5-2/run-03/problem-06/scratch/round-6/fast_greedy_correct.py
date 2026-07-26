"""Correct fast gcd-greedy for IMO 2026 P6.

Verified against the naive O(N^2) greedy on a_1 in {15, 385} for N up to 4000.

Idea: a_{n+1}=m is admissible iff for every i<=n, gcd(m, a_i) > 1.
Maintain prime -> sorted list of indices i (1-based) with p | a_i.
For candidate m, factor m, then for each prime p | m mark all indices in
indices(p) as covered; m admissible iff coverage == n.
To keep coverage-check fast, maintain a count of covered indices and a
'covered' bytearray reset incrementally (only the indices we touched).
"""
import math


def prime_factors(x, small_primes):
    fs = set()
    for p in small_primes:
        if p * p > x:
            break
        if x % p == 0:
            fs.add(p)
            while x % p == 0:
                x //= p
    if x > 1:
        fs.add(x)
    return fs


def sieve_primes(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def greedy_fast(a1, N):
    # bound on primes we need to factor: terms grow like a1 + N*M1, so prime factors
    # up to ~ a1 + N*M1. Precompute sieve up to that.
    M1 = rad(a1)
    maxval = a1 + (N + 5) * M1 + 10
    # cap sieve to something reasonable; for very large N we still need primes up to maxval
    # but maxval could be huge. Use trial division by small primes + Miller for leftovers.
    small_limit = min(maxval, 2_000_000)
    sp = sieve_primes(small_limit)
    a = [0] * N
    a[0] = a1
    # prime -> list of indices (0-based here, representing term index)
    from collections import defaultdict
    prime_idx = defaultdict(list)
    a0_primes = prime_factors(a1, sp)
    for p in a0_primes:
        prime_idx[p].append(0)
    covered = bytearray(N)
    touched = []
    for step in range(1, N):
        prev = a[step - 1]
        m = prev + 1
        while True:
            mf = prime_factors(m, sp)
            # reset touched
            for idx in touched:
                covered[idx] = 0
            touched = []
            cnt = 0
            ok = True
            for p in mf:
                lst = prime_idx.get(p)
                if lst:
                    for idx in lst:
                        if covered[idx] == 0:
                            covered[idx] = 1
                            touched.append(idx)
                            cnt += 1
            if cnt == step:
                # all prior terms covered
                ok = True
                break
            else:
                m += 1
        a[step] = m
        mf = prime_factors(m, sp)
        for p in mf:
            prime_idx[p].append(step)
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
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
    a = greedy_fast(a1, N)
    d = [a[i + 1] - a[i] for i in range(N - 1)]
    # detect period
    n = len(d)
    min_run = min(300, n // 4)
    found = None
    for T in range(1, n // 2):
        ok = True
        start = n - min_run
        for k in range(start, n - T):
            if d[k + T] != d[k]:
                ok = False
                break
        if ok:
            n0 = n - min_run
            while n0 > 0 and all(d[n0 - 1 + j + T] == d[n0 - 1 + j] for j in range(min(min_run, n - n0 - T + 1))):
                n0 -= 1
            found = (T, n0)
            break
    T, n0 = found if found else (None, None)
    M1 = rad(a1)
    L = sum(d[n0:n0 + T]) if T else None
    print(f"a1={a1}  M1={M1}  N={N}  T={T}  n0={n0}  L={L}")
