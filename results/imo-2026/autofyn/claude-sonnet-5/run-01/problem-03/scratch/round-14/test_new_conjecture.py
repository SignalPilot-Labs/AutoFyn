from fractions import Fraction as F
from itertools import product
import random

def e(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign*=-1
    return total

def all_selections(W):
    n=len(W); idx=list(range(n)); results=[]
    def rec(remaining, keep, dele, matched):
        if not remaining:
            results.append((keep[:], dele[:], matched[:])); return
        i = remaining[0]; rest = remaining[1:]
        rec(rest, keep, dele+[i], matched)
        rec(rest, keep+[i], dele, matched)
        for jpos,j in enumerate(rest):
            rec(rest[:jpos]+rest[jpos+1:], keep, dele, matched+[(i,j)])
    rec(idx, [], [], [])
    return results

def OPT(sigma, C, W):
    best=None
    for (K,D,M) in all_selections(W):
        vals=list(C)
        for i in K: vals.append(W[i])
        for (i,j) in M: vals.append(W[i]-W[j])
        val = e(vals)
        if best is None: best=val
        else: best = min(best,val) if sigma==1 else max(best,val)
    return best

def check(Z0, b0):
    z1 = Z0[0]; rest = Z0[1:]
    A1 = OPT(1,[b0], rest)
    results = []
    for l in range(len(rest)):
        zl = rest[l]
        d = z1-zl
        newC = [b0, d]
        newZ = rest[:l]+rest[l+1:]
        A3l = OPT(1, newC, newZ)
        Dl = abs(b0-d)
        results.append((l, A3l, Dl, A1))
    return A1, results

violations = []
checked=0
random.seed(1)
for trial in range(3000):
    q = random.randint(2,6)
    vmax = random.randint(1,12)
    Z0 = sorted([random.randint(0,vmax) for _ in range(q)], reverse=True)
    if len(set(Z0))<2: continue
    Z0 = [F(x) for x in Z0]
    b0 = F(random.randint(0,2*vmax),random.choice([1,2]))
    checked+=1
    A1, results = check(Z0,b0)
    for (l,A3l,Dl,A1_) in results:
        if A3l < min(A1_, Dl) - F(0):
            violations.append((Z0,b0,l,A3l,Dl,A1_))

print("checked", checked, "violations", len(violations))
for v in violations[:10]:
    print(v)
