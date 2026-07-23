import itertools, random

def e(vals):
    vals = sorted(vals, reverse=True)
    s = 0
    for i,v in enumerate(vals):
        s += v if i%2==0 else -v
    return s

def all_selections(p, b):
    idx = list(range(p))
    results = []
    def rec(remaining, K, D, M, cost):
        if not remaining:
            if cost<=b:
                results.append((tuple(K), tuple(D), tuple(M)))
            return
        i = remaining[0]
        rest = remaining[1:]
        rec(rest, K+[i], D, M, cost)
        if cost+1<=b:
            rec(rest, K, D+[i], M, cost+1)
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
        for bb in range(a+1,len(M)):
            i,j = M[a]; ii,jj = M[bb]
            if i>j: i,j=j,i
            if ii>jj: ii,jj=jj,ii
            if (i<ii<j<jj) or (ii<i<jj<j):
                return True
    return False

def all_matchings_on_support(support):
    if not support:
        yield ()
        return
    a = support[0]
    rest = support[1:]
    for k in range(len(rest)):
        b_ = rest[k]
        remaining = rest[:k]+rest[k+1:]
        for m in all_matchings_on_support(remaining):
            yield ((a,b_),) + m

random.seed(12345)
total_crossing_instances = 0
fails = 0
fail_examples=[]
by_budget_off = {}  # b = p-1-off
for p in range(2,9):
    for off in range(0,3):  # test b=p-1, p-2, p-3
        b = p-1-off
        if b<0: continue
        for t in range(80 if p<=7 else 15):
            Y = sorted([random.randint(1,500) for _ in range(p)], reverse=True)
            sels = all_selections(p,b)
            vals = [value(Y,s) for s in sels]
            optv = min(vals)
            opt_sels = [s for s,v in zip(sels,vals) if v==optv]
            for sel in opt_sels:
                K,D,M = sel
                if crosses(M):
                    key = off
                    by_budget_off[key] = by_budget_off.get(key,0)+1
                    total_crossing_instances += 1
                    support = sorted([x for pair in M for x in pair])
                    best_alt = None
                    for m in all_matchings_on_support(support):
                        if not crosses(m):
                            v = value(Y, (K,D,m))
                            if best_alt is None or v<best_alt:
                                best_alt = v
                    if best_alt is None or best_alt > optv:
                        fails += 1
                        fail_examples.append((p,b,off,Y,sel,optv,best_alt))
                    break  # only need one crossing-optimal sel per (Y,b) to log, avoid over-counting duplicates; but let's not break to be thorough
print("total crossing-optimal instances encountered:", total_crossing_instances)
print("by offset (0=b=p-1,1=b=p-2,2=b=p-3):", by_budget_off)
print("fixed-support-rematch fails:", fails)
for f in fail_examples[:10]:
    print(f)
