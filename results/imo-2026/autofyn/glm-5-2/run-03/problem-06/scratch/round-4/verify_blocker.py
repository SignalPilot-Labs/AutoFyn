import math, itertools

def greedy_seq(a1, N):
    a = [a1]
    while len(a) < N:
        m = a[-1] + 1
        while True:
            if all(math.gcd(m, x) > 1 for x in a):
                a.append(m); break
            m += 1
    return a

def support(n):
    s = set()
    for p in range(2, n+1):
        if n % p == 0:
            while n % p == 0: n//=p
            s.add(p)
            if n == 1: break
    return frozenset(s)

def minimals(family):
    # inclusion-minimal elements
    fam = list(set(family))
    out = []
    for i, s in enumerate(fam):
        if any(t < s for t in fam):  # proper subset
            continue
        out.append(s)
    return frozenset(out)

def transversals(family, ground):
    # enumerate minimal hitting sets over ground
    family = list(family)
    if not family: return [frozenset()]
    # recursive
    def rec(idx, chosen):
        if idx == len(family):
            # check minimality: no proper subset still hits all
            for x in chosen:
                if (chosen - {x}) & family_member_check(family, chosen - {x}) == family_member_check(family, chosen-{x}):
                    pass
            return [chosen]
        out = []
        # need to hit family[idx]
        for x in ground:
            if x in family[idx]:
                out += rec(idx+1, chosen | {x})
        return out
    # too slow; do iterative minimal hitting sets via powerset
    return None

def is_transversal(T, family):
    return all(T & s for s in family)

def minimal_transversals(family, ground):
    # enumerate all minimal transversals
    from itertools import combinations
    ground = list(ground)
    out = []
    # try subsets by increasing size — but ground small
    for r in range(1, len(ground)+1):
        for combo in combinations(ground, r):
            T = frozenset(combo)
            if is_transversal(T, family):
                # minimal?
                if not any(is_transversal(T - {x}, family) for x in T):
                    out.append(T)
    return out

a = greedy_seq(15, 40)
F = [support(x) for x in a]
ground = set()
for s in F: ground |= set(s)
MS = minimals(F)
print("MS:", set(MS))
MT = minimal_transversals(F, ground)
print("MT:", set(MT))
MTMT = minimal_transversals(MT, ground)
print("MT(MT):", set(MTMT))
print("MT(MT) == MS:", set(MTMT) == set(MS))
