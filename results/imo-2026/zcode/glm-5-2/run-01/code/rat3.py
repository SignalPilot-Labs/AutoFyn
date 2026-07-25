import sympy as sp
from sympy import symbols, expand, factor, simplify, cancel, Rational, together, collect

p,q = symbols('p q')
A,P,G = symbols('A P G')
def rot_half(v, t):
    x,y = v
    c = (1-t**2); s = 2*t   # drop common /(1+t^2) since line direction up to scale
    return (expand(c*x - s*y), expand(s*x + c*y))
# WAIT: dropping the /(1+t^2) changes the rotation unless we keep it consistent for ALL rays 
# since each ray's direction scaled independently is fine for LINE but for ANGLES between rays 
# at SAME vertex we need consistent scaling? No - angle between two lines is independent of 
# scaling each direction. And intersection only uses directions up to scale. 
# BUT the angle CONDITIONS (ang LNC=beta) compare angles at different vertices involving points,
# which is fine since points are computed correctly. The only place scaling matters is none, 
# because: (1) intersection: direction up to scale fine. (2) angle at a point between two segments: 
# uses actual point coordinates. So dropping /(1+t^2) is OK!
# However, for the rotation at C (rotating CA=(-p,-q)), we MUST apply a TRUE rotation (same scale), 
# but since it's a single direction used as a line, scaling is irrelevant. Good.

BA = (sp.Integer(-1), sp.Integer(0))
CA = (-p,-q)
dir_BK = rot_half(BA, A)
dir_BL = rot_half(BA, P)
dir_CL = rot_half(CA, A)
dir_CK = rot_half(CA, G)
def cross(u,v): return expand(u[0]*v[1]-u[1]*v[0])
W = (p-1, q)
# K: t*dir_BK - u*dir_CK = W. t = cross(W,dir_CK)/cross(dir_BK,dir_CK)
def get_point(d1,d2,W):
    tn = cross(W,d2); td = cross(d1,d2)
    # point = B + (tn/td)*d1 = (1,0) + tn*d1/td
    return expand(td + tn*d1[0]), expand(tn*d1[1]), td  # common denom td
Kx,Ky,Kden = get_point(dir_BK,dir_CK,W)
Lx,Ly,Lden = get_point(dir_BL,dir_CL,W)
print("Kden:", factor(Kden))
print("Lden:", factor(Lden))
print("Kx:", factor(Kx))
print("Ky:", factor(Ky))
print("Lx:", factor(Lx))
print("Ly:", factor(Ly))
