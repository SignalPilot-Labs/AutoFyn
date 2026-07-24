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
    p = [F(2**(n+1-i), denom) for i in range(1, n+2)]  # p[0]=p1,...,p[n]=p_{n+1}
    return p, fn

def refine(multiset, cuts, rng):
    ms = list(multiset)
    for _ in range(cuts):
        # pick a random piece with positive value, split randomly
        idx = rng.randrange(len(ms))
        val = ms[idx]
        # random split point strictly inside (0,val)
        num = rng.randint(1, 999)
        frac = F(num, 1000)
        f1 = val*frac
        f2 = val-f1
        if f1<=0 or f2<=0:
            continue
        ms[idx]=f1
        ms.append(f2)
    return ms

def random_exact_pairing(total_target, rng, min_pairs=1, max_pairs=3):
    # build P as exact pairs summing to total_target, arbitrary positive values
    npairs = rng.randint(min_pairs, max_pairs)
    # split total_target into npairs positive parts (pair masses), each contributes 2*half
    parts = []
    remaining = total_target
    for i in range(npairs-1):
        num = rng.randint(1,999)
        frac = F(num,1000)
        part = remaining*frac/ (npairs-i)  # rough random split
        parts.append(part)
        remaining -= part
    parts.append(remaining)
    P = []
    for part in parts:
        half = part/2
        P.append(half); P.append(half)
    return P

random.seed(1)
violations = 0
trials = 0
for n in range(3,7):
    p, fn = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    for trial in range(3000):
        rng = random
        # choose tau_P in [p3, p2) strictly less than p2 (so t* in (0,p3])
        num = rng.randint(1,999)
        tau_P = p3 + (p2-p3)*F(num,1000)  # in (p3,p2)
        if tau_P>=p2:
            continue
        tstar = p2-tau_P
        if tstar<=0:
            continue
        # v2 in (0, tstar]
        num2 = rng.randint(1,1000)
        v2 = tstar*F(num2,1000)
        if v2<=0:
            continue
        v1 = p1-v2-tau_P
        if v1 < p2:
            continue  # must satisfy sub-case c constraint v1>=p2
        P = random_exact_pairing(tau_P, rng)
        F_multiset = [v1,v2]+P
        assert abs(sum(F_multiset)-p1)==0, "F mass mismatch"
        tail = p[2:]  # p3,...,p_{n+1}
        cuts = rng.randint(0,3)
        Gp = refine(tail, cuts, rng)
        assert sum(Gp)==sum(tail), "G' mass mismatch"
        full = F_multiset+Gp
        assert sum(full)==p1+sum(tail)==1, "total mass mismatch"
        val = A(full)
        trials+=1
        if val < fn:
            violations+=1
            print("VIOLATION", n, val, fn, v1,v2,tau_P,P,Gp)
        # also check psi(t*) <= p3 and p2-fn > p3
        psi_tstar = A([tstar]+Gp)
        if psi_tstar > p3 + F(1,10**9):
            print("psi bound violation", n, psi_tstar, p3)
        if not (p2-fn > p3):
            print("arithmetic fact violation", n)
print("trials", trials, "violations", violations)
