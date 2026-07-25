import sympy as sp

c,s,d,t,sigma,tau = sp.symbols('c s d t sigma tau', real=True)

G0 = c*t*(1-2*d**2) - 2*s*d**3
f1 = -32*sigma**2*tau+24*sigma**2+22*sigma*tau-12*sigma-tau
f2 = -32*sigma**2*tau+8*sigma**2+38*sigma*tau-8*sigma-6*tau
Enum = c*t*f1.subs({sigma:s**2, tau:t**2}) + d*s*f2.subs({sigma:s**2, tau:t**2})
Num = c**5*t**3 - 3*c**3*d**2*s**2*t - c**3*s**2*t**3 + 2*c**2*d**3*s**3 - 6*c**2*d*s**3*t**2 - 9*c*d**2*s**4*t

def reduce_and_project00(expr):
    expr = sp.expand(expr)
    rem = sp.reduced(expr, [c**2+s**2-1, d**2+t**2-1], c,s,d,t)[1]
    rem = sp.expand(rem)
    f00 = sp.Rational(1,4)*(rem + rem.subs(c,-c) + rem.subs(d,-d) + rem.subs({c:-c,d:-d}))
    f00 = sp.expand(f00)
    f00 = f00.subs({s**8:sigma**4,s**6:sigma**3,s**4:sigma**2,s**2:sigma,
                     t**8:tau**4,t**6:tau**3,t**4:tau**2,t**2:tau})
    return sp.expand(f00)

B1 = reduce_and_project00(c*t*G0)
B2 = reduce_and_project00(s*d*G0)
B3 = reduce_and_project00(c*t*(-Enum))
B4 = reduce_and_project00(s*d*(-Enum))
B5 = reduce_and_project00(c*t*(-Num))
B6 = reduce_and_project00(s*d*(-Num))

claims = {
 'B1': tau*(1-sigma)*(2*tau-1),
 'B2': -2*sigma*(tau-1)**2,
 'B3': -tau*(sigma-1)*(32*sigma**2*tau-24*sigma**2-22*sigma*tau+12*sigma+tau),
 'B4': -2*sigma*(sigma-1)*(tau-1)*(16*sigma*tau-4*sigma-3*tau),
 'B5': tau*(sigma-1)*(8*sigma**2*tau-6*sigma**2-3*sigma+tau),
 'B6': 2*sigma**2*(sigma-1)*(tau-1)*(4*tau-1),
}
computed = dict(B1=B1,B2=B2,B3=B3,B4=B4,B5=B5,B6=B6)
for k in claims:
    diff = sp.expand(computed[k]-claims[k])
    print(k, "match" if diff==0 else f"MISMATCH: {diff}")
