import sys, math, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors
def gov(a1, N, min_run):
    M1=rad(a1); t0=time.time()
    a=greedy_fast(a1,N); dt=time.time()-t0
    d=[a[i+1]-a[i] for i in range(N-1)]
    sp=sieve_primes(min(a1+(N+5)*M1+20, 2_000_000))
    fund=None
    for T in range(1, N//2):
        need=max(min_run,2*T)
        if N-1-need<0: break
        if all(d[k+T]==d[k] for k in range(N-1-need,N-1-T)):
            if all(d[k+T]==d[k] for k in range(0,N-1-T)):
                fund=T; break
    if fund is None: return (a1,M1,N,None,None,None,None,"aperiodic",dt)
    L=sum(d[0:fund]); gs=sorted(prime_factors(L,sp))
    return (a1,M1,N,fund,L,gs,max(gs),"VIOL" if max(gs)>M1 else "ok",dt)
specs=[
    (750, 6000, 1500),     # 2·3·5^3, M1=30
    (3750, 6000, 1500),    # 2·3·5^4, M1=30
    (18750, 6000, 1500),   # 2·3·5^5, M1=30
    (2625, 6000, 1500),    # 3·5^3·7, M1=105
    (1275, 6000, 1500),    # 3·5^2·17, M1=255
    (1125, 6000, 1500),    # 3^2·5^3, M1=15
    (6375, 6000, 1500),    # 3·5^3·17, M1=255
    (11250, 5000, 1200),   # 2·3^2·5^4, M1=30
]
for a1,N,mr in specs:
    r=gov(a1,N,mr); a1,M1,_,T,L,gs,gmax,st,dt=r
    flag=" *** VIOL ***" if st=="VIOL" else ""
    print(f"a1={a1:6d} M1={M1:4d} N={N:5d} T={str(T):>5s} L={str(L):>6s} govmax={str(gmax):>3s} {st}{flag} fac={gs} ({dt:.0f}s)",flush=True)
