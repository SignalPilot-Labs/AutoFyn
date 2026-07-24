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

p=[0.43843283582089554, 0.2555970149253731, 0.1884328358208955, 0.11753731343283583]
comp=(1,0,0,1)
def obj(x):
    return phi_of_fragments(unpack(x,p,comp))[0]
best=None;bestx=None
for _ in range(20):
    x0=np.random.randn(2)
    res=minimize(obj,x0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-13,'maxiter':5000,'maxfev':5000})
    if best is None or res.fun<best: best=res.fun; bestx=res.x
frags = unpack(bestx,p,comp)
print("p=",p)
print("frags=",sorted(frags,reverse=True))
print("phi=",best)
