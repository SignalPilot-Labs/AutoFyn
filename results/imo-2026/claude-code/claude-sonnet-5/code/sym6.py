import sympy as sp

s, co, theta, b, c, alpha0, k = sp.symbols('s co theta b c alpha0 k', real=True)

# equation (1): concyclicity condition, in terms of s=sin x, co=cos x
cos_theta_x = sp.cos(theta)*co - sp.sin(theta)*s   # cos(theta+x)
sin_alpha_x = sp.sin(alpha0)*co - sp.cos(alpha0)*s  # sin(alpha0 - x)

eq1 = -b*sp.sin(theta)**2 - 2*b*sp.sin(theta)*s*cos_theta_x - b*s**2 \
      + c*sp.sin(theta)*sp.sin(alpha0+theta) - c*s*sin_alpha_x
eq1 = sp.expand(eq1)
print("eq1 (poly in s,co):")
sp.pprint(eq1)

# equation (2): k*sin(x+theta) = c*sin(theta)  =>  k*(s*cos(theta)+co*sin(theta)) - c*sin(theta) = 0
eq2 = k*(s*sp.cos(theta) + co*sp.sin(theta)) - c*sp.sin(theta)
print("eq2:")
sp.pprint(eq2)

# pythagorean
eq3 = s**2+co**2-1

# Solve eq2 for co in terms of s,k (linear in co):
co_sol = sp.solve(eq2, co)[0]
print("co in terms of s:", co_sol)

eq1_sub = sp.simplify(eq1.subs(co, co_sol))
eq3_sub = sp.simplify(eq3.subs(co, co_sol))

print("eq1 after substitution (should be polynomial in s):")
eq1_sub_poly = sp.together(eq1_sub)
sp.pprint(eq1_sub_poly)
print("eq3 after substitution:")
sp.pprint(sp.together(eq3_sub))
