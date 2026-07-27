import sympy as sp
mu,beta,Bs,Cs=sp.symbols('mu beta B C',positive=True)
As=sp.pi-Bs-Cs
xi=As+beta-mu
# (star):  2 sinC sinmu cos(beta+mu) sin(A+beta) - sinA sin(beta+mu) sin(C-beta-mu)
star = 2*sp.sin(Cs)*sp.sin(mu)*sp.cos(beta+mu)*sp.sin(As+beta) - sp.sin(As)*sp.sin(beta+mu)*sp.sin(Cs-beta-mu)
# (spade): sinC[ sin(xi) sin(beta-mu) + 2 sinmu sinbeta cos(xi) ] - sinB sin^2(beta+mu)
spade = sp.sin(Cs)*( sp.sin(xi)*sp.sin(beta-mu) + 2*sp.sin(mu)*sp.sin(beta)*sp.cos(xi) ) - sp.sin(Bs)*sp.sin(beta+mu)**2
diff = sp.simplify(sp.expand_trig(star - spade))
print("star - spade simplified =", diff)
ratio = sp.simplify(sp.expand_trig(spade)/sp.expand_trig(star))
print("spade/star =", ratio)
