import sympy as sp
from sympy import symbols, expand, groebner, Rational
p,q = symbols('p q'); k1,k2,l1,l2 = symbols('k1 k2 l1 l2')
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dot(u,v): return u[0]*v[0]+u[1]*v[1]
A=(sp.Integer(0),sp.Integer(0)); B=(sp.Integer(1),sp.Integer(0)); C=(p,q)
M=(sp.Rational(1,2),sp.Integer(0)); N=(p/2,q/2); K=(k1,k2); L=(l1,l2)
def sub(P,Q): return (P[0]-Q[0],P[1]-Q[1])
u1=sub(K,B); v1=sub(A,B); u2=sub(A,C); v2=sub(L,C)
eq1 = expand(cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2))
u1=sub(L,B); v1=sub(K,B); u2=sub(L,N); v2=sub(C,N)
eq2 = expand(cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2))
u1=sub(L,C); v1=sub(K,C); u2=sub(B,M); v2=sub(K,M)
eq3 = expand(cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2))

num = -2*k1**3*l1*l2*q + 2*k1**3*l2**2*p - 2*k1**3*l2**2 + 2*k1**2*k2*l1**2*q - 2*k1**2*k2*l1*l2*p + 2*k1**2*k2*l1*l2 + 2*k1**2*l1**2*l2*q + 2*k1**2*l2**3*q - k1**2*l2**2*p**2 - k1**2*l2**2*q**2 + k1**2*l2**2 - 2*k1*k2**2*l1*l2*q + 2*k1*k2**2*l2**2*p - 2*k1*k2**2*l2**2 - 2*k1*k2*l1**3*q - 2*k1*k2*l1**2*l2*p + 2*k1*k2*l1**2*l2 - 2*k1*k2*l1*l2**2*q + 2*k1*k2*l1*l2*p**2 + 2*k1*k2*l1*l2*q**2 - 2*k1*k2*l1*l2 - 2*k1*k2*l2**3*p + 2*k1*k2*l2**3 + 2*k2**3*l1**2*q - 2*k2**3*l1*l2*p + 2*k2**3*l1*l2 + 2*k2**2*l1**3*p - 2*k2**2*l1**3 - k2**2*l1**2*p**2 - k2**2*l1**2*q**2 + k2**2*l1**2 + 2*k2**2*l1*l2**2*p - 2*k2**2*l1*l2**2

# Note: OM^2-ON^2 = num/(2*(k1*l2-k2*l1))? Let's just reduce num mod ideal.
print("computing groebner basis (may take a while)...")
import time
t=time.time()
G = groebner([eq1,eq2,eq3], k1,k2,l1,l2,p,q, order='lex')
print("groebner time", time.time()-t)
print("basis size", len(G))
# reduce num
r = G.reduce(num)
print("remainder:", sp.simplify(r[1]))
