import sys
sys.path.insert(0,'/tmp/round-31')
from search2 import objective, best_phi, a4, in_region
from scipy.optimize import differential_evolution
import numpy as np

best_overall = -1e9
best_x = None
bounds = [(0.001,0.999)]*4
for seed in range(6):
    result = differential_evolution(objective, bounds, maxiter=150, popsize=20, tol=1e-10, seed=seed, polish=True, workers=1)
    val = -result.fun
    print(f"seed={seed} best={val} x={result.x}")
    if val > best_overall:
        best_overall = val
        best_x = result.x

print("OVERALL BEST:", best_overall, best_x)
