from fractions import Fraction as F
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total=F(0); sign=1
    for x in s:
        total+=sign*x; sign=-sign
    return total

def u_indicator_integral_from(multiset, v):
    # compute integral_v^infty u_S(x) dx directly via breakpoints
    s = sorted([x for x in multiset], reverse=True)
    # breakpoints are all distinct values in multiset union {v}
    pts = sorted(set(s+[v]), reverse=True)
    # restrict to points >= v
    pts = [p for p in pts if p>=v]
    if not pts or pts[-1]!=v:
        pts.append(v)
        pts = sorted(set(pts), reverse=True)
    total=F(0)
    for i in range(len(pts)-1):
        hi=pts[i]; lo=pts[i+1]
        mid_count = sum(1 for e in s if e>lo)  # count using open interval representative near lo+ (works since lo is a breakpoint or v)
        # to determine parity in interval (lo,hi), count elements > lo (works if no ties at lo other than boundary)
        if mid_count%2==1:
            total += hi-lo
    return total

random.seed(42)
trials=0
mismatches=0
for _ in range(3000):
    k = random.randint(1,7)
    S = [F(random.randint(1,1000),random.randint(1,50)) for _ in range(k)]
    v = F(random.randint(0,500), random.randint(1,50))
    S_gt_v = [x for x in S if x>v]
    eps = 1 if len(S_gt_v)%2==1 else 0
    lhs = u_indicator_integral_from(S, v)
    rhs = A(S_gt_v) - v*eps
    trials+=1
    if lhs!=rhs:
        mismatches+=1
        print("MISMATCH", S, v, lhs, rhs)
print("trials",trials,"mismatches",mismatches)
