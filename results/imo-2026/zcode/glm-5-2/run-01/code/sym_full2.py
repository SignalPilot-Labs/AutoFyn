import sympy as sp
from sympy import symbols, expand, groebner, Rational, sqrt

p,q = symbols('p q', real=True)
k1,k2,l1,l2 = symbols('k1 k2 l1 l2', real=True)
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dot(u,v): return u[0]*v[0]+u[1]*v[1]
A=(sp.Integer(0),sp.Integer(0)); B=(sp.Integer(1),sp.Integer(0)); C=(p,q)
M=(sp.Rational(1,2),sp.Integer(0)); N=(p/2,q/2)
K=(k1,k2); L=(l1,l2)
def sub(P,Q): return (P[0]-Q[0],P[1]-Q[1])

u1=sub(K,B); v1=sub(A,B); u2=sub(A,C); v2=sub(L,C)
eq1 = expand(cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2))
u1=sub(L,B); v1=sub(K,B); u2=sub(L,N); v2=sub(C,N)
eq2 = expand(cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2))
u1=sub(L,C); v1=sub(K,C); u2=sub(B,M); v2=sub(K,M)
eq3 = expand(cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2))

# OM^2 - ON^2. O = circumcenter of AKL with A=origin.
# Circumcenter of triangle with A=(0,0), K=(k1,k2), L=(l1,l2):
# O = ( (k1^2+k2^2)*l perpendicular stuff )... 
# O lies on perp bisector of AK and AL. 
# Solve: O·K = |K|^2/2, O·L = |L|^2/2.
# Let O=(ox,oy). ox*k1+oy*k2=(k1^2+k2^2)/2 ; ox*l1+oy*l2=(l1^2+l2^2)/2.
ox,oy = symbols('ox oy', real=True)
sol = sp.solve([ox*k1+oy*k2-(k1**2+k2**2)/2, ox*l1+oy*l2-(l1**2+l2**2)/2],[ox,oy])
ox = sol[ox]; oy = sol[oy]
ox=expand(ox); oy=expand(oy)
# OM^2 - ON^2
OM2 = (ox-sp.Rational(1,2))**2 + oy**2
ON2 = (ox-p/2)**2 + (oy-q/2)**2
diff = expand(OM2-ON2)
diff = sp.simplify(diff)
print("OM^2-ON^2 simplified:")
print(diff)
print()
# Substitute numerator over common denom; let's get numerator
num, den = sp.fraction(sp.together(OM2-ON2))
num = expand(num)
print("numerator of OM^2-ON^2:")
print(num)
print()
print("We want to show: num is in ideal <eq1,eq2,eq3> (over R[p,q,k,l]).")
