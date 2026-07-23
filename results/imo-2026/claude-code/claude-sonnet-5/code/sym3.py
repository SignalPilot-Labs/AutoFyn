import sympy as sp

x, theta, b, c, alpha0 = sp.symbols('x theta b c alpha0', real=True)

expr = -b*sp.sin(theta+x)**2 + c*sp.cos(alpha0) - (c*sp.Rational(1,2))*sp.cos(2*x-alpha0) - (c*sp.Rational(1,2))*sp.cos(alpha0+2*theta)

# expand everything in terms of cos(2x), sin(2x), cos(2theta), sin(2theta), etc.
expr_exp = sp.expand_trig(expr)
expr_exp = sp.expand(expr_exp)
print("expanded:")
sp.pprint(expr_exp)

# collect wrt cos(2x) and sin(2x)
expr_c = sp.collect(expr_exp, [sp.cos(2*x), sp.sin(2*x)])
print()
print("collected:")
sp.pprint(expr_c)

coeff_cos2x = expr_exp.coeff(sp.cos(2*x))
coeff_sin2x = expr_exp.coeff(sp.sin(2*x))
rest = sp.simplify(expr_exp - coeff_cos2x*sp.cos(2*x) - coeff_sin2x*sp.sin(2*x))
print("coeff cos2x:", sp.simplify(coeff_cos2x))
print("coeff sin2x:", sp.simplify(coeff_sin2x))
print("rest (should not involve x):", sp.simplify(rest))
