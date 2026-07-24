import sys, random, time
sys.path.insert(0,'/tmp/round-31')
from search2 import objective
from scipy.optimize import minimize

random.seed(42)
best = -1e9
best_x = None
t0=time.time()
i=0
while time.time()-t0 < 90:
    i+=1
    x0 = [random.random() for _ in range(4)]
    res = minimize(objective, x0, method='Nelder-Mead',
                    options={'xatol':1e-9,'fatol':1e-11,'maxiter':300})
    val = -res.fun
    if val > best:
        best = val
        best_x = res.x
        print(i, best, best_x, flush=True)
print("FINAL BEST", best, best_x, "iters", i)
