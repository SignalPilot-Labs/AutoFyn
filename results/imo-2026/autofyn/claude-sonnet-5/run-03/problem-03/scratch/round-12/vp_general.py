import numpy as np
from scipy.optimize import minimize
import itertools

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def softmax(x):
    e = np.exp(x - np.max(x))
    return e/e.sum()

def compositions_leq(total, k):
    # all (m_1,...,m_k) with m_i>=0 sum<=total
    def rec(remaining, slots):
        if slots == 1:
            for v in range(remaining+1):
                yield (v,)
            return
        for v in range(remaining+1):
            for rest in rec(remaining - v, slots-1):
                yield (v,) + rest
    return rec(total, k)

def V_shape(p, m, restarts=12):
    # m: tuple of cuts per piece (m_i cuts -> m_i+1 fragments)
    k = len(p)
    split_idx = [i for i in range(k) if m[i] > 0]
    fixed_vals = [p[i] for i in range(k) if m[i] == 0]
    if not split_idx:
        return oddsum(fixed_vals)
    dims = [m[i]+1 for i in split_idx]
    total_dim = sum(dims)
    best = None
    for _ in range(restarts):
        x0 = np.random.randn(total_dim)
        def f(x):
            frags = []
            off = 0
            for i, d in zip(split_idx, dims):
                frac = softmax(x[off:off+d])
                frags.extend(list(p[i]*frac))
                off += d
            return oddsum(fixed_vals + frags)
        res = minimize(f, x0, method='Nelder-Mead',
                        options={'xatol':1e-9,'fatol':1e-11,'maxiter':4000,'maxfev':6000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def V(p, n, restarts=10, verbose=False):
    k = len(p)
    best = None
    for m in compositions_leq(n, k):
        v = V_shape(p, m, restarts=restarts)
        if best is None or v < best:
            best = v
            bestm = m
    if verbose:
        print("  best shape", bestm, "V=", best)
    return best
