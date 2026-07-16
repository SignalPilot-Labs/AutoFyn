import sympy as sp, mpmath as mp
mp.mp.dps=30
al, be, ga, B, C = sp.symbols('alpha beta gamma B C', positive=True)
A = sp.pi - B - C
a = sp.sin(A); b = sp.sin(B); c = sp.sin(C)
tK = (c/2)*sp.sin(ga)/sp.sin(al+ga)
tL = (b/2)*sp.sin(be)/sp.sin(al+be)
Ax, Ay = c*sp.cos(B), c*sp.sin(B)
Kx, Ky = tK*sp.cos(B-al), tK*sp.sin(B-al)
Lx, Ly = a - tL*sp.cos(C-al), tL*sp.sin(C-al)
Px, Py = Kx-Ax, Ky-Ay
Qx, Qy = Lx-Ax, Ly-Ay
P2 = Px**2+Py**2; Q2 = Qx**2+Qy**2
s = a/2 - c*sp.cos(B)
E = P2*Qy - Q2*Py - s*(Px*Qy - Py*Qx)
RI  = sp.sin(C)*sp.sin(ga)*sp.sin(A+2*al+ga) - 2*sp.sin(A)*sp.sin(C-al-ga)*sp.sin(al+ga)
RII = sp.sin(B)*sp.sin(be)*sp.sin(A+2*al+be) - 2*sp.sin(A)*sp.sin(B-al-be)*sp.sin(al+be)

def numf(expr, vals):
    return float(sp.re(sp.N(expr.subs(vals), 30)))

Bv,Cv,alv=1.1,0.9,0.28
Avn=float(sp.pi)-Bv-Cv
def RIn(g): return mp.sin(Cv)*mp.sin(g)*mp.sin(Avn+2*alv+g)-2*mp.sin(Avn)*mp.sin(Cv-alv-g)*mp.sin(alv+g)
def RIIn(bb): return mp.sin(Bv)*mp.sin(bb)*mp.sin(Avn+2*alv+bb)-2*mp.sin(Avn)*mp.sin(Bv-alv-bb)*mp.sin(alv+bb)
gav=float(mp.findroot(RIn,0.3)); bev=float(mp.findroot(RIIn,0.3))

# Set beta on-constraint (RII=0), vary gamma off; check E/RI constant in gamma -> lambda_I
for gtest in [0.3,0.45,0.6]:
    v={al:alv,be:bev,ga:gtest,B:Bv,C:Cv}
    print("gamma=",gtest,"E/RI =", numf(E,v)/numf(RI,v))
print("---- set gamma on-constraint, vary beta, E/RII:")
for btest in [0.3,0.5,0.7]:
    v={al:alv,be:btest,ga:gav,B:Bv,C:Cv}
    print("beta=",btest,"E/RII =", numf(E,v)/numf(RII,v))
