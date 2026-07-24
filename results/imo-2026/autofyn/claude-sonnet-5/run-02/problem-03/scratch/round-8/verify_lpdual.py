from fractions import Fraction as F
import random

def sorted_desc(x): return sorted(x, reverse=True)

def phi(ms):
    s=sorted_desc(ms)
    tot=F(0)
    for i,v in enumerate(s):
        if i%2==0: tot+=v
    return tot

def theoremC(p):
    # p sorted desc, p1..pm
    p1=p[0]; rest=p[1:]
    final = [p1/2,p1/2]+rest
    return phi(final)

def theoremC_formula(p):
    p1=p[0]; rest=p[1:]
    tail_odd = sum(rest[i] for i in range(len(rest)) if i%2==0)
    return p1/2+tail_odd

def theoremD(p):
    p1=p[0]; pm=p[-1]; mid=p[1:-1]
    final=[p1/2,p1/2,pm/2,pm/2]+mid
    return phi(final)

def theoremD_formula(p):
    p1=p[0]; pm=p[-1]; mid=p[1:-1]
    mid_odd = sum(mid[i] for i in range(len(mid)) if i%2==0)
    return p1/2+pm/2+mid_odd

random.seed(5)
viol=0
for trial in range(2000):
    m = random.randint(2,8)
    raw = sorted([random.randint(1,50) for _ in range(m)], reverse=True)
    p = [F(x) for x in raw]
    c1 = theoremC(p); c2=theoremC_formula(p)
    d1 = theoremD(p); d2=theoremD_formula(p)
    if c1!=c2 or d1!=d2:
        viol+=1
        print("MISMATCH", p, c1,c2,d1,d2)
print("done, violations:", viol)
