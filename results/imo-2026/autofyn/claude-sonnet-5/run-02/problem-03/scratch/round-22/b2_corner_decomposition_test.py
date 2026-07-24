import numpy as np
from scipy.optimize import minimize, differential_evolution
import itertools, random

def phi_of_fragments(frags):
    frags = np.sort(np.array(frags))[::-1]
    T = frags.sum()
    A = 0.0
    for i, v in enumerate(frags):
        A += v if i % 2 == 0 else -v
    return (T + A) / 2.0

def comps(m, n):
    if m == 1:
        for c in range(n + 1):
            yield (c,)
    else:
        for c in range(n + 1):
            for rest in comps(m - 1, n - c):
                yield (c,) + rest

def phi_for_composition(p, comp, restarts=6):
    m = len(p)
    idx = [comp[i] + 1 for i in range(m)]
    total_free = sum(k - 1 for k in idx)

    def unpack(x):
        frags = []
        pos = 0
        for i, k in enumerate(idx):
            if k == 1:
                frags.append(p[i])
            else:
                raw = x[pos:pos + k - 1]
                pos += k - 1
                w = np.concatenate([raw, [0.0]])
                w = np.exp(w - w.max())
                w = w / w.sum()
                frags.extend(list(w * p[i]))
        return frags

    best = None
    for _ in range(restarts):
        if total_free == 0:
            val = phi_of_fragments(unpack(np.array([])))
            if best is None or val < best:
                best = val
            continue
        x0 = np.random.randn(total_free) * 1.5
        res = minimize(lambda x: phi_of_fragments(unpack(x)), x0,
                        method='Nelder-Mead',
                        options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 6000, 'maxfev': 6000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def phi_min(p, n, restarts=6):
    m = len(p)
    best = None
    bestcomp = None
    for comp in comps(m, n):
        val = phi_for_composition(p, comp, restarts=restarts)
        if best is None or val < best:
            best, bestcomp = val, comp
    return best, bestcomp

def a_n(n):
    Dn = 2 ** (n + 1) - 1
    return (2 ** n) / Dn, Dn

def in_box(p, n, tol=1e-9):
    T = sum(p)
    an, Dn = a_n(n)
    p1, p2 = p[0], p[1]
    return (p1 < T / 2 - tol) and (T / Dn + tol < p2 < an * T / 2 - tol)

def margin(p, n, restarts=6):
    T = sum(p)
    an, _ = a_n(n)
    pm, comp = phi_min(p, n, restarts=restarts)
    return an * T - pm, pm, comp

def random_box_point(n, m, rng, corner=False, eps=None):
    an, Dn = a_n(n)
    T = 1.0
    if corner:
        if eps is None:
            eps = 1e-3
        p1 = T / 2 - eps
        p2 = an * T / 2 - eps
    else:
        p1 = rng.uniform(T / Dn + 1e-4, T / 2 - 1e-4)  # loose upper sample range, refine below
        # ensure p1 in (p2, T/2) after choosing p2; sample p2 first actually
        p2 = rng.uniform(T / Dn + 1e-4, min(an * T / 2 - 1e-4, p1 - 1e-4))
        if p2 <= T / Dn or p2 >= an * T / 2 or p1 <= p2 or p1 >= T / 2:
            return None
    remaining = T - p1 - p2
    if remaining <= 0:
        return None
    tailn = m - 2
    if tailn == 0:
        return [p1, p2]
    # random descending tail summing to remaining, each <= p2
    cuts = sorted(rng.uniform(0, 1, tailn - 1)) if tailn > 1 else []
    fracs = []
    prev = 0
    for c in cuts:
        fracs.append(c - prev)
        prev = c
    fracs.append(1 - prev)
    tail = sorted([f * remaining for f in fracs], reverse=True)
    if tail[0] > p2 + 1e-12:
        return None
    p = [p1, p2] + tail
    if any(p[i] < p[i + 1] for i in range(len(p) - 1)):
        return None
    return p

def scan(n, m, ntrials=25, seed=0, restarts=5):
    rng = np.random.default_rng(seed)
    results = []
    tries = 0
    while len(results) < ntrials and tries < ntrials * 40:
        tries += 1
        p = random_box_point(n, m, rng, corner=False)
        if p is None or not in_box(p, n):
            continue
        mg, pm, comp = margin(p, n, restarts=restarts)
        results.append((mg, p, comp))
    results.sort(key=lambda t: t[0])
    return results

def corner_scan(n, m, ntrials=25, seed=1, eps=1e-3, restarts=5):
    rng = np.random.default_rng(seed)
    results = []
    tries = 0
    while len(results) < ntrials and tries < ntrials * 40:
        tries += 1
        p = random_box_point(n, m, rng, corner=True, eps=eps)
        if p is None or not in_box(p, n):
            continue
        mg, pm, comp = margin(p, n, restarts=restarts)
        results.append((mg, p, comp))
    results.sort(key=lambda t: t[0])
    return results

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    ntrials = int(sys.argv[2])
    restarts = int(sys.argv[3])
    for n in (n,):
        m = n + 1
        print(f"=== n={n}, m={m} ===")
        full = scan(n, m, ntrials=ntrials, seed=42, restarts=restarts)
        corner = corner_scan(n, m, ntrials=ntrials, seed=43, eps=2e-3, restarts=restarts)
        print("Full unrestricted-box scan, 5 smallest margins:")
        for mg, p, comp in full[:5]:
            print(f"  margin={mg:.6f}  p={[round(x,4) for x in p]}  comp={comp}")
        print("Corner-restricted scan (p1,p2 near box corner), 5 smallest margins:")
        for mg, p, comp in corner[:5]:
            print(f"  margin={mg:.6f}  p={[round(x,4) for x in p]}  comp={comp}")
        print(f"  best full margin = {full[0][0]:.6f}   best corner margin = {corner[0][0]:.6f}")
