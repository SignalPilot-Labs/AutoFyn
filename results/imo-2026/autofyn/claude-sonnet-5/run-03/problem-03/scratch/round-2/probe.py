import numpy as np
from scipy.optimize import minimize
from itertools import combinations_with_replacement
import random

def oddsum(vals):
    v = sorted(vals, reverse=True)
    return sum(v[0::2])

def value_for_cut_distribution(pieces, cuts, budget_check=True):
    """pieces: list of base piece lengths. cuts: list same length, cuts[i] = number of cuts spent on piece i.
    Returns function to optimize (minimize oddsum) over split fractions.
    We'll do random-restart local optimization.
    """
    k = len(pieces)
    # total number of free split points = sum(cuts)
    total_splits = sum(cuts)
    if total_splits == 0:
        return oddsum(pieces), pieces
    # parametrize each piece's cuts[i] sub-fractions via cumulative logistic transform
    def unpack(x):
        idx = 0
        allvals = []
        for i in range(k):
            ci = cuts[i]
            if ci == 0:
                allvals.append(pieces[i])
            else:
                # need ci free breakpoints in (0,1) sorted, use ci raw params -> softmax style
                raw = x[idx:idx+ci+1]
                idx += ci+1
                ex = np.exp(raw - np.max(raw))
                frac = ex / ex.sum()
                for f in frac:
                    allvals.append(f*pieces[i])
        return allvals

    nparams = sum(c+1 for c in cuts if c>0)
    best_val = None
    best_x = None
    for trial in range(30):
        x0 = np.random.randn(nparams)*1.0
        res = minimize(lambda x: oddsum(unpack(x)), x0, method='Nelder-Mead',
                        options={'maxiter':2000,'xatol':1e-9,'fatol':1e-12})
        if best_val is None or res.fun < best_val:
            best_val = res.fun
            best_x = res.x
    return best_val, unpack(best_x)

def xy_best_response(pieces, budget):
    """Try all distributions of `budget` cuts among len(pieces) pieces (allow 0..budget per piece,
    sum <= budget), return min oddsum and the winning distribution+split."""
    k = len(pieces)
    best = None
    best_info = None
    # enumerate all distributions of total cuts t=0..budget among k pieces
    from itertools import product
    def gen_distributions(k, budget):
        # all tuples of length k with nonneg ints summing to <= budget
        if k == 1:
            for t in range(budget+1):
                yield (t,)
            return
        for first in range(budget+1):
            for rest in gen_distributions(k-1, budget-first):
                yield (first,)+rest
    for dist in gen_distributions(k, budget):
        val, vals = value_for_cut_distribution(pieces, list(dist))
        if best is None or val < best:
            best = val
            best_info = (dist, vals)
    return best, best_info

# sanity check against known: n=1 threshold t=2/3 -> c(1)=2/3
print("=== n=1 sanity ===")
for t in [0.5,0.6,0.6667,0.7,0.8,0.9]:
    pieces=[t,1-t]
    val, info = xy_best_response(pieces, 1)
    print(f"t={t:.4f} val={val:.5f} dist/splits={info}")
