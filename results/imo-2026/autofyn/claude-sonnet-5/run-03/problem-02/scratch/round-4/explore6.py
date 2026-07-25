import sympy as sp
import numpy as np

t1,s2,u,a,b,cc = sp.symbols('t1 s2 u a b cc', real=True)
sinb = 2*u/(1+u**2); cosb = (1-u**2)/(1+u**2)
A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M=(A+B)/2; N=(A+C)/2
Rbeta = sp.Matrix([[cosb,-sinb],[sinb,cosb]])
K = B + t1*sp.Matrix([-cosb,sinb])
L = C + s2*Rbeta*(A-C)

def dot(V1,V2): return sp.expand(V1.dot(V2))
BL=L-B; BK=K-B; NL=L-N; NC=C-N

def sq(V1,V2,V3,V4):
    lhs=(V1.dot(V2))**2*(V3.dot(V3))*(V4.dot(V4))
    rhs=(V3.dot(V4))**2*(V1.dot(V1))*(V2.dot(V2))
    return sp.expand(lhs-rhs)

eq2 = sq(BL,BK,NL,NC)
q2,_ = sp.div(eq2, t1**2, t1)
g2 = sp.factor(q2)
num, den = sp.fraction(g2)
mulargs = num.args if num.func==sp.Mul else [num]
polyfactors=[f for f in mulargs if f.is_Add]
print(len(polyfactors))
for f in polyfactors:
    print(sp.degree(sp.Poly(f, u)), sp.degree(sp.Poly(f,s2)))
G2a, G2b = polyfactors[0], polyfactors[1]
if sp.degree(sp.Poly(G2a,u))>sp.degree(sp.Poly(G2b,u)):
    G2a, G2b = G2b, G2a
print("G2a chosen (deg u, deg s2):", sp.degree(sp.Poly(G2a,u)), sp.degree(sp.Poly(G2a,s2)))

# BL.BK/t1 and NL.NC as linear functions of s2
BLBK_over_t1 = sp.expand(dot(BL,BK)/t1)
NLNC = sp.expand(dot(NL,NC))

# lambdify for numeric testing
f_G2a = sp.lambdify((s2,u,a,b,cc), G2a, 'numpy')
f_BLBK = sp.lambdify((s2,u,a,b,cc), BLBK_over_t1, 'numpy')
f_NLNC = sp.lambdify((s2,u,a,b,cc), NLNC, 'numpy')

import random
random.seed(1)
mismatches=0
tested=0
for trial in range(2000):
    av = random.uniform(0.3,3)
    bv = random.uniform(-2,2)
    ccv = random.uniform(0.2,3)
    uv = random.uniform(-3,3)
    # solve quadratic G2a(s2)=0 for s2
    s2sym = sp.symbols('s2sym', real=True)
    expr = G2a.subs({u:uv,a:av,b:bv,cc:ccv})
    poly = sp.Poly(expr, s2)
    coeffs = poly.all_coeffs()
    roots = np.roots([float(c) for c in coeffs])
    for r in roots:
        if abs(r.imag) > 1e-7: continue
        rv = r.real
        blbk = f_BLBK(rv,uv,av,bv,ccv)
        nlnc = f_NLNC(rv,uv,av,bv,ccv)
        tested+=1
        if blbk*nlnc < -1e-9:
            mismatches+=1
print("tested", tested, "mismatches (opposite sign) among ALL real roots of G2a:", mismatches)

print()
print("Restricting to s2>0:")
random.seed(2)
mismatches=0
tested=0
for trial in range(5000):
    av = random.uniform(0.3,3)
    bv = random.uniform(-2,2)
    ccv = random.uniform(0.2,3)
    uv = random.uniform(-3,3)
    expr = G2a.subs({u:uv,a:av,b:bv,cc:ccv})
    poly = sp.Poly(expr, s2)
    coeffs = poly.all_coeffs()
    roots = np.roots([float(c) for c in coeffs])
    for r in roots:
        if abs(r.imag) > 1e-7: continue
        rv = r.real
        if rv <= 1e-9: continue
        blbk = f_BLBK(rv,uv,av,bv,ccv)
        nlnc = f_NLNC(rv,uv,av,bv,ccv)
        tested+=1
        if blbk*nlnc < -1e-9:
            mismatches+=1
            if mismatches < 10:
                print("mismatch at", av,bv,ccv,uv,rv, blbk, nlnc)
print("tested(s2>0)", tested, "mismatches:", mismatches)
