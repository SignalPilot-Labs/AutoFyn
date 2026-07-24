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
trials_per_n = 6000
for n in (3,4):
    p = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    fn = F(1, 2**(n+1)-1)
    s = sum(p[2:])
    for t in range(trials_per_n):
        num = random.randint(0, 9999)
        v = s + F(num,10000)*(p2-s)
        if v >= p2: continue
        rem = p1 - v
        if rem <= 0: continue
        npairs = random.randint(1,2)
        half = rem/2
        comp = random_partition(half, npairs)
        pair_vals = []
        for val in comp:
            pair_vals += [val, val]
        actual_npairs = len(comp)
        cuts_F = 2*actual_npairs
        if cuts_F > n: continue
        tail_budget_cuts = n - cuts_F   # max cuts for G' total = |R'| since G'={p2}+R'
        if tail_budget_cuts < 0: continue
        # need at least 0 cuts on tail overall but per Prop24 statement uses <= n-2 (worst case); use actual budget
        max_parts_R = max(1, tail_budget_cuts)   # cuts = parts (since G'=p2+R', cuts(G')=|R'|)
        Rprime = random_partition(s, max_parts_R)
        Gprime = [p2] + Rprime
        Fset = [v] + pair_vals
        S = Fset + Gprime
        total_cuts = (len(Fset)-1) + (len(Gprime)-1)
        if total_cuts > n: continue
        assert sum(S) == 1
        AS = A(S)
        if AS < fn - F(1,10**12):
            viol+=1
            if viol<=10:
                print("VIOLATION", n, v, AS, fn, "cuts_F", cuts_F, "cuts_G", len(Gprime)-1)
print("done, violations:", viol)
