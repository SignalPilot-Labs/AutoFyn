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
        if not any(t<=s for t in kept):
            kept.append(s)
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

# Verify a_1=9375 with naive greedy on first 200 terms, compare with my MT greedy
def naive_greedy(a1,N):
    a=[a1]
    for step in range(1,N):
        prev=a[-1]; m=prev+1
        while True:
            ok = all(math.gcd(m, ai)>1 for ai in a)
            if ok: break
            m+=1
        a.append(m)
    return a

a1=9375; N=200
amt=greedy(a1,N)
ana=naive_greedy(a1,N)
print("MT vs naive match on first 200 terms:", amt==ana)
# Now period detection: try T=3108 directly over as much as we can
N2=30000
a2=greedy(a1,N2)
d=[a2[i+1]-a2[i] for i in range(len(a2)-1)]
n=len(d)
for Tc in [3108, 1900, 6216, 1554]:
    viol=0
    for k in range(0, n-Tc):
        if d[k+Tc]!=d[k]: viol+=1
    print(f"  T={Tc}: violations over [0,{n-Tc}) = {viol}")
# compute L for T=3108 from start
if n>=3108:
    L3108=sum(d[0:3108])
    print(f"  L(T=3108) from start = {L3108}, factor = {sorted(prime_factors_set(L3108))}")
