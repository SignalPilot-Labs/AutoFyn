from fractions import Fraction as F
import itertools, random

a3 = F(8,15)

def bisect_subset_phi(p, S):
    idx = [i for i in range(4) if i not in S]
    R = [p[i] for i in idx]
    # alternating sum A(R): ranks in descending order (already sorted since p sorted desc and idx increasing)
    A = sum((F(1) if k%2==0 else F(-1))*v for k,v in enumerate(R))
    return (F(1)+A)/2

subsets = []
for r in range(0,4):
    for S in itertools.combinations(range(4), r):
        subsets.append(set(S))

def all_chambers(p):
    p1,p2,p3,p4 = p
    chambers = []  # (name, feasible(bool), phi)
    for S in subsets:
        phi = bisect_subset_phi(p, S)
        chambers.append((f"bisect{sorted(S)}", True, phi))
    # Double-Sandwich-Below
    feas = (p3 + p4/2 < p1) and (p1 < p2+p3)
    chambers.append(("DS-Below", feas, p2+p3+p4/2))
    # Double-Sandwich-Above
    feas = p1 > p2+p3
    chambers.append(("DS-Above", feas, p1+p4/2))
    # Triple-Pin
    feas = p1 > p2+p3
    chambers.append(("TriplePin", feas, F(1)-p1))
    # Chamber B1
    feas = (p2+p3-p4 < p1) and (p1 < p2+p3)
    chambers.append(("B1", feas, p1+p4))
    # Chamber B2
    feas = (p2 <= p1) and (p1 < p2+p3-p4)
    chambers.append(("B2", feas, p2+p3))
    # P1P2-tied-to-p3
    feas = p2 >= 2*p3
    chambers.append(("P1P2p3", feas, p1+p3))
    # Chamber-R22.1.1
    feas = (p1 >= 2*p3) and (p2 <= p3+p4)
    chambers.append(("R22.1.1", feas, p1/2+p3+p4))
    # Chamber A
    feas = (p1 >= 3*p4) and (p1 <= 2*p3+p4)
    chambers.append(("A", feas, p2+(p1+p4)/2))
    # Chamber A2
    feas = (p1 <= p2+2*p4)
    chambers.append(("A2", feas, (p1+p2)/2+p3))
    return chambers

def covered(p, exclude=set()):
    chambers = all_chambers(p)
    winners = []
    for name, feas, phi in chambers:
        if name in exclude: continue
        if feas and (a3 - phi) >= 0:
            winners.append(name)
    return winners

random.seed(1)
pts = []
# deterministic-ish grid using Fractions
N = 40
for i in range(1, N):
    p1 = F(1,2) * F(i, N)
    for j in range(1, N):
        p2 = F(1,15) + F(3,15) * F(j, N)
        if p2 > p1: continue
        rem = 1 - p1 - p2
        if rem <= 0: continue
        for k in range(1, 20):
            p3 = rem * F(k, 20)
            p4 = rem - p3
            if not (p1>=p2>=p3>=p4>0): continue
            pts.append((p1,p2,p3,p4))

print("num points", len(pts))

uncovered = 0
chamber_usage = {}
unique_needed = {}
for p in pts:
    winners = covered(p)
    if not winners:
        uncovered += 1
    for w in winners:
        chamber_usage[w] = chamber_usage.get(w,0)+1
    if len(winners) == 1:
        unique_needed[winners[0]] = unique_needed.get(winners[0], 0) + 1

print("uncovered:", uncovered)
print("chamber usage counts (top 25):")
for k,v in sorted(chamber_usage.items(), key=lambda x:-x[1])[:25]:
    print(f"  {k}: {v}")
print()
print("chambers that were the UNIQUE cover for some point (i.e. load-bearing, cannot drop):")
for k,v in sorted(unique_needed.items(), key=lambda x:-x[1]):
    print(f"  {k}: unique-cover count {v}")

all_names = set(x[0] for x in all_chambers(pts[0]))
never_unique = all_names - set(unique_needed.keys())
print()
print("chambers NEVER the unique cover on this sample (candidates for redundancy):", sorted(never_unique))

print()
print("=== Greedy minimal set cover on this sample ===")
remaining = set(range(len(pts)))
point_winners = [set(covered(p)) for p in pts]
chosen = []
while remaining:
    best = None; best_count = -1
    for name in all_names:
        cnt = sum(1 for i in remaining if name in point_winners[i])
        if cnt > best_count:
            best_count = cnt; best = name
    if best_count == 0:
        break
    chosen.append((best, best_count))
    remaining = {i for i in remaining if best not in point_winners[i]}
print("greedy chosen chambers (in order), remaining uncovered:", len(remaining))
for c in chosen:
    print(" ", c)
