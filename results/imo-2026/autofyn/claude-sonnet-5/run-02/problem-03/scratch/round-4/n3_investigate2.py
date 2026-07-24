import numpy as np
from scipy.optimize import minimize
import random

def optimal_split_of_p(base, k):
    # k = number of fragments p is split into (k-1 cuts), others untouched
    idxs = [k,1,1,1]
    def unpack(x):
        xs = np.sort(np.clip(x,1e-6,1-1e-6))
        prev=0; parts=[]
        for v in xs:
            parts.append((v-prev)*base[0]); prev=v
        parts.append((1-prev)*base[0])
        return parts + base[1:]
    def phi_of(x):
        frags = unpack(x)
        fs = sorted(frags, reverse=True)
        return sum(fs[j] for j in range(0,len(fs),2))
    best=None
    for trial in range(40):
        x0 = np.sort(np.random.rand(k-1))
        res = minimize(phi_of, x0, method='Nelder-Mead', options={'xatol':1e-11,'fatol':1e-14,'maxiter':4000})
        if best is None or res.fun<best[0]:
            best=(res.fun, unpack(res.x))
    return best

random.seed(3)
for trial in range(8):
    denom=1000
    a=sorted(random.sample(range(1,4*denom),3))
    parts=[a[0],a[1]-a[0],a[2]-a[1],4*denom-a[2]]
    if any(x<=0 for x in parts): continue
    base=sorted([x/(4*denom) for x in parts], reverse=True)
    print("base:",[round(v,4) for v in base])
    for k in [2,3,4]:
        val,frags=optimal_split_of_p(base,k)
        equal_val = None
        # compare to equal split
        eq = [base[0]/k]*k + base[1:]
        eq_sorted=sorted(eq,reverse=True)
        equal_val = sum(eq_sorted[j] for j in range(0,len(eq_sorted),2))
        print(f"  k={k}: optimal={val:.6f} equal-split={equal_val:.6f} frags={[round(f,4) for f in sorted(frags,reverse=True)]}")
