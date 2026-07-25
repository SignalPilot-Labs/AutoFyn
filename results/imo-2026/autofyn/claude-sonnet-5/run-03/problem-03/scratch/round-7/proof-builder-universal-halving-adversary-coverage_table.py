from fractions import Fraction as F
import random
exec(open('explore1.py').read().split("for n in")[0])

def best_subset_sum_le(vals, cap):
    best=F(0)
    n=len(vals)
    for mask in range(1<<n):
        s=F(0)
        for i in range(n):
            if mask&(1<<i):
                s+=vals[i]
        if s<=cap and s>best:
            best=s
    return best

def tailtie_val(p):
    p1=p[0]; tail=p[1:]
    T=best_subset_sum_le(tail,p1)
    r=p1-T
    return F(1,2)+r/F(2)

def check(n, trials=300):
    n1=n+1
    g=gamma(n); cc=c(n)
    rng=random.Random(9090+n)
    gen=random_balanced_partition(n1,rng)
    tot=0; fail=0
    while tot<trials:
        p=next(gen)
        if p[0]>=F(1,2): continue
        if p[-1]<=g: continue
        gaps=[p[i]-p[i+1] for i in range(n1-1)]
        if min(gaps)<=g: continue
        tot+=1
        b1=best_k1(p); b2=best_k2(p); tt=tailtie_val(p)
        best=min(b1,b2,tt)
        if best>cc: fail+=1
    return tot,fail

print("| n | trials | fraction still failing after best of {k1,k2,tailtie} |")
for n in [3,4,5,6,7,8]:
    tot,fail=check(n, trials=300)
    print(f"| {n} | {tot} | {100*fail/tot:.1f}% |")
