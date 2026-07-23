from fractions import Fraction as F
from itertools import product

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

violations=[]
checked=0
N=6
for z1i,z2i,z3i in product(range(2*N+1), repeat=3):
    zs = sorted([z1i,z2i,z3i], reverse=True)
    if len(set(zs))<2: continue
    z1,z2,z3 = F(zs[0],2), F(zs[1],2), F(zs[2],2)
    for b0i in range(0, 2*N+1):
        b0 = F(b0i,2)
        checked+=1
        rest=[z2,z3]
        A1 = OPT(1,[b0],rest)
        for l in range(2):
            zl = rest[l]; d = z1-zl
            newC=[b0,d]; newZ = rest[:l]+rest[l+1:]
            A3l = OPT(1,newC,newZ)
            Dl = abs(b0-d)
            if A3l < min(A1,Dl):
                violations.append((z1,z2,z3,b0,l,A3l,Dl,A1))
print("checked",checked,"violations",len(violations))
for v in violations[:10]: print(v)
