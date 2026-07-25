from fractions import Fraction as F

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    return [F(2)**i for i in range(0,l+1)]

def partitions(n, k, maxpart):
    if k==1:
        if 1<=n<=maxpart:
            yield (n,)
        return
    start = min(maxpart, n-(k-1))
    for first in range(start, (n+k-1)//k -1, -1):
        if first<1: break
        for rest in partitions(n-first, k-1, first):
            yield (first,)+rest

def min_oddsum_given_c1(ell, eps, c1, denom, max_extra=None):
    T = gamma(ell-1)
    cap = F(2)**(ell-1)
    total = F(2)**ell + eps
    rest_sum = total - c1
    if max_extra is None:
        max_extra = ell
    best=None; bestD=None
    if rest_sum == 0:
        return oddsum([c1]+T), []
    for k in range(1, max_extra+1):
        units_total = rest_sum*denom
        if units_total != int(units_total): continue
        units_total = int(units_total)
        cap_units = int(cap*denom)
        if units_total < k: continue
        for part in partitions(units_total, k, cap_units-1):
            D = [F(p,denom) for p in part]
            val = oddsum(D+[c1]+T)
            if best is None or val<best:
                best=val; bestD=D
    return best, bestD

for ell in [2,3]:
    cap = F(2)**(ell-1)
    for eps in [F(1,4), F(1,2), F(3,4)]:
        denom = 8
        hi = cap + 1 - eps
        print(f"--- ell={ell} eps={eps} cap={cap} hi={hi} ---")
        i=0
        c1 = cap
        while c1 < hi:
            best,bestD = min_oddsum_given_c1(ell, eps, c1, denom)
            target = F(2)**ell
            print(f"  c1={c1}: min_oddsum={best} margin={best-target if best else None}  D={bestD}")
            i+=1
            c1 = cap + F(i,denom)
