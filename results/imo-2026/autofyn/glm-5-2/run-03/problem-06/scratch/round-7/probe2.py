"""Robust period detection for |P_1|=2 cases."""
import sys, json
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import greedy_mt, rad, sieve_primes

def factorize(x):
    fs = {}
    d = 2; y = x
    while d*d <= y:
        while y % d == 0:
            fs[d] = fs.get(d,0)+1; y //= d
        d += 1
    if y > 1: fs[y] = fs.get(y,0)+1
    return fs

def run(a1, N):
    M1 = rad(a1)
    maxval = a1 + (N+5)*M1 + 50
    small_limit = min(maxval, 4_000_000)
    sp = sieve_primes(small_limit)
    a = greedy_mt(a1, N, sp)
    d = [a[i+1]-a[i] for i in range(N-1)]
    n = len(d)
    found = None
    for T in range(1, n//3):
        need = 3*T
        if n - need < 0: break
        ok = True
        for k in range(n - need, n - T):
            if d[k+T] != d[k]:
                ok = False; break
        if ok:
            n0 = n - need
            while n0 > 0 and d[n0-1+T] == d[n0-1]:
                n0 -= 1
            L = sum(d[n0:n0+T])
            Lprimes = sorted(factorize(L).keys())
            return dict(a1=a1, fac=factorize(a1), M1=M1, T=T, n0=n0, L=L,
                        Lprimes=Lprimes, maxgov=max(Lprimes),
                        gov_above_M1=[p for p in Lprimes if p > M1])
    return None

a1 = int(sys.argv[1])
N = int(sys.argv[2]) if len(sys.argv)>2 else 3000
r = run(a1, N)
print(json.dumps(r) if r else f"{a1}: NO PERIOD at N={N}")
