# Final clean verification of the whole proof chain in one place
from sympy import *
u, v, a, b, g = symbols('u v a b g', positive=True)

# Setup: B=(0,0), C=(2,0), A=(2u,2v), u>0,v>0. M=(u,v), N=(u+1,v).
# MN horizontal length 1. Perp bisector of MN: x = u + 1/2.
# Angles: alpha=KBA=ACL, beta=LBK=LNC, gamma=LCK=BMK. a=tan(alpha), b=tan(beta), g=tan(gamma).

# K = intersection of (ray from B: alpha from BA toward BC) and (ray from M: gamma from MB toward MC)
Kx = g*(a*v + u)/(a + g); Ky = g*(v - a*u)/(a + g)
# L = intersection of (ray from C: alpha from CA toward CB) and (ray from N: beta from NC toward NB)
Lx = (-a*b*v + 2*a + b*u + b)/(a + b); Ly = b*(a*(u-1) + v)/(a + b)

# The conditions ACL=alpha, KBA=alpha, LNC=beta hold by construction.
# Remaining: LBK=beta and LCK=gamma. These yield two polynomial equations:
cond1 = (a**2*b**2*u**2 - a**2*b**2*u + a**2*b**2*v**2 - a**2*b*v - 2*a**2*u
         - 2*a*b*u**2 - 2*a*b*u - 2*a*b*v**2 + 2*a*v - b**2*u**2 - b**2*u - b**2*v**2 + b*v)
cond2 = (a**2*g**2*u**2 - a**2*g**2*u + a**2*g**2*v**2 - a**2*g*v + 2*a**2*u - 2*a**2
         - 2*a*g*u**2 + 6*a*g*u - 2*a*g*v**2 - 4*a*g + 2*a*v - g**2*u**2 + 3*g**2*u - g**2*v**2 - 2*g**2 + g*v)

# Circumcenter target: x_O = u + 1/2.
# Claim: (cond1=0 and cond2=0) => the circumcenter of AKL has x-coordinate u+1/2.
# Proof: Let O=(u+1/2, y). From OA=OK solve y, then OA=OL is the residual to verify.
Ox = u + Rational(1,2)
Oy = symbols('Oy')
eqK = expand((Ox-Kx)**2 + (Oy-Ky)**2 - ((Ox-2*u)**2 + (Oy-2*v)**2))
y = solve(eqK, Oy)[0]
eqL = expand((Ox-Lx)**2 + (y-Ly)**2 - ((Ox-2*u)**2 + (y-2*v)**2))
R = cancel(eqL)
num = Poly(expand(fraction(R)[0]), u, v, a, b, g)
Q, rem = div(num, Poly(cond1, u,v,a,b,g), Poly(cond2, u,v,a,b,g))
print("=== FINAL VERIFICATION ===")
print("Remainder of circumcenter-residual upon division by (cond1, cond2):", "ZERO" if rem.is_zero else "NONZERO")
print()
print("Therefore: cond1=0 ∧ cond2=0  ⟹  x_O = u+1/2  ⟹  O on ⟂ bisector of MN  ⟹  OM = ON.  ∎")
