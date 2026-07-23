import itertools, random
from fractions import Fraction as F

def e(vals):
    vals = sorted(vals, reverse=True)
    s = 0
    for i,v in enumerate(vals):
        s += v if i%2==0 else -v
    return s

def all_selections(p, b):
    # indices 0..p-1
    idx = list(range(p))
    # generate all partitions into K, D, M (pairwise disjoint pairs), cost=|D|+|M|<=b
    results = []
    def rec(remaining, K, D, M, cost):
        if not remaining:
            if cost<=b:
                results.append((tuple(K), tuple(D), tuple(M)))
            return
        i = remaining[0]
        rest = remaining[1:]
        # keep i
        rec(rest, K+[i], D, M, cost)
        # delete i
        if cost+1<=b:
            rec(rest, K, D+[i], M, cost+1)
        # match i with some j in rest
        if cost+1<=b:
            for j in rest:
                rec([x for x in rest if x!=j], K, D, M+[(i,j)], cost+1)
    rec(idx, [], [], [], 0)
    return results

def value(Y, sel):
    K,D,M = sel
    vals = [Y[k] for k in K] + [Y[i]-Y[j] for (i,j) in M]
    return e(vals)

def crosses(M):
    for a in range(len(M)):
        for b_ in range(a+1,len(M)):
            i,j = M[a]; ii,jj = M[b_]
            if i>j: i,j=j,i
            if ii>jj: ii,jj=jj,ii
            if (i<ii<j<jj) or (ii<i<jj<j):
                return True
    return False

def is_noncrossing(sel):
    K,D,M = sel
    return not crosses(M)

random.seed(1)
fails = 0
trials = 0
counterexamples = []
for p in range(1,8):
    b = p-1
    for t in range(60):
        Y = sorted([random.randint(1,300) for _ in range(p)], reverse=True)
        sels = all_selections(p,b)
        vals = [value(Y,s) for s in sels]
        optv = min(vals)
        opt_sels = [s for s,v in zip(sels,vals) if v==optv]
        has_nc = any(is_noncrossing(s) for s in opt_sels)
        trials += 1
        if not has_nc:
            fails += 1
            counterexamples.append((p,b,Y,optv))

print("trials", trials, "fails (no non-crossing optimizer)", fails)
for c in counterexamples[:5]:
    print(c)
