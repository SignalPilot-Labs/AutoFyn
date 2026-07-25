import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as F
import itertools, random

def e0_coords(n):
    # exact via Fraction
    gamma = F(1, 2**(n+1)-1)
    pn1 = (F(2) - F(n*(n+1))*gamma) / F(2*(n+1))
    p = [pn1 + F(n+1-i)*gamma for i in range(1, n+2)]  # p[0]=p_1 ... p[n]=p_{n+1}
    return p  # descending order already (p_1 largest ... p_{n+1} smallest)

def cn(n):
    return F(2**n, 2**(n+1)-1)

def altsum_from_sorted_desc(vals):
    s=0.0
    for idx,v in enumerate(vals):
        if idx%2==0: s+=v
        else: s-=v
    return s

def oddsum_from_sorted_desc(vals):
    # OddSum = 1/2*(sum + AltSum); sum(vals) should be 1 (total mass), but compute directly for safety
    total = sum(vals)
    alt = altsum_from_sorted_desc(vals)
    return 0.5*(total+alt)

def evaluate(n, active_idx, x):
    """active_idx: list of indices (0-based) among 0..n that are split into 2 fragments each.
       x: array of split fractions in (0,1) for each active piece: fragment1 = x_i * p_i.
       Returns OddSum (float)."""
    p = [float(v) for v in e0_coords(n)]
    frags=[]
    active_set=set(active_idx)
    for i,v in enumerate(p):
        if i in active_set:
            j = active_idx.index(i)
            xi = x[j]
            xi = min(max(xi,1e-9),1-1e-9)
            frags.append(xi*v)
            frags.append((1-xi)*v)
        else:
            frags.append(v)
    frags.sort(reverse=True)
    return oddsum_from_sorted_desc(frags)

def best_for_active_set(n, active_idx, nrestarts=40, seed=0):
    rng = np.random.default_rng(seed)
    s=len(active_idx)
    best=None
    # structured starts: 0.5 (self tie), plus random
    starts=[np.full(s,0.5)]
    for _ in range(nrestarts):
        starts.append(rng.uniform(0.01,0.99,size=s))
    for x0 in starts:
        res = minimize(lambda x: evaluate(n, active_idx, x), x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':20000,'maxfev':20000})
        val = res.fun
        if best is None or val < best:
            best = val
    return best

def scan(n, s_values, restarts=30):
    results={}
    N=n+1
    for s in s_values:
        best_overall=None
        best_desc=None
        # candidate active sets: top-s (indices 0..s-1), bottom-s (indices N-s..N-1),
        # and a few random subsets
        candidates=[]
        candidates.append(('top', list(range(s))))
        candidates.append(('bottom', list(range(N-s,N))))
        # alternate
        if s<=N:
            alt = sorted(random.sample(range(N), s))
            candidates.append(('rand', alt))
        for name, idxs in candidates:
            val = best_for_active_set(n, idxs, nrestarts=restarts)
            if best_overall is None or val<best_overall:
                best_overall=val
                best_desc=name
        results[s]=(best_overall,best_desc)
    return results

import sys
for n in [6,8]:
    print(f"=== n={n}, c(n)={float(cn(n)):.6f} ===")
    N=n+1
    svals = list(range(1,N))  # s=1..n
    res = scan(n, svals, restarts=25)
    for s in svals:
        val,desc = res[s]
        print(f"s={s:2d} best_OddSum={val:.6f}  excess={val-float(cn(n)):+.6e}  ({desc})")
