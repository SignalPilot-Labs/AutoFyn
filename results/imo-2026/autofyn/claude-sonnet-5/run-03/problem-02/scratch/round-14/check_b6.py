import sympy as sp

c,s,d,t = sp.symbols('c s d t', real=True)

# definitions
G0 = c*t*(1-2*d**2) - 2*s*d**3

# Num as displayed (round13 authoritative)
Num = c**5*t**3 - 3*c**3*d**2*s**2*t - c**3*s**2*t**3 + 2*c**2*d**3*s**3 - 6*c**2*d*s**3*t**2 - 9*c*d**2*s**4*t

expr = sp.expand(s*d*(-Num))

# reduce mod c^2+s^2-1, d^2+t^2-1: repeatedly substitute c^2 -> 1-s^2, d^2->1-t^2
def reduce_mod(e):
    e = sp.expand(e)
    changed = True
    while changed:
        changed = False
        e2 = sp.expand(e.subs(c**2, 1-s**2))
        e2 = sp.expand(e2.subs(d**2, 1-t**2))
        if e2 != e:
            e = e2
            changed = True
    return e

# Better: use sympy's polynomial reduction (division) properly
c2s2 = c**2+s**2-1
d2t2 = d**2+t**2-1

# Use groebner-based reduction
from sympy import groebner, reduced
G = groebner([c2s2, d2t2], c,s,d,t, order='lex')
rem = sp.reduced(expr, [c2s2, d2t2], c,s,d,t)[1]
rem = sp.expand(rem)
print("degree check rem vars:", rem.free_symbols)

# parity projector for (0,0) part: average over c->-c and d->-d
f00 = sp.Rational(1,4)*(rem + rem.subs(c,-c) + rem.subs(d,-d) + rem.subs({c:-c,d:-d}))
f00 = sp.expand(f00)
print("f00 (should be function of c^2,s,d^2,t only, i.e. sigma=s^2? wait s,t appear too)")
print(f00)

sigma, tau = sp.symbols('sigma tau')
f00_st = f00.subs({s**6: sigma**3, s**4: sigma**2, t**4: tau**2, t**2: tau})
f00_st = sp.expand(f00_st)
print("in sigma,tau:", f00_st)
print("factor:", sp.factor(f00_st))

claimed = 2*sigma**2*(sigma-1)*(tau-1)*(4*tau-1)
print("diff:", sp.expand(f00_st - claimed))
