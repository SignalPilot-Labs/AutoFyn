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

# use approximate floats converted to fraction with denom 10^17 scaled -- instead use the printed ratios *some denom
pts = [
[0.34125, 0.22, 0.18375, 0.145, 0.11],
[0.47317073170731705, 0.24390243902439024, 0.16747967479674797, 0.07642276422764227, 0.03902439024390244],
]
# reconstruct as fractions with reasonable denom by scaling to sum 1 then use limit_denominator
from fractions import Fraction
for pt in pts:
    p = [Fraction(x).limit_denominator(100000) for x in pt]
    T=sum(p)
    p = [x for x in p]
    best=None;bestkey=None
    subsets=[]
    for k in range(1,5):
        for c in combinations(range(5),k): subsets.append(set(c))
    for S in subsets:
        v=phi_bisect_subset(p,S)
        if best is None or v<best: best=v;bestkey=('bisect',S)
    for k in range(0,4):
        for c in combinations(range(5),k):
            bs=set(c)
            for i in range(5):
                for j in range(5):
                    if i==j: continue
                    v=phi_pin(p,bs,i,j)
                    if v is not None and (best is None or v<best):
                        best=v; bestkey=('pin',bs,i,j)
    print(p, T, float(best/T), bestkey, float(a4))
