from fractions import Fraction as F
import random

c3 = F(8,15)
gamma3 = F(1,15)

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

random.seed(1)
trials = 0
fails = 0
r_negative = 0
examples = []
for _ in range(200000):
    # sample region B(3): p1<1/2, gaps>gamma3, p1+p2+p3+p4=1, all>0
    # generate via random gaps
    p4 = F(random.randint(1,2000), 100000)
    g3 = gamma3 + F(random.randint(1,3000),100000)  # p3-p4
    g2 = gamma3 + F(random.randint(1,3000),100000)  # p2-p3
    g1 = gamma3 + F(random.randint(1,3000),100000)  # p1-p2
    p3 = p4+g3
    p2 = p3+g2
    p1 = p2+g1
    total = p1+p2+p3+p4
    # normalize
    p1,p2,p3,p4 = p1/total, p2/total, p3/total, p4/total
    if p1>=F(1,2):
        continue
    # re-check gaps after normalization scale preserved ratios so gaps ok (linear)
    trials+=1
    r = p1-p2-p3
    if r<=0:
        r_negative+=1
        continue
    M = [p2,p2,p3,p3,r,p4]
    os = oddsum(M)
    if os >= c3:
        fails+=1
        if len(examples)<5:
            examples.append((p1,p2,p3,p4,r,os))

print("trials(valid region, ignoring r sign):", trials)
print("r<=0 count (infeasible witness):", r_negative)
feasible = trials - r_negative
print("feasible witness count:", feasible)
print("fails (OddSum>=c3) among feasible:", fails, f"{fails/feasible*100 if feasible else 0:.2f}%")
for ex in examples:
    print(ex)
