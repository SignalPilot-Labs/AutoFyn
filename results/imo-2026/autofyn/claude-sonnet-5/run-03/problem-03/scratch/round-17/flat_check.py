import numpy as np
from scipy.optimize import minimize_scalar

def oddsum(vals):
    v = sorted(vals, reverse=True)
    return sum(v[i] for i in range(0, len(v), 2))

p = (0.4211,0.3348,0.1910,0.0531)  # point 3
# m=(1,0,1,0): split piece0 into (a, p0-a), piece2 into (x, p2-x)
# fix piece0 split near optimum found: (0.349263,0.071837); vary x for piece2
a0, a1 = 0.349263, 0.071837
p2 = p[2]
xs = np.linspace(0.001, p2-0.001, 400)
vals = []
for x in xs:
    frags = [a0, a1, p[1], x, p2-x, p[3]]
    vals.append(oddsum(frags))
vals = np.array(vals)
print("min val", vals.min(), "at x=", xs[np.argmin(vals)])
# print range where val is within 1e-9 of min
mask = vals < vals.min() + 1e-9
print("flat region x in [", xs[mask].min(), ",", xs[mask].max(), "] width=", xs[mask].max()-xs[mask].min())
print("value at x=0.0955 (bisection):", oddsum([a0,a1,p[1],p2/2,p2/2,p[3]]))
print("value at x=0.01:", oddsum([a0,a1,p[1],0.01,p2-0.01,p[3]]))
print("value at x=0.15:", oddsum([a0,a1,p[1],0.15,p2-0.15,p[3]]))
