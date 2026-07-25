import sympy as sp

tau, sA, cA, sC, cC = sp.symbols('tau sA cA sC cC', real=True)
sB_expr = sA*cC + cA*sC
cB_expr = sA*sC - cA*cC

P1 = sA*tau*(tau*cC - sC)
Q1 = sA*sC*(tau**2+1) + 2*tau*sB_expr
R1 = -2*tau**2*sC*cA - tau*sA*sC + sA*cC

U, V = sp.symbols('U V')
F = sA*U*V - cA*(U+V) - sA
L = sp.expand(F - 4)
m_of_V = sp.diff(L, U)
n_of_V = sp.expand(L - m_of_V*U)

Xi = sp.expand(P1*n_of_V**2 - Q1*n_of_V*m_of_V + R1*m_of_V**2)
Xi_poly = sp.Poly(Xi, V)
c2 = Xi_poly.coeff_monomial(V**2)
c1 = Xi_poly.coeff_monomial(V)
c0 = Xi_poly.coeff_monomial(1)

c2f = sp.factor(c2)
c1f = sp.factor(c1)
c0f = sp.factor(c0)
print("c2 =", c2f)
print()
print("c1 =", c1f)
print()
print("c0 =", c0f)
