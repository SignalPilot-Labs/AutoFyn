from fractions import Fraction as F
import random

def e_of(sorted_desc):
    s=0; sign=1
    for x in sorted_desc:
        s+=sign*x; sign*=-1
    return s

def simple_static_rule(A, m):
    # A sorted descending
    A = sorted(A, reverse=True)
    k = len(A)
    best = None
    for r in range(0, min(m,k)+1):
        # delete top r via D (r ops), remaining budget m-r for matching the rest
        rest = A[r:]
        budget2 = m-r
        # greedily match consecutive pairs among 'rest' (in original sorted order) using up to budget2 matches
        # try matching first 2*budget2 elements of rest into budget2 pairs (consecutive), leave remainder untouched
        nmatch = min(budget2, len(rest)//2)
        matched_part = rest[:2*nmatch]
        leftover = rest[2*nmatch:]
        produced = [matched_part[2*i]-matched_part[2*i+1] for i in range(nmatch)]
        finalM = sorted(produced+leftover, reverse=True)
        val = e_of(finalM)
        if best is None or val<best:
            best = val
    return best

def target(m):
    return F(1, 2**(m+1)-1)

A1 = (F(239,500), F(112,500), F(75,500), F(74,500))
print("A1 m=3 simple:", simple_static_rule(A1,3), "target", float(target(3)*sum(A1)))

A2 = (F(1,2), F(333,1000), F(167,1000))
print("A2 m=2 simple:", simple_static_rule(A2,2), "target", float(target(2)*sum(A2)))

random.seed(11)
def rand_case2(k, denom=30):
    while True:
        vals = sorted([random.randint(1,denom) for _ in range(k)], reverse=True)
        if vals[-1]==0: continue
        Afull=[F(v) for v in vals]
        if Afull[0] < 2*Afull[1]:
            return tuple(Afull)

fails=0; total=0
for m in [2,3,4,5,6]:
    k=m+1
    trials=200
    tgt=target(m)
    for _ in range(trials):
        A = rand_case2(k, denom=40)
        S=sum(A)
        val = simple_static_rule(A,m)
        bound = tgt*S
        total+=1
        if bound-val<0:
            fails+=1
            if fails<=10:
                print("FAIL", m, A, val, float(val), float(bound))
print("total",total,"fails",fails)
