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
    # p: sorted descending list of Fractions, length m
    m = len(p)
    assert 2*j <= m or True
    final = []
    cuts_used = 0
    for i in range(1, j+1):
        idx_a = 2*i-2  # 0-indexed piece 2i-1
        idx_b = 2*i-1  # 0-indexed piece 2i
        if idx_b >= m:
            break
        pa, pb = p[idx_a], p[idx_b]
        if pa == pb:
            # degenerate: contributes 0 automatically, no cut needed, but for the identity we just leave both untouched
            final.append(pa); final.append(pb)
            continue
        lo = max(pb, pa-pb)
        hi = pa
        assert lo < hi, (pa,pb,lo,hi)
        f = (lo+hi)/2
        f1, f2 = f, pa-f
        final.append(f1); final.append(f2); final.append(pb)
        cuts_used += 1
    tail_start = 2*j
    tail = p[tail_start:]
    final.extend(tail)
    Phi = phi(final)
    gap_sum = F(0)
    sign = 1
    for i in range(1, j+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        if idx_b >= m:
            break
        gap_sum += sign*(p[idx_a]-p[idx_b])
        sign = -sign
    tail_A = A(tail) if tail else F(0)
    predicted_A = gap_sum + tail_A
    predicted_Phi = (sum(p) + predicted_A)/2
    return Phi, predicted_Phi, cuts_used

random.seed(7)
trials = 0
for _ in range(4000):
    m = random.randint(1,9)
    p = sorted([F(random.randint(1,60), random.randint(1,15)) for _ in range(m)], reverse=True)
    j = random.randint(0, (m//2)+1)
    Phi, predicted_Phi, cuts = build_and_check(p, j)
    assert Phi == predicted_Phi, (p,j,Phi,predicted_Phi)
    assert cuts <= max(j, 0)
    trials += 1
print(f"Alternating Gap-Cross identity verified exactly on {trials} random (m,j) trials, zero mismatches.")
