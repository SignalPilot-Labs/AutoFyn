import random, itertools
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize

n = 3
m = 4
a3 = F(8,15)
D3 = 15

def phi_of_multiset(vals):
    # vals: list of floats/Fractions, sorted descending -> odd rank (1-indexed) sum
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def phi_min_for_composition(p, comp, restarts=8):
    # p: tuple of 4 floats, comp: tuple (c1,c2,c3,c4) cuts on each piece
    # returns numeric estimate of min Phi achievable with exactly this composition
    idx = []
    pieces_fixed = []
    # build variable structure: for each piece i with c_i cuts, c_i+1 free fragments summing to p[i]
    # for c_i=0, fragment = p[i] fixed
    var_specs = []  # list of (piece_index, num_parts)
    fixed_vals = []
    for i, c in enumerate(comp):
        if c == 0:
            fixed_vals.append(p[i])
        else:
            var_specs.append((i, c+1, p[i]))
    if not var_specs:
        return phi_of_multiset(fixed_vals), fixed_vals
    # total free dims = sum(parts) - len(var_specs)  (since each group has a sum constraint)
    def unpack(x):
        vals = list(fixed_vals)
        pos = 0
        for (i, parts, tot) in var_specs:
            # parametrize via softmax-like positive simplex: use squared values normalized
            raw = x[pos:pos+parts]
            pos += parts
            sq = np.abs(raw) + 1e-12
            frac = sq / sq.sum()
            vals.extend((frac * tot).tolist())
        return vals

    def obj(x):
        vals = unpack(x)
        s = sorted(vals, reverse=True)
        return sum(s[i] for i in range(0, len(s), 2))

    total_dim = sum(parts for (_, parts, _) in var_specs)
    best = None
    for r in range(restarts):
        x0 = np.random.rand(total_dim)
        res = minimize(obj, x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':20000,'maxfev':20000})
        if best is None or res.fun < best[0]:
            best = (res.fun, unpack(res.x))
    return best

def all_compositions(n_cuts, m_pieces):
    # all tuples (c1..c_m) with 0<=ci, sum ci <= n_cuts
    res = []
    def rec(idx, remaining, cur):
        if idx == m_pieces:
            res.append(tuple(cur))
            return
        for c in range(remaining+1):
            rec(idx+1, remaining-c, cur+[c])
    rec(0, n_cuts, [])
    return res

comps = all_compositions(n, m)
print("num compositions:", len(comps))

def true_phi_min(p, comps):
    best = None
    for comp in comps:
        val, vals = phi_min_for_composition(p, comp, restarts=6)
        if best is None or val < best[0]:
            best = (val, comp, vals)
    return best

random.seed(1)
np.random.seed(1)

worst_margin = None
worst_p = None
trials = 60
results = []
for t in range(trials):
    # sample p in box: p1<T/2, T/15<p2<4T/15, p1>=p2>=p3>=p4>0, sum=1 (T=1)
    for _try in range(2000):
        p1 = random.uniform(0.26, 0.499)
        p2 = random.uniform(1/15+1e-4, min(p1, 4/15-1e-4))
        rem = 1 - p1 - p2
        if rem <= 0: continue
        p3 = random.uniform(0, min(p2, rem))
        p4 = rem - p3
        if p4 <=0 or p4 > p3: continue
        if p1 < p2 or p2 < p3 or p3 < p4: continue
        break
    else:
        continue
    p = (p1,p2,p3,p4)
    val, comp, vals = true_phi_min(p, comps)
    margin = float(a3) * 1.0 - val
    results.append((p, comp, val, margin))
    if worst_margin is None or margin < worst_margin:
        worst_margin = margin
        worst_p = (p, comp, vals)

print("worst margin found:", worst_margin)
print("worst p, comp, vals:", worst_p)

# distinct compositions that were ever optimal
from collections import Counter
cnt = Counter(r[1] for r in results)
print("composition frequency among optimal:", cnt)

print("\n--- detailed vals for each composition (first witness) ---")
seen = {}
for r in results:
    p, comp, val, margin = r
    if comp not in seen:
        seen[comp] = (p, val, margin)
for comp, (p, val, margin) in seen.items():
    print(comp, "p=", [round(x,5) for x in p], "phi=", round(val,6), "margin=", round(margin,6))
