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

def a_n(n):
    return F(2**n, 2**(n+1)-1)
def D_n(n):
    return 2**(n+1)-1

def bisect_top_k_bound(p, n):
    # returns min over k=0..n of (T+p_{k+1})/2 , i.e. covered if <= a_n*T for some k
    T = sum(p)
    m = len(p)
    an = a_n(n)
    for k in range(0, n+1):
        pk1 = p[k] if k < m else F(0)
        if pk1 <= T/D_n(n):
            return True
    return False

def try_build(p, j):
    m = len(p)
    j_eff = min(j, m//2)
    if j_eff == 0:
        tail = p[:]
        return list(tail), (A(tail) if tail else F(0)), 0
    C = None
    a_list = []; b_list = []
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        pa, pb = p[idx_a], p[idx_b]
        lo = max(pb, pa-pb)
        hi = pa if C is None else min(pa, C)
        if not (lo < hi):
            return None
        a_i = lo + (hi-lo)*F(1,1000)
        b_i = pa - a_i
        a_list.append(a_i); b_list.append(b_i)
        C = b_i
    tail = p[2*j_eff:]
    if tail:
        if not (C > tail[0]):
            return None
    final = []
    for i in range(1, j_eff+1):
        idx_a, idx_b = 2*i-2, 2*i-1
        final.append(a_list[i-1]); final.append(p[idx_b]); final.append(b_list[i-1])
    final.extend(tail)
    return final, None, j_eff

def altgapcross_covers(p, n):
    T = sum(p)
    an = a_n(n)
    m = len(p)
    for j in range(0, m//2+1):
        res = try_build(p, j)
        if res is None:
            continue
        final, _, j_eff = res
        Phi = phi(final)
        if Phi <= an*T:
            return True
    return False

def sample_case_b2(n, rng):
    # marking with m=n+1 pieces, p1<T/2, T/D_n<p2<a_n*T/2
    m = n+1
    an = a_n(n); Dn = D_n(n)
    while True:
        # sample random positive values, normalize T=1
        raw = [F(rng.randint(1,1000)) for _ in range(m)]
        raw.sort(reverse=True)
        T = sum(raw)
        p = [x/T for x in raw]
        p1,p2 = p[0],p[1]
        if p1 < F(1,2) and F(1,Dn) < p2 < an/2:
            return p

rng = random.Random(123)
for n in [3,4,5]:
    total=0; cov_bisect=0; cov_union=0
    trials = 40
    got=0
    attempts=0
    while got < trials and attempts < 200000:
        attempts += 1
        p = sample_case_b2(n, rng)
        got += 1
        b = bisect_top_k_bound(p, n)
        u = b or altgapcross_covers(p, n)
        total += 1
        cov_bisect += int(b)
        cov_union += int(u)
    print(f"n={n}: samples={total}, BisectTopK-only covered={cov_bisect} ({100*cov_bisect/total:.1f}%), "
          f"BisectTopK UNION AltGapCross covered={cov_union} ({100*cov_union/total:.1f}%)")
