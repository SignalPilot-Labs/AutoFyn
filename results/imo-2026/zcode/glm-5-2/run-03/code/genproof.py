from sympy import *

u, v = symbols('u v', positive=True)
a, b, g = symbols('a b g', positive=True)

Kx = g*(a*v + u)/(a + g); Ky = g*(v - a*u)/(a + g)
Lx = (-a*b*v + 2*a + b*u + b)/(a + b); Ly = b*(a*(u-1) + v)/(a + b)

# cond1 numerator (from cross_BA_BL*(1-ab) + dot_BA_BL*(a+b), dropping -2/(a+b)):
cond1_num = a**2*b**2*u**2 - a**2*b**2*u + a**2*b**2*v**2 - a**2*b*v - 2*a**2*u - 2*a*b*u**2 - 2*a*b*u - 2*a*b*v**2 + 2*a*v - b**2*u**2 - b**2*u - b**2*v**2 + b*v

# cond2 numerator (cross_CL_CK - g*dot_CL_CK, then drop 1/(a+g)):
dCLx = (u - 1) - v*a; dCLy = a*(u-1) + v
CKx = Kx - 2; CKy = Ky
cross_CL_CK = dCLx*CKy - dCLy*CKx
dot_CL_CK = dCLx*CKx + dCLy*CKy
cond2_raw = simplify((cross_CL_CK - g*dot_CL_CK)*(a+g))
cond2_num = expand(cond2_raw)
print("cond2_num:", cond2_num)

# Circumcenter: target Ox = u + 1/2
Ox = u + Rational(1,2)
Ax, Ay = 2*u, 2*v
Oy = symbols('Oy')
eqK = expand((Ox-Kx)**2 + (Oy-Ky)**2 - ((Ox-Ax)**2 + (Oy-Ay)**2))
Oyv = solve(eqK, Oy)[0]
eqL = (Ox-Lx)**2 + (Oyv-Ly)**2 - ((Ox-Ax)**2 + (Oyv-Ay)**2)
residual = cancel(eqL)
nr = expand(fraction(residual)[0])
print("\nresidual numerator total degree:", Poly(nr,u,v,a,b,g).total_degree())

# Reduce nr by (cond1_num, cond2_num) via polynomial division
P = Poly(nr, u,v,a,b,g)
P1 = Poly(cond1_num, u,v,a,b,g)
P2 = Poly(cond2_num, u,v,a,b,g)
Q, R = div(P, P1, P2)
print("remainder is zero?", R.is_zero)
print("remainder expr:", R.as_expr())
