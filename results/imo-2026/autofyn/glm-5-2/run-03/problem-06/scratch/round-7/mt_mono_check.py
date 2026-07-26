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
def trace_mt_prime_set_size(a1,N):
    """Track |union of MT primes| at each step; report growth/shrink events."""
    a=[a1]; P0=prime_factors_set(a1); MT=prune_minimal([frozenset([p]) for p in P0])
    prev_primes=set(P0)
    events_grow=[]; events_shrink=[]
    for step in range(1,N):
        prev=a[-1]; m=prev+1
        while True:
            Pm=prime_factors_set(m)
            if any(t<=Pm for t in MT): break
            m+=1
        a.append(m); S_new=prime_factors_set(m); MT=add_set(MT,S_new)
        cur=set()
        for T in MT: cur|=T
        if cur - prev_primes:
            events_grow.append((step, sorted(cur-prev_primes), len(cur)))
        if prev_primes - cur:
            events_shrink.append((step, sorted(prev_primes-cur), len(cur)))
        prev_primes = cur
    return MT, events_grow, events_shrink

# a_1=9375: count grow vs shrink events over 2000 steps
for a1,N in [(375, 3000), (9375, 3000)]:
    MT, eg, es = trace_mt_prime_set_size(a1,N)
    print(f"a1={a1}, N={N}: grow events={len(eg)}, shrink events={len(es)}")
    print(f"  first 5 grows: {eg[:5]}")
    print(f"  first 5 shrinks: {es[:5]}")
    cur=set()
    for T in MT: cur|=T
    print(f"  final MT primes: {sorted(cur)}")
