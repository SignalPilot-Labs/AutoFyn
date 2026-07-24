import numpy as np
from scipy.optimize import minimize

def phi_of_fragments(frags):
    frags = sorted(frags, reverse=True)
    return sum(frags[i] for i in range(0,len(frags),2)), frags

def unpack(x,p,comp):
    frags=[]; pos=0; m=len(p)
    for i in range(m):
        c=comp[i]
        if c==0: frags.append(p[i])
        else:
            t=np.sort(1/(1+np.exp(-x[pos:pos+c]))); pos+=c
            cuts=np.concatenate(([0.0],t,[1.0]))
            for j in range(c+1):
                frags.append(p[i]*(cuts[j+1]-cuts[j]))
    return frags

for p,comp in [
    ([0.4537953795379538, 0.2607260726072607, 0.17656765676567657, 0.10891089108910891],(1,0,0,1)),
    ([0.4701492537313433, 0.2562189054726368, 0.1791044776119403, 0.0945273631840796],(1,1,0,0)),
]:
    def obj(x):
        return phi_of_fragments(unpack(x,p,comp))[0]
    best=None;bestx=None
    for _ in range(30):
        x0=np.random.randn(sum(comp))
        res=minimize(obj,x0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-13,'maxiter':5000,'maxfev':5000})
        if best is None or res.fun<best: best=res.fun; bestx=res.x
    frags=unpack(bestx,p,comp)
    print("p=",p,"comp=",comp)
    print("frags sorted=",sorted(frags,reverse=True))
    print("phi=",best)
    print()
