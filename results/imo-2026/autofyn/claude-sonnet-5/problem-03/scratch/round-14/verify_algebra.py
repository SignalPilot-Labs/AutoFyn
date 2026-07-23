from fractions import Fraction as F
import random

def e3(x,y,z):
    s = sorted([x,y,z], reverse=True)
    return s[0]-s[1]+s[2]

random.seed(2)
bad=0
for _ in range(20000):
    b0 = F(random.randint(0,20))
    w = F(random.randint(0,20))
    d2 = F(random.randint(0,20))
    keepval = e3(b0,d2,w)
    if d2 >= max(b0,w):
        formula = d2 - abs(b0-w)
        if formula != keepval:
            bad+=1
    D2 = d2  # if we also set b0 term... wait D2=|b0-d2|, let's just check equivalence condition
# check the "Case A & keepval<D2 <=> w>2b0" claim
bad2=0
tested=0
for _ in range(20000):
    b0 = F(random.randint(0,20))
    w = F(random.randint(0,20))
    d2 = F(random.randint(0,20))
    if d2 < max(b0,w):
        continue
    tested+=1
    keepval = e3(b0,d2,w)
    D2 = abs(b0-d2)
    cond_lhs = keepval < D2
    cond_rhs = w > 2*b0
    if cond_lhs != cond_rhs:
        bad2+=1
print("bad formula count:", bad, "bad equivalence count:", bad2, "tested case A instances:", tested)
