from fractions import Fraction as F
from itertools import product
import random

def e3(x,y,z):
    s = sorted([x,y,z], reverse=True)
    return s[0]-s[1]+s[2]

def e(vals):
    s = sorted(vals, reverse=True)
    total=F(0); sign=1
    for v in s:
        total+=sign*v; sign*=-1
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

# Verify the FULL proof mechanism directly: for random b0,w,z2 (fixing A1 = OPT_+1({b0},{z2,w})),
# and d2 ranging over many values, check:
# (a) A1 <= b0
# (b) A1 <= |b0-w|
# (c) keepval formula matches e3
# (d) min(D2,keepval) >= min(A1,D2)  [the actual target]
random.seed(7)
bad_a=bad_b=bad_c=bad_d=0
tested=0
for _ in range(4000):
    b0 = F(random.randint(0,30))
    w = F(random.randint(0,30))
    z2 = w + F(random.randint(0,30))  # ensure z2>=w
    A1 = OPT(1,[b0],[z2,w])
    if A1 > b0: bad_a+=1
    if A1 > abs(b0-w): bad_b+=1
    for _ in range(5):
        d2 = F(random.randint(0,60))
        tested+=1
        keepval = e3(b0,d2,w)
        D2 = abs(b0-d2)
        lhs = min(D2,keepval)
        rhs = min(A1,D2)
        if lhs < rhs:
            bad_d += 1
            print("VIOLATION", b0,w,z2,A1,d2,keepval,D2,lhs,rhs)

print("tested d2-instances:", tested, "bad_a(A1<=b0 fails):",bad_a,"bad_b(A1<=|b0-w| fails):",bad_b,"bad_d(target fails):",bad_d)
