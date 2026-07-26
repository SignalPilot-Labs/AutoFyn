import math
def prime_factors_set(x):
    fs=set(); y=x; d=2
    while d*d<=y:
        if y%d==0:
            fs.add(d)
            while y%d==0: y//=d
        d+=1
    if y>1: fs.add(y)
    return fs
def rad(a1):
    r=1;x=a1;d=2
    while d*d<=x:
        if x%d==0:
            r*=d
            while x%d==0: x//=d
        d+=1
    if x>1: r*=x
    return r
def prune_minimal(family):
    kept=[]
    for s in sorted(family,key=len):
        if not any(t<=s for t in kept): kept.append(s)
    out=[]; seen=set()
    for s in kept:
        if s not in seen: seen.add(s); out.append(s)
    return out
def add_set(MT,S_new):
    S_new=frozenset(S_new); new=[]
    for T in MT:
        if T & S_new: new.append(T)
        else:
            for p in S_new: new.append(T|{p})
    return prune_minimal(new)
def greedy(a1,N):
    a=[a1]; P0=prime_factors_set(a1); MT=prune_minimal([frozenset([p]) for p in P0])
    for step in range(1,N):
        prev=a[-1]; m=prev+1
        while True:
            Pm=prime_factors_set(m)
            if any(t<=Pm for t in MT): break
            m+=1
        a.append(m); S_new=prime_factors_set(m); MT=add_set(MT,S_new)
    return a,MT

# e=7: a_1 = 3*5^7 = 234375. Check period and governing set if feasible (limit N for time)
a1 = 3 * 5**7  # = 234375
N = 20000
a,MT = greedy(a1,N)
d=[a[i+1]-a[i] for i in range(len(a)-1)]
n=len(d)
# search for period: smallest T with d[k]==d[k+T] for all k in [0, n-T-1]
# (periodic from n_0=0 hypothesis)
found=None
for T in range(1, min(n//2, 20000)):
    ok=True
    for k in range(0, n-T, 200):  # sparse check first
        if d[k+T]!=d[k]:
            ok=False; break
    if ok:
        # dense verify
        ok2=True
        for k in range(0, n-T):
            if d[k+T]!=d[k]:
                ok2=False; break
        if ok2:
            found=T; break
if found:
    L=sum(d[0:found])
    print(f"a1={a1} (3*5^7): T={found}, L={L}, factor(L)={sorted(prime_factors_set(L))}")
else:
    print(f"a1={a1}: no period found in N={N} (sparse+dense search to T<{n//2})")
    # report candidate T with longest suffix run
    best=(0,0)
    for T in range(1, min(n//2, 20000)):
        run=0; k=n-1-T
        while k>=0 and d[k+T]==d[k]:
            run+=1; k-=1
        if run>best[0]: best=(run,T)
    print(f"  best suffix-run: {best[0]} at T={best[1]}")
cur=set()
for T in MT: cur|=T
print(f"  final MT primes (N={N}): {sorted(cur)}")
