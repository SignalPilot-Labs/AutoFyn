import random
from fractions import Fraction as F

def oddsum(multiset):
    s = sorted(multiset, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def evensum(multiset):
    s = sorted(multiset, reverse=True)
    return sum(s[i] for i in range(1, len(s), 2))

def rand_frac(rng, lo, hi, denom=997):
    # random rational in [lo,hi]
    lo = F(lo); hi = F(hi)
    if hi <= lo:
        return lo
    t = F(rng.randint(0, denom), denom)
    return lo + t*(hi-lo)

def split_value(rng, value, style=None):
    """Split a positive value into a multiset of positive fractions summing to it.
       style: 'unsplit','two_unequal','many_equal','many_unequal','random'"""
    value = F(value)
    if value == 0:
        return []
    if style is None:
        style = rng.choice(['unsplit','two_unequal','many_equal','many_unequal','random'])
    if style == 'unsplit':
        return [value]
    if style == 'two_unequal':
        frac = rand_frac(rng, F(1,1000), F(999,1000))
        a = value*frac
        b = value-a
        return [a,b] if a>0 and b>0 else [value]
    if style == 'many_equal':
        n = rng.randint(2,8)
        return [value/n]*n
    if style == 'many_unequal':
        n = rng.randint(2,7)
        # random composition
        cuts = sorted(rand_frac(rng,0,1) for _ in range(n-1))
        pts = [F(0)] + cuts + [F(1)]
        parts = [value*(pts[i+1]-pts[i]) for i in range(n)]
        parts = [p for p in parts if p>0]
        return parts if parts else [value]
    if style == 'random':
        n = rng.randint(1,10)
        if n==1: return [value]
        cuts = sorted(rand_frac(rng,0,1) for _ in range(n-1))
        pts = [F(0)] + cuts + [F(1)]
        parts = [value*(pts[i+1]-pts[i]) for i in range(n)]
        parts = [p for p in parts if p>0]
        return parts if parts else [value]

def build_refinement(rng, top_level, k_clear, style=None):
    """Refinement S of Gamma_{top_level} (levels top_level..0), with top k_clear
       levels (top_level, top_level-1, ..., top_level-k_clear+1) unsplit,
       remaining levels (top_level-k_clear .. 0) split arbitrarily.
       Returns flat list of fragment values."""
    elems = []
    for i in range(top_level, -1, -1):
        if i > top_level - k_clear:
            elems.append(F(2)**i)
        else:
            elems.extend(split_value(rng, F(2)**i, style))
    return elems

def gen_dominance_chain(rng, level, k, total):
    """length-k descending positive sequence with Dominance-Chain property at `level`,
       exact sum = total. Requires total feasible: recursively a1>=2^(level-1)."""
    if k == 0:
        return []
    if k == 1:
        return [F(total)]
    lo = F(2)**(level-1) if level>=0 else F(0)
    total = F(total)
    assert total > lo*0  # sanity
    # a1 in [lo, total), leave rest>0 for k-1 remaining elements (level-1 chain)
    # rest must itself be expressible: just recurse, no strict upper constraint beyond total
    hi = total  # a1 can be up to total (leaving rest ~0), but need rest>0 strictly and a1>=lo
    if lo >= hi:
        a1 = hi  # degenerate; will produce near-zero rest, adjust
        a1 = hi * F(999,1000) if hi>0 else F(0)
    else:
        a1 = rand_frac(rng, lo, hi*F(999,1000))
    rest = total - a1
    tail = gen_dominance_chain(rng, level-1, k-1, rest)
    return [a1]+tail

def test_A(rng, trial_style=None):
    m = rng.randint(2,7)
    kp = rng.randint(1, m-1)  # k' = k-1, Theorem7 instance params (m-1,kp)
    if kp < 1: return None
    # B' dominance chain at level m-1, length kp, sum <= 2^(m-1)
    Bsum = rand_frac(rng, F(1,1000), F(2)**(m-1))
    Bp = gen_dominance_chain(rng, m-1, kp, Bsum)
    Bp.sort(reverse=True)
    b2 = Bp[0]
    Sp = sum(Bp)
    # S'' refinement of Gamma_{m-2}, top (kp-1) levels unsplit
    Spp = build_refinement(rng, m-2, kp-1, style=trial_style)
    # sanity: Theorem 7 holds
    lhs_thm7 = oddsum(Bp+Spp)
    assert lhs_thm7 >= Sp - F(1,10**9), f"Theorem7 sanity fail m={m} kp={kp}"
    # mu1 in [b2, 2^(m-1)]
    top = F(2)**(m-1)
    if b2 > top: return None
    mu1 = rand_frac(rng, b2, top)
    L = top - mu1
    R1 = split_value(rng, L, style=trial_style)
    lhs = oddsum(Bp+Spp+R1)
    ok = lhs >= Sp - F(1,10**12)
    return ('A', m, kp, ok, lhs, Sp, Bp, mu1, L, R1)

def test_B(rng, trial_style=None):
    m = rng.randint(3,8)
    k = rng.randint(2, m)  # need k<=m and k-2>=0, level m-k>=0 for S'' bottom
    kdd = k-2
    # B'' dominance chain at level m-2, length kdd, sum <= 2^(m-2)
    Bsum = rand_frac(rng, F(1,1000), F(2)**(m-2)) if kdd > 0 else F(0)
    Bpp = gen_dominance_chain(rng, m-2, kdd, Bsum)
    # b2 >= 2^(m-2), and b2 + sum(Bpp) <= 2^(m-1) (chain B'={b2}+B'' sum<=2^(m-1))
    lo_b2 = F(2)**(m-2)
    hi_b2 = F(2)**(m-1) - Bsum
    if hi_b2 <= lo_b2: return None
    b2 = rand_frac(rng, lo_b2, hi_b2)
    # mu1 < b2
    if b2 <= 0: return None
    mu1 = rand_frac(rng, 0, b2*F(999,1000))
    top = F(2)**(m-1)
    Lrest = top - mu1
    R1 = split_value(rng, Lrest, style=trial_style)
    # S'' refinement of Gamma_{m-2}: levels m-2..m-k unsplit (k-1 levels), levels 0..m-k-1 arbitrary
    Spp = build_refinement(rng, m-2, k-1, style=trial_style)
    lhs = oddsum(Bpp+[mu1]+R1+Spp)
    target = b2 + sum(Bpp)   # ground truth: actual sum of B'', not the (possibly unused) Bsum draw
    ok = lhs >= target - F(1,10**12)
    return ('B', m, k, ok, lhs, target, Bpp, b2, mu1, R1, Spp)

def run(n_trials, testfn, seed=0):
    rng = random.Random(seed)
    styles = [None,'unsplit','two_unequal','many_equal','many_unequal','random']
    fails = []
    tested = 0
    tight = []
    for i in range(n_trials):
        style = styles[i % len(styles)]
        try:
            r = testfn(rng, trial_style=style)
        except AssertionError as e:
            print("ASSERTION FAIL:", e)
            continue
        if r is None: continue
        tested += 1
        ok = r[3]
        margin = r[4]-r[5]
        if not ok:
            fails.append(r)
        elif margin < F(1,1000):
            tight.append((margin, r))
    return tested, fails, tight

if __name__ == '__main__':
    print("=== Sub-Problem A (Insertion-Robustness) ===")
    tested, fails, tight = run(20000, test_A, seed=1)
    print(f"tested={tested} fails={len(fails)}")
    if fails:
        for f in fails[:5]:
            print("FAIL:", f)
    tight.sort(key=lambda x: x[0])
    print("tightest 5 margins:", [(float(t[0])) for t in tight[:5]])

    print("=== Sub-Problem B (Level-Absorption) ===")
    tested, fails, tight = run(20000, test_B, seed=2)
    print(f"tested={tested} fails={len(fails)}")
    if fails:
        for f in fails[:5]:
            print("FAIL:", f)
    tight.sort(key=lambda x: x[0])
    print("tightest 5 margins:", [(float(t[0])) for t in tight[:5]])
