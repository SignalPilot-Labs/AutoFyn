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
    for r in range(1, len(ground)+1):
        for c in combinations(ground, r):
            cs = frozenset(c)
            if not all(cs & S for S in family): continue
            is_min = True
            for e in cs:
                sub = cs - frozenset([e])
                if all(sub & S for S in family):
                    is_min = False; break
            if is_min:
                hits.append(cs)
    return hits

# Try a1=175 (M1=35), period 274 — too big for brute MT. Use just enough terms to get stable MS
# Instead use a small synthetic example to confirm primal vs dual can differ
F = [frozenset({1,2,3}), frozenset({2,3}), frozenset({3,4})]
Fmin = [s for s in F if not any(other < s for other in F)]
print("Synthetic F =", [sorted(s) for s in F])
print("  primal MS (incl-min) =", sorted([sorted(s) for s in Fmin]))
mt = minimal_transversals(F)
print("  dual MT(F)           =", sorted([sorted(s) for s in mt]))
mtmt = minimal_transversals([frozenset(s) for s in mt])
print("  MT(MT(F))            =", sorted([sorted(s) for s in mtmt]))
print("  primal==MT(MT(F))?   =", sorted([sorted(s) for s in Fmin]) == sorted([sorted(s) for s in mtmt]))
print("  primal==dual MT?     =", sorted([sorted(s) for s in Fmin]) == sorted([sorted(s) for s in mt]))
