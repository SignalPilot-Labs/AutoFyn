from fractions import Fraction as F
import random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    if l<0: return []
    return [F(2)**i for i in range(0,l+1)]

def rand_frac(a,b,denom=20):
    lo = int(a*denom)+1
    hi = int(b*denom)-1
    if hi<lo:
        return F(a+b,2)
    return F(random.randint(lo, hi), denom)

random.seed(7)
trials=3000
fails=0
for _ in range(trials):
    ell = random.randint(2,5)
    cap = F(2)**(ell-1)
    T = gamma(ell-1)
    eps = rand_frac(0,1)
    hi = cap+1-eps
    if hi<=cap: continue
    c1p = cap + rand_frac(0, hi-cap) if hi>cap else cap
    total = F(2)**ell+eps
    rest_sum = total - c1p
    if rest_sum<=0: continue
    k = random.randint(1, ell)
    # random admissible D' at c1p: k positive elements < cap summing to rest_sum
    # generate via random simplex-ish split
    cuts = sorted([F(random.randint(1,999),1000)*rest_sum for _ in range(k-1)])
    parts=[]
    prev=F(0)
    for c in cuts:
        parts.append(c-prev); prev=c
    parts.append(rest_sum-prev)
    if any(p<=0 or p>=cap for p in parts): continue
    Dp = parts
    before = oddsum(Dp+[c1p]+T)

    # reduce to endpoint: transfer Delta = c1p-cap from c1 back into D elements (spread by headroom)
    Delta = c1p-cap
    headroom = [cap-p for p in Dp]
    totalheadroom = sum(headroom)
    if totalheadroom < Delta:
        continue  # shouldn't happen per our argument but check
    D = []
    remaining = Delta
    for p,h in zip(Dp,headroom):
        if totalheadroom==0: break
        share = Delta * (h/totalheadroom) if totalheadroom>0 else 0
        share = min(share, h)
        D.append(p+share)
    # fix rounding: adjust last to make sum exact
    diff = (rest_sum+Delta) - sum(D)
    D[-1]+=diff
    if any(d<=0 or d>=cap for d in D):
        continue
    after = oddsum(D+[cap]+T)
    if after > before + F(1,10**9):
        fails+=1
        if fails<=5:
            print("FAIL: endpoint value exceeds interior value (reduction direction violated)")
            print("ell",ell,"eps",eps,"c1p",c1p,"Dp",Dp,"before",before,"D",D,"after",after)
print("trials", trials, "fails", fails)
