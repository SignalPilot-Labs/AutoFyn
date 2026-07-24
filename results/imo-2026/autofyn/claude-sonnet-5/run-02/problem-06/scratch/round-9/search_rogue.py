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

cache={}
def P(x):
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

results = []
N = 4000
seeds = list(range(100, 1200))
import random
random.seed(1)
random.shuffle(seeds)
tested = 0
for a1 in seeds:
    if tested > 150:
        break
    Qf = factorize(a1)
    if len(Qf) < 2:
        continue
    tested += 1
    try:
        d = analyze(a1, N)
    except Exception as e:
        continue
    rp = rogue_pairs(d)
    for (Ap, Bp) in rp:
        nA = d['nmin'][Ap]; nB = d['nmin'][Bp]
        Fp = P(d['a'][nA]) - d['S0']
        Fpp = P(d['a'][nB]) - d['S0']
        if len(Fp) >= 2 or len(Fpp) >= 2:
            qstar = min(Fp & Fpp) if (Fp & Fpp) else None
            # check A'-side occurrences for failures against qstar
            occ = [n for n in range(max(nA,nB)+1, N+1) if d['rho'][n] == Ap]
            if qstar is not None and occ:
                fails = [n for n in occ if qstar not in P(d['a'][n])]
                results.append((a1, Ap, Bp, nA, nB, Fp, Fpp, qstar, len(occ), len(fails), fails[:20]))
print("tested seeds:", tested, " found instances:", len(results))
for r in results:
    a1, Ap, Bp, nA, nB, Fp, Fpp, qstar, nocc, nfail, failidx = r
    print("a1=",a1,"A'=",Ap,"B'=",Bp,"nA=",nA,"nB=",nB,"F'=",Fp,"F''=",Fpp,"q*=",qstar,
          "occurrences=",nocc,"fails=",nfail, "fail_idx_sample=",failidx)
