import numpy as np
from scipy.optimize import minimize

def oddsum(vals):
    v = sorted(vals, reverse=True)
    return sum(v[i] for i in range(0, len(v), 2))

p = (0.4416,0.3035,0.1851,0.0698)
p0,p1,p2,p3 = p

def best_for(a,x):
    return oddsum([a, p0-a, p1, x, p2-x, p3])

def best_a_for_x(x):
    def f(a):
        return best_for(a[0], x)
    res = minimize(f, [p0*0.3], method='Nelder-Mead', options={'xatol':1e-13,'fatol':1e-15,'maxiter':5000})
    return res.fun, res.x[0]

xs = np.linspace(0.0005, p2-0.0005, 2000)
vals = np.array([best_a_for_x(x)[0] for x in xs])
i = np.argmin(vals)
print("min", vals.min(), "at x=", xs[i], " vs p3=",p3, " vs p2/2=",p2/2)
val_at_p3, a_at = best_a_for_x(p3)
print("value forcing x=p3 exactly:", val_at_p3, "a=",a_at)
