import sys, math, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors

def gov(a1, N, min_run):
    M1=rad(a1)
    a=greedy_fast(a1,N)
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
        return (a1, M1, N, None, None, None, None, "aperiodic")
    L=sum(d[0:fund])
    govset=sorted(prime_factors(L,sp))
    return (a1, M1, N, fund, L, govset, max(govset), "VIOL" if max(govset)>M1 else "ok")

specs=[]
for p in [3,5,7]:
    for q in [5,7,11,13,17,19,23,29,31]:
        if q<=p: continue
        for e in [3,4]:
            a1=p*(q**e)
            if a1>60000: continue
            specs.append((a1, 4000, 1000))
seen=set(); specs2=[]
for s in specs:
    if s[0] not in seen:
        seen.add(s[0]); specs2.append(s)
specs=specs2
print(f"running {len(specs)} cases", flush=True)
for a1,N,mr in specs:
    t0=time.time()
    r=gov(a1,N,mr)
    dt=time.time()-t0
    a1,M1,_,T,L,gs,gmax,st = r
    flag = " *** VIOLATION ***" if st=="VIOL" else ""
    print(f"a1={a1:6d} M1={M1:4d} T={str(T):>5s} L={str(L):>6s} govmax={str(gmax):>3s} {st}{flag} fac={gs} ({dt:.0f}s)", flush=True)
