import numpy as np
from scipy.optimize import differential_evolution
from heuristic import ladder, compositions, make_objective

def min_phi_for_composition(p, comp, seed=0):
    obj, bounds = make_objective(p, comp)
    if not bounds:
        return obj(np.array([])), np.array([])
    res = differential_evolution(obj, bounds, seed=seed, tol=1e-10, maxiter=150, popsize=15, polish=True)
    return res.fun, res.x

def explore(n):
    p = ladder(n)
    target = 2**n/(2**(n+1)-1)
    comps = compositions(n, n+1)
    print(f"n={n}, num compositions={len(comps)}, target={target:.8f}")
    best_val=None; best=[]
    for comp in comps:
        val,x = min_phi_for_composition(p, comp)
        if best_val is None or val < best_val - 1e-6:
            best_val = val; best=[(comp,x,val)]
        elif abs(val-best_val)<1e-5:
            best.append((comp,x,val))
    print("found_min=",best_val,"diff=",best_val-target)
    print("num tied winners:", len(best))
    for comp,x,val in best[:40]:
        print(" ", comp, np.round(x,5))
    return best

if __name__=="__main__":
    import sys
    explore(int(sys.argv[1]))
