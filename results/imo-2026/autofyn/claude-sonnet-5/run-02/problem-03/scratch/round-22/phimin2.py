import numpy as np
from scipy.optimize import minimize

def compositions(n, m):
    def rec(m, budget):
        if m==1:
            for c in range(budget+1):
                yield (c,)
            return
        for c in range(budget+1):
            for rest in rec(m-1, budget-c):
                yield (c,)+rest
    yield from rec(m, n)

def phi_of_multiset(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

def phi_for_composition(p, comp, restarts=3):
    m = len(p)
    free_idx = [i for i in range(m) if comp[i] > 0]
    if not free_idx:
        return phi_of_multiset(list(p))
    dims = [comp[i] for i in free_idx]
    total_dim = sum(dims)

    def unpack(x):
        result = []
        idx = 0
        for i in range(m):
            if comp[i] == 0:
                result.append(p[i])
            else:
                c = comp[i]
                raw = np.concatenate([[0.0], x[idx:idx+c]])
                idx += c
                w = np.exp(raw - np.max(raw))
                w = w / w.sum()
                result.extend((w*p[i]).tolist())
        return result

    def negphi(x):
        return phi_of_multiset(unpack(x))

    best = None
    for trial in range(restarts):
        x0 = np.random.randn(total_dim)*1.5
        res = minimize(negphi, x0, method='Nelder-Mead',
                        options={'xatol':1e-7,'fatol':1e-10,'maxiter':800,'maxfev':800})
        if best is None or res.fun < best:
            best = res.fun
    return best

def phi_min(p, n, restarts=3):
    m = len(p)
    best = None
    bestcomp = None
    for comp in compositions(n, m):
        val = phi_for_composition(p, comp, restarts=restarts)
        if best is None or val < best:
            best = val
            bestcomp = comp
    return best, bestcomp
