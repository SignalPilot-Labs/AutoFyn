import numpy as np
from scipy.optimize import minimize
import itertools

base = [3/8, 1/4, 1/4, 1/8]  # p,q,r,s
comp = (2,0,0,0)  # split p into 3 fragments, others untouched
idxs = [c+1 for c in comp]

def unpack(x):
    frags=[]
    pos=0
    for i,k in enumerate(idxs):
        if k==1:
            frags.append(base[i])
        else:
            xs = x[pos:pos+k-1]
            pos += k-1
            xs = np.sort(np.clip(xs,1e-6,1-1e-6))
            prev=0
            parts=[]
            for v in xs:
                parts.append((v-prev)*base[i])
                prev=v
            parts.append((1-prev)*base[i])
            frags += parts
    return frags

def phi_of(x):
    frags = unpack(x)
    frags_sorted = sorted(frags, reverse=True)
    return sum(frags_sorted[j] for j in range(0,len(frags_sorted),2))

best=None
for trial in range(30):
    x0 = np.random.rand(2)
    res = minimize(phi_of, x0, method='Nelder-Mead', options={'xatol':1e-10,'fatol':1e-14,'maxiter':5000})
    if best is None or res.fun < best[0]:
        best = (res.fun, res.x)

print("min phi:", best[0])
print("fragments:", sorted(unpack(best[1]), reverse=True))
