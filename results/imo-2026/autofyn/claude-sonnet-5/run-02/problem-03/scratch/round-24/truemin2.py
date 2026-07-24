import itertools
import numpy as np
from scipy.optimize import minimize

def phi_of_fragments(frags):
    frags = sorted(frags, reverse=True)
    return sum(frags[i] for i in range(0,len(frags),2))

def eval_composition(p, comp):
    m = len(p)
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
                t = np.sort(1/(1+np.exp(-x[pos:pos+c])))
                pos+=c
                cuts = np.concatenate(([0.0], t, [1.0]))
                for j in range(c+1):
                    frags.append(p[i]*(cuts[j+1]-cuts[j]))
        return frags
    def obj(x):
        return phi_of_fragments(unpack(x))
    best=None
    for _ in range(6):
        x0=np.random.randn(nvars)
        res=minimize(obj,x0,method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-12,'maxiter':4000,'maxfev':4000})
        if best is None or res.fun<best: best=res.fun
    return best

def true_phimin(p, n=3):
    m=len(p); best=None; bestcomp=None
    for comp in itertools.product(range(n+1), repeat=m):
        if sum(comp)>n or sum(comp)==0: continue
        v=eval_composition(p,comp)
        if best is None or v<best: best=v; bestcomp=comp
    return best, bestcomp

a3=8/15
witnesses = [
[0.43843283582089554, 0.2555970149253731, 0.1884328358208955, 0.11753731343283583],
[0.49534450651769085, 0.25512104283054005, 0.18063314711359404, 0.06890130353817504],
[0.4939467312348668, 0.24939467312348668, 0.1694915254237288, 0.08716707021791767],
[0.4849699398797595, 0.25851703406813625, 0.17234468937875752, 0.0841683366733467],
]
for p in witnesses:
    tm,comp = true_phimin(p)
    print(p,"true_min",tm,"a3T",a3,"gap",a3-tm,"comp",comp)

print("\ncheck composition (1,0,0,1) asymmetric optimum vs symmetric bisect")
for p in witnesses:
    v = eval_composition(p, (1,0,0,1))
    p1,p2,p3,p4=p
    sym = (p1+p4)/2 + p2  # symmetric bisect p1,p4, middle untouched
    print(p, "asym_opt", v, "sym_bisect", sym)
