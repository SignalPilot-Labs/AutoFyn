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
def greedy_with_mt(a1,N):
    a=[a1]; P0=prime_factors_set(a1); MT=prune_minimal([frozenset([p]) for p in P0])
    mt_history=[(0, sorted([sorted(t) for t in MT]))]
    mt_prime_set = set(P0)
    for step in range(1,N):
        prev=a[-1]; m=prev+1
        while True:
            Pm=prime_factors_set(m)
            if any(t<=Pm for t in MT): break
            m+=1
        a.append(m); S_new=prime_factors_set(m); MT=add_set(MT,S_new)
        cur_primes=set()
        for T in MT: cur_primes|=T
        mt_prime_set |= cur_primes
    return a, MT, mt_prime_set

# Check the FINAL MT for a_1=375 and a_1=9375 (after the sequence is well into periodicity)
for a1,N in [(375, 5000), (9375, 8000)]:
    a, MT, mps = greedy_with_mt(a1,N)
    cur_primes=set()
    for T in MT: cur_primes|=T
    print(f"a1={a1}, N={N}:")
    print(f"  MT primes (in final MT): {sorted(cur_primes)}")
    print(f"  MT primes EVER seen: {sorted(mps)}")
    print(f"  |MT| (number of minimal transversals): {len(MT)}")
    print(f"  Sample MT members: {[sorted(t) for t in MT[:8]]}")
