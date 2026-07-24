import sympy

p = 13
K0max = 25
qmin = 17  # least admissible prime > p, excluding p itself... primes q>13

def check_ineq(s):
    lhs = sympy.factorial(s+1)
    rhs = K0max + sympy.Rational(p, qmin) * 2**(s+1) * (s+2)
    return lhs, rhs, lhs >= rhs

for s in range(1, 12):
    lhs, rhs, ok = check_ineq(s)
    print(s, lhs, float(rhs), ok)
