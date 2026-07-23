from fractions import Fraction as F
from itertools import combinations

def e(multiset):
    # sorted descending alternating sum
    s = sorted(multiset, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign*x
        sign *= -1
    return total

def all_selections(W):
    # yield (Kset, Dset, Mpairs) partitions of W (list of values with indices to allow duplicates)
    n = len(W)
    idx = list(range(n))
    # generate all partitions: choose matched pairs (a perfect matching on a subset), rest split into K/D
    # We'll do recursive generation
    results = []
    def rec(remaining, keep, dele, matched):
        if not remaining:
            results.append((keep[:], dele[:], matched[:]))
            return
        i = remaining[0]
        rest = remaining[1:]
        # delete i
        rec(rest, keep, dele+[i], matched)
        # keep i
        rec(rest, keep+[i], dele, matched)
        # match i with some j in rest
        for jpos, j in enumerate(rest):
            rec(rest[:jpos]+rest[jpos+1:], keep, dele, matched+[(i,j)])
    rec(idx, [], [], [])
    return results

def OPT(sigma, C, W):
    # C: list of background values, W: list of values (list to select from)
    best = None
    for (K,D,M) in all_selections(W):
        vals = list(C)
        for i in K:
            vals.append(W[i])
        for (i,j) in M:
            vals.append(W[i]-W[j])
        val = e(vals)
        if best is None:
            best = val
        else:
            if sigma==1:
                best = min(best,val)
            else:
                best = max(best,val)
    return best

# hand example
C = [F(0), F(10)]
Z1 = [F(15)]
print("OPT_+1(C,Z1) =", OPT(1,C,Z1))
print("e(C) =", e(C))

print("---- full base generator check ----")
b0 = F(0)
Z0 = [F(20), F(15), F(10)]
z1 = Z0[0]
rest = Z0[1:]  # [15,10]
A1 = OPT(1, [b0], rest)
print("A1 =", A1)
A3 = {}
for l in range(len(rest)):
    zl = rest[l]
    newC = [b0, z1-zl]
    newZ = rest[:l]+rest[l+1:]
    A3[zl] = OPT(1, newC, newZ)
    print(f"A3 for partner z={zl}: background={newC}, Z1={newZ}, A3={A3[zl]}")
M = min(A3.values())
print("M =", M, " trigger M<A1?", M<A1)
