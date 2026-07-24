import sys, time

def factorize(m, cache={}):
    if m in cache: return cache[m]
    orig=m
    f=set()
    d=2
    while d*d<=m:
        if m%d==0:
            f.add(d)
            while m%d==0: m//=d
        d+=1 if d==2 else 2
    if m>1: f.add(m)
    cache[orig]=f
    return f

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def simulate(a1, N):
    seq=[a1]
    hist=[a1]
    for n in range(1,N):
        c=seq[-1]+1
        while True:
            ok=True
            for h in hist:
                if gcd(c,h)==1:
                    ok=False
                    break
            if ok:
                break
            c+=1
        seq.append(c)
        hist.append(c)
    return seq

def analyze(a1, S0, N=8000):
    seq=simulate(a1,N)
    Q=factorize(a1)
    types={}
    for i,a in enumerate(seq):
        n=i+1
        f=factorize(a)
        rho=frozenset(f & S0)
        types.setdefault(rho,[]).append(n)
    return seq, types

if __name__=="__main__":
    pass

def report(a1, S0, N=8000):
    seq, types = analyze(a1, S0, N)
    persistent = {t:idx for t,idx in types.items() if len(idx)>=5}
    print(f"a1={a1} S0={sorted(S0)} N={N}: {len(persistent)} persistent-ish types (>=5 occ)")
    for t, idxs in sorted(persistent.items(), key=lambda kv:-len(kv[1]))[:10]:
        print(f"  type(core-part)={sorted(t)} count={len(idxs)} first5={idxs[:5]}")
    return seq, types
