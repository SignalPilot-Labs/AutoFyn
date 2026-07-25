import sympy as sp

u, cB, sB = sp.symbols('u cB sB')

x = (1-u**2)/(1+u**2)   # cos(A/3)
y = 2*u/(1+u**2)         # sin(A/3)

cosA = 4*x**3 - 3*x
sinA = 3*y - 4*y**3

# beta0 = pi/3 - A/3
cos_beta0 = sp.Rational(1,2)*x + sp.sqrt(3)/2*y
sin_beta0 = sp.sqrt(3)/2*x - sp.Rational(1,2)*y

sinAB = sinA*cB + cosA*sB   # sin(A+B)
X0 = sB*cosA / (2*sinAB)

# RHS = (1+cosB) cos(beta0) - sin(beta0)*G(beta0)
# G(beta0) = Kc - P sin(beta0) - Q cos(beta0)  [from file line 156 earlier: G(beta0)=Kc - P sin(beta0) - Q cos(beta0)]
sinA_sym, cosA_sym = sinA, cosA
Kc = 2*sinA_sym*sinAB
P = sp.Rational(1,2)*(sinA_sym*cB - cosA_sym*sB) + sp.Rational(3,2)*sinAB  # sin(A-B) = sinA cosB - cosA sinB
Q = -sinA_sym*sB

G_beta0 = Kc - P*sin_beta0 - Q*cos_beta0
RHS = (1+cB)*cos_beta0 - sin_beta0*G_beta0

target = (1+cB)**2*X0 - RHS**2

target_simplified = sp.together(target)
num, den = sp.fraction(target_simplified)
num = sp.expand(num)
den = sp.expand(den)
print("den factor:", sp.factor(den))

cosB_val = sp.Rational(808976,2721665)
sinB_val = sp.Rational(2598657,2721665)
print("check unit circle:", sp.simplify(cosB_val**2+sinB_val**2-1))

u_val = sp.Rational(1,4)

Num_val = num.subs({u:u_val, cB:cosB_val, sB:sinB_val})
Num_val = sp.nsimplify(Num_val)
print("Num sign:", sp.sign(Num_val), float(Num_val))

# n1 = cos^2(beta0) - X0, clear denominators similarly
expr_n1 = cos_beta0**2 - X0
expr_n1_t = sp.together(expr_n1)
n1_num, n1_den = sp.fraction(expr_n1_t)
n1_num = sp.expand(n1_num)
print("n1 den factor:", sp.factor(n1_den))

n1_val = n1_num.subs({u:u_val, cB:cosB_val, sB:sinB_val})
print("n1 numerator sign (raw, need denom sign too):", sp.sign(n1_val), float(n1_val))
n1_den_val = n1_den.subs({u:u_val, cB:cosB_val, sB:sinB_val})
print("n1 den sign:", sp.sign(n1_den_val), float(n1_den_val))

expr_n2 = X0 - cB**2
expr_n2_t = sp.together(expr_n2)
n2_num, n2_den = sp.fraction(expr_n2_t)
n2_num = sp.expand(n2_num)
print("n2 den factor:", sp.factor(n2_den))
n2_val = n2_num.subs({u:u_val, cB:cosB_val, sB:sinB_val})
n2_den_val = n2_den.subs({u:u_val, cB:cosB_val, sB:sinB_val})
print("n2 num sign:", sp.sign(n2_val), float(n2_val))
print("n2 den sign:", sp.sign(n2_den_val), float(n2_den_val))
