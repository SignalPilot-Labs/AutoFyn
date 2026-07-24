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
    # bisect pieces in bisect_set; also cut piece pin_i into (p[pin_j], p[pin_i]-p[pin_j]) if p[pin_i]>=p[pin_j]
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
    # cut count: 2*|bisect_set| + 1 (for pin) must be <=4... actually pin uses 1 cut, bisect uses 1 cut per piece
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
trials=0
covered=0
covered_pin=0
N=20000
uncovered_after_pin=[]
while trials<N:
    p = rand_marking_in_box()
    trials+=1
    T=sum(p)
    best = min(phi_bisect_subset(p,S) for S in subsets)
    ok = best <= a4*T
    if ok:
        covered+=1
        covered_pin+=1
        continue
    # try pin chambers: bisect_set subset of size<=3 (leaving room for 1 pin cut), pin_i,pin_j any distinct indices not in bisect_set... actually pin_i could be in bisect? no exclude
    best_pin = best
    for k in range(0,4):
        for c in combinations(range(5),k):
            bs = set(c)
            for i in range(5):
                for j in range(5):
                    if i==j: continue
                    v = phi_pin(p, bs, i, j)
                    if v is not None and v < best_pin:
                        best_pin = v
    if best_pin <= a4*T:
        covered_pin += 1
    else:
        if len(uncovered_after_pin) < 5:
            uncovered_after_pin.append((p,T,best_pin))

print(f"trials={trials} covered_bisect_subset={covered} ({covered/trials*100:.2f}%) covered_with_pin={covered_pin} ({covered_pin/trials*100:.2f}%)")
for p,T,best in uncovered_after_pin:
    print([float(x/T) for x in p], float(best/T), float(a4))
