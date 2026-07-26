import sys, math
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import sieve_primes, prime_factors, rad, add_set_to_MT, prune_minimal

def greedy(a1, N, sp):
    a=[0]*N; a[0]=a1
    P0=prime_factors(a1,sp); MT=prune_minimal([{p} for p in P0])
    for s in range(1,N):
        m=a[s-1]+1
        while True:
            Pm=prime_factors(m,sp)
            if any(t<=Pm for t in MT): break
            m+=1
        a[s]=m; MT=add_set_to_MT(MT,prime_factors(m,sp))
    return a

def min_period(d):
    n=len(d)
    for T in range(1,n//2):
        if all(d[k+T]==d[k] for k in range(n-T)): return T
    return None

sp=sieve_primes(2_000_000)
print("=== F2: minimal period of d_n vs reported T ===")
for a1,N in [(15,60),(35,200),(77,120),(91,120),(175,1200),(385,130000),(847,60000)]:
    a=greedy(a1,N,sp)
    d=[a[i+1]-a[i] for i in range(N-1)]
    T=min_period(d)
    M1=rad(a1)
    # check divisors of T as periods (is T the MINIMAL period?)
    minT=T
    for p in range(1,T+1):
        if T%p==0 and p<T:
            if all(d[k+p]==d[k] for k in range(len(d)-p)):
                if p<minT: minT=p
    L=sum(d[len(d)-T:len(d)]) if T else None
    print(f"  a1={a1} M1={M1}: reported-T={T} minimal-period-of-d={minT} L={L} T/minT={T//minT if minT else 'NA'}")
    # does d_n have ANY proper period (not necessarily |T)? check small periods
    proper=[]
    for p in range(1,min(T,40)+1):
        if p<T and all(d[k+p]==d[k] for k in range(len(d)-max(p,1))):
            proper.append(p)
    print(f"    proper periods <min(40,T): {proper}")
