from fractions import Fraction as F
import itertools, random

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def c(n):
    return F(2**n, 2**(n+1)-1)

n = 6
target_c = float(c(n))

base = [0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,0.0128]

def best_subset_tie_all_i(p):
    k = len(p)
    best_overall = None
    per_i = []
    for i in range(k):
        pi = p[i]
        others = [p[m] for m in range(k) if m != i]
        best_T = 0
        for mask in range(1 << len(others)):
            s = sum(others[b] for b in range(len(others)) if mask & (1<<b))
            if s <= pi and s > best_T:
                best_T = s
        r = pi - best_T
        val = 0.5*(1+r)
        per_i.append(val)
        if best_overall is None or val < best_overall:
            best_overall = val
    return best_overall, per_i

# test the exact rounded point
bo, per_i = best_subset_tie_all_i(base)
print("rounded point: best over i =", bo, "c(n)=", target_c, "beats?", bo<=target_c)

random.seed(1)
results = []
for trial in range(2000):
    # perturb indices 1..6 (keep index0 as largest, roughly) by small noise, renormalize to sum 1, re-sort descending
    noise = [random.uniform(-3e-4,3e-4) for _ in range(7)]
    pert = [base[i]+noise[i] for i in range(7)]
    s = sum(pert)
    pert = [x/s for x in pert]
    pert.sort(reverse=True)
    if pert[-1] <= 0: 
        continue
    gaps_ok = all(pert[i]-pert[i+1] > 1/(2**(n+1)-1) for i in range(6))
    if not gaps_ok or pert[0]>=0.5:
        continue
    bo, _ = best_subset_tie_all_i(pert)
    results.append(bo)

print(f"perturbed trials kept: {len(results)}")
print(f"min over trials of (best-over-i) = {min(results):.6f}")
print(f"max over trials of (best-over-i) = {max(results):.6f}")
print(f"mean = {sum(results)/len(results):.6f}")
beats = sum(1 for v in results if v <= target_c)
print(f"fraction beating c(n)={target_c:.6f}: {beats}/{len(results)}")
