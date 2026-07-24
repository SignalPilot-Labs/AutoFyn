import itertools, random
import numpy as np
from scipy.optimize import minimize

def phi(multiset):
    s = sorted(multiset, reverse=True)
    total = 0.0
    for i,x in enumerate(s):
        if i%2==0: total += x
        else: total -= x
    return (sum(multiset)+total)/2

def compositions(budget, parts):
    # all tuples of length parts, nonneg ints, sum <= budget
    res = []
    def rec(i, remaining, cur):
        if i==parts:
            res.append(tuple(cur))
            return
        for c in range(remaining+1):
            rec(i+1, remaining-c, cur+[c])
    rec(0, budget, [])
    return res

def fragments_from_params(piece_size, c, params):
    # c cuts -> c+1 fragments; params: c values in (0,1) sorted give breakpoints
    if c==0:
        return [piece_size]
    bp = np.sort(params)
    bp = np.clip(bp, 1e-9, 1-1e-9)
    edges = [0.0]+list(bp)+[1.0]
    return [piece_size*(edges[i+1]-edges[i]) for i in range(len(edges)-1)]

def min_phi_for_pieces(pieces, budget, seeds=8):
    n = len(pieces)
    best = None
    for comp in compositions(budget, n):
        total_params = sum(comp)
        if total_params == 0:
            frags = list(pieces)
            val = phi(frags)
            if best is None or val < best:
                best = val
            continue
        def objective(x):
            frags = []
            idx = 0
            for i,c in enumerate(comp):
                if c==0:
                    frags.append(pieces[i])
                else:
                    params = x[idx:idx+c]
                    idx += c
                    frags.extend(fragments_from_params(pieces[i], c, params))
            return phi(frags)
        local_best = None
        for seed in range(seeds):
            rng = np.random.default_rng(seed*7+1)
            x0 = rng.uniform(0.05,0.95,size=total_params)
            res = minimize(objective, x0, method='Nelder-Mead',
                            options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000,'maxfev':8000})
            if local_best is None or res.fun < local_best:
                local_best = res.fun
        if best is None or local_best < best:
            best = local_best
    return best

# ladder-ish witness base
p1 = 4468/10001
p2 = 2591/10001
s = 1 - p1 - p2

pts = [s/2, 0.15, 0.16, 0.17, 0.175, 0.18, 0.185, p1-p2, 0.19, 0.195, 0.20, 0.21, 0.2251, 0.24, 0.2591-1e-4]
results = []
for p3 in pts:
    if p3 < s/2 or p3 > min(p2,s):
        continue
    p4 = s - p3
    if p4 < 0 or p4 > p3:
        continue
    g = min_phi_for_pieces([p1,p2,p3,p4], budget=3, seeds=6)
    results.append((p3,p4,g))
    print(f"p3={p3:.5f} p4={p4:.5f} g={g:.6f}")
