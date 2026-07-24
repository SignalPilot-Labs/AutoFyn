import numpy as np
from scipy.optimize import differential_evolution
import itertools

def ladder(n):
    denom = 2**(n+1) - 1
    return [ (2**(n+1-i)) / denom for i in range(1, n+2)]

def compositions(total_budget, parts):
    def rec(parts_left, budget_left):
        if parts_left == 0:
            yield ()
            return
        for c in range(budget_left+1):
            for rest in rec(parts_left-1, budget_left-c):
                yield (c,) + rest
    return list(rec(parts, total_budget))

def phi_from_fragments(fragments_list):
    allvals = []
    for frags in fragments_list:
        allvals.extend(frags)
    allvals.sort(reverse=True)
    return sum(allvals[k] for k in range(0,len(allvals),2))

def make_objective(p, comp):
    # variable layout: for piece i with c_i cuts, c_i free vars in [0,p_i], sorted implicitly ok;
    # last fragment = p_i - sum(vars for that piece), clip negative via penalty
    nvars = sum(comp)
    def obj(x):
        idx=0
        fragments_list=[]
        penalty=0.0
        for i,c in enumerate(comp):
            if c==0:
                fragments_list.append([p[i]])
            else:
                vs = x[idx:idx+c]
                idx+=c
                s = sum(vs)
                last = p[i]-s
                if last < 0:
                    penalty += 1000*(-last)
                    last=0
                frags = list(vs)+[last]
                fragments_list.append(frags)
        val = phi_from_fragments(fragments_list)
        return val + penalty
    bounds = []
    for i,c in enumerate(comp):
        if c>0:
            for _ in range(c):
                bounds.append((0,p[i]))
    return obj, bounds

def min_phi_for_composition(p, comp, seed=0):
    obj, bounds = make_objective(p, comp)
    if not bounds:
        val = obj(np.array([]))
        return val, np.array([])
    res = differential_evolution(obj, bounds, seed=seed, tol=1e-12, maxiter=300, popsize=25, polish=True, mutation=(0.3,1.7), recombination=0.9)
    return res.fun, res.x

def explore(n, verbose=True):
    p = ladder(n)
    target = 2**n/(2**(n+1)-1)
    comps = compositions(n, n+1)
    best_val = None
    best = []
    for comp in comps:
        val, x = min_phi_for_composition(p, comp)
        if best_val is None or val < best_val - 1e-7:
            best_val = val
            best = [(comp,x,val)]
        elif abs(val-best_val) < 1e-6:
            best.append((comp,x,val))
    if verbose:
        print(f"n={n} target={target:.8f} found_min={best_val:.8f} diff={best_val-target:.2e}")
        for comp,x,val in best:
            print("  comp", comp, "x=", np.round(x,6), "val=", round(val,8))
    return p, target, best_val, best

if __name__=="__main__":
    import sys
    n = int(sys.argv[1])
    explore(n)
