import sympy as sp

A, C, theta = sp.symbols('A C theta', real=True, positive=True)
tau = sp.tan(theta)
sA, cA, sC, cC = sp.sin(A), sp.cos(A), sp.sin(C), sp.cos(C)
B = sp.pi - A - C
sB, cB = sp.sin(B), sp.cos(B)

P1 = sA*tau*(tau*cC - sC)
Q1 = sA*sC*(tau**2+1) + 2*tau*sB
R1 = -2*tau**2*sC*cA - tau*sA*sC + sA*cC

P2 = sA*tau*(tau*cB - sB)
Q2 = sA*sB*(tau**2+1) + 2*tau*sC
R2 = -2*tau**2*sB*cA - tau*sA*sB + sA*cB

U, V = sp.symbols('U V')
F = sA*U*V - cA*(U+V) - sA
L = sp.expand(F - 4)
m_of_V = sp.diff(L, U)
n_of_V = sp.expand(L - m_of_V*U)

Xi = sp.expand(P1*n_of_V**2 - Q1*n_of_V*m_of_V + R1*m_of_V**2)
Xi_poly = sp.Poly(Xi, V)
c2 = sp.trigsimp(sp.simplify(Xi_poly.coeff_monomial(V**2)))
c1 = sp.trigsimp(sp.simplify(Xi_poly.coeff_monomial(V)))
c0 = sp.trigsimp(sp.simplify(Xi_poly.coeff_monomial(1)))
print("c2 =", c2)
print("c1 =", c1)
print("c0 =", c0)
