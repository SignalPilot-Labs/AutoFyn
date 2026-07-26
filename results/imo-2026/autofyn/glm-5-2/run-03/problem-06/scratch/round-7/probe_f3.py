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

sp=sieve_primes(5_000_000)
# Prime power families: a1 = p^e, small radical = p
print("=== a1 = p^e (single-prime radical) ===")
rows=[]
for p in [2,3,5,7]:
    for e in [1,2,3,4,5]:
        a1=p**e
        # LOCK case: T=1,L=p expected
        N = 60 if p**e < 1000 else 4000
        a=greedy(a1,N,sp)
        d=[a[i+1]-a[i] for i in range(N-1)]
        T=min_period(d)
        L=sum(d[len(d)-T:len(d)]) if T else None
        rows.append((a1,p,e,T,L))
        print(f"  a1={a1}=p^{e} p={p}: T={T} L={L} rad={rad(a1)}")
print()
print("=== a1 = p*q products (two-prime radical), small ===")
for p,q in [(2,3),(2,5),(2,7),(2,11),(3,5),(3,7),(5,7),(2,13),(3,11)]:
    a1=p*q
    N=400
    a=greedy(a1,N,sp)
    d=[a[i+1]-a[i] for i in range(N-1)]
    T=min_period(d); L=sum(d[len(d)-T:len(d)]) if T else None
    print(f"  a1={a1}=p*q ({p}*{q}): T={T} L={L} rad={a1} M1={a1}")
print()
print("=== a1 = p^e * q (radical pq), e varies — the killer family ===")
for p,e,q in [(2,2,3),(2,3,3),(2,2,5),(2,3,5),(3,2,5),(5,2,7),(7,2,11),(2,2,7),(2,3,7)]:
    a1=p**e*q
    N=2000 if a1<2000 else 20000
    a=greedy(a1,N,sp)
    d=[a[i+1]-a[i] for i in range(N-1)]
    T=min_period(d); L=sum(d[len(d)-T:len(d)]) if T else None
    M1=rad(a1)
    print(f"  a1={a1}=p^{e}*q ({p}^{e}*{q}): T={T} L={L} rad(M1)={M1}")
