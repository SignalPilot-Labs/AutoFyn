import numpy as np
from fractions import Fraction as F
import itertools, random
from scipy.optimize import differential_evolution, minimize
random.seed(1); np.random.seed(1)

def D(n): return 2**(n+1)-1
def alpha(n): return 1.0/D(n)

def A_from_sorted_desc(pieces):
    s = np.sort(pieces)[::-1]
    sign = np.where(np.arange(len(s))%2==0, 1.0, -1.0)
    return float(np.sum(sign*s))

def pieces_from_marks(marks):  # marks: sorted array in (0,1)
    b = np.concatenate([[0.0], np.sort(marks), [1.0]])
    return np.diff(b)

def A_from_marks(marks):
    return A_from_sorted_desc(pieces_from_marks(marks))

# ---- n=2 closed form ----
def phi_n2_closed(a,b,c):  # a<=b<=c, a+b+c=1
    return min(a, b-a, c-b, abs(2*c-1))

# verify at dyadic and scan
dy = (F(1,7),F(2,7),F(4,7))
print("n=2 closed-form Phi(dyadic) =", float(phi_n2_closed(*[float(x) for x in dy])), "alpha=1/7=", 1/7)
# maximize min(a,b-a,c-b,|2c-1|) over a<=b<=c, a+b+c=1
# param a in [0,1/3], b in [a, (1-a)/2 ... ] use 2-param
best=None
for i in range(200001):
    a = random.random()/3
    rem = 1-a
    b = a + random.random()*(rem/2)  # b in [a, a+rem/2], c=1-a-b>=b iff b<=(1-a)/2... ensure b<=c: b <= (1-a)/2
    b = min(b, (1-a)/2)
    c = 1-a-b
    if b<a-1e-12 or c<b-1e-12: continue
    v = phi_n2_closed(a,b,c)
    if best is None or v>best[0]: best=(v,a,b,c)
print(f"n=2 Monte-Carlo max Phi = {best[0]:.6f} at a,b,c=({best[1]:.4f},{best[2]:.4f},{best[3]:.4f})")
print(f"  (dyadic = 1/7={1/7:.6f}, 2/7={2/7:.6f}, 4/7={4/7:.6f})")

# ===================== n=3: Phi via scipy minimization =====================
n=3
def phi_liu_scipy(liu_marks, n_xiang=3, seed=1, restarts=8):
    """min over Xiang's n_xiang marks (reals in (0,1), distinct, not at Liu marks) of A."""
    liu = np.sort(liu_marks)
    liu_set = set(np.round(liu,12))
    def obj(x):
        # x: n_xiang marks; penalize if too close to liu or each other
        xm = np.sort(x)
        pen = 0.0
        for v in xm:
            if v<=0 or v>=1: pen += 10.0*(abs(v)+abs(v-1))
        # distinctness from liu
        for v in xm:
            for w in liu:
                if abs(v-w)<1e-9: pen += 10.0
        for i in range(len(xm)):
            for j in range(i+1,len(xm)):
                if abs(xm[i]-xm[j])<1e-9: pen += 10.0
        marks = np.concatenate([liu, xm])
        return A_from_marks(marks) + pen
    bounds = [(1e-6, 1-1e-6)]*n_xiang
    best = None
    for r in range(restarts):
        rng = np.random.RandomState(seed+r)
        x0 = rng.uniform(1e-6, 1-1e-6, n_xiang)
        x0 = np.sort(x0)
        # avoid collision with liu
        for _ in range(50):
            ok = all(abs(v-w)>1e-4 for v in x0 for w in liu) and len(set(np.round(x0,8)))==n_xiang
            if ok: break
            x0 = np.sort(rng.uniform(1e-6,1-1e-6,n_xiang))
        res = minimize(obj, x0, method='Nelder-Mead', options={'maxiter':5000,'xatol':1e-10,'fatol':1e-12})
        # also differential evolution
        if best is None or res.fun < best:
            best = res.fun
    # global pass
    de = differential_evolution(obj, bounds, seed=seed, tol=1e-12, maxiter=200, popsize=25, polish=True)
    if de.fun < best: best = de.fun
    return best

# dyadic_3
dy3 = np.array([1/15, 3/15, 7/15])  # marks giving pieces (1,2,4,8)/15
print("\n"+"="*60)
print("n=3 dyadic: pieces (1,2,4,8)/15, alpha(3)=1/15=", 1/15)
phi_dy3 = phi_liu_scipy(dy3, restarts=12)
print(f"  Phi(dyadic_3) ~ {phi_dy3:.6f}  (alpha(3)=1/15={1/15:.6f})")

# perturb dyadic: second-order structure
print("\n--- Second-order: perturb dyadic_3, check Phi decreases to first order ---")
eps_vals = [0.02, 0.01, 0.005, 0.002, 0.001]
# perturbation directions in mark-space (3 marks). Use a generic direction.
rng = np.random.RandomState(7)
n_dir = 5
for di in range(n_dir):
    d = rng.randn(3); d = d/np.linalg.norm(d)*0.01
    print(f" direction {di}: d={d}")
    for eps in eps_vals:
        m = dy3 + eps*d
        if np.any(m<=0) or np.any(m>=1): continue
        phi = phi_liu_scipy(m, restarts=4)
        print(f"   eps={eps:.4f}: Phi={phi:.6f}  (alpha=1/15={1/15:.6f}, delta={phi-1/15:+.6f})")
    break  # one direction first; will do more below

