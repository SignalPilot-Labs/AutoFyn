import sympy

def fast_greedy(a1, N):
    a=[a1]; minimal=[frozenset(sympy.primefactors(a1))]
    for _ in range(N-1):
        cur=a[-1]; m=cur+1
        while True:
            ms=frozenset(sympy.primefactors(m))
            if all(ms&S for S in minimal):
                a.append(m)
                if not any(S<=ms for S in minimal):
                    minimal=[S for S in minimal if not(ms<=S)]; minimal.append(ms)
                break
            m+=1
    return a,minimal

def minimal_transversals(family):
    # family = list of frozensets. Find minimal hitting sets.
    # brute force: only feasible for small ground set
    ground = sorted(set().union(*family))
    # iterate over subsets of ground in increasing size
    from itertools import combinations
    hits = []
    for r in range(1, len(ground)+1):
        for c in combinations(ground, r):
            cs = frozenset(c)
            if all(cs & S for S in family):
                # check minimal: no proper subset is a hitting set
                if not any((cs - frozenset([e])) != cs and (cs - frozenset([e])).intersection(*[S for S in family]) == cs for e in cs) and not any(ss < cs for ss in hits):
                    # simpler: check no proper subset hits
                    is_min = True
                    for e in cs:
                        sub = cs - frozenset([e])
                        if all(sub & S for S in family):
                            is_min = False; break
                    if is_min:
                        hits.append(cs)
    return hits

# Test for a1 = 77 (T=18, small)
for a1, N in [(77, 200), (91, 200), (35, 200), (143, 400), (15, 200)]:
    a, primal_min = fast_greedy(a1, N)
    # Get distinct supports from a
    distinct_supports = sorted(set(frozenset(sympy.primefactors(x)) for x in a))
    # primal minimal = inclusion-minimal of distinct_supports
    primal_ms = []
    for s in distinct_supports:
        if not any(other < s for other in distinct_supports):
            primal_ms.append(s)
    primal_ms = sorted([sorted(s) for s in primal_ms])
    # dual MT
    mt = minimal_transversals(distinct_supports)
    mt_sorted = sorted([sorted(s) for s in mt])
    # MT(MT(F))
    mtmt = minimal_transversals([frozenset(s) for s in mt])
    mtmt_sorted = sorted([sorted(s) for s in mtmt])
    print(f"a1={a1}: distinct_supports#={len(distinct_supports)}")
    print(f"  primal MS (incl-min of F) = {primal_ms}")
    print(f"  dual MT(F)                = {mt_sorted}")
    print(f"  MT(MT(F)) (=primal?)      = {mtmt_sorted}")
    print(f"  primal==MT(MT(F))? {primal_ms == mtmt_sorted}")
