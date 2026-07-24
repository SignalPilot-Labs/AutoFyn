import numpy as np
from scipy.optimize import minimize
from itertools import product
import random

def compositions(n, m):
    # all (c_1,...,c_m) with c_i>=0, sum c_i <= n
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

def phi_for_composition(p, comp):
    m = len(p)
    # free params: for piece i with c_i cuts, c_i free numbers in (0, p_i), fragment = sorted breakpoints
    # We'll parametrize each piece's c_i+1 fragments via c_i unconstrained reals -> softmax-like split
    free_idx = [i for i in range(m) if comp[i] > 0]
    if not free_idx:
        return phi_of_multiset(list(p))
    dims = [comp[i] for i in free_idx]  # number of "free splits" per piece = c_i (c_i+1 fragments)
    total_dim = sum(dims)

    def unpack(x):
        frags = list(p)  # will replace touched pieces
        result = []
        idx = 0
        for i in range(m):
            if comp[i] == 0:
                result.append(p[i])
            else:
                c = comp[i]
                # use softmax on c+1 raw values (c free real params + a fixed 0) to get fractions summing to 1
                raw = np.concatenate([[0.0], x[idx:idx+c]])
                idx += c
                w = np.exp(raw - np.max(raw))
                w = w / w.sum()
                frs = w * p[i]
                result.extend(frs.tolist())
        return result

    def negphi(x):
        # we want MIN phi, so just return phi (minimize directly)
        vals = unpack(x)
        return phi_of_multiset(vals)

    best = None
    for trial in range(6):
        x0 = np.random.randn(total_dim)*1.5
        res = minimize(negphi, x0, method='Nelder-Mead',
                        options={'xatol':1e-9,'fatol':1e-12,'maxiter':4000,'maxfev':4000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def phi_min(p, n):
    m = len(p)
    best = None
    bestcomp = None
    for comp in compositions(n, m):
        if sum(comp) > n: continue
        val = phi_for_composition(p, comp)
        if best is None or val < best:
            best = val
            bestcomp = comp
    return best, bestcomp

if __name__ == "__main__":
    random.seed(0)
    np.random.seed(0)
    # case b2 box at n=3
    n=3
    Dn = 2**(n+1)-1
    an = 2**n/Dn
    print("n=3: D_n=",Dn,"a_n=",an)
    p = (0.45,0.15,0.25,0.15)
    T = sum(p)
    val, comp = phi_min(p, n)
    print(p, "-> phimin=",val, "target a_nT=",an*T, "comp=",comp)
