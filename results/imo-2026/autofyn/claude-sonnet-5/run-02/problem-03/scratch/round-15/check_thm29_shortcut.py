import random
from fractions import Fraction as F

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)], D

def A(S):
    S = sorted(S, reverse=True)
    total = F(0); sign=1
    for x in S:
        total += sign*x; sign=-sign
    return total

def random_split(piece, cuts):
    if cuts == 0:
        return [piece]
    pts = sorted(random.sample(range(1, 10000), cuts))
    pts = [F(p, 10000) for p in pts]
    bounds = [F(0)] + pts + [F(1)]
    fracs = [(bounds[i+1]-bounds[i]) for i in range(len(bounds)-1)]
    return [piece*fr for fr in fracs]

def random_refinement(pieces, total_cuts):
    k = len(pieces)
    if total_cuts <= 0:
        return list(pieces)
    cuts_alloc = [0]*k
    for _ in range(total_cuts):
        cuts_alloc[random.randrange(k)] += 1
    result = []
    for p, c in zip(pieces, cuts_alloc):
        result.extend(random_split(p, c))
    return result

random.seed(5)
# Test: for t* in the OPEN range (t* <= p3, i.e. tau_P >= p3), does naive
# "Theorem 29 with M=t*, F2={t*}, R=G'" conclusion A({t*} u G') <= t* - A(G')
# still hold, even though the hypothesis max(R) <= M/2 is violated?
for n in [3,4,5,6]:
    pieces, D = ladder(n)
    p2, p3 = pieces[1], pieces[2]
    tail = pieces[2:]
    fails = 0; tot=0
    worst_margin = None
    for _ in range(3000):
        tstar = F(random.randint(1,9999),10000) * p3   # tstar in (0,p3], the "open range" t*<=p3
        cuts = random.randint(0, n-2)
        Rp = random_refinement(tail, cuts)
        lhs = A([tstar]+Rp)
        rhs = tstar - A(Rp)
        tot+=1
        if lhs > rhs:
            fails += 1
            m = lhs-rhs
            if worst_margin is None or m > worst_margin:
                worst_margin = m
    print(f"n={n}: naive-shortcut conclusion A({{t*}}UR)<=t*-A(R) violated in {fails}/{tot} trials; worst violation margin={float(worst_margin) if worst_margin else None}")
