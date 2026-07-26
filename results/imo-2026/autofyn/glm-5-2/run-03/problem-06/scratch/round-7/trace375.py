import math
from collections import defaultdict

def prime_factors_set(x):
    fs = set()
    y = x
    d = 2
    while d*d <= y:
        if y % d == 0:
            fs.add(d)
            while y % d == 0:
                y //= d
        d += 1
    if y > 1:
        fs.add(y)
    return fs

def rad(a1):
    r=1; x=a1; d=2
    while d*d<=x:
        if x%d==0:
            r*=d
            while x%d==0: x//=d
        d+=1
    if x>1: r*=x
    return r

def prune_minimal(family):
    kept=[]
    for s in sorted(family, key=len):
        if not any(t<=s for t in kept):
            kept.append(s)
    out=[]; seen=set()
    for s in kept:
        if s not in seen:
            seen.add(s); out.append(s)
    return out

def add_set(MT, S_new):
    S_new=frozenset(S_new)
    new=[]
    for T in MT:
        if T & S_new:
            new.append(T)
        else:
            for p in S_new:
                new.append(T | {p})
    return prune_minimal(new)

def trace(a1, N, verbose=False):
    M1 = rad(a1)
    a = [a1]
    P0 = prime_factors_set(a1)
    MT = [frozenset([p]) for p in P0]
    MT = prune_minimal(MT)
    # recruitment log: for each prime p, the first step n at which p first appears in ANY MT member
    first_seen = {}  # prime -> (step, term a_n that triggered)
    for p in P0:
        first_seen[p] = (0, a1)
    print(f"a1={a1} M1={M1} P(a1)={sorted(P0)}")
    for step in range(1, N):
        prev = a[-1]
        m = prev+1
        while True:
            Pm = prime_factors_set(m)
            if any(t <= Pm for t in MT):
                break
            m += 1
        a.append(m)
        S_new = prime_factors_set(m)
        MT_new = add_set(MT, S_new)
        # detect newly recruited primes: primes in MT_new not in union(MT)
        old_primes = set()
        for T in MT: old_primes |= T
        new_primes = set()
        for T in MT_new:
            for p in T:
                if p not in old_primes:
                    new_primes.add(p)
        for p in new_primes:
            if p not in first_seen:
                first_seen[p] = (step, m)
                print(f"  step {step}: NEW prime {p} enters MT (term a_{step}={m}, P={sorted(S_new)})")
        MT = MT_new
        if verbose and step < 50:
            print(f"  step {step}: a_{step}={m}, P={sorted(S_new)}, |MT|={len(MT)}")
    # period detect
    d=[a[i+1]-a[i] for i in range(len(a)-1)]
    n=len(d)
    for min_run in [2000, 8000, 15000]:
        found=None
        for T in range(1, n//2):
            ok=True
            start=n-min_run
            for k in range(start, n-T):
                if d[k+T]!=d[k]:
                    ok=False; break
            if ok:
                found=(T, n-min_run); break
        if found:
            T,_=found
            L=sum(d[n-min_run: n-min_run+T])
            print(f"  min_run={min_run}: T={T}, L={L}, factor(L)={sorted(prime_factors_set(L))}")
            return a,d,first_seen,T,L
    print("  no period found")
    return a,d,first_seen,None,None

if __name__=='__main__':
    for a1,N in [(375, 30000), (9375, 30000)]:
        a,d,fs,T,L = trace(a1,N)
        print(f"  Recruitment log (prime -> first step):")
        for p in sorted(fs):
            step,term = fs[p]
            print(f"    {p}: first enters MT at step {step} (term a_{step}={term})")
        print()
