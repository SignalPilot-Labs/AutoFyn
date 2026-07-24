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

def build_and_check(p, j):
    m = len(p)
    j_eff = min(j, m//2)
    final = []
    cuts_used = 0
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        pa, pb = p[idx_a], p[idx_b]
        if pa == pb:
            final.append(pa); final.append(pb)
            continue
        lo = max(pb, pa-pb)
        hi = pa
        assert lo < hi, (pa,pb,lo,hi)
        f = (lo+hi)/2
        f1, f2 = f, pa-f
        final.append(f1); final.append(f2); final.append(pb)
        cuts_used += 1
    tail_start = 2*j_eff
    tail = p[tail_start:]
    final.extend(tail)
    Phi = phi(final)
    gap_sum = F(0)
    sign = 1
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        gap_sum += sign*(p[idx_a]-p[idx_b])
        sign = -sign
    tail_A = A(tail) if tail else F(0)
    predicted_A = gap_sum + tail_A
    predicted_Phi = (sum(p) + predicted_A)/2
    return Phi, predicted_Phi, cuts_used, j_eff

random.seed(7)
trials = 0
for _ in range(6000):
    m = random.randint(1,10)
    p = sorted([F(random.randint(1,60), random.randint(1,15)) for _ in range(m)], reverse=True)
    j = random.randint(0, (m//2)+2)
    Phi, predicted_Phi, cuts, j_eff = build_and_check(p, j)
    assert Phi == predicted_Phi, (p,j,Phi,predicted_Phi)
    assert cuts <= j_eff <= m-1 if m>=1 else True
    trials += 1
print(f"Alternating Gap-Cross identity verified exactly on {trials} random (m,j) trials, zero mismatches.")
print(f"cut budget check: cuts_used <= j_eff <= floor(m/2) <= n=m-1, always satisfied.")
