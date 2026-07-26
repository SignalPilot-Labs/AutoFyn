import sys
from fractions import Fraction as F
import itertools, random

def D_value(pieces):
    """D = alternating sum of descending sort = S_odd - S_even."""
    s = sorted(pieces, reverse=True)
    return sum(s[i] if i % 2 == 0 else -s[i] for i in range(len(s)))

def f2(pieces):
    """n=2 menu on a 3-piece multiset (any total T).
    menu = {c, |2a-T|, a-b, b-c} with a>=b>=c sorted, T=a+b+c.
    Each realized by an explicit <=2-mark strategy."""
    a, b, c = sorted(pieces, reverse=True)
    T = a + b + c
    return min(c, abs(2*a - T), a - b, b - c)

def f3(pieces):
    """n=3 construction (Theorem 6): min over ALL peels (i,j) i<j of f2(rest).
    rest after peeling p_i -> p_j + (p_i - p_j): {p_i - p_j} U {p_k: k!=i,j}."""
    ps = sorted(pieces, reverse=True)  # work with sorted; peels by position
    best = None
    n = len(ps)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if ps[i] < ps[j]: continue  # need p_i >= p_j (sorted so i<j works)
            rest = [ps[i] - ps[j]] + [ps[k] for k in range(n) if k != i and k != j]
            val = f2(rest)
            if best is None or val < best:
                best = val
    return best

def f4(pieces):
    """n=4 construction: min over ALL peels of f3(rest_4piece)."""
    ps = sorted(pieces, reverse=True)
    best = None
    n = len(ps)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if ps[i] < ps[j]: continue
            rest = [ps[i] - ps[j]] + [ps[k] for k in range(n) if k != i and k != j]
            val = f3(rest)
            if best is None or val < best:
                best = val
    return best

# n=4 constants
D4 = 31
target = F(1, D4)
g3 = F(8, D4)   # = 8/31, the Lemma-5 threshold
g0 = F(1, D4)
dyadic = [F(16, D4), F(8, D4), F(4, D4), F(2, D4), F(1, D4)]

print("target 1/31 =", float(target))
print("dyadic =", [float(x) for x in dyadic], "sum", float(sum(dyadic)))
print("f4(dyadic) =", f4(dyadic), "=", float(f4(dyadic)), " (should equal 1/31)")
print("f3(dyadic[1:]) on rest? sanity")
sys.stdout.flush()

# Verify the dyadic vertex: f4 should be exactly 1/31
assert f4(dyadic) == target, f"dyadic f4 != 1/31: {f4(dyadic)}"
print("ASSERT dyadic f4 == 1/31: PASS")
sys.stdout.flush()

# Very-flat polytope Pi_4:
# p1>=p2>=p3>=p4>=p5, sum=1, p2,p3,p4 < 8/31, p5 > 1/31
# (p5 < 8/31 automatic since p5<=p4<8/31)
# Gap param: w=p5, z=p4-p5, y=p3-p4, x=p2-p3, u=p1-p2
# Box from strict constraints (computed below).

worst_val = None
worst_cfg = None
worst_is_dyadic = False
n_grid = 0
n_escape = 0
n_escape_configs = []

# Grid search: grid p2,p3,p4,p5 in fractions with denominator 31*K, enforce constraints.
# Use K such that grid is ~ 12^4 = 20736. Step = 1/(31*12) = 1/372.
K = 12
den = D4 * K  # 372
steps = [F(i, den) for i in range(den + 1)]

# To keep it fast, iterate p5, p4, p3, p2 with pruning
import time
t0 = time.time()
# Precompute candidate p5 values in (1/31, 8/31)
p5_cands = [s for s in steps if s > g0 and s < g3]
print("p5 candidates:", len(p5_cands))
sys.stdout.flush()

