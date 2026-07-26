import sys, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors

def detect_period(d, min_run):
    """Find smallest T with a T-periodic tail of length >= max(min_run, 2T).
    Returns (T, n0) where d[n0..n-1] is T-periodic, or (None,None)."""
    n = len(d)
    best = None
    for T in range(1, n//2 + 1):
        need = max(min_run, 2*T)
        start = n - need
        if start < 0:
            break
        # check d[k]==d[k+T] for k in [start, n-T-1]
        ok = True
        for k in range(start, n - T):
            if d[k+T] != d[k]:
                ok = False
                break
        if not ok:
            continue
        # extend n0 backward
        n0 = start
        while n0 > 0 and d[n0-1+T] == d[n0-1]:
            n0 -= 1
        # the tail length n-n0 should be >= need (confirmed) and we want smallest T
        if (n - n0) >= need:
            return T, n0
    return None, None

def run_one(a1, N, min_run):
    M1 = rad(a1)
    t0=time.time()
    a = greedy_fast(a1, N)
    dt=time.time()-t0
    sp_limit = a1 + (N+5)*M1 + 20
    sp = sieve_primes(min(sp_limit, 2_000_000))
    d = [a[i+1]-a[i] for i in range(N-1)]
    T, n0 = detect_period(d, min_run)
    if T is None:
        return dict(a1=a1, M1=M1, N=N, time=round(dt,1), T=None, n0=None, L=None,
                   gov_max=None, status="aperiodic-within-N", min_run=min_run)
    L = sum(d[n0:n0+T])
    Lprimes = prime_factors(L, sp)
    gov_max = max(Lprimes) if Lprimes else 1
    viol = gov_max > M1
    return dict(a1=a1, M1=M1, N=N, time=round(dt,1), T=T, n0=n0, L=L,
               gov_max=gov_max, Lfac=sorted(Lprimes), status=("VIOLATION" if viol else "ok"), min_run=min_run)

if __name__ == '__main__':
    a1 = int(sys.argv[1]); N = int(sys.argv[2]); min_run = int(sys.argv[3]) if len(sys.argv)>3 else 500
    print(run_one(a1, N, min_run))
