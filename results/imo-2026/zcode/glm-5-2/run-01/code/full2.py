import sympy as sp, math, pickle
from sympy import symbols, expand, factor, simplify, Poly, groebner, Rational
import numpy as np
from scipy.optimize import fsolve
p,q = symbols('p q')
A,P,G = symbols('A P G')
def rotCW(v,t):
    x,y=v; return (expand((1-t**2)*x + 2*t*y), expand(-2*t*x + (1-t**2)*y))
def rotCCW(v,t):
    x,y=v; return (expand((1-t**2)*x - 2*t*y), expand(2*t*x + (1-t**2)*y))
BA=(-sp.Integer(1),sp.Integer(0)); CA=(-p,-q)
dir_BK=rotCW(BA,A); dir_BL=rotCW(BA,P)
dir_CL=rotCCW(CA,A); dir_CK=rotCCW(CA,G)
def cross(u,v): return expand(u[0]*v[1]-u[1]*v[0])
def dot(u,v): return expand(u[0]*v[0]+u[1]*v[1])
W=(p-1,q)
def get_point(d1,d2,W):
    tn=cross(W,d2); td=cross(d1,d2)
    return expand(td+tn*d1[0]), expand(tn*d1[1]), td
Kx,Ky,Kden = get_point(dir_BK,dir_CK,W)
Lx,Ly,Lden = get_point(dir_BL,dir_CL,W)
# verify numeric
Av=math.tan(math.radians(10.140977272332982)/2);beta=math.radians(21.08047146055647);gamma=math.radians(35.582220333404194)
Pv=math.tan((math.radians(10.140977272332982)+beta)/2); Gv=math.tan((math.radians(10.140977272332982)+gamma)/2)
pv,qv=0.25,0.75; subs={A:Av,P:Pv,G:Gv,p:pv,q:qv}
K=(float(Kx.subs(subs))/float(Kden.subs(subs)), float(Ky.subs(subs))/float(Kden.subs(subs)))
L=(float(Lx.subs(subs))/float(Lden.subs(subs)), float(Ly.subs(subs))/float(Lden.subs(subs)))
print("K=",K,"expect (0.6,0.071546)")
print("L=",L,"expect (0.210434,0.478582)")
