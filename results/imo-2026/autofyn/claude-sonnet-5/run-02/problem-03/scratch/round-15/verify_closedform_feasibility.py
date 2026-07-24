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

def closed_form_feasible(p, j):
    m = len(p)
    j_eff = min(j, m//2)
    if j_eff == 0:
        return True, 0
    gamma_prev = None  # C_0 = +inf
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        pa, pb = p[idx_a], p[idx_b]
        if not (pa > pb):
            return False, i
        floor_i = max(pb, pa-pb)
        if gamma_prev is not None and not (gamma_prev > floor_i):
            return False, i
        gamma_i = min(pa-pb, pb)
        gamma_prev = gamma_i
    tail = p[2*j_eff:]
    if tail and not (gamma_prev > tail[0]):
        return False, j_eff+1
    return True, j_eff

def try_build(p, j):
    m = len(p)
    j_eff = min(j, m//2)
    if j_eff == 0:
        tail = p[:]
        return list(tail), 0
    C = None
    a_list=[]; b_list=[]
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        pa, pb = p[idx_a], p[idx_b]
        lo = max(pb, pa-pb); hi = pa if C is None else min(pa,C)
        if not (lo<hi): return None
        a_i = lo + (hi-lo)*F(1,1000)
        b_i = pa-a_i
        a_list.append(a_i); b_list.append(b_i)
        C = b_i
    tail = p[2*j_eff:]
    if tail and not (C > tail[0]): return None
    final=[]
    for i in range(1,j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        final.append(a_list[i-1]); final.append(p[idx_b]); final.append(b_list[i-1])
    final.extend(tail)
    return final

random.seed(99)
match=0; mismatch=0
for _ in range(8000):
    m = random.randint(1,10)
    p = sorted([F(random.randint(1,60),random.randint(1,15)) for _ in range(m)], reverse=True)
    j = random.randint(0,(m//2)+1)
    cf_feas, _ = closed_form_feasible(p,j)
    built = try_build(p,j)
    greedy_feas = built is not None
    if cf_feas == greedy_feas:
        match+=1
    else:
        mismatch+=1
        print("MISMATCH", p, j, cf_feas, greedy_feas)
print(f"closed-form feasibility vs greedy-construction feasibility: match={match} mismatch={mismatch}")
