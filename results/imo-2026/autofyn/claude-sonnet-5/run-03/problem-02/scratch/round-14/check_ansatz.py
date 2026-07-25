import sympy as sp

sigma, tau = sp.symbols('sigma tau')

q1 = 512*sigma**4*tau**2-512*sigma**4*tau+96*sigma**4-928*sigma**3*tau**2+856*sigma**3*tau-144*sigma**3+506*sigma**2*tau**2-392*sigma**2*tau+48*sigma**2-85*sigma*tau**2+40*sigma*tau+3*tau**2

B1 = tau*(1-sigma)*(2*tau-1)
B4 = -2*sigma*(sigma-1)*(tau-1)*(16*sigma*tau-4*sigma-3*tau)
B6 = 2*sigma**2*(sigma-1)*(tau-1)*(4*tau-1)

lam = sp.symbols('l1_3 l1_2t l1_t2 l1_t3 l4_s l4_t l6_s l6_t')
l1_3,l1_2t,l1_t2,l1_t3,l4_s,l4_t,l6_s,l6_t = lam

mult1 = l1_3*sigma**3 + l1_2t*sigma**2*tau + l1_t2*sigma*tau**2 + l1_t3*tau**3
mult4 = l4_s*sigma + l4_t*tau
mult6 = l6_s*sigma + l6_t*tau

combo = sp.expand(mult1*B1 + mult4*B4 + mult6*B6)
target = sp.expand(-q1)

diff = sp.expand(combo - target)
poly = sp.Poly(diff, sigma, tau)
eqs = poly.coeffs()
sol = sp.linsolve(eqs, lam)
print(sol)
