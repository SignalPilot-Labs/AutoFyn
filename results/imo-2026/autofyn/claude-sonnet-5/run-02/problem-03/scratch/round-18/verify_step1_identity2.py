from fractions import Fraction as Fr
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = 0
    for i,x in enumerate(s):
        if i % 2 == 0:
            total += x
        else:
            total -= x
    return total

def u_indicator_integral(R, lo, hi):
    if hi<=lo: return Fr(0)
    breakpoints = sorted(set([r for r in R if lo<=r<=hi]+[lo,hi]))
    total = Fr(0)
    for i in range(len(breakpoints)-1):
        a,b = breakpoints[i], breakpoints[i+1]
        if b<=a: continue
        mid = (a+b)/2
        cnt = sum(1 for r in R if r>mid)
        if cnt %2==1:
            total += (b-a)
    return total

random.seed(3)
viol=0
tested=0
for _ in range(20000):
    k = random.randint(1,6)
    Rp = [Fr(random.randint(1,100),1000) for _ in range(k)]  # small fragments
    sumRp = sum(Rp)
    p2 = sumRp + Fr(random.randint(1,1000),1000)  # ensure p2 > sum(Rp), i.e. dominant
    v1 = p2 * Fr(random.randint(1,999),1000)  # v1 in (0,p2)
    v2 = v1 * Fr(random.randint(0,999),1000)  # v2 in [0,v1)
    if v2>=v1: continue
    tested+=1
    F=[v1,v2]
    Gp=[p2]+Rp
    lhs = A(F+Gp)
    Aprime = A(Rp)
    cross = u_indicator_integral(Rp, v2, v1)
    rhs = p2 - Aprime - (v1-v2) + 2*cross
    if lhs != rhs:
        viol+=1
        if viol<5:
            print("MISMATCH", v1,v2,p2,Rp, lhs, rhs)
print("tested", tested, "identity violations:", viol)
