import numpy as np
from fractions import Fraction as F
import itertools, random
from scipy.optimize import differential_evolution, minimize
random.seed(1); np.random.seed(1)

alpha = 1.0/15

def A_from_marks(marks):
    b = np.concatenate([[0.0], np.sort(marks), [1.0]])
    p = np.diff(b)
    s = np.sort(p)[::-1]
    sign = np.where(np.arange(len(s))%2==0, 1.0, -1.0)
    return float(np.sum(sign*s))

def phi_liu(liu_marks, n_xiang=3, seed=1, restarts=4, tol=1e-10, pop=15, de_maxiter=80):
    liu = np.sort(np.asarray(liu_marks,dtype=float))
    def obj(x):
        xm = np.sort(x)
        pen = 0.0
        for v in xm:
            if v<=1e-7: pen += 500*(1e-7-v)
            if v>=1-1e-7: pen += 500*(v-(1-1e-7))
        for v in xm:
            for w in liu:
                if abs(v-w)<1e-7: pen += 500*(1e-7-abs(v-w))
        for i in range(len(xm)):
            for j in range(i+1,len(xm)):
                if abs(xm[i]-xm[j])<1e-7: pen += 500*(1e-7-abs(xm[i]-xm[j]))
        marks = np.concatenate([liu, xm])
        return A_from_marks(marks) + pen
    bounds = [(1e-7, 1-1e-7)]*n_xiang
    best = np.inf
    for r in range(restarts):
        rng = np.random.RandomState(seed*131+r)
        x0 = rng.uniform(1e-5,1-1e-5,n_xiang); x0=np.sort(x0)
        res = minimize(obj, x0, method='Nelder-Mead',
                       options={'maxiter':6000,'xatol':1e-11,'fatol':1e-13})
        if res.fun<best: best=res.fun
    de = differential_evolution(obj, bounds, seed=seed, tol=tol, maxiter=de_maxiter, popsize=pop, polish=True)
    if de.fun<best: best=de.fun
    return best

dy3 = np.array([1/15, 3/15, 7/15])

# ---- Broad scan (reduced) ----
print("=== Broad scan: max Phi over 1200 random n=3 Liu configs ===")
rng = np.random.RandomState(123)
Nsamp=1200
best_phi=-1; best_marks=None; phis=[]
for i in range(Nsamp):
    m = np.sort(rng.uniform(0.02,0.98,3))
    if len(set(np.round(m,8)))<3: continue
    phi = phi_liu(m, restarts=2, pop=12, de_maxiter=50)
    phis.append(phi)
    if phi>best_phi: best_phi=phi; best_marks=m.copy()
print(f"max Phi in sample = {best_phi:.6f}  (alpha=1/15={alpha:.6f})")
print(f"argmax marks = {best_marks.round(4)}  (dyadic={[round(x,4) for x in [1/15,3/15,7/15]]})")
phis=np.array(phis)
print(f"Phi: min={phis.min():.4f}  50%={np.percentile(phis,50):.4f}  95%={np.percentile(phis,95):.4f}  max={phis.max():.4f}")
print(f"#configs with Phi > 0.5*alpha: {(phis>0.5*alpha).sum()}")
print(f"#configs with Phi > 0.9*alpha: {(phis>0.9*alpha).sum()}")

# ---- kink fit ----
print("\n=== Kink fit: fixed dir, fit delta ~ -c*eps ===")
d = np.array([0.5,-0.4,0.3]); d=d/np.linalg.norm(d)
eps_grid = np.array([0.001,0.002,0.004,0.008,0.016])
ds=[]
for eps in eps_grid:
    m = dy3 + eps*d
    if np.any(m<=0) or np.any(m>=1): ds.append(np.nan); continue
    phi = phi_liu(m, restarts=4, pop=20)
    ds.append(phi-alpha)
ds=np.array(ds)
c = np.dot(ds, -eps_grid)/np.dot(eps_grid,eps_grid)
print(f"  slope c (delta=-c*eps): {c:.4f}")
for eps,d_ in zip(eps_grid,ds):
    print(f"  eps={eps:.5f}: delta={d_:+.3e}  ratio(delta/(-c*eps))={d_/(-c*eps):.3f}")

# near dyadic
print("\n--- near-dyadic perturbations ---")
for off in [0.003,0.01,0.03]:
    m = dy3 + np.array([off,-off/2,off/3]); m=np.sort(m)
    phi = phi_liu(m, restarts=4, pop=20)
    print(f"  +[{off},-{-off/2:.3f},+{off/3:.3f}]: Phi={phi:.6f}  delta={phi-alpha:+.3e}")
