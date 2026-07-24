import sys, random
sys.path.insert(0,'/tmp/round-31')
from search2 import objective
from scipy.optimize import minimize
import numpy as np

random.seed(42)
best = -1e9
best_x = None
for i in range(4000):
    x0 = [random.random() for _ in range(4)]
    res = minimize(objective, x0, method='Nelder-Mead',
                    options={'xatol':1e-10,'fatol':1e-12,'maxiter':2000})
    val = -res.fun
    if val > best:
        best = val
        best_x = res.x
        print(i, best, best_x)
print("FINAL BEST", best, best_x)
