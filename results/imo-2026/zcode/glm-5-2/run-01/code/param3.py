import sympy as sp
from sympy import symbols, cos, sin, simplify, trigsimp, expand_trig, Rational, sqrt, factor, cancel, together, numer, denom

p,q = symbols('p q', positive=True)
a,b,g = symbols('a b g', positive=True)

# From the computation, denominators simplify:
# For K: denom = p*sin(2a+g) + q*cos(2a+g). Let's denote Dk = p sin(2a+g)+q cos(2a+g).
# Ky = sin(a)*[ -p^2 sin(a+g) + p sin(a+g) - q^2 sin(a+g) + q cos(a+g) ] / Dk
#    = sin(a)*[ (p-p^2-q^2) sin(a+g) + q cos(a+g) ] / Dk
# Kx = [ (p^2+q^2) sin(a+g) cos a + p sin a cos(a+g) - q sin a sin(a+g) ] / Dk
#    = [ R^2 sin(a+g) cos a + sin a (p cos(a+g) - q sin(a+g)) ] / Dk
#   note p cos(a+g) - q sin(a+g) = R cos( (a+g) + atan2(q,p) )... 

# Let me set theta = atan2(q,p), R=sqrt(p^2+q^2), so p=R cos th, q = R sin th.
th = symbols('theta', positive=True)
R = symbols('R', positive=True)
pp = R*cos(th); qq = R*sin(th)

# Redefine using R, theta for cleanliness, then we can convert back.
# Actually let me just recompute K,L from scratch in terms of R, theta.
# C = (R cos th, R sin th). CA unit = (-cos th, -sin th).
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
CAu = (-cos(th), -sin(th))
dir_BK = (-cos(a), sin(a))
dir_BL = (-cos(a+b), sin(a+b))
dir_CL = (cos(th)*CAu[0]-sin(a)*CAu[1] + 0, ) # = rot by a
# rot(CAu, a):
def rot(vec,t):
    x,y=vec; return (cos(t)*x - sin(t)*y, sin(t)*x + cos(t)*y)
dir_CL = rot(CAu, a)
dir_CK = rot(CAu, a+g)

# w = C - B = (R cos th - 1, R sin th)
w = (R*cos(th)-1, R*sin(th))
def intersect(d1,d2,w):
    t = cross(w,d2)/cross(d1,d2)
    return (1 + t*d1[0], 0 + t*d1[1])
K = intersect(dir_BK, dir_CK, w)
L = intersect(dir_BL, dir_CL, w)
Kx = trigsimp(K[0]); Ky = trigsimp(K[1])
Lx = trigsimp(L[0]); Ly = trigsimp(L[1])
print("Kx=",Kx); print("Ky=",Ky); print("Lx=",Lx); print("Ly=",Ly)
