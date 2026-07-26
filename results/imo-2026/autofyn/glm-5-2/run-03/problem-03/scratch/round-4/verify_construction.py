"""
Confirm: construction max D over flat configs approaches 1/15 at the dyadic
boundary (p4 -> 1/15+), never exceeds. Use exact fractions (Fraction) for
the dyadic config and a near-boundary family. Also check the full regime
p4 <= 1/15 (Lemma 4) + p4 > 1/15 (peel+n2) gives a complete cover, tight at dyadic.
"""
import numpy as np
from fractions import Fraction as F
import random
random.seed(11); np.random.seed(11)

def n2_menu_min_frac(rest):
    # rest: list of Fraction
    a,b,c = sorted(rest, reverse=True)
    T = a+b+c
    return min(c, abs(2*a - T), a-b, b-c)

def peel_options_frac(p):
    opts = []
    for i in range(4):
        for j in range(4):
            if i==j: continue
            pi, pj = p[i], p[j]
            if pi < pj: continue
            rest = [pi - pj]
            for k in range(4):
                if k==i or k==j: continue
                rest.append(p[k])
            opts.append((i,j,rest))
    return opts

def construction_D_frac(p):
    best = None; best_opt=None
    for opt in peel_options_frac(p):
        d = n2_menu_min_frac(opt[2])
        if best is None or d < best:
            best = d; best_opt = opt
    return best, best_opt

# Dyadic n=3 config: (8/15, 4/15, 2/15, 1/15)
dyadic = [F(8,15), F(4,15), F(2,15), F(1,15)]
d, opt = construction_D_frac(dyadic)
print(f"Dyadic config (8/15,4/15,2/15,1/15):")
print(f"  peel+n2 construction D = {d} = {float(d):.6f} (target 1/15={1/15:.6f})")
print(f"  best peel: piece {opt[0]+1} -> piece {opt[1]+1}, rest={[str(x) for x in opt[2]]}")
print(f"  Lemma 4 gives D = p4 = {dyadic[3]} = {float(dyadic[3]):.6f}")
print()

# Near-boundary flat: p4 = 1/15 + eps, dyadic-scaled rest
print("Near-boundary flat configs (p4 = 1/15 + eps, rest dyadic-scaled):")
for eps_f in [F(1,1000), F(1,200), F(1,100), F(1,50), F(1,20), F(1,10)]:
    p4 = F(1,15) + eps_f
    rem = 1 - p4
    # dyadic rest (8,4,2)/14 scaled to rem
    p1 = rem * F(8,14); p2 = rem * F(4,14); p3 = rem * F(2,14)
    cfg = [p1, p2, p3, p4]  # already sorted (p1>p2>p3>p4 for small eps)
    # verify sort
    assert cfg == sorted(cfg, reverse=True), cfg
    d, opt = construction_D_frac(cfg)
    lemma4 = p4
    print(f"  eps={float(eps_f):.4f}: p4={float(p4):.5f} | peel+n2 D={float(d):.6f} (=1/15? {abs(d-F(1,15))<F(1,10**9)}) | Lemma4 D={float(lemma4):.6f}")

print()
# Max construction D over a fine random flat sweep (float), report max and where
def n2_menu_min_f(rest):
    a,b,c = sorted(rest, reverse=True)
    T = a+b+c
    return min(c, abs(2*a-T), a-b, b-c)
def constr_f(p):
    best = 1e9
    for i in range(4):
        for j in range(4):
            if i==j: continue
            if p[i] < p[j]: continue
            rest = [p[i]-p[j]] + [p[k] for k in range(4) if k!=i and k!=j]
            d = n2_menu_min_f(rest)
            if d < best: best = d
    return best

maxd = 0; maxcfg=None; n=0
for _ in range(30000):
    x = sorted(np.random.dirichlet([1,1,1,1]), reverse=True)
    if x[3] <= 1/15 + 1e-6: continue
    n += 1
    d = constr_f(x)
    if d > maxd:
        maxd = d; maxcfg = x
print(f"Float sweep, flat configs: {n}")
print(f"MAX construction D = {maxd:.6f} (target 1/15={1/15:.6f})")
print(f"  at config {maxcfg}")
# Also scan near-boundary densely
maxd2 = 0; maxcfg2=None
for _ in range(30000):
    eps = np.random.uniform(1e-5, 0.03)
    p4 = 1/15 + eps
    rem = 1 - p4
    # dyadic rest with small perturbation
    base = np.array([8,4,2])/14 * rem
    pert = np.random.uniform(-0.01, 0.01, 3)
    p123 = base + pert
    if min(p123) <= p4: continue
    s = sum(p123) + p4
    p123 = p123/s * (1-p4) + 0  # rescale p123 to sum to rem... simpler:
    p123 = p123/sum(p123) * rem
    cfg = sorted([*p123, p4], reverse=True)
    if cfg[3] <= 1/15: continue
    d = constr_f(cfg)
    if d > maxd2: maxd2 = d; maxcfg2 = cfg
print(f"Near-boundary dense sweep: MAX construction D = {maxd2:.6f}")
print(f"  at config {maxcfg2}")
