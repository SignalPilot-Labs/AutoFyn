import sympy as sp
from sympy import symbols, cos, sin, tan, simplify, trigsimp, expand_trig, Rational, sqrt, expand, factor, together

R = symbols('R', positive=True)
th = symbols('theta', positive=True)
a,b,g = symbols('a b g', positive=True)

# K = (1 - SK cos a, SK sin a), SK = (R sin(a+g) - sin(a+g+theta))/sin(2a+g+theta)
# L = (1 - SL cos(a+b), SL sin(a+b)), SL = (R sin a - sin(a+theta))/sin(2a+b+theta)
SK = (R*sin(a+g) - sin(a+g+th))/sin(2*a+g+th)
SL = (R*sin(a) - sin(a+th))/sin(2*a+b+th)
Kx = 1 - SK*cos(a); Ky = SK*sin(a)
Lx = 1 - SL*cos(a+b); Ly = SL*sin(a+b)

# M = midpoint AB = (1/2, 0). N = midpoint AC = (R cos th/2, R sin th/2).
Mx=Rational(1,2); My=0
Nx = R*cos(th)/2; Ny = R*sin(th)/2

def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dot(u,v): return u[0]*v[0]+u[1]*v[1]
def sub(u,v): return (u[0]-v[0],u[1]-v[1])

# Condition A: angle LNC = beta. 
# angle LNC at N: rays NL, NC. vectors L-N, C-N.
NL = (Lx-Nx, Ly-Ny); NC=(R*cos(th)-Nx, R*sin(th)-Ny)
# angle = beta means tan matches AND it's the proper angle.
# We'll use: cross(NL,NC) = dot(NL,NC)*tan(beta)  -- oriented (assume positive orientation)
condA = expand(cross(NL,NC) - dot(NL,NC)*tan(b))
condA = trigsimp(condA)
print("condA (angle LNC=beta) simplified:")
print(condA)
print()

# Condition B: angle BMK = gamma at M. rays MB, MK. vectors B-M, K-M.
MB = (1-Mx, 0-My); MK = (Kx-Mx, Ky-My)
condB = expand(cross(MB,MK) - dot(MB,MK)*tan(g))
condB = trigsimp(condB)
print("condB (angle BMK=gamma) simplified:")
print(condB)
