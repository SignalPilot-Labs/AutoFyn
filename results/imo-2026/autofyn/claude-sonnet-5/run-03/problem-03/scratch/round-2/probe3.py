import numpy as np
from probe import xy_best_response

np.random.seed(1)
c2 = 4/7
maxval = 0
maxp = None
for trial in range(60):
    # random dirichlet on 3 pieces
    p = np.random.dirichlet([1,1,1])
    p = sorted(p, reverse=True)
    val, info = xy_best_response(p, 2)
    if val > maxval:
        maxval = val
        maxp = (p, info)
    if val > c2 + 1e-3:
        print("VIOLATION", p, val)
print("n=2 random search max val:", maxval, "target", c2)
print("argmax p:", maxp[0], "dist:", maxp[1][0])
