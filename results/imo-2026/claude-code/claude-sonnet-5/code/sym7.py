import sympy as sp

s, theta, b, c, alpha0, k = sp.symbols('s theta b c alpha0 k', real=True)
co = c/k - s/sp.tan(theta)

cos_theta_x = sp.cos(theta)*co - sp.sin(theta)*s
sin_alpha_x = sp.sin(alpha0)*co - sp.cos(alpha0)*s
eq1 = -b*sp.sin(theta)**2 - 2*b*sp.sin(theta)*s*cos_theta_x - b*s**2 \
      + c*sp.sin(theta)*sp.sin(alpha0+theta) - c*s*sin_alpha_x
eq1_num = sp.numer(sp.together(eq1))
eq1_num = sp.expand(eq1_num * sp.tan(theta)**0)  # keep as is
eq1_poly = sp.Poly(sp.expand(eq1_num), s)
print("eq1 as poly in s, degree:", eq1_poly.degree())
print(eq1_poly)

eq3 = s**2+co**2-1
eq3_num = sp.numer(sp.together(eq3))
eq3_poly = sp.Poly(sp.expand(eq3_num), s)
print("eq3 as poly in s, degree:", eq3_poly.degree())
print(eq3_poly)

res = sp.resultant(eq1_poly.as_expr(), eq3_poly.as_expr(), s)
res = sp.simplify(res)
print("Resultant (eliminating s), should give polynomial relation in k:")
sp.pprint(res)
