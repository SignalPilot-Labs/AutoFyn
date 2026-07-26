"""
Decode the true optimal Xiang strategy for n=3 flat configs.
Use scipy continuous optimization (Nelder-Mead / multistart) on mark positions,
plus a fine grid. For each config, print the optimal marks and resulting pieces
so we can identify the structure.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution
from itertools import combinations
import random
random.seed(2); np.random.seed(2)

TARGET = 1/15

def cumsum_zero(pieces):
    out = []; s = 0.0
    for p in pieces: s += p; out.append(s)
    return out

def pieces_from_marks(liu_bounds, xiang_marks):
    all_marks = sorted(set(list(liu_bounds) + list(xiang_marks)))
    pts = [0.0] + all_marks + [1.0]
    return [pts[i+1]-pts[i] for i in range(len(pts)-1)]

def D_of(pieces):
    a = sorted(pieces, reverse=True)
    return sum(x if k%2==0 else -x for k,x in enumerate(a))

def best_xiang(liu_pieces, n_marks=3, n_starts=32, grid_n=50):
    liu_bounds = cumsum_zero(liu_pieces)[:-1]
    # fine grid
    grid = np.linspace(0.002, 0.998, grid_n)
    cand = [g for g in grid if all(abs(g-b)>1e-9 for b in liu_bounds)]
    best = D_of(liu_pieces); best_marks=[]
    # 0..3 marks combos
    for k in range(0, n_marks+1):
        for combo in combinations(cand, k):
            pieces = pieces_from_marks(liu_bounds, combo)
            d = D_of(pieces)
            if d < best - 1e-12:
                best = d; best_marks = list(combo)
    # continuous refinement: optimize mark positions (up to 3) via multistart Nelder-Mead
    def D_param(xs):
        # clamp, sort, dedup-ish
        ms = sorted(xs)
        # penalize if too close to liu bounds (avoid degenerate)
        pieces = pieces_from_marks(liu_bounds, ms)
        return D_of(pieces)
    bounds = [(0.001, 0.999)]*n_marks
    from scipy.optimize import differential_evolution
    def D_param_bounded(xs):
        ms = sorted(np.clip(xs, 0.001, 0.999))
        # avoid liu bounds
        for b in liu_bounds:
            ms = [m if abs(m-b)>0.002 else (m+0.004 if m<b else m-0.004) for m in ms]
        ms = sorted(ms)
        pieces = pieces_from_marks(liu_bounds, ms)
        return D_of(pieces)
    res = differential_evolution(D_param_bounded, bounds, maxiter=60, seed=2, tol=1e-10, polish=True)
    if res.fun < best - 1e-9:
        best = res.fun
        best_marks = sorted(res.x.tolist())
    return best, best_marks, liu_bounds

def describe(liu_pieces, best, marks, liu_bounds):
    final = pieces_from_marks(liu_bounds, marks)
    final_sorted = sorted(final, reverse=True)
    return best, final_sorted, marks

# Test configs: the 1 exceedance, the big misses, plus random flats.
test_configs = [
    (0.53492536, 0.25931056, 0.13634754, 0.06941654),  # exceedance
    (0.38805732, 0.25983738, 0.18241242, 0.16969288),
    (0.40537408, 0.20967595, 0.19570976, 0.18924021),
    (0.57741497, 0.21460913, 0.13886942, 0.06910648),
    (0.47279711, 0.31216528, 0.12760392, 0.08743369),
    (0.45752712, 0.24225853, 0.22570841, 0.07450594),
    (0.43444898, 0.28112595, 0.19764664, 0.08677842),
    # uniform-ish
    (0.26, 0.25, 0.25, 0.24),
    (0.30, 0.25, 0.235, 0.215),
    # dyadic boundary
    (8/15, 4/15, 2/15, 1/15),
]

print(f"Target 1/15 = {TARGET:.6f}\n")
for p in test_configs:
    best, marks, lb = best_xiang(list(p), n_marks=3, n_starts=24, grid_n=50)
    final = pieces_from_marks(lb, marks)
    fs = sorted(final, reverse=True)
    pstr = ", ".join(f"{x:.5f}" for x in p)
    print(f"config ({pstr})")
    print(f"  best D = {best:.6f}  ({'OK' if best<=TARGET+1e-6 else 'EXCEEDS!'})")
    print(f"  xiang marks: {[round(m,5) for m in marks]}")
    print(f"  final pieces (sorted): {[round(x,5) for x in fs]}")
    # Check: do the final pieces reveal a pattern? E.g. pairs equal, or split-to-match
    # identify pairs (equal pieces)
    from collections import Counter
    c = Counter(round(x,5) for x in fs)
    pairs = [v for v,ct in c.items() if ct>=2]
    print(f"  equal-value groups (val:count): {dict(c)}")
    print()
