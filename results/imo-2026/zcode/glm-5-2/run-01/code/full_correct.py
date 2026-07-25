import sympy as sp, math, pickle
from sympy import symbols, expand, factor, simplify, Poly, groebner, Rational
import numpy as np
p,q = symbols('p q')
A,P,G = symbols('A P G')
def rot(v,t):  # CCW rotation by 2 arctan t, scaled by (1+t^2)
    x,y=v
    return (expand((1-t**2)*x + 2*t*y), expand(-2*t*x + (1-t**2)*y))
# wait let me just verify sign. CCW rot by angle phi of (x,y): (x cos - y sin, x sin + y cos).
# With cos=(1-t^2)/(1+t^2), sin=2t/(1+t^2): ( (1-t^2)x - 2t y, 2t x + (1-t^2)y )/(1+t^2).
# Apply to (-1,0): (-(1-t^2), -2t)/(1+t^2) = (-cos, -sin). That's CW (negative y). 
# So rotating (-1,0) by +phi gives (-cos phi, -sin phi)?? No: CCW rot of (-1,0) by phi: 
# (-1,0) has angle pi. +phi CCW -> angle pi+phi -> (cos(pi+phi),sin(pi+phi))=(-cos phi,-sin phi). 
# YES that's correct! CCW from (-1,0) by phi points DOWN (into 3rd quadrant). 
# But BK should point UP (K above x-axis). So the rotation at B is CW (by -alpha), not CCW!
# Earlier numeric: BK direction = (cos(180-alpha), sin(180-alpha)) = (-cos a, +sin a). 
# That's CW rotation of (-1,0) by alpha. So use -alpha rotation at B.
# At C: CL = CA + alpha (CCW from earlier: CA angle=-108, CL=-98, so +alpha, CCW). 
# So B rotations are CW, C rotations are CCW. Asymmetric!
def rot_cw(v,t):  # CW by 2 arctan t
    x,y=v; return (expand((1-t**2)*x + 2*t*y), expand(2*t*x - (1-t**2)*y))
# wait CW rot by phi: (x cos + y sin, -x sin + y cos). Apply (-1,0): (-(1-t^2), 2t)/(1+t^2)=(-cos,+sin). 
def rotCCW(v,t):
    x,y=v; return (expand((1-t**2)*x - 2*t*y), expand(2*t*x + (1-t**2)*y))
def rotCW(v,t):
    x,y=v; return (expand((1-t**2)*x + 2*t*y), expand(-2*t*x + (1-t**2)*y))
BA=(-sp.Integer(1),sp.Integer(0)); CA=(-p,-q)
# verify
Av=math.tan(math.radians(10.140977272332982)/2)
d=rotCW(BA,Av)
dn=np.array([float(d[0]),float(d[1])]);dn=dn/np.linalg.norm(dn)
print("BK via rotCW:",dn,"expect",[-math.cos(math.radians(10.14)),math.sin(math.radians(10.14))])
dir_BK=rotCW(BA,A); dir_BL=rotCW(BA,P)
dir_CL=rotCCW(CA,A); dir_CK=rotCCW(CA,G)
# verify CL
pv,qv=0.25,0.75
d=dir_CL.subs({A:Av,p:pv,q:qv})
dn=np.array([float(d[0]),float(d[1])]);dn=dn/np.linalg.norm(dn)
ca=np.array([-pv,-qv]);ca=ca/np.linalg.norm(ca)
# expected: rotate CA by +alpha CCW
import numpy as np
phi=math.radians(10.140977272332982)
exp=np.array([ca[0]*math.cos(phi)-ca[1]*math.sin(phi), ca[0]*math.sin(phi)+ca[1]*math.cos(phi)])
print("CL via rotCCW:",dn,"expect",exp)
