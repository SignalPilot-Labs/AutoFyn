import sympy
from itertools import combinations

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
    ground = sorted(set().union(*family)) if family else []
    hits = []
    # iterate subsets of ground in increasing size, stop when all minimal found
    for r in range(1, len(ground)+1):
        for c in combinations(ground, r):
            cs = frozenset(c)
            # check if it's a hitting set
            if not all(cs & S for S in family): continue
            # check minimality: no proper subset is a hitting set
            # only subsets of size r-1 are candidates; those are smaller so would have been processed
            is_min = True
            for e in cs:
                sub = cs - frozenset([e])
                if all(sub & S for S in family):
                    is_min = False; break
            if is_min:
                hits.append(cs)
    return hits

# Use smaller a_1 with short periods
for a1, N in [(15, 60), (35, 80), (77, 60), (91, 60)]:
    a, primal_min = fast_greedy(a1, N)
    distinct_supports = sorted(set(frozenset(sympy.primefactors(x)) for x in a))
    primal_ms = [s for s in distinct_supports if not any(other < s for other in distinct_supports)]
    primal_ms_sorted = sorted([sorted(s) for s in primal_ms])
    mt = minimal_transversals(distinct_supports)
    mt_sorted = sorted([sorted(s) for s in mt])
    mtmt = minimal_transversals([frozenset(s) for s in mt])
    mtmt_sorted = sorted([sorted(s) for s in mtmt])
    print(f"a1={a1}: distinct_supports#={len(distinct_supports)}")
    print(f"  primal MS (incl-min of F) = {primal_ms_sorted}")
    print(f"  dual MT(F)                = {mt_sorted}")
    print(f"  MT(MT(F))                 = {mtmt_sorted}")
    print(f"  primal==MT(MT(F))?        = {primal_ms_sorted == mtmt_sorted}")
