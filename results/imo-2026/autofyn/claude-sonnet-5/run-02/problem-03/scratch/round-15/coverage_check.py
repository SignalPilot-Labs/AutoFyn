import numpy as np
from scipy.optimize import minimize
import random
from fractions import Fraction as F

def phi(vals):
    s=sorted(vals,reverse=True)
    A=0.0; sign=1
    for v in s:
        A+=sign*v; sign=-sign
    return (sum(s)+A)/2

def compositions(m,n):
    res=[]
    def rec(i,remaining,cur):
        if i==m:
            res.append(tuple(cur)); return
        for c in range(remaining+1):
            rec(i+1,remaining-c,cur+[c])
    rec(0,n,[])
    return res

def eval_comp(p,comp,restarts=12):
    m=len(p); dims=sum(comp)
    if dims==0: return phi(p)
    def build(x):
        vals=[]; pos=0
        for i in range(m):
            c=comp[i]
            if c==0: vals.append(p[i]); continue
            raw=x[pos:pos+c]; pos+=c
            raw = np.clip(raw,-30,30)
            u=1/(1+np.exp(-raw)); u=np.sort(u)
            prev=0.0
            for uu in u:
                vals.append(p[i]*(uu-prev)); prev=uu
            vals.append(p[i]*(1-prev))
        return vals
    best=None
    for _ in range(restarts):
        x0=np.random.randn(dims)*1.3
        r=minimize(lambda x: phi(build(x)), x0, method='Nelder-Mead',
                   options={'xatol':1e-9,'fatol':1e-12,'maxiter':3000,'maxfev':3000})
        if best is None or r.fun<best: best=r.fun
    return best

def true_phi_min(p,n,restarts=10):
    m=len(p); best=None; bestcomp=None
    for comp in compositions(m,n):
        v=eval_comp(p,comp,restarts=restarts)
        if best is None or v<best: best=v; bestcomp=comp
    return best,bestcomp

def bisect_topk_best(p,n):
    m=len(p); best=None; bestk=None
    for k in range(0,n+1):
        vals=[]
        for i in range(k): vals+=[p[i]/2,p[i]/2]
        vals+=p[k:]
        v=phi(vals)
        if best is None or v<best: best=v; bestk=k
    return best,bestk

def an(n): 
    D=2**(n+1)-1; return F(2**n,D)

random.seed(7); np.random.seed(7)

def rand_case_b2(n):
    m=n+1
    a_n=float(an(n)); D_n=2**(n+1)-1
    for _ in range(4000):
        p1=random.uniform(0.05,0.499)
        lo=1.0/D_n; hi=min(a_n/2,p1)
        if lo>=hi: continue
        p2=random.uniform(lo+1e-6,hi-1e-6)
        rest=1.0-p1-p2
        if rest<=0: continue
        k=m-2
        if k==0:
            if abs(rest)>1e-9: continue
            tail=[]
        else:
            cuts=sorted(random.uniform(0,1)*rest for _ in range(k-1)) if k>1 else []
            prev=0.0; segs=[]
            for c in cuts: segs.append(c-prev); prev=c
            segs.append(rest-prev)
            tail=sorted(segs,reverse=True)
            if any(t<=1e-9 for t in tail): continue
            if tail[0]>p2+1e-9: continue
        p=[p1,p2]+tail
        if abs(sum(p)-1.0)>1e-6: continue
        yield p

for n in [3,4]:
    print("=== n=",n,"a_n=",float(an(n)))
    got=0
    matches=0
    for p in rand_case_b2(n):
        got+=1
        if got>8: break
        tphi,tcomp = true_phi_min(p,n,restarts=10)
        bphi,bk = bisect_topk_best(p,n)
        match = abs(tphi-bphi)<1e-4
        matches+=match
        print(f" p={[round(x,3) for x in p]} true={tphi:.5f}(comp={tcomp}) bisecttopk={bphi:.5f}(k={bk}) match={match} target={float(an(n)):.5f}")
    print(f"  matches: {matches}/{got}")
