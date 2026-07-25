import numpy as np
from probe import xy_best_response

np.random.seed(2)
c3 = 8/15
maxval=0; maxp=None
for trial in range(40):
    p = np.random.dirichlet([1,1,1,1])
    p = sorted(p, reverse=True)
    val, info = xy_best_response(p, 3)
    if val > maxval:
        maxval = val; maxp=(p,info)
    if val > c3+2e-3:
        print("VIOLATION", p, val)
print("n=3 random search max:", maxval, "target", c3, "argmax", maxp[0])
