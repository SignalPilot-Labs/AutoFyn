import sympy as sp

al, be, ga, B, C = sp.symbols('alpha beta gamma B C', positive=True)
A = sp.pi - B - C
# side lengths with circumdiameter k=1: a=sinA,b=sinB,c=sinC
a = sp.sin(A); b = sp.sin(B); c = sp.sin(C)

# t_K = BK from triangle BMK (defn of gamma), t_L = CL from triangle CNL (defn of beta)
tK = (c/2)*sp.sin(ga)/sp.sin(al+ga)
tL = (b/2)*sp.sin(be)/sp.sin(al+be)

# coordinates, B=(0,0), C=(a,0), A=(c cosB, c sinB)
Ax, Ay = c*sp.cos(B), c*sp.sin(B)
Kx, Ky = tK*sp.cos(B-al), tK*sp.sin(B-al)
Lx, Ly = a - tL*sp.cos(C-al), tL*sp.sin(C-al)

# vectors from A
Px, Py = Kx-Ax, Ky-Ay
Qx, Qy = Lx-Ax, Ly-Ay
P2 = sp.expand_trig(Px**2+Py**2)
Q2 = sp.expand_trig(Qx**2+Qy**2)

s = a/2 - c*sp.cos(B)   # = (b^2-c^2)/(2a)
# target identity (star): P2*Qy - Q2*Py - s*(Px*Qy-Py*Qx) = 0  ?
E = P2*Qy - Q2*Py - s*(Px*Qy - Py*Qx)

# constraints
RI  = sp.sin(C)*sp.sin(ga)*sp.sin(A+2*al+ga) - 2*sp.sin(A)*sp.sin(C-al-ga)*sp.sin(al+ga)
RII = sp.sin(B)*sp.sin(be)*sp.sin(A+2*al+be) - 2*sp.sin(A)*sp.sin(B-al-be)*sp.sin(al+be)

# numeric check: pick angles, solve constraints for ga,be, test E=0
import mpmath as mp
mp.mp.dps=30
def num(expr, vals):
    return complex(sp.N(expr.subs(vals), 25))

# choose B,C,alpha
import random
Bv, Cv, alv = 1.1, 0.9, 0.28
Av = sp.pi - Bv - Cv
# solve RI for ga, RII for be numerically
from mpmath import findroot, sin, pi
Avn = float(pi) - Bv - Cv
def RIn(g):
    return mp.sin(Cv)*mp.sin(g)*mp.sin(Avn+2*alv+g) - 2*mp.sin(Avn)*mp.sin(Cv-alv-g)*mp.sin(alv+g)
def RIIn(bb):
    return mp.sin(Bv)*mp.sin(bb)*mp.sin(Avn+2*alv+bb) - 2*mp.sin(Avn)*mp.sin(Bv-alv-bb)*mp.sin(alv+bb)
gav = mp.findroot(RIn, 0.3)
bev = mp.findroot(RIIn, 0.3)
print("gamma,beta=", gav, bev)
vals = {al:alv, be:float(bev), ga:float(gav), B:Bv, C:Cv}
print("E on-constraint =", num(E, vals))
print("RI,RII =", num(RI,vals), num(RII,vals))
# off constraint
vals2 = {al:alv, be:0.35, ga:0.4, B:Bv, C:Cv}
print("E off-constraint =", num(E, vals2))
print("RI,RII off =", num(RI,vals2), num(RII,vals2))
