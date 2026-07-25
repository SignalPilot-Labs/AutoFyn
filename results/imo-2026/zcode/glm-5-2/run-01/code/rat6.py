import sympy as sp, math
from sympy import symbols, expand, factor, simplify, N as Ne
p,q = symbols('p q')
A,P,G = symbols('A P G')
# Proper rotation keeping direction = (-cos(angle), sin(angle)) etc via cos/sin of the SAME angle.
# But we parametrize by half-angle t. The direction of a ray obtained by rotating vector v0 by angle 
# 2*arctan(t) (CCW): use cos=(1-t^2)/(1+t^2), sin=2t/(1+t^2). 
# For a LINE direction we can scale by (1+t^2): direction = ((1-t^2)*x - 2t*y, 2t*x + (1-t^2)*y).
# This IS a true rotation scaled by positive (1+t^2). Same for all. Let me verify with numeric.
def rot(v,t):
    x,y=v
    return (expand((1-t**2)*x - 2*t*y), expand(2*t*x + (1-t**2)*y))
BA=(-sp.Integer(1),sp.Integer(0)); CA=(-p,-q)
# numeric test
Av=math.tan(math.radians(10.140977272332982)/2)
dirBK_num = rot(BA,Av)
print("dirBK numeric:", float(dirBK_num[0]), float(dirBK_num[1]))
# normalize
import numpy as np
d=np.array([float(dirBK_num[0]),float(dirBK_num[1])]); d=d/np.linalg.norm(d)
print("normalized:", d, " expect ~ direction BK = (cos(180-a), sin(180-a))... ")
print("expected:", np.array([-math.cos(math.radians(10.140977272332982)), math.sin(math.radians(10.140977272332982))]))
