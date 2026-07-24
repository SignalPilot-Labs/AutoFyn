import numpy as np
from scipy.optimize import minimize
p1,p2,p3,p4 = 0.4468,0.2591,0.2251,0.0691
T = p1+p2+p3+p4
p=[p1,p2,p3,p4]; p=[x/T for x in p]
p1,p2,p3,p4=p
print("normalized", p1,p2,p3,p4, "sum",sum(p))

def phi(vals):
    s=sorted(vals,reverse=True)
    A=0.0; sign=1
    for v in s:
        A+=sign*v; sign=-sign
    return (sum(s)+A)/2

def f(z):
    x,y = z
    if not (0<=x<=p1 and 0<=y<=p3): return 10
    vals = [x, p1-x, p2, y, p3-y, p4]
    return phi(vals)

best=None
for _ in range(200):
    x0=np.random.rand(2)*[p1,p3]
    r = minimize(f, x0, method='Nelder-Mead', options={'xatol':1e-12,'fatol':1e-14,'maxiter':20000,'maxfev':20000})
    if best is None or r.fun<best[0]:
        best=(r.fun, r.x)
print("best phi", best[0], "x,y=",best[1])
x,y = best[1]
vals = sorted([x,p1-x,p2,y,p3-y,p4], reverse=True)
print("final multiset", vals)
print("x vs y diff", x-y, "p1-x vs y-p3... ", (p1-x), y, (p1-x)-y)
print("p1-x vs p3-y", (p1-x)-(p3-y))
