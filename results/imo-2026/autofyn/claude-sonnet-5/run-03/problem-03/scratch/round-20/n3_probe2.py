from fractions import Fraction as F
import random

c3 = F(8,15)
gamma3 = F(1,15)

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

random.seed(2)
patterns = {}
min_margin = None
minpt=None
count=0
for _ in range(300000):
    p4 = F(random.randint(1,2000), 100000)
    g3 = gamma3 + F(random.randint(1,3000),100000)
    g2 = gamma3 + F(random.randint(1,3000),100000)
    g1 = gamma3 + F(random.randint(1,3000),100000)
    p3 = p4+g3
    p2 = p3+g2
    p1 = p2+g1
    total = p1+p2+p3+p4
    p1,p2,p3,p4 = p1/total, p2/total, p3/total, p4/total
    if p1>=F(1,2):
        continue
    r = p1-p2-p3
    if r<=0:
        continue
    count+=1
    labeled = [('p2a',p2),('p2b',p2),('p3a',p3),('p3b',p3),('r',r),('p4',p4)]
    labeled.sort(key=lambda x:-x[1])
    order = tuple(x[0] for x in labeled)
    patterns[order] = patterns.get(order,0)+1
    os = oddsum([v for _,v in labeled])
    margin = c3-os
    if min_margin is None or margin<min_margin:
        min_margin=margin; minpt=(p1,p2,p3,p4,r,os)

print("feasible count:", count)
print("distinct orderings:", len(patterns))
for k,v in sorted(patterns.items(), key=lambda x:-x[1])[:10]:
    print(v,k)
print("min margin (c3-OddSum):", min_margin, float(min_margin))
print("achieved near:", minpt)
