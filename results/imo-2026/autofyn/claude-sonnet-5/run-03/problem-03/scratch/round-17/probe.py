import itertools, numpy as np
from scipy.optimize import minimize

def oddsum(vals):
    v = sorted(vals, reverse=True)
    return sum(v[i] for i in range(0, len(v), 2))

def compositions_leq(total, parts):
    # all (m_1..m_parts) with m_i>=0 sum<=total
    if parts == 1:
        for m in range(total+1):
            yield (m,)
        return
    for m in range(total+1):
        for rest in compositions_leq(total-m, parts-1):
            yield (m,) + rest

def best_split_value(p, m, restarts=20, seed=0):
    # p: tuple of piece sizes (k of them), m: tuple of #extra cuts per piece
    rng = np.random.default_rng(seed)
    k = len(p)
    # variables: for each split piece i (m_i>=1), softmax params of size m_i+1
    split_idx = [i for i in range(k) if m[i] >= 1]
    sizes = [m[i]+1 for i in split_idx]
    nvar = sum(sizes)
    if nvar == 0:
        # no splits at all
        return oddsum(list(p)), {i: [p[i]] for i in range(k)}

    def unpack(theta):
        frags = {}
        pos = 0
        for i, s in zip(split_idx, sizes):
            th = theta[pos:pos+s]
            pos += s
            e = np.exp(th - th.max())
            w = e / e.sum()
            frags[i] = p[i]*w
        return frags

    def objective(theta):
        frags = unpack(theta)
        allvals = []
        for i in range(k):
            if i in frags:
                allvals.extend(frags[i].tolist())
            else:
                allvals.append(p[i])
        return oddsum(allvals)

    best = None
    best_frags = None
    for r in range(restarts):
        theta0 = rng.normal(size=nvar)
        res = minimize(objective, theta0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':20000,'maxfev':20000})
        if best is None or res.fun < best:
            best = res.fun
            best_frags = unpack(res.x)
    return best, best_frags

def V(p, n, restarts=25, seed=0):
    k = len(p)
    results = []
    for m in compositions_leq(n, k):
        val, frags = best_split_value(p, m, restarts=restarts, seed=seed)
        results.append((val, m, frags))
    results.sort(key=lambda t: t[0])
    return results

points_n3 = [
    (0.4416,0.3035,0.1851,0.0698),
    (0.4378,0.3252,0.1898,0.0472),
    (0.4211,0.3348,0.1910,0.0531),
]

for idx, p in enumerate(points_n3):
    print("=== n=3 point", idx+1, p, "sum=", sum(p))
    res = V(p, 3, restarts=30, seed=idx)
    top = res[:6]
    for val, m, frags in top:
        fragstr = {i: [round(x,6) for x in v] for i,v in frags.items()} if isinstance(frags, dict) else frags
        print(f"  val={val:.6f} m={m} frags={fragstr}")