for p5 in p5_cands:
    rem4 = F(1) - p5
    # p4 in [p5, 8/31) and p4 <= rem4/4 (since p4>=p5 and p2,p3>=p4, p2,p3,p4<8/31)
    p4_cands = [s for s in steps if s >= p5 and s < g3 and s <= rem4]
    for p4 in p4_cands:
        rem3 = rem4 - p4
        p3_cands = [s for s in steps if s >= p4 and s < g3 and s <= rem3]
        for p3 in p3_cands:
            rem2 = rem3 - p3
            p2_cands = [s for s in steps if s >= p3 and s < g3 and s <= rem2]
            for p2 in p2_cands:
                p1 = rem2 - p2
                if p1 < p2: continue  # sort
                # very-flat check (p2,p3,p4<8/31 already enforced; p5>1/31 enforced)
                cfg = [p1, p2, p3, p4, p5]
                n_grid += 1
                v = f4(cfg)
                if worst_val is None or v > worst_val:
                    worst_val = v
                    worst_cfg = cfg[:]
                    worst_is_dyadic = (cfg == dyadic)
                if v > target + F(1, 10000):  # strict escape (allow tiny rational noise)
                    n_escape += 1
                    if len(n_escape_configs) < 20:
                        n_escape_configs.append((cfg[:], v))
                if n_grid % 2000 == 0:
                    print(f"  grid {n_grid} t={time.time()-t0:.1f}s worst={float(worst_val):.5f} esc={n_escape}")
                    sys.stdout.flush()

print("GRID DONE:", n_grid, "configs, t=", round(time.time()-t0,1),"s")
print("worst_val =", worst_val, "=", float(worst_val), " target=", float(target))
print("worst_cfg =", [float(x) for x in worst_cfg], " is_dyadic=", worst_is_dyadic)
print("worst_cfg exact =", [str(x) for x in worst_cfg])
print("escapes:", n_escape)
for c, v in n_escape_configs[:10]:
    print("  ESC cfg=", [float(x) for x in c], "v=", float(v), "exact v=", str(v))
sys.stdout.flush()

# Random search
random.seed(12345)
n_rand = 0
for _ in range(8000):
    # sample p2,p3,p4,p5 uniformly-ish in very-flat, p1=1-sum, enforce sort + constraints
    # sample 5 fractions summing to 1, sorted, p5>1/31, p2,p3,p4<8/31
    for _try in range(50):
        # random gaps
        xs = [random.random() for _ in range(5)]
        s = sum(xs)
        ps = sorted([F(round(x*den))/den for x in xs], reverse=True)  # rough
        # rescale to sum 1 with denominator
        tot = sum(ps)
        if tot == 0: continue
        ps = [p/tot for p in ps]
        # quantize to den
        ps2 = []
        # use raw fractions from random numerators summing to den
        nums = sorted([random.randint(1, den-1) for _ in range(5)], reverse=True)
        if sum(nums) != den:
            continue
        ps = [F(num, den) for num in nums]
        p1,p2,p3,p4,p5 = ps
        if not (p2 < g3 and p3 < g3 and p4 < g3): continue
        if not (p5 > g0): continue
        break
    else:
        continue
    n_rand += 1
    v = f4(ps)
    if worst_val is None or v > worst_val:
        worst_val = v; worst_cfg = ps[:]; worst_is_dyadic = (ps==dyadic)
    if v > target + F(1,10000):
        n_escape += 1
        if len(n_escape_configs) < 20:
            n_escape_configs.append((ps[:], v))
    if n_rand % 2000 == 0:
        print(f"  rand {n_rand} t={time.time()-t0:.1f}s worst={float(worst_val):.5f} esc={n_escape}")
        sys.stdout.flush()

print("RANDOM DONE:", n_rand, "configs, total t=", round(time.time()-t0,1),"s")
print("FINAL worst_val =", worst_val, "=", float(worst_val), " (target 1/31 =", float(target), ")")
print("FINAL worst_cfg =", [float(x) for x in worst_cfg])
print("FINAL worst_cfg exact =", [str(x) for x in worst_cfg])
print("is dyadic =", worst_is_dyadic, " cfg==dyadic:", worst_cfg==dyadic)
print("total escapes (f4 > 1/31):", n_escape)
for c,v in n_escape_configs[:10]:
    print("  ESC cfg=", [str(x) for x in c], "v=", str(v), float(v))
