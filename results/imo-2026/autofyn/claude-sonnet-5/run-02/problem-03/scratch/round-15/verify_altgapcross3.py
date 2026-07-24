from fractions import Fraction as F
import random

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a
def phi(vals):
    return (sum(vals)+A(vals))/2

def try_build(p, j):
    """Attempt the j-fold Alternating Gap-Cross construction on sorted-desc p (len m).
       Returns None if infeasible (chain constraints can't be satisfied), else (final_multiset, predicted_A)."""
    m = len(p)
    j_eff = min(j, m//2)
    if j_eff == 0:
        tail = p[:]
        return list(tail), (A(tail) if tail else F(0)), 0
    # sequential construction with ceiling C (upper bound on next pair's larger fragment)
    C = None  # no ceiling for i=1
    frags = []  # list of (value,) in order, but we just need final multiset + legality
    a_list = []
    b_list = []
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        pa, pb = p[idx_a], p[idx_b]
        lo = max(pb, pa-pb)
        hi = pa if C is None else min(pa, C)
        if not (lo < hi):
            return None  # infeasible
        # choose a_i close to lo to maximize b_i (room for next pair / tail)
        a_i = lo + (hi-lo)*F(1,1000)
        b_i = pa - a_i
        a_list.append(a_i); b_list.append(b_i)
        C = b_i
    # final tail interface check: b_j (=C) must exceed tail's max (p_{2j_eff+1}) if tail nonempty
    tail = p[2*j_eff:]
    if tail:
        if not (C > tail[0]):
            return None
    # build final multiset
    final = []
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        final.append(a_list[i-1]); final.append(p[idx_b]); final.append(b_list[i-1])
    final.extend(tail)
    # predicted A: gap sum with alternating sign, tail sign flip depends on parity of 3*j_eff
    gap_sum = F(0); sign=1
    for i in range(1,j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        gap_sum += sign*(p[idx_a]-p[idx_b]); sign=-sign
    tail_A = A(tail) if tail else F(0)
    shift = 3*j_eff
    tail_sign = 1 if shift % 2 == 0 else -1
    predicted_A = gap_sum + tail_sign*tail_A
    return final, predicted_A, j_eff

random.seed(3)
feasible=0; infeasible=0; mismatches=0
for _ in range(10000):
    m = random.randint(1,10)
    p = sorted([F(random.randint(1,60), random.randint(1,15)) for _ in range(m)], reverse=True)
    j = random.randint(0, (m//2)+1)
    res = try_build(p,j)
    if res is None:
        infeasible+=1
        continue
    final, predicted_A, j_eff = res
    actual_A = A(final)
    if actual_A != predicted_A:
        mismatches += 1
        print("MISMATCH", p, j, actual_A, predicted_A)
    else:
        feasible += 1
print(f"feasible & matched: {feasible}, infeasible(skipped): {infeasible}, mismatches: {mismatches}")

# Re-verify against the two round-14 witnesses using this general function
print("\n--- round-14 witness checks ---")
def normalize(vals):
    T = sum(vals)
    return [F(x)/T for x in vals]

w3 = [F(4468,10000),F(2591,10000),F(2251,10000),F(691,10000)]
w3 = normalize(w3)
w4 = [F(2933,10000),F(2514,10000),F(2131,10000),F(1338,10000),F(1085,10000)]
w4 = normalize(w4)

for name,p,j,target in [("n=3 witness (j=2)", w3, 2, F(8,15)), ("n=4 witness (j=1, expect fail since it's a pinned-tie not gap-cross)", w4, 1, F(16,31))]:
    res = try_build(p, j)
    if res is None:
        print(name, "-> infeasible for this j")
        continue
    final, predicted_A, j_eff = res
    Phi = phi(final)
    print(name, "Phi=", Phi, float(Phi), "target a_nT=", float(target), "closes:", Phi<target)
