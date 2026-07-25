import random
from fractions import Fraction as F

def oddsum(ms):
    s = sorted(ms, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def rand_frac(rng, lo, hi, denom=997):
    lo=F(lo); hi=F(hi)
    if hi<=lo: return lo
    t=F(rng.randint(0,denom),denom)
    return lo+t*(hi-lo)

def split_value_n(rng, value, n, style=None):
    """split value into exactly n positive parts (n-1 cuts)."""
    value=F(value)
    if n==1: return [value]
    if style is None:
        style = rng.choice(['equal','unequal'])
    if style=='equal':
        return [value/n]*n
    cuts = sorted(rand_frac(rng,0,1) for _ in range(n-1))
    pts=[F(0)]+cuts+[F(1)]
    parts=[value*(pts[i+1]-pts[i]) for i in range(n)]
    # ensure positivity; if any zero, nudge (rare with denom=997)
    parts=[p if p>0 else F(1,10**6) for p in parts]
    return parts

def gen_dominance_chain(rng, level, k, total):
    if k==0: return []
    if k==1: return [F(total)]
    lo = F(2)**(level-1) if level>=0 else F(0)
    total=F(total)
    hi=total
    if lo>=hi:
        a1=hi*F(999,1000)
    else:
        a1=rand_frac(rng, lo, hi*F(999,1000))
    rest=total-a1
    return [a1]+gen_dominance_chain(rng, level-1, k-1, rest)

def test_B_budgeted(rng, m, k, cut_budget):
    """m,k given; cut_budget = total cuts allowed for the WHOLE original response
       (|B|-1)+(sum|S_i|-1). B has k pieces -> k-1 cuts already spent on top.
       Remaining tail budget = cut_budget-(k-1), to be spent across m levels
       (level m-1's split (>=1 piece, i.e. >=0 extra cuts... but here level m-1
       is split into {mu1}+R1, so |that level's pieces|=1+|R1|), levels
       m-2..m-k unsplit (0 cuts, forced), levels 0..m-k-1 arbitrary."""
    kdd = k-2
    tail_budget = cut_budget - (k-1)
    if tail_budget < 0: return None
    # level m-1 needs >=1 piece for R1 (i.e. total >=2 pieces there: mu1+R1, R1 nonempty
    # per Level-Absorption's own framing) -- but R1 could in principle be empty (L=0);
    # we test the genuinely split case R1 nonempty, needing >=1 cut there.
    if tail_budget < 1: return None
    # distribute tail_budget cuts across: level m-1 (>=1), levels 0..m-k-1 (>=0 each)
    n_free_levels = max(0, m-k)  # levels 0..m-k-1
    cuts_top_tail = rng.randint(1, tail_budget)  # cuts spent on level m-1 (R1 has cuts_top_tail pieces... )
    remaining = tail_budget - cuts_top_tail
    # distribute `remaining` cuts among n_free_levels levels (stars and bars), each level's
    # piece count = 1+cuts_at_that_level
    level_cuts = [0]*n_free_levels
    for _ in range(remaining):
        if n_free_levels==0: break
        level_cuts[rng.randrange(n_free_levels)] += 1

    Bsum = rand_frac(rng, F(1,1000), F(2)**(m-2)) if kdd>0 else F(0)
    Bpp = gen_dominance_chain(rng, m-2, kdd, Bsum)
    lo_b2 = F(2)**(m-2)
    hi_b2 = F(2)**(m-1) - sum(Bpp)
    if hi_b2 <= lo_b2: return None
    b2 = rand_frac(rng, lo_b2, hi_b2)
    if b2<=0: return None
    mu1 = rand_frac(rng, 0, b2*F(999,1000))
    top = F(2)**(m-1)
    Lrest = top-mu1
    nR1 = cuts_top_tail  # R1 has cuts_top_tail pieces (level m-1 split into 1+cuts_top_tail total incl mu1)
    R1 = split_value_n(rng, Lrest, nR1)
    Spp=[]
    for i in range(m-2, m-k-1, -1):
        Spp.append(F(2)**i)  # unsplit forced levels
    for idx,i in enumerate(range(m-k-1, -1, -1)):
        n = 1+level_cuts[idx]
        Spp.extend(split_value_n(rng, F(2)**i, n))
    lhs = oddsum(Bpp+[mu1]+R1+Spp)
    target = b2+sum(Bpp)
    total_cuts_used = (k-1) + cuts_top_tail + sum(level_cuts)
    assert total_cuts_used <= cut_budget
    return lhs>=target-F(1,10**12), lhs, target, m, k, Bpp, b2, mu1, R1, Spp, total_cuts_used

def run_B(n_trials, seed=0):
    rng=random.Random(seed)
    fails=[]
    tested=0
    tight=[]
    for _ in range(n_trials):
        m = rng.randint(3,9)
        k = rng.randint(2,m)
        r = test_B_budgeted(rng, m, k, cut_budget=m)
        if r is None: continue
        tested+=1
        ok, lhs, target, *_ = r
        margin = lhs-target
        if not ok:
            fails.append(r)
        elif margin < F(1,1000):
            tight.append((margin,r))
    return tested, fails, tight

if __name__=='__main__':
    tested, fails, tight = run_B(30000, seed=7)
    print('Sub-Problem B (Level-Absorption), BUDGET-RESPECTING (cuts<=m):')
    print('tested=',tested,'fails=',len(fails))
    for f in fails[:5]:
        print(f)
    tight.sort(key=lambda x:x[0])
    print('tightest margins:', [float(t[0]) for t in tight[:8]])
