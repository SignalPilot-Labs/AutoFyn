import itertools
import numpy as np
from scipy.optimize import minimize

def A(fragments):
    fragments = sorted(fragments, reverse=True)
    s = 0.0
    for i, v in enumerate(fragments):
        s += v if i % 2 == 0 else -v
    return s  # = Phi_odd - Phi_even

def Phi_odd(fragments, T):
    return (A(fragments) + T) / 2.0

def compositions(total_budget, m):
    for combo in itertools.product(range(total_budget+1), repeat=m):
        if sum(combo) <= total_budget:
            yield combo

def phi_min_for_p(p, n, restarts=8, seed=0):
    m = len(p); T = sum(p)
    best = None
    rng = np.random.default_rng(seed)
    for comp in compositions(n, m):
        k = sum(comp)
        def build_frags(x):
            frags = []; idx = 0
            for i, ci in enumerate(comp):
                if ci == 0:
                    frags.append(p[i])
                else:
                    raw = np.clip(x[idx:idx+ci], -30, 30); idx += ci
                    ratios = np.sort(1/(1+np.exp(-raw)))
                    prev = 0.0
                    for r in ratios:
                        frags.append((r-prev)*p[i]); prev = r
                    frags.append((1-prev)*p[i])
            return frags
        if k == 0:
            val = Phi_odd(list(p), T)
            if best is None or val < best: best = val
            continue
        def objective(x):
            return Phi_odd(build_frags(x), T)
        for _ in range(restarts):
            x0 = rng.normal(size=k)
            res = minimize(objective, x0, method='Nelder-Mead',
                            options={'xatol':1e-10,'fatol':1e-12,'maxiter':6000})
            if best is None or res.fun < best: best = res.fun
    return best

n = 3
a3 = 8/15

p_unrestricted = [0.4682,0.2531,0.1696,0.1091]
pm = phi_min_for_p(p_unrestricted, n, restarts=12, seed=1)
print(f"unrestricted witness: Phi_min={pm:.6f}, a3*T={a3:.6f}, margin={a3-pm:.6f}")

eps = 2e-3
tail = [0.15, 0.05]
tail_sum_target = 1 - (0.5-eps) - (a3/2-eps)
tail = [t*tail_sum_target/sum(tail) for t in tail]
p_corner = [0.5-eps, a3/2-eps] + tail
print("corner p:", p_corner, "sum=", sum(p_corner))
pm2 = phi_min_for_p(p_corner, n, restarts=12, seed=2)
print(f"corner witness: Phi_min={pm2:.6f}, margin={a3-pm2:.6f}")
