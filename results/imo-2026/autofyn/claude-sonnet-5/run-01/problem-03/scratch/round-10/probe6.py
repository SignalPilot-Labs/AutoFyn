import random
exec(open('/tmp/round-10/probe4.py').read().split("random.seed")[0])

random.seed(777)
total=0
fails=0
for p in [7,8]:
    b = p-1
    trialsN = 40 if p==7 else 12
    for t in range(trialsN):
        Y = sorted([random.randint(1,600) for _ in range(p)], reverse=True)
        sels = all_selections(p,b)
        vals = [value(Y,s) for s in sels]
        optv = min(vals)
        opt_sels = [s for s,v in zip(sels,vals) if v==optv]
        for sel in opt_sels:
            K,D,M = sel
            if crosses(M):
                total+=1
                support = sorted([x for pair in M for x in pair])
                best_alt=None
                for m in all_matchings_on_support(support):
                    if not crosses(m):
                        v=value(Y,(K,D,m))
                        if best_alt is None or v<best_alt: best_alt=v
                if best_alt is None or best_alt>optv:
                    fails+=1
                    print("FAIL", p,b,Y,sel,optv,best_alt)
print("p=7,8 at b=p-1: crossing-optimal instances", total, "fails", fails)
