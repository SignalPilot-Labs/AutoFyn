import sympy as sp

tau, sA, cA, sC, cC = sp.symbols('tau sA cA sC cC', real=True)
sB_expr = sA*cC + cA*sC
cB_expr = sA*sC - cA*cC

P1 = sA*tau*(tau*cC - sC)
Q1 = sA*sC*(tau**2+1) + 2*tau*sB_expr
R1 = -2*tau**2*sC*cA - tau*sA*sC + sA*cC

P2 = sA*tau*(tau*cB_expr - sB_expr)
Q2 = sA*sB_expr*(tau**2+1) + 2*tau*sC
R2 = -2*tau**2*sB_expr*cA - tau*sA*sB_expr + sA*cB_expr

U, V = sp.symbols('U V')
F = sA*U*V - cA*(U+V) - sA
L = sp.expand(F - 4)

m_of_V = sp.diff(L, U)
n_of_V = sp.expand(L - m_of_V*U)

print("m(V) =", m_of_V)
print("n(V) =", n_of_V)

Xi = sp.expand(P1*n_of_V**2 - Q1*n_of_V*m_of_V + R1*m_of_V**2)
Xi_poly = sp.Poly(Xi, V)
print("Xi degree in V:", Xi_poly.degree())
c2 = Xi_poly.coeff_monomial(V**2)
c1 = Xi_poly.coeff_monomial(V)
c0 = Xi_poly.coeff_monomial(1)
c2 = sp.factor(c2)
print("c2 =", c2)

c1f = sp.factor(c1)
c0f = sp.factor(c0)
print("c1 =", c1f)
print("c0 =", c0f)
