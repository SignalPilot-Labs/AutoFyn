from fractions import Fraction as F
import random
from collections import Counter

def A(S):
    S = sorted(S, reverse=True)
    total = F(0)
    sign = 1
    for x in S:
        total += sign*x
        sign *= -1
    return total

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def funit(n):
    return F(1, 2**(n+1)-1)

def refine_random(pieces, cuts, rng):
    pcs = list(pieces)
    for _ in range(cuts):
        idx = rng.randrange(len(pcs))
        x = pcs[idx]
        if x <= 0: continue
        t = F(rng.randint(1,999),1000)
        a = x*t
        b = x-a
        if a==0 or b==0: continue
        pcs[idx]=a
        pcs.append(b)
    return pcs

def ell(pieces):
    c = Counter(pieces)
    return sum(1 for v,mult in c.items() if mult%2==1)

rng = random.Random(11)
worst = {}
for n in [2,3,4,5,6]:
    p = ladder(n)
    p1 = p[0]
    tail = p[1:]
    fn = funit(n)
    total_budget = n  # Xiang Yu's total cut budget matches Liu Bang's n points
    min_margin = None
    argmin = None
    violations = 0
    trials = 60000
    for trial in range(trials):
        c1 = rng.randint(1, total_budget)  # cuts spent on p1, at least 1 to get ell(F) potentially >=2
        if c1 > total_budget: continue
        remaining = total_budget - c1
        F_split = refine_random([p1], c1, rng)
        if ell(F_split) < 2:
            continue
        ctail = rng.randint(0, remaining)
        Gp = refine_random(tail, ctail, rng)
        S = F_split + Gp
        val = A(S)
        margin = val - fn
        if min_margin is None or margin < min_margin:
            min_margin = margin
            argmin = (F_split, Gp)
        if margin < 0:
            violations += 1
    worst[n] = (min_margin, violations, trials, argmin)
    print(n, "min margin A-f(n) over ell(F)>=2 configs:", min_margin, 
          "violations:", violations, "/", trials, "argmin:", argmin)
