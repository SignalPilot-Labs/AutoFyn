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

three_named = {(frozenset({0,3}),1,2), (frozenset({0,1}),2,3), (frozenset({0,2}),1,3)}

random.seed(2)
from collections import Counter
cnt=Counter()
N=30000
trials=0
while trials<N:
    p=rand_marking_in_box()
    trials+=1
    T=sum(p)
    best=min(phi_bisect_subset(p,S) for S in subsets)
    if best<=a4*T: continue
    # check if any of the 3 named close it
    named_ok = False
    p1,p2,p3,p4,p5=p
    for phi in [(T+abs(p2-p3-p5))/2,(T+abs(p3-p4-p5))/2,(T+abs(p2-p4-p5))/2]:
        if phi<=a4*T: named_ok=True
    if named_ok: continue
    # find winning pin not in the 3 named
    for k in range(0,4):
        for c in combinations(range(5),k):
            bs=set(c)
            for i in range(5):
                for j in range(5):
                    if i==j: continue
                    v=phi_pin(p,bs,i,j)
                    if v is not None and v<=a4*T:
                        cnt[(frozenset(bs),i,j)] += 1

print("chambers needed beyond the 3 named (count of points where they're the fix):")
for k,v in cnt.most_common(20):
    print(k,v)
