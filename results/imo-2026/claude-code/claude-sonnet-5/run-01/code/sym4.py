import sympy as sp

x, theta, b, c, alpha0 = sp.symbols('x theta b c alpha0', real=True)
C2x, S2x = sp.symbols('C2x S2x')  # stand-ins for cos(2x), sin(2x)

# fu-simplified expression:
# b/2*cos(2theta+2x) - b/2 + c*cos(alpha0) - c*cos(theta+x)*cos(alpha0+theta-x)
# expand cos(2theta+2x) = cos2x cos2theta - sin2x sin2theta
term1 = sp.Rational(1,2)*b*(C2x*sp.cos(2*theta) - S2x*sp.sin(2*theta))
# expand cos(theta+x)*cos(alpha0+theta-x) via product to sum:
# = 1/2[cos((theta+x)-(alpha0+theta-x)) + cos((theta+x)+(alpha0+theta-x))]
# = 1/2[cos(2x-alpha0) + cos(alpha0+2theta)]
# cos(2x-alpha0) = cos2x cos(alpha0) + sin2x sin(alpha0)
term2 = -c*( sp.Rational(1,2)*(C2x*sp.cos(alpha0) + S2x*sp.sin(alpha0)) + sp.Rational(1,2)*sp.cos(alpha0+2*theta) )

expr = term1 - sp.Rational(1,2)*b + c*sp.cos(alpha0) + term2

expr = sp.expand(expr)
coeff_C = sp.simplify(expr.coeff(C2x))
coeff_S = sp.simplify(expr.coeff(S2x))
rest = sp.simplify(expr - coeff_C*C2x - coeff_S*S2x)
print("coeff of cos(2x):", coeff_C)
print("coeff of sin(2x):", coeff_S)
print("constant (rest):", rest)
print()
print("equation: coeff_C*cos(2x) + coeff_S*sin(2x) + rest = 0")
