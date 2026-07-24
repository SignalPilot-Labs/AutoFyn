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
    # integral over [lo,hi) of indicator that N_R(x) is odd, where N_R(x)=#{r in R: r>x}
    # do it via breakpoints
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
for _ in range(3000):
    k = random.randint(1,6)
    Rp = [Fr(random.randint(1,500),1000) for _ in range(k)]
    p2 = Fr(random.randint(500,1000),1000)  # p2 > all R' pieces roughly, not strictly required for identity
    v1 = Fr(random.randint(1,999),1000)
    v2 = Fr(random.randint(0,999),1000)
    if v2>=v1: continue
    F=[v1,v2]
    Gp=[p2]+Rp
    lhs = A(F+Gp)
    Aprime = A(Rp)
    cross = u_indicator_integral(Rp, v2, v1)
    rhs = p2 - Aprime - (v1-v2) + 2*cross
    if lhs != rhs:
        viol+=1
        print("MISMATCH", v1,v2,p2,Rp, lhs, rhs)
print("identity violations:", viol)
