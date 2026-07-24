import sys, random
sys.path.insert(0,'/tmp/round-31')
from enum_chambers import gen_chambers
from fractions import Fraction as F

CHAMBERS = gen_chambers(5,4)
print("num chamber specs:", len(CHAMBERS))

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
    # x: 4 free values representing p2..p5 fractions between 0 and p1, we need sorted p1>=p2>=p3>=p4>=p5>0
    # parameterize via p1=1 fixed (scale-free), and p2,p3,p4,p5 as fractions of p1 in [0,1], sorted descending
    p1 = 1.0
    a,b,c,d = x
    # order enforce via sorting cumulative products isn't ideal; instead use x in [0,1]^4 sorted descending scaled by p1
    vals = sorted([a,b,c,d], reverse=True)
    p2,p3,p4,p5 = [v*p1 for v in vals]
    p = [p1,p2,p3,p4,p5]
    if not in_region(p):
        return 1e6  # penalize infeasible heavily (will be filtered)
    bp = best_phi(p)
    if bp is None:
        return 1e6
    T = sum(p)
    return -(bp - a4*T)  # we want to maximize (bp - a4T); minimize negative

best_val = -1e9
best_p = None
random.seed(0)
import itertools
N = 300000
for _ in range(N):
    x = [random.random() for _ in range(4)]
    val = -objective(x)
    if val > best_val:
        best_val = val
        best_p = x[:]

print("best (bp - a4T) found via random search:", best_val)
print("best x:", best_p)
vals = sorted(best_p, reverse=True)
p = [1.0]+[v for v in vals]
print("p:", p, "T=",sum(p))

# refine with scipy differential_evolution to search harder for violations
from scipy.optimize import differential_evolution

def obj2(x):
    return objective(x)

bounds = [(0.0,1.0)]*4
result = differential_evolution(obj2, bounds, maxiter=300, popsize=40, tol=1e-12, seed=1, polish=True, workers=-1)
print("DE best (bp-a4T):", -result.fun, "at x=", result.x)
vals = sorted(result.x, reverse=True)
p = [1.0]+vals
print("p:", p)
