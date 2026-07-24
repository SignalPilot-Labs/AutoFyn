from fractions import Fraction as F
import random

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def A(S):
    S = sorted(S, reverse=True)
    return sum((1 if i%2==0 else -1)*v for i,v in enumerate(S))

def random_partition(total, max_parts):
    if max_parts<=1 or total==0:
        return [total] if total>0 else []
    k = random.randint(1, max_parts)
    if k==1:
        return [total]
    cuts = sorted(random.sample(range(1, 10000), k-1))
    cuts = [0]+cuts+[10000]
    parts = [F(cuts[i+1]-cuts[i], 10000)*total for i in range(k)]
    parts[-1] += total - sum(parts)
    return [p for p in parts if p>0]

random.seed(2)
viol=0
trials_per_n = 4000
for n in (3,4):
    p = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    fn = F(1, 2**(n+1)-1)
    s = sum(p[2:])  # total of p3..p_{n+1}
    for t in range(trials_per_n):
        num = random.randint(0, 9999)
        v = s + F(num,10000)*(p2-s)
        if v >= p2: continue
        # F = {v} unpaired residual + pairs summing to p1 - v
        rem = p1 - v
        if rem < 0: continue
        npairs = random.randint(0,2)
        pair_vals=[]
        if npairs>0:
            half = rem/2
            comp = random_partition(half, npairs)
            for val in comp:
                pair_vals += [val, val]
        else:
            if rem != 0: continue
        Fset = [v] + pair_vals
        # G' = {p2} + R', R' refinement of {p3..p_{n+1}} with <= n-2 cuts (<= n-1 parts)
        Rprime = random_partition(s - p3, n-2) 
        # actually total of {p3,...} minus p3? wait R' refines {p3,...,p_{n+1}} entirely (total s), <=n-2 cuts means <=n-1 parts
        Rprime = random_partition(s, n-1)
        Gprime = [p2] + Rprime
        S = Fset + Gprime
        assert abs(sum(S) - 1) < F(1,10**9) or sum(S)==1
        AS = A(S)
        if AS < fn - F(1,10**12):
            viol+=1
            print("VIOLATION", n, v, AS, fn)
print("done, violations:", viol)
