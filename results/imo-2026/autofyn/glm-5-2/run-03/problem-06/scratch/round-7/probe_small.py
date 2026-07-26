"""Probe |P_1|=2 governing-set structure - small/batch."""
import sys, json
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import greedy_mt, rad, sieve_primes, prime_factors

def factorize(x):
    fs = {}
    d = 2
    y = x
    while d*d <= y:
        while y % d == 0:
            fs[d] = fs.get(d,0)+1
            y //= d
        d += 1
    if y > 1:
        fs[y] = fs.get(y,0)+1
    return fs

def run(a1, N):
    M1 = rad(a1)
    maxval = a1 + (N+5)*M1 + 50
    small_limit = min(maxval, 3_000_000)
    sp = sieve_primes(small_limit)
    a = greedy_mt(a1, N, sp)
    d = [a[i+1]-a[i] for i in range(N-1)]
    n = len(d)
    found = None
    for min_run in [200, 600, 1500]:
        if min_run > n-2: continue
        for T in range(1, n//2):
            ok = True
            start = n - min_run
            for k in range(start, n-T):
                if d[k+T] != d[k]:
                    ok = False; break
            if ok:
                n0 = n - min_run
                while n0 > 0 and all(d[n0-1+j+T]==d[n0-1+j] for j in range(min(min_run, n-n0-T+1))):
                    n0 -= 1
                found = (T, n0)
                break
        if found: break
    if not found:
        return None
    T, n0 = found
    L = sum(d[n0:n0+T])
    Lprimes = sorted(factorize(L).keys())
    return dict(a1=a1, fac=factorize(a1), M1=M1, T=T, n0=n0, L=L, Lprimes=Lprimes,
                maxgov=max(Lprimes) if Lprimes else None,
                gov_above_M1=[p for p in Lprimes if p > M1])

import sys
a1 = int(sys.argv[1])
N = int(sys.argv[2]) if len(sys.argv)>2 else 1500
r = run(a1, N)
if r is None:
    print(f"{a1}: NO PERIOD at N={N}")
else:
    print(json.dumps(r))
