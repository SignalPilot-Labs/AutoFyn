from fractions import Fraction as F
import random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def gamma(l):
    return [F(2)**i for i in range(0,l+1)]

random.seed(2)
violations=0
trials=20000
for _ in range(trials):
    ell = random.randint(2,6)
    cap = F(2)**(ell-1)
    T = gamma(ell-1)
    n = random.randint(1,ell)
    # random D with elements < cap
    D = [F(random.randint(1, int(cap*20)-1), 20) for _ in range(n)]
    if any(d<=0 or d>=cap for d in D): continue
    eps = F(random.randint(1,19),20)
    c1 = cap + F(random.randint(0, int((1-eps)*20)-1),20)
    if c1<cap or c1>=cap+1-eps: continue
    # pick element to shrink
    xi = random.randrange(len(D))
    x = D[xi]
    maxdelta = min(x, cap+1-eps-c1-F(1,1000))  # keep c1 in window after
    if maxdelta<=0: continue
    delta = F(random.randint(1, max(1,int(maxdelta*20))),20)
    if delta<=0 or delta>x or c1+delta>=cap+1-eps: continue
    D2 = D.copy(); D2[xi]=x-delta
    if D2[xi]<0: continue
    c1b = c1+delta
    before = oddsum(D+[c1]+T)
    after = oddsum(D2+[c1b]+T)
    if after<before:
        violations+=1
        if violations<=10:
            print("VIOLATION ell",ell,"eps",eps,"D",D,"c1",c1,"x",x,"delta",delta,"before",before,"after",after)
print("trials(effective)",trials,"violations",violations)
