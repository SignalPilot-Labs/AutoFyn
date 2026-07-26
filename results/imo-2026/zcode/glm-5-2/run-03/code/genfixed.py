from sympy import *

u, v = symbols('u v', positive=True)
a, b, g = symbols('a b g', positive=True)

A = Matrix([2*u, 2*v]); B = Matrix([0,0]); C = Matrix([2,0])
M = (A+B)/2; N = (A+C)/2

# K (verified)
Kx = g*(a*v + u)/(a + g); Ky = g*(v - a*u)/(a + g)
# L (now verified)
Lx = (-a*b*v + 2*a + b*u + b)/(a + b); Ly = b*(a*(u-1) + v)/(a + b)

# Direction vectors
dCLx = (u - 1) - v*a; dCLy = a*(u-1) + v   # rot_ccw(CA, a)
dNLx = 1 - u - b*v;   dNLy = -b*(1-u) - v   # rot_cw(NC, b)

# cond1: LBK = beta. K inside angle LBA => rays BA, BK, BL in order. BL at angle alpha+beta from BA.
#   BA=(2u,2v). BK direction (u+va, v-ua) [rot_cw of BA by a]. 
#   BL direction = rot_cw(BA, alpha+beta). rot_cw(2u,2v, t): (2u+2vt, -2ut+2v) ~ (u+vt, v-ut) with t=tan(a+b)=(a+b)/(1-ab).
#   But easier: angle between BA and BL. cross(BA,BL)/dot(BA,BL) should equal... 
#   Let me compute via: BL=(Lx,Ly) from origin B. 
cross_BA_BL = 2*u*Ly - 2*v*Lx
dot_BA_BL = 2*u*Lx + 2*v*Ly
# For uv,vv config: BA=(0.6,4) up-right slightly. BK rot_cw so clockwise. BL further cw. 
# The signed CW angle from BA has tan = cross2(BA,BL)/dot? cross2(BA,BL)=BAx*BLy-BAy*BLx. For CW rotation cross becomes... 
# Test numerically the relation:
import numpy as np
uv_,vv_=0.3,2.0; a_,b_,g_=2.37841,0.23342,0.04798
subs=[(u,uv_),(v,vv_),(a,a_),(b,b_),(g,g_)]
cr=float(cross_BA_BL.subs(subs)); dt=float(dot_BA_BL.subs(subs))
print(f"cross/dot = {cr/dt:.5f}, tan(alpha+beta)={(a_+b_)/(1-a_*b_):.5f}, tan(alpha+beta) actual neg? {-cr/dt:.5f}")
# so cross/dot = -tan(alpha+beta). => cross*(1-ab) + dot*(a+b) = 0  [since cross/dot = -(a+b)/(1-ab)]
cond1_expr = cross_BA_BL*(1 - a*b) + dot_BA_BL*(a + b)
cond1_num = factor(cond1_expr)
print("cond1 factored:", cond1_num)

# cond2: LCK=gamma. CL dir = dCL, CK = K-C = (Kx-2, Ky).
CKx = Kx - 2; CKy = Ky
cross_CL_CK = dCLx*CKy - dCLy*CKx
dot_CL_CK = dCLx*CKx + dCLy*CKy
# check sign numerically
cr2=float(cross_CL_CK.subs(subs)); dt2=float(dot_CL_CK.subs(subs))
print(f"\nLCK: cross/dot={cr2/dt2:.5f}, g={g_:.5f}, -g={-g_:.5f}")
# so cross/dot = g => cross - g*dot = 0  OR = -g. Determine:
cond2_expr_a = cross_CL_CK - g*dot_CL_CK
cond2_expr_b = cross_CL_CK + g*dot_CL_CK
print("cross - g*dot =", float(cond2_expr_a.subs(subs)), " cross + g*dot =", float(cond2_expr_b.subs(subs)))
