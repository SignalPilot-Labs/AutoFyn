import itertools, random
import numpy as np
from scipy.optimize import minimize

def phi_of_fragments(frags):
    frags = sorted(frags, reverse=True)
    return sum(frags[i] for i in range(0,len(frags),2))

def eval_composition(p, comp):
    # comp: tuple of cuts per piece, sum(comp)<=n
    m = len(p)
    # variables: for piece i with c_i cuts, c_i free split points in (0,1) sorted -> c_i+1 fragments
    idxs = [i for i in range(m) if comp[i]>0]
    nvars = sum(comp)
    if nvars==0:
        return phi_of_fragments(p)
    def unpack(x):
        frags=[]
        pos=0
        for i in range(m):
            c = comp[i]
            if c==0:
                frags.append(p[i])
            else:
                t = np.sort(1/(1+np.exp(-x[pos:pos+c])))  # squash to (0,1) sorted
                pos+=c
                cuts = np.concatenate(([0.0], t, [1.0]))
                for j in range(c+1):
                    frags.append(p[i]*(cuts[j+1]-cuts[j]))
        return frags
    def obj(x):
        return phi_of_fragments(unpack(x))
    best = None
    for _ in range(6):
        x0 = np.random.randn(nvars)
        res = minimize(obj, x0, method='Nelder-Mead', options={'xatol':1e-9,'fatol':1e-12,'maxiter':4000,'maxfev':4000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def true_phimin(p, n=3):
    m=len(p)
    best=None
    bestcomp=None
    for comp in itertools.product(range(n+1), repeat=m):
        if sum(comp) > n or sum(comp)==0:
            continue
        v = eval_composition(p, comp)
        if best is None or v<best:
            best=v; bestcomp=comp
    return best, bestcomp

a3 = 8/15
witnesses = [
[0.3579277864992151, 0.24332810047095763, 0.23861852433281006, 0.16012558869701726],
[0.3073248407643312, 0.2611464968152866, 0.25477707006369427, 0.1767515923566879],
[0.36812411847672777, 0.2552891396332863, 0.231311706629055, 0.14527503526093088],
[0.32362459546925565, 0.26537216828478966, 0.2588996763754045, 0.15210355987055016],
[0.36231884057971014, 0.2576489533011272, 0.2560386473429952, 0.12399355877616747],
]
for p in witnesses:
    tm, comp = true_phimin(p)
    print(p, "true_min~", tm, "a3T=",a3, "gap", a3-tm, "best comp", comp)

print("\n--- checking Theorem D' (bisect top+bottom, recurse on middle) coverage ---")
for p in witnesses:
    p1,p2,p3,p4 = p
    # middle {p2,p3}, budget 1: best of untouched (Phi'=p2) vs bisect p2 (compute exactly)
    # bisect p2: fragments p2/2,p2/2,p3
    frags = sorted([p2/2,p2/2,p3], reverse=True)
    phi_bisect_mid = sum(frags[i] for i in range(0,3,2))
    phi_mid = min(p2, phi_bisect_mid)
    phiD = (p1+p4)/2 + phi_mid
    print(p, "ThmD' value=", phiD, "a3T=",a3, "covers?", phiD<=a3)
