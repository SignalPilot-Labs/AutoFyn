"""
Verify the construction: PEEL ONCE (split p_i -> p_j + (p_i-p_j), Lemma 3) then
apply the CERTIFIED n=2 menu to the 3-piece rest. Total <= 3 marks.
Peeling lemma: D_final = D_rest EXACTLY (certified).
n=2 menu on rest (sorted a>=b>=c, total T): min(c, |2a-T|, a-b, b-c) <= T/7.

Check: over all flat n=3 configs (p4 > 1/15), is
  min over peeling choices {p1->p2, p1->p3, p1->p4, p2->p3, p2->p4, p3->p4}
  of (n=2-menu-min on the rest)  <=  1/15  ?
"""
import numpy as np
from itertools import combinations
import random
random.seed(7); np.random.seed(7)

TARGET = 1/15

def n2_menu_min(rest):
    """rest: list of 3 pieces (unsorted). Return min of the 4-menu D-values
    (scaled to total T): min(c, |2a-T|, a-b, b-c) where a>=b>=c, T=a+b+c."""
    a, b, c = sorted(rest, reverse=True)
    T = a + b + c
    v_c = c
    v_B = abs(2*a - T)   # |2a - T| = |a - (b+c)| = |a-b-c|
    v_ab = a - b
    v_bc = b - c
    return min(v_c, v_B, v_ab, v_bc)

def peel_options(p):
    """Yield (label, rest_3pieces) for each valid single split-to-match peel.
    p = (p1,p2,p3,p4) sorted desc. Peel p_i -> p_j + (p_i - p_j), pair (p_j,p_j)
    cancels, rest = {p_i - p_j} union {all pieces except p_i and one copy of p_j}.
    Requires p_i >= p_j (true for i<j by sort)."""
    p1,p2,p3,p4 = p
    pieces = {'p1':p1,'p2':p2,'p3':p3,'p4':p4}
    # peel options: split piece i into j + (i-j), pair (j,j) cancels.
    # rest = {i-j} + {all pieces except i and one copy of j}
    opts = []
    idx = {'p1':p1,'p2':p2,'p3':p3,'p4':p4}
    keys = ['p1','p2','p3','p4']
    for i in range(4):
        for j in range(4):
            if i==j: continue
            pi = p[i]; pj = p[j]
            if pi < pj: continue  # cannot split pi into pj + (pi-pj) if pi<pj
            rest = [pi - pj]
            for k in range(4):
                if k==i: continue
                if k==j:
                    continue  # remove one copy of pj
                rest.append(p[k])
            # rest has 3 pieces
            assert len(rest)==3
            opts.append((f'{keys[i]}->{keys[j]}', rest))
    return opts

def construction_D(p):
    """Min over peeling choices of n=2-menu-min on the rest."""
    best = float('inf'); best_label=None
    for label, rest in peel_options(p):
        d = n2_menu_min(rest)
        if d < best:
            best = d; best_label = label
    return best, best_label

# --- configs ---
def random_flat():
    while True:
        x = sorted(np.random.dirichlet([1,1,1,1]), reverse=True)
        if x[3] > 1/15 + 1e-6:
            return tuple(round(v,8) for v in x)

# random + structured (near boundary, uniform, spiky-flat)
configs = [random_flat() for _ in range(8000)]
# structured
for _ in range(2000):
    # near-dyadic-flat: scale dyadic (8,4,2,1)/15 with p4 slightly > 1/15
    eps = np.random.uniform(0.001, 0.05)
    p4 = 1/15 + eps
    rem = 1 - p4
    # perturb the (8,4,2) split
    r = np.random.uniform(-0.02, 0.02, 3)
    base = np.array([8,4,2])/14 * rem
    p123 = base + r
    if min(p123) > p4 and sorted(p123, reverse=True)[0] < 1:
        s = p123[0]+p123[1]+p123[2]+p4
        p123 = p123/s
        cfg = tuple(sorted([*p123, p4], reverse=True))
        if cfg[3] > 1/15:
            configs.append(cfg)
# uniform-ish
for _ in range(1000):
    u = np.random.uniform(0.2, 0.3, 4)
    u = sorted(u, reverse=True)
    s = sum(u); u = [x/s for x in u]
    if u[3] > 1/15:
        configs.append(tuple(u))
# spiky flat: p1 large
for _ in range(1000):
    p1 = np.random.uniform(0.4, 0.7)
    rem = 1-p1
    u = sorted(np.random.dirichlet([1,1,1])*rem, reverse=True)
    if u[2] > 1/15 and p1 >= u[0]:
        configs.append((p1, *u))
configs = list(dict.fromkeys(configs))

fail = 0; worst = 0; worst_cfg=None
label_counts = {}
for p in configs:
    d, lab = construction_D(p)
    if d > TARGET + 1e-9:
        fail += 1
        if d > worst:
            worst = d; worst_cfg = p
    label_counts[lab] = label_counts.get(lab, 0) + 1

print(f"Configs: {len(configs)}")
print(f"FAILURES (construction D > 1/15): {fail}")
print(f"Worst construction D: {worst:.6f} (target {TARGET:.6f}) at {worst_cfg}")
print(f"\nPeeling choice achieving the min (counts):")
for k,v in sorted(label_counts.items(), key=lambda x:-x[1]):
    print(f"  {k}: {v}")
