"""Verify strengthened cofactor-P1-divisibility: any governing r not in P_1."""
import sys
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import greedy_mt, rad, sieve_primes

def factorize(x):
    fs = set(); d=2; y=x
    while d*d<=y:
        while y%d==0: fs.add(d); y//=d
        d+=1
    if y>1: fs.add(y)
    return fs

def check(a1, N=600):
    M1 = rad(a1)
    P1 = factorize(a1)
    maxval = a1 + (N+5)*M1 + 50
    sp = sieve_primes(min(maxval, 2_000_000))
    a = greedy_mt(a1, N, sp)
    # determine governing set = primes of L (compute L from period)
    d = [a[i+1]-a[i] for i in range(N-1)]
    n = len(d)
    T=None
    for t in range(1, n//3):
        need=3*t
        if n-need<0: break
        ok=True
        for k in range(n-need, n-t):
            if d[k+t]!=d[k]: ok=False; break
        if ok:
            n0=n-need
            while n0>0 and d[n0-1+t]==d[n0-1]: n0-=1
            T=t; L=sum(d[n0:n0+t]); break
    if T is None: return f"a1={a1}: no period"
    G = factorize(L)
    p,q = sorted(P1)
    out = [f"a1={a1} P1={P1} M1={M1} G={G} T={T} L={L}"]
    for r in sorted(G):
        if r in P1: continue
        tot=0; fails=0
        for x in a:
            if x % r == 0:
                k = x//r
                tot+=1
                if k % p != 0 and k % q != 0:
                    fails+=1
        out.append(f"  r={r} (gov, not in P1): {tot} mult, {fails} cofactor-fails (not div by {p} or {q})")
    return "\n".join(out)

for a1 in [15, 35, 65, 77, 91, 143, 175, 375]:
    print(check(a1))
