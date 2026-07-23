from fractions import Fraction as F
import random

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

random.seed(99)
bad=0
tested=0
# include zero and tie-heavy edge cases
specials = [F(0), F(1,2), F(1)]
for _ in range(6000):
    b0 = random.choice([F(0)] + [F(random.randint(0,40),random.choice([1,2,4])) for _ in range(1)])
    w = random.choice([F(0)] + [F(random.randint(0,40),random.choice([1,2,4])) for _ in range(1)])
    z2 = w + F(random.randint(0,40),random.choice([1,2,4]))
    A1 = OPT(1,[b0],[z2,w])
    for _ in range(3):
        d2 = F(random.randint(0,80), random.choice([1,2,4]))
        tested += 1
        keepval = e([b0,d2,w])
        D2 = abs(b0-d2)
        lhs = min(D2,keepval); rhs = min(A1,D2)
        if lhs < rhs:
            bad += 1
            print("VIOL", b0,w,z2,A1,d2,keepval,D2)
print("tested", tested, "bad", bad)
