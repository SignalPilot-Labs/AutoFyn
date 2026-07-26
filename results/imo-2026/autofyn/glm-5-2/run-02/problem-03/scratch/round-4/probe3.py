import numpy as np
from fractions import Fraction as F
import itertools, random
from scipy.optimize import differential_evolution, minimize
random.seed(1); np.random.seed(1)

def D(n): return 2**(n+1)-1
alpha = 1.0/15

def A_from_marks(marks):
    b = np.concatenate([[0.0], np.sort(marks), [1.0]])
    p = np.diff(b)
    s = np.sort(p)[::-1]
    sign = np.where(np.arange(len(s))%2==0, 1.0, -1.0)
    return float(np.sum(sign*s))

def phi_liu_scipy(liu_marks, n_xiang=3, seed=1, restarts=12, tol=1e-11):
    liu = np.sort(np.asarray(liu_marks,dtype=float))
    def obj(x):
        xm = np.sort(x)
        pen = 0.0
        for v in xm:
            if v<=1e-7: pen += 1000*(1e-7-v)
            if v>=1-1e-7: pen += 1000*(v-(1-1e-7))
        for v in xm:
            for w in liu:
                if abs(v-w)<1e-7: pen += 1000*(1e-7-abs(v-w))
        for i in range(len(xm)):
            for j in range(i+1,len(xm)):
                if abs(xm[i]-xm[j])<1e-7: pen += 1000*(1e-7-abs(xm[i]-xm[j]))
        marks = np.concatenate([liu, xm])
        return A_from_marks(marks) + pen
    bounds = [(1e-7, 1-1e-7)]*n_xiang
    best = np.inf
    for r in range(restarts):
        rng = np.random.RandomState(seed*1000+r)
        x0 = rng.uniform(1e-5,1-1e-5,n_xiang); x0=np.sort(x0)
        res = minimize(obj, x0, method='Nelder-Mead',
                       options={'maxiter':20000,'xatol':1e-12,'fatol':1e-14})
        if res.fun<best: best=res.fun
    de = differential_evolution(obj, bounds, seed=seed, tol=tol, maxiter=400, popsize=40, polish=True, mutation=(0.5,1.5))
    if de.fun<best: best=de.fun
    return best

dy3 = np.array([1/15, 3/15, 7/15])
alpha = 1.0/15
phi_dy = phi_liu_scipy(dy3, restarts=20)
print(f"Phi(dyadic_3) = {phi_dy:.10f}  alpha=1/15={alpha:.10f}  err={phi_dy-alpha:.2e}")

# ---- Many perturbation directions, fixed small eps ----
print("\n--- strict local max test: many directions, eps=0.005 ---")
eps = 0.005
rng = np.random.RandomState(42)
ndir=20
dec=0; inc=0; flat=0
deltas=[]
for di in range(ndir):
    d = rng.randn(3); d=d/np.linalg.norm(d)
    m = dy3 + eps*d
    if np.any(m<=0) or np.any(m>=1): continue
    phi = phi_liu_scipy(m, restarts=6)
    delta = phi - alpha
    deltas.append(delta)
    flag = "DEC" if delta<-1e-7 else ("INC" if delta>1e-7 else "FLAT")
    if flag=="DEC": dec+=1
    elif flag=="INC": inc+=1
    else: flat+=1
    print(f" dir {di:2d}: d={d.round(4)}  Phi-1/15 = {delta:+.2e}  {flag}")
print(f"\nsummary: DEC={dec} INC={inc} FLAT={flat}  (need DEC=all for strict local max)")

# ---- second-order scaling: pick one direction, eps grid ----
print("\n--- scaling test (one direction): is delta ~ eps^2 ? ---")
d = np.array([0.7,-0.6,0.38]); d=d/np.linalg.norm(d)
for eps in [0.04,0.02,0.01,0.005,0.0025]:
    m = dy3 + eps*d
    if np.any(m<=0) or np.any(m>=1): 
        print(f" eps={eps}: out of bounds"); continue
    phi = phi_liu_scipy(m, restarts=8)
    delta = phi-alpha
    print(f" eps={eps:.5f}: Phi={phi:.8f}  delta={delta:+.3e}  delta/eps^2={delta/eps**2:+.3e}")

# ---- non-dyadic configs FAR from dyadic: confirm Phi < 1/15 ----
print("\n--- non-dyadic n=3 configs: confirm Phi < 1/15 ---")
test_configs = [
    ("equal (1/4)", [0.25,0.5,0.75]),
    ("(.5,.3,.15,.05) pieces", [0.05,0.20,0.50]),   # marks at 0.05,0.20,0.50 -> pieces .05,.15,.3,.5
    ("(0.6,0.2,0.1,0.1) pieces", [0.1,0.3,0.5]),
    ("extreme dominant", [0.0333,0.0666,0.1]),   # pieces ~ .033,.033,.033,.9
    ("random1", sorted(np.random.RandomState(3).uniform(0,1,3))),
    ("random2", sorted(np.random.RandomState(11).uniform(0,1,3))),
    ("near dyadic shifted", [1/15+0.05, 3/15+0.02, 7/15-0.03]),
]
for name,marks in test_configs:
    marks = sorted(marks)
    if any(m<=0 or m>=1 for m in marks): 
        print(f"  {name}: OOB"); continue
    if len(set(np.round(marks,8)))<3: 
        print(f"  {name}: dup"); continue
    # pieces
    b=[0]+list(marks)+[1]; pcs=np.diff(b)
    phi = phi_liu_scipy(marks, restarts=10)
    print(f"  {name}: pieces={np.round(sorted(pcs,reverse=True),4).tolist()}  Phi={phi:.6f}  delta={phi-alpha:+.4e}")
