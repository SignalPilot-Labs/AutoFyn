from fractions import Fraction as F
import random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    if l<0: return []
    return [F(2)**i for i in range(0,l+1)]

random.seed(11)
trials=2000
fails=0
tested=0
for _ in range(trials):
    ell = random.randint(2,6)
    cap = F(2)**(ell-1)
    T = gamma(ell-1)
    eps = F(random.randint(1,19),20)
    hi = cap+1-eps
    if hi<=cap: continue
    c1 = cap + F(random.randint(1, int((hi-cap)*40)),40)
    if c1>=hi: continue
    d1 = F(2)**ell+eps-c1
    if not (0<d1<cap): continue
    # k=1 case only
    before = oddsum([d1,c1]+T)
    Delta = c1-cap
    D0 = [d1, Delta]  # insert Delta as new element
    if any(x<=0 or x>=cap for x in D0): continue
    after = oddsum(D0+[cap]+T)
    tested+=1
    if after > before + F(1,10**9):
        fails+=1
        print("FAIL", ell, eps, c1, d1, before, after)
print("tested",tested,"fails",fails)
