import sympy as sp
al, be, ga, B, C = sp.symbols('alpha beta gamma B C', positive=True)
A = sp.pi - B - C
a = sp.sin(A); b = sp.sin(B); c = sp.sin(C)
# FORMS (b),(d): cevian-intersection forms
tK = a*sp.sin(C-al-ga)/sp.sin(A+2*al+ga)
tL = a*sp.sin(B-al-be)/sp.sin(A+2*al+be)
Ax, Ay = c*sp.cos(B), c*sp.sin(B)
Kx, Ky = tK*sp.cos(B-al), tK*sp.sin(B-al)
Lx, Ly = a - tL*sp.cos(C-al), tL*sp.sin(C-al)
Px, Py = Kx-Ax, Ky-Ay
Qx, Qy = Lx-Ax, Ly-Ay
P2 = Px**2+Py**2; Q2 = Qx**2+Qy**2
s = a/2 - c*sp.cos(B)
E = P2*Qy - Q2*Py - s*(Px*Qy - Py*Qx)
# numeric test off-constraint
import random
for _ in range(5):
    v={al:random.uniform(0.1,0.4),be:random.uniform(0.1,0.5),ga:random.uniform(0.1,0.5),
       B:random.uniform(0.8,1.3),C:random.uniform(0.7,1.2)}
    print("E(forms b,d) =", float(sp.re(sp.N(E.subs(v),25))))
