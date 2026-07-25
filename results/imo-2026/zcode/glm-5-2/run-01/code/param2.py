import sympy as sp
from sympy import symbols, cos, sin, tan, Matrix, simplify, Rational, sqrt, solve, expand, trigsimp

# Coordinates: A=(0,0), B=(1,0), C=(p,q), q>0.
# Let alpha, beta, gamma > 0 be the three equal angles.
# 
# Ray BK: starts at B=(1,0), direction angle (pi - alpha) => direction (cos(pi-alpha), sin(pi-alpha))=(-cos a, sin a)
# Ray BL: direction angle pi-(alpha+beta) => (-cos(a+b), sin(a+b))
# Ray CL: from C, direction = CA_angle + alpha. CA_angle = atan2(-q,-p). 
#   direction vector = R(alpha)*(CA_unit) where CA_unit = (-p,-q)/|CA|.
#   Let R = |CA| = sqrt(p^2+q^2). CA_unit = (-p/R, -q/R).
#   R(alpha) applied: (cos a * (-p/R) - sin a*(-q/R), sin a*(-p/R)+cos a*(-q/R))
#                   = ((-p cos a + q sin a)/R, (-p sin a - q cos a)/R)
# Ray CK: direction = R(alpha+gamma)*(CA_unit) = ((-p cos(a+g)+q sin(a+g))/R, (-p sin(a+g)-q cos(a+g))/R)
#
# K = BK ray ∩ CK ray.  L = BL ray ∩ CL ray.
# Parametrize points on rays by distance t from B and s from C:
#   K = B + t1 * dir_BK = C + s1 * dir_CK
#   L = B + t2 * dir_BL = C + s2 * dir_CL
#
# This gives K and L as functions of (alpha,beta,gamma) — but actually we need K via BK and CK 
# both, so K is intersection => determined by alpha, gamma (and triangle). 
# L determined by alpha, beta. 
# So K depends on (alpha,gamma), L depends on (alpha,beta). Then beta and gamma also appear in 
# the conditions at N and M. Let me just compute K, L symbolically and then the two conditions.

p,q = symbols('p q', positive=True)
a,b,g = symbols('a b g', positive=True)  # alpha, beta, gamma
R = sqrt(p**2+q**2)

def rot(vec, th):
    x,y=vec
    return (cos(th)*x - sin(th)*y, sin(th)*x + cos(th)*y)

CAu = (-p/R, -q/R)
dir_BK = (-cos(a), sin(a))
dir_BL = (-cos(a+b), sin(a+b))
dir_CL = rot(CAu, a)
dir_CK = rot(CAu, a+g)

# K = B + t*dir_BK = C + u*dir_CK. Solve for t,u (2D cross formula).
# B + t*dir_BK = C + u*dir_CK  =>  t*dir_BK - u*dir_CK = C - B = (p-1, q)
# Using cross products: t = cross(C-B, dir_CK)/cross(dir_BK, dir_CK)  [since -u term]
# Actually: t*d1 - u*d2 = w => t = cross(w, d2)/cross(d1,d2) ... let me derive:
# t d1 = w + u d2. cross both sides with d2: t cross(d1,d2) = cross(w,d2) + u*0 => t = cross(w,d2)/cross(d1,d2). Yes
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
wK = (p-1, q)
t = cross(wK, dir_CK)/cross(dir_BK, dir_CK)
K = (1 + t*dir_BK[0], 0 + t*dir_BK[1])
K = (simplify(K[0]), simplify(K[1]))

wL = (p-1, q)
tL = cross(wL, dir_CL)/cross(dir_BL, dir_CL)
L = (1 + tL*dir_BL[0], 0 + tL*dir_BL[1])
L = (simplify(L[0]), simplify(L[1]))

print("K computed. Kx sample trigsimp...")
Kx = trigsimp(K[0]); Ky=trigsimp(K[1])
print("Kx=",Kx)
print("Ky=",Ky)
