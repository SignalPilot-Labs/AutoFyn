from sympy import *

u, v = symbols('u v', positive=True)
a, b, g = symbols('a b g', positive=True)

# FIXED dNL: rot_cw(NC, b) where NC=(1-u, -v): (x - t*y? ) rot_cw(x,y,t)=(x+t y, -t x + y)
# NC=(1-u, -v): ( (1-u) + b*(-v), -b*(1-u) + (-v) ) = (1-u-bv, -b(1-u)-v)
dNLx = 1 - u - b*v; dNLy = -b*(1-u) - v

# K (unchanged, verified)
Kx = g*(a*v + u)/(a + g); Ky = g*(v - a*u)/(a + g)

# CL (verified rot_ccw)
dCLx = (u - 1) - v*a; dCLy = a*(u-1) + v

# L = C + p*dCL = N + q*dNL, C=(2,0), N=(1+u,v)
p, q = symbols('p q')
Lsol = solve([2 + p*dCLx - (1+u) - q*dNLx,
              0 + p*dCLy - v - q*dNLy], [p, q])
pp = Lsol[p]
Lx = simplify(2 + pp*dCLx); Ly = simplify(pp*dCLy)
print("L=",Lx,Ly)

# cond1: LBK=beta. BL at angle alpha+beta from BA. 
# Use the validated approach: cross/dot relation. Let me verify sign with numerics.
import numpy as np
# numeric config
uv_,vv_=0.3,2.0; a_,b_,g_=2.37841,0.23342,0.04798
subs=[(u,uv_),(v,vv_),(a,a_),(b,b_),(g,g_)]
print("\nNumeric Lx,Ly predicted:", float(Lx.subs(subs)), float(Ly.subs(subs)))
print("Numeric Lx,Ly actual: 1.51231402 0.02994964")
