import sys
from math import gcd
from collections import defaultdict

def factorize(x):
    f = set()
    d = 2
    while d*d <= x:
        if x % d == 0:
            f.add(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        f.add(x)
    return f

def gen(a1, N):
    a = [None, a1]
    while len(a) <= N:
        prev = a[-1]
        c = prev + 1
        while True:
            ok = True
            for x in a[1:]:
                if gcd(c, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

def P(x, cache={}):
    if x not in cache:
        cache[x] = factorize(x)
    return cache[x]

def analyze(a1, N, tail_frac=0.5, min_hits=8):
    a = gen(a1, N)
    Q = P(a1)
    tau = {n: P(a[n]) & Q for n in range(1, N+1)}
    tail_start = int(N*tail_frac)
    counts = defaultdict(int)
    for n in range(tail_start, N+1):
        counts[frozenset(tau[n])] += 1
    persistent_base = set(t for t,c in counts.items() if c >= min_hits)
    m = {}
    for t in persistent_base:
        for n in range(1, N+1):
            if frozenset(tau[n]) == t:
                m[t] = n
                break
    S = set()
    for t in persistent_base:
        S |= (P(a[m[t]]) - Q)
    S0 = Q | S
    rho = {n: P(a[n]) & S0 for n in range(1, N+1)}
    counts2 = defaultdict(int)
    for n in range(tail_start, N+1):
        counts2[frozenset(rho[n])] += 1
    persistent_ext = set(t for t,c in counts2.items() if c >= min_hits)
    nmin = {}
    for t in persistent_ext:
        for n in range(1, N+1):
            if frozenset(rho[n]) == t:
                nmin[t] = n
                break
    return dict(a=a, Q=Q, tau=tau, persistent_base=persistent_base, m=m, S=S, S0=S0,
                rho=rho, persistent_ext=persistent_ext, nmin=nmin)

def rogue_pairs(d):
    Q = d['Q']
    pairs = []
    lst = list(d['persistent_ext'])
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j: continue
            Ap, Bp = lst[i], lst[j]
            Abase, Bbase = Ap & Q, Bp & Q
            if Abase and Bbase and (Abase & Bbase == set()) and (Ap & Bp == set()):
                pairs.append((Ap, Bp))
    return pairs

for a1 in [4807, 187, 209, 175]:
    print("="*70)
    print("a1 =", a1)
    N = 6000
    d = analyze(a1, N)
    print("Q =", d['Q'], "S (recruited core extra) =", d['S'], "S0 =", d['S0'])
    print("persistent_base:", d['persistent_base'])
    print("persistent_ext:", d['persistent_ext'])
    rp = rogue_pairs(d)
    print("num rogue pairs at THIS S0:", len(rp))
    for (Ap, Bp) in rp[:6]:
        nA = d['nmin'][Ap]; nB = d['nmin'][Bp]
        Fp = P(d['a'][nA]) - d['S0']
        Fpp = P(d['a'][nB]) - d['S0']
        print(f"  pair A'={Ap} (n_A={nA}) B'={Bp} (n_B={nB})  F'={Fp}  F''={Fpp}")

print("="*70)
print("SEARCH for rogue pairs with |F'| or |F''| >= 2 at properly recruited core")
import random
found = []
for a1 in [15,21,33,35,45,55,65,77,85,91,95,105,115,119,121,133,143,145,155,161,169,175,187,195,205,209,215,221,231,247,253,259,265,275,287,299,305,319,323,329,335,341,355,365,371,377,385,391,395,403,415,425,437,451,455,469,475,481,493,497,505,517]:
    try:
        d = analyze(a1, 4000, min_hits=6)
    except Exception as e:
        print(a1, "ERR", e); continue
    rp = rogue_pairs(d)
    for (Ap,Bp) in rp:
        nA=d['nmin'][Ap]; nB=d['nmin'][Bp]
        Fp = P(d['a'][nA]) - d['S0']; Fpp = P(d['a'][nB]) - d['S0']
        if len(Fp)>=2 or len(Fpp)>=2:
            found.append((a1,Ap,Bp,nA,nB,Fp,Fpp))
            print(a1, "A'=",Ap,"B'=",Bp,"nA=",nA,"nB=",nB,"F'=",Fp,"F''=",Fpp)
print("total found:", len(found))
