from fractions import Fraction as F
import itertools, random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    # Gamma_{l} = {1,2,4,...,2^l}
    return [F(2)**i for i in range(0,l+1)]

def search(ell, eps, denom, max_extra=None, verbose=False):
    eps = F(eps)
    T = gamma(ell-1)  # Gamma_{ell-1}
    cap = F(2)**(ell-1)
    total = F(2)**ell + eps
    best = None
    bestC = None
    # c1 ranges over [cap, cap+1-eps) at grid resolution
    c1_vals = set()
    n1 = denom
    lo = cap
    hi = cap + 1 - eps
    steps = max(1, int((hi-lo)*denom))
    for i in range(steps+1):
        c1 = lo + F(i, denom)
        if c1 < hi:
            c1_vals.add(c1)
    c1_vals.add(lo)
    if max_extra is None:
        max_extra = ell  # |C| <= ell+1 => rest has <= ell elements
    for c1 in c1_vals:
        rest_sum = total - c1
        if rest_sum <= 0: continue
        # enumerate rest multisets with k=0..max_extra elements, each < cap, positive, summing to rest_sum
        # grid search over compositions with denom resolution; k up to max_extra
        for k in range(1, max_extra+1):
            # generate all multisets of k positive rationals (multiples of 1/denom) < cap summing to rest_sum
            # use stars and bars on grid units, sorted descending to avoid dup, cap constraint
            units_total = rest_sum * denom
            if units_total != int(units_total): 
                continue
            units_total = int(units_total)
            cap_units = int(cap*denom)  # strict less than cap
            if units_total < k: continue
            # partitions of units_total into k positive parts each <= cap_units-1, unordered
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
            cnt=0
            for part in partitions(units_total, k, cap_units-1):
                cnt+=1
                if cnt>200000:
                    break
                D = [F(p,denom) for p in part]
                C = D + [c1]
                val = oddsum(C+T)
                if best is None or val < best:
                    best = val
                    bestC = C
    return best, bestC, F(2)**ell

for ell,eps,denom in [(2, F(1,2), 6), (2, F(1,3), 6), (3, F(1,2), 4), (3, F(1,3), 6)]:
    best,bestC,target = search(ell, eps, denom)
    print(f"ell={ell} eps={eps} denom={denom}: best={best} target=2^ell={target} margin={best-target if best else None}  C={bestC}")
