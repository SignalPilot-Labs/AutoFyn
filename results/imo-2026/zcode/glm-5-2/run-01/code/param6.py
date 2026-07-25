import sympy as sp
from sympy import symbols, cos, sin, tan, simplify, trigsimp, expand, Rational, sqrt, I, together, numer, denom, cancel, fu

R = symbols('R', positive=True)
th = symbols('theta', positive=True)
a = symbols('a', positive=True)
tb, tg = symbols('tb tg')  # tan(b), tan(g)

# Use tb=tan(b), tg=tan(g). Express cos(a+b),sin(a+b) via tan addition:
# cos(a+b) = (cos a - sin a tb)/sqrt(1+tb^2)... introduces sqrt. 
# Better keep b,g symbolic but solve linear eqs.
b,g = symbols('b g', positive=True)

SK = (R*sin(a+g) - sin(a+g+th))/sin(2*a+g+th)
SL = (R*sin(a) - sin(a+th))/sin(2*a+b+th)
Kx = 1 - SK*cos(a); Ky = SK*sin(a)
Lx = 1 - SL*cos(a+b); Ly = SL*sin(a+b)
Nx = R*cos(th)/2; Ny = R*sin(th)/2
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dot(u,v): return u[0]*v[0]+u[1]*v[1]

NL = (Lx-Nx, Ly-Ny); NC=(R*cos(th)/2, R*sin(th)/2)
# angle LNC = b : cross(NL,NC)/dot(NL,NC) = tan(b)
condA = cross(NL,NC) - dot(NL,NC)*tan(b)
condA = expand(condA)
# solve for b? condA is in b via cos(a+b),sin(a+b),tan(b),sin(2a+b+th). 
# It's not simply linear. Let me just solve condA=0 for b and condB=0 for g symbolically? hard.
# Instead: substitute specific NUMERIC triangle and param, verify with exact rational trig? 
# 
# Better plan: Use tan half-angle substitution t=tan(a/2) won't help since b,g independent.
#
# Realization: condA = 0 determines b given a. Let me solve condA=0 for SL or rearrange.
# Actually note SL = (R sin a - sin(a+th))/sin(2a+b+th). The dependence on b is through sin(2a+b+th)
# AND through Lx,Ly via cos(a+b),sin(a+b). Messy.
# 
# Let me try a SMARTER substitution: param by the RAYS directly. 
# Let me instead verify numerically that condA is satisfiable and OM=ON, then for RIGOR, 
# use a Groebner computation in the tan variables.
print("condA depends on b nonlinearly. Switching strategy.")
