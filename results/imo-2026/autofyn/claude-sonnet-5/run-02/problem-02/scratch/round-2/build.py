import sympy as sp

p,q,k1,k2,l1,l2 = sp.symbols('p q k1 k2 l1 l2', real=True)

B = sp.Matrix([0,0])
C = sp.Matrix([1,0])
A = sp.Matrix([p,q])
K = sp.Matrix([k1,k2])
L = sp.Matrix([l1,l2])
M = (A+B)/2
N = (A+C)/2

def cross(u,v):
    return u[0]*v[1]-u[1]*v[0]
def dot(u,v):
    return u[0]*v[0]+u[1]*v[1]

def dict_eq(u,v,w,z):
    return sp.expand(cross(u,v)*dot(w,z) - cross(w,z)*dot(u,v))

eq1 = dict_eq(K-B, A-B, A-C, L-C)
eq2 = dict_eq(L-B, K-B, L-N, C-N)
eq3 = dict_eq(L-C, K-C, B-M, K-M)

eq1p = sp.Poly(eq1, l2)
a1, a0 = eq1p.all_coeffs()
a1 = sp.expand(a1); a0 = sp.expand(a0)
D = sp.expand(-a1)
l2_num = sp.expand(a0)   # l2 = a0/D  since a1=-D -> eq1 = -D*l2+a0=0 -> l2=a0/D
print("D =", D)
check_direct = sp.simplify(eq1.subs(l2, l2_num/D))
print("direct l2 substitution check (should be 0):", check_direct)

# Substitute l2 into eq3, clear denominator D
eq3_sub = sp.together(eq3.subs(l2, l2_num/D))
num3, den3 = sp.fraction(eq3_sub)
num3 = sp.expand(num3)
print("den3 factors:", sp.factor(den3))
print("num3 degree in l1:", sp.Poly(num3, l1).degree())

# factor num3
fac = sp.factor(num3)
print("num3 factored:", fac)

X = fac.args[-1]  # last factor
X = sp.expand(X)
print("X =", X)

# eq2 substitution
eq2_sub = sp.together(eq2.subs(l2, l2_num/D))
num2, den2 = sp.fraction(eq2_sub)
num2 = sp.expand(num2)
print("den2 factor:", sp.factor(den2))
print("num2 degree in l1:", sp.Poly(num2, l1).degree())
print("num2 total degree in k1,k2:", sp.Poly(num2, k1,k2).total_degree())

# Circumcenter of A, K, L (with l2 substituted)
Ax,Ay = p,q
Kx,Ky = k1,k2
Lx,Ly = l1, l2_num/D

Dcirc = 2*(Ax*(Ky-Ly) + Kx*(Ly-Ay) + Lx*(Ay-Ky))
Ox_num = (Ax**2+Ay**2)*(Ky-Ly) + (Kx**2+Ky**2)*(Ly-Ay) + (Lx**2+Ly**2)*(Ay-Ky)

target = sp.together(Ox_num/Dcirc - (p/sp.Integer(2)+sp.Rational(1,4)))
Fn_num_raw, Fn_den_raw = sp.fraction(target)
Fn_num_raw = sp.expand(Fn_num_raw)
print("Fn_den_raw factor:", sp.factor(Fn_den_raw))
print("Fn_num_raw degree in l1:", sp.Poly(Fn_num_raw, l1).degree())

# Manual division of Fn_num_raw by eq2_num in l1, coefficients as rational functions
Pf = sp.Poly(Fn_num_raw, l1)
Pg = sp.Poly(num2, l1)
cf = Pf.all_coeffs()  # [a2,a1,a0] for Fn_num_raw
cg = Pg.all_coeffs()  # [b2,b1,b0] for eq2_num
print("Fn_num_raw coeffs (deg2..0) lens:", len(cf))
print("eq2_num coeffs (deg2..0) lens:", len(cg))

a2,a1_,a0_ = cf
b2,b1_,b0_ = cg
q0 = sp.cancel(a2/b2)
r1 = sp.cancel(a1_ - q0*b1_)
r0 = sp.cancel(a0_ - q0*b0_)
print("q0 =", q0)
print("r1 =", sp.factor(r1))
print("r0 =", sp.factor(r0))

D2 = sp.expand(-k1*q + k2*p - k2)
E1 = sp.expand(-2*k1*p*q + k1*q + k2*p**2 - k2*p - k2*q**2)
E0 = sp.expand(k1*p**2*q + k1*p*q - k1*q**3 - k1*q - k2*p**2 + 2*k2*p*q**2 + k2*p)
Llin = sp.expand(E1*l1+E0)

LHS = sp.expand(Fn_num_raw*D2 - (k2-q)*num2)
RHS = sp.expand(D*X*Llin)
print("Identity check (LHS-RHS, should be 0):", sp.expand(LHS-RHS))

# relation between Dcirc and D3
Dcirc_sub = sp.together(Dcirc.subs(l2, l2_num/D))
numDc, denDc = sp.fraction(Dcirc_sub)
print("Dcirc numerator (cleared by D):", sp.factor(numDc))
print("denDc:", denDc)

print("X irreducible over QQ(p,q)[k1,k2]?", sp.factor_list(X, k1, k2))
D2sym = sp.expand(-k1*q + k2*p - k2)
print("D linear check:", sp.Poly(D, k1, k2).total_degree())
print("D2 linear check:", sp.Poly(D2sym, k1, k2).total_degree())

# resultant of X and D w.r.t. k2 (eliminate k2), should be nonzero poly in k1,p,q
res_D = sp.resultant(sp.Poly(X, k2), sp.Poly(D, k2))
print("resultant(X,D,k2) == 0 ?", sp.expand(res_D) == 0)
res_D2 = sp.resultant(sp.Poly(X, k2), sp.Poly(D2sym, k2))
print("resultant(X,D2,k2) == 0 ?", sp.expand(res_D2) == 0)

# quick numeric sanity check with witness
subs_w = {p:sp.Rational(35,100), q:sp.Rational(9,10), k1:sp.Float(0.1790,20), k2:sp.Float(0.2390,20), l1:sp.Float(0.6848,20)}
print("eq1 at witness:", float(eq1.subs({**subs_w, l2: sp.Float(0.2514,20)})))
print("X at witness (k1,k2):", float(X.subs(subs_w)))
print("D at witness:", float(D.subs(subs_w)))
print("D2 at witness:", float(D2sym.subs(subs_w)))
