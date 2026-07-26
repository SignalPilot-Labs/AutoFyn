import sys, math
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import sieve_primes, prime_factors, rad, add_set_to_MT, prune_minimal
def track(a1,N,sp):
    a=[0]*N; a[0]=a1
    P0=prime_factors(a1,sp); MT=prune_minimal([{p} for p in P0])
    active=set(P0); dropped=set(); v=0
    for s in range(1,N):
        m=a[s-1]+1
        while True:
            Pm=prime_factors(m,sp)
            if any(t<=Pm for t in MT): break
            m+=1
        a[s]=m; MT=add_set_to_MT(MT,prime_factors(m,sp))
        na=set()
        for t in MT: na|=set(t)
        for p in dropped:
            if p in na: v+=1
        dropped |= (active-na); active=na
    return v,len(dropped),sorted(active)
sp=sieve_primes(3_000_000)
cases=[(15,200),(35,400),(77,300),(91,300),(175,1500),(385,130000),(847,60000),
       (45,300),(539,1500),(175,1500),(273,4000),(605,20000),(1183,20000),(2431,30000)]
for a1,N in cases:
    v,d,act=track(a1,N,sp)
    M1=rad(a1)
    print(f"a1={a1} M1={M1}: re-entry-viols={v} dropped={d} final_active={act} all_active_le_M1={all(p<=M1 for p in act)}")
