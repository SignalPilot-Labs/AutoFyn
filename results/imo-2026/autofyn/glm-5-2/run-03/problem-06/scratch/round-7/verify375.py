import sys, math, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors

def naive_greedy(a1, N):
    a=[a1]
    for _ in range(N-1):
        prev=a[-1]; m=prev+1
        while True:
            if all(math.gcd(m,x)>1 for x in a):
                break
            m+=1
        a.append(m)
    return a

a1=375
N=400
f=greedy_fast(a1,N)
n=naive_greedy(a1,N)
print("fast==naive (first 400 terms):", f==n)
if f!=n:
    for i,(x,y) in enumerate(zip(f,n)):
        if x!=y:
            print(f"  diff idx {i}: fast={x} naive={y}"); break

# Now deep run + independent period check
N2=20000
t0=time.time()
a=greedy_fast(a1,N2)
print(f"deep run N={N2} time={time.time()-t0:.1f}s", flush=True)
d=[a[i+1]-a[i] for i in range(N2-1)]
# check period T=852 over the whole array
T=852
viol_count=sum(1 for k in range(0, N2-1-T) if d[k+T]!=d[k])
print(f"T=852 violations over [0,{N2-1-T}]: {viol_count}")
# find true n0
n0=0
while n0 < N2-1-T and d[n0+T]==d[n0]:
    n0+=1
# actually find earliest start of periodic tail
n0start = 0
# scan: find smallest n0 such that d[n0..] is T-periodic
import sys
def tail_periodic_start(d, T):
    n=len(d)
    # binary search the smallest n0 with d[k]==d[k+T] for all k in [n0, n-1-T]
    lo, hi = 0, n-1-T
    # linear from 0
    n0=0
    while n0 <= n-1-T and d[n0+T]==d[n0]:
        n0+=1
    # n0 is first index where it FAILS; so tail starts at n0 (fails at n0 means d[n0]!=d[n0+T])
    # wait: if d[n0+T]==d[n0] we advance; so the periodic tail starts at the first n0 where it BEGAN holding forever
    # but a single failure could be transient. Better: find largest n0 such that [n0, n-1] is T-periodic
    # = smallest index from which no violation
    last_fail=-1
    for k in range(n-1-T, -1, -1):
        if d[k+T]!=d[k]:
            last_fail=k
            break
    return last_fail+1
s=tail_periodic_start(d,T)
tail_len = (N2-1)-s
print(f"T=852 periodic tail starts at n0={s}, tail length={tail_len}, tail_len/2T={tail_len/(2*T):.2f}")
L=sum(d[s:s+T])
print(f"L = {L}, factors={sorted(prime_factors(L, sieve_primes(200000)))}")
print(f"M1=rad({a1})={rad(a1)}, gov_max={max(prime_factors(L, sieve_primes(200000)))}")
