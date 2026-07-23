import sys
sys.path.insert(0,'/tmp/round-10')
exec(open('/tmp/round-10/probe4.py').read().split("random.seed")[0])  # reuse function defs only

def check(Yraw, note=""):
    Y = sorted(Yraw, reverse=True)
    p = len(Y)
    b = p-1
    sels = all_selections(p,b)
    vals = [value(Y,s) for s in sels]
    optv = min(vals)
    opt_sels = [s for s,v in zip(sels,vals) if v==optv]
    any_crossing = False
    any_fail = False
    for sel in opt_sels:
        K,D,M = sel
        if crosses(M):
            any_crossing = True
            support = sorted([x for pair in M for x in pair])
            best_alt = None
            for m in all_matchings_on_support(support):
                if not crosses(m):
                    v = value(Y,(K,D,m))
                    if best_alt is None or v<best_alt: best_alt = v
            if best_alt is None or best_alt>optv:
                any_fail = True
                print("FAIL", note, Y, sel, optv, best_alt)
    print(note, "p=",p,"b=",b,"OPT=",optv,"had crossing optimum:",any_crossing,"fail:",any_fail)

check([92,89,77,73], "known p=4 per-j counterexample instance (adapted to b=p-1)")
check([463,461,372,291,237,180], "round-9 reroute dead-end instance")
check([39,36,30,28,22,18,14], "round-7 OPT<NC general-b counterexample, at b=p-1")
check([400,218,194,187,169,27,3], "second round-7 counterexample, at b=p-1")
check([43,33,20,16,11,8,2], "round-6 local-exchange dead-end instance, at b=p-1")
