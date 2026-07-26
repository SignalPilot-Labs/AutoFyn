import sys, math, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors
def naive_greedy(a1, N):
    a=[a1]
    for _ in range(N-1):
        prev=a[-1]; m=prev+1
        while True:
            if all(math.gcd(m,x)>1 for x in a): break
            m+=1
        a.append(m)
    return a
a1=9375
f=greedy_fast(a1,200); n=naive_greedy(a1,200)
print("9375 fast==naive (200 terms):", f==n)
if f!=n:
    for i,(x,y) in enumerate(zip(f,n)):
        if x!=y: print(f"  diff idx {i}: fast={x} naive={y}"); break
# deeper confirm with larger N
N=22000
t0=time.time(); a=greedy_fast(a1,N); print(f"N={N} time={time.time()-t0:.1f}s",flush=True)
d=[a[i+1]-a[i] for i in range(N-1)]
T=3108
viol=sum(1 for k in range(0,N-1-T) if d[k+T]!=d[k])
print(f"T=3108 violations over [0,{N-1-T}]: {viol}")
# fundamental check
fund=None
for Tc in range(1,N//2):
    if all(d[k+Tc]==d[k] for k in range(0,N-1-Tc)):
        fund=Tc; break
print(f"fundamental period = {fund}")
L=sum(d[0:fund]); sp=sieve_primes(200000)
print(f"L={L} fac={sorted(prime_factors(L,sp))} govmax={max(prime_factors(L,sp))} M1={rad(a1)}")
