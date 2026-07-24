import random
from fractions import Fraction as F
from itertools import combinations

a4 = F(16,31)

def A(sorted_desc):
    s = F(0)
    for i,v in enumerate(sorted_desc):
        s += v if i%2==0 else -v
    return s

def phi_from_fragments(fragments):
    T = sum(fragments)
    sd = sorted(fragments, reverse=True)
    return (T + A(sd))/2

def phi_bisect_subset(p, S):
    frags = []
    for i in range(5):
        if i in S:
            frags += [p[i]/2, p[i]/2]
        else:
            frags += [p[i]]
    return phi_from_fragments(frags)

subsets = []
for k in range(1,5):
    for c in combinations(range(5), k):
        subsets.append(set(c))

def phi_pin(p, bisect_set, pin_i, pin_j):
    if pin_i in bisect_set or pin_j == pin_i:
        return None
    if p[pin_i] < p[pin_j]:
        return None
    frags = []
    for i in range(5):
        if i in bisect_set:
            frags += [p[i]/2, p[i]/2]
        elif i == pin_i:
            frags += [p[pin_j], p[pin_i]-p[pin_j]]
        else:
            frags += [p[i]]
    ncuts = len(bisect_set) + 1
    if ncuts > 4:
        return None
    return phi_from_fragments(frags)

def rand_marking_in_box(maxden=200):
    while True:
        vals = [random.randint(1,maxden) for _ in range(5)]
        vals.sort(reverse=True)
        p = [F(v) for v in vals]
        T = sum(p)
        if p[0] < T*F(1,2) and T*F(1,31) < p[1] < T*F(8,31):
            return p

random.seed(0)
from collections import Counter
winner_counter = Counter()
trials=0
N=20000
while trials<N:
    p = rand_marking_in_box()
    trials+=1
    T=sum(p)
    best = min(phi_bisect_subset(p,S) for S in subsets)
    if best <= a4*T:
        continue
    best_pin = None
    best_key=None
    for k in range(0,4):
        for c in combinations(range(5),k):
            bs = set(c)
            for i in range(5):
                for j in range(5):
                    if i==j: continue
                    v = phi_pin(p, bs, i, j)
                    if v is not None and (best_pin is None or v < best_pin):
                        best_pin = v
                        best_key = (frozenset(bs), i, j)
    if best_pin is not None and best_pin <= a4*T:
        winner_counter[best_key] += 1

print("num points needing a pin chamber:", sum(winner_counter.values()))
print("top winning (bisect_set,i,j) chambers:")
for k,v in winner_counter.most_common(15):
    print(k, v)
