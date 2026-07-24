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
[0.4537953795379538, 0.2607260726072607, 0.17656765676567657, 0.10891089108910891],
[0.4701492537313433, 0.2562189054726368, 0.1791044776119403, 0.0945273631840796],
[0.4831730769230769, 0.25, 0.17548076923076922, 0.09134615384615384],
]
for p in witnesses:
    tm,comp=true_phimin(p)
    print(p,"true_min",tm,"gap",a3-tm,"comp",comp)

print("\n--- final tiny residual ---")
final_res = [
[0.4965034965034965, 0.24825174825174826, 0.16958041958041958, 0.08566433566433566],
[0.44881889763779526, 0.25984251968503935, 0.1889763779527559, 0.10236220472440945],
[0.4940577249575552, 0.26485568760611206, 0.15959252971137522, 0.08149405772495756],
]
for p in final_res:
    tm,comp = true_phimin(p)
    print(p,"true_min",tm,"gap",a3-tm,"comp",comp)
