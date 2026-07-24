import sys, random
sys.path.insert(0,'/tmp/round-31')
from enum_chambers import gen_chambers

CHAMBERS = gen_chambers(5,4)

def A_sorted_desc(vals):
    s = sorted(vals, reverse=True)
    tot = 0.0
    sign = 1
    for v in s:
        tot += sign*v
        sign *= -1
    return tot

def phi_for_chamber(p, spec):
    partition, hosts, bisect_set = spec
    Q = []
    for B, h in zip(partition, hosts):
        if len(B) == 1:
            i = B[0]
            if i in bisect_set:
                continue
            else:
                Q.append(p[i])
        else:
            others = [i for i in B if i != h]
            s = sum(p[i] for i in others)
            rho = p[h] - s
            if rho < -1e-12:
                return None
            Q.append(max(rho,0.0))
    T = sum(p)
    return (T + A_sorted_desc(Q))/2.0

def best_phi(p):
    best = None
    for spec in CHAMBERS:
        v = phi_for_chamber(p, spec)
        if v is None:
            continue
        if best is None or v < best:
            best = v
    return best

a4 = 16.0/31.0

def in_region(p):
    T = sum(p)
    p1,p2 = p[0], p[1]
    return p1 < 0.5*T*(1-1e-9) and (T/31.0)*(1+1e-9) < p2 < (8*T/31.0)*(1-1e-9)

def objective(x):
    p1 = 1.0
    a,b,c,d = x
    vals = sorted([a,b,c,d], reverse=True)
    p2,p3,p4,p5 = [v*p1 for v in vals]
    p = [p1,p2,p3,p4,p5]
    if not in_region(p):
        return 1e6
    bp = best_phi(p)
    if bp is None:
        return 1e6
    T = sum(p)
    return -(bp - a4*T)

if __name__ == "__main__":
    from scipy.optimize import differential_evolution
    bounds = [(0.0,1.0)]*4
    result = differential_evolution(objective, bounds, maxiter=200, popsize=25, tol=1e-12, seed=1, polish=True, workers=1)
    print("DE best (bp-a4T):", -result.fun, "at x=", result.x)
    vals = sorted(result.x, reverse=True)
    p = [1.0]+vals
    print("p:", p)
