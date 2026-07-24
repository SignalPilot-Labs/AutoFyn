import random
from fractions import Fraction as F
from itertools import combinations

a4 = F(16,31)

def A(sorted_desc):
    s=F(0)
    for i,v in enumerate(sorted_desc):
        s += v if i%2==0 else -v
    return s

def phi_bisect_subset(p, S):
    frags=[]
    for i in range(5):
        if i in S: frags += [p[i]/2,p[i]/2]
        else: frags += [p[i]]
    T=sum(frags); sd=sorted(frags,reverse=True)
    return (T+A(sd))/2

subsets=[]
for k in range(1,5):
    for c in combinations(range(5),k):
        subsets.append(set(c))

def phi_pin(p, bisect_set, pin_i, pin_j):
    if pin_i in bisect_set or pin_j==pin_i: return None
    if p[pin_i] < p[pin_j]: return None
    frags=[]
    for i in range(5):
        if i in bisect_set: frags += [p[i]/2,p[i]/2]
        elif i==pin_i: frags += [p[pin_j], p[pin_i]-p[pin_j]]
        else: frags += [p[i]]
    if len(bisect_set)+1>4: return None
    T=sum(frags); sd=sorted(frags,reverse=True)
    return (T+A(sd))/2

def rand_marking_in_box(maxden=300):
    while True:
        vals=[random.randint(1,maxden) for _ in range(5)]
        vals.sort(reverse=True)
        p=[F(v) for v in vals]
        T=sum(p)
        if p[0]<T*F(1,2) and T*F(1,31)<p[1]<T*F(8,31):
            return p

random.seed(2)
N=30000
trials=0
covered_named=0
uncov=[]
while trials<N:
    p=rand_marking_in_box()
    trials+=1
    T=sum(p)
    vals=[phi_bisect_subset(p,S) for S in subsets]
    best=min(vals)
    ok = best<=a4*T
    if not ok:
        # full pin search exact
        for k in range(0,4):
            for c in combinations(range(5),k):
                bs=set(c)
                for i in range(5):
                    for j in range(5):
                        if i==j: continue
                        v=phi_pin(p,bs,i,j)
                        if v is not None and v<best:
                            best=v
        ok = best<=a4*T
    if ok:
        covered_named+=1
    else:
        uncov.append((p,T,best))

print(f"trials={trials} covered_full_pin_family={covered_named} ({covered_named/trials*100:.4f}%)")
print("uncovered count:", len(uncov))
for p,T,b in uncov[:10]:
    print(p, T, b, a4*T)
