import numpy as np
from scipy.optimize import minimize

def oddsum(vals):
    v = sorted(vals, reverse=True)
    return sum(v[i] for i in range(0, len(v), 2))

p = (0.4211,0.3348,0.1910,0.0531)  # point 3
p0,p1,p2,p3 = p

def best_a_for_x(x):
    # optimize a in (0,p0) for fixed x
    def f(a):
        return oddsum([a[0], p0-a[0], p1, x, p2-x, p3])
    res = minimize(f, [p0/2], method='Nelder-Mead', options={'xatol':1e-12,'fatol':1e-14})
    return res.fun, res.x[0]

xs = np.linspace(0.001, p2-0.001, 800)
vals = []
for x in xs:
    v,a = best_a_for_x(x)
    vals.append(v)
vals = np.array(vals)
i = np.argmin(vals)
print("global min", vals.min(), "at x=", xs[i])
mask = vals < vals.min()+1e-7
print("flat/near-min x range:", xs[mask].min(), xs[mask].max(), "width", xs[mask].max()-xs[mask].min())
print("value at bisection x=p2/2=",p2/2, ":", best_a_for_x(p2/2))
