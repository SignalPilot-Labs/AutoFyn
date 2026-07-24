import random
from fractions import Fraction as F

def A(S):
    s = sorted(S, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign=-sign
    return total

def rand_pos(lo=1,hi=50,dlo=1,dhi=20):
    return F(random.randint(lo,hi), random.randint(dlo,dhi))

random.seed(2)

# Proposition 28: F2 = split of p2 into k>=2 fragments with dominant f1 >= Total(F2\{f1}) + s
# R = legal refinement (here: any multiset with total s < p2), claim A(F2 union R) <= p2 - A(R)
viol=0; hits=0
for _ in range(30000):
    p2 = rand_pos(5,50,1,5)
    k = random.randint(2,5)
    # random split of p2 into k positive fragments
    cuts = sorted(random.sample(range(1,1000), k-1))
    parts = []
    prev = 0
    for c in cuts:
        parts.append(F(c,1000)*p2)
        prev=c
    parts.append(p2 - sum(parts))
    if any(x<=0 for x in parts): continue
    F2 = parts
    f1 = max(F2)
    F2pp = list(F2)
    F2pp.remove(f1)
    # random R with total s < p2 (dominance needs s = total R)
    s_frac = F(random.randint(1,999),1000)  # in (0,1)
    s = s_frac*p2  # ensures s<p2
    rk = random.randint(0,4)
    if rk==0:
        R=[]
        s=F(0)
    else:
        # random positive fragments summing to s
        rcuts = sorted(random.sample(range(1,1000), rk-1)) if rk>1 else []
        rparts=[]
        for c in rcuts:
            rparts.append(F(c,1000)*s)
        rparts.append(s-sum(rparts))
        if any(x<=0 for x in rparts): continue
        R = rparts
    dominant = f1 >= sum(F2pp) + s
    if not dominant: continue
    hits+=1
    lhs = A(F2+R)
    rhs = p2 - A(R)
    if lhs > rhs + F(1,10**9):
        viol+=1
print("Prop28 dominant-fragment hits:", hits, "violations:", viol)
