from fractions import Fraction as F
import random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

random.seed(1)
violations=0
trials=20000
for _ in range(trials):
    n = random.randint(1,6)
    # random rest multiset D
    D = [F(random.randint(1,50), random.randint(1,20)) for _ in range(n)]
    c1 = F(random.randint(1,50), random.randint(1,20))
    T = [F(random.randint(1,50), random.randint(1,20)) for _ in range(random.randint(0,5))]
    if not D: continue
    xi = random.randrange(len(D))
    x = D[xi]
    if c1 < x:  # only test transfer TO the (weakly) larger element c1
        continue
    delta = F(random.randint(1,min(1000, int(x*20)+1)), 20)
    if delta<=0 or delta>=x: continue
    D2 = D.copy(); D2[xi] = x-delta
    c1b = c1+delta
    before = oddsum(D+[c1]+T)
    after = oddsum(D2+[c1b]+T)
    if after < before:
        violations+=1
        if violations<=10:
            print("VIOLATION", D, c1, T, "x=",x,"delta=",delta, "before",before,"after",after)
print("trials",trials,"violations",violations)
