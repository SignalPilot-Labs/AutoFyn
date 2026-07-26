import sys, math, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors

def gov(a1, N, min_run):
    M1=rad(a1)
    t0=time.time()
    a=greedy_fast(a1,N); dt=time.time()-t0
    d=[a[i+1]-a[i] for i in range(N-1)]
    sp=sieve_primes(min(a1+(N+5)*M1+20, 2_000_000))
    fund=None
    for T in range(1, N//2):
        need=max(min_run,2*T)
        if N-1-need < 0: break
        if all(d[k+T]==d[k] for k in range(N-1-need, N-1-T)):
            if all(d[k+T]==d[k] for k in range(0, N-1-T)):
                fund=T; break
    if fund is None:
        return (a1,M1,N,None,None,None,None,"aperiodic",dt)
    L=sum(d[0:fund]); gs=sorted(prime_factors(L,sp))
    return (a1,M1,N,fund,L,gs,max(gs),"VIOL" if max(gs)>M1 else "ok",dt)

# Siblings of 375 = 3·5^3; close-prime NON-LOCK small-M1
specs=[
    (9375, 15000, 4000),   # 3·5^5, M1=15 -- deep
    (375, 20000, 4000),    # re-confirm
    (875, 4000, 1000),     # 5^3·7, M1=35
    (1375, 4000, 1000),    # 5^3·11, M1=55
    (1625, 4000, 1000),    # 5^3·13, M1=65
    (686, 4000, 1000),     # 2·7^3, M1=14 (even, |P1|=2 -> LOCK?)
    (1925, 4000, 1000),    # 5^2·7·11, M1=77
    (625, 2000, 500),      # 5^4, single prime LOCK
]
for a1,N,mr in specs:
    r=gov(a1,N,mr)
    a1,M1,_,T,L,gs,gmax,st,dt=r
    flag=" *** VIOL ***" if st=="VIOL" else ""
    print(f"a1={a1:6d} M1={M1:4d} N={N:5d} T={str(T):>5s} L={str(L):>6s} govmax={str(gmax):>3s} {st}{flag} fac={gs} ({dt:.0f}s)",flush=True)
