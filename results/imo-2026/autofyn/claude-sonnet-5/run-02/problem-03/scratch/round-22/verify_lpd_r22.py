import itertools, random
import numpy as np
from scipy.optimize import minimize

def phi(fragments):
    fragments = sorted(fragments, reverse=True)
    s = 0.0
    for i, v in enumerate(fragments):
        s += v if i % 2 == 0 else -v
    return s

def compositions(total_budget, m):
    # all tuples (c1..cm) with 0<=ci, sum<=total_budget
    for combo in itertools.product(range(total_budget+1), repeat=m):
        if sum(combo) <= total_budget:
            yield combo

def phi_min_for_p(p, n, restarts=6, seed=0):
    m = len(p)
    best = None
    rng = np.random.default_rng(seed)
    for comp in compositions(n, m):
        k = sum(comp)  # number of cuts used
        if k == 0:
            frags = list(p)
            val = phi(frags)
            if best is None or val < best:
                best = val
            continue
        # free params: for each piece i with ci cuts, ci fractions in (0,1) that are cumulative split ratios
        # param vector length = sum(comp)
        def build_frags(x):
            frags = []
            idx = 0
            for i, ci in enumerate(comp):
                if ci == 0:
                    frags.append(p[i])
                else:
                    # x[idx:idx+ci] in R, map via sigmoid to (0,1), sort, use as cumulative ratios
                    raw = x[idx:idx+ci]
                    idx += ci
                    ratios = 1/(1+np.exp(-raw))
                    ratios = np.sort(ratios)
                    prev = 0.0
                    for r in ratios:
                        frags.append((r-prev)*p[i])
                        prev = r
                    frags.append((1-prev)*p[i])
            return frags
        def objective(x):
            return phi(build_frags(x))
        for _ in range(restarts):
            x0 = rng.normal(size=k)
            res = minimize(objective, x0, method='Nelder-Mead',
                            options={'xatol':1e-9,'fatol':1e-11,'maxiter':5000})
            if best is None or res.fun < best:
                best = res.fun
    return best

n = 3
a3 = 8/15

p_unrestricted = [0.4682,0.2531,0.1696,0.1091]
pm = phi_min_for_p(p_unrestricted, n, restarts=10, seed=1)
print("unrestricted witness: phi_min =", pm, "margin =", a3 - pm)

eps = 2e-3
p_corner = [0.5-eps, a3/2-eps]
p_corner += [0.15, 0.05]  # arbitrary tail summing appropriately; renormalize
# renormalize to sum 1, keep p1,p2 fixed roughly, adjust tail proportionally
tail_sum_target = 1 - p_corner[0] - p_corner[1]
tail = [0.15, 0.05]
tail = [t*tail_sum_target/sum(tail) for t in tail]
p_corner = [p_corner[0], p_corner[1]] + tail
print("corner point:", p_corner, "sum=", sum(p_corner))
pm2 = phi_min_for_p(p_corner, n, restarts=10, seed=2)
print("corner witness: phi_min =", pm2, "margin =", a3 - pm2)
