import random, itertools
from fractions import Fraction as F

def A(S):
    s = sorted(S, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign*=-1
    return total

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p_1..p_{n+1}

def rand_legal_refinement(pieces, budget):
    # pieces: list of fractions (multiset), budget: number of cuts allowed total
    # perform up to `budget` random cuts, each splitting a randomly chosen current fragment into two positive parts
    frags = list(pieces)
    cuts_used = random.randint(0, budget)
    for _ in range(cuts_used):
        idx = random.randrange(len(frags))
        val = frags[idx]
        if val <= 0: continue
        r = F(random.randint(1,999),1000)
        a = val*r
        b = val-a
        if a<=0 or b<=0: continue
        frags[idx] = a
        frags.append(b)
    return frags

random.seed(3)
f = lambda n: F(1, 2**(n+1)-1)

viol=0
trials=3000
n = 5
D = 2**(n+1)-1
L = ladder(n)  # p1..p_{n+1}, indices 1..n+1 -> L[0..n]
p1,p2,p3 = L[0],L[1],L[2]
tail = L[2:]  # p3..p_{n+1}
for _ in range(trials):
    # build F = {v1,v2} U P with v1>=p2>v2, P exact pairs, tau_P < p3
    npairs = random.randint(0,2)
    P=[]
    tau_P = F(0)
    for _ in range(npairs):
        val = F(random.randint(1,999),1000)*p3/ (npairs if npairs else 1)  # keep small
        P += [val,val]
        tau_P += 2*val
    if tau_P >= p3:
        continue
    v2max = p2 - tau_P
    v2 = F(random.randint(1,999),1000) * v2max
    if v2 >= p2: v2 = p2*F(999,1000)
    v1 = p1 - v2 - tau_P
    if v1 < p2:  # need v1>=p2 for sub-case c
        continue
    F_ = [v1,v2]+P
    # G' legal refinement of tail with remaining budget: cuts used on p1 = len(F_)-1, remaining budget n-cuts_on_p1
    cuts_on_p1 = len(F_)-1
    remaining = n - cuts_on_p1
    if remaining < 0:
        continue
    Gp = rand_legal_refinement(tail, remaining)
    total_val = A(F_+Gp)
    target = f(n)
    if total_val < target - F(1,10**9):
        viol+=1
        print("VIOLATION", n, F_, Gp, total_val, target)
print(f"n={n}: trials attempted with valid config, violations={viol}")
