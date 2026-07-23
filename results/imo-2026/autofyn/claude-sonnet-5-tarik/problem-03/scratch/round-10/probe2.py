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
    # support: sorted list of indices to be perfectly matched among themselves (even size)
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

random.seed(2)
trials=0
fixed_support_fails = 0
examples=[]
for p in range(2,8):
    b = p-1
    for t in range(40):
        Y = sorted([random.randint(1,300) for _ in range(p)], reverse=True)
        sels = all_selections(p,b)
        vals = [value(Y,s) for s in sels]
        optv = min(vals)
        opt_sels = [s for s,v in zip(sels,vals) if v==optv]
        # among optimal sels that ARE crossing, check if same-support non-crossing rematching achieves optv
        for sel in opt_sels:
            K,D,M = sel
            if crosses(M):
                trials += 1
                support = sorted([x for pair in M for x in pair])
                # try all matchings on this exact support, check any non-crossing one achieves <= optv when combined with same K,D
                best_alt = None
                for m in all_matchings_on_support(support):
                    if not crosses(m):
                        v = value(Y, (K,D,m))
                        if best_alt is None or v<best_alt:
                            best_alt = v
                if best_alt is None or best_alt > optv:
                    fixed_support_fails += 1
                    examples.append((p,b,Y,sel,optv,best_alt))
print("trials (crossing-optimal instances found)", trials, "fixed-support-rematch fails", fixed_support_fails)
for ex in examples[:5]:
    print(ex)

# Test the round-6 dead-end counterexample specifically, but restricted to b=p-1
Y2 = sorted([43,33,20,16,11,8,2], reverse=True)
p2 = len(Y2)
b2 = p2-1
sels2 = all_selections(p2,b2)
vals2 = [value(Y2,s) for s in sels2]
optv2 = min(vals2)
opt_sels2 = [s for s,v in zip(sels2,vals2) if v==optv2]
print("Y2 dead-end example at b=p-1:", "p=",p2,"b=",b2,"OPT=",optv2)
crossing_opts = [s for s in opt_sels2 if crosses(s[2])]
print("num optimal selections that are crossing:", len(crossing_opts), "/ total optimal", len(opt_sels2))
for sel in crossing_opts[:3]:
    K,D,M = sel
    support = sorted([x for pair in M for x in pair])
    best_alt=None
    for m in all_matchings_on_support(support):
        if not crosses(m):
            v = value(Y2,(K,D,m))
            if best_alt is None or v<best_alt: best_alt=v
    print("sel", sel, "best same-support NC rematch:", best_alt, "vs optv", optv2)
