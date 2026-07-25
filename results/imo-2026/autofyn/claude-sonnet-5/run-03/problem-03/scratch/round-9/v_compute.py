import itertools, random
import numpy as np
from scipy.optimize import minimize

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def split_response(p, m, softmax_params):
    # p: value to split into m+1 positive parts using softmax params (m free params -> m+1 parts)
    z = np.concatenate(([0.0], softmax_params))
    e = np.exp(z - np.max(z))
    w = e / e.sum()
    return p * w

def V_for_allocation(p, mvec, restarts=8):
    k = len(p)
    # objective: given free params for each split piece, compute OddSum, minimize
    dims = [m for m in mvec]
    total_dim = sum(dims)
    if total_dim == 0:
        return oddsum(p)
    def unpack(x):
        vals = []
        idx = 0
        for i,m in enumerate(mvec):
            if m == 0:
                vals.append(p[i])
            else:
                params = x[idx:idx+m]
                idx += m
                parts = split_response(p[i], m, params)
                vals.extend(parts.tolist())
        return vals
    def obj(x):
        vals = unpack(x)
        return oddsum(vals)
    best = None
    for _ in range(restarts):
        x0 = np.random.randn(total_dim)*1.5
        res = minimize(obj, x0, method='Nelder-Mead',
                        options={'xatol':1e-8,'fatol':1e-10,'maxiter':3000,'maxfev':3000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def V(p, n, restarts=8):
    k = len(p)
    best = None
    # enumerate all mvec with sum(mvec) <= n, mvec length k
    for total in range(0, n+1):
        for mvec in itertools.product(range(total+1), repeat=k):
            pass
    # more efficient: enumerate compositions directly
    def compositions(total, parts):
        if parts == 1:
            yield (total,)
            return
        for i in range(total+1):
            for rest in compositions(total-i, parts-1):
                yield (i,) + rest
    seen = set()
    for total in range(0, n+1):
        for mvec in compositions(total, k):
            if mvec in seen: continue
            seen.add(mvec)
            val = V_for_allocation(p, mvec, restarts=restarts)
            if best is None or val < best:
                best = val
    return best

if __name__ == "__main__":
    random.seed(1)
    np.random.seed(1)
    n = 2  # k=3
    # test concavity along a segment through balanced region
    def rand_balanced():
        while True:
            a = random.uniform(0.05,0.45)
            b = random.uniform(0.05, 1-a-0.05)
            c = 1-a-b
            p = sorted([a,b,c], reverse=True)
            if p[0] < 0.5 and min(p[0]-p[1], p[1]-p[2]) > 1/(2**3-1):
                return p
    for trial in range(6):
        pA = rand_balanced()
        pB = rand_balanced()
        pM = [(x+y)/2 for x,y in zip(pA,pB)]
        VA = V(pA, n, restarts=12)
        VB = V(pB, n, restarts=12)
        VM = V(pM, n, restarts=12)
        target = (VA+VB)/2
        print(f"trial {trial}: pA={pA} VA={VA:.5f}; pB={pB} VB={VB:.5f}; pM={pM} VM={VM:.5f}; avg={target:.5f}; VM-avg={VM-target:.5f}")

def sweep():
    import numpy as np
    n = 2
    # vary p1 from 0.15 to 0.49, keep p2/p3 ratio fixed, both remainder balanced
    ratio = 0.62  # p2 = ratio*(1-p1), p3 = (1-ratio)*(1-p1)
    p1s = np.linspace(0.15, 0.49, 18)
    vals = []
    for p1 in p1s:
        rem = 1-p1
        p2 = ratio*rem
        p3 = rem-p2
        p = sorted([p1,p2,p3], reverse=True)
        v = V(p, n, restarts=10)
        vals.append(v)
        print(f"p1={p1:.4f} p={[round(x,4) for x in p]} V={v:.5f}")
    # check discrete second difference for concavity (should be <=0 if concave)
    print("\nsecond differences (want <=0 for concavity):")
    for i in range(1, len(vals)-1):
        d2 = vals[i-1] - 2*vals[i] + vals[i+1]
        print(f"i={i} p1={p1s[i]:.4f} d2={d2:.6f}")

if __name__ == "__main__":
    pass
