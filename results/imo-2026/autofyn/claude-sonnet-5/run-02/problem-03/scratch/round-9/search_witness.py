from fractions import Fraction as F
import random

def phi(S):
    S = sorted(S, reverse=True)
    return sum(S[i] for i in range(0,len(S),2))

p = [F(2,5), F(3,10), F(1,5), F(1,10)]
best = phi(p)
bestS=list(p)
random.seed(0)
for trial in range(300000):
    pcs = list(p)
    ncuts = random.randint(0,3)
    for _ in range(ncuts):
        idx = random.randrange(len(pcs))
        x = pcs[idx]
        t = F(random.randint(1,999),1000)
        a = x*t; b = x-a
        if a==0 or b==0: continue
        pcs[idx]=a; pcs.append(b)
    val = phi(pcs)
    if val < best:
        best = val; bestS = list(pcs)
print("best found:", best, float(best), bestS)
