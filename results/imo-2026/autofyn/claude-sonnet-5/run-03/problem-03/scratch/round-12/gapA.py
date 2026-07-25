from fractions import Fraction as F

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    if l<0: return []
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

def gapA_min(ell, eps, denom):
    cap = F(2)**(ell-1)
    Tprime = gamma(ell-2)
    budget = cap+eps
    best=None; bestD=None
    for k in range(1, ell+1):
        units = budget*denom
        if units != int(units): continue
        units=int(units)
        capu = int(cap*denom)
        if units<k: continue
        for part in partitions(units,k,capu-1):
            D=[F(p,denom) for p in part]
            val = oddsum(D+Tprime)
            if best is None or val<best:
                best=val; bestD=D
    return best, bestD

for ell in [2,3,4]:
    for eps in [F(1,4),F(1,3),F(1,2),F(3,4)]:
        denom = 12 if ell<=3 else 8
        best,bestD = gapA_min(ell,eps,denom)
        target = F(2)**(ell-1)
        print(f"ell={ell} eps={eps}: min OddSum(D+Gamma_{{ell-2}})={best}  target={target} margin={best-target}  D={bestD}")
