import itertools, random
from fractions import Fraction as F

def E_even_rank(vals):
    # even sorted-rank sum: sort descending, take 0-indexed even positions (rank 2,4,...)
    v = sorted(vals, reverse=True)
    return sum(v[i] for i in range(1, len(v), 2))

def brute_vertex_candidates(tau, s, k):
    # enumerate p from 0..k pins from tau (with repetition), remaining k-p coords tied to v
    r = len(tau)
    cands = []
    for p in range(0, k+1):
        q = k - p
        if p == 0:
            pin_combos = [()]
        else:
            pin_combos = itertools.product(range(r), repeat=p)
        for pins in pin_combos:
            pin_vals = [tau[i] for i in pins]
            rem = s - sum(pin_vals)
            if q == 0:
                if abs(rem) < 1e-9:
                    F_ = list(pin_vals)
                    cands.append(F_)
                continue
            if rem < -1e-9:
                continue
            v = rem/q if q>0 else 0
            if v < -1e-9: continue
            F_ = list(pin_vals) + [max(v,0.0)]*q
            cands.append(F_)
    best = max(cands, key=lambda F_: E_even_rank(F_+tau))
    return E_even_rank(best+tau), best

def random_search_max(tau, s, k, trials=200000):
    best = -1e18
    for _ in range(trials):
        # random point on simplex sum=s, k coords, nonneg
        cuts = sorted([random.random() for _ in range(k-1)]) if k>1 else []
        bounds=[0]+cuts+[1]
        F_ = [(bounds[i+1]-bounds[i])*s for i in range(k)]
        val = E_even_rank(F_+tau)
        if val > best:
            best = val
    return best

random.seed(5)
maxdiff=0
for trial in range(15):
    r = random.randint(2,4)
    tau = sorted([round(random.uniform(0.1,5),3) for _ in range(r)], reverse=True)
    s = round(random.uniform(0.5,10),3)
    k = random.randint(1,3)
    vertex_val, vertex_F = brute_vertex_candidates(tau, s, k)
    rs_val = random_search_max(tau, s, k, trials=100000)
    diff = rs_val - vertex_val
    maxdiff = max(maxdiff, diff)
    print(f"tau={tau} s={s} k={k}  vertex_max={vertex_val:.5f}  random_search_max={rs_val:.5f}  diff={diff:.5f}")
print("max positive diff (random search exceeding vertex prediction):", maxdiff)
