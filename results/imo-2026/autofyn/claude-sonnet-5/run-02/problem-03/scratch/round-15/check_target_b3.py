from fractions import Fraction as F
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign*x
        sign = -sign
    return total

def ladder(n):
    denom = 2**(n+1)-1
    fn = F(1, denom)
    p = [F(2**(n+1-i), denom) for i in range(1, n+2)]
    return p, fn

def refine(multiset, cuts, rng):
    ms = list(multiset)
    for _ in range(cuts):
        idx = rng.randrange(len(ms))
        val = ms[idx]
        num = rng.randint(1, 999)
        frac = F(num, 1000)
        f1 = val*frac
        f2 = val-f1
        if f1<=0 or f2<=0:
            continue
        ms[idx]=f1
        ms.append(f2)
    return ms

def random_exact_pairing(total_target, npairs, rng):
    parts=[]
    remaining=total_target
    for i in range(npairs-1):
        num=rng.randint(1,999)
        frac=F(num,1000)
        part=remaining*frac/(npairs-i)
        parts.append(part)
        remaining-=part
    parts.append(remaining)
    P=[]
    for part in parts:
        half=part/2
        P.append(half); P.append(half)
    return P

random.seed(3)
violations=0
trials=0
for n in range(3,8):
    p, fn = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    tail_full = p[1:]
    max_npairs = (n-1)//2  # need c=1+2*npairs <= n
    if max_npairs<1: continue
    for trial in range(4000):
        rng=random
        npairs = rng.randint(1,max_npairs)
        c_used = 1+2*npairs
        tail_budget = n - c_used
        num = rng.randint(1,999)
        tau_P = p3 + (p2-p3)*F(num,1000)
        if tau_P>=p2: continue
        tstar = p2-tau_P
        if tstar<=0: continue
        num2=rng.randint(1,1000)
        v2 = tstar*F(num2,1000)
        if v2<=0: continue
        v1 = p1-v2-tau_P
        if v1<p2: continue
        P_ = random_exact_pairing(tau_P, npairs, rng)
        Fm=[v1,v2]+P_
        assert sum(Fm)==p1
        cuts = rng.randint(0, tail_budget)
        Gp = refine(tail_full, cuts, rng)
        assert sum(Gp)==sum(tail_full)
        full=Fm+Gp
        assert sum(full)==1
        val=A(full)
        trials+=1
        if val<fn:
            violations+=1
            if violations<=10:
                print("VIOLATION",n,val,fn,"cuts",cuts,"tail_budget",tail_budget,"npairs",npairs)
print("trials",trials,"violations",violations)
