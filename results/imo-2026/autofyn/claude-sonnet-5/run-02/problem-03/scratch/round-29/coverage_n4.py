import random
from fractions import Fraction as F
from itertools import combinations

a4 = F(16,31)
D4 = 31

def A(sorted_desc):
    # alternating sum, sorted descending, odd positions (1-indexed) plus, even minus
    s = F(0)
    for i,v in enumerate(sorted_desc):
        if i % 2 == 0:
            s += v
        else:
            s -= v
    return s

def phi_S(p, S):
    # p: list of 5 Fractions sorted descending (p1..p5), S: subset of indices {0..4} (0-indexed) to bisect
    R = [p[i] for i in range(5) if i not in S]
    R_sorted = sorted(R, reverse=True)
    T = sum(p)
    return (T + A(R_sorted))/2

# all subsets of size 1..4 of {0,1,2,3,4}
subsets = []
for k in range(1,5):
    for c in combinations(range(5), k):
        subsets.append(set(c))
print("num chambers:", len(subsets))

def rand_marking_in_box(maxden=200):
    # generate random p1>=p2>=p3>=p4>=p5>0 with p1<T/2, T/31<p2<8T/31
    while True:
        # random positive integers, then sort, normalize
        vals = [random.randint(1,maxden) for _ in range(5)]
        vals.sort(reverse=True)
        p = [F(v) for v in vals]
        T = sum(p)
        if p[0] < T*F(1,2) and T*F(1,31) < p[1] < T*F(8,31):
            return p

random.seed(0)
trials = 0
covered = 0
uncovered_examples = []
N = 20000
while trials < N:
    p = rand_marking_in_box()
    trials += 1
    T = sum(p)
    best = min(phi_S(p,S) for S in subsets)
    if best <= a4*T:
        covered += 1
    else:
        if len(uncovered_examples) < 8:
            uncovered_examples.append((p, T, best))

print(f"trials={trials} covered={covered} coverage={covered/trials*100:.2f}%")
print("uncovered examples (p, T, best_phi, a4*T):")
for p,T,best in uncovered_examples:
    print(p, T, best, a4*T, float(best/T))

print("\nratios of uncovered examples (p1/T,p2/T,p3/T,p4/T,p5/T):")
for p,T,best in uncovered_examples:
    print([float(x/T) for x in p])
