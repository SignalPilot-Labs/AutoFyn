from fractions import Fraction as F
import random
exec(open('explore1.py').read().split("for n in")[0])

def best_subset_sum_le_with_set(vals, cap):
    best=F(0); bestset=[]
    n=len(vals)
    for mask in range(1<<n):
        s=F(0); idxs=[]
        for i in range(n):
            if mask&(1<<i):
                s+=vals[i]; idxs.append(i)
        if s<=cap and s>best:
            best=s; bestset=idxs
    return best,bestset

def build_multiset_and_check(p):
    p1=p[0]; tail=p[1:]
    T,idxset=best_subset_sum_le_with_set(tail,p1)
    r=p1-T
    M=[]
    for i,v in enumerate(tail):
        if i in idxset:
            M.append(v)  # untouched
            M.append(v)  # tied fragment (from p1)
        else:
            M.append(v/2)
            M.append(v/2)
    if r>0:
        M.append(r)
    direct = oddsum(M)
    formula = F(1,2)+r/F(2)
    return direct, formula

random.seed(42)
for n in [3,4,5,6]:
    n1=n+1
    for trial in range(20):
        xs=[random.random() for _ in range(n1)]
        xs.sort(reverse=True)
        s=sum(xs)
        p=[F(x/s).limit_denominator(500) for x in xs]
        p[-1]+= (1-sum(p))
        p.sort(reverse=True)
        if p[-1]<=0: continue
        d,f = build_multiset_and_check(p)
        if d!=f:
            print("MISMATCH", n, p, d, f)
print("done - no mismatches printed means formula verified exactly")
