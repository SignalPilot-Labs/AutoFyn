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

# q=3 exhaustive search, integers 0..N, plus b0 over 0..N (and half-integers)
N = 10
violations = []
triggered_count = 0
checked = 0
vals_range = [F(i,2) for i in range(0, 2*N+1)]  # half-integer steps 0..N
for z1v,z2v,z3v in product(range(N+1), repeat=3):
    zs = sorted([z1v,z2v,z3v], reverse=True)
    if len(set(zs))<2: continue
    z1,z2,z3 = F(zs[0]), F(zs[1]), F(zs[2])
    for b0i in range(0, 2*N+1):
        b0 = F(b0i,2)
        checked += 1
        rest = [z2,z3]
        A1 = OPT(1,[b0], rest)
        A3 = {}
        for l in range(2):
            zl = rest[l]
            newC = [b0, z1-zl]
            newZ = rest[:l]+rest[l+1:]
            A3[l] = OPT(1, newC, newZ)
        M = min(A3.values())
        if M < A1:
            triggered_count += 1
            kstars = [l for l in range(2) if A3[l]==M]
            for k in kstars:
                d = z1 - rest[k]
                D = abs(b0-d)
                if M != D:
                    violations.append((z1,z2,z3,b0,k,M,D))
print("checked", checked, "triggered", triggered_count, "violations", len(violations))
for v in violations[:10]:
    print(v)
