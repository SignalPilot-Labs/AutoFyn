import sympy as sp
al,u,w,B,C = sp.symbols('alpha u w B C', positive=True)
A = sp.pi-B-C
# Derive the u-relation: K = intersection of ray A (angle u from AB) and ray B (angle alpha).
# Use coordinates B=0, C=(a,0), A=(c cosB, c sinB), a=sinA,b=sinB,c=sinC
a=sp.sin(A);b=sp.sin(B);c=sp.sin(C)
# BK = c sin u/sin(al+u); K on ray from B at angle (B-al)
BK=c*sp.sin(u)/sp.sin(al+u)
Ax,Ay=c*sp.cos(B),c*sp.sin(B)
Kx,Ky=BK*sp.cos(B-al),BK*sp.sin(B-al)
M=(sp.Matrix([Ax,Ay]))/2
# gamma = angle BMK  (at M between MB and MK); MB direction = -M (B=0)
def ang(vx,px1,py1,px2,py2):
    pass
import sympy
# cot(angle BMK): vectors M->B = (0-Mx,0-My), M->K=(Kx-Mx,Ky-My)
MBx,MBy=-M[0],-M[1]; MKx,MKy=Kx-M[0],Ky-M[1]
cross=MBx*MKy-MBy*MKx; dot=MBx*MKx+MBy*MKy
cotg = dot/cross    # cot(angle) = dot/|cross| ; sign: take cot = dot/cross (2D)
# angle ACK: vectors C->A=(Ax-a,Ay), C->K=(Kx-a,Ky)
CAx,CAy=Ax-a,Ay; CKx,CKy=Kx-a,Ky
cross2=CAx*CKy-CAy*CKx; dot2=CAx*CKx+CAy*CKy
cot_ACK=dot2/cross2
# constraint: angle_ACK = alpha + gamma. As cot relation is messy; test numerically the relation
# cot u = cot al + 2 cot gamma  and check angle_ACK = al+gamma
import numpy as np
subs={al:0.28,B:1.1,C:0.9}
# find u by imposing angle_ACK - (al + angle_BMK)=0
from mpmath import findroot, mpf
import mpmath as mp
mp.mp.dps=25
def gval(uu):
    s=dict(subs); s[u]=uu
    g=float(sp.N(sp.acot(cotg).subs(s)))
    ack=float(sp.N(sp.acot(cot_ACK).subs(s)))
    return ack-(0.28+g)
uu=float(mp.findroot(gval,0.12))
print("u solved from constraint:",uu, " expected ~0.11915")
# so u-relation: acot(cot_ACK) - al - acot(cotg) = 0. Let's get cleaner: define the u-equation
# Print simplified cotg and cot_ACK
print("cotg=",sp.simplify(sp.expand_trig(cotg)))
print("cot_ACK=",sp.simplify(sp.expand_trig(cot_ACK)))
