import sympy as sp

x, theta, b, c, alpha0 = sp.symbols('x theta b c alpha0', real=True)

expr = -b*sp.sin(theta)**2 - 2*b*sp.sin(theta)*sp.sin(x)*sp.cos(theta+x) - b*sp.sin(x)**2 \
       + c*sp.sin(theta)*sp.sin(alpha0+theta) - c*sp.sin(x)*sp.sin(alpha0-x)

expr2 = sp.expand_trig(expr)
expr2 = sp.simplify(expr2)
print("expr simplified:")
sp.pprint(expr2)

# Try rewriting in terms of cos(2theta), cos(2x), cos(2theta+2x) etc via product-to-sum
expr3 = sp.simplify(sp.expand(sp.trigsimp(expr, method='fu')))
print("fu-simplified:")
sp.pprint(expr3)
