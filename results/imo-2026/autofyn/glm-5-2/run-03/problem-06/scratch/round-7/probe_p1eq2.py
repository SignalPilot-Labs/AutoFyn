"""Probe |P_1|=2 governing-set structure across many a_1 (incl. refutation family)."""
import sys
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
    # find period with min_run
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
    # governing set = primes of L (per distinct-supports-stabilize under Gap A)
    # check: all a_{n0..n0+T-1} differences match a_{n0+T..n0+2T-1}
    return dict(a1=a1, fac=factorize(a1), M1=M1, T=T, n0=n0, L=L, Lprimes=Lprimes,
                maxgov=max(Lprimes) if Lprimes else None,
                gov_above_M1=[p for p in Lprimes if p > M1])

cases = [
    15, 35, 65, 77, 91, 143, 175, 847,   # known |P_1|=2 NON-LOCK
    375, 9375,                            # refutation witnesses 3*5^e, e=3,5
    # 3*5^e family odd e>=3
    3*5**7, 3*5**9,
    # p*q^e other two-prime-rad
    5*7**3, 7*11**3, 3*7**3,
    # small-rad large-value p^k (LOCK-like)
    5**3, 7**5,
    # even-e siblings
    3*5**2, 3*5**4,
]

print(f"{'a1':>8} {'fac':<14} {'M1':>5} {'N':>6} {'T':>5} {'L':>10} {'Lprimes':<25} {'gov>M1':<15} {'maxgov':>6}")
results = []
for a1 in cases:
    N = 3000 if a1 <= 2000 else 1500
    if a1 > 100000: N = 600
    try:
        r = run(a1, N)
    except Exception as e:
        print(f"{a1:>8} ERROR {e}")
        continue
    if r is None:
        print(f"{a1:>8} {str(factorize(a1)):<14} {rad(a1):>5} NO PERIOD at N={N}")
        results.append(dict(a1=a1, fac=factorize(a1), M1=rad(a1), N=N, T=None))
        continue
    print(f"{r['a1']:>8} {str(r['fac']):<14} {r['M1']:>5} {N:>6} {r['T']:>5} {r['L']:>10} {str(r['Lprimes']):<25} {str(r['gov_above_M1']):<15} {r['maxgov']:>6}")
    results.append(r)
