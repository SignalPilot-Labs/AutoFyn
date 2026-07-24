from fractions import Fraction as F
import random

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def A(S):
    S = sorted(S, reverse=True)
    return sum((1 if i%2==0 else -1)*v for i,v in enumerate(S))

def random_partition(total, max_parts=6):
    # random composition of `total` into a random number of positive parts (Fraction)
    k = random.randint(1, max_parts)
    if k==1:
        return [total]
    cuts = sorted(random.sample(range(1, 10000), k-1))
    cuts = [0]+cuts+[10000]
    parts = [F(cuts[i+1]-cuts[i], 10000)*total for i in range(k)]
    # ensure sum exact
    parts[-1] += total - sum(parts)
    return [p for p in parts if p>0]

random.seed(1)
viol=0
trials_per_n = 3000
for n in range(3,7):
    p = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    fn = F(1, 2**(n+1)-1)
    s4 = sum(p[3:])  # total of p4..p_{n+1}
    for t in range(trials_per_n):
        # random w' >= p3, w' < p2
        # choose w' uniformly in [p3, p2)
        num = random.randint(0, 9999)
        wprime = p3 + F(num,10000)*(p2-p3)
        if wprime >= p2: continue
        # pairs P_2: random pairs summing with wprime to p2
        rem = p2 - wprime
        if rem < 0: continue
        npairs = random.randint(0,3)
        pair_vals = []
        if npairs>0:
            # split rem into npairs*2 with pair structure: choose npairs random values summing (each doubled) to rem
            # generate npairs positive fracs summing to rem/2
            half = rem/2
            comp = random_partition(half, max_parts=npairs) if npairs>1 else [half]
            if len(comp)!=npairs:
                # fallback single group
                comp = [half]
            for v in comp:
                pair_vals += [v,v]
        else:
            if rem != 0:
                continue  # need rem=0 if no pairs
        Gprime = [wprime] + pair_vals + [p3] + random_partition(s4, max_parts=5)
        total_check = sum(Gprime)
        assert total_check == p2 + p3 + s4
        AG = A(Gprime)
        bound = p2 - fn
        if AG > bound + F(1,10**12):
            viol+=1
            print("VIOLATION", n, wprime, AG, bound)
print("trials done, violations:", viol)
