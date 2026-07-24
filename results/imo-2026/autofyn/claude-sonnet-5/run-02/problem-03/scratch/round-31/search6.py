import sys, random, time
sys.path.insert(0,'/tmp/round-31')
from search2 import objective
from scipy.optimize import differential_evolution, minimize

# Two-stage: DE global then local polish, several seeds, track absolute best
best=-1e9; bestx=None
bounds=[(0.0,1.0)]*4
t0=time.time()
seed=0
while time.time()-t0<240:
    res = differential_evolution(objective, bounds, maxiter=100, popsize=15, tol=1e-10, seed=seed, polish=True, workers=1)
    val=-res.fun
    if val>best:
        best=val; bestx=res.x
        print("seed",seed,"new best",best,bestx, flush=True)
    seed+=1
print("DONE. best=",best,"x=",bestx,"seeds tried",seed)
