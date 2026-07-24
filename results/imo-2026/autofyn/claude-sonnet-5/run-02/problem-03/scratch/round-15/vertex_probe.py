import numpy as np
from scipy.optimize import minimize
import itertools, random

def phi(vals):
    s = sorted(vals, reverse=True)
    total = sum(s)
    A = 0.0
    sign = 1
    for v in s:
        A += sign*v
        sign = -sign
    return (total+A)/2

def compositions(m, n):
    # all (c_1,...,c_m) with c_i>=0 sum<=n
    res = []
    def rec(i, remaining, cur):
        if i==m:
            res.append(tuple(cur))
            return
        for c in range(remaining+1):
            rec(i+1, remaining-c, cur+[c])
    rec(0, n, [])
    return res

def eval_composition(p, comp, restarts=25):
    m = len(p)
    # variables: for each piece i with c_i cuts, c_i free split-fraction params in (0,1)^{c_i} via cumulative softmax
    idxs = [i for i in range(m) if comp[i]>0]
    dims = sum(comp)
    if dims==0:
        return phi(p), p[:]
    def unpack(x):
        vals=[]
        pos=0
        for i in range(m):
            c=comp[i]
            if c==0:
                vals.append(p[i])
            else:
                # x[pos:pos+c] logits -> softmax over c+1 parts
                logits = x[pos:pos+c+1] if False else None
                pos+=c
        return vals
    # simpler: reparametrize using c free numbers in (0,1) as cumulative cut positions, sorted
    def build(x):
        vals=[]
        pos=0
        for i in range(m):
            c = comp[i]
            if c==0:
                vals.append(p[i]); continue
            raw = x[pos:pos+c]; pos+=c
            u = 1/(1+np.exp(-raw))  # sigmoid to (0,1)
            u = np.sort(u)
            prev=0.0
            for uu in u:
                vals.append(p[i]*(uu-prev)); prev=uu
            vals.append(p[i]*(1-prev))
        return vals
    best=None; bestx=None
    for _ in range(restarts):
        x0 = np.random.randn(dims)*1.5
        res = minimize(lambda x: phi(build(x)), x0, method='Nelder-Mead',
                        options={'xatol':1e-9,'fatol':1e-12,'maxiter':5000,'maxfev':5000})
        val = res.fun
        if best is None or val<best:
            best=val; bestx=build(res.x)
    return best, bestx

def true_phi_min(p, n, restarts=15):
    m=len(p)
    best=None; beststruct=None; bestcomp=None
    for comp in compositions(m,n):
        val, vals = eval_composition(p, comp, restarts=restarts)
        if best is None or val<best:
            best=val; beststruct=vals; bestcomp=comp
    return best, beststruct, bestcomp

random.seed(2); np.random.seed(2)

witnesses3 = [
 [0.4468,0.2591,0.2251,0.0691-0.0001],  # from round14 report (approx, adjust sum)
]
def normalize(p):
    s=sum(p); return [x/s for x in p]

# Use round-14's own reported near-tight n=3, n=4 witnesses
w3 = normalize([0.4468,0.2591,0.2251,0.0691])
w4 = normalize([0.2933,0.2514,0.2131,0.1338,0.1085])

for name,p,n,an in [("n=3 round14 witness", w3, 3, 8/15), ("n=4 round14 witness", w4, 4, 16/31)]:
    best, struct, comp = true_phi_min(p, n, restarts=20)
    print(name, "p=",[round(x,4) for x in p])
    print("  target a_n*T =", an, " true_phi_min~", best, " margin~", an-best, " comp=",comp)
    print("  final multiset ~", sorted([round(x,4) for x in struct], reverse=True))
