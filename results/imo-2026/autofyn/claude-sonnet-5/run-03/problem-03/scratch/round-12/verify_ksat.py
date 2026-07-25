from fractions import Fraction as F
import random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    if l<0: return []
    return [F(2)**i for i in range(0,l+1)]

random.seed(5)
trials=3000
fails=0
tested=0
for _ in range(trials):
    ell = random.randint(2,6)
    cap = F(2)**(ell-1)
    T = gamma(ell-1)
    eps = F(random.randint(1,19),20)
    hi = cap+1-eps
    if hi<=cap: continue
    c1 = cap + F(random.randint(1,int((hi-cap)*40)),40)
    if c1>=hi: continue
    rest_sum = F(2)**ell+eps-c1
    k = ell  # saturated
    # random split of rest_sum into k positive parts < cap
    cuts = sorted([F(random.randint(1,999),1000)*rest_sum for _ in range(k-1)])
    parts=[]; prev=F(0)
    for cpt in cuts:
        parts.append(cpt-prev); prev=cpt
    parts.append(rest_sum-prev)
    if any(p<=0 or p>=cap for p in parts): continue
    Dp = parts
    before = oddsum(Dp+[c1]+T)
    Delta = c1-cap
    headroom = [cap-p for p in Dp]
    totalheadroom = sum(headroom)
    if totalheadroom < Delta: 
        print("INSUFFICIENT HEADROOM even at k=ell", ell, eps, c1, Dp); continue
    # greedily allocate
    D0=[]
    rem = Delta
    for p,h in zip(Dp,headroom):
        take = min(h, rem)
        D0.append(p+take)
        rem -= take
    assert rem<=F(1,10**6), rem
    if any(x<=0 or x>=cap for x in D0): continue
    after = oddsum(D0+[cap]+T)
    tested+=1
    if after > before + F(1,10**9):
        fails+=1
        print("FAIL", ell,eps,c1,Dp,before,D0,after)
print("tested",tested,"fails",fails)
