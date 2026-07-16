import sympy as sp
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
E2 = (k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b)
E3 = b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b)
# E2, E3 linear in kb -> solve each
kb2 = sp.solve(E2, kb)[0]   # kb as function of lb
kb3 = sp.solve(E3, kb)[0]
kb2 = sp.together(kb2); kb3 = sp.together(kb3)
# equation: kb2 - kb3 = 0 -> numerator quadratic in lb
diff = sp.together(kb2 - kb3)
num = sp.numer(diff)
num = sp.expand(num)
polylb = sp.Poly(num, lb)
print("degree in lb:", polylb.degree())
fact = sp.factor(num)
print("FACTORED numerator of (kb2-kb3):")
print(fact)
