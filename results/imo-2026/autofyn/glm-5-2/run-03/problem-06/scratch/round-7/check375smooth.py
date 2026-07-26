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
    return a

# For a_1=375: is every term {2,3,5,7,19}-smooth? List all distinct prime factors across the period.
a1=375; N=2000
a=greedy(a1,N)
allprimes=set()
for x in a:
    allprimes |= prime_factors_set(x)
print(f"a1=375: distinct primes appearing in first {N} terms: {sorted(allprimes)}")
print(f"  Governing set {{2,3,5,7,19}}; transients present: {sorted(allprimes - {2,3,5,7,19})}")
# count terms with a prime outside governing set
gov={2,3,5,7,19}
viol=0
for x in a:
    if prime_factors_set(x) - gov:
        viol+=1
print(f"  Terms with a prime outside governing set: {viol}/{N}")

# Same for a_1=9375
a1=9375; N=4000
a=greedy(a1,N)
allprimes=set()
for x in a: allprimes |= prime_factors_set(x)
print(f"\na1=9375: distinct primes in first {N} terms: {len(allprimes)}")
gov67={2,3,5,7,67}
print(f"  Governing set {{2,3,5,7,67}}; transients present: {len(allprimes - gov67)} distinct primes")
viol=0
for x in a:
    if prime_factors_set(x) - gov67: viol+=1
print(f"  Terms with a prime outside governing set: {viol}/{N} ({100*viol/N:.1f}%)")
