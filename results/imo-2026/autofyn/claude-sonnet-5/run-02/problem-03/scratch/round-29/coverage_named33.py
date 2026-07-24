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

def rand_marking_in_box(maxden=300):
    while True:
        vals=[random.randint(1,maxden) for _ in range(5)]
        vals.sort(reverse=True)
        p=[F(v) for v in vals]
        T=sum(p)
        if p[0]<T*F(1,2) and T*F(1,31)<p[1]<T*F(8,31):
            return p

def three_pin_phis(p):
    p1,p2,p3,p4,p5=p
    T=sum(p)
    phi1=(T+abs(p2-p3-p5))/2
    phi2=(T+abs(p3-p4-p5))/2
    phi3=(T+abs(p2-p4-p5))/2
    return [phi1,phi2,phi3]

random.seed(2)
N=30000
trials=0
covered_bisect=0
covered_named=0
uncov=[]
while trials<N:
    p=rand_marking_in_box()
    trials+=1
    T=sum(p)
    vals=[phi_bisect_subset(p,S) for S in subsets]
    best=min(vals)
    if best<=a4*T:
        covered_bisect+=1
        covered_named+=1
        continue
    extra=three_pin_phis(p)
    best2=min(vals+extra)
    if best2<=a4*T:
        covered_named+=1
    else:
        if len(uncov)<10:
            uncov.append((p,T,best2))

print(f"trials={trials} bisect_only={covered_bisect} ({covered_bisect/trials*100:.2f}%) named33={covered_named} ({covered_named/trials*100:.2f}%)")
for p,T,b in uncov:
    print([float(x/T) for x in p], float(b/T), float(a4))
